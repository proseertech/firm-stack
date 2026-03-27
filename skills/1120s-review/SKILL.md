---
name: 1120s-review
version: 1.0.0
description: |
  Cross-reference a completed Form 1120-S (S-corporation income tax return) against
  source documents — trial balance, Schedule K-1s, officer W-2s, and supporting
  schedules — to verify income, deductions, credits, and shareholder allocations.
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

## Required Inputs

- Completed Form 1120-S and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Officer W-2s
- Prior-year return (for AAA balance, basis, and carryforwards)
- Any supporting workpapers

## Workflow

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss to the book-to-tax reconciliation (M-1). Flag unexplained M-1 adjustments.
2. **Verify officer compensation** — Confirm officer wages on Form 1125-E tie to W-2s and are reasonable relative to income.
3. **Verify Schedule K items** — Check each separately stated item (interest, dividends, Section 1231, credits, etc.) against source.
4. **Verify K-1 allocations** — Confirm K-1 totals for each shareholder sum to Schedule K. Verify ownership percentages are consistent with the shareholder agreement or prior-year return.
5. **Verify balance sheet (Schedule L)** — Tie beginning and ending balances to prior-year return and current trial balance. Flag material unexplained changes.
6. **Verify AAA and M-2** — Confirm AAA beginning balance ties to prior-year return. Verify current-year movements are correctly reflected.
7. **Summarize findings** — Confirmed items, variances, and preparer questions.

## Control Points

- **K-1 total mismatch** — K-1 allocations must equal Schedule K totals. Any discrepancy is a hard stop.
- **Material variance** — Discrepancies above the firm's materiality threshold require preparer correction before filing.

## Red Flags

- Ordinary income/loss doesn't reconcile to the trial balance within a small rounding amount
- K-1 percentages don't match shareholder agreement
- AAA balance goes below zero without a distribution in excess of basis being flagged
- Officer compensation appears unreasonably low relative to S-corp income
- Prior-year credits or carryforwards present but no schedule supporting the carryforward amount

## Output Format

Structured findings report:
- **Confirmed** — Line items that tie
- **Variances** — Discrepancies with amounts and source
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment

## Safety Constraints

- Do not mark the return reviewed-complete if K-1 totals don't foot to Schedule K.
- Do not adjust AAA or basis without preparer review.
