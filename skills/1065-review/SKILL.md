---
name: 1065-review
version: 1.1.0
description: |
  Cross-reference a completed Form 1065 (partnership income tax return) against
  source documents — trial balance, Schedule K-1s, and supporting schedules —
  to verify income, deductions, credits, and partner allocations. Quantifies
  materiality, grades findings by severity, verifies partner outside basis,
  and flags audit risk items.
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
- Partner basis schedules (if losses are allocated)
- Any supporting workpapers

## Workflow

1. **Establish materiality and scope** — Quantify materiality for this return. Use the firm's configured materiality threshold; if not configured, use 2% of total gross receipts as working materiality. Every finding in subsequent steps is classified as material or immaterial relative to this threshold.
2. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss through M-1. Flag unexplained book-to-tax adjustments.
3. **Verify Schedule K items** — Check each separately stated item against source (interest, dividends, Section 1231, QBI, credits, etc.).
4. **Verify K-1 allocations** — Confirm K-1 totals for all partners sum to Schedule K. Verify percentages tie to the partnership agreement or are consistent with prior year.
5. **Verify partner outside basis** — For each partner receiving a loss, confirm outside basis is sufficient. Outside basis = capital account (tax basis) + share of liabilities. If liabilities are allocated under IRC 752, check that recourse/nonrecourse allocation is consistent with the partnership agreement. Flag losses exceeding basis — these are suspended under IRC 704(d).
6. **Verify capital accounts (Schedule L and K-1 Part II)** — Tie beginning capital account balances to prior-year K-1s. Verify contributions, distributions, and income/loss allocations for each partner.
7. **Check for special allocations** — If the partnership agreement has special allocations, verify they are reflected in the K-1s. Reference IRC 704(b): special allocations must have substantial economic effect. If special allocations are present, flag that the economic effect test (or alternate test) should be documented.
8. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
9. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

- **K-1 total mismatch** — K-1 allocations must equal Schedule K totals. Any discrepancy is a hard stop.
- **Capital account method** — Confirm whether capital accounts are reported on tax basis, GAAP, Section 704(b), or other. Flag if the method changed from prior year.
- **Partner loss without basis** — A loss allocated to a partner without documented outside basis is a hard stop requiring documentation.

## Red Flags

- K-1 percentages don't match the partnership agreement
- Capital account balances don't foot to the balance sheet
- Large guaranteed payment without a corresponding expense deduction
- Negative capital accounts without a deficit restoration obligation or qualified income offset
- 743(b) or 734(b) adjustments present but no supporting schedule
- Partner's share of loss exceeds outside basis — loss limitation applies under IRC 704(d)
- Liability allocations under IRC 752 not documented — affects outside basis for all partners
- Guaranteed payments: confirm deductibility and self-employment tax treatment
- Cross-return coordination needed: K-1 amounts should tie to each partner's Form 1040 or entity return

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X] (X% of gross receipts)
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into sections:
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW)
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

## Safety Constraints

- Do not mark the return reviewed-complete if K-1 totals don't foot to Schedule K.
- Do not adjust capital accounts or basis without preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
