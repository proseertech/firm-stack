# 1120 Review — Detailed Verification Procedures

Read this file when the workflow in SKILL.md points here. Each section expands a workflow step; the step numbers below match the SKILL.md workflow.

## Step 1 — Prior-year orientation and carryover sweep

The prior-year return is a required input, but using it only to tie the NOL amount wastes it. Two procedures:

**Correspondence and adjustments.** Ask for IRS and state correspondence, exam adjustments, and amended returns since the prior filing. Beginning balances (Schedule L, M-2, every carryover) must tie to the prior year **as adjusted**, not as filed — if the prior return was later amended or adjusted on exam, every tie-out to the as-filed numbers inherits the stale figures and gives false comfort.

**Carryover completeness sweep.** Trace each of these from the prior return into the current one; a dropped carryover is a straight income or deduction misstatement:

- Charitable contribution carryforward (5-year life — confirm nothing expired unused, and oldest-first ordering)
- Capital loss carryforward — corporate capital losses offset **only capital gains** (3 back / 5 forward); a capital loss netted against ordinary income is a HIGH finding
- Section 1231(c) five-year lookback — prior 1231 losses recharacterize current 1231 gain as **ordinary** up to the unrecaptured amount; software misses this when prior-year data wasn't proforma'd
- Section 481(a) adjustment spread from a prior method change — confirm the correct year's installment is on the return
- Installment sale gross-profit recognition (Form 6252) for payments received this year
- Section 179 carryforward
- Section 163(j) disallowed-interest carryforward (also verified in step 14)

## Step 2 — Schedule M-1 / M-3 mechanics

**Which schedule.** If total assets at year-end are $10 million or more, Schedule M-3 (with Form 8916-A where applicable) is required in place of M-1 — a review that reconciles M-1 on a $10M+ client is reviewing the wrong schedule and missing a required-form failure. If audited financial statements report uncertain tax positions (ASC 740 UTBs), confirm Schedule UTP was considered.

**Expected-addback checklist.** The common M-1 failure is not an unexplained item — it's a **missing** addback, which looks clean because nothing is there to question. Confirm each of these appears as a permanent addback wherever the underlying expense exists in the trial balance:

