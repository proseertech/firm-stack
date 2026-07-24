---
name: 1120-review
version: 1.11.0
description: |
  Cross-reference a completed Form 1120 (C-corporation income tax return) against its
  source documents — trial balance, supporting schedules, Form 4562, Form 3800, and the
  prior-year return — to catch errors before filing. Verifies income, deductions, credits,
  and the Schedule J tax computation tie out; reconciles Schedule M-1/M-3 book-to-tax and
  Schedule L / M-2; tests NOL usage (80% cap, Sec. 382), DRD mechanics, and entity-level
  taxes beyond the 21% rate (CAMT, PHC, AET); sweeps for required international forms;
  includes an initial-return branch for first-year corporations; grades findings by
  severity; and flags audit-risk items. Use this whenever a C-corp return needs a second
  set of eyes before it goes out the door — "review the 1120", "tie out the C-corp
  return", "does the 1120 match the trial balance", "check the corporate return before we
  file" — even if they don't name the form or say the word "review".
trigger: |
  "review the 1120", "1120 review", "C-corp return review", "check the C-corp return",
  "1120 cross-reference", "tie out the C-corp return", "verify the 1120",
  "does the 1120 tie out", "check the 1120 before filing", "review the corporate return",
  "cross-reference the 1120 to the trial balance", "the C-corp return doesn't tie",
  "first year corporate return", "initial return review"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1120 Review: C-Corporation Return Cross-Reference

## Purpose

Catch errors in a Form 1120 before it is filed. Verify that income, deductions, credits, and the tax computation on the return tie to the trial balance and source documents, and surface anything that would draw IRS scrutiny. Two failure modes matter equally here: numbers that don't tie, and numbers that tie perfectly to the books but are legally wrong (a capital loss netted against ordinary income, an NOL used past the 80% cap, a missing addback that makes the M-1 look clean). The deliverable is a severity-graded findings report a preparer can act on line by line.

This is a review, not a sign-off: findings go to the responsible preparer, who decides what to correct and owns the filed return.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

Do not apply a percentage-based materiality threshold — a percentage of gross receipts, total assets, or net income belongs in a financial-statement audit, not a tax review. A $2,000 error that changes the tax due is a real finding regardless of how small it is against total assets.

Classify each finding by severity (impact + risk), not by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table — including items you are uncertain about or consider low-severity. Severity ranks the list; it does not filter it. Filtering happens at preparer review; your job here is complete coverage, because an error dropped now surfaces only after filing.

## Required Inputs

Confirm these are present before starting. A review run against a missing schedule or the wrong year's trial balance produces false comfort — the gaps look "clean" only because nothing was there to check.

- Completed Form 1120 and all schedules (C, D, E, J, K, L, M-1, M-2, M-3 if applicable)
- Trial balance or financial statements for the tax year
- Prior-year return (for NOL carryforwards, credit carryforwards, E&P, and the carryover sweep)
- IRS/state correspondence and any amended returns or exam adjustments since the prior filing (if any)
- Fixed-asset register (for the Form 4562 tie-out)
- K-1s received from any pass-through the corporation owns
- Form 8832 acceptance (first-year returns of LLCs electing corporate status)
- Any supporting workpapers
- CCH Axcess Diagnostics report and Input Override Report (if available)

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Detailed procedures for the flagged steps live in **`references/corporate-verification-procedures.md`** — read it when you reach a step that points there. The section headers in that file match the step numbers below.

