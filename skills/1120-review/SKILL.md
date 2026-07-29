---
name: 1120-review
version: 1.13.0
description: |
  Cross-reference a completed Form 1120 (C-corporation income tax return) against its
  source documents — trial balance, supporting schedules, Form 4562, Form 3800, and the
  prior-year return — to catch errors before filing. Verifies income, deductions, credits,
  and the Schedule J tax computation tie out; reconciles Schedule M-1/M-3 book-to-tax and
  Schedule L / M-2; walks Schedule K; tests NOL usage (80% cap by vintage, §382), DRD
  mechanics, and entity-level taxes beyond the 21% rate (CAMT, PHC, AET); sweeps for
  required international forms; checks §163(j), depreciation and R&E; includes a
  first-year branch; grades findings by severity; and flags audit-risk items. Use this
  whenever a C-corp return needs a second set of eyes before it goes out the door —
  "review the 1120", "tie out the C-corp return", "does the 1120 match the trial balance",
  "check the corporate return before we file" — even if they don't name the form or say the
  word "review".
trigger: |
  "review the 1120", "1120 review", "C-corp return review", "check the C-corp return",
  "1120 cross-reference", "tie out the C-corp return", "verify the 1120",
  "does the 1120 tie out", "check the 1120 before filing", "review the corporate return",
  "cross-reference the 1120 to the trial balance", "the C-corp return doesn't tie",
  "first year corporate return", "initial return review"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1120 Review: C-Corporation Return Cross-Reference

## Purpose

Catch errors in a Form 1120 before it is filed. Verify that income, deductions, credits, and the tax computation tie to the trial balance and source documents, and surface anything that would draw IRS scrutiny.

Two failure modes matter equally here: numbers that don't tie, and numbers that tie perfectly to the books but are **legally wrong** — a capital loss netted against ordinary income, an NOL used past the 80% cap, a missing addback that makes the M-1 look clean. A tie-out alone catches only the first kind.

The deliverable is a severity-graded findings report a preparer can act on line by line. This is a review, not a sign-off: findings go to the responsible preparer, who decides what to correct and owns the filed return.

## Review Posture: Verify and Flag, Don't Re-Prepare

The job is to test **presence, classification, consistency, and tie-out** — books to return, prior year to beginning balances, workpapers to forms, triggers to required forms — and then flag what doesn't hold.

- **Do not rebuild a complex regime from scratch.** CAMT, BEAT, §382, transfer pricing, the detailed foreign tax credit, §163(j) ATI, PHC and accumulated earnings tax computations, and R&E timing are the preparer's work. Confirm the analysis exists, that its inputs match the return, and that its conclusion carries through consistently. An independent recomputation on partial data produces confident wrong answers.
- **Do not adjust numbers.** Report the discrepancy and the recommended direction ("update return to match trial balance"); the correction is the preparer's.
- **Uncertainty is a finding, not a silent pass.** Where the data or the law is unclear, write a **[MEDIUM]** or **[HIGH]** "Preparer to analyze" row stating exactly what is unresolved and what document would resolve it.
- **Missing input stops that step.** If the support a step depends on is absent, do not review around the gap — record a Missing Support item and a findings row, then move on. Each step below names its blocking inputs.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). **Beyond that, every discrepancy is a finding** — and every one becomes a row in the findings table.

Do not apply a percentage-based materiality threshold — a percentage of gross receipts, total assets, or net income belongs in a financial-statement audit, not a tax review. A $2,000 error that changes the tax due is a real finding regardless of how small it is against total assets.

Classify each finding by severity (impact + risk), not by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance — including items you are uncertain about or consider low-severity. Severity ranks the list; it does not filter it. Filtering happens at preparer review; your job here is complete coverage, because an error dropped now surfaces only after filing.

## Terminology

Use these terms consistently across the review and both reference files.

- **"As adjusted"** — the prior-year figures after amended returns and exam adjustments. Every beginning balance ties to the prior year *as adjusted*, never as originally filed.
- **NOL vintage** — three buckets, tracked and ordered separately: **pre-2018** (20-year life, no 80% cap), **2018–2020** (indefinite life, five-year CARES carryback, 80% cap applies for tax years beginning after 2020), and **post-2020** (indefinite life, no carryback, 80% cap). Netting them into one pool is the root of most NOL errors.
- **Controlled group** — the §1563 / §52(a)-(b) group. It drives §448(c) gross-receipts aggregation, §163(j), the §179 dollar limit shared among component members, CAMT AFSI aggregation, and the §1561 accumulated earnings credit. A standalone test on a group member is the wrong test.
- **Applicable corporation** — the CAMT status determination (three-year average adjusted financial statement income, or AFSI, above the statutory threshold), reported on Form 4626.
- **AOGI** — adjusted ordinary gross income, the denominator in the 60% personal holding company test.
- **ATI** — adjusted taxable income, the §163(j) base.
- **Total receipts** — the Form 1125-E threshold measure; use the definition in the applicable year's instructions, not book revenue.

