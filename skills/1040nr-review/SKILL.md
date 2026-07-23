---
name: 1040nr-review
version: 1.0.0
description: |
  Cross-reference a completed Form 1040-NR (nonresident alien income tax return),
  dual-status return, or first/final-year resident return against source documents —
  the residency day-count workpaper, visa/immigration documents, Forms W-2, 1042-S,
  8805, 8288-A, and treaty position support — to catch errors before filing. Verifies
  the residency determination is documented and consistent with the return type filed,
  ECI vs. FDAP characterization and the Schedule NEC rate applied, treaty positions and
  Form 8833 disclosure, withholding credits tied to 1042-S/8805/8288-A, Schedule OI
  completeness, and required companion filings (8843, 8840, 8938, 3520). Use whenever a
  nonresident or foreign-national return needs a second set of eyes — "review the
  1040-NR", "check the nonresident return", "does the treaty rate look right", "review
  the dual-status return" — even if they don't say "NRA" or "review".
trigger: |
  "review the 1040-NR", "1040-NR review", "nonresident return review",
  "foreign national return", "NRA return", "check the nonresident return",
  "dual-status return", "review the dual status", "1040-NR cross-reference",
  "substantial presence", "check the treaty position", "does the treaty rate look right",
  "Schedule NEC", "1042-S reconciliation", "closer connection"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1040-NR Review: Foreign National Return Cross-Reference

## Purpose

Catch errors before a Form 1040-NR (or dual-status return) is filed. Foreign-national returns fail differently than domestic 1040s: the highest-stakes question is *upstream* of every line — whether the taxpayer is a resident or nonresident at all, and for which part of the year. A return can tie perfectly to its source documents and still be the wrong return. So this review verifies two layers: (1) the residency determination is documented, and the return type filed matches it; (2) the return itself ties to source documents, with income characterized under the right regime (graduated rates on effectively connected income vs. flat 30%/treaty rate on FDAP).

The deliverable is a severity-graded findings report for a professional preparer. Residency conclusions, election choices, and treaty positions are verified against the file — this skill checks that they are *documented and internally consistent*, not whether they are the *right* call; that judgment belongs to the preparer and signing partner, with substantive research handed to `tax-advisor`.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross income to decide whether a variance is acceptable — foreign information-return penalties in this area start at five figures per form regardless of the income on the return.

Classify findings by severity (impact + risk), not by dollar-amount materiality:

- **HIGH** — Wrong return type for the documented residency status, undocumented residency determination (no day counts), income taxed under the wrong regime (ECI vs. FDAP), treaty rate applied with no treaty article identified or no Form 8833 where required, withholding credits that don't tie to 1042-S/8805/8288-A, missing required companion filings (8843, 8938, 3520, 5471/8621 triggers), missing forms
- **MEDIUM** — Documentation gaps (day counts asserted but not supported, visa history incomplete), defensible-but-thin positions, Schedule OI items answered inconsistently with the facts, items that could draw IRS correspondence
- **LOW** — Minor rounding, presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about. Severity ranks the list; it does not filter it. Coverage is the job at this stage — the preparer decides what to act on.

## Required Inputs

- Completed Form 1040-NR (or dual-status package) with all schedules (A, NEC, OI) and attachments
- Residency workpaper: day counts in the U.S. for the current and two prior years, visa type and history, green-card status
- Visa/immigration documents (or the foreign national organizer capturing them)
- Income documents: W-2s, Forms 1042-S, 8805 (partnership §1446 withholding), 8288-A (FIRPTA withholding), 1099s, foreign employer statements
- Treaty position support: the treaty article relied on, and Form 8833 if attached
- Prior-year return (residency status continuity, carryovers, prior elections — 6013(g)/(h), §871(d) net election, QEF elections)
- CCH Axcess Diagnostics report and Input Override Report (if available)

If a required input is missing, say so before starting rather than reviewing around the gap. A 1040-NR review without the day-count workpaper cannot verify the single most consequential item on the return — that finding would be a guess.

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