1. **Orient: prior-year return and correspondence** — Confirm beginning balances and carryovers tie to the prior year **as adjusted** (exam adjustments, amended returns), not just as filed, and run the carryover completeness sweep — charitable 5-year, capital loss (corporate losses offset only capital gains), Section 1231(c) lookback recharacterization, Section 481(a) spread, installment gross profit, Section 179. Procedures in the references file.
2. **Reconcile income and deductions to trial balance** — Tie Schedule M-1 book-to-tax differences; flag unexplained items. If total assets are $10 million or more, confirm Schedule M-3 (with Form 8916-A where applicable) is filed instead of M-1 — reconciling M-1 on an M-3-required client is reviewing the wrong schedule. If audited financials disclose uncertain tax positions, confirm Schedule UTP was considered. Then work the **expected-addback checklist** in the references file — the common M-1 failure is a *missing* addback (meals, entertainment, club dues, lobbying, fines, officer life insurance, parking/QTF, gifts over $25), which looks clean because nothing is there to question.
3. **Verify gross income** — Tie gross receipts and other income lines to the trial balance. Confirm the digital-asset question on page 1 is answered and consistent with the source documents — a 1099-DA or crypto activity on custody statements with a "No" answer is a finding. Reconcile any Forms 1099-DA (broker reporting is new; basis may be missing or wrong).
4. **Verify deductions** — Spot-check significant deductions (compensation, depreciation, interest) against supporting schedules or Form 4562, then work the deduction mechanics in the references file: charitable 10% limitation and substantiation (Form 8283 / appraisal / accrual-basis 3.5-month rule), Section 267(a)(2) deferral of amounts accrued to cash-basis related parties (year-end owner bonuses are the classic catch), Section 162(m) where the corporation is publicly held, and UNICAP/inventory (accrual + Section 263A above the Section 448(c) threshold; book LCM write-downs added back).
5. **Verify the dividends-received deduction (Schedule C)** — Beyond ownership documentation: the DRD percentage matches the ownership tier, the 45-day holding period is met, debt-financed stock is reduced under Section 246A, and the taxable-income limitation is recomputed. Mechanics in the references file.
6. **Verify credits** — Confirm each credit against the applicable form (Form 3800, etc.).
7. **Verify tax computation (Schedule J)** — Recalculate the tax liability. Confirm estimated tax payments and withholding, then test for an underpayment penalty (Form 2220 — prior-year safe harbor is unavailable to large corporations). Screen the entity-level taxes beyond the 21% rate per the references file: CAMT applicability (Form 4626) where group AFSI could reach the threshold, personal holding company status (Schedule PH — mechanical and self-assessed for closely held corporations with 60%+ passive income), and accumulated earnings tax exposure (IRC 531) if retained earnings are growing without clear business purpose.
8. **Verify NOL usage, not just the amount** — The carryforward tying to the prior year is necessary but not sufficient: post-2017 NOLs are capped at 80% of taxable income and must be tracked by vintage, and an ownership change triggers the Section 382 annual limitation. Procedures in the references file.
9. **Verify balance sheet (Schedule L)** — Tie beginning and ending balances. Flag unexplained changes.
10. **Verify retained earnings (M-2)** — Confirm beginning retained earnings ties to the prior-year return (as adjusted — see step 1). Verify current-year movements. If distributions exceed E&P, Form 5452 is required to support nondividend treatment.
11. **International information-return presence check** — For every foreign trigger visible in the file (foreign owners, CFCs, foreign partnerships/DREs, PFICs, property transfers, foreign accounts), confirm the required form is attached or documented N/A — 5471, 5472, 8865, 8858, 8621, 926, and GILTI/FDII/BEAT (8992/8993/8991) where thresholds are met. Trigger table in the references file. These penalties are automatic, per-form, and keep the statute open; this check is presence, not substance.
12. **Verify Section 199A / QBI reporting (if applicable)** — C-corporations are not pass-through entities and do not generate QBI for their shareholders. However, if the C-corp owns pass-through interests (partnership or S-corp K-1s), confirm:
    - QBI information from incoming K-1s is properly received and documented (the C-corp itself is not eligible for the 199A deduction, but the K-1 data should be retained for the entity's own records and for any ultimate owner-level QBI computation).
    - If the C-corp is a specified service trade or business (SSTB), note that its income does not qualify for 199A at the owner level — this affects any individual who might own the C-corp stock directly or through a pass-through.
    - No 199A deduction is claimed at the C-corp level — the QBI deduction is only available to individuals, trusts, and estates under IRC 199A.
13. **Verify depreciation and R&E capitalization** — Tie Form 4562 to the fixed-asset schedule or trial-balance additions; depreciation is a book-tax difference the M-1 reconciliation alone can't validate. Two 2025 regime changes make software defaults unreliable:
    - **Split-rate bonus depreciation** — 40% for property acquired before January 20, 2025; 100% for property acquired and placed in service on or after that date (OBBBA). Confirm each significant addition uses the rate matching its **acquisition** date.
    - **Section 174/174A** — Domestic research costs are currently deductible for tax years beginning after 2024; foreign R&E remains capitalized over 15 years. Any catch-up deduction of previously capitalized domestic R&E must be supported by a Rev. Proc. 2025-28 transition election or Form 3115 — an M-1 that "ties" can still reflect an unauthorized method change. This is the largest book-tax law change on 2025 corporate returns.
    - Verify Section 179 amounts against the applicable year's limits and phase-out.
14. **Verify the Section 163(j) interest limitation** — If aggregate average annual gross receipts exceed the IRC 448(c) small-business threshold (inflation-adjusted; verify the applicable year's amount) or the corporation is a tax shelter under 448(d)(3), confirm Form 8990 is attached and the limitation computed. For tax years beginning after 2024, depreciation/amortization/depletion is **added back to ATI again** (OBBBA) — a computation carried forward on the 2024 EBIT basis understates the limit. Confirm prior-year disallowed-interest carryforwards tie to the prior return.
15. **Initial-return branch** *(when the Initial Return box is checked or this is year 1)* — Run the first-year checklist in the references file: Form 8832 classification election accepted and effective-date consistent, permissible tax year, accounting-method box consistent with Section 448, first-year election statements attached (Section 195/248 startup and organizational costs, de minimis safe harbor), Schedule L beginning balances zero, estimated-tax setup (no prior-year safe harbor in year 1), and depreciation conventions (mid-quarter test). Most first-year elections cannot be fixed after the first return.
16. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
17. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

Stop and route to the preparer before the return is treated as final when:

- **NOL carryforward** — An NOL deduction is taken. Confirm the carryforward amount ties to the prior-year return or NOL schedule **and** the usage is legal (80% cap by vintage; Section 382 limitation if an ownership change occurred). An ownership change with no 382 analysis is a hard stop, not a finding to note.
- **Initial return with missing election statements** — First-year elections ride with the first return and are largely irreversible; do not treat an initial return as reviewable-complete while required election statements or the Form 8832 acceptance are missing.
- **Any discrepancy beyond rounding** — Every variance beyond the $10 rounding tolerance needs preparer review and correction before filing. Do not resolve it yourself; the preparer owns the return.

## Red Flags

- Book income and taxable income reconciliation has unexplained permanent or timing differences
- A trial-balance account for meals, entertainment, dues, penalties, or officer life insurance with **no** corresponding M-1/M-3 addback — the missing-addback failure looks clean
- Schedule M-1 filed where total assets are $10 million or more — Schedule M-3 is required
- Depreciation on the return significantly exceeds Form 4562
- A capital loss netted against ordinary income — corporate capital losses offset only capital gains
- NOL deduction equal to 100% of taxable income sourced from post-2017 losses, or an equity raise/buyout in the ownership history with no Section 382 analysis
- Large dividend deduction (DRD) without supporting ownership documentation, at a percentage that doesn't match the ownership tier, or on stock held briefly around the ex-dividend date
- Year-end accrued bonuses or interest payable to a >50% cash-basis shareholder deducted before payment
- Closely held corporation with predominantly passive income and no Schedule PH analysis
- Prior-year credit carryforwards with no supporting schedule
- Accumulated earnings appear to exceed reasonable business needs — IRC 531 exposure
- Related-party transactions present without supporting transfer pricing documentation
- Cross-return coordination needed: if the corporation owns pass-through interests, K-1 income should tie to the issuing entity's return
- Digital-asset question answered "No" but a 1099-DA or crypto activity appears in the source documents
- Foreign accounts, foreign shareholders (25%+), or foreign subsidiaries/interests visible in source docs — possible FinCEN 114 (FBAR) / Form 5471 / Form 5472 exposure with per-form automatic penalties; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- 2025 fixed-asset additions straddling January 19 all claimed at a single bonus rate, or a catch-up R&E deduction with no Rev. Proc. 2025-28 election or Form 3115 in the file
- Interest expense deducted in full with no Form 8990 despite gross receipts above the IRC 448(c) threshold
- Initial Return box checked but Schedule L shows beginning balances, or no first-year election statements are attached

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
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by dollar impact for preparer attention
- **Missing Support** — Items where source docs are absent
- **Required-Form Status** — International forms, M-3/UTP, 4626, Schedule PH, 8990: present / documented N/A / open
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1120", client/Corporation name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
4. **Required-form status** — Table: form, trigger, status (present / N/A documented / open)
5. **Missing support** — Bulleted list of absent source documents
6. **Preparer questions** — Bulleted list of items requiring judgment
7. **Audit risk** — 1-3 bullet points, factual
8. **199A/QBI verification** — Summary of the QBI check results (no 199A at C-corp level; incoming K-1 QBI data documented; SSTB note)

Save as `[ClientName]_[TaxYear]_1120_Review.docx` (e.g., `ABCCorp_2025_1120_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete while any discrepancy beyond rounding is unresolved — a "clean" review with open variances misleads the preparer into filing.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (apportionment, state modifications, nexus questions) to Preparer Questions rather than reviewing them here.
- State audit risk as facts, not as a probability or percentage ("this item may draw scrutiny because…"). Judging what level of risk is acceptable is the signing partner's call, not the reviewer's.
- Do not invent authority. Cite an IRC §, regulation, or procedure only when you are confident it applies; otherwise describe the issue and leave the citation for the preparer to confirm.
- Do not hardcode inflation-adjusted amounts (Section 448(c) threshold, Section 179 limits) — statutory fixed thresholds (the $10M M-3 line, the $1M Section 162(m) cap) may be stated, but verify year-indexed figures against the applicable year.
