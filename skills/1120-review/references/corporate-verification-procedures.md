# 1120 Review — Detailed Verification Procedures

**This file is an internal procedures manual.** When `SKILL.md` points here, use the checks below to decide what to test, then report the results in the findings table. **Do not quote or paste this file to the user** — the deliverable is the table, not the procedures.

Section names match the pointers in the SKILL.md workflow. Terminology follows the Terminology section of `SKILL.md`.

**Posture throughout: presence and consistency, not reprojection.** For every regime below, the job is to confirm the workpaper exists, spot-check its inputs and conclusion against the return, and flag mismatches. Do not rebuild §382, CAMT, PHC, the accumulated earnings tax, the foreign tax credit, or transfer pricing from scratch — a partial recomputation produces a confident wrong number, and the preparer owns the computation.

---

## Prior-year orientation and carryover sweep

**Goal: confirm every beginning balance and carryforward on this return comes from the prior year as adjusted, and that nothing was dropped.**

Checks:

1. **Correspondence and adjustments** — Request IRS and state correspondence, exam adjustments, and amended returns filed since the prior return. Tie Schedule L, M-2, and every carryover to the prior year **as adjusted**. A tie-out to as-filed figures inherits stale numbers and gives false comfort.
2. **Carryover completeness** — Trace each of the following from the prior return into this one. A dropped carryover is a straight income or deduction misstatement that the trial balance cannot surface:
   - Charitable contribution carryforward — five-year life; confirm nothing expired unused and that oldest-first ordering was applied
   - Capital loss carryforward — corporate capital losses offset **only capital gains** (three-year carryback, five-year carryforward); a capital loss against ordinary income is a hard stop
   - §1231(c) five-year lookback — prior §1231 losses recharacterize current §1231 gain as **ordinary** up to the unrecaptured amount. Returns prepared without prior-year data often miss this
   - §481(a) adjustment spread from a prior method change — confirm the correct year's installment is on the return
   - Installment sale gross profit (Form 6252) for payments received this year
   - §179 carryforward
   - §163(j) disallowed-interest carryforward — also tested in the §163(j) step
   - General business credit and other credit carryforwards, used oldest-first
3. **Blocking input** — Prior-year return plus the prior-year NOL, credit, and carryover schedules. Absent either, stop and record Missing Support at **[HIGH]**; the sweep is unverifiable without them.

---

## Schedule M-1 / M-3 mechanics

**Goal: confirm the required reconciliation schedule was used, and that the reconciliation is complete in both directions.**

Checks:

1. **Which schedule is required** — Total assets at year end of $10 million or more requires **Schedule M-3** (with Form 8916-A where applicable) in place of M-1. A review that reconciles M-1 on a $10M+ client is reviewing the wrong schedule *and* missing a required-form failure. Confirm the page 1 / Schedule K indicators and the schedule actually attached agree.
2. **Uncertain tax positions** — If audited financial statements report uncertain tax positions (ASC 740 UTBs) and the asset threshold is met, confirm **Schedule UTP** was considered.
3. **Both endpoints tie** — Book income on M-1 line 1 (or M-3 Part I) to the financial statements or trial balance, and taxable income before NOL and special deductions to Form 1120 line 28.
4. **Expected-addback sweep** — The common M-1 failure is not an unexplained item; it is a **missing** addback, which looks clean because nothing is there to question. For each item below, confirm a permanent addback appears wherever the underlying expense exists in the trial balance:
   - 50% of business meals; 100% of entertainment
   - Club dues
   - Lobbying and political expenditures, including the lobbying portion of association dues — check the association's annual disclosure
   - Fines and penalties (§162(f))
   - Officer and key-person life insurance premiums where the corporation is the beneficiary
   - Employee parking and other qualified transportation fringes disallowed under §274(a)(4)
   - Business gifts over $25 per recipient
   - Settlement payments subject to a nondisclosure agreement in sexual-harassment matters (§162(q))
5. **Flag the clean-looking gap** — A trial-balance account for meals, dues, penalties, lobbying, or officer life insurance with no corresponding M-1/M-3 adjustment is a finding even though the reconciliation "ties."

---

## Deduction mechanics

**Goal: confirm significant deductions are supported, correctly limited, and timed to the right year.**

Checks:

