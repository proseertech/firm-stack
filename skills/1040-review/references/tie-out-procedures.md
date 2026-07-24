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

## Filing status and dependents (page 1)

The line tie-out starts at income, but header errors are invisible to it — check page 1 first:

- Filing status is consistent with the facts in the file (marriage, divorce, death of spouse,
  head-of-household support test). A status change from prior year should have a known reason.
- Dependent names and SSNs tie to the prior-year return; a dropped or added dependent should be
  explained. A dependent's own return must be marked "can be claimed as a dependent."
- **CTC vs. ODC age test.** Child tax credit requires the child to be under 17 at year-end; older
  dependents get the credit for other dependents. Software applies whatever birthdate was entered —
  verify against the prior year, because a child aging out of CTC is a real tax change that looks
  like an error but isn't (and the reverse is an error that looks fine).
- For divorced/separated parents claiming a noncustodial child, confirm Form 8332 (or equivalent
  release) is on file.

## Wages and compensation

Tie W-2 Box 1 wages to Line 1a. Check Box 12 codes for deferred comp, HSA, etc.

- **Equity compensation basis reconciliation.** If W-2 Box 12 shows Code V (NQSO exercise) or the
  wage detail shows RSU vesting income, look for same-year sales on the 1099-B. Broker-reported
  basis typically excludes the compensation element already taxed in wages — verify the Form 8949
  basis adjustment (code B) so the spread isn't taxed twice. This is the most common 1040 error at
  firms with equity-comp clients; a 1099-B that "ties" at broker basis is exactly the failure mode.
- **Excess Social Security withholding.** If one taxpayer has two or more W-2s, total the Box 4
  amounts. Combined withholding above the annual maximum is a refundable credit on Schedule 3 —
  software only catches it when both W-2s are keyed to the same spouse, so verify the assignment.

## Investment income

Tie 1099-INT, 1099-DIV, and Schedule B. Verify 1099-B transactions on Schedule D / Form 8949.

- **Structured notes / auto-call income.** Check 1099-MISC Box 3 for structured note or
  contingent coupon income (e.g., "BNS CI AUTO TSLA", "GS CI AUTO NVDA"). This is ordinary income
  that should flow to Form 8960 (NIIT) as investment income. Verify the income type is coded
  correctly for NIIT purposes — CCH Axcess may not automatically classify it.
- **Brokerage cash bonuses.** Promotional bonuses from brokerages (CashPlus, sign-up bonuses)
  also appear on 1099-MISC Box 3. These are ordinary income, not investment income. Small amounts
  ($500-$1,000 range) but commonly recurring.
- **Form 8960 completeness.** When MAGI exceeds the NIIT threshold, confirm Form 8960 includes
  *all* net investment income — interest, dividends, capital gains, passive K-1 income, net rental
  income — not just the structured-note items above. An incomplete 8960 understates tax at 3.8% of
  whatever was left out.

## Retirement income

Tie 1099-R distributions to Line 4 or 5. Verify taxable amount and any rollover exclusions.

Read the distribution codes, not just the amounts:

- **RMD verification.** If the taxpayer is at or past RMD age (73), confirm required minimum
  distributions were taken from each applicable account. A missed RMD carries a 25% excise (10% if
  timely corrected) and needs Form 5329 with a waiver request — not silence.
- **Code 1 (early distribution).** Requires the 10% additional tax or Form 5329 claiming a
  documented exception. A code-1 distribution with neither is a finding.
- **QCD verification.** A qualified charitable distribution (code Y) is excluded from income only
  if paid directly from the IRA to the charity and the taxpayer is 70½+; confirm the "QCD" notation
  next to Line 4b and that the same contribution isn't also deducted on Schedule A.

## Real estate sales

Inventory Forms 1099-S and Closing Disclosures — 1099-S is IRS-matched, so an unreported sale
generates a CP2000 on full gross proceeds:

- If the principal residence was sold, verify the Section 121 exclusion support (2-of-5-year
  ownership and use) and the exclusion limit for the filing status.
- **Report the sale whenever a 1099-S was issued**, even if the gain is fully excluded — exclusion
  without reporting still draws the matching notice.
- If a home office or rental use existed, verify depreciation recapture — the recaptured portion
  is not excludable under Section 121.

## Other income (1099-G, W-2G, 1099-K, 1099-Q, 1099-SA)

- **1099-G.** State refunds are taxable only to the extent the prior-year SALT deduction produced
  a benefit (Rev. Rul. 2019-11) — check the prior-year Schedule A against the applicable cap; with
  the higher 2025+ cap, more refunds are partially taxable than under the $10,000 years.
  Unemployment compensation is fully taxable.
- **W-2G.** Gambling winnings tie to Line 8b; losses are deductible only up to winnings and only
  if itemizing.
- **1099-K.** For personal items sold at a loss, verify the offsetting entry at the top of
  Schedule 1 rather than netting to zero silently.
- **1099-Q / 1099-SA.** Confirm distributions are matched to qualified education or medical
  expenses; unmatched distributions are taxable plus penalty.

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
- **Excess business loss (Section 461(l)).** The final gate: aggregate business losses above the
  inflation-adjusted annual threshold (per filing status) are disallowed and become an NOL
  carryforward. Verify Form 461 is present when combined Schedule C/E/F losses are large — a loss
  that cleared basis, at-risk, and passive can still be limited here, and skipping this gate lets
  a non-deductible loss reach the return.
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
  Bill for 2025+). Confirm CCH Axcess is applying the correct cap.
- **Mortgage interest.** Tie Schedule A interest to Forms 1098. When principal balances are large,
  verify the acquisition-debt limitation was actually applied — $750,000 for debt incurred after
  12/15/2017, $1,000,000 for grandfathered debt — software applies the limit only if the
  average-balance inputs were entered, and that input is commonly skipped. Home-equity interest is
  deductible only to the extent the proceeds acquired or improved the residence; ask for the
  tracing rather than assuming.
- **Charitable substantiation.** Noncash gifts over $500 need Form 8283; over $5,000 need a
  qualified appraisal and signed Form 8283 Section B; any single cash gift of $250+ needs a
  contemporaneous written acknowledgment on file. Substantiation failure is 100% disallowance
  regardless of proof of payment, so a missing acknowledgment is a real finding, not housekeeping.
- **Premium tax credit (Form 1095-A → Form 8962).** If a Form 1095-A exists or Marketplace
  coverage is indicated anywhere in the file, Form 8962 must be attached reconciling advance
  credits. A 1095-A with no 8962 is an automatic e-file reject or guaranteed IRS correspondence,
  and unreconciled excess advance credit changes the balance due.

## Withholding and estimated payments

Tie federal withholding to all W-2s and 1099s. Verify estimated tax payments against IRS records
if available.

- **Additional Medicare tax (Form 8959).** When earned income exceeds the threshold for the filing
  status, verify Form 8959 is present and reconcile the additional withholding in W-2 Box 6 to it —
  the Box 1/Box 2 tie the review already does doesn't cover Box 6, and the mismatch is a purely
  mechanical catch.

## Carryovers

Review the CCH Axcess Carryover worksheet ("Tax Return Carryovers to [Next Year]"):

- Verify prior-year carryovers were correctly brought forward from the prior return's carryforward
  schedule.
- Verify current-year carryovers are reasonable given the return's activity.
- Specifically reconcile: capital loss carryovers, passive loss carryovers (Form 8582), and
  foreign tax credit carryovers (Form 1116).
