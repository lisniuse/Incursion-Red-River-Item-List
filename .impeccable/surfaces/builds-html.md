---
version: 1
slug: "builds-html"
primary_target: "builds.html"
related_targets: []
---

# Weapon Builds — surface brief

## Scope and mode

New page `builds.html` inside the existing static site, linked from a two-entry `index.html`. Visitor mode: **Operate**. The page is a working modding bench, not a showcase.

## Audience and job

Incursion Red River players choosing one of Firestar's 42 presets and copying its console command. They arrive knowing the weapon, need to see the full part set and stats, then copy one line. Accessory kits (Armour, Laser/Torch, Sights) are secondary and use a simple part-list mode.

## Content and constraints

- Source of truth: `Weapon builds by Firestar.htm`. Preserve item IDs exactly, including duplicates and the missing `additem` prefixes where the source omits them (normalise only the prefix, never the ID).
- Stats are an unlabeled pair; show the raw reading and state that the meaning is not recorded.
- No compatibility data, icons, or renders exist. The schematic is an authored diagram, not a game screenshot.
- Must work on GitHub Pages and offline: no external fonts, scripts, or network requests at runtime.

## Success and failure

Success: a player picks a weapon, reads the slot arrangement and stats, and copies the command in seconds. Failure that must be avoided: a page that looks like a game replica costume, invents compatibility, or hides the command line under visual noise.

## Direction contract

THESIS: The build is read as a schematic — the gun at center, its real preset parts as labeled branches — so the whole loadout is legible before any text list. Refuses the item-table page as the primary reading.

OWN-WORLD: Near-black green-tinted ground (#030504), phosphor green ink (#39ff88), cyan for identifiers (#72d6ff), amber for measurements (#ffca6b). Blueprint grid, 1px hairline branches, dense monospace data, compact corners. No glass, glow, or gradient text.

STORY: Scan the weapon rail → understand the slot arrangement and stat reading → inspect a part → copy the full command.

FIRST VIEWPORT: Three-column bench. Left: searchable weapon rail grouped by class. Center: blueprint stage with the weapon schematic and branch labels. Right: stat readout, part list, and copy action. A sticky command bar keeps the full command one click away.

FORM: User-pinned composition (center weapon with four-side slot tree, selected via structured question); no seed roll. Code-led build.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance.
