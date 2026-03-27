---
name: 1041-review
version: 1.2.0
description: |
  Cross-reference a completed Form 1041 (fiduciary income tax return) against
  source documents for grantor trusts, simple trusts, and complex trusts.
  Verifies income, deductions, distributable net income (DNI), and beneficiary
  allocations on Schedule K-1. Grades findings by severity, shows DNI
  calculation explicitly, and flags audit risk items.
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

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences in the $10-$100 range are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross income or trust assets to determine whether a variance is acceptable. That approach belongs in financial statement audits, not tax review.

Classify findings by severity (impact + risk) rather than by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, DNI miscalculation, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Do not dismiss or deprioritize findings because the dollar amount is small relative to gross income. A $500 error is still an error that needs correction.

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
   - **Note**: This skill covers trusts. For decedent estates during administration, additional considerations apply including IRC 642(c) charitable deductions and the IRC 645 election to treat a revocable trust as part of the estate.
2. **Reconcile income to source documents** — Tie interest, dividends, capital gains, and pass-through income to 1099s and K-1s.
3. **Verify deductions** — Confirm fiduciary fees, attorney fees, and other deductions are properly allocated between income and principal per the trust instrument.
4. **Verify DNI and distribution deduction** — Show the DNI calculation explicitly: gross income minus deductions allocable to income, with specific exclusion of capital gains allocated to corpus (unless the trust instrument or local law allocates gains to income). Confirm the income distribution deduction ties to actual distributions. For complex trusts, verify the 65-day election (IRC 663(b)) if distributions in the first 65 days of the following year are being treated as current-year distributions.
5. **Verify Schedule K-1 allocations** — Confirm K-1 totals for all beneficiaries sum to the income distribution deduction. Verify each K-1 character of income (ordinary, qualified dividends, capital gains) is correctly allocated.
6. **Verify tax computation** — Confirm the tax is calculated at trust rates (which compress quickly) or that the income is properly flowed out to beneficiaries.
7. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
8. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]." Include: trust compressed tax brackets — verify whether distributing more income to beneficiaries in lower brackets would reduce total tax.

## Control Points

- **DNI mismatch** — If K-1 totals don't match the income distribution deduction, this is a hard stop.
- **Trust instrument review** — Any deduction allocation question (income vs. principal) must be resolved against the trust instrument, not assumed.

## Red Flags

- Grantor trust return showing tax due (should be informational only)
- Simple trust accumulating income (violates simple trust requirement)
- Capital gains allocated to income rather than principal without trust instrument support
- Fiduciary fees appear unreasonable relative to trust assets
- Prior-year excess deductions or capital loss carryforwards with no supporting schedule
- Trust compressed tax brackets: income retained at trust level when distribution to lower-bracket beneficiaries would reduce total tax
- Cross-return coordination needed: K-1 amounts should tie to each beneficiary's Form 1040; if the trust receives K-1s from pass-throughs, those should tie to the issuing entity's return

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
- **Trust Type Confirmed** — Grantor / Simple / Complex with supporting rationale
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by dollar impact for preparer attention
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

## Safety Constraints

- Do not determine income vs. principal allocation without reference to the trust instrument.
- Do not mark the return reviewed-complete if K-1 totals don't foot to the income distribution deduction.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
- Do not dismiss findings because the dollar amount is small relative to gross income.
