---
name: excel-report-format
version: 1.0.0
description: |
  Standardize an Excel report to the firm's look and feel. Applies consistent
  formatting: fonts, header styles, number formats, column widths, freeze panes,
  and any firm-specific design standards to produce a polished, client-ready report.
trigger: |
  "format this report", "standardize this Excel", "apply firm formatting",
  "make this look professional", "clean up this spreadsheet", "Excel formatting"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Excel Report Format: Standardize to Firm Look and Feel

## Purpose

Apply consistent, professional formatting to an Excel report so that all client-facing output looks uniform and polished. Eliminates ad-hoc formatting from system exports and one-off spreadsheets.

## Required Inputs

- Description of the Excel file (or the file itself)
- Intended audience (internal review vs. client-facing)
- Any firm-specific formatting standards (if known)

## Workflow

1. **Assess current state** — Understand the report structure: header rows, data rows, total rows, number of columns, and any existing formatting.
2. **Apply header formatting** — Bold column headers, apply background color (firm standard or a clean neutral), freeze the header row.
3. **Apply number formatting** — Currency columns formatted as `$#,##0` or `$#,##0.00`. Percentages as `0.0%`. Integers without decimals. Consistent across all data columns.
4. **Apply total row formatting** — Bold total rows, top border above totals, consistent with the rest of the sheet.
5. **Standardize column widths** — Auto-fit or set consistent widths. No truncated text.
6. **Apply font and style standards** — Consistent font (e.g., Calibri 10pt for data, 11pt for headers). No mixed fonts.
7. **Set print area and page setup** — If the report will be printed or exported to PDF: set print area, landscape if wide, fit to page, add header/footer with client name and date.
8. **Produce instructions or VBA** — Output either step-by-step instructions or a VBA macro that applies the formatting.

## Control Points

- **Client-facing reports** — Confirm the report is ready for client delivery before applying final formatting (content errors are harder to spot in a nicely formatted report).

## Red Flags

- Report has merged cells that will interfere with consistent formatting
- Multiple sheets with inconsistent structures requiring different formatting logic

## Output Format

Depending on what's most useful:
1. **Step-by-step instructions** — Numbered list of formatting steps to apply manually
2. **VBA macro** — A ready-to-run macro that applies the formatting automatically
3. **Format specification** — A reference table of formatting rules to apply

## Safety Constraints

- Do not modify formulas or data values — formatting only.
- Note any merged cells or structural issues that need to be resolved before formatting is applied.
