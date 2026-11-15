# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Incursion Red River players who spawn gear and weapons through the in-game console. They are at a PC, in or between raids, and want an item ID or a working loadout command they can paste without editing. Secondary audience: players comparing tested weapon builds before spending an inventory slot.

## Product Purpose

A static reference site that turns the game's vendor export and a curated build list into copy-ready `AddItem` console commands. Success means the player finds the right ID or build in seconds, copies one line, and the command works in game.

## Positioning

The catalog is reconciled against the exact 825 row names from the `DT_Vendor_Old` export rather than guessed asset names, and it clearly separates what is verified (row exists in the export) from what is not (command succeeds, attachment fits, build retested). No account, server, build step, or network call is required.

## Operating Context

Players use the site on desktop browsers, often beside the game, and may download a single HTML file and open it offline. Commands are pasted into the game console. Builds originate from Firestar's community list; several builds include both long and short barrel options in one command.

## Capabilities and Constraints

- 825 exact vendor row IDs in `data/vendor-row-ids.json`; the terminal browses, searches and copies them.
- 42 curated build commands from `Weapon builds by Firestar.htm`, grouped by weapon class, plus Armour, Laser/Torch and Sights accessory kits.
- Build stat values are only recorded as an unlabeled pair such as `59.3/0`; the source does not define what the two numbers mean.
- No item icons, weapon renders, prices, or attachment-compatibility data exist in the repository. Compatibility must never be invented.
- The build list has not been retested against the current game version.
- The site must stay dependency-free and work from GitHub Pages and from a local file where feasible.
- The hub and build bench ship in English and Simplified Chinese, with the choice stored locally; the item terminal remains English and item IDs are never translated.

## Brand Commitments

Existing site identity: near-black green-tinted ground, phosphor-green accent, monospace data type, dense but calm terminal layout. The catalog's tone is factual and explicit about unverified data.

## Evidence on Hand

- `Incursion_Terminal.html` — searchable item catalog terminal.
- `builds.html` — generated build bench with the schematic and bilingual UI.
- `tools/build_data.py`, `tools/render_builds.py`, `tools/builds-template.html` — build parser, renderer and page template.
- `Item_List.htm` — plain-text catalog.
- `Weapon builds by Firestar.htm` — 42 build commands and three accessory kits.
- `data/vendor-row-ids.json` — source note, 825 row IDs, corrections and retained legacy IDs.
- `README.md` — provenance, corrections table, and explicit non-claims.

## Product Principles

1. Never invent an ID, a compatibility rule, or a stat meaning. Show the source's exact value and label the uncertainty.
2. Copying is the primary action; every view ends one click away from a valid command line.
3. The catalog and builds are the content; the interface earns its place by making the build structure legible, not by decorating it.
4. Offline and GitHub Pages parity: no external fonts, scripts, APIs, or build step at runtime.
5. Preserve provenance: corrections, retained legacy IDs, and unverified claims travel with the data.

## Accessibility & Inclusion

Keyboard-operable selection, visible focus, body text at 4.5:1 contrast or better, and no information carried by color alone. Respect reduced-motion preferences for any traced or animated diagram.