**Form locations**
- **Schedule K (Other Information)** — accounting method, ownership and affiliation questions, foreign ownership, dividend distributions in excess of E&P, tax-exempt interest, and the §163(j) small-business questions. It is the return's own trigger list for downstream forms; walking it is step 6.
- **Schedule M-3 replaces M-1** at $10 million or more of total assets, with Form 8916-A where applicable.
- **Form 1120 has no Schedule K-1.** Where the corporation *receives* a K-1 from a pass-through, box and code assignments on that K-1 are renumbered between form years — verify any code against the applicable year's Form 1065 or 1120-S K-1 instructions before reporting it as wrong.

## Required Inputs

Confirm these are present before starting. A review run against a missing schedule or the wrong year's trial balance produces false comfort — the gaps look "clean" only because nothing was there to check.

- Completed Form 1120 and all schedules (C, D, E, G, J, K, L, M-1, M-2, M-3 if applicable)
- Trial balance or financial statements for the tax year
- Prior-year return **and** the prior-year NOL, credit, and carryover schedules
- IRS/state correspondence and any amended returns or exam adjustments since the prior filing
- Fixed-asset register with acquisition **and** placed-in-service dates (for the Form 4562 tie-out)
- DRD workpaper: payer-by-payer ownership percentages, holding periods, and debt-financing detail
- K-1s received from any pass-through the corporation owns
- Ownership/stock ledger and cap-table history (for §382 and Schedule K ownership questions)
- Foreign activity detail: subsidiaries, branches, accounts, related-party transactions, ownership above 25%
- §163(j) workpaper and prior-year Form 8990, if applicable
- Form 8832 acceptance (LLCs electing corporate status) and, for a consolidated group, Form 851 and any Forms 1122
- Any supporting workpapers
- CCH Axcess Diagnostics report and Input Override Report (if available)

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Detailed procedures live in **`references/corporate-verification-procedures.md`**; the first-year checks in **`references/initial-return-checklist.md`**. Read each when you reach the step that points to it.

Sections B and C are **conditional** — run a step only when its trigger facts are present, and state in the deliverable which conditional steps you skipped and why. A skipped step with no note reads as a cleared step.

---

### Section A — Core review (all years)

**1. Orient on the prior year, correspondence, and carryovers.**
*Goal: establish that every beginning balance and carryforward on this return comes from the prior year as adjusted.*
- Tie Schedule L beginning balances, M-2 beginning retained earnings, and every carryforward to the prior-year return **as adjusted** for amended returns and exam adjustments — not as originally filed.
- Run the carryover completeness sweep: charitable 5-year carryforward, capital loss carryforward, §1231(c) five-year lookback, §481(a) adjustment spread, installment gross profit (Form 6252), §179 carryforward, §163(j) disallowed interest, and credit carryforwards. A dropped carryover is a straight misstatement the trial balance cannot surface.
- Procedures in `references/corporate-verification-procedures.md` → *Prior-year orientation and carryover sweep*.
- **Blocking inputs:** prior-year return; prior-year NOL/credit/carryover schedules. Absent either, stop this step and record Missing Support at **[HIGH]** — the carryover sweep is unverifiable without them.

**2. Verify gross income.**
*Goal: prove every income line comes from the books, in the right character.*
- Tie gross receipts, returns and allowances, and each other-income line to the trial balance.
- Verify cost of goods sold on **Form 1125-A**, and confirm book lower-of-cost-or-market write-downs and inventory reserves were added back — COGS is usually the largest number on the return and an untouched book write-down is invisible to an M-1 that "ties."
- Verify Schedule D and Form 4797: capital gains netted correctly, and **corporate capital losses offset only capital gains** (three-year carryback, five-year carryforward). Apply the §1231(c) lookback, which recharacterizes current §1231 gain as ordinary up to unrecaptured prior §1231 losses.
- Confirm the **digital-asset question on Schedule K** is answered and consistent with the source documents; reconcile any Forms 1099-DA, where broker basis reporting is new and may be missing or wrong.
- Confirm income from pass-through K-1s is picked up by character — it does not sit in the trial balance the way a reviewer expects and is easy to drop entirely.

**3. Verify deductions.**
*Goal: confirm each significant deduction is supported, correctly limited, and timed.*
- Spot-check compensation, rent, interest, taxes, and depreciation against payroll registers, leases, loan documents, and Form 4562.
- Confirm **Form 1125-E** is attached where total receipts are $500,000 or more, and that officer compensation on it agrees with page 1 and the W-2s.
- Work the mechanics in `references/corporate-verification-procedures.md` → *Deduction mechanics*: the charitable 10% limitation and substantiation, §267(a)(2) deferral of amounts accrued to cash-basis related parties (year-end owner bonuses are the classic catch), §162(m) for publicly held corporations, and UNICAP/§263A above the §448(c) threshold.
- **Blocking input:** fixed-asset register for the depreciation line — without it, do not clear depreciation here; it is tested in step 12.

