---
name: 1065-review
version: 1.14.0
description: |
  Cross-reference a completed Form 1065 (partnership income tax return) against its
  source documents — trial balance, Schedule K-1s, partnership agreement, and supporting
  schedules — to catch errors before filing. Verifies income, deductions, credits, and
  partner allocations tie out; confirms K-1 totals foot to Schedule K; tests allocated losses
  through the basis / at-risk / passive tiers; checks tax-basis capital, §704(c) disclosure,
  distributions, and transfers of partnership interests; verifies QBI, depreciation, §163(j),
  K-2/K-3 and foreign withholding, and PTET; and flags audit-risk items. Use this whenever
  someone wants a partnership return checked, tied out, or reviewed before it goes out the
  door — "review the 1065", "check the K-1s", "does this partnership return tie", "look over
  the LLC return before we file", "the K-1s don't foot" — even if they don't name the form or
  say the word "review".
allowed-tools:
- Read
- Write
- Bash
- AskUserQuestion
when-to-use: |
  "review the 1065", "partnership return review", "check the K-1s", "1065 cross-reference",
  "tie out the partnership return", "verify the 1065", "check the partnership return",
  "review the LLC return", "do the K-1s foot", "K-1s don't tie", "partner allocations",
  "check partner basis", "look over the 1065 before we file"
metadata:
  tier: power-user
---

# 1065 Review: Partnership Return Cross-Reference

## Purpose

Catch errors before a Form 1065 is filed. Verify that income, deductions, and partner allocations tie to the trial balance and source documents, and that K-1 totals are mathematically consistent with Schedule K. The deliverable is a severity-graded findings report a preparer can act on line by line.

This is a technical review for a professional preparer; it does not replace the signing partner's sign-off.

## Accuracy Standard

Tax returns must be substantially correct, so the tolerance here is tight. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

Do **not** apply a percentage-based materiality threshold — no percentage of gross receipts, total assets, or net income. That approach belongs in a financial statement audit; a variance that is immaterial to the financials can still be a filing error on a tax return.

Classify findings by severity (impact + risk), not by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table — including items you are uncertain about or consider low-severity. Severity ranks the list; it does not filter it. Deciding what to act on is the preparer's job at a later step; your job here is complete coverage, and a variance you drop because it "looked minor" is the one that surfaces after filing.

## Terminology

Use these terms consistently across the review and both reference checklists.

**Concepts**
- **Outside basis** — the partner's adjusted basis in the partnership interest (§705): tax-basis capital plus the partner's share of partnership liabilities. Partner-level; the partnership supplies inputs, not the answer.
- **Tax-basis capital** — the Schedule K-1 Part II Item L capital account maintained under the transactional approach (Notice 2019-66). **Excludes** §743(b) adjustments.
- **Recourse / qualified nonrecourse financing (QNRF) / nonrecourse** — the three-way liability split on Schedule K-1 Item K1. "QNRF" is the §465(b)(6) real-property category; use the same three labels everywhere.
- **Hot assets** — §751 unrealized receivables and inventory (substantially appreciated inventory for §751(a) purposes).
- **Mixing-bowl** — the §737 and §704(c)(1)(B) seven-year distribution rules.
- **EBIE / ETI / EBII** — §163(j) excess business interest expense, excess taxable income, excess business interest income.

**Form locations — do not abbreviate either "Item K" without its qualifier**
- **Form 1065 page 1, Item K(1) / K(2)** — the entity-level §465 at-risk **aggregation** and §469 passive **grouping** checkboxes.
- **Schedule K-1 Part II, Item J** — profit/loss/capital percentages, plus the "decrease due to sale or exchange of partnership interest" checkbox.
- **Schedule K-1 Part II, Item K1 / K2 / K3** — liability split (nonrecourse / QNRF / recourse) / lower-tier partnership liabilities included / liabilities subject to partner guarantees or other payment obligations.
- **Schedule K-1 Part II, Item L** — capital account analysis and the capital-account method checkboxes.
- **Schedule K-1 Part II, Item M** — "Did the partner contribute property with a built-in gain or loss?"
- **Item N** — Schedule K-1 Part II, net unrecognized §704(c) gain or loss, beginning and ending.

