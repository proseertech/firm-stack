---
name: 1041-review
version: 1.0.0
description: |
  Cross-reference a completed Form 1041 (fiduciary income tax return) against
  source documents for grantor trusts, simple trusts, and complex trusts.
  Verifies income, deductions, distributable net income (DNI), and beneficiary
  allocations on Schedule K-1.
trigger: |
  "review the 1041", "trust return review", "grantor trust", "fiduciary return",
  "1041 cross-reference", "tie out the trust return", "trust K-1 review"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1041 Review: Fiduciary Return Cross-Reference

## Purpose

Catch errors before a Form 1041 is filed. Verify that trust income, deductions, and beneficiary allocations tie to source documents and that the return is consistent with the trust instrument and applicable fiduciary accounting rules.

## Required Inputs

- Completed Form 1041 and all schedules (B, D, G, J, K-1s)
- Trust instrument (trust agreement or will)
- Financial statements or fiduciary accounting report for the tax year
- Source documents: 1099s, K-1s from pass-throughs, brokerage statements
- Prior-year return (for carryforwards, excess deductions)

## Workflow

1. **Identify trust type** — Confirm whether this is a grantor trust, simple trust, or complex trust. The reporting rules differ materially.
   - **Grantor trust**: Income taxed to grantor; return may be informational only.
   - **Simple trust**: Required to distribute all income; no charitable deduction.
   - **Complex trust**: May accumulate income; may have charitable deduction.
2. **Reconcile income to source documents** — Tie interest, dividends, capital gains, and pass-through income to 1099s and K-1s.
3. **Verify deductions** — Confirm fiduciary fees, attorney fees, and other deductions are properly allocated between income and principal per the trust instrument.
4. **Verify DNI and distribution deduction** — Recalculate distributable net income (Schedule B) and confirm the income distribution deduction ties to actual distributions.
5. **Verify Schedule K-1 allocations** — Confirm K-1 totals for all beneficiaries sum to the income distribution deduction. Verify each K-1 character of income (ordinary, qualified dividends, capital gains) is correctly allocated.
6. **Verify tax computation** — Confirm the tax is calculated at trust rates (which compress quickly) or that the income is properly flowed out to beneficiaries.
7. **Summarize findings** — Confirmed, variances, preparer questions.

## Control Points

- **DNI mismatch** — If K-1 totals don't match the income distribution deduction, this is a hard stop.
- **Trust instrument review** — Any deduction allocation question (income vs. principal) must be resolved against the trust instrument, not assumed.

## Red Flags

- Grantor trust return showing tax due (should be informational only)
- Simple trust accumulating income (violates simple trust requirement)
- Capital gains allocated to income rather than principal without trust instrument support
- Fiduciary fees appear unreasonable relative to trust assets
- Prior-year excess deductions or capital loss carryforwards with no supporting schedule

## Output Format

Structured findings report: Trust Type Confirmed, Confirmed Items, Variances, Preparer Questions.

## Safety Constraints

- Do not determine income vs. principal allocation without reference to the trust instrument.
- Do not mark the return reviewed-complete if K-1 totals don't foot to the income distribution deduction.
