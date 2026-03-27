---
name: rd-analysis
version: 1.0.0
description: |
  Screen a business client for R&D tax credit study candidacy. Analyzes activities,
  entity type, and tax profile to determine whether a formal Section 41 R&D credit
  study is likely to generate material, usable credits worth the study fee.
trigger: |
  "R&D credit", "research credit", "should we do an R&D study",
  "research and development tax credit", "Section 41", "R&D analysis"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# R&D Analysis: Research & Development Tax Credit Candidate Screening

## Purpose

Determine whether a client is a strong candidate for a Section 41 R&D tax credit study before recommending one. The credit is available to businesses that conduct qualified research activities (QRAs) and is refundable or payroll-offset eligible for some small businesses.

## Required Inputs

- Business description and primary activities
- Industry
- Entity type (C-corp, S-corp, partnership) and tax profile
- Approximate annual W-2 wages for employees doing technical work
- Annual spend on supplies or contract research related to technical activities
- Whether the company has previously claimed the R&D credit
- Gross receipts for the past 5 years (for the alternative simplified credit base)

## Workflow

1. **Screen for qualified research activities** — Apply the four-part test:
   - Permitted purpose (new or improved product, process, software, technique, formula, or invention)
   - Technological uncertainty (not known in advance how to accomplish the goal)
   - Process of experimentation (testing alternatives to eliminate uncertainty)
   - Technological in nature (relies on engineering, science, computer science, or similar)
   Flag activities that clearly don't qualify (e.g., routine quality control, market research, social sciences).
2. **Estimate qualified research expenses (QREs)** — Wages for time spent on QRAs, supply costs, and 65% of contract research costs.
3. **Estimate the credit** — Apply the alternative simplified credit (ASC) method: 14% × (current-year QREs − 50% of average QREs for the prior 3 years). Or regular method if beneficial.
4. **Assess ability to use the credit** — C-corps: directly offset tax. Pass-throughs: flows to owners who must have sufficient tax liability. Startups: payroll tax offset election available for companies ≤5 years old with ≤$5M in gross receipts.
5. **Estimate study cost** — R&D credit studies typically range from $5,000-$25,000+ depending on complexity and number of employees interviewed.
6. **Produce recommendation** — Strong candidate, possible candidate, or not recommended.

## Control Points

- **Activities must meet the four-part test** — Do not recommend a study for activities that clearly don't qualify. The credit has been subject to IRS scrutiny, and overstated claims create audit risk.
- **Pass-through owner tax liability** — For S-corps and partnerships, confirm the owners have sufficient tax liability to use the credit before recommending.

## Red Flags

- Business is primarily in services with no technical development activities
- "R&D" activities described are really routine operations or incremental improvements to existing processes
- Business has a history of NOLs — credit may not be usable without the payroll tax offset election
- Prior-year returns show the credit was claimed aggressively — review for consistency

## Output Format

Candidate screening summary:
- Activity assessment against the four-part test
- Estimated QREs (wages, supplies, contract research)
- Estimated credit amount (ASC method)
- Ability to use assessment
- Estimated study cost range
- Estimated ROI
- Recommendation: Strong / Possible / Not Recommended
- Caveats and next steps

## Safety Constraints

- This is a screening tool, not a formal R&D study. Do not represent the output as documentation sufficient to support an R&D credit claim.
- Flag any activities that are borderline qualifiers — these require specialist review before claiming.
