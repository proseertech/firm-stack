---
name: 1120s-review
version: 1.11.0
description: |
  Cross-reference a completed Form 1120-S (S-corporation return) against its source
  documents — trial balance, Schedule K-1s, officer W-2s, Form 1125-E, and supporting
  schedules — to catch errors before filing. Verifies the S election is valid and
  undisturbed (shareholder eligibility, second class of stock via non-pro-rata
  distributions), income, deductions, credits, and shareholder allocations, checks that
  K-1s foot to Schedule K, and flags audit-risk items including reasonable-compensation
  exposure. Includes a first-year initial-return branch (2553 acceptance, election
  statements, basis initiation). Use this whenever someone hands you a drafted
  or finished S-corp return and wants it checked, tied out, or reviewed against the books —
  "review the 1120-S", "does the S-corp return tie to the TB", "check the K-1 allocations",
  "second set of eyes on this S-corp before we file" — even if they don't name the form or
  say the word "review."
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

## Accuracy Standard

A tax return must be substantially correct, so the bar here is different from a financial-statement audit — there is no percentage materiality. Do not use a percentage of gross receipts, total assets, or net income to decide whether a variance is acceptable; that test belongs to audit engagements, not tax review.

The only tolerance is rounding: differences of $10 or less are expected (consistent with IRS whole-dollar rounding and normal software behavior). Every discrepancy beyond that is a finding.

Grade findings by severity — impact plus risk, not dollar size:

- **HIGH** — Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM** — Documentation gaps, defensible-but-thin positions, items that could draw IRS correspondence
- **LOW** — Minor rounding ($10–$100 range), presentation preferences, informational items

Report *every* discrepancy outside the rounding tolerance, including low-severity or uncertain ones. Severity ranks the list; it does not filter it. Filtering understates coverage, and the item you drop as "probably fine" is the one that surfaces after filing. A separate preparer review decides what to act on — your job here is complete coverage.

## Required Inputs

- Completed Form 1120-S and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Officer W-2s and Form 1125-E
- Distribution detail by shareholder and date
- K-1s received from any partnership or LLC in which the corporation is a partner
- Form 2553 acceptance letter (first-year returns or new clients)
- Prior-year return (for AAA balance, basis, and carryforwards)
- Shareholder basis worksheets (if losses flow through)
- Any supporting workpapers
- CCH Axcess Diagnostics report and Input Override Report (if available)

If a required input is missing, say so before starting rather than reviewing around the gap — a review that silently skips the basis worksheet or the prior-year return gives false assurance.

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

1. **Verify the S election and continuing eligibility** — Confirm the S election is in effect (Form 2553 accepted; for a first-year return or new client, sight the IRS acceptance letter — see the initial-return branch in step 2). Screen for termination events: more than 100 shareholders; any ineligible shareholder (nonresident aliens, partnerships, corporations — trusts only if QSST, ESBT, or grantor); and a second class of stock. **Compare the distribution detail to ownership percentages** — non-pro-rata distributions are the classic inadvertent second-class-of-stock trap; the return can look clean while the election is silently at risk. If the election is invalid or terminated, every downstream check is moot — stop and route to the preparer.
2. **Initial-return branch** *(first-year returns only)* — When the Initial Return box is checked or this is year 1:
   - Form 2553 acceptance letter sighted and the effective date matches the return year; if the election was late, confirm the Rev. Proc. 2013-30 late-election relief statement is attached.
   - First-year election statements attached where applicable: overall accounting method, IRC 195/248 startup and organizational costs, de minimis safe harbor.
   - Accounting method is consistent with the corporation's IRC 448(c) gross-receipts status.
   - Stock and debt basis schedules (Form 7203 support) initiated from actual initial contributions — basis tracking that starts wrong stays wrong every year after.
   - No carryover balances: beginning AAA, retained earnings, and carryforwards start at zero unless assets came from a predecessor entity.
   - State S election filed where the state requires its own — route to Preparer Questions.
