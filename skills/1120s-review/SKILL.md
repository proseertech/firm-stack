---
name: 1120s-review
version: 1.13.0
description: |
  Cross-reference a completed Form 1120-S (S-corporation return) against its source
  documents — trial balance, Schedule K-1s, officer W-2s, Form 1125-E, and supporting
  schedules — to catch errors before filing. Verifies the S election is valid and
  undisturbed (shareholder eligibility, one-class-of-stock, non-pro-rata distributions),
  ties page 1 and Schedule K to the books, confirms K-1s foot to Schedule K and follow
  per-share-per-day allocation, tests stock and debt basis, reconciles AAA/OAA/M-2, and
  works the special regimes (former-C-corp BIG and E&P, §1375, §199A, §163(j), K-2/K-3,
  PTET). Includes a first-year branch (Form 2553 acceptance, cost elections, basis
  initiation). Use this whenever someone hands you a drafted or finished S-corp return and
  wants it checked, tied out, or reviewed against the books — "review the 1120-S", "does
  the S-corp return tie to the TB", "check the K-1 allocations", "second set of eyes on
  this S-corp before we file" — even if they don't name the form or say the word "review."
trigger: |
  "review the 1120-S", "review the 1120S", "S-corp return review", "check the S-corp",
  "1120-S cross-reference", "tie out the S-corp return", "verify the 1120S",
  "does the S-corp tie to the trial balance", "check the K-1 allocations",
  "reasonable comp check", "did we tie out the S-corp", "S-corp return before we file",
  "second look at the S-corp"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1120-S Review: S-Corporation Return Cross-Reference

## Purpose

Catch errors before a Form 1120-S is filed. Verify that income, deductions, and shareholder allocations on the return tie to the trial balance and source documents, and that each K-1 is mathematically consistent with the Schedule K totals. The deliverable is a severity-graded findings report a preparer can act on line by line.

This is a technical review for a professional preparer; it does not replace the signing partner's sign-off.

## Review Posture: Verify and Flag, Don't Re-Prepare

The job is to test **presence, classification, consistency, and tie-out** — books to return, Schedule K to K-1, workpapers to forms, prior year to beginning balances — and then flag what doesn't hold.

- **Do not rebuild a complex regime from scratch.** Built-in gains, the §199A deduction and its limitations, §163(j) ATI, R&E timing under §174/§174A, and multi-state PTET are the preparer's computations. Confirm the workpaper exists, that its inputs match the return, and that its conclusion is carried through consistently. An independent recomputation on partial data produces confident wrong answers.
- **Uncertainty is a finding, not a silent assumption.** Where the data or the law is unclear, write a **[MEDIUM]** or **[HIGH]** "Preparer to analyze" row stating exactly what is unresolved and what document would resolve it.
- **Missing input stops that step.** If the support a step depends on is absent, do not review around the gap — record a Missing Support item and a findings row, and move on. Each step below names its blocking inputs.

## Accuracy Standard

A tax return must be substantially correct, so the bar here is different from a financial-statement audit — there is no percentage materiality. Do not use a percentage of gross receipts, total assets, or net income to decide whether a variance is acceptable; that test belongs to audit engagements, not tax review.

The only tolerance is rounding: differences of $10 or less are expected (consistent with IRS whole-dollar rounding and normal software behavior). **Every discrepancy beyond that is a finding** — including one that looks trivial next to the entity's size.

Grade findings by severity — impact plus risk, not dollar size:

- **HIGH** — Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM** — Documentation gaps, defensible-but-thin positions, items that could draw IRS correspondence
- **LOW** — Minor rounding ($10–$100 range), presentation preferences, informational items

Report *every* discrepancy outside the rounding tolerance, including low-severity or uncertain ones. Severity ranks the list; it does not filter it. Filtering understates coverage, and the item you drop as "probably fine" is the one that surfaces after filing. A separate preparer review decides what to act on — your job here is complete coverage.

## Terminology

Use these terms consistently across the review and all three reference checklists.

**Concepts**
- **Stock basis / debt basis** — the two separate shareholder basis pools under §1367. **S-corporation basis does not include entity-level liabilities** — the single most common error carried over by preparers working from a 1065 mindset.
- **AAA** — accumulated adjustments account (§1368(e)(1)); **OAA** — other adjustments account (tax-exempt income and its related nondeductible expenses); **PTI** — pre-1983 previously taxed income; **AE&P** — accumulated earnings and profits from C-corporation years.
- **Per-share-per-day** — the §1377(a)(1) pro-rata allocation rule. **§1377(a)(2) closing of the books** is the elective alternative on a complete termination of a shareholder's interest.
- **NUBIG / recognition period** — net unrealized built-in gain and the five-year §1374 window.
- **Total receipts** — the Form 1125-E and Schedule B threshold measure; use the definition in the applicable year's instructions, not book revenue.

**Form locations**
- **Schedule B (Other Information)** — carries the digital-asset question and the total-receipts/total-assets test that governs whether Schedules L and M-1 are required. The digital-asset question is **not** on page 1 of Form 1120-S.
- **Schedule M-2** — the AAA, PTI/shareholders' undistributed taxable income, and OAA columns.
- **Form 7203** — the *shareholder's* stock and debt basis form, filed with their 1040. The corporation doesn't file it but must furnish the inputs.

