---
name: fixed-assets
version: 1.2.0
description: |
  Review fixed asset additions, disposals, and the depreciation schedule.
  Applies the firm's capitalization threshold ($2,500 default) to determine
  capitalize vs. expense, evaluates Section 179 and bonus depreciation
  opportunities, handles special asset categories (leasehold improvements,
  software, IT assets), and verifies depreciation calculations.
trigger: |
  "fixed assets", "depreciation", "capitalize or expense", "R&M review",
  "asset additions", "fixed asset schedule", "should I capitalize this"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Fixed Assets: Capitalization Review & Depreciation Schedule

## Purpose

Ensure fixed asset additions are properly capitalized or expensed under the firm's capitalization policy, and that the depreciation schedule is accurate and complete. Evaluate accelerated depreciation opportunities (Section 179, bonus depreciation) and handle special asset categories.

## Required Inputs

- List of potential fixed asset additions for the period (from the GL or a listing)
- Firm's capitalization threshold (default: $2,500)
- Existing depreciation schedule (if reviewing depreciation)
- Description and cost of each item being evaluated

## Workflow

1. **Confirm capitalization threshold** — Default is $2,500. Confirm with the client's capitalization policy if different.
2. **Review each addition** — For each item:
   - Cost vs. threshold: capitalize if ≥ threshold, expense if < threshold
   - Nature: is this a new asset, an improvement (extends useful life), or routine repair and maintenance?
   - Asset class and useful life: what depreciation method and recovery period applies?
   - **Section 179 / bonus depreciation**: For each capitalized asset, evaluate §179 eligibility (property type, business use percentage) and the applicable bonus depreciation percentage. Default to the client's standing election policy (typically bonus depreciation at the current applicable rate). Flag for tax team review only when one of these triggers applies: aggregate §179 elections for the year are approaching the annual limitation; the client has material state tax exposure in a state that does not conform to federal bonus depreciation; the asset is listed property or has < 50% business use; or projected taxable income may not absorb a full §179 deduction.
3. **Special asset categories** — Apply category-specific rules:
   - **Leasehold improvements**: determine if this is qualified improvement property (QIP) eligible for 15-year recovery and bonus depreciation. If the remaining lease term is shorter than the recovery period, flag for review.
   - **Software**: apply internal-use software capitalization rules (ASC 350-40 for GAAP; Section 167 for tax). Distinguish development-stage costs (capitalize) from post-implementation costs (expense). Flag development-stage costs that may qualify for R&D credit instead of capitalization.
   - **IT assets**: computers and peripherals are 5-year MACRS property. Confirm correct asset class assignment.
4. **Flag R&M vs. capitalize judgment calls** — Items near the threshold or involving improvements vs. repairs require professional judgment.
5. **Review depreciation schedule** — Confirm new assets were added at the correct cost and date. Verify MACRS or GAAP depreciation calculations for the period.
6. **Identify disposals** — Check for assets that may have been disposed of during the period without being removed from the schedule.
7. **Summarize findings** — List of capitalize vs. expense recommendations with amounts, depreciation schedule issues, and accelerated depreciation opportunities.

## Control Points

- **Material capitalize/expense judgment calls** — Items near the threshold where the nature (improvement vs. repair) is unclear require manager review.
- **Partial-year assets** — Assets placed in service or disposed of mid-year need the correct convention applied (half-year, mid-quarter).
- **Section 179 limitation** — If Section 179 elections are approaching the annual limitation, flag for tax team confirmation before proceeding.

## Red Flags

- Large R&M expense spike — may indicate capitalization items were expensed
- Asset on the schedule with zero net book value still generating depreciation
- Addition with no supporting invoice or description
- Disposal of a high-value asset without a gain/loss entry
- Leasehold improvement on a lease with remaining term shorter than the recovery period
- Software costs that may include research-stage activities eligible for R&D credit instead of capitalization
- Section 179 election approaching annual limitation — confirm with tax team

## Output Format

1. Capitalize vs. expense recommendation table with amounts and rationale
2. Accelerated depreciation opportunities (Section 179 / bonus) with estimated tax impact
3. Special asset category notes (if applicable)
4. Depreciation schedule issues (if reviewed)
5. Journal entries needed (proposed, for manager approval)

## Safety Constraints

- Do not automatically capitalize or expense items above the materiality threshold without manager confirmation.
- Do not remove assets from the depreciation schedule without confirming disposal documentation exists.
