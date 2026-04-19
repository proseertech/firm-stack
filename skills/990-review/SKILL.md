---
name: 990-review
version: 1.3.0
description: |
  Cross-reference a completed Form 990-PF (private foundation return) against
  source documents — financial statements, investment schedules, grants paid, and
  officer compensation records — to verify accuracy and compliance with private
  foundation excise tax rules. Grades findings by severity, independently
  recalculates the distributable amount, and flags audit risk items.
trigger: |
  "review the 990", "private foundation return", "990-PF review",
  "check the private foundation return", "990 cross-reference"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 990 Review: Private Foundation Return Cross-Reference

## Purpose

Catch errors and compliance issues before a Form 990-PF is filed. Verify that financials tie to source documents and that the distribution requirement, investment income excise tax, and disqualified person transactions are correctly reported.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences in the $10-$100 range are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

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
- Prior-year return (for distributable amount carryover)

## Workflow

1. **Reconcile financial statements** — Tie Part I revenue and expenses to the financial statements. Tie Part II balance sheet to the ending balance sheet.
2. **Verify investment income and excise tax** — Confirm net investment income in Part VI and the 1.39% excise tax computation.
3. **Verify distributable amount and qualifying distributions (IRC 4942)** — Independently calculate the 5% distributable amount: 5% of the average fair market value of non-charitable-use assets. Show the math in the output. Confirm qualifying distributions meet or exceed the distributable amount. Flag any carryover of undistributed income.
4. **Verify grants paid** — Tie Part XV grants and contributions paid to grant records. Confirm grant recipients and amounts.
5. **Verify officer compensation** — Tie Part VIII compensation to W-2s and confirm reasonableness.
6. **Check for self-dealing and restricted transactions** — Flag any transactions with disqualified persons reported in Part VII-A.
7. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
8. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

- **Distribution shortfall** — If qualifying distributions fall below the distributable amount, flag immediately — undistributed income carries an excise tax.
- **Self-dealing** — Any transaction with a disqualified person must be reviewed by the preparer before the return is finalized.

## Red Flags

- Distributable amount exceeds qualifying distributions
- Grants paid to individuals without a documented expenditure responsibility procedure
- Investment income on the return doesn't tie to brokerage statements
- Officer compensation appears unreasonably high relative to foundation assets
- Jeopardizing investments present but not disclosed
- Program-related investments (PRIs) counted as qualifying distributions — confirm they meet IRC 4944(c) criteria
- Cross-return coordination needed: if the foundation owns pass-through interests, K-1 income should tie to the issuing entity's return

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

## Safety Constraints

- Do not mark the return reviewed-complete if the distribution requirement is not met without preparer resolution.
- Do not clear self-dealing transactions without preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
