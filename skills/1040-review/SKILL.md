---
name: 1040-review
version: 2.3.0
description: |
  Cross-reference a completed Form 1040 (individual income tax return) or an
  extension projection against its source documents — W-2s, 1099s, K-1s, brokerage
  statements, and supporting schedules — to confirm every income, deduction, credit,
  and withholding line ties back correctly and nothing was omitted or miscoded. This
  is the preparer/reviewer tie-out step. Use it whenever someone wants a 1040 checked
  before it is filed or before an extension payment is set, even when they don't name
  the form or the word "review": "does this individual return tie out", "did we miss
  any income", "second set of eyes on this 1040 before I sign", "is the extension
  payment reasonable", "self-review before e-file". Grades findings by severity and
  flags audit-risk items; supports both final-return review and extension-projection
  mode.
trigger: |
  "review the 1040", "check the individual return", "1040 cross-reference",
  "tie out the 1040", "tie out the individual return", "verify the individual return",
  "second review on the 1040", "self-review the 1040", "check the 1040 before filing",
  "review before I sign", "did we miss any income", "does the return tie out",
  "extension projection", "check the extension", "review the projection",
  "is the extension payment reasonable"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1040 Review: Individual Return Cross-Reference

## Purpose

Catch errors before a Form 1040 is filed or an extension payment is calculated. Verify that every line on the return ties to a source document and that no income, deduction, or credit has been omitted or misstated. The deliverable is a scannable dashboard of findings a reviewer can act on — not a narrated walk-through.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. Do not use a percentage of gross income, total assets, or net income to decide whether a variance is acceptable — that approach belongs in financial statement audits, not tax review, and here it would wave through a real omission just because it's small relative to the return.

Classify findings by severity (impact + risk), not by dollar-amount materiality:

