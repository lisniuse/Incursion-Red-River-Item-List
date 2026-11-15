---
name: Incursion Red River Item List
description: A near-black armorer's terminal where every weapon build is read as a schematic and copied as a console command.
colors:
  phosphor-green: "#39ff88"
  accent-hover: "#63ffa3"
  phosphor-wash: "rgba(57, 255, 136, 0.11)"
  signal-cyan: "#72d6ff"
  measure-amber: "#ffca6b"
  void-black: "#030504"
  panel-black: "#050a07"
  phosphor-ink: "#d7ffe2"
  muted-sage: "#9dc4ab"
  dim-sage: "#7fa68c"
  command-ink: "#c3ebd0"
  hairline: "rgba(126, 226, 162, 0.16)"
  hairline-strong: "rgba(126, 226, 162, 0.3)"
  on-accent: "#02110a"
typography:
  display:
    fontFamily: "Segoe UI Variable Display, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(36px, 5vw, 64px)"
    fontWeight: 650
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Segoe UI Variable Display, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(26px, 2.3vw, 38px)"
    fontWeight: 650
    lineHeight: 1.02
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Segoe UI Variable Display, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(20px, 2vw, 27px)"
    fontWeight: 650
    lineHeight: 1.1
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Segoe UI Variable Display, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  control:
    fontFamily: "Segoe UI Variable Display, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: normal
    letterSpacing: "0.01em"
  label:
    fontFamily: "ui-monospace, Cascadia Mono, SFMono-Regular, Consolas, monospace"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: normal
    letterSpacing: "0.12em"
  measure:
    fontFamily: "ui-monospace, Cascadia Mono, SFMono-Regular, Consolas, monospace"
    fontSize: "44px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.035em"
    fontFeature: "tnum"
  data:
    fontFamily: "ui-monospace, Cascadia Mono, SFMono-Regular, Consolas, monospace"
    fontSize: "11.5px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
rounded:
  micro: "3px"
  chip: "4px"
  control: "7px"
  block: "8px"
  stage: "10px"
  card: "12px"
  pill: "99px"
spacing:
  2xs: "4px"
  xs: "8px"
  sm: "12px"
  md: "14px"
  lg: "18px"
  xl: "22px"
  2xl: "26px"
  3xl: "54px"
components:
  button-primary:
    backgroundColor: "{colors.phosphor-green}"
    textColor: "{colors.on-accent}"
    typography: "{typography.control}"
    rounded: "{rounded.block}"
    padding: "0 12px"
    height: "36px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
  button-ghost:
    backgroundColor: "rgba(57, 255, 136, 0.06)"
    textColor: "{colors.phosphor-ink}"
    typography: "{typography.control}"
    rounded: "{rounded.block}"
    padding: "0 12px"
    height: "36px"
  nav-link:
    textColor: "{colors.muted-sage}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "34px"
  nav-link-active:
    backgroundColor: "{colors.phosphor-wash}"
    textColor: "{colors.phosphor-ink}"
  input-search:
    backgroundColor: "rgba(0, 0, 0, 0.28)"
    textColor: "{colors.phosphor-ink}"
    rounded: "{rounded.block}"
    padding: "0 34px 0 31px"
    height: "36px"
  rail-item-active:
    backgroundColor: "{colors.phosphor-wash}"
    textColor: "{colors.phosphor-ink}"
    padding: "7px 14px"
    width: "100%"
  schematic-slot:
    backgroundColor: "rgba(4, 8, 6, 0.86)"
    textColor: "{colors.phosphor-ink}"
    rounded: "{rounded.block}"
    padding: "7px 9px"
    width: "100%"
  schematic-slot-selected:
    backgroundColor: "rgba(57, 255, 136, 0.1)"
    textColor: "{colors.phosphor-ink}"
  stat-reading:
    textColor: "{colors.measure-amber}"
    typography: "{typography.measure}"
  badge:
    textColor: "{colors.muted-sage}"
    typography: "{typography.label}"
    rounded: "{rounded.chip}"
    padding: "0 7px"
    height: "22px"
  path-card:
    backgroundColor: "rgba(5, 10, 7, 0.58)"
    textColor: "{colors.phosphor-ink}"
    rounded: "{rounded.card}"
    padding: "22px"
  command-block:
    backgroundColor: "rgba(0, 0, 0, 0.3)"
    textColor: "{colors.command-ink}"
    rounded: "{rounded.block}"
    padding: "9px 10px"
