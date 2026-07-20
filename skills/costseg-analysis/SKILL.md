---
name: costseg-analysis
version: 1.1.0
description: |
  Screen a real property client for cost segregation study candidacy — decide
  whether a study is worth commissioning before you recommend one. Weighs property
  type, cost basis, placed-in-service date, the client's tax profile, and prior
  depreciation to estimate first-year benefit against the study fee. Use this
  whenever someone is weighing accelerated depreciation on a building: "should we
  do a cost seg on this property", "is this client a cost seg candidate", "would a
  cost seg pay off", "they just bought a building — worth accelerating depreciation?",
  "can we free up depreciation this year", or a look-back / catch-up study question —
  even if they don't say "cost segregation." This is a candidacy screen, not the study.
trigger: |
  "cost seg", "cost segregation", "cost seg analysis", "should we do a cost seg",
  "is this a cost seg candidate", "would a cost seg pay off", "bonus depreciation candidate",
  "accelerated depreciation", "accelerate depreciation on the building", "reclassify building components",
  "5/7/15-year property", "look-back study", "catch-up depreciation", "they bought a building"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# Cost Seg Analysis: Cost Segregation Study Candidate Screening

## Purpose

Decide whether a real property client is a strong enough candidate to justify commissioning a cost segregation study — before you recommend one. A study reclassifies building components into shorter-life (5/7/15-year, §1245) property so they depreciate faster instead of over 27.5/39 years (§1250). It only pays off when the accelerated deductions are large enough to beat the study fee *and* the client can actually use them this year. This screen produces a go / maybe / no call with the numbers behind it; it is not the study itself.

## Scope & Handoffs

- This is a **candidacy screen**, not a cost segregation study — do not represent the output as one.
- R&D credit candidacy → **`rd-analysis`**. Open-ended "how should we treat this depreciation position" research → **`tax-advisor`**.

## Required Inputs

Confirm these before screening. If key facts are missing, ask — a benefit estimate built on a guessed basis or placed-in-service year is worthless.

- **Property type** — commercial, industrial, multifamily, mixed-use (drives typical reclassification %)
- **Cost basis** or acquisition price (land excluded — land is not depreciable)
- **Placed-in-service or acquisition date**
- **Tax profile** — entity type, marginal rate, current and projected taxable income
- **Prior depreciation** — whether bonus depreciation was already taken on this property
- **Usability constraints** — passive activity limitations, at-risk limits, NOL carryforwards, or AMT exposure that could keep the client from using the deductions this year

## Workflow

1. **Assess property eligibility.** Best candidates: commercial / industrial / multifamily / mixed-use property, cost basis ≥ $500K, placed in service within roughly the last 15 years (or newly acquired), owned by a client with enough taxable income to absorb the deductions. Note any factor that falls short — a $300K basis or a client with no current income changes the answer.
2. **Estimate potential benefit.** Apply a typical reclassification range for the property type (commonly ~20–40% of cost moved into 5/7/15-year property). Then apply the bonus depreciation rate **in effect for the placed-in-service year**. OBBBA (2025) permanently restored **100% bonus depreciation** for qualifying property acquired and placed in service after Jan 19, 2025; property acquired on or before that date remains on the prior phase-down (40% in 2025, 20% in 2026). Confirm the rate for the specific acquisition and placed-in-service dates rather than assuming — it materially changes the first-year number.
3. **Test whether the client can use the deductions.** Screen for passive activity rules, at-risk limitations, NOLs that would absorb the deduction anyway, and AMT exposure. A large deduction the client cannot use this year is not a benefit — it is a deferral.
4. **Estimate study cost.** Cost seg study fees typically run $5,000–$15,000+, scaling with property size and complexity.
5. **Compute ROI.** Estimated first-year tax savings ÷ study fee. A ratio of roughly ≥ 3:1 generally signals a good candidate; state the ratio, not just a verdict.
6. **Produce the recommendation.** Strong candidate / possible candidate (needs more analysis) / not recommended — each with the reason and the numbers behind it.

## Control Points

Stop and get the client's or CPA's confirmation before recommending when:

- **Passive activity limitation applies.** If this property is a passive activity for the client, confirm they have enough passive income to absorb the accelerated deductions — otherwise the benefit is suspended, not realized.
- **The property was placed in service in a prior year (look-back study).** A look-back can trigger a one-time §481(a) catch-up deduction in the current year via an accounting-method change. Confirm the client can absorb that lump deduction this year before recommending.

## Red Flags

Pause and surface to the user when:

- The property is entirely land — nothing to depreciate, so nothing to reclassify.
- The client has large NOL carryforwards — accelerating depreciation may add little, since income is already sheltered.
- The applicable bonus depreciation rate is low (e.g., transitional or pre-2025 phase-down property) **and** the reclassified property lives aren't materially shorter than their current classification — the acceleration may not clear the study fee.
- The client plans to sell the property soon — depreciation recapture on the accelerated portion could claw back much of the benefit.

## Output Format

A candidate screening summary:

- Property details and eligibility assessment
- Estimated reclassification (% and $) and first-year deduction
- Estimated tax savings, with the assumed marginal rate stated
- Estimated study cost range
- Estimated ROI ratio
- Recommendation: **Strong / Possible / Not Recommended**, with the driving reason
- Caveats and next steps (including that a firm number requires the actual study)

## Safety Constraints

- This is a screening tool, not a study — never represent the output as a cost segregation study or as a filing-ready deduction figure.
- Do not make a definitive recommendation without confirming the client can actually use the deductions this year (usability drives the whole analysis).
- The first-year number turns on the current bonus depreciation rate — verify the rate for the placed-in-service year rather than assuming, since it changes with legislation.
