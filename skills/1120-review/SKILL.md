---
name: 1120-review
version: 1.3.0
description: |
  Cross-reference a completed Form 1120 (C-corporation income tax return) against
  source documents — trial balance, supporting schedules, and workpapers — to verify
  income, deductions, credits, and tax computation. Grades findings by severity and
  flags audit risk items including accumulated earnings tax exposure.
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

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences in the $10-$100 range are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross receipts, total assets, or net income to determine whether a variance is acceptable. That approach belongs in financial statement audits, not tax review.

Classify findings by severity (impact + risk) rather than by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about or consider low-severity. Severity is for prioritization, not filtering — all findings go in the table. A separate preparer review step decides what to act on; your job at this stage is coverage.

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
5. **Verify tax computation (Schedule J)** — Recalculate the tax liability. Confirm estimated tax payments and withholding. Check for accumulated earnings tax exposure (IRC 531) if retained earnings are growing without clear business purpose for the accumulation.
6. **Verify balance sheet (Schedule L)** — Tie beginning and ending balances. Flag unexplained changes.
7. **Verify retained earnings (M-2)** — Confirm beginning retained earnings ties to prior-year return. Verify current-year movements.
8. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
9. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

- **NOL carryforward** — If an NOL deduction is taken, confirm the carryforward amount ties to the prior-year return or NOL schedule.
- **Any discrepancy beyond rounding** — Every variance outside the $10-$100 rounding range requires preparer review and correction before filing.

## Red Flags

- Book income and taxable income reconciliation has unexplained permanent or timing differences
- Depreciation on the return significantly exceeds Form 4562
- Large dividend deduction (DRD) without supporting ownership documentation
- Prior-year credit carryforwards with no supporting schedule
- Accumulated earnings appear to exceed reasonable business needs — IRC 531 exposure
- Related-party transactions present without supporting transfer pricing documentation
- Cross-return coordination needed: if the corporation owns pass-through interests, K-1 income should tie to the issuing entity's return

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
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

## Safety Constraints

- Do not mark the return reviewed-complete if any discrepancies beyond rounding remain unresolved.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
