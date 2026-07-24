---
name: 1041-review
version: 1.10.0
description: |
  Cross-reference a completed Form 1041 (fiduciary income tax return) against its
  source documents — the trust instrument, fiduciary accounting, 1099s, and pass-through
  K-1s — to catch errors before filing. Works for grantor, simple, and complex trusts
  and decedent estates during administration.
  Verifies income, deductions, distributable net income (DNI), the income distribution
  deduction, and beneficiary allocations on Schedule K-1; shows the DNI calculation
  explicitly; grades findings by severity; and flags audit-risk items. Use this whenever
  someone wants a trust or fiduciary return checked, tied out, or reviewed before it goes
  out the door — "review the 1041", "check the trust return", "does the DNI tie", "tie the
  K-1s to the distribution deduction", "look over the trust return before we file" — even
  if they don't name the form or say the word "review".
trigger: |
  "review the 1041", "trust return review", "fiduciary return", "grantor trust",
  "1041 cross-reference", "tie out the trust return", "trust K-1 review",
  "check the trust return", "verify the 1041", "does the DNI tie", "check the DNI",
  "distribution deduction", "estate return review", "look over the trust return before we file"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1041 Review: Fiduciary Return Cross-Reference

## Purpose

Catch errors before a Form 1041 is filed. Verify that trust income, deductions, and beneficiary allocations tie to source documents and that the return is consistent with the trust instrument and applicable fiduciary accounting rules.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross income or trust assets to determine whether a variance is acceptable. That approach belongs in financial statement audits, not tax review.

Classify findings by severity (impact + risk) rather than by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, DNI miscalculation, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about or consider low-severity. Severity is for prioritization, not filtering — all findings go in the table. A separate preparer review step decides what to act on; your job at this stage is coverage.

## Required Inputs

- Completed Form 1041 and all schedules (B, D, G, I, J, K-1s — Schedule I is required whenever an income distribution deduction is taken)
- Trust instrument (trust agreement or will)
- Financial statements or fiduciary accounting report for the tax year
- Source documents: 1099s, K-1s from pass-throughs, brokerage statements
- Prior-year return (for carryforwards, excess deductions)
- CCH Axcess Diagnostics report and Input Override Report (if available)

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Detailed procedures for estate-specific items (post-death income splitting, IRD, the 691(c) deduction), the initial-return branch, basis step-up, tax-exempt expense allocation, charitable verification, loss limitations, the separate share rule, final-year mechanics, and ESBTs live in **`references/estate-and-dni-procedures.md`** — read it when the return involves any of them.

1. **Identify entity type** — Confirm whether this is a grantor trust, simple trust, complex trust, or decedent estate. The reporting rules differ materially.
   - **Grantor trust**: Income taxed to grantor; return may be informational only.
   - **Simple trust**: Required to distribute all income; no charitable deduction.
   - **Complex trust**: May accumulate income; may have charitable deduction.
   - **Estate**: Decedent's estate during administration — may elect a fiscal year (trusts are calendar-year), may combine with a revocable trust under an IRC 645 election, and carries the estate-specific checks in the references file: post-death income splitting, income in respect of a decedent, and the IRC 691(c) deduction.
   - **ESBT check**: If Box A shows an electing small business trust, the S-corporation portion is taxed separately at the top rate with **no DNI or distribution deduction for S items** — treating S-corp income as ordinary DNI silently breaks the entire DNI tie-out. See the references file.
