---
name: costseg-analysis
version: 1.0.0
description: |
  Screen a real property client for cost segregation study candidacy. Analyzes
  property type, cost basis, acquisition date, tax profile, and depreciation
  history to determine whether a cost seg study is likely to generate material
  tax savings worth the study fee.
trigger: |
  "cost seg", "cost segregation", "bonus depreciation candidate",
  "should we do a cost seg", "accelerated depreciation", "cost seg analysis"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# Cost Seg Analysis: Cost Segregation Study Candidate Screening

## Purpose

Determine whether a client is a strong candidate for a cost segregation study before recommending one. A cost seg is only worthwhile if the tax savings exceed the study fee and the client can use the resulting deductions.

## Required Inputs

- Property type (commercial, industrial, multifamily, mixed-use)
- Property cost basis or acquisition price
- Year placed in service or acquisition date
- Client's tax profile: entity type, tax bracket, current and projected taxable income
- Whether bonus depreciation was previously taken on the property
- Whether the client has passive activity limitations, NOL carryforwards, or other constraints that could limit benefit

## Workflow

1. **Assess property eligibility** — Cost segs are most valuable for: commercial/industrial/multifamily properties, cost basis ≥ $500K, placed in service within the last 15 years (or newly acquired), and clients with sufficient taxable income to use the deductions.
2. **Estimate potential benefit** — Typical reclassification percentages by property type (e.g., 20-40% of cost to 5/7/15-year property). Apply current bonus depreciation percentage (currently phasing down post-TCJA).
3. **Assess ability to use the deductions** — Check for passive activity rules, at-risk limitations, NOLs that would absorb the deduction anyway, or AMT exposure.
4. **Estimate study cost** — Typical cost seg study fees range from $5,000-$15,000+ depending on property size and complexity.
5. **Compute ROI** — Estimate first-year tax savings vs. study fee. A ratio of ≥ 3:1 is generally a good candidate.
6. **Produce recommendation** — Strong candidate, possible candidate (needs more analysis), or not recommended (with reason).

## Control Points

- **Passive activity limitation** — If the client is subject to passive activity rules for this property, confirm they have sufficient passive income to absorb the accelerated deductions before recommending.
- **Look-back study** — If the property was placed in service in a prior year, a look-back study may trigger a catch-up deduction in the current year — confirm the client can absorb the one-time deduction.

## Red Flags

- Property is entirely land (not depreciable)
- Client has large NOL carryforwards — accelerating depreciation may have minimal benefit
- Bonus depreciation percentage is low and the reclassified property life isn't materially shorter than the original classification
- Client plans to sell the property soon — depreciation recapture could offset the benefit

## Output Format

Candidate screening summary:
- Property details and eligibility assessment
- Estimated reclassification and first-year deduction
- Estimated tax savings (with assumed rate)
- Estimated study cost range
- Estimated ROI
- Recommendation: Strong / Possible / Not Recommended
- Caveats and next steps

## Safety Constraints

- This is a screening tool, not a study. Do not represent the output as a cost segregation study.
- Do not make a definitive recommendation without confirming the client's ability to use the deductions.