**Box codes cited in this skill** — shorthand only. **K-1 box and code assignments are renumbered between form years; verify every code against the applicable year's Form 1120-S Schedule K-1 instructions before reporting a code as wrong.** Software defaults lag form changes, and a review finding that cites a stale code is itself a finding.
- **Box 17 code V** — §199A information, furnished as a supporting statement (QBI, W-2 wages, UBIA, SSTB status, REIT dividends). All §199A components live in that one statement; there is **no separate box code for W-2 wages or UBIA**.
- **Box 17 code AC** — gross receipts for §448(c), which shareholders need for their own small-business and §163(j) testing.
- **Box 17 code N** — business interest expense.

## Required Inputs

- Completed Form 1120-S and all schedules (B, K, K-1s, L, M-1, M-2 as required)
- Trial balance or financial statements for the tax year
- Officer W-2s, payroll registers, and Form 1125-E
- Distribution detail by shareholder and date, plus the shareholder/stock ledger
- Shareholder stock and debt basis worksheets, and any shareholder notes (if losses or distributions flow through)
- K-1s received from any partnership or LLC in which the corporation is a partner
- Form 2553 and the IRS acceptance letter (CP 261) — first-year returns and new clients
- Prior-year return (for AAA/OAA, AE&P, basis, and carryforwards)
- Fixed-asset schedule with acquisition **and** placed-in-service dates
- Built-in-gains workpaper and the conversion-date asset appraisal/NUBIG schedule, if the corporation was ever a C corporation
- §163(j) workpaper and prior-year Form 8990, if applicable
- PTET payment records and state credit schedules, if a PTET election was made
- Any supporting workpapers
- CCH Axcess Diagnostics report and Input Override Report (if available)

If a required input is missing, say so before starting rather than reviewing around the gap — a review that silently skips the basis worksheet or the prior-year return gives false assurance.

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Detail for the first-year checks lives in **`references/initial-return-checklist.md`**; basis, distributions, and the AAA/OAA ordering rules in **`references/basis-and-distributions.md`**; the former-C-corporation regimes in **`references/former-c-corp-regimes.md`**. Read each when you reach the step that points to it.

Sections B and C are **conditional** — run a step only when its trigger facts are present, and say in the deliverable which conditional steps you skipped and why. A skipped step with no note reads as a cleared step.

---

### Section A — Core review (all years)

**1. Confirm the S election and continuing eligibility.**
*Goal: establish that the entity is actually an S corporation for this year before reviewing anything computed on that assumption.*
- Sight Form 2553 and the IRS acceptance letter (CP 261); confirm the effective date covers this tax year. For a late election, confirm the Rev. Proc. 2013-30 relief statement is in the file.
- Count shareholders against the 100-shareholder limit, applying the §1361(c)(1) family aggregation rule.
- Screen every shareholder for eligibility: individuals who are US citizens or residents, estates, and only qualifying trusts (grantor, QSST, ESBT, voting, or testamentary within its two-year window) and qualifying exempt organizations. Nonresident aliens, partnerships, corporations, IRAs, and most other trusts are ineligible. A trust or exempt-org shareholder with no QSST/ESBT election evidence in the file is a finding.
- Screen for termination events under §1362(d): revocation, ceasing to qualify, or three consecutive years of excess passive investment income with AE&P (step 11).
- **Blocking input:** no Form 2553 or acceptance letter for a first-year return or new client → Missing Support finding; do not assume the election.
- **Hard stop:** an ineligible shareholder or a confirmed second class of stock means the entity classification is wrong and every downstream computation is moot. Route to the preparer before continuing.

**2. Test for a second class of stock.**
*Goal: detect a one-class-of-stock problem without manufacturing one.*
- Read the governing provisions — charter, articles, bylaws, shareholder agreements, and applicable state law. Under Reg. §1.1361-1(l) the one-class test turns on whether all outstanding shares confer **identical rights to distribution and liquidation proceeds**. Differences in *voting* rights are fine.
- Compare the distribution detail to ownership percentages. **Non-pro-rata distributions do not by themselves create a second class of stock** — they are evidence to run down, not a conclusion. The usual explanations are (a) a binding agreement that does confer different rights (a real problem), (b) payments mischaracterized as distributions when they are compensation, loans, expense reimbursements, or a redemption, or (c) timing differences within the year. Identify which, and flag it for the preparer with the documents you'd need.
- Check shareholder loans against the §1361(c)(5) straight-debt safe harbor; debt that fails it can be treated as a second class of equity.
- **Blocking input:** distributions materially non-pro-rata with no shareholder agreement in the file → Missing Support finding plus a **[HIGH]** row; do not clear the election.

