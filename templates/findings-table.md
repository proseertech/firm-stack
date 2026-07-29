<!--
Canonical findings-table block for the tax return review skills
(skills/*-review/SKILL.md). CI runs scripts/lint_review_skills.py to check
every review skill's Output Format section against this file.

Three placeholders are per-form; everything else must match byte-for-byte:
  {{EXAMPLE_ROWS}}   one or more form-specific example table rows
  {{FORM_EXAMPLES}}  the e.g. list of form references for that return type
  {{SORT_ORDER}}     the form/schedule reading order for that return type

To change the shared wording, edit this file and every review skill together
in the same PR — the lint fails until they agree.
-->
### Findings Table (required format)

A markdown table in chat, a Word table in .docx. One row per item. **Exactly these 5 columns, in this order:**

| Line / Schedule | Current treatment | Recommended treatment | Reason | Authority |
|---|---|---|---|---|
{{EXAMPLE_ROWS}}

Column rules:
- **Line / Schedule** — Specific form reference (e.g., {{FORM_EXAMPLES}}). **Severity** is a bold tag at the start of this cell: **[HIGH]**, **[MEDIUM]**, **[LOW]**. Omit the tag for confirmed items.
- **Current treatment** — What the return currently shows. State "Blank" or "Not checked" when a field is omitted. Include the dollar amount inline if relevant.
- **Recommended treatment** — The specific correction, or "No change — confirmed correct" for items that tie. Use "Preparer to analyze" where the answer needs judgment or data you don't have. For optional improvements, prefix with "Optional:".
- **Reason** — The factual or legal basis for the recommendation. Explain *why*, not just *what*.
- **Authority** — IRC section, Reg., Revenue Ruling, form instructions, or source document. Use "—" if none applies.

Table rules:
- **Every reviewed item goes in the table** — issues, confirmed items, items confirmed not applicable, and optional recommendations alike. Do not omit correct items; they show the reviewer checked them.
- **Sort rows by form/schedule order** ({{SORT_ORDER}}), not by severity. Severity tags handle prioritization within the natural reading flow.
- **One row per line item.** Do not split a single issue across multiple rows, and do not merge two issues into one.