**4. Reconcile book to tax on the required schedule.**
*Goal: confirm the right reconciliation schedule was used and that it is complete in both directions.*
- **Determine which schedule is required first.** Total assets of $10 million or more requires **Schedule M-3** (with Form 8916-A where applicable) in place of M-1. Reconciling M-1 on an M-3-required client is reviewing the wrong schedule *and* missing a required-form failure — see Control Points.
- Tie book income on M-1 line 1 / M-3 Part I to the financial statements or trial balance, and taxable income before NOL and special deductions to Form 1120 line 28.
- Work the **expected-addback checklist** in `references/corporate-verification-procedures.md` → *Schedule M-1 / M-3 mechanics*. The common failure is a **missing** addback — meals, entertainment, club dues, lobbying, fines, officer life insurance, qualified transportation fringes, gifts over $25 — which looks clean precisely because nothing is there to question.
- If audited financial statements report uncertain tax positions, confirm **Schedule UTP** was considered.

**5. Verify Schedule L and Schedule M-2.**
*Goal: confirm the balance sheet ties and retained earnings rolls.*
- Tie beginning balances to the prior year as adjusted (step 1) and ending balances to the trial balance; flag every unexplained movement.
- Confirm loans to and from shareholders and related parties on Schedule L agree with the notes supporting the §267(a)(2) analysis in step 3.
- Roll M-2: beginning retained earnings + current-year book income − distributions ± other adjustments = ending. If distributions exceed E&P, **Form 5452** is required to support nondividend treatment.

**6. Walk Schedule K (Other Information).**
*Goal: use the return's own questionnaire as the trigger list for downstream forms.*
- Confirm the accounting-method box is consistent with §448 and with how the books are kept.
- Confirm the affiliation and ownership questions are answered: membership in an affiliated or parent-subsidiary controlled group, 20%/50% ownership of the corporation, and the corporation's own 20%/50% interests in other corporations and partnerships. These drive the controlled-group aggregations in Terminology and the international sweep in step 10.
- Confirm the foreign-ownership question (25% or more) agrees with the Forms 5472 count reported, and that the number of 5472s attached matches.
- Confirm the dividend-distributions-in-excess-of-E&P answer agrees with step 5 and Form 5452.
- Confirm the §163(j) small-business questions agree with the conclusion reached in step 13. An answer claiming the exception with a Form 8990 attached — or the reverse — is an internal contradiction on the face of the return.
- Line numbers on Schedule K move between form years; verify against the applicable year's instructions rather than a remembered line reference.

**7. Verify credits.**
*Goal: confirm each credit is on the right form, correctly limited, and supported.*
- Tie each credit to its source form and to **Form 3800**, and confirm the general business credit limitation and any carryforward or carryback ties to the prior-year schedule.
- Confirm credit carryforwards from step 1 are used oldest-first and none expired unused.
- **Blocking input:** the credit workpaper or study for any substantive credit (R&D, energy). Absent it, record Missing Support rather than accepting the amount.

**8. Verify the Schedule J tax computation and payments.**
*Goal: confirm the tax, the payments, and the penalty exposure.*
- Recompute the regular tax at the 21% flat rate on taxable income per line 30, and confirm base erosion, recapture, and other Schedule J Part I items.
- Tie estimated payments, prior-year overpayment applied, and any credits for federal tax paid to the payment records, then test for an underpayment penalty on **Form 2220** — the prior-year safe harbor is unavailable to large corporations, and annualization matters where income was uneven. A payments-only check misses a penalty the software never computed.
- Screen the entity-level taxes beyond the 21% rate per `references/corporate-verification-procedures.md` → *Entity-level taxes beyond the 21% rate*: CAMT applicability and Form 4626, personal holding company status and Schedule PH, and accumulated earnings tax exposure. **Screen and flag; do not compute these regimes.**

---

### Section B — Initial-return branch (year 1 only)

**9. Run the initial-return checks.** *(Conditional — the Initial Return box (Item E) is checked, the filing history shows year 1, or this is a new client whose prior returns the firm did not prepare.)*
*Goal: confirm the positions that get copied forward for the life of the entity were set deliberately.*
- Work `references/initial-return-checklist.md`: entity classification and Form 8832 acceptance, permissible tax year, accounting-method selection consistent with §448, start-up / organizational / stock-issuance cost classification, the statement-required elections, zero opening Schedule L balances, estimated-tax setup with no prior-year safe harbor, and first-year depreciation conventions.
- Most first-year positions cannot be fixed after the first return without a method change or relief.
- **Hard stop:** a missing Form 8832 acceptance where corporate classification depends on it, or a missing statement-required first-year election. See Control Points. Note that **§195 and §248 do not require election statements** — do not report a missing statement for either.

---

### Section C — Special regimes and high-risk areas