1. **Charitable contributions** — Verify the 10% limitation computation (taxable income before the charitable deduction and before NOL and capital-loss carrybacks); spot-check rather than rebuilding the return. Confirm any carryforward created or used ties to the prior return. Confirm substantiation: Form 8283 for property gifts over $500, and a qualified appraisal with signed appraiser and donee sections over $5,000 — a substantiation failure voids the deduction entirely. For an accrual-basis corporation deducting a year-end accrual, confirm board authorization before year end and payment within 3½ months after (§170(a)(2)).
2. **Related-party accruals (§267(a)(2))** — Amounts accrued to a cash-basis related party, including a >50% shareholder — interest, compensation, rent, bonuses — are not deductible until actually paid. Tie the accrual to a payment date, not just to the trial balance. Year-end accrued owner bonuses are the most common closely held C-corp adjustment.
3. **Officer compensation** — Confirm **Form 1125-E** is attached at total receipts of $500,000 or more, and that the officer compensation on it agrees with page 1 and the W-2s.
4. **Compensation cap (§162(m))** — If the corporation is publicly held (including certain foreign private issuer and debt-registrant cases), compensation over $1 million per covered employee is nondeductible regardless of reasonableness. Rare in a small-firm client base, but a one-line check when compensation is large.
5. **UNICAP and inventory** — Above the §448(c) threshold (aggregated under the controlled-group rules): the accrual method is required and §263A UNICAP applies to produced and acquired-for-resale inventory. Confirm the 263A addback exists or the small-business exemption is documented. Regardless of size: book lower-of-cost-or-market write-downs and inventory reserves are generally not deductible for tax — confirm they are added back. COGS is usually the largest number on the return, and an untouched book write-down flowing into tax COGS is material and invisible to the M-1 "tie."

---

## Dividends-received deduction mechanics

**Goal: verify a DRD workpaper exists, then spot-check the tier, holding period, and limitations against Schedule C. Flag mismatches; do not rebuild the schedule.**

Checks:

1. **Workpaper exists, payer by payer** — Ownership percentage, acquisition and disposition dates, dividend dates and amounts, and any debt financing. Without it, a Schedule C amount is unverifiable: record Missing Support at **[MEDIUM]**, or **[HIGH]** where the DRD is significant.
2. **Percentage tier** — 50% below 20% ownership; 65% at 20–79%; 100% at 80% or more (affiliated group). Confirm the percentage claimed matches documented ownership for each payer (§243).
3. **Holding period** — 45 days within the 91-day window around the ex-dividend date (§246(c)), extended for certain preferred dividends. Stock bought and sold around a dividend fails even where ownership documentation exists.
4. **Debt-financed portfolio stock** — The DRD is reduced under §246A to the extent the stock is debt-financed. Confirm the reduction where portfolio stock was acquired with borrowed funds.
5. **Taxable-income limitation** — The aggregate DRD is limited to the applicable percentage of taxable income, unless the full DRD creates or increases an NOL (§246(b)). Spot-check the limitation computation and confirm the exception was applied correctly rather than trusting a software flag.
6. **Foreign-source dividends are a different regime** — Dividends from specified 10%-owned foreign corporations run through the §245A participation exemption, not §243, with their own holding-period and hybrid-dividend rules. Confirm the correct Schedule C lines were used and that a §245A position has support; do not net the two regimes together.

---

## Entity-level taxes beyond the 21% rate

**Goal: confirm each regime was tested and that the corresponding form is present or a documented N/A. Confirm status; do not compute the tax.**

Checks:

1. **Form 2220 underpayment test** — Don't stop at "estimates were paid": test the payments against the required annual installments. The prior-year safe harbor is unavailable to large corporations, and annualization applies where income was uneven. An underpayment penalty the software never computed survives a payments-only check.
2. **Corporate AMT (CAMT)** — Where the corporation, together with its controlled group and any foreign parent group, could plausibly reach the three-year average adjusted financial statement income threshold, confirm applicable-corporation status was **tested** and that **Form 4626** is attached or the exemption is documented. A Schedule J recompute at 21% "ties" and still misses a 15% floor tax. Confirm the test was run; do not compute AFSI.
3. **Personal holding company (Schedule PH)** — Applies to closely held corporations (5 or fewer individuals own more than 50% by value) where passive income — dividends, interest, rents, royalties — is 60% or more of adjusted ordinary gross income. PHC status is mechanical and **self-assessed on the return**: a 20% tax on undistributed PHC income, reported on **Schedule PH**. Confirm the test was run and the schedule is present or N/A is documented. Treat a borderline AOGI classification as a "Preparer to analyze" row rather than concluding it.
4. **Accumulated earnings tax (§531)** — Distinct from PHC: AET is asserted on examination, not self-reported. Screen for growing retained earnings without a documented business purpose, and note the §535(c) accumulated earnings credit. Flag the exposure and the absence of a documented reasonable-needs analysis; do not compute the tax.

