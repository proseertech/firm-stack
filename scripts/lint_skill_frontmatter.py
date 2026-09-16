#!/usr/bin/env python3
"""Lint every skill's YAML frontmatter against the schema in templates/SKILL.md.tmpl.

The findings-table lint (lint_review_skills.py) only covers the eight
skills/*-review/SKILL.md files, and only their Output Format section. Nothing
checked frontmatter — which is how commit 7ec5b99 was able to rename `trigger`
to `when-to-use` and move `tier` under `metadata` across all 24 skills while
leaving templates/SKILL.md.tmpl and docs/skill-authoring.md teaching the retired
spelling. A contributor starting from the template would have silently
reintroduced the drift.

Checks, per skills/*/SKILL.md:
  - frontmatter is present and terminated
  - required keys present: name, version, description, allowed-tools,
    when-to-use, metadata
  - retired keys absent at the top level: trigger, tier
  - `name` matches the containing directory
  - every allowed-tools entry is a known tool
  - metadata.tier is one of the documented tiers

Deliberately dependency-free (no PyYAML): CI runs bare `python3`, and the
frontmatter this validates is a flat subset of YAML.

Run from anywhere: python3 scripts/lint_skill_frontmatter.py
Exits 0 when clean, 1 with a per-file error list otherwise.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_KEYS = ("name", "version", "description", "allowed-tools",
                 "when-to-use", "metadata")
RETIRED_KEYS = {
    "trigger": "renamed to 'when-to-use'",
    "tier": "moved under 'metadata:'",
}
KNOWN_TOOLS = {
    "Read", "Write", "Edit", "Grep", "Glob", "Bash", "AskUserQuestion",
    "WebSearch", "WebFetch", "Agent", "Task", "NotebookEdit", "TodoWrite",
}
KNOWN_TIERS = {"all-staff", "power-user", "developer"}


def split_frontmatter(text: str):
    """Return (frontmatter_lines, error) for a '---' delimited YAML block."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, "no YAML frontmatter (file must start with '---')"
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[1:i], None
    return None, "frontmatter is not terminated by a closing '---'"


def top_level_keys(fm_lines):
    """Map top-level key -> its inline value (empty for block/nested keys)."""
    keys = {}
    for line in fm_lines:
        if not line or line[0] in " \t#" or ":" not in line:
            continue
        key, _, value = line.partition(":")
        if key.strip() == key:
            keys[key] = value.strip()
    return keys


def block_items(fm_lines, key):
    """List items belonging to a top-level `key:` block ('- value' lines)."""
    items, collecting = [], False
    for line in fm_lines:
        if line.startswith(f"{key}:"):
            collecting = True
            continue
        if collecting:
            stripped = line.strip()
            if stripped.startswith("- "):
                items.append(stripped[2:].strip())
            elif stripped and not line[0].isspace():
                break
    return items


def nested_value(fm_lines, parent, child):
    """Value of `child:` nested one level under `parent:`, or None."""
    collecting = False
    for line in fm_lines:
        if line.startswith(f"{parent}:"):
            collecting = True
            continue
        if collecting:
            if line.strip() and not line[0].isspace():
                break
            if line.strip().startswith(f"{child}:"):
                return line.split(":", 1)[1].strip()
    return None


def check_skill(path: Path) -> list[str]:
    fm_lines, err = split_frontmatter(path.read_text(encoding="utf-8"))
    if err:
        return [err]

    errors = []
    keys = top_level_keys(fm_lines)

    for key in REQUIRED_KEYS:
        if key not in keys:
            errors.append(f"missing required frontmatter key '{key}'")

    for key, guidance in RETIRED_KEYS.items():
        if key in keys:
            errors.append(f"retired frontmatter key '{key}' — {guidance}")

    expected = path.parent.name
    if "name" in keys and keys["name"] != expected:
        errors.append(
            f"name '{keys['name']}' does not match directory '{expected}'")

    tools = block_items(fm_lines, "allowed-tools")
    if "allowed-tools" in keys and not tools:
        errors.append("allowed-tools is present but lists no tools")
    for tool in tools:
        if tool not in KNOWN_TOOLS:
            errors.append(
                f"unknown tool '{tool}' in allowed-tools "
                f"(known: {', '.join(sorted(KNOWN_TOOLS))})")

    if "metadata" in keys:
        tier = nested_value(fm_lines, "metadata", "tier")
        if tier is None:
            errors.append("metadata block has no 'tier:'")
        elif tier.split("#")[0].strip() not in KNOWN_TIERS:
            errors.append(
                f"metadata.tier '{tier}' is not one of {sorted(KNOWN_TIERS)}")

    return errors


def main() -> int:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        print("error: no skills matched skills/*/SKILL.md", file=sys.stderr)
        return 1

    failed = False
    for skill in skills:
        errors = check_skill(skill)
        rel = skill.relative_to(ROOT)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"ok   {rel}")

    if failed:
        print("\nThe frontmatter schema lives in templates/SKILL.md.tmpl and is "
              "documented in docs/skill-authoring.md — keep all three in sync.",
              file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
