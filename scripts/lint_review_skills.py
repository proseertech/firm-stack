#!/usr/bin/env python3
"""Lint the tax return review skills against the canonical findings-table block.

Every skills/*-review/SKILL.md must contain the shared findings-table block
defined in templates/findings-table.md (placeholders {{EXAMPLE_ROWS}},
{{FORM_EXAMPLES}}, {{SORT_ORDER}} are per-form; the rest is byte-for-byte).
This keeps the 5-column format from drifting as skills are edited one at a
time — the exact failure mode that produced inconsistent review output.

Also checks, per skill:
  - example rows have exactly 5 columns
  - severity tags are only **[HIGH]** / **[MEDIUM]** / **[LOW]**
  - confirmed rows ("No change — confirmed correct") carry no severity tag
  - no remnants of the retired text-block format ("Issue #[", "| # | Severity")

Run from anywhere: python3 scripts/lint_review_skills.py
Exits 0 when clean, 1 with a per-file error list otherwise.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "templates" / "findings-table.md"
SKILLS_GLOB = "*-review/SKILL.md"

PLACEHOLDERS = {
    "{{EXAMPLE_ROWS}}": r"(?P<example_rows>\|[^\n]*\|(?:\n\|[^\n]*\|)*)",
    "{{FORM_EXAMPLES}}": r"[^\n]+?",
    "{{SORT_ORDER}}": r"[^\n]+?",
}

ALLOWED_TAGS = {"**[HIGH]**", "**[MEDIUM]**", "**[LOW]**"}
LEGACY_MARKERS = ["Issue #[", "| # | Severity"]


def load_template() -> str:
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->\n", "", text, count=1, flags=re.DOTALL)
    return text.strip("\n")


def template_regex(template: str) -> re.Pattern:
    parts = re.split(r"(\{\{[A-Z_]+\}\})", template)
    pattern = "".join(
        PLACEHOLDERS[p] if p in PLACEHOLDERS else re.escape(p) for p in parts
    )
    return re.compile(pattern)


def check_example_rows(rows_block: str) -> list[str]:
    errors = []
    for row in rows_block.strip("\n").split("\n"):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        label = cells[0] if cells else row
        if len(cells) != 5:
            errors.append(
                f"example row has {len(cells)} columns, expected 5: {row[:60]}"
            )
            continue
        tags = re.findall(r"\*\*\[[^\]]*\]\*\*", cells[0])
        for tag in tags:
            if tag not in ALLOWED_TAGS:
                errors.append(f"unknown severity tag {tag} in row: {label}")
        if "confirmed correct" in row and tags:
            errors.append(
                f"confirmed row must not carry a severity tag "
                f"(column rules say to omit it): {label}"
            )
    return errors


def check_skill(path: Path, block_re: re.Pattern) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = []

    matches = list(block_re.finditer(text))
    if not matches:
        errors.append(
            "canonical findings-table block missing or drifted from "
            "templates/findings-table.md (check wording, bullet order, and the "
            "blank line between the example table and 'Column rules:')"
        )
    elif len(matches) > 1:
        errors.append("canonical findings-table block appears more than once")
    else:
        errors.extend(check_example_rows(matches[0].group("example_rows")))

    for marker in LEGACY_MARKERS:
        if marker in text:
            line_no = text[: text.index(marker)].count("\n") + 1
            errors.append(
                f"retired text-block format remnant {marker!r} at line {line_no} "
                "— use the 5-column findings table"
            )
    return errors


def main() -> int:
    skills = sorted((ROOT / "skills").glob(SKILLS_GLOB))
    if not skills:
        print(f"error: no skills matched skills/{SKILLS_GLOB}", file=sys.stderr)
        return 1

    block_re = template_regex(load_template())
    failed = False
    for skill in skills:
        rel = skill.relative_to(ROOT)
        errors = check_skill(skill, block_re)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"ok   {rel}")

    if failed:
        print(
            "\nShared wording lives in templates/findings-table.md — edit it and "
            "all review skills together.",
            file=sys.stderr,
        )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