3. **Reconcile income and deductions to the trial balance** — Tie Schedule K ordinary income/loss to the book-to-tax reconciliation (M-1). Flag unexplained M-1 adjustments. Check accrued expenses payable to cash-basis shareholders (bonuses, rent, interest) — under IRC 267(a)(2) they are not deductible until paid, and year-end shareholder accruals that survived into the deduction are a routine review catch.
4. **Verify officer compensation and shareholder fringes** — Confirm officer wages on Form 1125-E tie to the W-2s. Compare officer compensation to distributions: if distributions materially exceed compensation, flag the reasonable-compensation issue. This is a well-known S-corp audit trigger — recharacterization as wages carries FICA employment-tax exposure under IRC 3111/3121, per the *David E. Watson, P.C.* line of cases. Then check W-2 **composition**, not just totals: health insurance premiums for >2% shareholders belong in W-2 Box 1 (not Social Security/Medicare wages) with a matching corporate deduction — missing Box 1 treatment costs the shareholder the self-employed health insurance deduction at the 1040 level. Treat other >2% shareholder fringes the same way. If an ERC refund was received (or a claim denied) during the year, confirm the wage-deduction reduction was handled for the credit year.
5. **Verify Schedule K items** — Check each separately stated item (interest, dividends, Section 1231, credits, etc.) against source. Then run the check in reverse: scan page 1 ordinary income for items that must be separately stated — tax-exempt interest, portfolio income, Section 1231 gains, COD income, charitable contributions — wrong character survives a tie-out that only looks at what already made it to Schedule K. Rental activities belong on Form 8825 / Schedule K line 2, not netted into page 1. If the corporation holds partnership or LLC interests, tie the incoming K-1 amounts into Schedule K — pass-through income won't sit in the trial balance the way the reviewer expects and is easy to drop. Confirm the digital-asset question on page 1 is answered and consistent with the source documents — a 1099-DA or crypto activity on custody statements with a "No" answer is a finding. Reconcile any Forms 1099-DA (broker reporting is new; basis may be missing or wrong).
6. **Verify K-1 allocations** — Confirm each shareholder's K-1 totals sum to Schedule K. Verify ownership percentages against the shareholder agreement or prior-year return. Items are allocated **per share, per day** — if ownership changed mid-year, static year-end percentages produce wrong K-1s that still foot: confirm the pro-rata daily allocation, or the IRC 1377(a)(2) closing-of-the-books election statement if the parties chose it, and check distribution ordering around the change.
7. **Verify shareholder basis** — For each shareholder taking a loss, check that the K-1 loss does not exceed stock plus debt basis. Cross-reference the basis worksheet if provided; if a loss flows through and no worksheet exists, flag it as requiring basis documentation. Debt basis counts only **bona fide debt running directly from the shareholder to the corporation** — guarantees of third-party loans, back-to-back arrangements, and related-entity loans don't create basis; if debt basis supports a loss, confirm the note and payment history exist.
8. **Verify the balance sheet (Schedule L)** — Tie beginning and ending balances to the prior-year return and current trial balance. Flag unexplained changes.
9. **Verify AAA, OAA, and M-2** — Confirm the AAA beginning balance ties to the prior-year return, and that current-year movements are correctly reflected. Verify the M-2 columns are properly segregated: tax-exempt income and its related nondeductible expenses go to OAA, not AAA, and any PTI column is preserved — tax-exempt income posted to AAA distorts the taxability of future distributions.
10. **Check former-C-corporation exposure** — If the corporation was ever a C corporation (or acquired assets with C-corp basis, IRC 1374(d)(8)):
    - **Built-in gains tax** — dispositions of assets held at the election date within the recognition period trigger entity-level tax under IRC 1374; confirm a BIG analysis exists before clearing asset sales.
    - **C-corp E&P** — distribution ordering applies (AAA first, then E&P as taxable dividends requiring Forms 1099-DIV); distributions exceeding AAA with E&P present and no 1099-DIV is a finding.
    - **Excess passive income** — passive investment income over 25% of gross receipts with E&P present triggers the IRC 1375 tax, and three consecutive years terminates the election.