---

## NOL usage legality

**Goal: confirm the NOL deduction is supported, correctly reported, and legally usable. The amount tying to the prior year is necessary but not sufficient.**

Checks:

1. **Sort the carryforward into vintages first** — the rules differ by the year the loss arose, and mixing them is the root of most NOL errors:
   - **Pre-2018 NOLs** — 20-year carryforward, no 80% limitation; confirm nothing expired unused.
   - **2018–2020 NOLs** — indefinite carryforward and a five-year carryback under the CARES Act; the 80% limitation did **not** apply for tax years beginning before 2021 but **does** apply now.
   - **Post-2020 NOLs** — indefinite carryforward, no carryback, and the 80% limitation applies.
2. **80% limitation** — Post-2017 NOLs are deductible only up to 80% of taxable income computed before the NOL deduction. An NOL deduction equal to 100% of taxable income sourced from post-2017 losses is a **[HIGH]** finding.
3. **Ordering** — Pre-2018 losses are used first and must be tracked separately from later vintages. Confirm the schedule applies them in the correct order rather than netting one pool.
4. **Reporting on the return** — Confirm the available NOL carryover from prior years is reported on **Schedule K** (line 12 on recent forms — verify the line against the applicable year's instructions), stated **before** reduction by the current-year deduction, and that the line 29a deduction agrees with the attached NOL computation schedule.
5. **§382 ownership change** — Ask about equity raises, buyouts, redemptions, and transfers of stock by gift or at death. A shift of more than 50 percentage points among 5% shareholders over a three-year testing period triggers an annual limitation equal to the value of the loss corporation multiplied by the long-term tax-exempt rate. **If an ownership change is indicated, verify a §382 limitation schedule exists in the file; if it does not, hard-stop and route to the preparer.** Do not attempt to compute the limitation.
6. **Blocking inputs** — Prior-year NOL schedule by vintage; ownership and cap-table history.

---

## International information-return presence check

**Goal: confirm the required form is attached, or a documented N/A exists, for every trigger visible in the file. Presence, not substance.**

Penalties here are automatic, per-form, five figures, and they keep the statute of limitations open on the entire return. On many corporate returns the largest single exposure is a form that isn't there.

| Trigger visible in the file | Required form |
|---|---|
| 25%+ foreign shareholder, or foreign related-party transactions | 5472 (one per related party) |
| Officer, director, or 10%+ shareholder of a foreign corporation; a CFC | 5471 (+ 8992 for GILTI/NCTI where CFC income exists) |
| Interest in a foreign partnership | 8865 |
| Foreign disregarded entity or foreign branch | 8858 |
| Foreign mutual funds or pooled investments | 8621 (PFIC) |
| Property transferred to a foreign corporation | 926 |
| Foreign financial accounts | FinCEN 114 — hand to `fbar-workpaper` |
| FDII-eligible export income | 8993 (a deduction opportunity, not just compliance) |
| Gross receipts at or above $500M with base-eroding payments | 8991 (BEAT) |

Additional checks:

1. **Foreign tax credit** — If an FTC is claimed, confirm **Form 1118** is attached with its required schedules, that the creditable taxes tie to the foreign tax carryover schedule, and that the income is assigned to the correct §904(d) separate categories and sourced consistently with the Schedule C and Form 8992/8993 positions. Confirm presence and consistency; do not rebuild the limitation or the carryover.
2. **Cross-check Schedule K** — The foreign-ownership answer and the reported count of Forms 5472 must agree with the forms actually attached.
3. **Blocking input** — Foreign activity detail. If the source documents show foreign operations, ownership, or accounts and no detail was provided, record Missing Support at **[HIGH]**; an undocumented trigger *is* the exposure.
4. **Scope** — This check is presence and consistency only. Substantive review of a 5471, GILTI, FDII, or BEAT computation is a separate engagement; say so rather than partially working it.
