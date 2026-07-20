---
name: tax-workpapers
version: 1.1.0
description: |
  Build an Excel workbook that summarizes a client's 1099 activity (INT, DIV, B,
  R, NEC, MISC), SSA-1099, and Schedule K-1s (1065, 1120-S, 1041) into structured,
  formula-linked tabs ready for tax return data entry. Works for any return type —
  individuals (1040), partnerships and investment funds (1065), S-corps (1120-S),
  and trusts/estates (1041). Handles consolidated brokerage statements, wash sales,
  bond amortization, state withholding, and documents that arrive in waves.
  Use this whenever someone needs raw tax source documents turned into workpapers —
  even if they don't say "workpapers": "summarize these 1099s," "pull the brokerage
  statements into Excel," "get the return ready to input," "organize the tax docs,"
  "build the capital gains schedule," or "compile the K-1s." This is the bridge
  between the source PDFs and the return.
trigger: |
  "tax work papers", "tax workpapers", "1099 summary", "K-1 summary",
  "capital gains work papers", "capital gains schedule", "tax return prep",
  "summarize 1099s", "summarize the brokerage statements", "pull together 1099 and K-1",
  "compile tax documents", "organize the tax docs", "get the return ready to input",
  "tax season workpapers", "brokerage statement summary", "build the workpapers",
  "fund workpapers", "partnership workpapers", "investment fund 1099s"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: all-staff
---

# Tax Work Papers: 1099 & K-1 Workbook Builder

## Purpose

Turn a client's raw 1099 and K-1 source documents into a professional Excel
workbook whose tabs are structured for tax return data entry. Works for any
entity type — individuals (1040), partnerships and investment funds (1065),
S-corporations (1120-S), and trusts/estates (1041). These workpapers are the
bridge between the source PDFs and the return: every number on the return should
trace back to a cell here, and every cell here should trace back to a source
document.

This produces internal preparer workpapers, not a filing. It does not exercise
tax judgment on ambiguous items — it surfaces them for the preparer.

## Required Inputs

- **Entity name and TIN** — whose return these workpapers support
- **Return type** — 1040, 1065, 1120-S, 1041, or other (determines which tabs
  are relevant and how K-1s flow)
- **Tax year** — confirm before extracting any data; a document from the wrong
  year silently corrupts the workbook
- **Source document folder** — path containing 1099 PDFs, K-1 PDFs, and/or
  brokerage statements
- **Prior-year workpapers** (optional) — for comparison and completeness checking
- **Expected document list** (optional) — from `firm-stack:tax-info-request` or
  prior-year return; used to flag missing documents

The return type drives which tabs to build and how K-1s flow (received vs.
issued). The tab-selection matrix, every tab's column layout, the per-return-type
K-1 box maps, and the Excel formatting standards live in
**`references/workbook-structure.md`** — read it before building the workbook.

## Critical Principles

These three principles are what make the workpapers reviewable and trustworthy.
They apply to every tab.

### Formulas over hard-coded values

Tax workpapers are reviewed and revised repeatedly during the season. If a value
changes, every downstream cell that depends on it should update automatically — a
hard-coded total silently goes stale and the error surfaces only after filing.

- **Every total, subtotal, and summary cell uses a formula** (SUM, cross-sheet
  references, `=C-D`, etc.) — never a static number.
- **Input cells** (amounts transcribed from source documents) are the only cells
  that hold hard-coded numbers.
- **Cross-sheet references** pull from the detail sheets into the summary sheet
  (e.g., `='1099-INT'!B16`), so a correction on a detail tab flows through
  automatically.
- **Gain/Loss columns** on the 1099-B sheet use `=Proceeds - Cost Basis`
  (and `- Wash` when applicable), never the pre-computed gain from the source
  document.

### Entity discipline

Only include accounts that belong to the entity named on the workpapers. 1099
PDFs from the same custodian sometimes cover multiple entities (e.g., an LLC and
its members), so a mismatched account quietly inflates the wrong return. Verify
the account name/TIN on each source document matches the entity before adding it.

### Color coding (financial model convention)

- **Blue font**: hard-coded inputs transcribed from source documents
- **Black font**: all formulas and calculations
- **Yellow fill**: placeholders where source data is missing or estimated

The blue/black split lets a reviewer see at a glance what was typed in versus
what was computed — a black number that should be blue (or vice versa) is a tell.

## Workflow

1. **Confirm scope** — Entity name, TIN, tax year, source folder path. If an
   expected document list is available (from `firm-stack:tax-info-request` or
   prior-year return), load it for completeness checking. **Gate**: Entity and
   year confirmed before proceeding.

