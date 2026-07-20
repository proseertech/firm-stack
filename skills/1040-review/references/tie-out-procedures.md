# 1040 Tie-Out Procedures and Special Cases

Detailed, line-by-line tie-out for the "tie out every line" phase of the 1040 review
(Phase D in SKILL.md). Work through each income, deduction, credit, and withholding
category below. The special cases flagged in **bold** are the ones that most often cost a
firm money when missed — read them, don't skim them.

---

## Source-document special cases (document-inventory phase)

Two situations look like errors but aren't, and one looks fine but hides omitted income:

- **Consolidated 1099 sub-account mapping.** When a taxpayer has consolidated 1099s (e.g.,
  Morgan Stanley), map each account number on the return's Interest & Dividend Summary back to
  a specific sub-account within the consolidated 1099 in the workpapers. Confirming "a Morgan
  Stanley 1099 exists" is not enough — income from an unmapped sub-account can be silently
  omitted. Confirm coverage of each sub-account individually.
- **Revocable / grantor trust 1099s.** If any 1099 is in the name of a revocable or grantor
  trust, confirm the trust is disregarded for income tax purposes and all income is properly
  reported on the grantor's 1040. This is correct treatment — do not flag it as a name mismatch.

---

## Wages and compensation

Tie W-2 Box 1 wages to Line 1a. Check Box 12 codes for deferred comp, HSA, etc.

## Investment income

Tie 1099-INT, 1099-DIV, and Schedule B. Verify 1099-B transactions on Schedule D / Form 8949.

- **Structured notes / auto-call income.** Check 1099-MISC Box 3 for structured note or
  contingent coupon income (e.g., "BNS CI AUTO TSLA", "GS CI AUTO NVDA"). This is ordinary income
  that should flow to Form 8960 (NIIT) as investment income. Verify the income type is coded
  correctly for NIIT purposes — the software may not automatically classify it.
- **Brokerage cash bonuses.** Promotional bonuses from brokerages (CashPlus, sign-up bonuses)
  also appear on 1099-MISC Box 3. These are ordinary income, not investment income. Small amounts
  ($500-$1,000 range) but commonly recurring.

## Retirement income

Tie 1099-R distributions to Line 4 or 5. Verify taxable amount and any rollover exclusions.

## Pass-through income

Tie each K-1 to the appropriate schedule (E, F, etc.). For each pass-through entity reporting a
loss, work the limitation stack in order — each gate below can reduce the deductible loss, and
skipping one lets a non-deductible loss reach the return:

- **Basis limitation.** Does the taxpayer have sufficient basis to absorb the loss? If no basis
  worksheet is provided and a loss is claimed, this is a hard stop — flag as requiring basis
  documentation.
- **At-risk limitation.** Is Form 6198 present? If losses are claimed from an activity, at-risk
  must be addressed.
- **Passive activity.** Is Form 8582 present? Flag any pass-through loss flowing through without
  Form 8582 when the taxpayer has W-2 income (suggesting they may not materially participate).
- **QBI deduction.** Verify the Section 199A computation. Flag if income is from a specified
  service trade or business (SSTB) above the income threshold without a phase-out calculation.
- **Cost segregation losses.** If a large rental loss is present, determine whether it is driven
  by a cost segregation study. If so, verify:
  - Real estate professional status — 750-hour log and material participation documentation
  - Correct bonus depreciation rate for the tax year
  - Cost seg study report on file
  - Whether the loss is passive or nonpassive based on RE pro qualification

## Deductions and credits

Check Schedule A itemized deductions or standard deduction. Verify credits (child tax, EV,
education, etc.) against supporting forms.

- **SALT cap.** When verifying Schedule A, check the SALT limitation on Line 5e against the
  current-year statutory cap. Do not hardcode the cap amount — reference the applicable limit for
  the tax year under review (e.g., $10,000 under original TCJA; $40,000 under One Big Beautiful
  Bill for 2025+). Confirm the software is applying the correct cap.

## Withholding and estimated payments

Tie federal withholding to all W-2s and 1099s. Verify estimated tax payments against IRS records
if available.

## Carryovers

Review the tax software's "Tax Return Carryovers to [Next Year]" schedule:

- Verify prior-year carryovers were correctly brought forward from the prior return's carryforward
  schedule.
- Verify current-year carryovers are reasonable given the return's activity.
- Specifically reconcile: capital loss carryovers, passive loss carryovers (Form 8582), and
  foreign tax credit carryovers (Form 1116).
