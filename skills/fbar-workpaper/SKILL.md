---
name: fbar-workpaper
version: 1.1.0
description: |
  Build Excel FBAR workpapers (FinCEN Form 114) from foreign bank account source
  documents — scanned statements, tax withholding certificates, multi-currency accounts.
  Produces a 4-sheet workpaper: summary, account detail, interest income (Schedule B /
  Form 1116), and open-items checklist. Use whenever a client discloses money held
  outside the U.S. or hands over foreign bank paperwork — "client has an account
  overseas", "do we need an FBAR", "foreign account reporting", "they had a bank account
  in [country]", "build the FBAR workpaper", "foreign interest to report" — even if they
  never say "FBAR" or "FinCEN 114." Also covers the related U.S. reporting the same
  documents feed: Schedule B foreign accounts, Form 1116 foreign tax credit, and Form
  8938 (FATCA) threshold screening.
trigger: |
  "FBAR", "FinCEN 114", "foreign bank account", "foreign accounts", "BSA filing",
  "Report of Foreign Bank", "foreign financial account", "FBAR workpaper",
  "foreign account disclosure", "foreign interest income", "Schedule B foreign",
  "Form 1116", "FATCA", "Form 8938", "foreign bank statement", "money overseas",
  "offshore account", "account in [country]", "do we need to report a foreign account",
  "did they file an FBAR"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# FBAR Workpaper Builder

## Purpose

Build a professional Excel workpaper documenting foreign bank accounts for FinCEN
Form 114 (FBAR) filing and related U.S. income reporting (Schedule B, Form 1116,
Form 8938). Use whenever a client discloses non-U.S. financial accounts, provides
foreign bank statements, or receives foreign tax withholding certificates.

FBAR is a high-penalty compliance item, which is why every number in these workpapers
must trace directly to a source document — a figure that can't be tied out is a figure
that can't be defended. Penalty for non-willful failure: a $10,000 statutory base, inflation-adjusted (roughly
$16,536 per violation for 2025 assessments) and applied per FBAR form — not per account
(Bittner v. United States, 2023). Penalty for willful failure: the greater of the
inflation-adjusted $100,000 base (roughly $165,353) or 50% of the highest account value
anytime during the year. Confirm the current-year adjusted figures before relying on them.

## Required Inputs

- **Client name and TIN** — whose return the workpapers support
- **Tax year** — confirm before extracting any data
- **Foreign bank statement(s)** — scanned PDFs or image files
- **Foreign tax withholding certificate(s)** — if foreign tax was withheld on interest
- **Filing status** — determines Form 8938 thresholds (single vs. MFJ)
- **Prior-year FBAR** (optional) — for account continuity and completeness checking

If a required input is missing, ask before proceeding. A workpaper built on an
incomplete account list understates the client's exposure, and the gap surfaces only
after filing.

## Workflow

### Phase 1 — Confirm Scope

1. Confirm client name, TIN, tax year, and filing status before touching any documents.
2. Identify all accounts disclosed. For each: bank name, country, account number,
   account type (deposit, securities, other), and whether the client has ownership
   vs. signatory-only authority.
3. Ask if any accounts were opened or closed during the year — these still require
   FBAR reporting if the aggregate threshold was met at any point.

**Gate:** Client name, TIN, tax year, and complete account list confirmed before proceeding.

---

### Phase 2 — Extract Source Documents

Foreign bank statements are almost always scanned PDFs, so convert them to images for
vision-based extraction and pull each account's balances, sub-account detail, and any
tax-certificate income. The conversion snippet and the field-by-field extraction targets
are in **`references/workpaper-layout.md`**.

**Gate:** All source documents accounted for. If a document is missing (e.g., no
annual statement showing maximum balance), flag it as an open item before continuing.

---

### Phase 3 — Establish Exchange Rates

Use two different rates — do not mix them. They measure different things, and using a
balance rate on income (or vice versa) produces figures that won't reconcile to either form.

| Purpose | Rate | Source |
|---|---|---|
| FBAR balance conversion | Treasury FMS year-end rate (12/31/XX) | https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/ |
| Interest income (Schedule B) | IRS annual average rate | https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates |

- Bank statements often include their own rate — use as a cross-check only, not the
  official rate.
- If the official IRS annual average rate is not yet published (common for extension
  filers), note "TBD — pending IRS release" and flag in open items.

**Gate:** Both rates identified or flagged as TBD before converting any amounts.

---

### Phase 4 — Build the Workpaper (4 Sheets)

Build a single `.xlsx` workbook with four sheets:

1. **FBAR Summary** — taxpayer block, one row per account, aggregate USD total, threshold
   note (aggregate >$10,000 USD at any point during the year triggers filing), filing
   instructions.
2. **Account Detail** — one section per account: institution master, year-end balances,
   sub-account/deposit detail, annual averages.
3. **Interest Income (Schedule B / Form 1116)** — income by category at the IRS annual
   average rate, foreign tax withheld, U.S. reporting treatment notes.
