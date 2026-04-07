---
name: tax-workpapers
version: 1.0.0
description: |
  Build tax work papers that summarize 1099 activity (INT, DIV, B, R, NEC, MISC),
  SSA-1099, and Schedule K-1 estimates (1065, 1120-S, 1041) into a single Excel
  workbook for tax return preparation. Works for any entity type — individuals
  (1040), partnerships (1065), S-corps (1120-S), trusts (1041), and investment
  funds. Handles consolidated brokerage statements, wash sales, bond amortization,
  state withholding, and incremental document arrival.
trigger: |
  "tax work papers", "tax workpapers", "1099 summary", "K-1 summary",
  "capital gains work papers", "tax return prep", "summarize 1099s",
  "pull together 1099 and K-1", "compile tax documents", "tax season workpapers",
  "brokerage statement summary", "build the workpapers", "fund workpapers",
  "partnership workpapers", "investment fund 1099s"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: all-staff
---

# Tax Work Papers: 1099 & K-1 Workbook Builder

## Purpose

Build a professional Excel workbook that summarizes all 1099 and K-1 source
documents into structured tabs ready for tax return data entry. Works for any
entity type — individuals (1040), partnerships and investment funds (1065),
S-corporations (1120-S), and trusts/estates (1041). This is the bridge between
raw source documents and the tax return — every number on the return should
trace back to a cell in these workpapers.

## Required Inputs

- **Entity name and TIN** — whose return these workpapers support
- **Return type** — 1040, 1065, 1120-S, 1041, or other (determines which tabs
  are relevant and how K-1s flow)
- **Tax year** — confirm before extracting any data
- **Source document folder** — path containing 1099 PDFs, K-1 PDFs, and/or
  brokerage statements
- **Prior-year workpapers** (optional) — for comparison and completeness checking
- **Expected document list** (optional) — from `firm-stack:tax-info-request` or
  prior-year return; used to flag missing documents

### Entity Type Determines Tab Selection

Not all tabs apply to every return type. Use this guide:

| Tab | 1040 (Individual) | 1065 (Partnership/Fund) | 1120-S (S-Corp) | 1041 (Trust) |
|-----|:--:|:--:|:--:|:--:|
| 1099-INT | Y | Y | Y | Y |
| 1099-DIV | Y | Y | Y | Y |
| 1099-B | Y | Y | Y | Y |
| 1099-R | Y | - | - | Y |
| 1099-NEC | Y | Y | Y | - |
| 1099-MISC | Y | Y | Y | Y |
| SSA-1099 | Y | - | - | - |
| K-1 (1065) | Y (received) | Y (received from underlying investments) | Y (received) | Y (received) |
| K-1 (1120-S) | Y (received) | - | - | Y (received) |
| K-1 (1041) | Y (received) | - | - | - |
| K-1 Issued | - | Y (issued to partners) | Y (issued to shareholders) | Y (issued to beneficiaries) |

**Partnership / investment fund specifics:**
- Partnerships receive K-1s from underlying fund-of-fund investments — these go
  on the K-1 (1065) tab as received K-1s
- Partnerships also **issue** K-1s to their own partners — add a "K-1 Issued"
  tab if preparing workpapers for a 1065 return, summarizing what flows out to
  each partner
- Investment funds often have many brokerage accounts across multiple custodians
  with heavy 1099-B activity — the capital gains tab will be the primary focus
- Fund expense allocations (management fees, fund admin, audit) should be noted
  on a separate row in the 1099-B tab or a dedicated section

---

## Critical Principles

### Formulas Over Hard-Coded Values

This is the single most important rule. Tax work papers are reviewed and revised
multiple times during tax season. If a value changes, every downstream cell that
depends on it should update automatically.

- **Every total, subtotal, and summary cell MUST use a formula** (SUM, cross-sheet
  references, `=C-D`, etc.) — never a static number.
- **Input cells** (amounts transcribed from source documents) are the only cells
  that should contain hard-coded numbers.