2. **Initial-return branch** — If the Initial Return box is checked (or this is the entity's first year): confirm the EIN and entity data; verify the tax-year selection (a fiscal year is available only to estates — a trust on a fiscal year without a 645 election is a finding); verify any IRC 645 election (Form 8855 timely filed; combined trust-and-estate reporting applied only for the election period); confirm required election statements are attached; and expect **no beginning-balance carryovers** — a carryforward on a first-year return needs an explanation. Details in the references file.
3. **Reconcile income to source documents** — Tie interest, dividends, capital gains, and pass-through income to 1099s and K-1s. Confirm the digital-asset question on page 1 is answered and consistent with the source documents — a 1099-DA or crypto activity on custody statements with a "No" answer is a finding. Reconcile any Forms 1099-DA (broker reporting is new; basis may be missing or wrong). Two completeness checks: compare income sources line-by-line to the prior-year return — the cheapest missing-1099 detector — and, for estates and trusts funded at death, verify 1099-B cost basis reflects the **date-of-death step-up**: brokers often carry the decedent's original basis, and inherited property is automatically long-term (procedures in the references file).
4. **Verify deductions** — Confirm fiduciary fees, attorney fees, and other deductions are properly allocated between income and principal per the trust instrument. If tax-exempt income exists, confirm indirect expenses (fiduciary fees especially) are allocated between taxable and tax-exempt income with the computation attached to the return, and the tax-exempt income is disclosed under Other Information on page 2. If a charitable deduction is claimed, verify it under IRC 642(c): authorized by the governing instrument **and** paid from gross income, with the tax-exempt portion disallowed and Form 1041-A filed where required (procedures in the references file).
5. **Verify DNI and distribution deduction** — Show the DNI calculation explicitly: gross income minus deductions allocable to income, with specific exclusion of capital gains allocated to corpus (unless the trust instrument or local law allocates gains to income). Confirm the income distribution deduction ties to actual distributions. For complex trusts, verify the 65-day election (IRC 663(b)) if distributions in the first 65 days of the following year are being treated as current-year distributions.
6. **Verify Schedule K-1 allocations** — Confirm K-1 totals for all beneficiaries sum to the income distribution deduction. Verify each K-1 character of income (ordinary, qualified dividends, capital gains) is correctly allocated. If the governing instrument creates substantially separate and independent shares, apply the **separate share rule (IRC 663(c))** — DNI is computed per share, so the K-1 total can tie to the distribution deduction while the allocation among beneficiaries is wrong (procedures in the references file).
7. **Verify K-1 loss limitations** — For losses arriving on K-1s from pass-throughs, confirm the trust's basis, at-risk, and passive-activity limitations were applied before the loss reached the return. Material participation for a trust turns on the **trustee's** activity — a litigated, fact-heavy area; flag it and hand substantive analysis to `tax-advisor` rather than concluding it here.
8. **Verify tax computation** — Confirm the tax is calculated at trust rates (which compress quickly) or that the income is properly flowed out to beneficiaries.
9. **Verify Schedule I (AMT) and Form 8960 (NIIT)** — Schedule I must be completed whenever an income distribution deduction is taken, regardless of whether AMT is owed — DNI on a minimum-tax basis flows to K-1 Box 12. Trusts hit the 3.8% net investment income tax at the compressed top-bracket threshold (a fraction of the individual thresholds), so nearly every income-retaining trust owes it: confirm Form 8960 is present and the undistributed-NII base is correct.
10. **Verify payments and Form 1041-T** — Tie the payments section to records: estimated payments, extension payment, prior-year overpayment applied, and backup withholding on 1099s. If estimated payments are allocated to beneficiaries, verify the Form 1041-T election — it is irrevocable and must be filed within 65 days after year-end.
11. **Final-year returns** — If this is the entity's final year: confirm remaining DNI is distributed, and unused capital-loss/NOL carryovers and excess deductions pass out to beneficiaries on K-1 Box 11 with character retained (IRC 67(e) AGI-level deductions vs. itemized) — mischaracterized excess deductions change every beneficiary's 1040 (procedures in the references file).
12. **Verify Section 199A / QBI reporting** — Trusts and estates can claim the QBI deduction on Form 8995 or 8995-A for QBI from pass-through interests they hold directly. The fiduciary also reports QBI information to beneficiaries on K-1 Box 13, code P. Confirm:
   - If the trust receives K-1s from pass-through entities (1065 or 1120-S), the QBI components (QBI amount, W-2 wages, UBIA of qualified property, SSTB flag) are properly received and included in the trust's 199A computation.
   - If the trust distributes income to beneficiaries, the QBI allocation between the trust and beneficiaries is correctly computed. The IRC 199A allocation is based on the proportion of DNI distributed vs. retained — consistent with the income distribution deduction.
   - The trust's Form 8995 or 8995-A is present if QBI-eligible income exists and taxable income exceeds zero.
   - K-1 Box 13, code P reports the beneficiary's share of QBI components (QBI, W-2 wages, UBIA, SSTB flag) — these must tie to the trust's overall 199A computation.
   - If the trust is a grantor trust, QBI flows to the grantor's 1040 — confirm the grantor-trust K-1 (if issued) reports QBI information correctly.
13. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
14. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]." Include: trust compressed tax brackets — verify whether distributing more income to beneficiaries in lower brackets would reduce total tax.