- **HIGH** — Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM** — Documentation gaps, questionable-but-defensible positions needing support, items that could trigger correspondence
- **LOW** — Minor differences ($10–$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about or consider low-severity. Severity is for prioritization, not filtering — all findings go in the table. A separate preparer review step decides what to act on; your job at this stage is coverage, and a finding left out of the table is a finding no one gets to weigh.

## Required Inputs

- Completed Form 1040 (PDF or data export)
- All source documents: W-2s, 1099s (INT, DIV, B, R, SSA, MISC, NEC), K-1s, brokerage statements
- Any supporting workpapers or schedules
- Basis worksheets for pass-through entities (if losses are claimed)

## Workflow

Execute the phases below silently, then present the dashboard (Phase E). The detailed,
line-by-line tie-out mechanics and the special cases that most often trip up a 1040 live in
**`references/tie-out-procedures.md`** — read that file when you reach Phase D.

### Phase A — Determine review mode

Ask whether this is a **final return review** or an **extension projection review**. Projection mode changes what counts as an error:

- K-1s using SALY (same as last year) amounts are expected — flag as "pending actual K-1", not as errors.
- Not all 1099s may be final — note which documents are preliminary.
- The primary objective is verifying the extension payment amount is reasonable.
- Instead of a "do not mark review complete" hold, produce an **open items list for final return** tracking what must be resolved before filing.
- Focus the summary on: is the estimated balance due / overpayment / extension payment reasonable given available information?

### Phase B — Orient: two-year comparison and diagnostics

- **Two-Year Comparison** — Review the worksheet the tax software generates. Flag any line with a change greater than 25% or $10,000 for investigation; each significant variance should be explained by the end of the review. This surfaces the biggest questions early and focuses the rest of the review.
- **Diagnostics and overrides** — Read the software's Return Information / Diagnostics page and Input Override Report. Address each diagnostic by severity (QBI errors, missing income type codes, date issues). Document the reason for each input override. Wash sale overrides on capital gains worksheets are common and legitimate — before flagging one, check whether the override amount matches a wash sale disallowed amount on the corresponding 1099-B.

### Phase C — Inventory source documents

List all source docs provided. Flag any that appear missing based on the return (e.g., K-1 income on Schedule E with no K-1 provided). Two source-document situations look like errors but aren't (grantor-trust 1099s), and one looks fine but hides omitted income (unmapped consolidated-1099 sub-accounts) — both are detailed in `references/tie-out-procedures.md`.

### Phase D — Tie out every line

Work through each income, deduction, credit, withholding, and carryover category, tying each line to its source document. The per-category procedures and the special cases — structured-note/auto-call income to Form 8960, brokerage cash bonuses, the pass-through loss limitation stack (basis → at-risk → passive → QBI), cost-segregation rental losses, the SALT cap, carryover reconciliation — are in **`references/tie-out-procedures.md`**. Read it before starting this phase; the special cases are where returns quietly go wrong.

### Phase E — Dashboard summary

**Do not narrate the phases above.** Play-by-play ("checking wages… wages tie") buries the findings the reviewer actually needs. Present only the compact summary — something a reviewer can scan in under 60 seconds:

1. **Bottom line** (2-3 sentences): Is the return / extension payment reasonable? What is the single most important issue?
2. **Findings table** — one row per issue, no detail paragraphs:

   | # | Severity | Line / Schedule | Description | Amount |
   |---|----------|-----------------|-------------|--------|
   | 1 | HIGH | Sch E, Line 28 | K-1 loss with no basis worksheet | ($42,000) |
   | 2 | MEDIUM | Sch B | Sub-account 789 not mapped to 1099 | $3,200 |

3. **Audit risk** — 1-3 bullet points, factual (not a score or probability).
4. **Open items count** *(extension mode only)* — e.g., "4 items pending for final return (3 SALY K-1s, 1 preliminary 1099)."

**Do not list confirmed line items.** Lines that tie correctly are the expected case; listing them adds bulk without value. End the summary with: *"Expand any issue by number, say 'walk through all' to resolve one at a time, or ask for the full tie-out schedule."*

### Phase F — Interactive resolution

After the dashboard, the reviewer drives. For each item they raise:

- **Resolve** — reviewer provides an explanation or correction that clears the item
- **Defer** — move to the open items list for later follow-up
- **Escalate** — flag for partner review

When expanding an issue, show the full detail block:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Track which items are resolved vs. still open, and update the findings table as items clear.

## Control Points

Stop and get a human decision before treating the review as done when:

- **Any discrepancy beyond rounding remains** — Every variance beyond the $10 rounding tolerance requires preparer review and correction before filing.
- **Source documents are missing** — Do not mark the review complete if source docs are missing for reported income; income you can't tie to a document is income you can't confirm.
- **A pass-through loss is claimed without basis** — A loss with no basis worksheet is a hard stop; the loss may not be deductible, so it needs documentation before the review continues.
- **Extension projection mode** — Produce an open items list rather than blocking completion. The list tracks what must be resolved before the final return is filed.

## Red Flags

Pause and surface to the reviewer when:

- Reported income doesn't match any source document on file
- K-1 shows a large loss but no basis worksheet is present
- Withholding on the return exceeds withholding on source documents
- Prior-year carryforwards are present but no supporting schedule is
- QBI deduction taken without a supporting computation
- Pass-through loss claimed without basis documentation or Form 6198
- Passive loss allowed without Form 8582 or evidence of material participation
- QBI deduction taken on SSTB income above threshold without phase-out calculation
- Large ISO exercise, accelerated depreciation, or preference items present — verify Form 6251 is present and the AMT computation is correct
- Cross-return coordination needed: K-1 amounts from a related 1120-S, 1065, or 1041 should tie to the issuing entity's return
- Large rental loss driven by cost segregation — verify RE pro status and bonus depreciation rate
- Software diagnostics unresolved or input overrides undocumented
- Consolidated 1099 sub-accounts not individually mapped to the return
- Significant Two-Year Comparison variances unexplained

## Output Format

**Default output is the dashboard summary** (Phase E) — a compact table plus bottom line. The full detail block for each issue appears only when the reviewer expands it (Phase F). The dashboard groups findings into:

- **Issues** — Severity-graded (HIGH / MEDIUM / LOW), ranked by dollar impact
- **Missing Support** — Source docs absent
- **Preparer Questions** — Items requiring judgment or additional facts
- **Audit Risk** — 1-3 bullet points
- **Open Items for Final Return** *(extension projection mode only)* — SALY K-1s, preliminary documents, items pending for final filing

Confirmed line items are **not listed by default**. Request "full tie-out schedule" to see them.

### Excel / Workpaper Output

When producing an Excel workpaper (extension payment summary, tax computation, reconciliation, etc.), **all computed cells must use Excel formulas, not hard-coded values** — a hard-coded total can't be traced or re-run, which defeats the point of a workpaper:

- **Totals**: `=SUM(range)` — never type a static total
- **Balance due / overpayment**: `=tax_cell - payments_cell` (e.g., `=B12-B18`)
- **Effective rates, differences, variances**: formulas referencing source cells
- **Subtotals feeding into grand totals**: `=SUM()` of detail rows, not of subtotal rows (avoid double-counting)

The reviewer needs to see the math tie by formula and to adjust an input and watch the result update.

## Safety Constraints

- Do not mark the return as reviewed-complete while any discrepancies beyond rounding, or any missing documents, remain.
- Do not draft a response to an IRS notice based on this review without preparer confirmation.
- Do not characterize audit risk as a probability or percentage. Judgment on acceptable risk levels belongs to the signing partner.
- Do not hardcode SALT caps, bonus depreciation rates, or other amounts that change by tax year — always reference the applicable year's statutory amount.
