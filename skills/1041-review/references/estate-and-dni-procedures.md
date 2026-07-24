# Estate and DNI Procedures — Form 1041 Review

Detailed procedures for the workflow steps in SKILL.md that point here. Each section states the check, how to perform it against the source documents, and why a miss matters.

## Decedent estates

### Post-death income splitting

Income earned through the date of death belongs on the decedent's final Form 1040; income earned after death belongs on the estate's 1041 (or, for assets that passed directly, on the beneficiary's return). Brokers do not split 1099s at death — a single 1099 issued under the decedent's SSN routinely covers the whole year.

Procedure: get the date of death. For each 1099 issued under the decedent's SSN or the estate's EIN, allocate interest and dividends around the date of death (accrual for interest; record-date for dividends) and confirm the 1041 picks up only the post-death portion, with the pre-death portion accounted for on the final 1040. A "nominee" adjustment on either return is the usual mechanical fix — verify it nets to the full 1099 amount across the two returns. Income double-reported or dropped between the returns is a HIGH finding.

### Income in respect of a decedent (IRD)

IRD is income the decedent earned but had not received at death — final paychecks, accrued bonuses, retirement account distributions, installment-sale collections, accrued-but-unpaid interest. IRD goes on the return of whoever receives it (estate or beneficiary), keeps its character, and — critically — gets **no basis step-up**.

Procedure: scan the source documents for IRD categories. Confirm IRD items are reported by the recipient, not the final 1040, and that no step-up was applied to them.

### The IRC 691(c) deduction

If the estate paid federal estate tax and the 1041 (or a beneficiary) reports IRD, the recipient is entitled to an income tax deduction for the estate tax attributable to that IRD. This is one of the most commonly missed deductions on estate-period returns.

Procedure: if IRD is reported and a Form 706 was filed with tax due, confirm the 691(c) deduction was computed (estate tax with the IRD included minus estate tax with it excluded, apportioned to the IRD items) and allocated between the estate and beneficiaries in proportion to the IRD each reports. IRD with estate tax paid and no 691(c) deduction is a finding — the tax overstatement is often material.

### Fiscal year and the IRC 645 election

Estates may elect any fiscal year ending within 12 months of death; trusts must use a calendar year. A qualified revocable trust may join the estate's return — and its fiscal year — via the IRC 645 election on Form 8855.

Procedure: confirm the year-end on page 1 is permissible for the entity type. A trust on a fiscal year with no 645 election in the file is a finding. If a 645 election exists: Form 8855 was filed by the due date of the first combined return, the combined reporting covers only the election period (which ends based on whether a 706 was required), and the trust did not also file a separate 1041 for the same period.

## Initial-return branch

When the Initial Return box is checked, or the entity's first year is under review:

1. **Entity data** — EIN assigned to this entity (not the decedent's SSN or a related trust's EIN), legal name matches the instrument, fiduciary name and address current.
2. **Tax-year selection** — Estates: any permissible fiscal year; evaluate whether the year-end selected matches what the fiduciary intended (a short first year is common and fine). Trusts: calendar year only, absent a 645 election.
3. **Elections attached** — The first return is where one-time elections live: IRC 645 (Form 8855), fiscal year (by filing), accounting method, and any treatment elections the preparer intended. Confirm each intended election is actually attached or reflected — a missed first-year election usually cannot be fixed later.
4. **No inherited carryovers** — A first-year return should have no capital-loss, NOL, or excess-deduction carryforwards. A carryover on an initial return means either the box is wrong or an amount was pulled from the wrong taxpayer (e.g., the decedent's carryovers, which die with the decedent except as used on the final 1040).
5. **Funding tie-out** — Opening assets should trace to the estate inventory, trust funding schedule, or date-of-death valuations; this establishes the basis positions every later year relies on.

## Date-of-death basis step-up (1099-B review)

Assets includible in the decedent's estate take a basis equal to date-of-death fair market value (IRC 1014), and inherited property is **automatically long-term** regardless of holding period. Brokers frequently fail to re-baseline: the account transfers with the decedent's original cost basis intact.

Procedure: for estates, and for trusts that became irrevocable at death, compare 1099-B basis on sold positions against date-of-death values (statement values at death, or the 706/inventory). Basis equal to the decedent's original cost on a covered position is a finding — gain is overstated. Check the holding-period column: inherited positions coded short-term are misreported. Two caveats: (a) alternate valuation date, if elected on the 706, replaces date-of-death value; (b) IRC 1014(e) denies the step-up for appreciated property gifted to the decedent within one year of death and passing back to the donor — flag, don't conclude.

## Tax-exempt income: disclosure and expense allocation

If the entity holds municipal bonds or other exempt income sources:

1. Tax-exempt interest is disclosed under Other Information on page 2.
2. Direct expenses of exempt income are fully disallowed.
3. **Indirect expenses — fiduciary fees above all — must be allocated** between taxable and tax-exempt income (typically by relative income), the exempt portion disallowed, and the computation **attached to the return**. Fully deducted fiduciary fees on a muni-heavy portfolio is a recurring exam adjustment.
4. The exempt income (net of allocated expenses) enters the DNI computation — it is part of DNI even though not taxed, and it changes the character mix reported on the K-1s.

## Charitable deduction (IRC 642(c))

Unlike individuals, a trust or estate gets a charitable deduction only if **both** conditions hold: the payment is made **pursuant to the governing instrument** (the will or trust must authorize it), and it is paid **from gross income** (not principal). There are no percentage limits, but:

- The portion traceable to tax-exempt income is disallowed.
- Estates (and pre-1969 trusts) may deduct amounts permanently **set aside**; ordinary trusts may not — payment (or the 642(c)(1) prior-year election) is required.
- The 642(c)(1) election lets a payment made in the following year be deducted in the current year — confirm the election statement if used.
- **Form 1041-A** is required for trusts claiming a 642(c) deduction unless an exception applies (e.g., trusts required to distribute all income currently).

Procedure: read the instrument for the charitable authorization; trace the payment to a gross-income source in the fiduciary accounting; check the exempt-income disallowance; confirm 1041-A or the exception.

## K-1 loss limitations

A pass-through loss reaches the 1041 only after clearing, in order: (1) the trust's **basis** in the partnership interest or S-corp stock, (2) **at-risk** (IRC 465), and (3) **passive activity** (IRC 469). The passive gate turns on material participation, which for a trust is measured by the **trustee's** activity in the business — an unsettled, litigated area (the *Frank Aragona Trust* line). Procedure: for each K-1 loss, ask for the basis schedule and the passive/non-passive characterization; if losses are treated as non-passive on the strength of trustee involvement, flag it and hand the analysis to `tax-advisor`. A loss deducted with no basis schedule is a hard-stop finding, same as the other review skills.

## Separate share rule (IRC 663(c))

When a trust or estate has substantially separate and independent shares for different beneficiaries (e.g., "divide into equal shares for my three children, each administered separately"), DNI is computed **share by share**, as if each share were a separate entity. A distribution to one beneficiary carries out only that share's DNI.

Why it matters here: the skill's core control point — K-1 totals foot to the distribution deduction — still passes when separate shares are ignored, but individual K-1s are wrong: a beneficiary who received a disproportionate distribution gets too much or too little DNI. Procedure: read the instrument for separate-share language; if present, confirm the software computed per-share DNI (most default to single-share) and that each K-1's income matches its share's DNI, not a pro-rata slice of the total.

## Final-year mechanics

On the entity's final 1041 (termination box checked):

1. **Remaining DNI** — All income in the final year is treated as distributed; the distribution deduction should flush the entity's income to the beneficiaries.
2. **Carryovers pass out** — Unused capital-loss and NOL carryovers pass to the beneficiaries (K-1 Box 11, codes B/C–E) and survive on their returns; they do not evaporate.
3. **Excess deductions** — Final-year deductions in excess of income pass to beneficiaries (K-1 Box 11, code A), **with character retained**: IRC 67(e) fiduciary-only expenses (fiduciary fees, etc.) are adjustments to the beneficiary's AGI, while items like state taxes remain itemized deductions in the beneficiary's hands. Reporting the whole excess as one undifferentiated amount is a finding — it changes each beneficiary's 1040.
4. **Nothing stranded** — No income, credit, or carryover should remain at the entity after the final year.

## Electing small business trusts (ESBTs)

If Box A on page 1 identifies an ESBT: the S-corporation items are computed in a **separate S-portion calculation**, taxed at the entity level at the highest rate (with its own QBI interaction), and are **excluded from DNI** — no distribution deduction, no flow-through of S items on the K-1s. The non-S portion follows normal trust rules.

Procedure: confirm the S-corp K-1 items are segregated into the S-portion computation (usually an attached statement), the S-portion tax appears on Schedule G, and the DNI computation and beneficiary K-1s contain only non-S items. S-corp income mixed into DNI is a HIGH finding — every downstream number is wrong, even if the totals foot.