**3. Reconcile page 1 and Schedule K to the trial balance.**
*Goal: prove the return's income and deductions come from the books.*
- Tie page 1 ordinary income/loss and each Schedule K item through the book-to-tax reconciliation; flag every unexplained M-1 adjustment.
- Test accrued expenses payable to cash-basis shareholders (bonuses, rent, interest): under §267(a)(2) they are not deductible until paid. Year-end shareholder accruals that survived into the deduction are a routine catch.
- Trace prior-year carryovers into the return: §481(a) adjustment spread, installment-sale gross profit, §179 carryover, charitable contribution carryover, disallowed business interest, and suspended losses. A dropped carryover is an income omission the TB reconciliation cannot see.
- If the corporation holds partnership or LLC interests, tie the incoming K-1 amounts into Schedule K by character — pass-through income does not sit in the trial balance the way a reviewer expects and is easy to drop entirely.
- **Blocking inputs:** prior-year return; partnership K-1s received.

**4. Verify officer compensation, Form 1125-E, and shareholder fringes.**
*Goal: confirm compensation is reported, deductible, and defensible in amount.*
- Tie officer wages to the W-2s and payroll registers, and confirm page 1 officer compensation and salaries/wages are not double-counting the same payroll.
- Confirm **Form 1125-E is attached when total receipts are $500,000 or more** (use the instructions' definition of total receipts). Missing 1125-E above the threshold is a finding.
- Compare officer compensation to distributions and to the corporation's net income. Material distributions with little or no compensation to a shareholder performing services is the classic reasonable-compensation exposure — recharacterization as wages carries FICA liability under §3111/§3121, per Rev. Rul. 74-44 and the *Watson* line of cases. **Flag and explain the exposure; do not set a "correct" compensation figure** — that is a valuation judgment for the preparer and the client.
- Check W-2 **composition**, not just totals: a >2% shareholder is treated as a partner for fringe-benefit purposes (§1372), so accident and health premiums, group-term life, and similar benefits belong in W-2 Box 1 (excluded from Social Security and Medicare wages for health premiums) with a matching corporate deduction. Missing Box 1 treatment costs the shareholder the self-employed health insurance deduction at the 1040 level.
- If an ERC refund was received or a claim denied during the year, confirm the wage-deduction reduction was handled in the correct credit year.
- **Blocking inputs:** officer W-2s; payroll registers; distribution detail.

**5. Verify Schedule K items and character.**
*Goal: confirm each item is on the right line, in the right character, and nothing that must be separately stated is buried.*
- Check each separately stated item against source: interest, dividends, §1231, capital gains, credits, charitable contributions, §179, tax-exempt income.
- Run the check in **reverse** — scan page 1 ordinary income for items that must be separately stated (tax-exempt interest, portfolio income, §1231 gains, COD income, charitable contributions). Wrong character survives a tie-out that only looks at what already reached Schedule K.
- Confirm rental activities are on Form 8825 / Schedule K line 2 rather than netted into page 1; commingled rentals corrupt the passive-loss and §199A analyses at the shareholder level.
- Confirm the **digital-asset question on Schedule B** is answered and consistent with the source documents. Reconcile any Forms 1099-DA — broker reporting is new and basis may be missing or wrong. A "No" answer with crypto activity on custody statements is a finding.
- Confirm distributions of appreciated property triggered entity-level gain under §311(b).

**6. Verify K-1 allocations.**
*Goal: confirm the K-1s foot to Schedule K and reflect the right ownership for the right days.*
- Sum every K-1 box, code by code, to the corresponding Schedule K line. **Foot the codes, not just the totals** — offsetting code-level errors can produce a K-1 set that sums correctly and is still wrong on every return.
- Compare each shareholder's percentage to the stock ledger, shareholder agreement, or prior-year K-1.
- Allocations are **per share, per day** (§1377(a)(1)). If ownership changed mid-year, static year-end percentages produce K-1s that foot but are wrong: confirm the daily pro-rata computation, or the §1377(a)(2) closing-of-the-books election statement with the required shareholder consents if the parties chose it.
- Confirm every shareholder's identifying information and that the number of Schedules K-1 matches the shareholder count on Schedule B.
- **Hard stop:** K-1 totals that don't foot to Schedule K. The return is not fileable; halt downstream steps and surface it.

**7. Verify shareholder stock and debt basis.**
*Goal: confirm losses and distributions are supported by basis, and that the corporation furnished what shareholders need for Form 7203.*
- For each shareholder taking a loss, confirm the loss does not exceed stock plus debt basis, and that the §1366(d) ordering was applied. Detail in `references/basis-and-distributions.md`.
- Confirm debt basis rests on **bona fide indebtedness running directly from the shareholder to the corporation** (Reg. §1.1366-2(a)(2)). Guarantees of third-party debt create no basis until the shareholder actually pays; related-entity and back-to-back loans need the note and payment history in the file.
- Confirm **entity-level liabilities are not in anyone's basis** — that is partnership mechanics, and it does not apply here.
- Confirm the corporation furnished the inputs each shareholder needs for Form 7203 where a loss, non-dividend distribution, stock disposition, or loan repayment occurred.
- **Blocking input:** basis worksheets where losses or distributions flow through.
- **Hard stop:** a loss flowing through with no basis substantiation.

**8. Verify the balance sheet and book-tax reconciliation (Schedules L and M-1).**
*Goal: confirm the balance sheet ties, and that L and M-1 are present if required.*
- **First check whether they are required.** Under the Schedule B total-receipts/total-assets test (both below $250,000 — verify the applicable year's threshold and question number), Schedules L and M-1 are not required. **Schedule M-2 is still required regardless.** If L and M-1 are properly omitted, say so in the findings table rather than reporting them as missing.
- If L and M-1 are present — whether required or voluntary — reconcile them: beginning balances to the prior-year return, ending balances to the trial balance, and every unexplained movement flagged.
- Confirm loans to and from shareholders on Schedule L agree with the notes supporting debt basis in step 7 and with the distribution detail in step 2.

**9. Verify AAA, OAA, PTI, and Schedule M-2.**
*Goal: confirm the accounts that determine the taxability of future distributions are right.*
- Tie the beginning AAA, OAA, and PTI columns to the prior-year return.
- Confirm column segregation: tax-exempt income and its related nondeductible expenses go to **OAA**, not AAA. Tax-exempt income posted to AAA distorts the taxability of every later distribution.
- Confirm the AAA adjustment ordering: a net positive adjustment is applied before distributions; a net negative adjustment after. **Distributions cannot reduce AAA below zero** — a negative AAA is possible from losses, never from distributions. A distribution-driven negative AAA is an error, not a balance.
- Reconcile total distributions across the M-2, Schedule K line 16d, and the distribution detail by shareholder.
- Detail and the §1368 ordering rules in `references/basis-and-distributions.md`.
- **Blocking input:** prior-year return.

---

### Section B — First-year and new-client add-ons

**10. Run the initial-return checks.**
*Goal: confirm the positions that get copied forward for the life of the entity were set deliberately.*
- Trigger: the Initial Return box is checked, this is the first S year (including a C-to-S conversion), or this is a new client whose prior returns the firm didn't prepare.
- Work `references/initial-return-checklist.md`: Form 2553 acceptance and effective date, C-to-S conversion carryovers, tax year and accounting method, §195/§248 cost classification, statement-required elections, initial stock and debt basis, opening AAA/OAA/AE&P, and state S election.
- Year-1 treatment often controls permanently. The §195/§248 and accounting-method positions are irrevocable or need a method change to fix.

---

### Section C — Special regimes and high-risk areas

**11. Check former-C-corporation exposure.** *(Conditional — run only if prior returns or workpapers show C-corporation history, or the corporation acquired assets with a carryover basis from a C corporation under §1374(d)(8).)*
*Goal: confirm the three C-corp legacy regimes were considered and documented.*
- **Built-in gains (§1374)** — for dispositions inside the five-year recognition period, confirm a BIG workpaper exists tying to the conversion-date NUBIG schedule, and that any tax computed flows to Schedule K and reduces the shareholders' pass-through under §1366(f)(2). **Verify the analysis exists; do not compute NUBIG yourself.**
- **AE&P and distribution ordering** — distributions follow AAA, then PTI, then AE&P as a taxable dividend requiring Forms 1099-DIV, then OAA, then stock basis, then gain. Distributions beyond AAA with AE&P present and no 1099-DIV issued is a finding.
- **Excess passive investment income (§1375)** — passive investment income above 25% of gross receipts with AE&P at year end triggers entity-level tax; three consecutive such years terminates the election under §1362(d)(3).
- **LIFO recapture (§1363(d))** — for a recent conversion, confirm the recapture was reported on the final C return and the installment payments are being made.
- Detail in `references/former-c-corp-regimes.md`.
- **Blocking inputs:** prior-year and pre-conversion returns; NUBIG/appraisal schedule; BIG workpaper.

**12. Verify Section 199A / QBI reporting.**
*Goal: confirm the code V statement is complete and internally consistent. The deduction itself is computed on the shareholder's return — this is an informational-reporting check.*
- All §199A information goes in the **Box 17 code V statement**: QBI, W-2 wages, UBIA of qualified property, SSTB status, and any REIT dividends or PTP income. There is no separate box code for wages or UBIA; the statement's completeness *is* the check.
- **Separate reporting per trade or business.** More than one trade or business (including a rental that is a separate activity) requires a separate set of figures for each. One blended set is a finding and makes every shareholder's computation unverifiable.
- **QBI reasonableness** — start from each shareholder's share of ordinary business income/loss and remove items not includible: capital gains and losses, dividends, interest income not properly allocable to a trade or business, and **net §1231 gain treated as capital gain**. Note the asymmetry: §1231 **loss** treated as ordinary **is** included in QBI. Test for reasonableness against Schedule K; treat a difference you cannot explain as a **[MEDIUM]** "Preparer to analyze" row rather than reclassifying items yourself.
- **W-2 wages and UBIA allocation** — an S corporation has no special allocations, so QBI, W-2 wages, and UBIA must all be allocated on the same **per-share-per-day** percentages used in step 6. Percentages that diverge between the code V statement and the K-1 face are a finding.
- **Compensation interaction** — officer wages reduce QBI while raising the W-2 wage limitation. Note the interaction where it matters for the shareholders, but do not recommend a compensation level on §199A grounds; step 4 governs.
- **SSTB status** — disclose if the corporation, or any separate trade or business within it, is an SSTB: health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage services, investing and investment management, trading, dealing in securities, or any trade or business whose principal asset is the reputation or skill of its owners or employees. **Engineering and architecture are excluded from SSTB** for §199A purposes (§199A(d)(2)(A)) — an engineering or architecture firm flagged as an SSTB is itself a finding, and an expensive one for the shareholders.
- **Negative QBI** — a loss year produces negative QBI that must be reported; it reduces the shareholder's overall QBI and carries forward at the shareholder level.

**13. Verify depreciation, §179, and R&E treatment.**
*Goal: confirm the fixed-asset and R&E positions on the return match the workpapers and the supporting elections. This is a documentation and consistency check, not a recomputation.*
- Tie Form 4562 to the fixed-asset schedule and trial-balance additions; confirm class lives, conventions, and placed-in-service dates, and check listed-property and passenger-auto limits.
- **Bonus depreciation** — 40% for property **acquired** before January 20, 2025; 100% for property acquired and placed in service on or after that date (OBBBA). The controlling date is acquisition, including the written-binding-contract date. Confirm the register's rate matches each asset's acquisition date; a single rate applied across a straddle year is a finding. Verify against the register — don't recompute the depreciation.
- **§179** — check against the applicable year's dollar limit and phase-out, confirm the entity-level taxable-income limitation was applied, and note that each shareholder faces a separate limit on their own return.
- **§174/§174A** — confirm current-year R&E treatment (domestic currently deductible for tax years beginning after 2024; foreign capitalized and amortized over 15 years) is consistent with the workpapers and with any §174A capitalization election. If a **catch-up deduction of previously capitalized domestic R&E** appears, confirm a Rev. Proc. 2025-28 transition election or Form 3115 is in the file. An M-1 that "ties" can still reflect an unauthorized method change. If a §41 credit is claimed, confirm the §280C-style reduction or election is consistent.
- **Blocking input:** fixed-asset schedule with acquisition dates. Without it, do not clear depreciation.

**14. Verify the Section 163(j) interest limitation.**
*Goal: determine whether the limitation applies, then confirm the form and the shareholder disclosures.*
- **Small-business exception** — available only if average annual gross receipts for the three prior years are at or below the §448(c) threshold (verify the applicable year's amount) **and** the corporation is not a tax shelter. Aggregate gross receipts under §448(c)(2) with the §52(a)/(b) and §414(m)/(o) rules — a corporation under the threshold on its own books can still fail on a controlled-group basis.
- **Tax-shelter check** — a corporation that allocates more than 35% of losses to shareholders who are limited entrepreneurs (not active in management) is a syndicate, therefore a tax shelter, and cannot use the small-business exception regardless of gross receipts. Less common than in partnerships, and routinely missed when it applies.
- If the limitation applies, confirm **Form 8990** is attached and its inputs tie to the return. For tax years beginning after 2024, depreciation, amortization, and depletion are **added back to ATI again** (OBBBA) — a workpaper carried forward on the 2024 EBIT base understates the allowable deduction, which costs the client money and is still a finding.
- **Carryforward stays at the entity level.** Unlike a partnership, an S corporation carries disallowed business interest forward itself; there is no excess-business-interest-expense allocation to shareholders. A K-1 reporting EBIE to shareholders is a finding.
- Confirm **gross receipts are reported on each K-1 (Box 17 code AC)** — shareholders need it for their own §448(c) and §163(j) testing, and it is frequently omitted. Treat omission as a **[MEDIUM]** finding.
- If a §163(j)(7)(B) electing real property trade or business election is in effect, it is **irrevocable** and requires ADS for nonresidential real property, residential rental property, and QIP. Confirm step 13's register actually reflects ADS.
- **Blocking inputs:** §163(j) workpaper; prior-year Form 8990 for carryforwards.

**15. Verify Schedules K-2/K-3 and foreign reporting.**
*Goal: confirm the schedules were filed or the exception is documented — silence is not an exception.*
- Confirm K-2/K-3 were filed, or the **domestic filing exception** is documented: no or limited foreign activity, the shareholder-notification condition as it applies for the year, and **no shareholder requested a K-3 by the one-month date** (one month before the unextended due date). A request after that date means the corporation must furnish the K-3 to that shareholder even though it need not file it with the IRS. The notification condition has changed across form years — verify against the applicable year's instructions rather than a prior-year checklist.
- If the exception is not clearly met and the schedules are absent, that is a **[HIGH]** finding: the §6699 failure-to-file penalty runs **per shareholder, per month**.
- Confirm K-2/K-3 content is consistent with Schedule K and the K-1s — foreign taxes, source, and category must agree across the three.
- Confirm Forms 1042/1042-S where US-source FDAP was paid to a foreign person, and flag exposure for Forms 5471, 8858, 8865, 926, 8621, and 8938/FinCEN 114 where the source documents show foreign entities, transfers, or accounts. Each carries a standalone penalty. Hand the FBAR workpaper itself to `fbar-workpaper`.
- **Blocking input:** foreign activity detail where the source documents show foreign operations, accounts, or taxes.

**16. Verify state PTET (federal side).**
*Goal: confirm the federal deduction, the payments, and the shareholder credit disclosures all describe the same transaction. This is a coordination check — do not attempt state computations.*
- Confirm the PTET election is valid and timely for the year.
- Confirm the tax was **actually paid within the year** — deduction timing under Notice 2020-75. Accrued-but-unpaid PTET is a common mistimed deduction. Tie the deduction to the GL payment detail.
- Confirm the deduction is taken at the **entity level** rather than passed through as a separately stated state tax, and that it reduces the QBI reported in step 12.
- Confirm shareholder-level credit information — by shareholder, by state, resident vs. nonresident — appears on K-1 footnotes or state schedules.
- Confirm the **AAA impact** is booked (the PTET deduction reduces AAA), including the ordering interaction where AE&P exists.
- OBBBA as enacted did not restrict entity-level PTET deductions — do not adjust for a limitation that was not enacted, but confirm no state-level change applies.
- **Blocking input:** PTET payment records and state credit schedules.

---

### Section D — Reporting

**17. Summarize findings.** Produce the severity-graded report (see Output Format), and state which conditional steps in Sections B and C were skipped and why.

**18. Assess audit risk.** Note 1–3 items presenting elevated audit risk, stated as facts: "This item may draw scrutiny because [specific reason]."

## Elections: Statement-Required vs. Deemed

Two different failure modes, so test them differently. Do not report a missing statement for an election the regulations deem made by return treatment.

### Deemed elections — made by how the return is filed; no statement required

- **§195 start-up expenditures** — Deduct up to $5,000, reduced dollar-for-dollar to the extent start-up expenditures exceed $50,000, and amortize the remainder over 180 months beginning with the month the **active trade or business begins**. Under Reg. §1.195-1(b) the taxpayer is **deemed to elect** this treatment for that year; no election statement is required.
- **§248 organizational expenditures** — The corporate analogue: up to $5,000 (same $50,000 phase-down), remainder over 180 months beginning with the month the **corporation begins business**. Under Reg. §1.248-1(c) the corporation is **deemed to elect**; no statement is required.
- **What to test instead of a statement:**
  - **Classification** — §195 start-up vs. §248 organizational vs. **stock-issuance costs**. Costs of issuing or selling stock are capital costs that reduce paid-in capital: not deductible, not amortizable. This is the corporate parallel to partnership syndication costs, and it fails the same way.
  - **Mechanics on the return** — the $5,000 (as limited) and the 180-month amortization actually appear, starting in the correct month. A schedule keyed to the incorporation date rather than the business-start month, or defaulted to January, is a finding.
  - **Deliberateness** — capitalizing instead of deducting/amortizing forgoes the deemed election, is **irrevocable**, and applies to **all** costs in the category. If the return capitalizes, confirm it was a decision, not a data-entry default.

### Statement- or form-required elections — absence is a finding

- **§179** expensing — Form 4562, Part I; check the limit, phase-out, and taxable-income limitation
- **De minimis safe harbor**, Reg. §1.263(a)-1(f) — annual election statement
- **Bonus depreciation elect-out**, §168(k)(7) — statement by class; silence means bonus applies
- **§163(j)(7)(B) electing real property trade or business** — irrevocable, and requires ADS; must be consistent with the fixed-asset register
- **§174A** capitalize-and-amortize election, or a Rev. Proc. 2025-28 transition election / Form 3115 for an R&E method change
- **§1377(a)(2) closing of the books** — on a complete termination of a shareholder's interest; requires the statement and the consent of all affected shareholders
- **§1368(e)(3) election to distribute AE&P first**, and the deemed-dividend election — each requires a statement with shareholder consents
- **Reg. §1.1367-1(g)** — election to apply losses before nondeductible non-capital expenses in the basis ordering; binding on later years
- **§444** fiscal-year election — Form 8716, with the annual Form 8752 required payment
- **§1362(f) inadvertent termination relief** — a ruling request, not a return election; flag it rather than assuming relief

## Filing Mechanics and Required Attachments

Cheap to check, expensive to miss.

- **Return requirement and due date** — §6037(a); 15th day of the 3rd month after year end (§6072(b)), with an automatic six-month extension on Form 7004. Confirm the return is timely or the extension is in the file.
- **K-1s furnished to shareholders** — required by the return due date (§6037(b)). The §6699 penalty runs **per shareholder, per month**, and applies to an incomplete return as well as a late one.
- **E-file mandate** — verify the return is being e-filed where required; the aggregate-return threshold now captures most firms' S-corp filings.
- **Schedule B answers** — walk them. Several drive attachments or downstream steps: the digital-asset question, the total-receipts/total-assets test for Schedules L and M-1, AE&P at year end, ownership questions, and debt-forgiveness and stock-restructuring questions.
- **Form 1125-A** — required where there is inventory or cost of goods sold.
- **Form 1125-E** — required at total receipts of $500,000 or more.
- **Form 8825** — present for rental real estate rather than rentals buried on page 1.
- **Form 4797 / Form 8949** — present where asset dispositions occurred, and consistent with the BIG analysis in step 11.
- **Schedules K-2/K-3** — filed or the exception documented (step 15).
- **Form 7203** — the shareholder's form, not the corporation's. Confirm the inputs were furnished; do not report the corporation as delinquent for not attaching it.

## Control Points

Stop for a preparer decision — don't quietly reconcile past these. On any hard stop, **halt the downstream steps**, record the finding, and surface it before suggesting the return is close to fileable.

- **S election invalid or terminated** — An ineligible shareholder, a confirmed second class of stock, or a defective or missing election means the entity-level classification is wrong and every downstream check is moot. A *suspected* second class from non-pro-rata distributions is not itself a conclusion — get the governing documents (step 2) before calling it.
- **K-1 totals don't foot to Schedule K** — Allocations must equal the Schedule K totals, code by code. Any discrepancy is a hard stop; a return whose K-1s don't sum is not fileable.
- **Any discrepancy beyond the $10 rounding tolerance** — Every variance needs preparer review and correction before filing. There is no size below which a variance is ignored.
- **Shareholder loss without basis** — A loss flowing through with no basis worksheet, or a loss exceeding stock plus debt basis, is a hard stop; the loss may be non-deductible and suspended under §1366(d).
- **Distribution beyond AAA with AE&P present and no 1099-DIV** — The distribution is a taxable dividend to the shareholders; filing without the information return understates their income and misses an information-reporting obligation.

## Red Flags

Flag and explain — do not recompute or change the return.

- Ordinary income/loss doesn't reconcile to the trial balance within the rounding tolerance
- K-1 percentages don't match the stock ledger or shareholder agreement
- Distributions not proportionate to stock ownership — second-class-of-stock and inadvertent-termination risk, or payments mischaracterized as distributions
- Officer compensation appears low relative to S-corp income and shareholder services; distributions materially exceed officer W-2 wages
- Form 1125-E absent with total receipts of $500,000 or more
- >2% shareholder health premiums deducted by the corporation but absent from W-2 Box 1, or other >2% shareholder fringes not run through payroll
- Shareholder loss exceeds stock plus debt basis without a supporting schedule, or debt basis claimed from a **guarantee** of third-party debt
- Entity-level liabilities included in shareholder basis — partnership mechanics applied to an S corporation
- AAA reduced below zero **by distributions** (impermissible), or tax-exempt income posted to AAA rather than OAA
- Distributions on Schedule K line 16d, Schedule M-2, and the shareholder distribution detail that don't agree
- Schedules L and M-1 omitted without meeting the Schedule B total-receipts/total-assets test, or Schedule M-2 omitted (always required)
- Mid-year stock transfer with K-1s allocated on static year-end percentages and no §1377(a)(2) statement with shareholder consents
- Trust, estate, or exempt-organization shareholder with no QSST/ESBT or eligibility documentation
- Prior-year credits or carryforwards appearing with no schedule supporting the amount
- Former C corp: recognition-period asset sales with no built-in-gains analysis; distributions beyond AAA with AE&P present and no 1099-DIV; passive investment income over 25% of gross receipts with AE&P and no §1375 computation; a recent conversion with no LIFO recapture trail
- Distribution of appreciated property with no §311(b) gain recognized
- Box 17 code V statement blended across multiple trades or businesses, or reporting UBIA and W-2 wages under separate box codes rather than in the code V statement
- QBI, W-2 wage, or UBIA percentages that diverge from the per-share-per-day percentages on the K-1 face
- An engineering or architecture firm flagged as an SSTB, or an actual SSTB with no disclosure
- 2025 fixed-asset additions straddling January 19 all claimed at a single bonus rate, or a catch-up R&E deduction with no Rev. Proc. 2025-28 election or Form 3115 in the file
- A §163(j)(7)(B) real property elect-out with MACRS rather than ADS lives in the register
- Interest expense deducted in full with no Form 8990 despite gross receipts above the §448(c) threshold on an aggregated basis; a §163(j) computation still on the 2024 EBIT base; EBIE allocated to shareholders on a K-1; or K-1s missing the code AC gross-receipts amount
- No Schedules K-2/K-3 and no documented domestic filing exception; or K-2/K-3 content inconsistent with Schedule K and the K-1s
- Foreign taxes, accounts, or subsidiaries visible in source docs with no corresponding information returns — possible FinCEN 114 (FBAR) exposure; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- PTET deduction with no evidence the tax was paid during the year, PTET not reflected in AAA, or PTET that doesn't reduce the QBI reported on the K-1s
- ERC refund received with no corresponding wage-deduction adjustment in the credit year
- Tax-exempt interest, portfolio income, or §1231 items buried in page 1 ordinary income
- Digital-asset question on Schedule B answered "No" but a 1099-DA or crypto activity appears in the source documents
- Accrued bonuses, rent, or interest payable to a cash-basis shareholder deducted before payment (§267(a)(2))

## Output Format

**The chat response and the .docx both use the same 5-column findings table.** This is the primary deliverable — a single table where every reviewed line item appears, with its current treatment, recommended treatment, reason, and authority.

### Findings Table (required format)

A markdown table in chat, a Word table in .docx. One row per item. **Exactly these 5 columns, in this order:**

| Line / Schedule | Current treatment | Recommended treatment | Reason | Authority |
|---|---|---|---|---|
| **[HIGH]** Page 1, Line 21 | Ordinary income $45,200 | $46,100 per trial balance | Trial balance ordinary income totals $46,100; return understates by $900. | Trial balance; §61 |
| **[HIGH]** Page 1, Line 7 / Form 1125-E | Officer comp $0; distributions $310,000; total receipts $1.4M | Preparer to determine reasonable compensation and attach Form 1125-E | Sole shareholder performs all services; zero wages with material distributions is the core reasonable-compensation exposure, and Form 1125-E is required at total receipts of $500,000 or more. | §3121; Rev. Rul. 74-44; Form 1125-E instr. |
| **[HIGH]** Sch M-2, AAA column | Ending AAA $(42,000) after $180,000 of distributions | Limit the distribution reduction to zero AAA; recharacterize the excess under §1368 ordering | Distributions cannot reduce AAA below zero; the excess is tested against AE&P, then stock basis, then gain. | §1368(e); Reg. §1.1368-2(a)(3)(ii) |
| **[MEDIUM]** K-1, Box 17 code AC | Blank | Report gross receipts for §448(c) | Shareholders need entity gross receipts for their own small-business and §163(j) testing. | §448(c); Form 1120-S K-1 instr. |
| Sch L / Sch M-1 | Not completed | No change — confirmed correct | Total receipts and total assets are each below the Schedule B threshold, so Schedules L and M-1 are not required; Schedule M-2 is completed. | Form 1120-S instr., Sch B |
| Page 1, Line 7 | Officer comp $120,000 | No change — confirmed correct | Tied to W-2 and payroll registers. | §162 |

Column rules:
- **Line / Schedule** — Specific form reference (e.g., "Page 1, Line 7", "Sch K, Line 1", "K-1 Box 17 code V"). **Severity** is a bold tag at the start of this cell: **[HIGH]**, **[MEDIUM]**, **[LOW]**. Omit the tag for confirmed items.
- **Current treatment** — What the return currently shows. State "Blank" or "Not checked" when a field is omitted. Include the dollar amount inline if relevant.
- **Recommended treatment** — The specific correction, or "No change — confirmed correct" for items that tie. Use "Preparer to analyze" where the answer needs judgment or data you don't have. For optional improvements, prefix with "Optional:".
- **Reason** — The factual or legal basis for the recommendation. Explain *why*, not just *what*.
- **Authority** — IRC section, Reg., Revenue Ruling, form instructions, or source document. Use "—" if none applies.

Table rules:
- **Every reviewed item goes in the table** — issues, confirmed items, items confirmed not applicable, and optional recommendations alike. Do not omit correct items; they show the reviewer checked them.
- **Sort rows by form/schedule order** (page 1; Schedules B, K, L, M-1, M-2; K-1s; attached forms — 1125-A, 1125-E, 4562, 4797, 8825, 8949, 8990, K-2/K-3; then state and PTET items), not by severity. Severity tags handle prioritization within the natural reading flow.
- **One row per line item.** Do not split a single issue across multiple rows, and do not merge two issues into one.

### Section Organization

Surround the table with these sections:

1. **Bottom line** — 2-3 sentence summary
2. **Findings Table** — The 5-column table above
3. **Missing Support** — Bulleted list of absent source documents and workpapers, with the step each one blocked
4. **Preparer Questions** — Bulleted list of items requiring judgment, including every "Preparer to analyze" row
5. **Audit Risk** — 1-3 bullet points with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary + the findings table; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1120-S", client/S-Corp name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — 5 columns: Line/Schedule, Current treatment, Recommended treatment, Reason, Authority. Use `Table Grid` style. Bold the header row. Severity tags (**[HIGH]**, etc.) are bold prefixes in column 1.
4. **Missing support** — Bulleted list of absent source documents, with the step each one blocked
5. **Preparer questions** — Bulleted list of items requiring judgment
6. **Audit risk** — 1-3 bullet points, factual
7. **Scope note** — Which conditional steps in Sections B and C were run and which were skipped, with the reason
8. **199A/QBI verification** — Summary of the Box 17 code V statement check by trade or business (QBI, W-2 wages, UBIA, SSTB, negative QBI)

Save as `[ClientName]_[TaxYear]_1120S_Review.docx` (e.g., `ABCCorp_2025_1120S_Review.docx`).

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
- **`1040-review`** — shareholder-level follow-through (Form 7203, §199A deduction, basis, suspended losses).
- **`tax-workpapers`** — incoming 1099s and partnership K-1s that need summarizing before the tie-out.

## Safety Constraints

- Do not mark the return reviewed-complete while any hard-stop control point is open — the return isn't fileable and "complete" would be misleading.
- Do not adjust AAA, OAA, or shareholder basis yourself — surface the issue for preparer review; those balances drive shareholder-level tax and are the preparer's call.
- Do not recompute built-in gains, the §199A deduction, §163(j) ATI, R&E timing, or state PTET from scratch. Verify the workpaper exists, its inputs tie to the return, and its conclusion carries through consistently.
- Do not state a reasonable-compensation figure. Identify the exposure and the factors; the amount is a valuation judgment for the preparer and the client.
- Do not conclude that the S election is void from non-pro-rata distributions alone. The one-class test turns on the governing provisions; request them and flag the issue.
- Do not report a K-1 box or code as wrong without confirming the assignment in the applicable year's Schedule K-1 instructions. Codes are renumbered between form years.
- Do not express audit risk as a probability or percentage. State the factual reason an item may draw scrutiny; judging acceptable risk is the signing partner's decision.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (PTET elections and payments, composite returns, nonresident-shareholder withholding, apportionment) to Preparer Questions rather than reviewing them here.