- 50% of meals; 100% of entertainment
- Club dues
- Lobbying and political expenditures (including the lobbying portion of association dues — check the association's disclosure)
- Fines and penalties (Sec. 162(f))
- Officer/key-person life insurance premiums where the corporation is beneficiary
- Employee parking and other qualified transportation fringes disallowed under Sec. 274(a)(4)
- Business gifts over $25 per recipient
- Settlement payments subject to a nondisclosure agreement in sexual-harassment matters (Sec. 162(q))

A trial-balance account (meals, dues, penalties, insurance) with no corresponding M-1/M-3 adjustment is a finding even though the reconciliation "ties."

## Step 4 — Deduction mechanics

**Charitable contributions.** Beyond tying the amount: (a) the deduction is capped at 10% of taxable income computed before the deduction (and before NOL/capital-loss carrybacks) — recompute the cap; (b) any carryforward created or used ties to the prior return; (c) property gifts over $500 need Form 8283, over $5,000 a qualified appraisal with the signed appraiser/donee sections — substantiation failure voids the deduction entirely; (d) an accrual-basis corporation deducting a year-end accrual needs board authorization before year-end and payment within 3.5 months after (Sec. 170(a)(2)).

**Related-party accruals (Sec. 267(a)(2)).** Amounts accrued to a cash-basis related party (including a >50% shareholder) — interest, compensation, rent, bonuses — are not deductible until actually paid. Year-end accrued owner bonuses are the most common closely-held C-corp adjustment; tie the accrual to a payment date, not just to the trial balance.

**Compensation cap (Sec. 162(m)).** If the corporation is an applicable corporation (publicly held, including certain foreign-private-issuer and debt-registrant cases), compensation over $1 million per covered employee is nondeductible regardless of reasonableness. Rare for a small-firm client base, but a one-line check when compensation is large.

**UNICAP and inventory.** If aggregate average gross receipts exceed the Sec. 448(c) threshold (inflation-adjusted; verify the applicable year's amount): accrual method is required, and Sec. 263A UNICAP applies to produced or acquired-for-resale inventory — confirm the 263A addback exists or the small-business exemption is documented. Whatever the size: book lower-of-cost-or-market write-downs and inventory reserves are generally not deductible for tax — confirm they are added back. COGS is usually the largest number on the return; an untouched book write-down flowing into tax COGS is material and invisible to the M-1 "tie."

## Step 5 — Dividends-received deduction mechanics

The existing red flag (large DRD without ownership documentation) catches the crude case. The mechanics to verify on Schedule C:

- **Percentage tier** — 50% DRD below 20% ownership; 65% at 20–79%; 100% at 80%+ (affiliated group). Confirm the percentage claimed matches documented ownership.
- **Holding period** — 45 days during the 91-day window around the ex-dividend date (Sec. 246(c)); stock bought and sold around a dividend fails even when ownership documentation exists.
- **Debt-financed portfolio stock** — the DRD is reduced under Sec. 246A where the stock is debt-financed.
- **Taxable-income limitation** — the aggregate DRD is limited to the applicable percentage of taxable income unless it creates or increases an NOL (Sec. 246(b)); recompute rather than trusting the software flag.

## Step 7 — Entity-level taxes beyond the 21% rate

- **Form 2220 underpayment test** — Don't stop at "estimates were paid": test the payments against the required annual installments (prior-year safe harbor unavailable to large corporations; annualization if income was uneven). An underpayment penalty the software didn't compute survives a payments-only check.
- **Corporate AMT (CAMT)** — If the corporation (with its controlled group and, where applicable, foreign parent group) could plausibly have three-year average adjusted financial statement income over $1 billion, confirm applicable-corporation status was tested and Form 4626 attached or the exemption documented. A Schedule J recompute at 21% "ties" and still misses a 15% floor tax.
- **Personal holding company (Schedule PH)** — For closely held corporations (5 or fewer individuals own >50% by value) where passive income (dividends, interest, rents, royalties) is 60%+ of adjusted ordinary gross income: PHC status is mechanical and self-assessed — 20% tax on undistributed PHC income, reported on Schedule PH. This is distinct from the accumulated earnings tax the skill already screens (AET is exam-asserted; PHC belongs on the return).

## Step 8 — NOL usage legality

The amount tying to the prior year is necessary but not sufficient — the **usage** can still be illegal:

- **80% limitation** — Post-2017 NOLs are deductible only up to 80% of taxable income (computed before the NOL). Pre-2018 NOLs remain 100% usable and expire (20-year life) — the two vintages must be tracked separately and ordered correctly. An NOL deduction equal to 100% of taxable income sourced from post-2017 losses is a HIGH finding.
- **Section 382** — If an ownership change occurred (>50 percentage-point shift among 5% shareholders over 3 years — ask about equity raises, buyouts, and gifts/estates of stock), the annual usage is capped at the value of the loss corporation × the long-term tax-exempt rate. If a change happened and no 382 limitation appears, stop and route to the preparer.

## Step 11 — International information-return presence check

This is a presence check, not a substantive review: confirm the form is attached (or documented N/A) wherever the trigger exists. Penalties are automatic, per-form, five figures, and keep the statute open — the largest exposure on many returns is a form that isn't there.

| Trigger visible in the file | Required form |
|---|---|
| 25%+ foreign shareholder, or foreign related-party transactions | 5472 (one per related party) |
| Officer/director/10%+ shareholder of a foreign corporation; CFC | 5471 (+ 8992 GILTI/NCTI where CFC income exists) |
| Interest in a foreign partnership | 8865 |
| Foreign disregarded entity or foreign branch | 8858 |
| Foreign mutual funds / pooled investments | 8621 (PFIC) |
| Property transferred to a foreign corporation | 926 |
| Foreign financial accounts | FinCEN 114 — hand to `fbar-workpaper` |
| FDII-eligible export income | 8993 (deduction opportunity, not just compliance) |
| Gross receipts ≥ $500M with base-eroding payments | 8991 (BEAT) |

Foreign tax credit claimed → Form 1118 attached and sourced.

## Step 15 — Initial-return branch

Run this branch when the Initial Return box (Item E) is checked or the filing history shows year 1. First-year elections are where permanent damage happens — most are due with the first return and cannot be fixed later without relief:

1. **Entity classification** — If the entity is an LLC taxed as a corporation, confirm Form 8832 was filed and accepted (or is attached for the election year); confirm the effective date matches the return's start date.
2. **Tax year** — Confirm the year-end selected is permissible and matches any stated business purpose; short-period return mechanics (proration, annualization for estimates) applied correctly.
3. **Accounting method** — The method box (cash/accrual) is consistent with Sec. 448 (C corporations above the gross-receipts threshold, and certain entities regardless of size, cannot use cash). First-year method selection IS the election — no Form 3115 needed now, but the wrong box sets a method that later requires one.
4. **Election statements attached** — Sweep for the statements that must ride with the first return: Sec. 195/248 startup and organizational cost amortization (deemed elected if costs are deducted/amortized, but confirm the amounts and 15-year life), de minimis safe harbor under Reg. 1.263(a)-1(f), and any inventory/UNICAP method choices.
5. **Schedule L** — Beginning balance column should be zero/blank for a true first year; a populated beginning balance means a predecessor or a wrong Initial Return box — either way, a finding.
6. **Estimated-tax setup** — First-year corporations have no prior-year safe harbor; confirm current-year estimates were computed and the client has an EFTPS enrollment.
7. **Depreciation conventions** — First-year placed-in-service dates drive convention (mid-quarter test if >40% of additions in Q4) — check it; year 1 is when the register's conventions get set.
