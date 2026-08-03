# CCBT "In-Between Care" Stress Modules — Source Package

Interactive React prototypes for ComPsych's CCBT stress **in-between care** program:
short, self-contained wellbeing activities sent to members between counseling touchpoints.
Built on **Material Sunrise** (ComPsych's in-house design system, based on Material Design 3).

## How it's built (read this first)
- Each module is a **single self-contained HTML file**: React 18 (UMD) + Babel-in-browser.
  The JSX lives in a `<script type="text/jsx-source" id="app-src">` block near the bottom of
  each file — **that's where the screens, steps, and copy are.** Everything above it is inlined
  Sunrise design tokens + CSS (safe to skim past).
- Every module ships in **two "looks"** that share the same step model and data:
  - **Utility** — a clean white-card DS flow (Content Section Template + progress tracker).
  - **Immersion** — a full-screen calming "papercut" treatment (`BreathBackground`), same steps.
- `index.html` is the **explorer shell**: a tier-grouped module dropdown + a Utility/Immersion
  toggle. It hosts each module in an iframe and supports **seamless switching** between the two
  looks mid-flow via a `postMessage` state bridge (step index + user inputs transfer across).
- `tokens.css` mirrors the Sunrise design tokens used inline across all files.
- `spec/` holds the two clinical source documents the module set was derived from — useful for
  justifying the rotation logic and each module's clinical intent in a run-of-show.

## The screen flow, in short
Most modules follow: **Intro (Start) → Learn → the activity step(s) → Done (recap)**.
The activity step is where the member interacts (write fields, selection cards, sliders, etc.).

## Module map
Tier 1 = core stress rotation; Tier 2 = supporting content. `id` matches the shell config in `index.html`.

| Module (name) | id | Tier | Clinical intent | Utility file | Immersion file |
|---|---|---|---|---|---|
| Solving the Problem | solving | 1 | Structured problem-solving: name a stressor → brainstorm options → pick a next step | `concept-2.html` | `solving-the-problem-immersion.html` |
| In-the-Moment Reset | reset | 1 | Guided breathing / grounding reset for an acute stress spike | `in-the-moment-reset.html` | `in-the-moment-reset-3.html` |
| Grounding | grounding | 1 | 5-4-3-2-1 five-senses grounding walk | `grounding-utility.html` | `grounding-immersion.html` |
| Self-Compassion Break | selfcompassion | 1 | Neff self-compassion: notice what's hard → "you're not alone" → offer a kind word | `selfcompassion-utility.html` | `selfcompassion-immersion.html` |
| Support Map | support | 1 | Map your circle (practical / someone to talk to / who lifts you) → choose one person to reach out to | `support-utility.html` | `support-immersion.html` |
| Three Good Things | gratitude | 1 | Positive-psychology gratitude: name three good things, one per step, with a between-step "moment of delight" | `gratitude-utility.html` | `gratitude-immersion.html` |
| Did You Know | benefits | 1 | Resource-awareness browse of EAP/CCBT benefits, ending in clickable resource cards | `didyouknow-utility.html` | `didyouknow-immersion.html` |
| Find Support | screener | 1 | Light needs-screener that routes to the matching resource | `screener-utility.html` | `screener-immersion.html` |
| Check-in | pulse | 1 | Weekly 1–5 stress pulse-check with a tiered response | `pulse-utility.html` | `pulse-immersion.html` |
| Know Your Stress | psychoed | 2 | Interactive stress-response "wave" explainer (psychoeducation) | `psychoed-utility.html` | `psychoed-immersion.html` |
| Reflect | reflect | 2 | Reflective prompt (reframe / lift / boundary) + a guided write | `reflect-utility.html` | `reflect-immersion.html` |

## To run locally
Static files, no build step. From this folder: `python3 serve.py` (or any static server), then open
`index.html`. The public hosted version of this same explorer is on Vercel.

## Where to look for a run-of-show
- Screen names, step labels, and on-screen copy: the `STEPS`/`SC_STEPS`/`SENSES`/`RESOURCES`
  arrays and the `*Controls` / screen components inside each file's `app-src` script block.
- The demo's headline feature is **seamless Utility ↔ Immersion switching** (see `index.html`).
- `spec/` explains *why* each module exists and how they rotate week to week.