2. **Inventory source documents** — List every PDF in the source folder. Group
   by form type. For consolidated 1099s, note which sub-accounts are included.
   Populate the Document Tracker tab. **Gate**: User confirms the document list
   is complete (or acknowledges what's still outstanding).

3. **Extract data from PDFs** — Read each PDF and extract relevant box amounts.
   For consolidated 1099s with many pages, pay special attention to:
   - **Summary pages** (usually near the front) — totals per sub-account
   - **1099-B broker summaries** — proceeds, basis, gain/loss by category;
     every sub-account with trading activity should appear
   - **Supplemental detail** — per-lot transactions, wash sales, bond
     amortization, market discount
   Common pitfalls: consolidated 1099s may have 5+ sub-accounts (capture all);
   some custodians report wash sales in a separate section; bond market discount
   may only appear in supplemental pages.

4. **Build the workbook** — Use `openpyxl` to create the workbook programmatically,
   following the tab layouts and formatting standards in
   `references/workbook-structure.md`. A bundled helper,
   `scripts/build_workbook.py`, builds the styled skeleton with the firm
   formatting, the blue-input / black-formula color coding, and real `=SUM()`
   total rows already baked in — import its helpers (`add_sheet`, `write_header`,
   `write_data_row`, `write_formula_cell`, `write_sum_total_row`) so you only
   supply the transcribed data, not the scaffolding. Run `python
   scripts/build_workbook.py --demo` to see the API (a 1099-B tab with the
   `=C-D-E` wash-sale column and a K-1 summary tab). Save to `/tmp/` first, then
   copy to the user's folder as a final step. Use a version suffix if a file
   already exists (e.g., `_v2.xlsx`). **Gate**: Workbook created without errors.

5. **Validate** — Run these checks before delivering:
   - LibreOffice headless recalculation to verify formulas
   - Cross-check workbook totals against source PDFs
   - Qualified dividends <= ordinary dividends (per custodian and total)
   - 1099-B gain/loss = proceeds - cost basis - wash (per row)
   - K-1 total row sums match across entities
   - Every input cell has blue font; every total cell is a formula
   - Tax year on every source document matches the declared year
   **Gate**: All validation checks pass or exceptions are documented.

6. **Deliver** — Save final workbook to user's folder. Report summary of what
   was included, any missing documents, and any flagged items.

### Incremental updates

Documents arrive in waves during tax season. When new documents come in after
the initial workbook is built, append rather than rebuild — appending preserves
any manual annotations the preparer added:

1. Open the existing workbook (read it with openpyxl, `data_only=False` to
   preserve formulas)
2. Add new rows to the appropriate detail tabs
3. Extend `=SUM()` ranges to include the new rows
4. Update the Document Tracker tab
5. Increment the version suffix
6. Re-run validation checks

Do not rebuild the workbook from scratch unless the user explicitly asks.

## Control Points

- **Missing source documents** — If the expected document list has items not
  found in the source folder, flag them before building. Do not silently omit.
  Ask the user whether to proceed without them or wait.
- **Entity / TIN mismatch** — If a source document's account name or TIN does
  not match the declared entity, stop and confirm with the user before including
  or excluding it.
- **Corrected forms** — If a corrected 1099 (marked "CORRECTED") is found,
  confirm it should replace the original. Mark the original as "Superseded" in
  the Document Tracker.
- **K-1 estimates vs. finals** — Flag estimate K-1s prominently. When the final
  K-1 arrives, confirm it should replace the estimate.
- **Materiality exceptions** — Any discrepancy between the source document total
  and the workpaper transcription that exceeds $100 requires investigation
  before delivery.

## Red Flags

- Wash sale disallowed loss exceeds cost basis (possible transcription error)
- Qualified dividends exceed ordinary dividends on any row
- Negative gross distribution on a 1099-R
- K-1 loss claimed without basis documentation — note for preparer
- Tax year on a source document does not match the workpaper year
- Consolidated 1099 sub-account missing from workpapers (count mismatch)
- 1099-R distribution code suggests early withdrawal penalty (Code 1) — flag
  for Form 5329 consideration
- PTP K-1 — flag for passive activity limitation and potential UBTI analysis

## Output Format

A single `.xlsx` workbook saved to the user's specified folder. File naming
convention: `{EntityName}_{TaxYear}_Workpapers.xlsx` (e.g.,
`Smith_2025_Workpapers.xlsx`). Append `_v2`, `_v3` for subsequent versions.

Include only the tabs that have data — skip empty form types rather than leaving
blank tabs. The available tabs, in order, are: 1099-INT, 1099-DIV, 1099-B,
1099-R, 1099-NEC, 1099-MISC, SSA-1099, K-1 (1065), K-1 (1120-S), K-1 (1041),
K-1 Issued (1065/1120-S/1041 returns only), Document Tracker, and Tax Return
Summary. See `references/workbook-structure.md` for which tabs apply to each
return type and the layout of each.

Alongside the file, report a short summary: what was included, any missing
documents, and any flagged items.

## Safety Constraints

- Do not file, submit, or transmit anything — workpapers are internal preparer
  documents only.
- Do not overwrite an existing workbook without creating a versioned copy first.
- Do not discard or move source PDFs.
- Flag discrepancies but do not resolve them — resolution is the preparer's job.
- Do not assume tax treatment for ambiguous items (e.g., whether a 1099-R is a
  rollover or taxable distribution) — note the distribution code and let the
  preparer determine treatment.

## Integration with Other firm-stack Skills

- **`firm-stack:tax-info-request`** — Use its output as the expected document
  checklist for Step 1. Missing items become flags in the Document Tracker.
- **`firm-stack:1040-review`** — For individual returns, the completed workpapers
  are the primary source documents that 1040-review cross-references against the
  return. The Tax Return Summary tab maps directly to return lines.
- **`firm-stack:1065-review`** — For partnership/fund returns, the workpapers
  provide the source document trail that 1065-review verifies against the return.
  The K-1 Issued tab should tie to the K-1 allocations reviewed by 1065-review.
- **`firm-stack:1120s-review`** — Same relationship as 1065-review for S-corp
  returns.
- **`firm-stack:1041-review`** — Same relationship for trust/estate returns.
  K-1 Issued tab ties to beneficiary allocation schedules.
