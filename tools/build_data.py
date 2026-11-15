#!/usr/bin/env python3
"""Parse 'Weapon builds by Firestar.htm' into structured build data.

The source is a plain-text file. Item IDs are preserved exactly; only a
missing `additem` prefix is normalised so every part is a usable command.

Usage (from the repository root):
    python tools/build_data.py            # print JSON
    python tools/build_data.py --check    # print a compact audit
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "Weapon builds by Firestar.htm"

RULE_RE = re.compile(r"^[─—\-]{5,}$")
STAT_RE = re.compile(r"^(?:(L|S)\s*)?([\d.]+)\s*/\s*([\d.]+)$")
INLINE_STATS_RE = re.compile(r"^(.*?)\s*\((.*)\)\s*$")

SECTION_ORDER = [
    "Rifles", "SMG's", "Pistols", "DMR's", "Snipers", "Shotguns",
    "Armour", "Laser/Torch", "Sights",
]
KIT_SECTIONS = {"Armour", "Laser/Torch", "Sights"}

# Order matters: the first matching rule wins.
SLOT_RULES = [
    ("magazine", r"rnd|round|drum|mag5|powermag|_mag(_|$)|[-_]shell"),
    ("ammo", r"^(x?338|556x45|545x39|762x39|762x51|762x54|9x19|45acp|57x28|12x70|x300)(_|$)"),
    ("muzzle", r"suppressor|silencer|muzzle|brake|flash_hider|compensator|thread_adapter|_claw"),
    ("barrel", r"barrel"),
    ("optic", r"sight|scope|optic|acog|rmr|holographic|reflex|thermal|vudu|hamr|deltapoint|exps3|uh-1|mrd|mrds|sight_mount"),
    ("tactical", r"laser|flashlight|tactical_device|peq|aplc|apl-?c"),
    ("stock", r"buttstock|_stock|stock_adapter|buffertube|buffer_mount|buffer_tube"),
    ("grip", r"pistol_grip"),
    ("foregrip", r"foregrip|combat_grip|angled_grip|vertical_grip|se3_foregrip"),
    ("chassis", r"chassis"),
    ("rail", r"(^|_)rail(_|$)|rail_mount|picatinny|_b-13(_|$)|offset_rail"),
    ("handguard", r"handguard|dust_cover"),
]

SLOT_LABELS = {
    "receiver": "Receiver",
    "magazine": "Magazine",
    "ammo": "Ammunition",
    "muzzle": "Muzzle",
    "barrel": "Barrel",
    "optic": "Optic",
    "tactical": "Laser / Light",
    "stock": "Stock",
    "grip": "Pistol Grip",
    "foregrip": "Foregrip",
    "chassis": "Chassis",
    "rail": "Rail",
    "handguard": "Handguard",
    "other": "Other",
}


def classify(item_id: str, index: int, qty: int) -> str:
    low = item_id.lower()
    if index == 0:
        for slot, pattern in SLOT_RULES:
            if slot == "magazine" and re.search(pattern, low):
                return slot
        if qty >= 100:
            return "ammo"
        return "receiver"
    for slot, pattern in SLOT_RULES:
        if re.search(pattern, low):
            return slot
    if re.search(r"adapter|gas_block|mount", low):
        return "other"
    return "other"


def pretty(item_id: str) -> str:
    return item_id.replace("_", " ").strip()


def split_command(line: str) -> list[dict]:
    parts: list[dict] = []
    for raw in line.split("|"):
        seg = raw.strip()
        if not seg:
            continue
        missing_prefix = not re.match(r"^additem\s+", seg, re.I)
        if missing_prefix:
            seg = "additem " + seg
        body = re.sub(r"^additem\s+", "", seg, flags=re.I).strip()
        match = re.match(r"^(.+?)\s+(\d+)$", body)
        missing_qty = match is None
        if match:
            item_id, qty = match.group(1).strip(), int(match.group(2))
        else:
            item_id, qty = body, 1
        if not item_id:
            continue
        parts.append({
            "id": item_id,
            "qty": qty,
            "cmd": f"additem {item_id} {qty}",
            "normalised": missing_prefix or missing_qty,
        })
    return parts


def annotate(parts: list[dict], kit: bool = False) -> list[dict]:
    seen: dict[tuple[str, str], int] = {}
    out = []
    for index, part in enumerate(parts):
        slot = "kit" if kit else classify(part["id"], index, part["qty"])
        key = (slot, part["id"])
        seen[key] = seen.get(key, 0) + 1
        out.append({
            **part,
            "slot": slot,
            "slotLabel": "Item" if kit else SLOT_LABELS.get(slot, "Other"),
            "display": pretty(part["id"]),
            "dup": seen[key],
        })
    return out


def parse_stats(text: str) -> list[dict]:
    text = text.strip()
    if not text:
        return [{"key": None, "label": "Standard", "a": None, "b": None, "raw": ""}]
    options = [option.strip() for option in text.split(" - ") if option.strip()]
    parsed = []
    for index, option in enumerate(options):
        match = STAT_RE.match(option)
        if not match:
            return [{"key": None, "label": "Standard", "a": None, "b": None, "raw": text}]
        key = match.group(1)
        label = {"L": "Long", "S": "Short"}.get(key or "", "Standard")
        if key is None and len(options) > 1:
            label = f"Option {index + 1}"
        parsed.append({
            "key": key,
            "label": label,
            "a": float(match.group(2)),
            "b": float(match.group(3)),
            "raw": f"{match.group(2)}/{match.group(3)}",
        })
    return parsed


def read_sections() -> list[dict]:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    sections: list[dict] = []
    current: dict | None = None
    index = 0
    while index < len(lines):
        if not RULE_RE.match(lines[index].strip()):
            index += 1
            continue
        title_at = index + 1
        while title_at < len(lines) and not lines[title_at].strip():
            title_at += 1
        end_at = title_at + 1
        while end_at < len(lines) and not RULE_RE.match(lines[end_at].strip()):
            end_at += 1
        if title_at >= len(lines):
            break
        current = {"title": lines[title_at].strip(), "entries": []}
        sections.append(current)
        index = end_at + 1
        while index < len(lines):
            line = lines[index].strip()
            if RULE_RE.match(line):
                break
            if line:
                current["entries"].append(line)
            index += 1
    return sections


def build_variant(label: str, key: str | None, stats: list[dict], command: str) -> dict:
    parts = annotate(split_command(command))
    return {
        "label": label,
        "key": key,
        "stats": stats,
        "statsRaw": stats[0].get("raw", "") if stats else "",
        "parts": parts,
        "command": " | ".join(part["cmd"] for part in parts),
        "partCount": len(parts),
        "hasReceiver": any(part["slot"] == "receiver" for part in parts),
        "ammoCount": sum(part["qty"] for part in parts if part["slot"] == "ammo"),
    }


def parse() -> dict:
    builds: list[dict] = []
    kits: list[dict] = []

    for section_index, section in enumerate(read_sections()):
        title = section["title"]
        entries = section["entries"]

        if title in KIT_SECTIONS:
            commands = [line for line in entries if re.match(r"^additem\b", line, re.I)]
            if not commands:
                continue
            parts = annotate(split_command(" | ".join(commands)), kit=True)
            kits.append({
                "id": re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"),
                "name": title,
                "section": "Kits",
                "sectionIndex": section_index,
                "parts": parts,
                "command": " | ".join(part["cmd"] for part in parts),
                "partCount": len(parts),
                "display": title,
            })
            continue

        current_name: str | None = None
        pending_stats: list[str] = []
        for line in entries:
            if re.match(r"^additem\b", line, re.I):
                if current_name is None:
                    continue
                inline = INLINE_STATS_RE.match(current_name)
                stats_text = ""
                name = current_name
                if inline:
                    name = inline.group(1).strip()
                    stats_text = inline.group(2).strip()
                if pending_stats:
                    stats_text = " - ".join(pending_stats)
                stats = parse_stats(stats_text)
                parts = annotate(split_command(line))
                builds.append({
                    "kind": "build",
                    "name": name,
                    "section": title,
                    "sectionIndex": section_index,
                    "stats": stats,
                    "statsRaw": stats_text,
                    "parts": parts,
                    "command": " | ".join(part["cmd"] for part in parts),
                    "partCount": len(parts),
                    "hasReceiver": any(part["slot"] == "receiver" for part in parts),
                    "ammoCount": sum(part["qty"] for part in parts if part["slot"] == "ammo"),
                })
                pending_stats = []
                continue
            if line.startswith("(") and line.endswith(")"):
                pending_stats.append(line[1:-1].strip())
            else:
                current_name = line
                pending_stats = []

    # Merge same-name entries (MPX S/L) into one build with variants.
    merged: list[dict] = []
    for build in builds:
        if merged and merged[-1]["name"] == build["name"] and merged[-1]["section"] == build["section"]:
            merged[-1]["_variants"].append(build)
        else:
            build["_variants"] = [build]
            merged.append(build)

    out_builds = []
    for build in merged:
        raw_variants = build["_variants"]
        variants: list[dict] = []
        if len(raw_variants) > 1:
            for raw in raw_variants:
                stat = raw["stats"][0] if raw["stats"] else {"label": "Standard", "key": None}
                variants.append(build_variant(stat["label"], stat["key"], raw["stats"], raw["command"]))
        else:
            stat_options = build["stats"]
            if len(stat_options) > 1:
                for stat in stat_options:
                    variants.append(build_variant(stat["label"], stat["key"], [stat], build["command"]))
            else:
                stat = stat_options[0] if stat_options else {"label": "Standard", "key": None}
                variants.append(build_variant(stat["label"], stat["key"], stat_options, build["command"]))

        primary = variants[0]
        entry = {
            "id": re.sub(r"[^a-z0-9]+", "-", build["name"].lower()).strip("-"),
            "name": build["name"],
            "display": build["name"],
            "section": build["section"],
            "sectionIndex": build["sectionIndex"],
            "statsRaw": build["statsRaw"],
            "stats": build["stats"],
            "variants": variants,
            "parts": primary["parts"],
            "command": primary["command"],
            "partCount": primary["partCount"],
            "hasReceiver": primary["hasReceiver"],
            "missingReceiver": not primary["hasReceiver"],
            "ammoCount": primary["ammoCount"],
        }
        out_builds.append(entry)

    out_builds.sort(key=lambda item: item["sectionIndex"])
    kits.sort(key=lambda item: item["sectionIndex"])

    return {
        "generatedFrom": "Weapon builds by Firestar.htm",
        "sourceNote": "Stat values are reproduced exactly as supplied; their meaning is not recorded. Compatibility and in-game command success are not verified.",
        "slotLabels": SLOT_LABELS,
        "sections": SECTION_ORDER,
        "builds": out_builds,
        "kits": kits,
        "counts": {
            "builds": len(out_builds),
            "kits": len(kits),
            "variants": sum(len(build["variants"]) for build in out_builds),
            "commands": len({variant["command"] for build in out_builds for variant in build["variants"]} | {kit["command"] for kit in kits}),
        },
    }


if __name__ == "__main__":
    data = parse()
    if "--check" in sys.argv:
        print(json.dumps(data["counts"], indent=2))
        for build in data["builds"]:
            slots: dict[str, int] = {}
            for part in build["parts"]:
                slots[part["slot"]] = slots.get(part["slot"], 0) + 1
            variants = ",".join(variant["label"] for variant in build["variants"])
            flag = " MISSING-RECEIVER" if build["missingReceiver"] else ""
            print(f'{build["section"]:9} {build["name"]:11} v[{variants}] parts={build["partCount"]:2} {slots}{flag}')
        for kit in data["kits"]:
            print(f'KIT       {kit["name"]:11} parts={kit["partCount"]}')
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))
