# CCBT · Stress Program — Module Explorer

Self-contained React prototypes for ComPsych's **Sunrise** design system, exploring CCBT stress
modules and lightweight "in-between care" activities. Every module is built in two presentation
looks — **Utility** (the Material Sunrise card flow) and **Immersion** (a full-screen "papercut"
world) — and the shell lets you switch between them seamlessly, preserving each module's state.

## Run locally

No build step — these are plain HTML files with React + Babel loaded from a CDN. Serve the folder
with any static server, e.g.:

```bash
npx serve .
# or
python3 -m http.server 4180
```

Then open **`index.html`** (the Module Explorer shell). Pick a module from the tier-grouped dropdown
and toggle **Utility / Immersion**; **‹ Prev / Next ›** in the top bar steps the active module.

## Modules (by tier)

**Tier 1**
- `concept-2.html` / `solving-the-problem-immersion.html` — Solving the Problem
- `in-the-moment-reset.html` / `in-the-moment-reset-3.html` — In-the-Moment Reset (paced breathing)
- `grounding-utility.html` / `grounding-immersion.html` — Grounding (5-4-3-2-1)
- `screener-utility.html` / `screener-immersion.html` — Find Support (needs screener + router)
- `pulse-utility.html` / `pulse-immersion.html` — Check-in (weekly stress pulse)

**Tier 2**
- `psychoed-utility.html` / `psychoed-immersion.html` — Know Your Stress (interactive explainer)
- `reflect-utility.html` / `reflect-immersion.html` — Reflect (reflective prompt)

`index.html` is the shell that hosts them all. Add a module by editing the `MODULES` config there
(set `tier` to auto-group it in the dropdown).

## Notes for contributors

- Each module is a **single self-contained file**: inline Material Sunrise tokens + components,
  React 18 UMD + `@babel/standalone`, JSX in a `<script type="text/jsx-source">` block.
- Shell ↔ module state transfer uses `postMessage` (`reset:getState` / `reset:setState`, plus
  `reset:next` / `reset:prev` for the shell's step nav).
- Any reference imagery used during design was **licensed for inspiration only** — all visual assets
  here are authored from scratch (no traced paths, no stock assets). Keep it that way.