---

# Design System: Incursion Red River Item List

## Overview

**Creative North Star: "The Armorer's Terminal"**

The site is an instrument on a dark workbench, not a game UI. Its primary surface is a three-lane bench: a weapon rail on the left, a dot-grid stage in the center where a line-drawn weapon sits inside a tree of hairline traces, and a readout lane on the right that ends in the command the player copies. The hub is the same instrument seen from the door: one display headline, one line schematic, and two branch cards into the bench and the terminal. Everything is near-black, green-tinted, and dense, but the density is ordered — rail, stage, readout — so the loadout can be read before a single line of the command.

The palette assigns jobs instead of decorating. Phosphor green is the machine (structure, selection, action); cyan is every identifier the player must trust or copy exactly; amber is every measurement. Names and prose are set in the OS's own sans because the site may never fetch a font; every ID, field label, and number is monospace. The result is a dual voice — human names, machine data — that stays legible in two languages without translating a single item ID.

The world's refusals are confirmed by both the direction contract and the build: no glass or backdrop blur, no outer glow, no gradient text, no game renders or icon illustrations standing in for the schematic. Depth is tonal and linear, never cast. The loudest element on the bench is the measurement readout; the only large green fill is the copy button. Those two signals never multiply: one reading and one copy action per view.

**Key Characteristics:**
- Near-black green-tinted ground (`#030504`), one panel step lighter (`#050a07`), hairline structure
- Green system signal, cyan identifiers, amber measurements — no fourth accent
- System sans for names and prose; monospace for every ID, label, and measurement
- Three-lane bench on desktop, stacked bench plus fixed copy bar on narrow screens
- Dot-grid schematic stage with 1px curved branch traces and compact slot nodes
- Compact corners (3–12px), flat-by-default surfaces, a single 58px topbar offset

## Colors

A one-hue environment: near-black ground, phosphor-green signal, with cyan and amber used as narrowly scoped data channels.

### Primary
- **Phosphor Green** (`#39ff88`): the machine signal. Active tab underlines, selected borders and dots, schematic traces, the primary copy button, the skip link, and text selection. Its wash (`rgba(57, 255, 136, 0.11)`) is the canonical selected fill; hovers and lighter tints stay between 4.5% and 6%.
- **Accent Hover** (`#63ffa3`): the lighter fill the primary copy button takes on hover, never used as static text or a border.
- **On-Accent** (`#02110a`): the ink that sits on green — primary button text, skip link, selected text. Green is never used as text on a green fill.

### Secondary
- **Signal Cyan** (`#72d6ff`): identifiers and interactive chrome. Item IDs everywhere, links, the `KIT` rail tag, the search field's focus border, and the global 2px focus outline. Cyan marks what must be reproduced exactly; it never carries an action by itself.

### Tertiary
- **Measure Amber** (`#ffca6b`): measurements only. The 44px stat pair, the amber stat echo beside rail names, the `×2` duplicate count on a slot, and the receiver warning when a command contains no weapon item.

### Neutral
- **Void Black** (`#030504`): the page ground, the rail and readout backgrounds, and the topbar. This is the only page background; there is no light theme.
- **Panel Black** (`#050a07`): the one tonal lift, used for meta-grid cells and small panel fills — roughly 1% lightness above the ground, not a second surface system.
- **Phosphor Ink** (`#d7ffe2`): body and heading text, slot names, selected state text.
- **Muted Sage** (`#9dc4ab`): secondary text, labels, inactive controls. Measured at 10.6:1 on the ground and 10.4:1 on panel black.
- **Dim Sage** (`#7fa68c`): tertiary text, placeholders, the `/` divider in the stat pair, the stage caption. Still 7.4:1 on panel black.
- **Command Ink** (`#c3ebd0`): the command preview text only — a slightly desaturated green that keeps a long copied string calmer than body ink.
- **Hairline** (`rgba(126, 226, 162, 0.16)`): every structural divider, panel border, and group separator.
- **Hairline Strong** (`rgba(126, 226, 162, 0.3)`): boundaries of interactive things — inputs, buttons, segmented controls, badges, the language switch.

