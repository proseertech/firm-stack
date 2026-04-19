---
name: excel-formula-refresh
version: 1.2.0
description: |
  Replace hard-coded totals and subtotals in an accounting system export with
  proper Excel SUM, SUBTOTAL, or SUMIF formulas. Ensures that total rows sum
  the amounts above them rather than containing static exported values that
  won't update when data changes.
trigger: |
  "formula refresh", "fix the totals", "add SUM formulas", "add SUBTOTAL formulas",
  "hard-coded export", "totals aren't formulas", "replace hard-coded numbers", "Excel totals"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Excel Formula Refresh: Replace Hard-Coded Totals with Live Formulas

## Purpose

Accounting system exports (from Sage Intacct, QBO, or others) often contain hard-coded total rows — static numbers that were accurate at export time but don't update if the data is edited. This skill replaces those hard-coded totals with live Excel formulas — SUM, SUBTOTAL, or SUMIF — chosen based on the structure of the report.

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

- Total row contains a formula that references a different range than expected (may indicate a prior manual adjustment)
- Multiple layers of subtotals where the structure is ambiguous

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

- Do not modify the source data rows — only replace values in total/subtotal rows.
- Flag any cells where the correct range or formula choice is ambiguous rather than guessing.