- **Cross-sheet references** should pull from the detail sheets into the summary
  sheet (e.g., `='1099-INT'!B16`). Corrections on a detail tab automatically
  flow to the summary.
- **Gain/Loss columns** on the 1099-B sheet should use `=Proceeds - Cost Basis`
  formulas (and `- Wash` when applicable), not the pre-computed gain from the
  source document.

### Entity Discipline

Only include accounts that belong to the entity named on the work papers. 1099
PDFs from the same custodian sometimes cover multiple entities (e.g., an LLC and
its members). Verify the account name/TIN on each source document matches the
entity before adding it to the workbook.

### Color Coding (Financial Model Convention)

- **Blue font**: Hard-coded inputs transcribed from source documents
- **Black font**: All formulas and calculations
- **Yellow fill**: Placeholders where source data is missing or estimated

---

## Workbook Structure

Create one `.xlsx` workbook with these tabs. Only include tabs that have data —
skip empty form types rather than leaving blank tabs.

### Tab: 1099-INT

Summarizes all interest income across custodians.

| Column | Content |
|--------|---------|
| A | Custodian / Account |
| B | Interest Income (Box 1) |
| C | Tax-Exempt Interest (Box 8) |
| D | Tax-Exempt Bond Premium (Box 13) |
| E | Bond Premium (Box 11) |
| F | Federal Tax Withheld (Box 4) |
| G | State Tax Withheld (Box 17) |
| H | State |
| I | Notes |

- One row per custodian account
- For consolidated 1099s (like Goldman Sachs with multiple sub-accounts), break
  out each sub-account on its own row with the account number in the label
- **Total row** at bottom: `=SUM()` formulas for each numeric column
- The Notes column should indicate the source form

### Tab: 1099-DIV

Summarizes all dividend income across custodians.

| Column | Content |
|--------|---------|
| A | Custodian / Account |
| B | Ordinary Dividends (Box 1a) |
| C | Qualified Dividends (Box 1b) |
| D | Capital Gain Distributions (Box 2a) |
| E | Nondividend Distributions (Box 3) |
| F | Section 199A Dividends (Box 5) |
| G | Exempt-Interest Dividends (Box 12) |
| H | Specified Private Activity Bond Int (Box 13) |
| I | Foreign Tax Paid (Box 7) |
| J | Federal Tax Withheld (Box 4) |
| K | State Tax Withheld (Box 16) |
| L | State |
| M | Notes |

- Total row with `=SUM()` formulas
- **Validation row** below totals: `=IF(C_total > B_total, "ERROR: QDI > Ord", "OK")`
  — qualified dividends must never exceed ordinary dividends

### Tab: 1099-B (Capital Gains)

This is the most complex tab. Summarizes all capital gains and losses.

| Column | Content |
|--------|---------|
| A | Custodian / Account |
| B | Box / Category |
| C | Proceeds |
| D | Cost Basis |
| E | Wash Sale Adjustment |
| F | Gain / (Loss) — **ALWAYS a formula** |
| G | Term (Short-Term, Long-Term, Ordinary, Expense) |
| H | Notes |

**Row-level guidance:**

