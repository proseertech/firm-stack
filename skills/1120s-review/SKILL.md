---
name: 1120s-review
version: 1.2.0
description: |
  Cross-reference a completed Form 1120-S (S-corporation income tax return) against
  source documents — trial balance, Schedule K-1s, officer W-2s, and supporting
  schedules — to verify income, deductions, credits, and shareholder allocations.
  Grades findings by severity and flags audit risk items including reasonable
  compensation analysis.
trigger: |
  "review the 1120-S", "S-corp return review", "check the S-corp", "1120-S cross-reference",
  "tie out the S-corp return", "verify the 1120S"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1120-S Review: S-Corporation Return Cross-Reference

## Purpose

Catch errors before a Form 1120-S is filed. Verify that income, deductions, and shareholder allocations on the return tie to the trial balance and source documents, and that K-1s are mathematically consistent with Schedule K totals.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences in the $10-$100 range are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross receipts, total assets, or net income to determine whether a variance is acceptable. That approach belongs in financial statement audits, not tax review.

Classify findings by severity (impact + risk) rather than by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Do not dismiss or deprioritize findings because the dollar amount is small relative to gross receipts. A $500 error is still an error that needs correction.

## Required Inputs

- Completed Form 1120-S and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Officer W-2s
- Prior-year return (for AAA balance, basis, and carryforwards)
- Shareholder basis worksheets (if losses flow through)
- Any supporting workpapers

## Workflow

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss to the book-to-tax reconciliation (M-1). Flag unexplained M-1 adjustments.
2. **Verify officer compensation** — Confirm officer wages on Form 1125-E tie to W-2s. Compare officer compensation to distributions: if distributions materially exceed compensation, flag the reasonable compensation issue. Reference the *David E. Watson, P.C.* line of cases and the FICA employment tax implications under IRC 3111/3121 — this is a well-known S-corp audit trigger.
3. **Verify Schedule K items** — Check each separately stated item (interest, dividends, Section 1231, credits, etc.) against source.
4. **Verify K-1 allocations** — Confirm K-1 totals for each shareholder sum to Schedule K. Verify ownership percentages are consistent with the shareholder agreement or prior-year return.
5. **Verify shareholder basis** — For each shareholder receiving a loss, check that the K-1 loss does not exceed stock plus debt basis. If basis worksheets are provided, cross-reference. If not provided and a loss flows through, flag as requiring basis documentation.
6. **Verify balance sheet (Schedule L)** — Tie beginning and ending balances to prior-year return and current trial balance. Flag unexplained changes.
7. **Verify AAA and M-2** — Confirm AAA beginning balance ties to prior-year return. Verify current-year movements are correctly reflected.
8. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
9. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

- **K-1 total mismatch** — K-1 allocations must equal Schedule K totals. Any discrepancy is a hard stop.
- **Any discrepancy beyond rounding** — Every variance outside the $10-$100 rounding range requires preparer review and correction before filing.
- **Shareholder loss without basis** — A loss flowing through to a shareholder without a basis worksheet is a hard stop requiring documentation.

## Red Flags

- Ordinary income/loss doesn't reconcile to the trial balance within a small rounding amount
- K-1 percentages don't match shareholder agreement
- AAA balance goes below zero without a distribution in excess of basis being flagged
- Officer compensation appears unreasonably low relative to S-corp income
- Distributions to shareholders significantly exceed officer W-2 wages — reasonable compensation risk
- Shareholder loss exceeds stock plus debt basis without supporting basis schedule
- Prior-year credits or carryforwards present but no schedule supporting the carryforward amount
- Cross-return coordination needed: K-1 amounts should tie to each shareholder's Form 1040, Schedule E

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

- Do not mark the return reviewed-complete if K-1 totals don't foot to Schedule K.
- Do not adjust AAA or basis without preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
- Do not dismiss findings because the dollar amount is small relative to gross receipts.