1. **Verify the residency determination and return type** — This gates everything else.
   - Confirm the substantial presence test is documented: current-year days + 1/3 prior-year days + 1/9 second-prior-year days, with the day counts tied to the organizer or travel records, not asserted.
   - Confirm exempt-individual days are handled: F, J, M, Q visa holders exclude days (students: five calendar years; teachers/trainees: the 2-of-6-year rule) and **Form 8843 must be attached** to support excluded days.
   - If substantial presence is met but nonresident status is claimed: confirm the **closer connection exception (Form 8840)** is attached and the taxpayer was present fewer than 183 days in the current year, or a **treaty tie-breaker** position is taken with Form 8833 disclosure per Regs. §301.7701(b)-7.
   - If green-card test applies, nonresident filing is only supportable via treaty tie-breaker — confirm the disclosure and flag the §7701(b)(6) long-term-resident/expatriation implications to the preparer.
   - First or final residency year: confirm the residency start/end date logic (including the §7701(b)(2)(C) 10-day de minimis rule and the no-lapse rule), and that a **dual-status return** is assembled correctly — the correct form as the return, the other as the statement, with dual-status restrictions applied (no standard deduction, no joint return absent an election, limited credits).
   - Elections: if a §6013(g)/(h) full-year or joint election, or a §7701(b) first-year election, is relied on, confirm the election statement is attached and its requirements (extension timing for §7701(b), both spouses' signatures for §6013) are met.
2. **Verify income scoping and sourcing** — Nonresidents are taxed on U.S.-source and effectively connected income only; residents (and full-year-election filers) on worldwide income. Confirm the income on (or off) the return matches the documented status: wages sourced under Regs. §1.861-4(b) (workday allocation for split-year or cross-border commuters), stock option sourcing over the grant-to-vest period, and — for resident-period or election filers — that worldwide income was actually requested and included, with §911 exclusion mechanics verified if claimed.
3. **Verify ECI vs. FDAP characterization** — Every income item lands in one of two regimes; misclassification changes the rate and the return page.
   - ECI (wages, business income, §871(d)-elected rental income): graduated rates, page 1.
   - FDAP (dividends, interest, royalties, rents without the net election, pensions): **Schedule NEC** at 30% or the treaty rate — confirm the rate column matches the treaty article claimed and the treaty country matches the taxpayer's residence.
   - U.S. rental real estate: if reported net of expenses, confirm the **§871(d) net election** (or Regs. §1.871-10(d)(1)(ii) statement) is in the file — current year or carried forward from a prior year; net reporting without the election is a HIGH finding.
   - U.S. real property sales: FIRPTA — gain reported as ECI, and the Form 8288-A withholding credit tied to the stamped copy.
4. **Verify Schedule OI** — Every question answered and consistent with the rest of the file: country of residence, visa type and changes, days present by year (must match the residency workpaper), treaty benefits claimed (country, article, amount — must match Schedule NEC and any 8833), prior-year treaty claims.
5. **Verify withholding and payments tie-out** — Tie every withholding credit to its source form: W-2 Box 2, **1042-S** (by income code; confirm gross income on the 1042-S is also on the return), **8805**, **8288-A**, 1099 backup withholding. Withholding claimed with no supporting form is a HIGH finding; a 1042-S in the file with no corresponding return entry is omitted income. Confirm estimated payments and the correct filing deadline (April 15 with U.S. wages subject to withholding; June 15 otherwise; automatic 2-month extension for taxpayers abroad under §6081).
6. **Verify deductions, exemptions, and credits under NRA limits** — No standard deduction (except students/business apprentices from India by treaty); itemized deductions limited (state income taxes, charitable to U.S. organizations, casualty); dependents claimable only in narrow cases (residents of Canada/Mexico, treaty). Confirm nothing flowed in from domestic-1040 software defaults. Check SE tax: if self-employment income exists, confirm residency-for-SE-tax under any applicable **totalization agreement** and a certificate of coverage if exemption is claimed.
7. **Companion-filing sweep** — Confirm the required attachments and separate filings are present or documented as N/A: Form 8843 (exempt individuals), 8840 (closer connection), 8833 (treaty positions, including where required by Regs. §301.7701(b)-7), 8938 (specified foreign assets — applies to resident and election filers), FinCEN 114 (residents under substantial presence are U.S. persons for FBAR; hand the workpaper to `fbar-workpaper`), 3520 (foreign gifts/bequests/trust distributions), 5471/8621/8865/8858/926 triggers (foreign entities, PFICs — flag and hand analysis to `tax-advisor`), W-7 ITIN applications for family members, Form 8288/8804-C withholding-side obligations.
8. **Verify the tax computation** — Page 1 tax at graduated rates on ECI + Schedule NEC tax at the stated rates + any §1446/FIRPTA reconciliation; NIIT does not apply to nonresidents — Form 8960 on an NRA return is a finding; AMT and the Canada MFS AMT-credit trap flagged where present.
9. **Summarize findings** — Produce the severity-graded report (see Output Format).
10. **Audit risk assessment** — Note 1–3 items presenting elevated audit risk, stated as facts: "This item may draw scrutiny because [specific reason]." Note the six-year statute for substantial omissions (§6501(e)) where income scoping is thin.

## Control Points

Stop and get a human decision — these are judgment calls or hard stops, not mechanical checks:

- **Residency status unsupported** — No day-count workpaper, or day counts that contradict the return type filed, is a hard stop. Do not review the rest of the return as if the status were established.
- **Treaty position without identified authority** — A treaty rate or tie-breaker claim with no treaty article identified (or a missing Form 8833 where disclosure is required) goes to the preparer; the $1,000 §6712 penalty and the position itself are their call. Substantive treaty analysis → `tax-advisor`.
- **Election decisions** — §6013(g)/(h), §7701(b) first-year, and §871(d) net elections are client planning decisions with multi-year consequences. Verify documentation; never resolve the choice silently.
- **Expatriation indicators** — Green-card holder for 8 of the last 15 years surrendering status, or §877A covered-expatriate facts: flag immediately and route to the preparer and `tax-advisor`; exit-tax analysis is out of scope for this review.
- **Missing companion filing with penalty exposure** (8938, 3520, 5471, 8621) — Hard stop until the preparer confirms filing, documented N/A, or accepted exposure.

## Red Flags

Pause and surface to the reviewer when:

- The return type doesn't match the day counts (1040-NR filed but substantial presence met with no 8840/treaty tie-breaker; or a 1040 filed with no green card and no substantial presence)
- Form 8843 days excluded for an F/J visa holder past the five-year (or 2-of-6) window
- Schedule NEC uses a treaty rate but Schedule OI names no treaty country or a different one
- Rental real estate reported net with no §871(d) election in the file
- A 1042-S or 8805 in the file with no corresponding income or withholding entry on the return
- Standard deduction taken (non-India-treaty), or dependents claimed outside the Canada/Mexico/treaty exceptions — domestic software defaults leaking through
- Worldwide income not requested for a resident-period or §6013 election filer
- Foreign mutual funds or pooled investments on statements — PFIC/Form 8621 exposure; hand to `tax-advisor`
- Gifts or bequests from foreign persons above the Form 3520 reporting threshold with no 3520 in the file
- U.S. real property or ≥10% U.S. business ownership — BEA survey registration (BE-10/BE-11 family) unaddressed
- Dual-status return allows a credit or deduction barred in dual-status years, or a joint return with no §6013 election statement
- State filing posture assumes the federal treaty position applies — many states do not conform; route to Preparer Questions

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., treaty article, or procedure if applicable]
```

Organized into sections:
- **Residency Determination Verified** — Status, test applied, day counts, elections — with the support cited
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by consequence for preparer attention
- **Missing Support** — Source docs absent (day counts, visa history, 1042-S, election statements, treaty authority)
- **Companion Filings** — Status of each required attachment/separate filing (8843, 8840, 8833, 8938, FBAR, 3520, 5471/8621) — present / N/A documented / open
- **Preparer Questions** — Items requiring judgment or client facts
- **Audit Risk Items** — 1–3 items with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1040-NR" (or "Dual-Status Return"), client name, tax year, preparer name, review date
2. **Residency determination** — Status, test, day counts, elections, and support
3. **Bottom line** — 2-3 sentence summary
4. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
5. **Companion filings status** — Table: form, requirement trigger, status
6. **Missing support** — Bulleted list of absent source documents
7. **Preparer questions** — Bulleted list of items requiring judgment
8. **Audit risk** — 1-3 bullet points, factual

Save as `[ClientName]_[TaxYear]_1040NR_Review.docx` (e.g., `Tanaka_2025_1040NR_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Handoffs