11. **Verify Section 199A / QBI reporting** — The S-corp reports QBI information on each K-1 (Box 17, codes V through AC): QBI amount, W-2 wages (code W), and UBIA of qualified property (code AC). Confirm:
   - QBI amount on each K-1 equals the shareholder's share of ordinary income/loss from Schedule K (line 1), adjusted for separately stated income/gains that are excluded from QBI (e.g., Section 1231 gains, capital gains).
   - W-2 wage amount (code W) is correctly allocated among shareholders per ownership percentage (or an alternative method if documented).
   - UBIA of qualified property (code AC) is reported if the entity has qualified property.
   - SSTB classification: if the S-corp is a Specified Service Trade or Business, this must be disclosed on the K-1. The SSTB flag flows to the shareholder's 1040 for the 199A phase-out calculation. An incorrect SSTB classification can overstate or understate the shareholder's QBI deduction.
   - If the S-corp had a loss for the year, confirm the QBI amount on the K-1 reflects the loss (negative QBI reduces the shareholder's overall QBI).
12. **Verify depreciation and R&E capitalization** — Tie Form 4562 to the fixed-asset schedule or trial-balance additions; depreciation is a book-tax difference the M-1 reconciliation alone can't validate. Two 2025 regime changes make software defaults unreliable:
   - **Split-rate bonus depreciation** — 40% for property acquired before January 20, 2025; 100% for property acquired and placed in service on or after that date (OBBBA). Confirm each significant addition uses the rate matching its **acquisition** date.
   - **Section 174/174A** — Domestic research costs are currently deductible for tax years beginning after 2024; foreign R&E remains capitalized over 15 years. Any catch-up deduction of previously capitalized domestic R&E must be supported by a Rev. Proc. 2025-28 transition election or Form 3115.
   - Verify Section 179 amounts against the applicable year's limits and phase-out.
13. **Verify the Section 163(j) interest limitation** — If aggregate average annual gross receipts exceed the IRC 448(c) small-business threshold (inflation-adjusted; verify the applicable year's amount) or the corporation is a tax shelter under 448(d)(3), confirm Form 8990 is attached and the limitation computed. For tax years beginning after 2024, depreciation/amortization/depletion is **added back to ATI again** (OBBBA). Separately, confirm gross receipts are reported on each K-1 (code AC) — shareholders need it for their own 163(j) tests, and it is frequently omitted.
14. **Verify Schedules K-2/K-3** — Confirm K-2/K-3 were filed, or the domestic filing exception is documented (no or limited foreign activity, shareholders notified, and no shareholder requested a K-3 by the one-month date). Silence is not an exception — the failure-to-file penalty runs per shareholder, per month.
15. **Verify state PTET (federal side)** — If a state pass-through entity tax election was made: confirm the election is valid for the year, the tax was **actually paid within the year** (deduction timing under Notice 2020-75 — accrued-but-unpaid PTET is a common mistimed deduction), the deduction is taken at the entity level rather than passed through as a separately stated state tax, shareholder-level credit information appears on K-1 footnotes or state schedules, and the AAA/OAA impact is booked correctly (including ordering interactions where C-corp E&P exists).
16. **Summarize findings** — Produce the severity-graded report (see Output Format).
17. **Assess audit risk** — Note 1–3 items presenting elevated audit risk, stated as facts: "This item may draw scrutiny because [specific reason]."

## Control Points

Stop for a preparer decision — don't quietly reconcile past these:

- **S election invalid or terminated** — An ineligible shareholder, a second class of stock, or a defective/missing election means the entity-level classification is wrong and every downstream check is moot. Hard stop; route to the preparer before reviewing further.
- **K-1 totals don't foot to Schedule K** — Allocations must equal the Schedule K totals. Any discrepancy is a hard stop; a return where the K-1s don't sum is not fileable.
- **Any discrepancy beyond rounding** — Every variance beyond the $10 rounding tolerance needs preparer review and correction before filing.
- **Shareholder loss without basis** — A loss flowing through without a basis worksheet is a hard stop; without basis substantiation the loss may be non-deductible.

## Red Flags

Pause and surface to the user when:

- Ordinary income/loss doesn't reconcile to the trial balance within a small rounding amount
- K-1 percentages don't match the shareholder agreement
- AAA goes below zero without a corresponding distribution-in-excess-of-basis being flagged
- Officer compensation appears unreasonably low relative to S-corp income
- Distributions to shareholders significantly exceed officer W-2 wages — reasonable-compensation risk
- Shareholder loss exceeds stock plus debt basis without a supporting basis schedule
- Prior-year credits or carryforwards appear with no schedule supporting the amount
- Cross-return coordination needed — K-1 amounts should tie to each shareholder's Form 1040, Schedule E
- Digital-asset question answered "No" but a 1099-DA or crypto activity appears in the source documents
- Foreign tax paid, foreign accounts, or foreign subsidiaries/interests visible in source docs — possible FinCEN 114 (FBAR) / foreign information-return exposure; flag as a preparer question and hand the FBAR workpaper itself to `fbar-workpaper`
- 2025 fixed-asset additions straddling January 19 all claimed at a single bonus rate, or a catch-up R&E deduction with no Rev. Proc. 2025-28 election or Form 3115 in the file
- Interest expense deducted in full with no Form 8990 despite gross receipts above the IRC 448(c) threshold, or K-1s missing the code AC gross-receipts amount
- No Schedules K-2/K-3 and no documented domestic filing exception
- PTET deduction with no evidence the tax was paid during the year, or PTET payments not reflected in AAA
- Distributions not proportionate to stock ownership — second-class-of-stock / inadvertent-termination risk
- >2% shareholder health premiums deducted by the corporation but absent from W-2 Box 1
- Mid-year stock transfer with K-1s allocated on static year-end percentages and no IRC 1377(a)(2) statement
- Former C corp: election-date assets sold with no built-in-gains analysis, or distributions beyond AAA with E&P present and no 1099-DIV issued
- ERC refund received with no corresponding wage-deduction adjustment
- Tax-exempt interest, portfolio income, or Section 1231 items buried in page 1 ordinary income

## Output Format

A structured findings report. Each issue reads:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into:

- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked within severity by dollar impact for preparer attention
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1–3 items with a factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1120-S", client/S-Corp name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
4. **Missing support** — Bulleted list of absent source documents
5. **Preparer questions** — Bulleted list of items requiring judgment
6. **Audit risk** — 1-3 bullet points, factual
7. **199A/QBI verification** — Summary of the QBI check results (K-1 Box 17 codes V–AC, W-2 wage allocation, SSTB classification, loss QBI)

Save as `[ClientName]_[TaxYear]_1120S_Review.docx` (e.g., `ABCCorp_2025_1120S_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete while K-1 totals don't foot to Schedule K — the return isn't fileable and "complete" would be misleading.
- Do not adjust AAA or basis yourself — surface the issue for preparer review; those balances drive shareholder-level tax and are the preparer's call.
- Do not express audit risk as a probability or percentage. State the factual reason an item may draw scrutiny; judging acceptable risk is the signing partner's decision.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items surfaced during the review (PTET elections and payments, composite returns, nonresident-shareholder withholding, apportionment) to Preparer Questions rather than reviewing them here.
