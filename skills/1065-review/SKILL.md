---
name: 1065-review
version: 1.0.0
description: |
  Cross-reference a completed Form 1065 (partnership income tax return) against
  source documents — trial balance, Schedule K-1s, and supporting schedules —
  to verify income, deductions, credits, and partner allocations.
trigger: |
  "review the 1065", "partnership return review", "check the K-1s", "1065 cross-reference",
  "tie out the partnership return", "verify the 1065"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1065 Review: Partnership Return Cross-Reference

## Purpose

Catch errors before a Form 1065 is filed. Verify that income, deductions, and partner allocations tie to the trial balance and source documents, and that K-1 totals are mathematically consistent with Schedule K.

## Required Inputs

- Completed Form 1065 and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Partnership agreement (for allocation percentages and special allocations)
- Prior-year return (for capital account balances, basis, carryforwards)
- Any supporting workpapers

## Workflow

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss through M-1. Flag unexplained book-to-tax adjustments.
2. **Verify Schedule K items** — Check each separately stated item against source (interest, dividends, Section 1231, QBI, credits, etc.).
3. **Verify K-1 allocations** — Confirm K-1 totals for all partners sum to Schedule K. Verify percentages tie to the partnership agreement or are consistent with prior year.
4. **Verify capital accounts (Schedule L and K-1 Part II)** — Tie beginning capital account balances to prior-year K-1s. Verify contributions, distributions, and income/loss allocations for each partner.
5. **Check for special allocations** — If the partnership agreement has special allocations, verify they are reflected in the K-1s and have substantial economic effect.
6. **Summarize findings** — Confirmed items, variances, preparer questions.

## Control Points

- **K-1 total mismatch** — K-1 allocations must equal Schedule K totals. Any discrepancy is a hard stop.
- **Capital account method** — Confirm whether capital accounts are reported on tax basis, GAAP, Section 704(b), or other. Flag if the method changed from prior year.

## Red Flags

- K-1 percentages don't match the partnership agreement
- Capital account balances don't foot to the balance sheet
- Large guaranteed payment without a corresponding expense deduction
- Negative capital accounts without a deficit restoration obligation or qualified income offset
- 743(b) or 734(b) adjustments present but no supporting schedule

## Output Format

Structured findings report: Confirmed, Variances, Missing Support, Preparer Questions.

## Safety Constraints

- Do not mark the return reviewed-complete if K-1 totals don't foot to Schedule K.
- Do not adjust capital accounts or basis without preparer review.
