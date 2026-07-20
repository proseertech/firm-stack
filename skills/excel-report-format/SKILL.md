---
name: excel-report-format
version: 1.3.0
description: |
  Standardize an Excel workbook to the firm's look and feel — fonts, header and
  total-row styles, number formats, column widths, freeze panes, and print setup —
  to turn a raw system export or one-off spreadsheet into a polished, client-ready
  report. Use this whenever someone wants a spreadsheet cleaned up, made to look
  professional or consistent, put "on brand," or dressed up before it goes to a
  client — even when they don't say "formatting." This is presentation only: it
  restyles cells and never touches values or formulas. If the ask is to fix static
  totals into live SUM formulas, that's `excel-formula-refresh`, not this skill.
trigger: |
  "format this report", "standardize this Excel", "apply firm formatting",
  "make this look professional", "make it look nice", "make it presentable",
  "clean up this spreadsheet", "tidy up this workbook", "make it client-ready",
  "on-brand formatting", "polish this spreadsheet", "fix the formatting",
  "Excel formatting", "style this report", "consistent formatting"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
  - Bash
tier: all-staff
---

# Excel Report Format: Standardize to Firm Look and Feel

## Purpose

Apply the firm's standard formatting to an Excel report so client-facing output looks uniform and polished instead of carrying the ad-hoc look of a system export or one-off spreadsheet. This is a presentation pass — it restyles cells (fonts, fills, borders, number formats, layout, print setup) and leaves every value and formula untouched.

## Scope & Handoffs

This skill changes how the workbook *looks*, never what it *computes*. If the request is to convert hard-coded total rows into live `SUM`/`SUBTOTAL`/`SUMIF` formulas, that's a different job — hand off to **`excel-formula-refresh`**. The two pair naturally: refresh the totals first so the numbers are live, then run this skill to make it presentable.

## Required Inputs

- Description of the Excel file (or the file itself)
- Intended audience (internal review vs. client-facing) — sets how far to push polish and print setup
- Any firm-specific formatting overrides (if the firm departs from the reference below)

## Workflow

1. **Assess current state across all sheets** — Understand the structure of each sheet in the workbook: header rows, data rows, total rows, number of columns, and any existing formatting. Apply the standardization to every sheet unless the user specifies a subset.
2. **Apply header formatting** — Use the Firm Formatting Reference below: section headers get the dark-blue fill with white bold text; column headers get the soft-blue fill with bold text. Freeze the header row.
3. **Apply number formatting** — Use the formats specified in the Firm Formatting Reference (currency, negatives, percentages, dates). Consistent across all data columns.
4. **Apply total and subtotal row formatting** — Total rows: soft-green fill, bold, top=medium border, bottom=double border. Subtotal rows: light-gray fill, bold, bottom=thin border. Data rows stay white.
5. **Standardize column widths** — Auto-fit or set consistent widths. No truncated text.
6. **Apply font and style standards** — Calibri 10pt for data, 10pt bold for column headers, 11pt white bold for section headers, 9pt gray italic for notes. No mixed fonts.
7. **Set print area and page setup** — If the report will be printed or exported to PDF: set print area, landscape if wide, fit to page, add header/footer with client name and date.
8. **Produce instructions or VBA** — Output either step-by-step instructions or a VBA macro that applies the formatting.

## Firm Formatting Reference

This is the firm's standard look for client-facing and internal Excel deliverables. Apply these defaults unless the user specifies overrides. Limit fills to structural rows — data rows stay white.

**Color palette and typography:**

| Element | Fill | Font | Border |
|---------|------|------|--------|
| Section headers | #1F4E79 (dark blue) | White, bold, 11pt | — |
| Column headers | #D6E4F0 (soft blue) | Bold, 10pt | — |
| Total rows | #E2EFDA (soft green) | Bold | top=medium, bottom=double |
| Subtotal rows | #F2F2F2 (light gray) | Bold | bottom=thin |
| Flagged / callout items | #FFF2CC (soft yellow) | Bold | — |
| **Data rows** | **No fill (white)** | Normal, 10pt | — |
| Negative values | No fill | Red font (#C00000) | — |
| Notes / comments | No fill | Gray italic (#666666), 9pt | — |

**Number formats:**
- Currency: `$#,##0` (use `$#,##0.00` only when cents matter to the audience)
- Currency with negatives in parentheses: `$#,##0;($#,##0)`
- Percentages: `0.0%`
- Integers / counts: `#,##0`
- Dates: `m/d/yyyy` (or match the client's prevailing convention)

**Structure:**
- Freeze the header row; freeze the first column as well if the report is wide
- Auto-fit column widths; widen to eliminate truncation
- Landscape + fit-to-page for print/PDF when the report is wide
- Avoid merged cells in data rows (they break sort and filter)

**Consistency:**
- Apply the same palette, fonts, and number formats to every sheet in the workbook
- When sheets differ in structure (summary vs. detail), keep the palette consistent but adapt layout per sheet

## Control Points

- **Client-facing reports** — Confirm the content is final and correct before applying formatting. Polish makes a report look authoritative, which makes content errors harder to catch — nobody scrutinizes numbers that are already dressed up for the client. Formatting comes last, after the numbers are right.

## Red Flags

- Report has merged cells that will interfere with consistent formatting
- Multiple sheets with inconsistent structures requiring different formatting logic

## Output Format

Depending on what's most useful:
1. **Step-by-step instructions** — Numbered list of formatting steps to apply manually
2. **VBA macro** — A ready-to-run macro that applies the formatting automatically
3. **Format specification** — A reference table of formatting rules to apply
4. **Bundled helper script** — When you have the `.xlsx` file itself and openpyxl is available, run `scripts/format_report.py` to apply the Firm Formatting Reference programmatically: `python format_report.py input.xlsx [output.xlsx]`. It writes a new formatted workbook (defaults to `<input>-formatted.xlsx`, never overwriting the original), detects header/total/subtotal/note rows heuristically (tunable constants at the top of the file — not hard-coded to one layout), and enforces the safety constraint by asserting every cell value and formula is unchanged before saving. Use it for a fast, consistent pass; fall back to instructions or VBA when the file isn't in hand or the layout needs manual judgment.

## Safety Constraints

- Formatting only — never change a cell's value or formula. A restyle that silently alters a number turns a cosmetic task into a data error that ships to the client. If a value looks wrong, flag it; don't fix it here.
- Note any merged cells or structural issues that need to be resolved before formatting can be applied cleanly, rather than working around them silently.
