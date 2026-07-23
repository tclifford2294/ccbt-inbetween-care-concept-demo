#!/usr/bin/env python3
"""Static file server with caching disabled, for live prototype preview.

Plain `python -m http.server` sends Last-Modified/ETag headers, so browsers
(and the preview panel) keep serving stale files after edits. This handler
forces every response to be uncached so a normal reload always shows the
latest version — no hard-refresh or ?v= cache-busting needed.

It listens on an IPv6 dual-stack socket ("::") so `localhost` works whether the
browser resolves it to 127.0.0.1 (IPv4) or ::1 (IPv6). Binding IPv4-only made
Safari hang trying the IPv6 address first. HTTP/1.1 keep-alive is enabled so
pages load over a single connection instead of one per file.
"""
import os
import socket
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

# Serve from this script's own directory, regardless of where it's launched from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class NoCacheHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # keep-alive → faster multi-asset loads

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_header(self, keyword, value):
        # Drop conditional-cache headers so the browser never serves a 304 stale copy.
        if keyword.lower() in ("last-modified", "etag"):
            return
        super().send_header(keyword, value)


class DualStackServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6

    def server_bind(self):
        # Accept both IPv4 (127.0.0.1) and IPv6 (::1) on the same socket.
        try:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        except (AttributeError, OSError):
            pass
        super().server_bind()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4180
    server = DualStackServer(("::", port), NoCacheHandler)
    print(f"Serving {os.getcwd()} on http://localhost:{port}/ (no-cache, dual-stack)")
    server.serve_forever()
