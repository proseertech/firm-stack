# Workbook Build — Formulas & Styling

Reference for building the projection sheet in Phase 4. The section order and judgment are in
SKILL.md; this file holds the exact formula patterns, styling palette, and column widths.

---

## Excel Formula Rules

Every calculated cell must use a formula. Never hardcode a derived value.

| Cell Type | Formula Pattern |
|-----------|----------------|
| Income line (curr year) | `=-SUMIF('TB Sheet'!$E:$E,B{r},'TB Sheet'!$D:$D)` — B{r} is the label cell |
| Expense line (curr year) | `=SUMIF('TB Sheet'!$E:$E,B{r},'TB Sheet'!$D:$D)` — B{r} is the label cell |
| Variance | `=D{r}-C{r}` |
| Section total | `=SUM(D{start}:D{end})` |
| Net income | `=D{income}-D{expenses}-D{depreciation}` |
| K-1 per-owner | `=D{r}*0.5` (or actual %) |
| K-1 taxable total | `=SUM(D{line_refs})` |
| 199A deduction | `=MIN(D{qbi}*0.2, D{w2}*0.5)` |
| Reconciliation | `=SUM(all_tag_totals) - TB_grand_total` |

**What stays hardcoded** (inputs only): prior-year return amounts, owner percentages, tax
rates, depreciation from future dep reports, property names, notes text.

Track row numbers in a `rows = {}` dict while building so formulas reference correct cells.

**Column layout** (always this order):
| B: Description | C: [Prior Year] Actual | D: [Current Year] Estimated | E: Variance | F+: Notes |

- Column C: Hardcoded from the filed return (reference data)
- Column D: SUMIF formula referencing B{r} (the label cell in the same row) as the criteria — NEVER hardcode the tag name inside the formula. The column B label IS the tag. Form line references (e.g., "Line 1a") go in the Notes column, not in column B.
- Column E: Formula `=D{r}-C{r}`
- Notes column: Explanations, flags, assumptions

---

## Styling Rules

**Only 5 fill colors. Data rows have NO fill — leave them white.**
Fills are reserved for structural rows only. This keeps the workpaper light and readable.

| Element | Fill | Font | Border |
|---------|------|------|--------|
| Section headers | #1F4E79 (dark blue) | White, bold, 11pt | — |
| Column headers | #D6E4F0 (soft blue) | Bold, 10pt | — |
| Total rows | #E2EFDA (soft green) | Bold | top=medium, bottom=double |
| Subtotal rows | #F2F2F2 (light gray) | Bold | bottom=thin |
| Flagged items | #FFF2CC (soft yellow) | Bold | — |
| **Data rows** | **No fill (white)** | Normal, 10pt | — |
| Losses / negatives | No fill | Red font (#C00000) | — |
| Notes column | No fill | Gray italic (#666666), 9pt | — |
| Non-taxable K-1 items | No fill | Gray font (#666666) | — |

Numbers: Right-aligned, `#,##0` or `#,##0;(#,##0)` for items that can be negative.
Column widths: B=44, C-F=15-17, Notes=45.

**Trial Balance tag column fills** (optional — for visual scanning):

| Tag Category | Fill Color |
|-------------|-----------|
| Income tags | #E2EFDA (light green) |
| Expense tags | #FDE9D9 (light orange) |
| COGS tags | #D6E4F0 (light blue) |
| BS tags | #F2F2F2 (light gray) |
| K1 separately stated | #E8D5F5 (light purple) |
| Nondeductible | #FFC7CE (light red) |
| Capital/reclassify | #FFF2CC (light yellow) |
