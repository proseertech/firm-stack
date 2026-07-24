---
name: 1065-review
version: 1.11.0
description: |
  Cross-reference a completed Form 1065 (partnership income tax return) against its
  source documents — trial balance, Schedule K-1s, partnership agreement, and supporting
  schedules — to catch errors before filing. Verifies income, deductions, credits, and
  partner allocations tie out; confirms K-1 totals foot to Schedule K; checks partner
  outside basis against allocated losses; and flags audit-risk items. Use this whenever
  someone wants a partnership return checked, tied out, or reviewed before it goes out the
  door — "review the 1065", "check the K-1s", "does this partnership return tie", "look over
  the LLC return before we file", "the K-1s don't foot" — even if they don't name the form
  or say the word "review".
trigger: |
  "review the 1065", "partnership return review", "check the K-1s", "1065 cross-reference",
  "tie out the partnership return", "verify the 1065", "check the partnership return",
  "review the LLC return", "do the K-1s foot", "K-1s don't tie", "partner allocations",
  "check partner basis", "look over the 1065 before we file"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
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

## Required Inputs

- Completed Form 1065 and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Partnership agreement (for allocation percentages and special allocations)
- Prior-year return (for capital account balances, basis, carryforwards)
- Partner basis schedules (if losses are allocated)
- Distribution detail by partner and date (to test distributions against basis)
- Forms 8804/8805 and withholding records, if any partner is foreign
- Any supporting workpapers
- CCH Axcess Diagnostics report and Input Override Report (if available)

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

Before starting, confirm the required inputs are present. A review run against a missing K-1 or an absent partnership agreement produces false "confirmed" items and misses real allocation errors — surface what's missing rather than reviewing around the gap.