**The Three-Signal Rule.** Green is the system and the action, cyan is an identifier, amber is a measurement. No screen adds a fourth accent hue, and no value swaps channels: a stat never turns green, an ID never turns amber, a selected border never turns cyan.

**The Near-Black Ground Rule.** Ground and panel stay within one step of each other (`#030504` to `#050a07`), and tinted washes never exceed 11% alpha. A full green surface fill is reserved for the primary copy button, the skip link, and text selection; everything else signals with 1px lines and washes.

## Typography

**Display Font:** Segoe UI Variable Display (with Segoe UI, system-ui, -apple-system)
**Body Font:** same system sans stack
**Label/Mono Font:** ui-monospace (with Cascadia Mono, SFMono-Regular, Consolas)

**Character:** Two voices, one bench. The sans is the OS speaking — names, headings, guidance — chosen because the site is single-file, offline, and may not fetch a font. The monospace is the machine speaking — IDs, field labels, counts, measurements, commands — and it carries the terminal identity that a display face would otherwise have to supply. The identity comes from the split and from tracking, not from a novelty typeface.

### Hierarchy
- **Display** (650, `clamp(36px, 5vw, 64px)`, 0.98, -0.04em): the hub headline only, capped at 13ch and balanced. In Chinese it relaxes to `clamp(32px, 4.2vw, 52px)`, line-height 1.08, -0.02em, max 17ch.
- **Headline** (650, `clamp(26px, 2.3vw, 38px)`, 1.02, -0.025em): the selected build name on the bench; fixed at 28px below 640px.
- **Title** (650, `clamp(20px, 2vw, 27px)`, 1.1, -0.025em): hub branch-card titles. Names inside panels (slot nodes, part rows) sit at 12–13px/600 and are not this step.
- **Body** (400, 14px, 1.5): the base. Hub intro copy is 15px/1.6 and capped at 56ch; card copy is 12.5px/1.55 at 44ch; the bench foot note is 12px mono at 62ch.
- **Control** (600, 12px sans, 0.01em): buttons, top nav, copy-bar labels, rail toggle. Rail item names are 13px/600; the selected part name is 13px/600.
- **Label** (400, 11px mono, 0.08–0.16em uppercase): field keys on slot nodes, readout and part-list headings, rail group titles, meta terms, the `STATIC / OFFLINE` status, and the stage caption.
- **Measure** (600, 44px/1 mono, -0.035em, tabular numerals): the stat pair, dropping to 38px at 1120px and below. The slash divider is 26px/400 in dim sage.
- **Data** (400, 11.5px/1.55 mono): the command preview. Item IDs in part rows and the selected card are 11px mono in cyan at 82–100% strength.

**The Mono-Means-Data Rule.** Anything copied, typed, measured, or identified is monospace with tabular numerals; names and prose are sans. Setting a weapon name in mono is a category error, and setting an item ID in sans is an offence against copyability.

**The Uppercase-Is-A-Label Rule.** Uppercase plus 0.08–0.16em tracking belongs to 11px mono field and section labels only. Display headlines and weapon names stay sentence case, in both languages.

**The Bilingual Tracking Rule.** Switching to Chinese relaxes display tracking (-0.04em to -0.02em), opens its line-height (0.98 to 1.08), and shrinks its clamp; mono labels keep Latin tracking. Section names and UI strings translate — weapon names and item IDs never do.

## Layout

The bench is a three-lane grid: rail `264px`, a fluid stage, readout `350px`, inside a `1720px` maximum with 1px hairline rules at the outer edges. At 1320px the lanes tighten to `240px` / fluid / `322px`; at 1120px the grid collapses to a single column. The topbar is a 58px constant — the rail and readout are sticky at `top: 58px` with `height: calc(100dvh - 58px)`, and the rail's group titles stick inside that. The bench column pads 20px/22px; the readout pads 18px/16px with 14px between blocks; the rail head is 12px and rail items 7px/14px.

The stage is the composition's center: height `clamp(480px, 62vh, 640px)`, 14px below the bench head, 1px hairline, 10px radius, and a 24px dot grid drawn at 14% green under an elliptical mask that fades it out around the weapon. Slot nodes form three banks — 174px columns left and right, a centered bottom row inset 190px — with curved 1px traces meeting anchor dots on the silhouette. At 1320px the columns narrow to 160px and the bottom row insets to 176px.

