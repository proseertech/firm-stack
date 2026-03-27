---
name: 1120-review
version: 1.0.0
description: |
  Cross-reference a completed Form 1120 (C-corporation income tax return) against
  source documents — trial balance, supporting schedules, and workpapers — to verify
  income, deductions, credits, and tax computation.
trigger: |
  "review the 1120", "C-corp return review", "1120 cross-reference",
  "tie out the C-corp return", "verify the 1120"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1120 Review: C-Corporation Return Cross-Reference

## Purpose

Catch errors before a Form 1120 is filed. Verify that income, deductions, and the tax computation on the return tie to the trial balance and source documents.

## Required Inputs

- Completed Form 1120 and all schedules (C, D, E, J, K, L, M-1, M-2, M-3 if applicable)
- Trial balance or financial statements for the tax year
- Prior-year return (for NOL carryforwards, credit carryforwards, E&P)
- Any supporting workpapers

## Workflow

1. **Reconcile income and deductions to trial balance** — Tie Schedule M-1 book-to-tax differences. Flag unexplained items.
2. **Verify gross income** — Tie gross receipts and other income lines to the trial balance.
3. **Verify deductions** — Spot-check significant deductions (compensation, depreciation, interest) against supporting schedules or Form 4562.
4. **Verify credits** — Confirm each credit against the applicable form (Form 3800, etc.).
5. **Verify tax computation (Schedule J)** — Recalculate the tax liability. Confirm estimated tax payments and withholding.
6. **Verify balance sheet (Schedule L)** — Tie beginning and ending balances. Flag material unexplained changes.
7. **Verify retained earnings (M-2)** — Confirm beginning retained earnings ties to prior-year return. Verify current-year movements.
8. **Summarize findings** — Confirmed items, variances, preparer questions.

## Control Points

- **NOL carryforward** — If an NOL deduction is taken, confirm the carryforward amount ties to the prior-year return or NOL schedule.
- **Material variance** — Discrepancies above materiality require preparer correction before filing.

## Red Flags

- Book income and taxable income reconciliation has unexplained permanent or timing differences
- Depreciation on the return significantly exceeds Form 4562
- Large dividend deduction (DRD) without supporting ownership documentation
- Prior-year credit carryforwards with no supporting schedule

## Output Format

Structured findings report: Confirmed, Variances, Missing Support, Preparer Questions.

## Safety Constraints

- Do not mark the return reviewed-complete if material variances remain unresolved.