Detailed procedures for the loss-limitation tiers, distributions, and interest transfers live in **`references/loss-limits-and-transactions.md`**; the first-year checks live in **`references/initial-return-checklist.md`**. Read each when you reach the step that points to it.

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss through M-1. Flag unexplained book-to-tax adjustments. Trace prior-year carryovers into the current return: a §481(a) adjustment spread, installment-sale gross profit, §179 carryover, excess business interest expense, and suspended losses — the prior-year return is a required input, and a dropped carryover is a straight income omission the TB reconciliation can't catch.
2. **Verify Schedule K items** — Check each separately stated item against source (interest, dividends, Section 1231, QBI, credits, etc.). Confirm the digital-asset question on page 1 is answered and consistent with the source documents — a 1099-DA or crypto activity on custody statements with a "No" answer is a finding. Reconcile any Forms 1099-DA (broker reporting is new; basis may be missing or wrong). Confirm rental activities are segregated on Form 8825 / Schedule K line 2 rather than commingled with line 1 — commingled rentals are wrong character of income and corrupt both the passive-loss and QBI analyses. Verify self-employment earnings (line 14a / K-1 code A) are computed for general partners and active LLC members and include guaranteed payments for services; confirm no partner received a W-2 — all partner compensation flows through the K-1. Guaranteed payments for services and for capital must be stated separately (K-1 lines 4a/4b).
3. **Verify K-1 allocations** — Confirm K-1 totals for all partners sum to Schedule K. Verify percentages tie to the partnership agreement or are consistent with prior year. Foot the Analysis of Net Income (Loss) grid to Schedule K and verify partner-type classification (general vs. limited, individual vs. corporate) — misclassification feeds SE income errors and IRS matching notices.
4. **Verify partner outside basis** — For each partner receiving a loss, confirm outside basis is sufficient. Outside basis = capital account (tax basis) + share of liabilities. If liabilities are allocated under IRC 752, check that recourse/nonrecourse allocation is consistent with the partnership agreement. Flag losses exceeding basis — these are suspended under IRC 704(d). Check the K-1 Item K detail, not just the total: the three-way split (recourse / qualified nonrecourse / nonrecourse) drives each partner's at-risk amount, a partner guarantee (Item K3 checkbox) flips recourse allocation, and lower-tier partnership liabilities must be separately reported.
5. **Verify the remaining loss-limitation tiers (at-risk and passive)** — Basis is only the first gate. Work the at-risk (IRC 465) and passive-activity (IRC 469) tiers per `references/loss-limits-and-transactions.md`: aggregation/grouping checkboxes (page 1 Item K), activity-by-activity K-1 reporting, grouping consistency with prior year, and self-rental recharacterization. A loss can clear basis and still be non-deductible — and missing activity segregation makes every downstream partner return wrong.
6. **Verify capital accounts (Schedule L and K-1 Part II)** — Tie beginning capital account balances to prior-year K-1s. Verify contributions, distributions, and income/loss allocations for each partner. Confirm tax-basis capital uses the transactional approach with IRC 743(b) basis adjustments **excluded** — 743(b) embedded in tax capital is a pervasive software/legacy error that misstates the partner's capital every year thereafter.
7. **Check for special allocations and IRC 704(c)** — If the partnership agreement has special allocations, verify they are reflected in the K-1s. Reference IRC 704(b): special allocations must have substantial economic effect. If special allocations are present, flag that the economic effect test (or alternate test) should be documented. For property contributed with FMV ≠ basis, verify the 704(c) allocation method is identified and applied to depreciation/gain allocations, and that K-1 Item N (net unrecognized 704(c) gain/loss) is completed — a mandatory disclosure the IRS matches; see `references/loss-limits-and-transactions.md`.
8. **Verify distributions and interest transfers** — Test every distribution against the distributee's outside basis (IRC 731 gain, Form 7217 for property distributions, IRC 737, marketable securities as cash) and, for any transfer of a partnership interest, verify K-1 Item J changes are supported and Form 8308 is filed with the required IRC 751(a) detail. Procedures in `references/loss-limits-and-transactions.md` — these transactional events are invisible to the TB reconciliation and carry their own penalties.
9. **Verify Section 199A / QBI reporting** — The partnership reports QBI information on each K-1 (Box 20, code Z): QBI amount, W-2 wages (code W), UBIA of qualified property (code Z-2), and SSTB classification. Confirm:
   - QBI amount on each K-1 equals the partner's share of ordinary income/loss from Schedule K (line 1), adjusted for separately stated items excluded from QBI (e.g., Section 1231 gains, capital gains, guaranteed payments).
   - W-2 wage allocation (code W) is consistent with the partnership agreement and ownership percentages (or an alternative allocation method if documented).
   - UBIA of qualified property is reported (Box 20, code Z component) if the partnership has qualified property.
   - SSTB classification: if the partnership is a Specified Service Trade or Business (health, law, accounting, consulting, athletics, financial services, architecture, engineering, or any trade where the principal asset is reputation/skill), this must be disclosed on the K-1. The SSTB flag flows to each partner's 1040 for the 199A phase-out.
   - Guaranteed payments to partners are excluded from QBI — confirm they are not included in the Box 20 code Z QBI amount.
   - If the partnership had a loss for the year, confirm the QBI amount reflects the loss (negative QBI reduces each partner's overall QBI).
10. **Verify depreciation and R&E capitalization** — Tie Form 4562 to the fixed-asset schedule or trial-balance additions; depreciation is a book-tax difference the TB reconciliation alone can't validate. Two 2025 regime changes make software defaults unreliable:
   - **Split-rate bonus depreciation** — 40% for property acquired before January 20, 2025; 100% for property acquired and placed in service on or after that date (OBBBA). Confirm each significant addition uses the rate matching its **acquisition** date; a fixed-asset register that applies one rate to the whole year is a finding.
   - **Section 174/174A** — Domestic research costs are currently deductible for tax years beginning after 2024; foreign R&E remains capitalized over 15 years. Any catch-up deduction of previously capitalized domestic R&E must be supported by a Rev. Proc. 2025-28 transition election or Form 3115 — an M-1 that "ties" can still reflect an unauthorized method change.
   - Verify Section 179 amounts against the applicable year's limits and phase-out.
11. **Verify the Section 163(j) interest limitation** — If aggregate average annual gross receipts exceed the IRC 448(c) small-business threshold (inflation-adjusted; verify the applicable year's amount) or the partnership is a tax shelter under 448(d)(3), confirm Form 8990 is attached and the limitation computed. For tax years beginning after 2024, depreciation/amortization/depletion is **added back to ATI again** (OBBBA) — a computation carried forward on the 2024 EBIT basis understates the limit. Confirm excess business interest expense is allocated to partners on K-1 (code K) and prior-year disallowed-interest carryforwards tie to the prior return.
12. **Verify Schedules K-2/K-3 and foreign-partner withholding** — Confirm K-2/K-3 were filed, or the domestic filing exception is documented (no or limited foreign activity, all partners are eligible types, partners notified, and no partner requested a K-3 by the one-month date). Silence is not an exception — the failure-to-file penalty runs per partner, per month. If any partner is foreign, verify IRC 1446 withholding on effectively connected income was computed, paid, and reported on Forms 8804/8805/8813 — the withholding liability is the partnership's own, with entity-level penalties and interest.
13. **Verify state PTET (federal side)** — If a state pass-through entity tax election was made: confirm the election is valid for the year, the tax was **actually paid within the year** (deduction timing under Notice 2020-75 — accrued-but-unpaid PTET is a common mistimed deduction), the deduction is taken at the entity level on page 1 rather than passed through as a separately stated state tax, and partner-level credit information appears on K-1 footnotes or state schedules.
14. **Initial-return branch** — If the Initial Return box is checked (or this is otherwise year 1), run the first-year checks in `references/initial-return-checklist.md`: election statements attached, entity-classification posture, tax-year selection, BBA election status, beginning capital equal to initial contributions, and basis tracking initiated. First-year elections missed here are often permanent or costly to fix late.
15. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
16. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

- **K-1 total mismatch** — K-1 allocations must equal Schedule K totals. Any discrepancy is a hard stop: at least one partner's K-1 is wrong, and the error flows straight to that partner's return.
- **Capital account method** — Confirm whether capital accounts are reported on tax basis, GAAP, Section 704(b), or other. Flag if the method changed from prior year; a silent method change breaks the beginning-to-ending capital roll and can misstate every partner's balance.
- **Partner loss without basis** — A loss allocated to a partner without documented outside basis is a hard stop. Under IRC 704(d) the loss is suspended, so filing it as currently deductible overstates the partner's deduction.

## Red Flags

- K-1 percentages don't match the partnership agreement
- Capital account balances don't foot to the balance sheet
- Large guaranteed payment without a corresponding expense deduction
- Negative capital accounts without a deficit restoration obligation or qualified income offset
- 743(b) or 734(b) adjustments present but no supporting schedule
- Partner's share of loss exceeds outside basis — loss limitation applies under IRC 704(d)
- Liability allocations under IRC 752 not documented — affects outside basis for all partners
- Guaranteed payments: confirm deductibility and self-employment tax treatment
- Partnership has not elected out of centralized partnership audit regime (BBA/CPAR) under IRC 6221(b) — entity-level audit adjustments possible; confirm election status
- Cross-return coordination needed: K-1 amounts should tie to each partner's Form 1040 or entity return
- Digital-asset question answered "No" but a 1099-DA or crypto activity appears in the source documents
- Foreign tax paid, foreign accounts, or foreign partners visible in source docs — possible FinCEN 114 (FBAR) / foreign information-return exposure; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- 2025 fixed-asset additions straddling January 19 all claimed at a single bonus rate, or a catch-up R&E deduction with no Rev. Proc. 2025-28 election or Form 3115 in the file
- Interest expense deducted in full with no Form 8990 despite gross receipts above the IRC 448(c) threshold
- No Schedules K-2/K-3 and no documented domestic filing exception
- PTET deduction on page 1 with no evidence the tax was paid during the year
- A partner on payroll (W-2), or line 14a blank while general partners/active LLC members have ordinary income or guaranteed payments for services
- A distribution exceeding the distributee's outside basis with no IRC 731 gain reported, or a property distribution with no Form 7217
- K-1 Item J percentages changed from prior year with no Form 8308 and no transfer documentation
- Tax-basis capital accounts that include IRC 743(b) adjustments
- A foreign partner with no Forms 8804/8805 in the file
- Initial Return box checked but no election statements attached and no first-year review performed

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into sections:
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by dollar impact for preparer attention
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1065", client/Partnership name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
4. **Missing support** — Bulleted list of absent source documents
5. **Preparer questions** — Bulleted list of items requiring judgment
6. **Audit risk** — 1-3 bullet points, factual
7. **199A/QBI verification** — Summary of the QBI check results (K-1 Box 20 code Z, W-2 wages, UBIA, SSTB)

Save as `[ClientName]_[TaxYear]_1065_Review.docx` (e.g., `ABCLLP_2025_1065_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete if K-1 totals don't foot to Schedule K.
- Do not adjust capital accounts or basis without preparer review.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (PTET elections and payments, composite returns, nonresident-partner withholding, apportionment) to Preparer Questions rather than reviewing them here.