## Control Points

- **DNI mismatch** — If K-1 totals don't match the income distribution deduction, this is a hard stop.
- **Trust instrument review** — Any deduction allocation question (income vs. principal) must be resolved against the trust instrument, not assumed.

## Red Flags

- Grantor trust return showing tax due (should be informational only)
- Simple trust accumulating income (violates simple trust requirement)
- Capital gains allocated to income rather than principal without trust instrument support
- Fiduciary fees appear unreasonable relative to trust assets
- Prior-year excess deductions or capital loss carryforwards with no supporting schedule
- Trust compressed tax brackets: income retained at trust level when distribution to lower-bracket beneficiaries would reduce total tax
- Cross-return coordination needed: K-1 amounts should tie to each beneficiary's Form 1040; if the trust receives K-1s from pass-throughs, those should tie to the issuing entity's return
- Digital-asset question answered "No" but a 1099-DA or crypto activity appears in the source documents
- Foreign tax paid on 1099s, foreign accounts on custody statements, or foreign-trust indicators — possible FinCEN 114 (FBAR) / Form 8938 / Form 3520 exposure; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- Post-death income reported on the wrong return (decedent's final 1040 vs. the estate's 1041), or IRD present with no IRC 691(c) deduction computed
- Income distribution deduction taken with no Schedule I attached
- Income retained at the entity level with no Form 8960 despite investment income above the compressed threshold
- 1099-B basis on an estate or inherited account equal to the decedent's original basis — missing date-of-death step-up
- Charitable deduction claimed where the governing instrument does not authorize charitable payments, or paid from principal rather than gross income
- ESBT box checked but S-corporation K-1 income is included in DNI
- A trust filing on a fiscal year with no IRC 645 election in the file

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into sections:
- **Entity Type Confirmed** — Grantor / Simple / Complex / Estate (with ESBT flag if applicable) and supporting rationale
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by dollar impact for preparer attention
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1041", client/Trust name, tax year, preparer name, review date
2. **Entity type confirmed** — Grantor / Simple / Complex / Estate (with ESBT flag if applicable) and supporting rationale
3. **Bottom line** — 2-3 sentence summary
4. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
5. **Missing support** — Bulleted list of absent source documents
6. **Preparer questions** — Bulleted list of items requiring judgment
7. **Audit risk** — 1-3 bullet points, factual
8. **199A/QBI verification** — Summary of the QBI check results

Save as `[ClientName]_[TaxYear]_1041_Review.docx` (e.g., `SmithTrust_2025_1041_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not determine income vs. principal allocation without reference to the trust instrument.
- Do not conclude trustee material participation for passive-loss purposes — flag it; substantive analysis goes to `tax-advisor`.
- Do not mark the return reviewed-complete if K-1 totals don't foot to the income distribution deduction.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (resident-state fiduciary filings driven by trustee/beneficiary residency, state PTET credits on incoming K-1s) to Preparer Questions rather than reviewing them here.