**Box codes cited in this skill** — shorthand only. **K-1 box and code assignments have been renumbered more than once; verify every code against the applicable year's Form 1065 Schedule K-1 instructions before reporting a code as wrong.** Software defaults lag form changes, and a review finding that cites a stale code is itself a finding.
- **Box 11 code F / Box 13 code V** — §743(b) positive / negative income adjustments
- **Box 13 code K1** — excess business interest expense (recent forms split the former single code K into K1/K2/K3)
- **Box 20 code Z** — §199A information, furnished as a supporting statement (QBI, W-2 wages, UBIA, SSTB status). There is no separate box code for wages or UBIA; the statement is the deliverable.
- **Box 20 codes AE / AF** — excess taxable income / excess business interest income
- **Box 20 code AG** — gross receipts for §448(c)
- **Box 20 codes AB / AC / AD** — §751 gain (loss) / §1(h)(5) collectibles gain / unrecaptured §1250 gain: the character detail a transferor needs, matching the Form 8308 detail

## Required Inputs

- Completed Form 1065 and all schedules (B-1/B-2 as applicable, K, K-1s, L, M-1, M-2, M-3 if required)
- Trial balance or financial statements for the tax year
- Partnership agreement (for allocation percentages and special allocations)
- Prior-year return (for capital account balances, basis, carryforwards)
- Partner basis schedules (if losses are allocated)
- Distribution detail by partner and date (to test distributions against basis)
- Contributed-property and §704(c) tracking schedules, if any property came in with FMV ≠ basis
- Fixed-asset schedule with acquisition **and** placed-in-service dates
- §163(j) workpaper and prior-year Form 8990, if applicable
- Forms 8804/8805/8813, 1042/1042-S, and withholding records, if any partner is foreign
- Any supporting workpapers
- CCH Axcess Diagnostics report and Input Override Report (if available)

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Before starting, confirm the required inputs are present. A review run against a missing K-1 or an absent partnership agreement produces false "confirmed" items and misses real allocation errors — surface what's missing rather than reviewing around the gap.

