---
name: 990-review
version: 1.10.0
description: |
  Cross-reference a completed Form 990-PF (private foundation return) against
  source documents — financial statements, investment schedules, grants paid, and
  officer compensation records — to verify accuracy and compliance with private
  foundation excise tax rules. Independently recalculates the 5% distributable
  amount, checks the net investment income excise tax, screens for self-dealing,
  grades findings by severity, and flags audit risk items. Use this whenever
  someone wants a completed 990-PF checked before filing — "review the 990",
  "tie out the foundation return", "did the foundation meet its distribution
  requirement", "check the excise tax", "look over the private foundation return"
  — even if they don't say "990-PF" or "cross-reference."
trigger: |
  "review the 990", "990-PF review", "private foundation return",
  "check the private foundation return", "990 cross-reference",
  "tie out the foundation return", "foundation return review",
  "check the distribution requirement", "did the foundation distribute enough",
  "check the excise tax", "self-dealing check"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 990 Review: Private Foundation Return Cross-Reference

## Purpose

Catch errors and compliance issues before a Form 990-PF is filed. Verify that financials tie to source documents and that the distribution requirement, net investment income excise tax, and disqualified person transactions are correctly reported. The private foundation excise regime is unforgiving — a missed distribution or an unflagged self-dealing transaction carries excise tax and, if uncorrected, escalating penalties — so the review has to be independent, not a re-read of the preparer's own numbers.

This produces reviewer findings for a preparer to act on. It does not sign or file the return.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of total assets or net investment income to determine whether a variance is acceptable. That approach belongs in financial statement audits, not tax review.

Classify findings by severity (impact + risk) rather than by dollar-amount materiality:
- **HIGH**: Incorrect excise tax computation, distribution shortfall, self-dealing transactions, missing forms
- **MEDIUM**: Documentation gaps, grant recipients without expenditure responsibility, items that could trigger IRS correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about or consider low-severity. Severity is for prioritization, not filtering — all findings go in the table. A separate preparer review step decides what to act on; your job at this stage is coverage.

## Required Inputs

- Completed Form 990-PF and all schedules
- Financial statements (balance sheet, income statement) for the tax year
- Grant payment records
- Investment account statements
- Officer/disqualified person compensation records
- Schedule B and donor/contribution records (to test substantial-contributor status)
- Estimated tax payment records (EFTPS confirmations)
- Prior-year return (for distributable amount carryover)
- CCH Axcess Diagnostics report and Input Override Report (if available)

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Part references below are to the **2021-and-later Form 990-PF revision**. Pre-2021 returns use an older numbering (e.g., the excise tax was Part VI, grants were Part XV) — if reviewing an older return, map accordingly rather than reporting findings against the wrong part.

The detailed mechanics — column-allocation rules, Part IX valuation inputs, qualifying-distribution qualification tests, the disqualified-person list, the Chapter 42 screens, and the initial-return branch — live in **`references/pf-review-procedures.md`**. Read it before starting; the steps below say what to verify, the reference says how.