- **Substantive treaty analysis** (tie-breaker outcomes, article interpretation, competent-authority questions), **PFIC regime choices** (QEF/deemed-sale/retroactive elections), and **expatriation/exit-tax analysis** → `tax-advisor`
- **FBAR workpaper** for taxpayers who are U.S. persons for the year → `fbar-workpaper`
- **Client-facing explanation** of residency status or election trade-offs → `tax-memo` or `client-email`

## Safety Constraints

- Do not conclude residency status yourself where the day counts or visa history are missing — state the dependency and stop; a review built on an assumed status is worse than no review.
- Do not opine on whether a treaty position is correct — verify it is identified, disclosed, and internally consistent; the position belongs to the preparer and signing partner.
- Do not resolve election decisions (§6013(g)/(h), §7701(b), §871(d)) — present the documentation status and consequences; the client and preparer own the choice.
- Do not characterize audit risk as a probability or percentage. Judgment on acceptable risk belongs to the signing partner.
- Do not hardcode thresholds or amounts that change by tax year (§911 exclusion, Form 8938 thresholds, gift-reporting thresholds) — reference the applicable year's figures.
- This review covers the **federal return only**. State the scope limit in the deliverable, and route state items (treaty non-conformity, state residency divergence, state credit for foreign taxes) to Preparer Questions rather than reviewing them here.