The readout runs top to bottom as stat pair, meta grid, selected part (only when a part is picked), parts list (capped at `min(30vh, 250px)`), and command. The command is never more than one action away: it is the last block of the right lane on desktop, and at 1120px and below it becomes a fixed bottom copy bar with the build name and part/stat summary, above `env(safe-area-inset-bottom)`. Below 1120px the stage stops being absolute: the rig centers at 78% width (52% for pistols), the traces are hidden, and the slot banks become `auto-fit` grids with 148px minimums; the readout turns static and reserves 88px at the bottom for the copy bar.

The hub is a separate, calmer composition: `1180px` maximum, 54px top padding, a two-column hero (1.05fr / 0.95fr, 34px gap) with the schematic on the right, then two branch cards (1.35fr / 0.65fr, 18px gap, 22px padding). At 900px the hero stacks with the schematic first and the cards become one column; at 640px the gutters drop to 16px and headings to 38px.

Density is rhythmic rather than modular: 4px inside icon groups, 8px between tight controls, 12px inside controls and rail heads, 14px between list rows and mobile gutters, 18px page gutters and block gaps, 22px bench and card padding, 26px hub gutter, 54px hub top. Optical 7px/9px/10px/11px values inside controls are deliberate, not rounding errors.

**The Three-Lane Rule.** A wide bench has exactly rail, stage, readout. The center lane is reserved for the schematic — no data table, no second list, no marketing block displaces the weapon.

**The One-Click-Away Rule.** The full command is always rendered or fixed on screen: last block of the readout on desktop, a fixed copy bar on narrow screens. Never bury the copy action behind a tab or an overflow menu.

**The 58px Constant Rule.** The topbar is 58px tall and every sticky offset derives from it. A new sticky surface uses the same constant rather than inventing a second header height.

## Elevation & Depth

The system is flat by default. Panels and cards cast no shadows; depth comes from a one-step tonal lift (`#050a07`), 1px hairline separators, and a single radial vignette on the stage (`transparent 42%` to `rgba(0,0,0,0.42)` at the edges) that pushes the schematic forward. The stage and dot grid are isolated in their own stacking context but use no blur or glass. The only cast shadow in the product is the toast's ambient lift; the only other shadow-like effects are a 2px inset underline on active tabs and a 1px cyan ring on a focused search field.

### Shadow Vocabulary
- **Active underline** (`box-shadow: inset 0 -2px 0 #39ff88`): pressed top-nav links and segmented-control options; the 2px mark is what distinguishes "current" from "hovered".
- **Focus ring** (`box-shadow: 0 0 0 1px rgba(114, 214, 255, 0.35)`): the search input's focus, paired with a cyan border. All other focus uses the 2px cyan outline.
- **Toast lift** (`box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45)`): the transient copy-confirmation toast only.

**The Flat-By-Default Rule.** Cards, rails, readouts, and the stage are flat at rest. If a new surface needs to separate, lift the tone by one step or draw a hairline — do not add a drop shadow.

**The No-Glow Rule.** Selection and focus are a 1px border, a wash of 11% or less, and a 2px cyan outline. Outer glows, halo shadows, and backdrop blur are refused.

## Shapes

The form language is compact and drafted. Corners are small and tightly tiered: 3px on the `KIT` micro tag, 4px on badges and the focus radius, 7px on top-nav links and the language switch, 8px on every control and panel (buttons, inputs, slot nodes, kit cards, command block, meta grid, toast), 10px on the stage only, 12px on hub branch cards, and 99px on scrollbar thumbs only. Icon buttons take 5px and the skip link 6px as local exceptions.

Borders are 1px and green-tinted; structure is drawn, not extruded. Schematic strokes are the authored exception: 1.6px for the weapon outline, 2.2px for the emphasized detail, 1px for traces, 1.6px when a trace is active. Circles are used as instruments — a 26px brand ring with crosshair ticks, 2.4px anchor dots, and a 6px status dot; the rail's current marker is the square exception at 4px. No panel is clipped with clip-path; the only mask is the dot grid's elliptical fade.

**The Compact-Corner Rule.** Controls stop at 7–8px, the stage at 10px, hub cards at 12px. Pills belong to scrollbar thumbs and nothing else; no rounded-full buttons, inputs, or tags.

