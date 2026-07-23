---
name: 1065-review
version: 1.6.0
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
- Any supporting workpapers

## Workflow

Before starting, confirm the required inputs are present. A review run against a missing K-1 or an absent partnership agreement produces false "confirmed" items and misses real allocation errors — surface what's missing rather than reviewing around the gap.

1. **Reconcile income and deductions to trial balance** — Tie Schedule K ordinary income/loss through M-1. Flag unexplained book-to-tax adjustments.
2. **Verify Schedule K items** — Check each separately stated item against source (interest, dividends, Section 1231, QBI, credits, etc.).
3. **Verify K-1 allocations** — Confirm K-1 totals for all partners sum to Schedule K. Verify percentages tie to the partnership agreement or are consistent with prior year.
4. **Verify partner outside basis** — For each partner receiving a loss, confirm outside basis is sufficient. Outside basis = capital account (tax basis) + share of liabilities. If liabilities are allocated under IRC 752, check that recourse/nonrecourse allocation is consistent with the partnership agreement. Flag losses exceeding basis — these are suspended under IRC 704(d).
5. **Verify capital accounts (Schedule L and K-1 Part II)** — Tie beginning capital account balances to prior-year K-1s. Verify contributions, distributions, and income/loss allocations for each partner.
6. **Check for special allocations** — If the partnership agreement has special allocations, verify they are reflected in the K-1s. Reference IRC 704(b): special allocations must have substantial economic effect. If special allocations are present, flag that the economic effect test (or alternate test) should be documented.
7. **Verify Section 199A / QBI reporting** — The partnership reports QBI information on each K-1 (Box 20, code Z): QBI amount, W-2 wages (code W), UBIA of qualified property (code Z-2), and SSTB classification. Confirm:
   - QBI amount on each K-1 equals the partner's share of ordinary income/loss from Schedule K (line 1), adjusted for separately stated items excluded from QBI (e.g., Section 1231 gains, capital gains, guaranteed payments).
   - W-2 wage allocation (code W) is consistent with the partnership agreement and ownership percentages (or an alternative allocation method if documented).
   - UBIA of qualified property is reported (Box 20, code Z component) if the partnership has qualified property.
   - SSTB classification: if the partnership is a Specified Service Trade or Business (health, law, accounting, consulting, athletics, financial services, architecture, engineering, or any trade where the principal asset is reputation/skill), this must be disclosed on the K-1. The SSTB flag flows to each partner's 1040 for the 199A phase-out.
   - Guaranteed payments to partners are excluded from QBI — confirm they are not included in the Box 20 code Z QBI amount.
   - If the partnership had a loss for the year, confirm the QBI amount reflects the loss (negative QBI reduces each partner's overall QBI).
8. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
9. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

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
