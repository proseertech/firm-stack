---
name: fixed-assets
version: 1.0.0
description: |
  Review fixed asset additions, disposals, and the depreciation schedule.
  Applies the firm's capitalization threshold ($2,500 default) to determine
  capitalize vs. expense, and verifies depreciation calculations.
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

Ensure fixed asset additions are properly capitalized or expensed under the firm's capitalization policy, and that the depreciation schedule is accurate and complete.

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
3. **Flag R&M vs. capitalize judgment calls** — Items near the threshold or involving improvements vs. repairs require professional judgment.
4. **Review depreciation schedule** — Confirm new assets were added at the correct cost and date. Verify MACRS or GAAP depreciation calculations for the period.
5. **Identify disposals** — Check for assets that may have been disposed of during the period without being removed from the schedule.
6. **Summarize findings** — List of capitalize vs. expense recommendations with amounts, plus depreciation schedule issues.

## Control Points

- **Material capitalize/expense judgment calls** — Items near the threshold where the nature (improvement vs. repair) is unclear require manager review.
- **Partial-year assets** — Assets placed in service or disposed of mid-year need the correct convention applied (half-year, mid-quarter).

## Red Flags

- Large R&M expense spike — may indicate capitalization items were expensed
- Asset on the schedule with zero net book value still generating depreciation
- Addition with no supporting invoice or description
- Disposal of a high-value asset without a gain/loss entry

## Output Format

1. Capitalize vs. expense recommendation table with amounts
2. Depreciation schedule issues (if reviewed)
3. Journal entries needed (proposed, for manager approval)

## Safety Constraints

- Do not automatically capitalize or expense items above the materiality threshold without manager confirmation.
- Do not remove assets from the depreciation schedule without confirming disposal documentation exists.