4. **Open Items Checklist** — the standard nine-item list, each marked resolved or pending.

USD equivalents are formulas (`=E*F`, `=B*C`), never hard-coded values, so the workpaper
recomputes when a rate is corrected. The full column-by-column layout for every sheet,
plus the standard open-items list, is in **`references/workpaper-layout.md`** — read it
when laying out the sheets.

**Gate:** Open items reviewed with preparer before delivering workpaper.

---

### Phase 5 — Validate

Before delivering, verify:

- Every balance and income amount traces to a specific source document page
- Maximum balance is confirmed — not assumed to equal year-end balance
- Exchange rates are the correct official rates (not bank rates)
- USD equivalents are formulas, not hard-coded values
- Aggregate threshold analysis is complete (all accounts combined)
- Form 8938 threshold assessed separately from FBAR threshold
- Open items list is complete and has been reviewed

**Gate:** All validation checks pass or exceptions documented in open items.

---

### Phase 6 — Deliver

Save workpaper to client folder. File naming: `{ClientName}_{TaxYear}_FBAR.xlsx`
(e.g., `Smith_2025_FBAR.xlsx`). Append `_v2`, `_v3` for revisions.

Report to preparer:
- Accounts included and aggregate USD total
- Maximum balance status (confirmed vs. flagged)
- Open items count and which require client follow-up
- Any amounts needing Form 1116 or Form 8938 follow-up

---

## Control Points

These are hard stops. Do not proceed past them without explicit confirmation.

1. **Aggregate threshold not clearly met** — If it is unclear whether the $10,000
   threshold was crossed (e.g., only year-end balances available and they are near
   the threshold), stop and flag. FBAR is required if the threshold was exceeded at
   ANY point during the year.

2. **Maximum balance unknown** — If only year-end balance is available and the
   monthly averages suggest the balance may have been higher at some point, flag as
   open item and do not complete the FBAR Summary until confirmed.

3. **Multiple accounts, unclear ownership** — Signatory-only accounts still require
   FBAR reporting. If ownership vs. signatory authority is ambiguous, confirm with
   client before completing the workpaper.

4. **Form 8938 threshold exceeded** — If aggregate foreign financial assets exceed
   $50,000 ($100,000 MFJ) at year-end or $75,000 ($150,000 MFJ) at any point,
   flag for Form 8938 preparation in addition to FBAR. These are separate filings
   with different thresholds and penalties.

5. **Corrected or amended source document** — If a corrected bank statement or tax
   certificate is received after the workpaper is built, stop and rebuild from the
   corrected document. Note the correction in the Open Items Checklist.

---

## Red Flags

Pause and surface to the preparer:

- Year-end balance close to $10,000 threshold — maximum balance may have crossed it
- Foreign tax certificate shows "Foreign Resident" (or equivalent) exemption — verify
  treaty status and U.S. reporting treatment; exempt from foreign tax ≠ exempt from
  U.S. Schedule B
- Multiple sub-account deposit numbers — each may be a separate FBAR account;
  confirm treatment
- Account opened or closed mid-year — still reportable; check for maximum balance
  during the period the account was open
- Withholding rate on certificate does not match expected treaty rate — possible
  over-withholding; flag for Form 1116 and possible refund claim
- Prior-year FBAR included an account not present in current-year documents —
  confirm account was closed or confirm it should still be reported

---

## Output Format

Single `.xlsx` workbook with 4 sheets, in order:

1. FBAR Summary
2. Account Detail
3. Interest Income (Schedule B / Form 1116)
4. Open Items Checklist

Naming convention: `{ClientName}_{TaxYear}_FBAR.xlsx`. Formatting per
`firm-stack:excel-report-format`; FBAR-specific override: open-items rows use peach
fill (#FDE8D8), section headers navy (#2B4770). Full layout in
`references/workpaper-layout.md`.

---

## Safety Constraints

- Do not transmit, submit, or file anything to BSA E-Filing or any government system.
  Workpapers are internal preparer documents only.
- Do not confirm a maximum balance that has not been verified from source documents.
  Year-end balance is not the maximum balance.
- Do not overwrite an existing workpaper without creating a versioned copy first.
- Do not assume treaty exemption applies without client confirmation of residency status.
- Flag discrepancies but do not resolve them — resolution is the preparer's judgment.
- Do not use bank-provided exchange rates as the official rate for U.S. reporting
  purposes. Always source from Treasury FMS (balances) and IRS (income).

---

## Integration with Other firm-stack Skills

- **`firm-stack:excel-report-format`** — Apply for all formatting standards.
  FBAR workpapers follow firm palette with the peach open-items override noted above.
- **`firm-stack:tax-workpapers`** — If the client also has domestic 1099 activity,
  the interest income from Sheet 3 of this workpaper feeds into the 1099-INT tab
  of tax-workpapers. Cross-reference to avoid double-counting.
- **`firm-stack:1040-review`** — Schedule B Part III, Form 1116, and Form 8938
  are reviewed as part of 1040-review. The FBAR workpaper is the source document
  trail for those forms.
