---
name: 990-review
version: 1.1.0
description: |
  Cross-reference a completed Form 990-PF (private foundation return) against
  source documents — financial statements, investment schedules, grants paid, and
  officer compensation records — to verify accuracy and compliance with private
  foundation excise tax rules. Quantifies materiality, grades findings by severity,
  independently recalculates the distributable amount, and flags audit risk items.
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

## Required Inputs

- Completed Form 990-PF and all schedules
- Financial statements (balance sheet, income statement) for the tax year
- Grant payment records
- Investment account statements
- Officer/disqualified person compensation records
- Prior-year return (for distributable amount carryover)

## Workflow

1. **Establish materiality and scope** — Quantify materiality for this return. Use the firm's configured materiality threshold; if not configured, use 2% of total assets as working materiality. Every finding in subsequent steps is classified as material or immaterial relative to this threshold.
2. **Reconcile financial statements** — Tie Part I revenue and expenses to the financial statements. Tie Part II balance sheet to the ending balance sheet.
3. **Verify investment income and excise tax** — Confirm net investment income in Part VI and the 1.39% excise tax computation.
4. **Verify distributable amount and qualifying distributions (IRC 4942)** — Independently calculate the 5% distributable amount: 5% of the average fair market value of non-charitable-use assets. Show the math in the output. Confirm qualifying distributions meet or exceed the distributable amount. Flag any carryover of undistributed income.
5. **Verify grants paid** — Tie Part XV grants and contributions paid to grant records. Confirm grant recipients and amounts.
6. **Verify officer compensation** — Tie Part VIII compensation to W-2s and confirm reasonableness.
7. **Check for self-dealing and restricted transactions** — Flag any transactions with disqualified persons reported in Part VII-A.
8. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
9. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

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
Amount: $[X] (X% of total assets)
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into sections:
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW)
- **Compliance Flags** — Foundation-specific compliance items
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

## Safety Constraints

- Do not mark the return reviewed-complete if the distribution requirement is not met without preparer resolution.
- Do not clear self-dealing transactions without preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