Detailed procedures for the loss-limitation tiers, distributions, transfers, and §704(c) live in **`references/loss-limits-and-transactions.md`**; the first-year checks live in **`references/initial-return-checklist.md`**. Read each when you reach the step that points to it.

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss through M-1. Flag unexplained book-to-tax adjustments. Trace prior-year carryovers into the current return: a §481(a) adjustment spread, installment-sale gross profit, §179 carryover, excess business interest expense, and suspended losses — the prior-year return is a required input, and a dropped carryover is a straight income omission the TB reconciliation can't catch.
2. **Verify Schedule K items** — Check each separately stated item against source (interest, dividends, Section 1231, QBI, credits, etc.). Confirm the digital-asset question on **Schedule B (Other Information)** — not page 1 — is answered and consistent with the source documents — a 1099-DA or crypto activity on custody statements with a "No" answer is a finding. Reconcile any Forms 1099-DA (broker reporting is new; basis may be missing or wrong). Confirm rental activities are segregated on Form 8825 / Schedule K line 2 rather than commingled with line 1 — commingled rentals are wrong character of income and corrupt the passive-loss, at-risk, and QBI analyses simultaneously. Verify self-employment earnings (line 14a / K-1 code A) are computed for general partners and active LLC members and include guaranteed payments for services; confirm no partner received a W-2 — all partner compensation flows through the K-1. Guaranteed payments for services and for capital must be stated separately (K-1 lines 4a/4b).
3. **Verify K-1 allocations** — Confirm K-1 totals for all partners sum to Schedule K. Verify percentages tie to the partnership agreement or are consistent with prior year. Foot the Analysis of Net Income (Loss) grid to Schedule K and verify partner-type classification (general vs. limited, individual vs. corporate) — misclassification feeds SE income errors and IRS matching notices. Check the Part II identity items: a disregarded-entity partner (Item H2) must show the beneficial owner's name and TIN, and a retirement-plan partner (Item I2) needs UBTI information reported.
4. **Verify partner outside basis inputs** — Outside basis is computed on the partner's return; the partnership's job is to furnish accurate inputs. For each partner receiving a loss, confirm the inputs support the loss: tax-basis capital plus the §752 share of liabilities, adjusted for current-year contributions and distributions. Check the Item K1 detail, not just the total — the three-way split (nonrecourse / QNRF / recourse) drives each partner's at-risk amount, a guarantee or other payment obligation (Item K3) flips recourse allocation, and lower-tier partnership liabilities must be separately identified (Item K2). Remember that allocated EBIE reduces outside basis when allocated even though it is not currently deductible. Flag losses exceeding basis: they are limited under §704(d) and carry forward.
5. **Verify the remaining loss-limitation tiers (at-risk and passive)** — Basis is only the first gate. Work the three tiers **in order** — §704(d) basis, then §465 at-risk, then §469 passive — per `references/loss-limits-and-transactions.md`. Loss disallowed at the basis tier never reaches the at-risk or passive tiers, so an at-risk or passive computation run on the full allocated loss is wrong. At the entity level the review is about **detail and classification**, not the partner's answer: page 1 Item K(1)/K(2) checkboxes, activity-by-activity K-1 reporting, grouping consistency with prior year, and related-party rentals flagged for self-rental analysis. A loss can clear basis and still be non-deductible — and missing activity segregation makes every downstream partner return wrong.
6. **Verify capital accounts (Schedule L and K-1 Part II)** — Tie beginning tax-basis capital to prior-year K-1s. Verify the transactional roll for each partner (Notice 2019-66): beginning capital + contributions ± tax-basis income/loss − distributions ± other adjustments = ending capital. Confirm the Item L method checkbox says tax basis and matches how the accounts are actually maintained. Confirm **§743(b) adjustments are excluded** from tax-basis capital and tracked on a separate schedule — 743(b) embedded in tax capital is a pervasive software/legacy error that misstates the partner's capital every year thereafter.
7. **Check for special allocations and §704(c)** — If the partnership agreement has special allocations, verify they are reflected in the K-1s. Under §704(b), special allocations must have substantial economic effect; if any are present, flag that the economic effect test (or the alternate test) should be documented. For property contributed with FMV ≠ basis, verify the §704(c) allocation method is identified property-by-property (traditional, traditional with curative, or remedial), applied consistently, and actually followed in the depreciation and gain allocations — and that **Item N** is completed and reconciles to the internal §704(c) tracking schedules. Item M and Item N must agree: "Yes" in Item M with a blank Item N is an internal inconsistency on the face of the K-1. Blank Item N on a partnership holding §704(c) property is a finding. Procedures in `references/loss-limits-and-transactions.md`.
8. **Verify distributions and transfers of partnership interests** — Test every distribution against the distributee's outside basis: §731(a)(1) gain where money (including deemed money from liability decreases) exceeds basis, no loss on nonliquidating distributions, §731(c) marketable securities treated as money unless an exception is identified, Form 7217 information for property distributions, and the §737 / §704(c)(1)(B) mixing-bowl rules. For any transfer of an interest, verify Item J changes and the sale-or-exchange checkbox are supported, §706 varying-interest allocations were made on a consistent method, hot assets were analyzed and Form 8308 filed with the required §751(a) detail, any §743(b) adjustment is computed and reported, and — if the transferor is foreign — §1446(f) withholding and §864(c)(8) reporting were addressed. Procedures in `references/loss-limits-and-transactions.md` — these transactional events are invisible to the TB reconciliation and carry their own penalties.
9. **Verify Section 199A / QBI reporting** — §199A information goes on **Box 20 code Z** as a supporting statement; the statement's completeness *is* the check. Per trade or business, confirm:
   - **Separate reporting per trade or business.** A partnership with more than one trade or business (including rentals that are separate activities) must report QBI, W-2 wages, UBIA, and SSTB status **for each**. One blended set of figures is a finding and makes every partner's §199A computation unverifiable.
   - **QBI starting point** — the partner's share of Schedule K line 1 ordinary business income/loss, plus line 2 rental income where the rental rises to a §162 trade or business or meets the Rev. Proc. 2019-38 safe harbor, less items not includible in QBI: capital gains and losses, dividends, interest income not properly allocable to a trade or business, and **net §1231 gain treated as capital gain**. Note the asymmetry — §1231 **loss** treated as ordinary **is** included in QBI.
   - **Guaranteed payments, both directions** — excluded from the recipient partner's QBI, **and** the partnership's deduction for them reduces the QBI allocated to all partners. Removing the payment from the recipient's QBI without reducing entity-level QBI double-counts the benefit.
   - **Entity-level deductions reduce QBI** — a page 1 PTET deduction lowers ordinary income and therefore QBI. Confirm this step and step 13 agree.
   - **W-2 wage allocation** — each partner's share of W-2 wages must be determined in the same manner as that partner's share of the **wage expense deduction** (Reg. §1.199A-2(b)(3)), not by general profit percentage. A partnership with special allocations that spreads wages pro-rata by ownership is a finding.
   - **UBIA allocation** — allocated in the same proportion as **tax depreciation** on the qualified property for the year (Reg. §1.199A-2(a)(3)). Where §704(c) property or a curative/remedial method skews depreciation allocations, UBIA must follow. This is the most common QBI/§704(c) inconsistency — reconcile against step 7.
   - **SSTB status** — disclose if the partnership, or any separate trade or business within it, is an SSTB: health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage services, investing and investment management, trading, dealing in securities, or any trade or business whose principal asset is the reputation or skill of its owners or employees. **Engineering and architecture are excluded from SSTB** for §199A purposes (§199A(d)(2)(A)) — an engineering or architecture firm flagged as an SSTB is itself a finding, and an expensive one for the partners.
   - **Negative QBI** — a loss year produces negative QBI that must be reported; it reduces the partner's overall QBI and carries forward at the partner level.
