---
name: fixed-assets
version: 1.3.0
description: |
  Reviews fixed asset additions, disposals, and the depreciation schedule, and
  decides capitalize vs. expense against the firm's capitalization threshold
  ($2,500 default). Use whenever someone is looking at asset purchases, a repairs
  & maintenance account, or a depreciation schedule — "should we capitalize this
  or expense it," "is this a repair or an improvement," "review the fixed asset
  additions," "why did R&M spike," "check the depreciation," "can we take 179 or
  bonus on this," "what's the useful life," "did we book the disposal." Covers
  Section 179 and bonus depreciation eligibility, special categories (leasehold
  improvements / QIP, internal-use software, IT assets), MACRS lives and
  conventions, and disposals. Fire it even when the form or the word
  "depreciation" isn't said, as long as the question is about whether a cost gets
  capitalized or how an asset is being depreciated.
trigger: |
  "fixed assets", "depreciation", "capitalize or expense", "capitalize vs expense",
  "R&M review", "repairs and maintenance", "repair or improvement",
  "asset additions", "fixed asset schedule", "depreciation schedule",
  "should I capitalize this", "should we expense this", "useful life",
  "Section 179", "bonus depreciation", "179 or bonus", "leasehold improvement",
  "QIP", "MACRS", "did we book the disposal", "asset disposal"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Fixed Assets: Capitalization Review & Depreciation Schedule

## Purpose

Ensure fixed asset additions are properly capitalized or expensed under the firm's capitalization policy, and that the depreciation schedule is accurate and complete. Evaluate accelerated depreciation opportunities (Section 179, bonus depreciation) and handle special asset categories. The value is a defensible capitalize/expense call and a clean schedule — each recommendation tied to a specific item, its cost, and the rule that governs it.

## Required Inputs

Confirm these before starting. A capitalize/expense review run without the actual costs and descriptions produces guesses, and a wrong call surfaces only in a later depreciation true-up or an exam.

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

Stop and get a human decision before proceeding when:

- **Material capitalize/expense judgment calls** — Items near the threshold where the nature (improvement vs. repair) is unclear require manager review. The improvement-vs-repair line is a judgment call with real tax timing consequences, not a formula.
- **Partial-year assets** — Assets placed in service or disposed of mid-year need the correct convention applied (half-year, mid-quarter). The mid-quarter convention triggers off aggregate Q4 additions, so the right convention can't be settled item by item — confirm the period's full addition pattern.
- **Section 179 limitation** — If Section 179 elections are approaching the annual limitation, flag for tax team confirmation before proceeding. An election booked over the limit gets disallowed and has to be unwound after the fact.

## Red Flags

Pause and surface to the user when you see:

- **Large R&M expense spike** — may indicate capitalization items were buried in repairs & maintenance; scan the account for individual items at or above the threshold and re-test them as improvements.
- **Zero net book value asset still generating depreciation** — a fully depreciated asset can't take further deprecation; the schedule likely has a cost/basis or accumulated-depreciation error.
- **Addition with no supporting invoice or description** — you can't classify or assign a life to a cost you can't see; request the source document before deciding.
- **Disposal of a high-value asset without a gain/loss entry** — the asset left the balance sheet but the gain or loss on disposal was never booked.
- **Leasehold improvement on a lease with remaining term shorter than the recovery period** — recovery period and lease term are mismatched; flag for review.
- **Software costs that may include research-stage activities** — these may be eligible for R&D credit instead of capitalization; route to the tax team before capitalizing.
- **Section 179 election approaching the annual limitation** — confirm with the tax team before electing further.

## Output Format

1. Capitalize vs. expense recommendation table with amounts and rationale
2. Accelerated depreciation opportunities (Section 179 / bonus) with estimated tax impact
3. Special asset category notes (if applicable)
4. Depreciation schedule issues (if reviewed)
5. Journal entries needed (proposed, for manager approval)

## Safety Constraints

- Recommend, don't decide, on items above the materiality threshold — surface the capitalize/expense call for manager confirmation rather than booking it, since the treatment drives the client's tax timing.
- Do not remove an asset from the depreciation schedule without confirming disposal documentation exists — dropping an asset that was never actually disposed of overstates the loss and leaves the books wrong.
- Journal entries are proposed for approval, never posted directly.