**10. International information-return presence check.** *(Conditional — any foreign trigger visible in the file.)*
*Goal: confirm the required form is attached or documented N/A for every trigger. Presence, not substance.*
- Work the trigger table in `references/corporate-verification-procedures.md` → *International information-return presence check*: Forms 5471, 5472, 8865, 8858, 8621, 926, 8991/8992/8993, and Form 1118 where a foreign tax credit is claimed.
- These penalties are automatic, per-form, five figures, and they keep the statute of limitations open on the entire return. The largest exposure on many corporate returns is a form that isn't there.
- Foreign financial accounts go to `fbar-workpaper`; do not build the FinCEN 114 workpaper here.
- **Blocking input:** foreign activity detail. If the source documents show foreign operations, ownership, or accounts and no detail was provided, record Missing Support at **[HIGH]** — an undocumented trigger is the exposure.

**11. Verify NOL usage, not just the amount.** *(Conditional — an NOL deduction is claimed on line 29a.)*
*Goal: confirm the deduction is both supported and legal.*
- Tie the carryforward to the prior-year NOL schedule as adjusted, sorted into the three **vintages** (pre-2018 / 2018–2020 / post-2020 — see Terminology). Confirm the ordering applies pre-2018 losses first rather than netting one pool.
- Confirm post-2017 NOLs are limited to 80% of taxable income computed before the NOL deduction, and that pre-2018 NOLs are tracked separately with their 20-year expiry.
- Confirm the reporting: the available prior-year NOL carryover on **Schedule K** (line 12 on recent forms — verify against the applicable year's instructions), stated **before** reduction by the current-year deduction, and a line 29a deduction that agrees with the attached NOL computation schedule.
- Screen the ownership history for a **§382** ownership change — an equity raise, buyout, redemption, or a transfer of stock by gift or at death. If a change is indicated, verify a §382 limitation schedule exists; do not compute the limitation. Procedures in `references/corporate-verification-procedures.md` → *NOL usage legality*.
- **Hard stop:** an ownership change with no §382 analysis in the file. See Control Points.
- **Blocking inputs:** prior-year NOL schedule; ownership/cap-table history.

**12. Verify the dividends-received deduction (Schedule C).** *(Conditional — dividend income is reported.)*
*Goal: verify a DRD workpaper exists, then spot-check the tier, holding period, and limitations against Schedule C. Flag mismatches rather than rebuilding the schedule.*
- Confirm the percentage tier matches documented ownership for each payer.
- Confirm the 45-day holding period within the 91-day window around each ex-dividend date; stock bought and sold around a dividend fails even where ownership documentation exists.
- Confirm any debt-financed portfolio stock reduction (§246A) and the taxable-income limitation, and that the limitation exception where the DRD creates or increases an NOL was applied correctly.
- Confirm foreign-source dividends were **not** run through §243. Dividends from specified 10%-owned foreign corporations belong in the §245A participation-exemption regime, with its own holding-period and hybrid-dividend rules and its own Schedule C lines. Do not net the two regimes.
- Mechanics in `references/corporate-verification-procedures.md` → *Dividends-received deduction mechanics*.
- **Blocking input:** the DRD workpaper with payer-level ownership, holding periods, and debt financing. Without it, a Schedule C amount is unverifiable — record Missing Support at **[MEDIUM]**, or **[HIGH]** if the DRD is significant.

**13. Verify depreciation, §179, and R&E treatment.**
*Goal: confirm the fixed-asset and R&E positions match the register and the supporting elections. A documentation and consistency check, not a recomputation.*
- Tie **Form 4562** to the fixed-asset register and trial-balance additions; confirm class lives, conventions, and placed-in-service dates, and check listed-property and passenger-auto limits.
- **Bonus depreciation** — 40% for property **acquired** before January 20, 2025; 100% for property acquired and placed in service on or after that date (OBBBA). The controlling date is acquisition, including the written-binding-contract date. Confirm the register's rate matches each asset's acquisition date and flag obvious mismatches; a single rate applied across a straddle year is a finding. Verify against the register — do not recompute the depreciation.
- **§179** — check the claimed amount against the applicable year's dollar limit and phase-out **using the workpaper**, flagging obvious excess. Remember the dollar limit is shared among controlled-group component members.
- **§174/§174A** — confirm current-year R&E treatment (domestic currently deductible for tax years beginning after 2024; foreign capitalized and amortized over 15 years) is consistent with the workpapers and any §174A capitalization election. If a **catch-up deduction of previously capitalized domestic R&E** appears, look for a Rev. Proc. 2025-28 transition election or Form 3115 and flag its absence — **do not recompute the amortization**. An M-1 that "ties" can still reflect an unauthorized method change; this is the largest book-tax law change on 2025 corporate returns. If a §41 credit is claimed, confirm the §280C-style reduction or election is consistent.
- **Blocking input:** fixed-asset register with acquisition dates.

**14. Verify the Section 163(j) interest limitation.**
*Goal: determine whether Form 8990 should be present, then confirm presence and high-level consistency. Do not rebuild ATI or the limitation.*
- Determine applicability: average annual gross receipts for the three prior years above the §448(c) threshold (verify the applicable year's amount, and aggregate under §448(c)(2) with the §52(a)/(b) and §414(m)/(o) rules), or tax-shelter status under §448(d)(3). A corporation under the threshold standalone can still fail on a controlled-group basis.
- If the limitation applies, confirm **Form 8990** is attached, that its inputs tie to the return, and that disallowed-interest carryforwards tie to the prior-year schedule.
- For tax years beginning after 2024, depreciation, amortization, and depletion are **added back to ATI again** (OBBBA). A workpaper carried forward on the 2024 EBIT base understates the allowable deduction — that costs the client money and is still a finding.
- Confirm consistency with the Schedule K §163(j) answers from step 6.
- If a §163(j)(7)(B) electing real property trade or business election is in effect, it is **irrevocable** and requires ADS for nonresidential real property, residential rental property, and QIP. Confirm step 13's register actually reflects ADS.
- Interest fully deducted + gross receipts above the threshold (or tax-shelter status) + no Form 8990 is at least **[MEDIUM]**, and **[HIGH]** where the disallowance would be material.
- **Blocking inputs:** §163(j) workpaper; prior-year Form 8990 for carryforwards.

**15. Coordinate incoming K-1s — and confirm no §199A deduction appears.**
*Goal: a C corporation claims no QBI deduction; the check is that none appears and that the K-1 data the corporation actually needs was captured.*
- **A C corporation is not eligible for §199A** — the deduction is available only to individuals, estates, and trusts. **Any QBI or §199A deduction anywhere on Form 1120 is a [HIGH] finding.** This is a real risk when a preparer or a software template carries over from 1120-S work.
- QBI, W-2 wage, UBIA, and SSTB figures on a K-1 received by the corporation are **not usable on this return**. Retain them in the workpapers for the issuing entity's records and for any ultimate owner-level analysis, but do not carry them onto the 1120. If a K-1 shows SSTB status and the workpapers treat the activity as non-SSTB, raise it as a **Preparer Question** — do not reclassify.
- Confirm the K-1 data that *does* matter to a C-corp partner was captured: ordinary and separately stated income by character, §163(j) items (excess business interest expense, excess taxable income, excess business interest income) feeding step 14, gross receipts for the §448(c) aggregation, foreign items feeding Form 1118 and step 10, and the corporation's basis in the interest.
- **Blocking input:** the K-1s themselves. A pass-through interest on Schedule L with no K-1 in the file is Missing Support at **[HIGH]**.

---

### Section D — Reporting

**16. Summarize findings.**
*Goal: produce the authoritative list.*
- Generate the 5-column findings table (see Output Format) as the complete record of issues, confirmed items, and optional improvements.
- Write the **Bottom line** in 2-3 sentences, stating the count of HIGH / MEDIUM / LOW items and naming any open hard-stop condition explicitly.
- State which conditional steps in Sections B and C were run and which were skipped, with the reason.

**17. Assess audit risk.**
*Goal: rank the exposure already documented — introduce nothing new.*
- Select **1-3 rows already in the findings table** that present elevated audit risk. Typical candidates: NOL and §382 issues, DRD inconsistencies, missing international forms, an absent Form 8990, PHC or accumulated earnings exposure, related-party pricing.
- Restate each as one bullet: "This item may draw scrutiny because [specific statutory or return-based reason]."
- Do not introduce a fact, amount, or issue that is not already a table row.

## Elections: Statement-Required vs. Deemed

Two different failure modes, so test them differently. **Do not report a missing statement for an election the regulations deem made by return treatment.**

### Deemed elections — made by how the return is filed; no statement required

- **§195 start-up expenditures** — Deduct up to $5,000, reduced dollar-for-dollar to the extent start-up expenditures exceed $50,000, and amortize the remainder over 180 months beginning with the month the **active trade or business begins**. Under Reg. §1.195-1(b) the corporation is **deemed to elect** this treatment for that year; no election statement is required.
- **§248 organizational expenditures** — Up to $5,000 (same $50,000 phase-down), remainder over 180 months beginning with the month the **corporation begins business**. Under Reg. §1.248-1(c) the corporation is **deemed to elect**; no statement is required.
- **What to test instead of a statement:**
  - **Classification** — §195 start-up vs. §248 organizational vs. **stock-issuance and capital-raising costs**. Costs of issuing or selling stock, underwriting and placement fees, and the legal and accounting fees attributable to the offering are capital costs that reduce paid-in capital: not deductible, not amortizable, no 180-month schedule. They are routinely swept into the §248 bucket.
  - **Mechanics on the return** — the $5,000 (as limited) and the 180-month amortization actually appear, each starting in its own correct month. A schedule keyed to the incorporation date rather than the business-start month, or defaulted to January, is a finding.
  - **Deliberateness** — capitalizing instead of deducting/amortizing forgoes the deemed election, is **irrevocable**, and applies to **all** costs in the category. If the return capitalizes, confirm it was a decision, not a data-entry default.

### Statement- or form-required elections — absence is a finding

- **Form 8832** entity classification — the acceptance letter is the evidence, not the intent
- **§179** expensing — Form 4562, Part I; limit, phase-out, and the controlled-group sharing rule
- **De minimis safe harbor**, Reg. §1.263(a)-1(f) — annual election statement
- **Bonus depreciation elect-out**, §168(k)(7) — statement by class; silence means bonus applies
- **§163(j)(7)(B) electing real property trade or business** — irrevocable, and requires ADS; must be consistent with the fixed-asset register
- **§174A** capitalize-and-amortize election, or a Rev. Proc. 2025-28 transition election / Form 3115 for an R&E method change
- **LIFO** — Form 970 with the return adopting it
- **§266** election to capitalize carrying charges; **Reg. §1.263(a)-3(n)** election to capitalize repairs — annual statements
- **§453(d)** installment-method elect-out — statement with a timely return
- **Form 1128** — change of annual accounting period; **Form 3115** — any other method change
- **Consolidated return** — Form 851 with the return, and Form 1122 consent for each new member's first consolidated year

## Filing Mechanics and Required Attachments

Cheap to check, expensive to miss.

- **Due date** — For a calendar-year C corporation, the 15th day of the **4th** month after year end (§6072(b)) — later than a 1065 or 1120-S, and a common diary error when a firm's corporate calendar is set from its pass-through calendar. Confirm the applicable year's rule for a June 30 fiscal year, which has its own timing. Automatic six-month extension on Form 7004.
- **E-file mandate** — verify the return is being e-filed where required; the aggregate-return threshold now captures most firms' corporate filings.
- **Form 1125-A** — required where there is inventory or cost of goods sold.
- **Form 1125-E** — required at total receipts of $500,000 or more.
- **Schedule M-3 (+ Form 8916-A)** — required at $10 million or more of total assets, in place of M-1.
- **Schedule UTP** — where assets meet the threshold and audited financials record an uncertain tax position.
- **Form 2220** — where an estimated-tax underpayment exists.
- **Form 4626** (CAMT), **Schedule PH** (personal holding company), **Form 8990** (§163(j)), **Form 5452** (nondividend distributions), **Form 3800** (general business credit), **Form 1118** (foreign tax credit) — each where its trigger is present.
- **International forms** — per step 10's trigger table.
- **Form 851 / Forms 1122** — for a consolidated group.

## Control Points

Stop for a preparer decision. On any hard stop, **halt the downstream steps**, record the finding, and do not produce "ready to file" messaging of any kind until it is resolved.

- **NOL usage** — An NOL deduction requires all three: the carryforward ties to the prior-year schedule as adjusted, the usage respects vintage and the 80% cap, and no ownership change occurred without a §382 analysis. **An ownership change with no §382 analysis is a hard stop**, not a finding to note.
- **Capital loss against ordinary income** — Corporate capital losses offset only capital gains. This is legally wrong regardless of how cleanly it ties to the books; hard stop.
- **Initial return with missing classification evidence or a required first-year election** — First-year positions ride with the first return and are largely irreversible. Do not treat an initial return as review-complete while the Form 8832 acceptance or a statement-required election is missing. **§195 and §248 statements are not required** — their absence is not a control point.
- **Required form absent** — Total assets of $10 million or more with no Schedule M-3, or any foreign trigger with no corresponding information return and no documented N/A. These are hard stops and HIGH findings, not minor suggestions: the international penalties are automatic and hold the statute open.
- **Any discrepancy beyond the $10 rounding tolerance** — Every variance becomes a table row with a recommended direction. Do not adjust the number yourself; the preparer owns the return. There is no size below which a variance is ignored.

## Red Flags

Each triggered red flag produces **exactly one findings-table row**, with all five columns populated: severity tag, current treatment as shown on the return, recommended treatment (a specific correction, or "Flag for preparer review" / "Preparer to analyze"), the reason the risk exists, and authority where one applies. **Do not attempt full recomputation** of PHC tax, accumulated earnings tax, CAMT, BEAT, §382, transfer pricing, or the detailed §163(j) limitation — confirm presence and consistency, and flag the exposure.

- Book income and taxable income reconciliation has unexplained permanent or timing differences
- A trial-balance account for meals, entertainment, dues, penalties, lobbying, or officer life insurance with **no** corresponding M-1/M-3 addback — the missing-addback failure looks clean
- Schedule M-1 filed where total assets are $10 million or more — Schedule M-3 is required
- Depreciation on the return significantly exceeds Form 4562, or Form 4562 doesn't tie to the fixed-asset register
- A capital loss netted against ordinary income
- NOL deduction equal to 100% of taxable income sourced from post-2017 losses; NOL vintages not tracked separately; or an equity raise, buyout, or stock transfer in the ownership history with no §382 analysis
- Large DRD without payer-level ownership documentation, at a percentage that doesn't match the ownership tier, on stock held briefly around the ex-dividend date, or with no taxable-income limitation computation
- Foreign-source dividends claimed under §243 rather than the §245A participation exemption, or the two regimes netted on one Schedule C line
- NOL carryover on Schedule K reported net of the current-year deduction, or a line 29a deduction that doesn't agree with the attached NOL schedule
- Year-end accrued bonuses, interest, or rent payable to a >50% cash-basis shareholder deducted before payment (§267(a)(2))
- Book LCM write-downs or inventory reserves flowing into tax COGS with no addback; UNICAP absent above the §448(c) threshold with no documented small-business exemption
- Form 1125-E absent with total receipts of $500,000 or more, or officer compensation on it disagreeing with page 1 or the W-2s
- Closely held corporation with predominantly passive income and no Schedule PH analysis
- Accumulated earnings appear to exceed reasonable business needs — §531 exposure
- Group AFSI plausibly at the CAMT threshold with no applicable-corporation determination and no Form 4626
- Prior-year credit carryforwards with no supporting schedule, or credits expiring unused
- Estimated payments confirmed but no Form 2220 test — an uncomputed underpayment penalty survives a payments-only check
- Schedule K ownership, affiliation, or foreign-ownership questions blank or inconsistent with the forms attached; §163(j) answers contradicting the Form 8990 posture
- Controlled-group membership indicated on Schedule K but §448(c), §179, §163(j), or CAMT tested on a standalone basis
- Distributions exceeding E&P with no Form 5452
- Related-party transactions present without supporting transfer pricing documentation
- Foreign accounts, foreign shareholders at 25% or more, or foreign subsidiaries and branches visible in source docs with no corresponding information returns — possible FinCEN 114 (FBAR), 5471, or 5472 exposure with per-form automatic penalties; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- Foreign tax credit claimed with no Form 1118
- 2025 fixed-asset additions straddling January 19 all claimed at a single bonus rate, or a catch-up R&E deduction with no Rev. Proc. 2025-28 election or Form 3115 in the file
- A §163(j)(7)(B) real property elect-out with MACRS rather than ADS lives in the register
- Interest expense deducted in full with no Form 8990 despite gross receipts above the §448(c) threshold on an aggregated basis, or a §163(j) computation still on the 2024 EBIT base
- **A §199A or QBI deduction appearing anywhere on Form 1120** — a C corporation is not eligible
- A pass-through interest on Schedule L with no K-1 in the file
- Consolidated group indicated with no Form 851, or a new member with no Form 1122
- Digital-asset question on Schedule K answered "No" but a 1099-DA or crypto activity appears in the source documents
- Initial Return box checked but Schedule L shows beginning balances, or a statement-required first-year election or the Form 8832 acceptance is missing

## Output Format

**The chat response and the .docx both use the same 5-column findings table.** This is the primary deliverable — a single table where every reviewed line item appears, with its current treatment, recommended treatment, reason, and authority.

### Findings Table (required format)

A markdown table in chat, a Word table in .docx. One row per item. **Exactly these 5 columns, in this order:**

| Line / Schedule | Current treatment | Recommended treatment | Reason | Authority |
|---|---|---|---|---|
| **[HIGH]** Line 29a / NOL schedule | NOL deduction $840,000 = 100% of taxable income | Limit to 80% of taxable income and provide the §382 analysis | Carryforward arose in 2021, so the 80% cap applies; the 2024 equity round appears to be a >50-point ownership shift with no §382 limitation in the file. | §172(a)(2); §382 |
| **[HIGH]** Sch M-1 | M-1 filed; total assets $14.2M | File Schedule M-3 with Form 8916-A | Schedule M-3 is required at $10 million or more of total assets; M-1 is the wrong schedule and its absence is a required-form failure. | Form 1120 instr., Sch M-3 |
| **[HIGH]** Line 30 area | §199A deduction $18,400 claimed | Remove; no QBI deduction is available | §199A is available only to individuals, estates, and trusts; a C corporation cannot claim it. | §199A(a) |
| **[MEDIUM]** Sch C, Line 2 | DRD $15,000 | $22,500 per ownership % | 45%-owned payer; the 65% tier applies to the $34,615 dividend. | §243(c) |
| **[MEDIUM]** Sch M-1, Line 5c | Travel $3,200 on books, $0 on return | Add back $3,200 | Travel per GL not reflected on the return; the M-1 reconciliation is incomplete. | §274; Form 1120 instr. |
| Sch J, Line 2 | Tax $2,100 | No change — confirmed correct | Tax computed at the 21% flat rate on line 30 taxable income; verified. | §11(b) |

Column rules:
- **Line / Schedule** — Specific form reference (e.g., "Sch C, Line 2", "Sch J, Line 2", "Sch M-1, Line 5c"). **Severity** is a bold tag at the start of this cell: **[HIGH]**, **[MEDIUM]**, **[LOW]**. Omit the tag for confirmed items.
- **Current treatment** — What the return currently shows. State "Blank" or "Not checked" when a field is omitted. Include the dollar amount inline if relevant.
- **Recommended treatment** — The specific correction, or "No change — confirmed correct" for items that tie. Use "Preparer to analyze" where the answer needs judgment or data you don't have. For optional improvements, prefix with "Optional:".
- **Reason** — The factual or legal basis for the recommendation. Explain *why*, not just *what*.
- **Authority** — IRC section, Reg., Revenue Ruling, form instructions, or source document. Use "—" if none applies.

Table rules:
- **Every reviewed item goes in the table** — issues, confirmed items, items confirmed not applicable, and optional recommendations alike. Do not omit correct items; they show the reviewer checked them.
- **Sort rows by form/schedule order** (page 1 income, then page 1 deductions; Schedules C, D, G, J, K; L, M-1 or M-3, M-2; then attached forms — 1125-A, 1125-E, 4562, 4797, 3800, 2220, 4626, PH, 8990, 5452, and the international forms; then state items), not by severity. Severity tags handle prioritization within the natural reading flow.
- **One row per line item.** Do not split a single issue across multiple rows, and do not merge two issues into one.

### Section Organization

Surround the table with these sections:

1. **Bottom line** — 2-3 sentences: overall status, the count of HIGH / MEDIUM / LOW findings, and any open hard-stop condition named explicitly
2. **Findings Table** — The 5-column table above
3. **Required-Form Status** — Present / documented N/A / open, for: Schedule M-3 and Form 8916-A, Schedule UTP, Form 1125-A, Form 1125-E, Form 2220, Form 4626, Schedule PH, Form 8990, Form 5452, Form 1118, and each international form triggered
4. **Missing Support** — Bulleted list of absent source documents and workpapers, naming the step each one blocked
5. **Preparer Questions** — Bulleted list of items requiring judgment, including every "Preparer to analyze" row
6. **Audit Risk Items** — 1-3 bullets restating the highest-risk rows already in the table, with no new facts

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary + the findings table; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1120", client/Corporation name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary with the HIGH/MEDIUM/LOW counts and any hard stop
3. **Findings table** — 5 columns: Line/Schedule, Current treatment, Recommended treatment, Reason, Authority. Use `Table Grid` style. Bold the header row. Severity tags (**[HIGH]**, etc.) are bold prefixes in column 1. This is the main body — a preparer should be able to work the return from this table alone.
4. **Required-form status** — Table: form, trigger, status (present / N/A documented / open)
5. **Missing support** — Bulleted list, with the step each item blocked
6. **Preparer questions** — Bulleted list of items requiring judgment
7. **Audit risk** — 1-3 bullet points, factual, drawn from the table
8. **Scope note** — Which conditional steps in Sections B and C were run and which were skipped, with the reason

Save as `[ClientName]_[TaxYear]_1120_Review.docx` (e.g., `ABCCorp_2025_1120_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity tags in column 1
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Handoffs

- **`fbar-workpaper`** — foreign accounts surfaced during the review; build the FinCEN 114 workpaper there, not here.
- **`costseg-analysis`** — a building placed in service or a major leasehold buildout.
- **`rd-analysis`** — substantive R&E activity with no study in the file.
- **`nexus-screen`** — multistate activity, remote employees, or inventory in other states surfaced during the review.
- **`tax-workpapers`** — incoming 1099s and pass-through K-1s that need summarizing before the tie-out.

## Safety Constraints

- Do not mark the return reviewed-complete while any hard-stop control point or any discrepancy beyond rounding is unresolved — a "clean" review with open variances misleads the preparer into filing.
- Do not adjust or correct figures yourself. Report the variance and the recommended direction; the correction is the preparer's.
- Do not recompute CAMT, BEAT, §382, transfer pricing, the detailed foreign tax credit, §163(j) ATI, PHC tax, accumulated earnings tax, or R&E timing from scratch. Verify the analysis exists, its inputs tie to the return, and its conclusion carries through consistently.
- Do not compute or propose a §199A deduction on Form 1120 under any circumstances. A C corporation is not eligible; if one appears, it is a HIGH finding.
- Do not report a K-1 box or code as wrong without confirming the assignment in the applicable year's Form 1065 or 1120-S K-1 instructions. Codes are renumbered between form years.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (apportionment, state modifications, nexus questions) to Preparer Questions rather than reviewing them here.
- State audit risk as facts, not as a probability or percentage. Judging what level of risk is acceptable is the signing partner's call, not the reviewer's.
- Do not invent authority. Cite an IRC §, regulation, or procedure only when you are confident it applies; otherwise describe the issue and leave the citation for the preparer to confirm.
- Do not hardcode inflation-adjusted amounts (the §448(c) threshold, §179 limits, the CAMT AFSI threshold's indexed components). Statutory fixed thresholds — the $10M Schedule M-3 line, the $1M §162(m) cap, the $500,000 Form 1125-E line, the §535(c) accumulated earnings credit — may be stated, but verify year-indexed figures against the applicable year.
