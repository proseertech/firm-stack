---
name: 1065-review
version: 1.3.0
description: |
  Cross-reference a completed Form 1065 (partnership income tax return) against
  source documents — trial balance, Schedule K-1s, and supporting schedules —
  to verify income, deductions, credits, and partner allocations. Grades findings
  by severity, verifies partner outside basis, and flags audit risk items.
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

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences in the $10-$100 range are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross receipts, total assets, or net income to determine whether a variance is acceptable. That approach belongs in financial statement audits, not tax review.

Classify findings by severity (impact + risk) rather than by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about or consider low-severity. Severity is for prioritization, not filtering — all findings go in the table. A separate preparer review step decides what to act on; your job at this stage is coverage.

## Required Inputs

- Completed Form 1065 and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Partnership agreement (for allocation percentages and special allocations)
- Prior-year return (for capital account balances, basis, carryforwards)
- Partner basis schedules (if losses are allocated)
- Any supporting workpapers

## Workflow

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss through M-1. Flag unexplained book-to-tax adjustments.
2. **Verify Schedule K items** — Check each separately stated item against source (interest, dividends, Section 1231, QBI, credits, etc.).
3. **Verify K-1 allocations** — Confirm K-1 totals for all partners sum to Schedule K. Verify percentages tie to the partnership agreement or are consistent with prior year.
4. **Verify partner outside basis** — For each partner receiving a loss, confirm outside basis is sufficient. Outside basis = capital account (tax basis) + share of liabilities. If liabilities are allocated under IRC 752, check that recourse/nonrecourse allocation is consistent with the partnership agreement. Flag losses exceeding basis — these are suspended under IRC 704(d).
5. **Verify capital accounts (Schedule L and K-1 Part II)** — Tie beginning capital account balances to prior-year K-1s. Verify contributions, distributions, and income/loss allocations for each partner.
6. **Check for special allocations** — If the partnership agreement has special allocations, verify they are reflected in the K-1s. Reference IRC 704(b): special allocations must have substantial economic effect. If special allocations are present, flag that the economic effect test (or alternate test) should be documented.
7. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
8. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

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
- Partnership has not elected out of centralized partnership audit regime (BBA/CPAR) under IRC 6221(b) — entity-level audit adjustments possible; confirm election status
- Cross-return coordination needed: K-1 amounts should tie to each partner's Form 1040 or entity return

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
- Do not adjust capital accounts or basis without preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
