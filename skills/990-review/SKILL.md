---
name: 990-review
version: 1.0.0
description: |
  Cross-reference a completed Form 990-PF (private foundation return) against
  source documents — financial statements, investment schedules, grants paid, and
  officer compensation records — to verify accuracy and compliance with private
  foundation excise tax rules.
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

1. **Reconcile financial statements** — Tie Part I revenue and expenses to the financial statements. Tie Part II balance sheet to the ending balance sheet.
2. **Verify investment income and excise tax** — Confirm net investment income in Part VI and the 1.39% excise tax computation.
3. **Verify distributable amount and qualifying distributions** — Confirm the 5% minimum distribution requirement calculation and that qualifying distributions meet or exceed it. Flag any carryover of undistributed income.
4. **Verify grants paid** — Tie Part XV grants and contributions paid to grant records. Confirm grant recipients and amounts.
5. **Verify officer compensation** — Tie Part VIII compensation to W-2s and confirm reasonableness.
6. **Check for self-dealing and restricted transactions** — Flag any transactions with disqualified persons reported in Part VII-A.
7. **Summarize findings** — Confirmed items, variances, compliance flags, preparer questions.

## Control Points

- **Distribution shortfall** — If qualifying distributions fall below the distributable amount, flag immediately — undistributed income carries an excise tax.
- **Self-dealing** — Any transaction with a disqualified person must be reviewed by the preparer before the return is finalized.

## Red Flags

- Distributable amount exceeds qualifying distributions
- Grants paid to individuals without a documented expenditure responsibility procedure
- Investment income on the return doesn't tie to brokerage statements
- Officer compensation appears unreasonably high relative to foundation assets
- Jeopardizing investments present but not disclosed

## Output Format

Structured findings report: Confirmed, Variances, Compliance Flags, Preparer Questions.

## Safety Constraints

- Do not mark the return reviewed-complete if the distribution requirement is not met without preparer resolution.
- Do not clear self-dealing transactions without preparer review.
