---
name: excel-formula-refresh
version: 1.3.0
description: |
  Replace hard-coded total and subtotal rows in an accounting export (trial balance,
  P&L, GL detail, or any spreadsheet) with live Excel SUM, SUBTOTAL, or SUMIF formulas,
  so totals recalculate when the detail changes instead of showing stale exported numbers.
  Use this whenever the totals in a workbook are typed-in values rather than formulas —
  even when the user doesn't say "formula." Fires for "the totals don't add up when I edit
  a row," "these numbers are hard-coded," "make the totals dynamic/live," "the total won't
  update," "add formulas to this export," and reviewing a spreadsheet whose totals need to
  tie to their detail. This is about the math in total cells; standardizing fonts, colors,
  and layout is excel-report-format.
trigger: |
  "formula refresh", "fix the totals", "add SUM formulas", "add SUBTOTAL formulas",
  "hard-coded export", "hard-coded totals", "totals aren't formulas", "replace hard-coded numbers",
  "Excel totals", "make the totals live", "make the totals dynamic", "totals won't update",
  "totals don't recalculate", "the total doesn't add up", "convert totals to formulas"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Excel Formula Refresh: Replace Hard-Coded Totals with Live Formulas

## Purpose

Accounting system exports often contain hard-coded total rows — static numbers that were accurate at export time but silently go wrong once someone edits a detail row, because the total doesn't recalculate. This skill replaces those hard-coded totals with live Excel formulas — SUM, SUBTOTAL, or SUMIF — choosing the function that fits the report's structure so every total ties to the detail above it and stays correct as the data changes.

Scope is the math in total cells. Formatting the report to the firm's look (fonts, borders, number formats) is `excel-report-format`.

## Required Inputs

- The Excel file or worksheet description
- Column structure (which columns contain amounts)
- How to identify total rows (e.g., "Total" in column A, bold rows, specific row labels)

## Workflow

1. **Identify the data structure** — Understand the layout: where the data rows are, how total rows are identified, and whether there are subtotals and grand totals.
2. **Identify hard-coded total cells** — Find cells in total rows that contain static numbers instead of formulas, across every sheet in the workbook (not just the active sheet). These are the targets.
3. **Determine the correct formula range** — For each total cell, identify which rows above it should be included. Watch for:
   - Subtotals that shouldn't include other subtotals (to avoid double-counting — candidate for SUBTOTAL)
   - Header rows or blank rows that should be excluded
   - Grouped/tagged structures where a category label drives the total (candidate for SUMIF)
4. **Generate the replacement formulas** — Choose the right function for each total cell:
   - `=SUM(range)` — simple total of a contiguous block of detail rows with no nested subtotals.
   - `=SUBTOTAL(9, range)` — use when the range contains nested subtotal rows. SUBTOTAL automatically ignores other SUBTOTAL results in the referenced range, which prevents double-counting and lets the grand total reference the whole range without excluding subtotal rows manually. Use function code `109` instead of `9` if the report uses filtering and the total should also ignore hidden rows.
   - `=SUMIF(criteria_range, criteria, sum_range)` — grouped or tagged structures where totals pull by category label rather than by position.
   - For a grand total above mixed detail and subtotal rows, SUBTOTAL is usually the cleanest choice. If the existing subtotals are `SUM` (not `SUBTOTAL`), either convert them to SUBTOTAL so the grand total can reference the full range, or have the grand total `SUM` only the detail rows.
5. **Provide output** — Specify exactly which cells to update and with what formula.

## Control Points

- **Double-counting subtotals** — If a grand total would include both subtotal rows and the detail rows that make up those subtotals, the safe options are (a) use SUBTOTAL for both the subtotals and the grand total so the grand total auto-ignores them, or (b) have the grand total use SUM over only the detail rows. Flag the ambiguity and confirm the intended approach with the user before writing formulas that could double-count.

## Red Flags

- A total cell already contains a formula, but one referencing a different range than expected — may be a prior manual adjustment. Surface it and confirm before overwriting; don't assume the existing formula is wrong.
- Multiple layers of nested subtotals where the grouping is ambiguous. Show the user the structure you inferred and confirm before writing formulas.

## Output Format

A table of replacement formulas. Example of a report with two subtotals and a grand total, using SUBTOTAL throughout so the grand total can reference the full range:

| Cell | Current Value | Replacement Formula | Notes |
|---|---|---|---|
| C15 | 125,430 | =SUBTOTAL(9,C5:C14) | Subtotal |
| C28 | 847,220 | =SUBTOTAL(9,C18:C27) | Subtotal |
| C30 | 972,650 | =SUBTOTAL(9,C5:C29) | Grand total — auto-ignores the nested SUBTOTAL rows |

Alternative (simple SUM) when there are no nested subtotals:

| Cell | Current Value | Replacement Formula |
|---|---|---|
| C15 | 125,430 | =SUM(C5:C14) |

Include any notes on ranges the user should verify before applying.

## Safety Constraints

- Touch only total and subtotal cells. Do not modify, reorder, or delete the source detail rows — those are the client's data, and a formula refresh must never change what the report says, only make the totals recompute it.
- When the correct range or formula choice is ambiguous, flag it and confirm rather than guessing — a wrong range produces a total that looks right but silently mis-adds, and the error surfaces only after the file has been relied on.