- One row per custodian + term + box combination (e.g., "GS ADV — Box A ST
  Covered" and "GS ADV — Box A LT Covered" are separate rows)
- **Gain formula**: `=C-D` when no wash sale; `=C-D-E` when wash sale is present
  (wash stored as a negative number so subtracting it adds back the disallowed
  loss)
- When a custodian embeds the wash adjustment in the reported basis, leave
  column E empty, use `=C-D`, and note "Wash sale adj $X included in basis"

**Bond market discount / amortization:**

- Bonds sold at a market discount may generate ordinary income under IRC 1276
  rather than capital gain. If the 1099-B supplemental detail shows market
  discount amounts, add a note section below the summary.
- Bonds reported under the "ordinary" or "bond method" category should get
  their own row with Term = "Ordinary"

**Capital Gains Summary section** (below the detail rows):

| Row | Formula |
|-----|---------|
| Total Short-Term | `=SUM` of all ST gain cells |
| Total Long-Term | `=SUM` of all LT gain cells |
| Total Ordinary | `=SUM` of ordinary gain cells |
| Total Net | `=ST + LT + Ordinary` |
| Investment Mgmt Fees | Reference to fee row (memo line) |

### Tab: 1099-R

Summarizes retirement distributions.

| Column | Content |
|--------|---------|
| A | Payer / Account |
| B | Gross Distribution (Box 1) |
| C | Taxable Amount (Box 2a) |
| D | Taxable Amount Not Determined (Box 2b) |
| E | Distribution Code (Box 7) |
| F | IRA/SEP/SIMPLE (Box 7 checkbox) |
| G | Federal Tax Withheld (Box 4) |
| H | State Tax Withheld (Box 14) |
| I | State |
| J | Notes |

- Distribution code is critical — it determines tax treatment (e.g., Code 1 =
  early distribution + 10% penalty; Code G = direct rollover; Code 7 = normal)
- Flag Roth conversions (Code 2 or Code 7 with Roth rollover) — these need
  special treatment on Form 8606
- Total row with `=SUM()` for dollar columns

### Tab: 1099-NEC

Summarizes nonemployee compensation.

| Column | Content |
|--------|---------|
| A | Payer |
| B | Nonemployee Compensation (Box 1) |
| C | Federal Tax Withheld (Box 4) |
| D | State Tax Withheld (Box 5) |
| E | State |
| F | Notes |

- Flag if any NEC income may be subject to SE tax vs. not (e.g., director fees,
  consulting vs. one-time payments)
- Total row with `=SUM()`

### Tab: 1099-MISC

Summarizes miscellaneous income.

| Column | Content |
|--------|---------|
| A | Payer / Account |
| B | Rents (Box 1) |
| C | Other Income (Box 3) |
| D | Federal Tax Withheld (Box 4) |
| E | Notes |

- Note the nature of Box 3 income (structured note auto-calls, substitute
  payments, incentive bonuses, etc.)

### Tab: SSA-1099

Summarizes Social Security benefits.

| Column | Content |
|--------|---------|
| A | Recipient |
| B | Total Benefits Paid (Box 3) |
| C | Benefits Repaid (Box 4) |
| D | Net Benefits (Box 5) — **formula: `=B-C`** |
| E | Federal Tax Withheld (Box 6) |
| F | Notes |

### Tab: K-1 (1065)

Summarizes all Schedule K-1 (Form 1065) partnership income. One column per
partnership, with a TOTAL column using `=SUM()` across all partnerships.

**Rows to include** (include a row if any K-1 reports it):

- Box 1: Ordinary Business Income
- Box 2: Net Rental Real Estate Income (Loss)
- Box 5: Interest Income
- Box 6a: Ordinary Dividends
- Box 6b: Qualified Dividends
- Box 8: Net ST Capital Gain (Loss)
- Box 9a: Net LT Capital Gain (Loss)
- Box 11A: Other Portfolio Income
- Box 11C: Section 1256 Contracts
- Box 11S: Non-Portfolio Capital Gain (Loss)
- Box 13A: Charitable Contributions
- Box 13H: Investment Interest Expense
- Box 13L/ZZ: Other Deductions
- Box 13AE: Portfolio Deductions
- Box 19A: Distributions
- Box 20A: Investment Income
- Box 20B: Investment Expenses
- Box 20N: Business Interest Expense
- Box 20Z: Section 199A Information (note "See stmt" if applicable)
- Box 21: Foreign Taxes Paid

Note at top if any K-1s are estimates vs. final.

### Tab: K-1 (1120-S)

Summarizes all Schedule K-1 (Form 1120-S) S-corporation income. Same column-
per-entity layout as the 1065 tab.

**Rows to include:**

- Box 1: Ordinary Business Income (Loss)
- Box 2: Net Rental Real Estate Income (Loss)
- Box 3: Other Net Rental Income (Loss)
- Box 4: Interest Income
- Box 5a: Ordinary Dividends
- Box 5b: Qualified Dividends
- Box 7: Royalties
- Box 8a: Net ST Capital Gain (Loss)
- Box 9a: Net LT Capital Gain (Loss)
- Box 10: Net Section 1231 Gain (Loss)
- Box 12A: Charitable Contributions
- Box 12G: Investment Interest Expense
- Box 13A: Low-Income Housing Credit
- Box 14A: Net Earnings from Self-Employment (rare for S-corps)
- Box 16A: Tax-Exempt Interest Income
- Box 16B: Other Tax-Exempt Income
- Box 16C: Nondeductible Expenses
- Box 16D: Distributions
- Box 17A: Investment Income
- Box 17B: Investment Expenses
- Box 17V: Section 199A — QBI / W-2 Wages / UBIA (note "See stmt")

### Tab: K-1 (1041)

Summarizes all Schedule K-1 (Form 1041) trust/estate income. Same column-per-
entity layout.

**Rows to include:**

- Box 1: Interest Income
- Box 2a: Ordinary Dividends
- Box 2b: Qualified Dividends
- Box 3: Net ST Capital Gain
- Box 4a: Net LT Capital Gain
- Box 4b: 28% Rate Gain
- Box 5: Other Portfolio and Nonbusiness Income
- Box 6: Ordinary Business Income
- Box 7: Net Rental Real Estate Income
- Box 9: Directly Apportioned Deductions
- Box 10: Estate Tax Deduction
- Box 11: Final Year Deductions (excess deductions on termination)
- Box 13: Credits and Credit Recapture
- Box 14A: Tax-Exempt Interest
- Box 14B: Foreign Taxes

### Tab: K-1 Issued (1065 / 1120-S / 1041 returns only)

When preparing workpapers for a partnership, S-corp, or trust return, this tab
summarizes the K-1s the entity **issues** to its partners/shareholders/beneficiaries.
This is the outbound side — what flows from the entity to its owners.

| Column | Content |
|--------|---------|
| A | K-1 Line Item |
| B through G (or more) | One column per partner/shareholder/beneficiary |
| Last column | TOTAL — `=SUM()` across all owner columns |

Rows mirror the applicable K-1 tab structure (1065, 1120-S, or 1041 boxes).

The total column should tie to the entity's return lines. For example, the sum
of all partners' Box 1 ordinary income should equal the partnership's Form 1065
page 1 ordinary income.

### Tab: Document Tracker

Tracks which source documents have been incorporated.

| Column | Content |
|--------|---------|
| A | Document / Custodian |
| B | Form Type (1099-INT, K-1, etc.) |
| C | Date Received |
| D | Status (Incorporated / Pending / Corrected / Superseded) |
| E | Incorporated By |
| F | Notes |

This tab supports incremental document arrival. When new documents come in,
add rows and update the detail tabs rather than rebuilding the workbook.

### Tab: Tax Return Summary

Combines 1099 and K-1 totals into a single view for tax return data entry.
Adapt the rows to the return type — not all rows apply to all entity types.

| Column | Content |
|--------|---------|
| A | Income Category |
| B | 1099 Amount — **cross-sheet formula** (e.g., `='1099-INT'!B16`) |
| C | K-1 Amount — **cross-sheet formula** |
| D | Combined Total — **formula**: `=B+C` |

**Common rows (all entity types):**

- Interest Income (1099-INT + K-1 interest boxes)
- Ordinary Dividends (1099-DIV + K-1 dividend boxes)
- Qualified Dividends (1099-DIV + K-1 QDI boxes)
- Short-Term Capital Gains (1099-B + K-1 ST boxes)
- Long-Term Capital Gains (1099-B + K-1 LT + cap gain distributions)
- Ordinary Gains (1099-B ordinary rows)
- Other Income (1099-MISC + K-1 other income)
- Foreign Tax Paid (1099-DIV + K-1 foreign tax)

**Individual (1040) additional rows:**

- Retirement Distributions — Gross / Taxable (1099-R)
- Social Security — Net Benefits (SSA-1099)
- Nonemployee Compensation (1099-NEC)
- Rental Income (K-1 rental boxes)
- Section 199A / QBI (K-1 199A boxes — "See stmt")
- Charitable Contributions (K-1 charitable boxes)

**Partnership / Fund (1065) additional rows:**

- Management Fees / Fund Expenses (memo)
- Net Investment Income (for fund reporting)
- Rental Income (if applicable)
- Section 199A / QBI (if applicable)
- Total allocable to partners (should tie to K-1 Issued tab totals)

**Withholding Summary section:**

| Row | Formula |
|-----|---------|
| Federal Withholding — 1099s | `=SUM` of all federal withholding columns across 1099 tabs |
| Federal Withholding — 1099-R | `='1099-R'!G_total` (1040 only) |
| State Withholding (by state) | `=SUM` of state withholding columns, grouped by state |

Every cell in this tab must be a formula — never transcribed from the detail sheets.

---

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

4. **Build the workbook** — Use `openpyxl` to create the workbook programmatically.
   Apply all formatting standards (see below). Save to `/tmp/` first, then copy
   to the user's folder as a final step. Use version suffix if a file already
   exists (e.g., `_v2.xlsx`). **Gate**: Workbook created without errors.

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

---

## Incremental Updates

Documents arrive in waves during tax season. When new documents come in after
the initial workbook is built:

1. Open the existing workbook (read it with openpyxl, `data_only=False` to
   preserve formulas)
2. Add new rows to the appropriate detail tabs
3. Extend `=SUM()` ranges to include the new rows
4. Update the Document Tracker tab
5. Increment the version suffix
6. Re-run validation checks

Do NOT rebuild the workbook from scratch unless the user explicitly asks.
Appending preserves any manual annotations the preparer may have added.

---

## Formatting Standards

- **Headers**: White bold text on blue fill (#4472C4)
- **Number format**: `#,##0.00;(#,##0.00)` (parentheses for negatives)
- **Column widths**: Auto-fit to content, minimum 14 for money columns
- **Freeze panes**: Freeze below the header row
- **Borders**: Thin borders on all data cells
- **Alternating row fill**: Light green (#E2EFDA) on even rows
- **Summary totals**: Bold, double-underline border on the net total row
- **Page setup**: Landscape, fit to width

---

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

Single `.xlsx` workbook saved to the user's specified folder. File naming
convention: `{EntityName}_{TaxYear}_Workpapers.xlsx` (e.g.,
`Smith_2025_Workpapers.xlsx`). Append `_v2`, `_v3` for subsequent versions.

Tabs included (only those with data — skip empty form types):
1. 1099-INT
2. 1099-DIV
3. 1099-B
4. 1099-R
5. 1099-NEC
6. 1099-MISC
7. SSA-1099
8. K-1 (1065) — K-1s received from partnerships
9. K-1 (1120-S) — K-1s received from S-corps
10. K-1 (1041) — K-1s received from trusts/estates
11. K-1 Issued — K-1s issued to partners/shareholders/beneficiaries (1065/1120-S/1041 returns only)
12. Document Tracker
13. Tax Return Summary

## Safety Constraints

- Do not file, submit, or transmit anything — workpapers are internal preparer
  documents only.
- Do not overwrite an existing workbook without creating a versioned copy first.
- Do not discard or move source PDFs.
- Flag discrepancies but do not resolve them — resolution is the preparer's job.
- Do not assume tax treatment for ambiguous items (e.g., whether a 1099-R is a
  rollover or taxable distribution) — note the distribution code and let the
  preparer determine treatment.

---

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