**The 1px Structure Rule.** Every structural edge starts as a 1px hairline at 16% green. Interactive borders start at 30% and may escalate to full green on hover or selection; panels are never framed at 2px. The only 2px rules are the active-tab underline and the focus outline.

## Components

### Buttons
- **Shape:** 8px radius, 36px minimum height, 0 12px padding, 7px icon gap.
- **Primary:** solid phosphor green (`#39ff88`) with on-accent ink (`#02110a`), 600 12px sans, 15px inline SVG icon. This is the copy command action and the only large green fill in the UI. Hover to accent-hover (`#63ffa3`) on both fill and border; active translates down 1px.
- **Ghost / Secondary:** 6% green wash with a 30% hairline border and ink text. Hover raises to a 12% wash and a 52% green border. Small variant is 32px tall with 0 9px padding.
- **Icon buttons:** 24px square, 5px radius, muted icon, hover border-strong plus a dark wash; 32px copy columns in part rows carry no fill, a hairline left divider, and a 13px icon that turns green on hover.
- **Focus:** global 2px cyan outline at 2px offset (4px radius), never removed.

### Cards / Containers
- **Corner style:** 8px for in-panel blocks, 12px for hub branch cards.
- **Readout blocks:** no box — a hairline bottom border and 15px of padding separate sections.
- **Meta grid:** three equal cells with 1px hairline gaps, panel-black cells, 8px outer radius; terms are 11px mono uppercase, values 600 14px mono with tabular numerals.
- **Parts list:** 8px, hairline border, rows separated by hairlines, scroll capped at `min(30vh, 250px)`.
- **Selected part:** 8px, 34% green border, 4.5% green wash, mono green slot key, cyan ID, 13px name, and two actions (copy item, clear).
- **Hub branch cards:** 12px, hairline, `rgba(5,10,7,0.58)` for the main card and `rgba(3,6,4,0.4)` for the side card, 22px padding, 220px minimum height on the main. Hover shifts the border to 46% green, the fill to 5.5%, and slides the arrow 3px.
- **Shadow strategy:** none; see Elevation & Depth.

### Inputs / Fields
- **Style:** the search field is the only input — 36px tall, 8px radius, `rgba(0,0,0,0.28)` fill, 30% hairline border, 12px mono ink, a 14px left search icon, and a `/` key hint on the right.
- **Focus:** cyan border plus a 1px cyan ring; the caret and text stay ink.
- **States:** placeholder is dim sage at full opacity; no error or disabled input exists, so none is specified.

### Navigation
- **Topbar:** 58px, ground background, hairline bottom, 18px gutters, brand mark 26px, brand name 14px/600 sans over an 11px mono uppercase subtitle at 0.16em.
- **Links:** 34px tall, 7px radius, 600 12px sans in muted sage; hover is a 6% wash and ink text; current is an 11% wash, ink text, and a 2px green inset underline.
- **Language switch:** a 7px segmented control with a 30% border; 11px mono buttons at 5px/8px padding; the active language takes the 11% wash and ink text but no underline.
- **Status:** a 6px green dot plus 11px mono uppercase `STATIC / OFFLINE`, hidden below 1120px.
- **Rail:** sticky 58px offset, search head, a counts line (`38 BUILDS / 3 KITS`), sticky group titles with a gradient-to-ground fade, and 7px/14px items marked by a 4px square that turns green when current. Kits carry a cyan `KIT` tag with a 3px radius.
- **Mobile:** the rail becomes a fixed drawer `min(86vw, 330px)` with a 60% black backdrop, a `Browse builds` button, focus moved to search, Escape closes, and a `translateX(-102%)` → `none` transition at 220ms.

### Schematic Stage (signature)
The stage is the product's signature component: a 1px hairline frame with a 24px dot grid, a faint outer vignette, and an authored 520×200 line weapon centered at 64% width (52% SMG, 42% pistol, 66% shotgun, 70% DMR/sniper). Slot nodes are 8px cards at `rgba(4,8,6,0.86)` with a 1px 20% green border, an 11px mono uppercase slot key, a 12px/600 name clamped to two lines, and an amber `×N` when the command repeats a part. Hover raises the border to 48% and lifts the node 1px; selection uses the full green border plus a 10% wash. Curved 1px traces at 22% green connect nodes to anchor dots, becoming a 1.6px full-green stroke and dot when its part is selected. On selection the trace draws over 550ms with a per-node 22ms delay, nodes enter over 400ms staggered 16ms, and all of it collapses to the final state under `prefers-reduced-motion`.