10. **Verify depreciation, §179, and R&E capitalization** — Tie Form 4562 to the fixed-asset schedule and trial-balance additions; depreciation is a book-tax difference the TB reconciliation alone can't validate. Confirm each significant addition's class life, convention, and placed-in-service date, and check listed-property and passenger-auto limits. Then work the 2025 regime changes, which make software defaults unreliable:
   - **Split-rate bonus depreciation** — 40% for property **acquired** before January 20, 2025; 100% for property acquired and placed in service on or after that date (OBBBA). The controlling date is acquisition (including the written-binding-contract date), not placed-in-service. A fixed-asset register that applies one rate to the whole year is a finding, and a straddle year is where it happens.
   - **§179** — Check against the applicable year's dollar limit and phase-out threshold, confirm the partnership-level taxable-income limitation was applied, and note that each partner faces a separate limit on their own return — a partnership §179 election does not guarantee a partner deduction.
   - **§174/§174A** — Domestic research costs are currently deductible for tax years beginning after 2024; foreign R&E remains capitalized and amortized over 15 years. Any catch-up deduction of previously capitalized domestic R&E must be supported by a Rev. Proc. 2025-28 transition election or Form 3115, and an election to capitalize and amortize domestic R&E under §174A must be documented. An M-1 that "ties" can still reflect an unauthorized method change. If a §41 credit is claimed, confirm the §280C-style reduction or election is consistent with the R&E treatment.
   - **Handoffs** — A building placed in service or a major leasehold buildout is a cost-segregation question; route it to `costseg-analysis` rather than analyzing it here. Substantive R&E activity with no study is a question for `rd-analysis`.