1. **Determine foundation type and filing posture** — Confirm the foundation is a private **non-operating** foundation before applying the standard workflow — it assumes one. If this is a private operating foundation, column (c) adjusted net income must be completed and the distributable-amount framework runs through Part XIII instead; flag the difference and review under the POF rules rather than forcing the non-operating template onto the return. If the **initial-return box** is checked (or this is the foundation's first year), run the first-year branch in the references file: determination-letter/Form 1023 status, prorated first-year distributable amount, accounting method affirmatively established, complete initial officer listing, and no prior-year carryovers.
2. **Reconcile financial statements** — Tie Part I revenue and expenses to the financial statements. Tie Part II balance sheet to the ending balance sheet. Close the loop with Part III: net assets must roll from beginning to end with unrealized gains/losses and similar non-Part-I items as reconciling entries. Parts I and II can each tie to the books and still be inconsistent with each other — Part III is where that shows.
3. **Verify Part I column allocation** — Check that expenses land in the correct columns per the rules in the references file: investment expenses in column (b); charitable disbursements in column (d) on the cash basis; dual-use allocations reasonable, consistent, and documented; no federal income or excise taxes in (b)–(d); straight-line depreciation only in (b) and none in (d). Column (b) drives the excise-tax base and column (d) drives qualifying distributions — a misallocation silently corrupts both computations this review recalculates, so this check comes before either recalculation.
4. **Verify investment income and excise tax** — Confirm net investment income in Part V and the 1.39% excise tax computation. Apply the Part IV capital-gain mechanics (see reference): donated property sold uses the **donor's carryover basis**, not FMV at the date of gift; the donated-vs-purchased column is completed; and line 7(b) is never negative — capital losses offset only capital gains, with no netting against other investment income and no carryover. Then tie the Part V payments section to records: estimated payments made timely via EFTPS, prior-year overpayment applied, Form 2220 if underpaid.
5. **Verify distributable amount and qualifying distributions (IRC 4942)** — Independently calculate the 5% distributable amount: 5% of the average fair market value of non-charitable-use assets (Part IX minimum investment return → Part X distributable amount). Show the math in the output — and validate the Part IX inputs before trusting it: monthly-average FMV for marketable securities, cash averaged, real-estate appraisals no more than five years old, exempt-function assets excluded, short-year proration (see reference). Confirm qualifying distributions (Part XI) meet or exceed the distributable amount, and test that counted distributions actually **qualify** — grants to foundation-controlled organizations, grants to non-functionally-integrated Type III supporting organizations, recoveries of prior-year distributions, and in-kind property distributions each have special rules (see reference). Flag any carryover of undistributed income (Part XII).
6. **Verify grants paid and screen for taxable expenditures (IRC 4945)** — Tie Part XIV (Supplementary Information) grants and contributions paid to grant records; confirm recipients and amounts. Then screen **all expenditures**, not just grants, for 4945 exposure: lobbying or political spending anywhere in the general ledger; grants to individuals for travel or study without advance IRS approval of the grant plan; grants to non-501(c)(3) recipients without expenditure responsibility; and foreign grantees without an equivalency determination or exercised expenditure responsibility, with the required attachment on the return.
7. **Verify officer compensation and Part VII completeness** — Tie Part VII compensation to W-2s and confirm reasonableness. Part VII must list every officer, director, trustee, and foundation manager who served **at any time** during the year (unpaid positions shown at $0, not omitted) and the five highest-paid independent contractors over $50,000 — including investment-advisor fees even when netted against investment returns; netted advisor fees belong in Part VII **and** in column (b). If any employee's compensation exceeds $1 million, the 21% IRC 4960 excise applies via Form 4720 regardless of how reasonable the compensation is.
8. **Check for self-dealing and Chapter 42 exposure** — Build the disqualified-person list first (see reference): substantial contributors, foundation managers, >20% owners, their family members, and 35%-controlled entities — and check Schedule B against donor records, because a donor who crossed the substantial-contributor threshold this year is a **new disqualified person** the screen must include. Flag any transactions with disqualified persons reported in Part VI-B (Statements Regarding Activities for Which Form 4720 May Be Required). If the foundation holds more than 2% of any business entity, run the IRC 4943 excess-business-holdings test: aggregate the foundation's holdings with all disqualified persons' holdings against the 20% limit, and check the 5-year disposition clock on holdings received by gift or bequest.

For every Chapter 42 finding this review surfaces (IRC 4941 self-dealing, 4942 shortfall, 4943 excess holdings, 4944 jeopardizing investments, 4945 taxable expenditures, 4960 excess compensation), the finding is incomplete without its consequence: note on the finding that **Form 4720** must be filed, correction within the correction period is required, and abatement under IRC 4962 / reasonable cause should be considered.
9. **Verify Section 199A / QBI reporting (if applicable)** — Private foundations are tax-exempt entities and are not eligible for the 199A QBI deduction. However, if the foundation owns pass-through interests (partnership or S-corp K-1s), confirm:
   - QBI information from incoming K-1s is received and documented (the foundation itself cannot claim a QBI deduction, but the K-1 data should be retained for record-keeping).
   - No 199A deduction is claimed at the foundation level — only individuals, trusts, and estates under IRC 199A are eligible.
   - If the foundation's pass-through investment is an SSTB, note this for any ultimate individual owners who may have QBI implications.
10. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
11. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

Stop and get a preparer decision before treating the return as reviewed-complete when:

- **Distribution shortfall** — If qualifying distributions fall below the distributable amount, flag it immediately. Undistributed income carries an excise tax under IRC 4942, and the shortfall must be resolved (or a valid carryover applied) before filing.
- **Self-dealing** — Any transaction with a disqualified person must go to the preparer before the return is finalized. Self-dealing is prohibited regardless of fairness or benefit to the foundation, so it is a judgment call the preparer owns, not one to clear silently.
- **Other Chapter 42 exposure (4943 / 4944 / 4945 / 4960)** — Route to the preparer with the Form 4720 consequence attached. Correction periods, dispositions, and abatement requests are preparer decisions, not items to clear silently.

## Red Flags

- Distributable amount exceeds qualifying distributions
- Grants paid to individuals without a documented expenditure responsibility procedure
- Investment income on the return doesn't tie to brokerage statements
- Officer compensation appears unreasonably high relative to foundation assets
- Jeopardizing investments present but not disclosed
- Program-related investments (PRIs) counted as qualifying distributions — confirm they meet IRC 4944(c) criteria
- Investment-advisor fees netted against investment returns and missing from Part VII and column (b)
- Foundation-plus-disqualified-person holdings exceed 20% of a business entity, or a gifted/bequeathed holding is approaching its 5-year disposition deadline — IRC 4943
- Lobbying or political expenditures anywhere in the general ledger, or foreign grants without an equivalency determination or expenditure responsibility — IRC 4945
- Grants to foundation-controlled organizations or non-functionally-integrated Type III supporting organizations counted as qualifying distributions
- A private operating foundation reviewed on the non-operating framework (column (c) blank, Part XIII skipped)
- Cross-return coordination needed: if the foundation owns pass-through interests, K-1 income should tie to the issuing entity's return
- Unrelated business income with no Form 990-T — K-1s showing UBTI (partnership Box 20, code V), debt-financed rental income, or controlled-entity payments trigger a 990-T filing requirement at $1,000 of gross UBI; a missed 990-T is an unfiled return with tax due, and UBI must also be excluded from the Part V excise-tax base
- Foreign financial accounts — Part VI-A Line 16 answered "Yes" (or foreign custody accounts visible on statements) means a FinCEN 114 (FBAR) filing requirement with its own deadline; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`

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
- **Compliance Flags** — Foundation-specific compliance items
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 990-PF", client/Foundation name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
4. **Compliance flags** — Foundation-specific compliance items (distribution requirement, excise tax, Chapter 42 screens, Form 4720 status)
5. **Missing support** — Bulleted list of absent source documents
6. **Preparer questions** — Bulleted list of items requiring judgment
7. **Audit risk** — 1-3 bullet points, factual
8. **199A/QBI verification** — Summary of the QBI check results (no 199A at foundation level; incoming K-1 QBI data documented)

Save as `[ClientName]_[TaxYear]_990PF_Review.docx` (e.g., `SmithFoundation_2025_990PF_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete if the distribution requirement is not met without preparer resolution — an unaddressed shortfall means an excise tax the foundation owes.
- Do not clear self-dealing transactions on your own; they require preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
- Report the distributable-amount and excise-tax math you performed, not just the conclusion, so the preparer can check it — an independent recalculation is only useful if it is auditable.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (state charitable registrations and attorney-general filings, Part VI-A Line 8 state reporting) to Preparer Questions rather than reviewing them here.