Kit entries replace the rig with a manifest: an `auto-fit` grid of 190px-minimum cards (160px on mobile), each showing an 11px mono `ITEM` key, a 12px name, and a cyan ID. The stage always carries the 11px mono caption `SCHEMATIC · NOT A GAME RENDER` in dim sage, and the bench foot repeats that slot grouping is inferred and fit is unverified.

### Stat Readout (signature)
The stat pair is set 44px/600 mono in amber with tabular numerals, a 26px dim slash between the values, and a 12px muted note capped at 34ch stating that the source does not label the two values. It drops to 38px on narrow screens. For accessory kits the same slot renders empty dashes; no kit reading exists in the source. The meta grid below it reports Parts, Ammo, and Option in mono, with `Ammo` formatted with thousands separators (`1,000`) and `Option` from the variant label (`Standard`, `Long`, `Short`).

### Command Block
The command preview is an 11.5px/1.55 mono `<pre>` on a 30% black fill with a hairline border, 8px radius, 9px/10px padding, `pre-wrap` and `break-word` so a long `AddItem` line never forces horizontal scroll. The note above it explains prefix normalization in 12px muted prose with inline mono code. The primary copy button sits above the note; the toast confirms with `Copied 13-item command` in 12px mono, a 42% green border on `#04120b`, and a 160ms fade/8px rise, auto-dismissing after 2.3s.

**The Selection-Is-A-Wash Rule.** Selected and current states are a 1px green border plus an 11% green wash, and on horizontal tabs a 2px inset underline. Text does not invert to green-on-black except on the primary button and skip link; the selection marker is a 4px square, not a background fill.

**The Diagram-Disclaimer Rule.** Any schematic carries the `SCHEMATIC · NOT A GAME RENDER` caption and the bench-foot sentence that grouping is inferred and in-game success is unverified. A schematic without both is off-system.

## Do's and Don'ts

### Do:
- **Do** draw structure with the hairline tokens (`rgba(126,226,162,0.16)` for dividers, `0.3` for interactive borders) before reaching for a fill or shadow.
- **Do** keep measurements amber and tabular (`font-variant-numeric: tabular-nums`; the pair is 44px/600 mono), and keep identifiers cyan in mono at 11px.
- **Do** keep every copied ID character-exact — casing, underscores, and game-side spellings intact — and never translate weapon names or IDs.
- **Do** show state with more than color: the rail adds a 4px dot, tabs add an inset 2px underline, inputs add a 1px ring.
- **Do** keep the global focus treatment: 2px cyan outline, 2px offset, 4px radius.
- **Do** respect `prefers-reduced-motion`: the trace draw, node entrance, drawer, toast, and hero draw all resolve instantly.
- **Do** keep prose measures tight — 34ch for the stat note, 44ch for card copy, 56ch for hub intro, 62ch for the bench foot, 78ch for the hub footer.
- **Do** use the primary green button once per view: copy full build in the readout, or copy command in the mobile bar.
- **Do** keep the OS font stacks; the site must work offline with no external font request.

### Don't:
- **Don't** add glass, backdrop blur, outer glow, or gradient text. Existing gradients are functional — sticky group-title fades, the dot-grid mask, the stage vignette — never decoration or text fills.
- **Don't** put game screenshots, weapon renders, or illustrated icons on the bench; the only weapon imagery is the authored line schematic.
- **Don't** invent a label or unit for the stat pair, or a compatibility claim for a slot; show the source reading and the unverified note.
- **Don't** use green for a stat value, amber for an identifier, or cyan for an action; the three signal channels do not swap.
- **Don't** introduce a light theme, a second surface family, or a saturated panel fill.
- **Don't** set weapon or build names in uppercase or in mono, and don't add letterspacing to display headlines.
- **Don't** use pill radii on buttons, inputs, or tags; 99px is for scrollbar thumbs only.
- **Don't** replace the 1px hairline with a 2px frame or a cast shadow to create hierarchy; use the one-step tonal lift instead.