11. **Verify the Section 163(j) interest limitation** — First determine whether the limitation applies at all:
   - **Small-business exception** — Available only if average annual gross receipts for the three prior years are at or below the §448(c) threshold (inflation-adjusted; verify the applicable year's amount) **and** the partnership is not a tax shelter. Gross receipts must be aggregated under §448(c)(2) with the §52(a)/(b) and §414(m)/(o) rules — a partnership under the threshold on its own books can still fail on a controlled-group basis.
   - **Syndicate disqualifier** — A partnership that allocates more than 35% of losses to limited partners or limited entrepreneurs is a syndicate, therefore a tax shelter, and **cannot** use the small-business exception regardless of gross receipts. This is the most common missed Form 8990. It is the same test that can force accrual accounting — confirm the two conclusions on this return agree.
   - **Form 8990** — Attached when required, and the computation supports the limit.
   - **ATI base for tax years beginning after 2024** — Depreciation, amortization, and depletion are **added back to ATI again** (OBBBA). A workpaper carried forward on the 2024 EBIT base understates the allowable deduction; that costs the client money and is still a finding.
   - **Partner-level reporting** — EBIE allocated on Box 13 code K1, with ETI (Box 20 code AE) and EBII (Box 20 code AF) reported so partners can determine whether prior-year EBIE becomes deductible. Report gross receipts (Box 20 code AG) so partners can run their own §448(c) test. Prior-year disallowed-interest carryforwards must tie to the prior return.
   - **Electing real property trade or business** — If the partnership elected out under §163(j)(7)(B), the election is **irrevocable** and requires ADS for nonresidential real property, residential rental property, and QIP. Confirm the depreciation in step 10 actually reflects ADS; an elect-out with MACRS lives in the fixed-asset register is a HIGH finding on both steps.
12. **Verify Schedules K-2/K-3 and foreign-partner withholding** —
   - **K-2/K-3 filed, or the domestic filing exception documented** — The exception requires no or limited foreign activity, all direct partners of eligible types (US individuals and specified domestic estates, grantor trusts, non-grantor trusts, and single-shareholder S corporations), and that **no partner requested a K-3 by the one-month date** (one month before the unextended due date). If a partner requests after that date, the partnership must furnish the K-3 to that partner even though it need not file it with the IRS. The partner-notification condition applied in earlier form years and has since changed — verify the conditions against the applicable year's instructions rather than a prior-year checklist. **Silence is not an exception**: the failure-to-file penalty runs **per partner, per month**.
   - **§1446(a) — ECI withholding** — If any partner is foreign, verify withholding on effectively connected taxable income was computed, paid via quarterly Forms 8813, and reported on Forms 8804/8805. The withholding liability is the **partnership's own**, with entity-level penalties and interest — this is not a partner-level exposure.
   - **§1441/§1442 — FDAP** — US-source fixed or determinable income allocable to a foreign partner is separately withheld on and reported on Forms 1042/1042-S. A partnership that filed 8804/8805 and nothing else, while allocating US-source dividends or interest to foreign partners, has a gap.
   - **§1446(f)** — A foreign partner's transfer of an interest in a partnership engaged in a US trade or business triggers transferee withholding, with a secondary obligation on the partnership if the transferee did not withhold. Coordinate with step 8.
   - **Foreign information returns** — Flag exposure for Forms 8865, 5471, 8858, 926, 8621, and 8938/FinCEN 114 where the source documents show foreign entities, transfers, or accounts. Each carries its own standalone penalty. Hand the FBAR workpaper itself to `fbar-workpaper`.
13. **Verify state PTET (federal side)** — If a state pass-through entity tax election was made: confirm the election is valid and timely for the year; the tax was **actually paid within the year** (deduction timing under Notice 2020-75 — accrued-but-unpaid PTET is a common mistimed deduction); the deduction is taken at the entity level on page 1 rather than passed through as a separately stated state tax; the deduction's effect on QBI is reflected in step 9; and partner-level credit information (by partner, by state, resident vs. nonresident) appears on K-1 footnotes or state schedules. OBBBA as enacted did not restrict entity-level PTET deductions — do not adjust for a limitation that was not enacted, but confirm no state-level change applies.
14. **Initial-return branch** — If the Initial Return box is checked (or the facts show this is year 1), run `references/initial-return-checklist.md`: entity-classification posture, formation date vs. business start date, tax-year and accounting-method adoption, start-up / organizational / syndication cost classification, the statement-required elections, BBA/CPAR posture, beginning tax-basis capital equal to initial contributions, and basis tracking initiated. Year-1 treatment frequently controls permanently — the §195/§709 and accounting-method choices are irrevocable or require a method change to fix.
15. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
16. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Elections: Statement-Required vs. Deemed

Two different failure modes, so test them differently. Do not report a missing statement for an election the regulations deem made by return treatment.

### Deemed elections — made by how the return is filed; no statement required

- **§195 start-up expenditures** — Deduct up to $5,000, reduced dollar-for-dollar to the extent start-up expenditures exceed $50,000, and amortize the remainder over 180 months beginning with the month the **active trade or business begins**. Under Reg. §1.195-1(b) the taxpayer is **deemed to elect** this treatment for the year the active trade or business begins; no election statement is required.
- **§709 organizational expenses** — Same mechanics at the partnership level: deduct up to $5,000 (same $50,000 phase-down) and amortize the remainder over 180 months beginning with the month the **partnership begins business**. Under Reg. §1.709-1(b)(2) the partnership is **deemed to elect** this treatment for the year it begins business; no election statement is required.
- **What to test instead of a statement:**
  - **Classification** — §195 start-up vs. §709 organizational vs. **syndication**. Organizational expenses must meet §709(b)(3) / Reg. §1.709-2(a) (incident to creation of the partnership, chargeable to capital account, and of a character that would be amortized over the partnership's life). Syndication costs — selling or issuing partnership interests, promotional and marketing materials, offering memoranda, brokerage and placement fees, registration fees, and the legal and accounting fees attributable to the offering — are **capitalized permanently** under Reg. §1.709-2(b): not deductible, not amortizable.
  - **Mechanics on the return** — the $5,000 (as limited) and the 180-month amortization actually appear, and amortization starts in the **correct month**: business-start month for §195, partnership-begins-business month for §709. These can differ from the formation date and from each other.
  - **Deliberateness** — capitalizing instead of deducting/amortizing forgoes the deemed election. That choice is **irrevocable** and applies to **all** costs in the category. If the return capitalizes, confirm it was a decision and is documented, not a data-entry default.

### Statement- or form-required elections — absence is a finding

- **§179** expensing — elected on Form 4562, Part I; verify against the applicable year's limit, phase-out, and the taxable-income limitation
- **De minimis safe harbor**, Reg. §1.263(a)-1(f) — annual election statement attached
- **Bonus depreciation elect-out**, §168(k)(7) — statement by class; silence means bonus applies
- **§163(j)(7)(B) electing real property trade or business** — irrevocable; requires ADS depreciation, so it must be consistent with the fixed-asset register
- **§174A** capitalize-and-amortize election, or a Rev. Proc. 2025-28 transition election / Form 3115 for an R&E method change
- **§754** — signed statement attached; once in effect it binds subsequent years until revoked with consent
- **§444** fiscal-year election — Form 8716, with the annual Form 8752 required payment
- **BBA/CPAR** — elect out under §6221(b) on a timely filed return with **Schedule B-2** listing every eligible partner; otherwise designate a partnership representative
- **§471(c)** small-taxpayer inventory method and other method adoptions made by return treatment in year 1 — see `references/initial-return-checklist.md`

## Filing Mechanics and Required Attachments

Cheap to check, expensive to miss.

- **Due date and extension** — 15th day of the 3rd month after year end (§6072(b)); automatic six-month extension on Form 7004 (Reg. §1.6081-2). Confirm the return is timely or the extension is in the file.
- **K-1s furnished to partners** — Required by the return due date (§6031(b)). The §6698 failure-to-file/furnish penalty runs **per partner, per month**, and applies to an incomplete return as well as a late one.
- **E-file mandate** — Verify the return is being e-filed where required; the aggregate-return threshold now captures most firms' partnership filings (Reg. §301.6011-3).
- **Schedule B answers** — Walk them; several drive attachments (foreign partners, §754 election in effect, debt forgiveness, like-kind exchanges, distributions of appreciated property, ownership questions).
- **Schedule B-1** — Required where any entity or individual owns 50% or more, directly or indirectly.
- **Schedule B-2** — Required with a §6221(b) elect-out; the election fails without it.
- **Schedules C and M-3** — Required at the asset/receipts thresholds or with a reportable entity partner. Confirm the page 1 checkbox and the schedule agree.
- **Form 8825** — Present for rental real estate rather than rentals buried on page 1.

## Control Points

- **K-1 total mismatch** — K-1 allocations must equal Schedule K totals. Any discrepancy is a hard stop: at least one partner's K-1 is wrong, and the error flows straight to that partner's return.
- **Capital account method** — Confirm whether capital accounts are reported on tax basis, GAAP, §704(b), or other, and that the Item L checkbox matches the actual maintenance. Tax-basis capital must use the transactional approach (Notice 2019-66) with §743(b) **excluded**. Flag any change from prior year; a silent method change breaks the beginning-to-ending capital roll and can misstate every partner's balance.
- **Partner loss without basis** — A loss allocated to a partner without supporting outside basis inputs is a hard stop. Under §704(d) the loss is limited and carried forward, so reporting it as currently deductible overstates the partner's deduction.
- **Loss-tier ordering** — §704(d) first, then §465, then §469. Any workpaper that applies at-risk or passive limits to loss already disallowed for lack of basis is computed wrong regardless of the arithmetic.
- **Syndicate consistency** — The >35%-of-losses-to-limited-partners test drives both the accrual-method requirement and the §163(j) small-business exception. A return that reaches opposite conclusions on the same facts is internally inconsistent; resolve it before sign-off.

## Red Flags

- K-1 percentages don't match the partnership agreement
- Capital account balances don't foot to the balance sheet, or the Item L method checkbox contradicts how the accounts are maintained
- Large guaranteed payment without a corresponding expense deduction, or services and capital not split between lines 4a and 4b
- Negative capital accounts without a deficit restoration obligation or qualified income offset
- §743(b) or §734(b) adjustments present but no supporting schedule, or §743(b) included in tax-basis capital
- Partner's share of loss exceeds outside basis — limited under §704(d)
- Liability allocations under §752 not documented — affects outside basis for all partners
- Guaranteed payments: confirm deductibility and self-employment tax treatment
- Partnership has not elected out of the centralized partnership audit regime (BBA/CPAR) under §6221(b), or elected out with no Schedule B-2 — confirm election status
- Cross-return coordination needed: K-1 amounts should tie to each partner's Form 1040 or entity return
- Digital-asset question answered "No" but a 1099-DA or crypto activity appears in the source documents
- Foreign tax paid, foreign accounts, or foreign partners visible in source docs — possible FinCEN 114 (FBAR) / foreign information-return exposure; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- 2025 fixed-asset additions straddling January 19 all claimed at a single bonus rate, or a catch-up R&E deduction with no Rev. Proc. 2025-28 election or Form 3115 in the file
- A §163(j)(7)(B) real property elect-out with MACRS rather than ADS lives in the fixed-asset register
- Interest expense deducted in full with no Form 8990 despite gross receipts above the §448(c) threshold on an aggregated basis, or despite syndicate status
- §163(j) computation still on the 2024 EBIT base for a tax year beginning after 2024 — understates the deduction
- EBIE allocated to partners with no corresponding reduction to outside basis inputs
- No Schedules K-2/K-3 and no documented domestic filing exception; or 8804/8805 filed with no 1042/1042-S despite US-source FDAP allocated to foreign partners
- A foreign partner's transfer with no §1446(f) withholding or §864(c)(8) analysis
- PTET deduction on page 1 with no evidence the tax was paid during the year, or a PTET deduction that doesn't reduce the QBI reported on the K-1s
- Box 20 code Z blended across multiple trades or businesses; W-2 wages or UBIA allocated by ownership percentage in a partnership with special allocations or §704(c) property
- An engineering or architecture firm flagged as an SSTB, or an actual SSTB with no disclosure
- A partner on payroll (W-2), or line 14a blank while general partners/active LLC members have ordinary income or guaranteed payments for services
- A distribution exceeding the distributee's outside basis with no §731(a)(1) gain reported, or a property distribution with no Form 7217 information furnished
- A loss recognized on a nonliquidating distribution, or on a liquidating distribution that included property other than money, unrealized receivables, and inventory
- Marketable securities distributed and treated as property with no §731(c) exception identified
- Item J percentages changed from prior year with no Form 8308 and no transfer documentation, or "all capital gain" reported by a transferor in a partnership holding hot assets
- Item M answered "Yes" with Item N blank; or Item N populated but not reconciling to the §704(c) tracking schedule
- Amortization of syndication costs, or start-up and organizational costs lumped into one figure with no §195 / §709 / syndication split
- 180-month amortization starting at the formation date rather than the business-start month
- Initial Return box checked with no first-year review performed

## Output Format

**The chat response and the .docx both use the same 5-column findings table.** This is the primary deliverable — a single table where every reviewed line item appears, with its current treatment, recommended treatment, reason, and authority.

### Findings Table (required format)

A markdown table in chat, a Word table in .docx. One row per item. **Exactly these 5 columns, in this order:**

| Line / Schedule | Current treatment | Recommended treatment | Reason | Authority |
|---|---|---|---|---|
| **[HIGH]** Sch K, Line 1 | Ordinary income $78,500 | $79,200 per trial balance | Trial balance ordinary income totals $79,200; return understates by $700. | Trial balance; §702 |
| **[HIGH]** Form 8990 | Not attached; interest expense $412,000 deducted in full | Compute §163(j); attach Form 8990 | 41% of losses allocated to limited partners makes the partnership a syndicate, so the §448(c) small-business exception is unavailable regardless of gross receipts. | §163(j)(3); §448(d)(3); §1256(e)(3)(B) |
| **[HIGH]** K-1 Part II, Item N | Blank; Item M answered "Yes" | Report beginning and ending net unrecognized §704(c) gain | Mandatory disclosure for partnerships with §704(c) property; Item M and Item N contradict each other on the face of the K-1. | §704(c); Form 1065 K-1 instr. |
| **[MEDIUM]** K-1, Box 20 code Z | W-2 wages allocated 50/50 by ownership | Allocate in proportion to each partner's share of wage expense | Partnership specially allocates wage expense 70/30; §199A wage allocation must follow the wage expense deduction, not profit percentage. | Reg. §1.199A-2(b)(3) |
| Page 1, Line 20 | Organizational costs: $5,000 deducted, $9,400 amortized over 180 months from June 2025 | No change — confirmed correct | Costs meet Reg. §1.709-2(a); amortization starts in the month the partnership began business; deemed election under Reg. §1.709-1(b)(2), no statement required. | §709(b); Reg. §1.709-1(b)(2) |
| Page 1, Line 10 | Guaranteed payments $24,000 | No change — confirmed correct | Tied to payroll registers and partnership agreement. | §707(c) |

Column rules:
- **Line / Schedule** — Specific form reference (e.g., "Page 1, Line 10", "Sch K, Line 1", "K-1 Box 1"). **Severity** is a bold tag at the start of this cell: **[HIGH]**, **[MEDIUM]**, **[LOW]**. Omit the tag for confirmed items.
- **Current treatment** — What the return currently shows. State "Blank" or "Not checked" when a field is omitted. Include the dollar amount inline if relevant.
- **Recommended treatment** — The specific correction, or "No change — confirmed correct" for items that tie. Use "Preparer to analyze" where the answer needs judgment or data you don't have. For optional improvements, prefix with "Optional:".
- **Reason** — The factual or legal basis for the recommendation. Explain *why*, not just *what*.
- **Authority** — IRC section, Reg., Revenue Ruling, form instructions, or source document. Use "—" if none applies.

Table rules:
- **Every reviewed item goes in the table** — issues, confirmed items, items confirmed not applicable, and optional recommendations alike. Do not omit correct items; they show the reviewer checked them.
- **Sort rows by form/schedule order** (page 1, then Schedules B, K, L, M-1, M-2, then K-1s and attached forms), not by severity. Severity tags handle prioritization within the natural reading flow.
- **One row per line item.** Do not split a single issue across multiple rows, and do not merge two issues into one.

### Section Organization

Surround the table with these sections:

1. **Bottom line** — 2-3 sentence summary
2. **Findings Table** — The 5-column table above
3. **Missing Support** — Bulleted list of absent source documents
4. **Preparer Questions** — Bulleted list of items requiring judgment
5. **Audit Risk Items** — 1-3 bullet points with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary + the findings table; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1065", client/Partnership name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — 5 columns: Line/Schedule, Current treatment, Recommended treatment, Reason, Authority. Use `Table Grid` style. Bold the header row. Severity tags (**[HIGH]**, etc.) are bold prefixes in column 1.
4. **Missing support** — Bulleted list of absent source documents
5. **Preparer questions** — Bulleted list of items requiring judgment
6. **Audit risk** — 1-3 bullet points, factual
7. **199A/QBI verification** — Summary of the QBI check results by trade or business (Box 20 code Z statement completeness, W-2 wages, UBIA, SSTB)

Save as `[ClientName]_[TaxYear]_1065_Review.docx` (e.g., `ABCLLP_2025_1065_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity tags in column 1
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete if K-1 totals don't foot to Schedule K.
- Do not adjust capital accounts or basis without preparer review.
- Do not compute a partner's final at-risk or passive result as if it were the partnership's determination — outside basis, at-risk, material participation, real-estate-professional status, grouping, and the §199A deduction itself are partner-level. Report whether the partnership furnished the detail those computations require.
- Do not report a K-1 box or code as wrong without confirming the assignment in the applicable year's Schedule K-1 instructions. Codes are renumbered between form years.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (PTET elections and payments, composite returns, nonresident-partner withholding, apportionment) to Preparer Questions rather than reviewing them here.
