---
name: excel-formula-refresh
version: 1.0.0
description: |
  Replace hard-coded totals and subtotals in an accounting system export with
  proper Excel SUM formulas. Ensures that total rows sum the amounts above them
  rather than containing static exported values that won't update when data changes.
trigger: |
  "formula refresh", "fix the totals", "add SUM formulas", "hard-coded export",
  "totals aren't formulas", "replace hard-coded numbers", "Excel totals"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Excel Formula Refresh: Replace Hard-Coded Totals with SUM Formulas

## Purpose

Accounting system exports (from Sage Intacct, QBO, or others) often contain hard-coded total rows — static numbers that were accurate at export time but don't update if the data is edited. This skill replaces those hard-coded totals with proper Excel SUM formulas.

## Required Inputs

- The Excel file or worksheet description
- Column structure (which columns contain amounts)
- How to identify total rows (e.g., "Total" in column A, bold rows, specific row labels)

## Workflow

1. **Identify the data structure** — Understand the layout: where the data rows are, how total rows are identified, and whether there are subtotals and grand totals.
2. **Identify hard-coded total cells** — Find cells in total rows that contain static numbers instead of formulas. These are the targets.
3. **Determine the correct SUM range** — For each total cell, identify which rows above it should be included in the sum. Watch for:
   - Subtotals that shouldn't include other subtotals (to avoid double-counting)
   - Header rows or blank rows that should be excluded
4. **Generate the replacement formulas** — For each total cell: `=SUM(C5:C12)` or similar. If subtotals are included in a grand total, use `=SUM()` that skips the subtotals (e.g., reference only the data rows, or use `=SUMIF()` for grouped structures).
5. **Provide output** — Specify exactly which cells to update and with what formula.

## Control Points

- **Double-counting subtotals** — If a grand total would include both subtotal rows and the detail rows that make up those subtotals, flag this before providing formulas. The user must confirm the intended range.

## Red Flags

- Total row contains a formula that references a different range than expected (may indicate a prior manual adjustment)
- Multiple layers of subtotals where the structure is ambiguous

## Output Format

A table of replacement formulas:
| Cell | Current Value | Replacement Formula |
|---|---|---|
| C15 | 125,430 | =SUM(C5:C14) |
| C28 | 847,220 | =SUM(C18:C27) |

Plus any notes on ranges to verify before applying.

## Safety Constraints

- Do not modify the source data rows — only replace values in total/subtotal rows.
- Flag any cells where the correct SUM range is ambiguous rather than guessing.
