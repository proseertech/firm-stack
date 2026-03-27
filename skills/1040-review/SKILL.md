---
name: 1040-review
version: 1.0.0
description: |
  Cross-reference a completed Form 1040 (individual income tax return) against
  source documents — W-2s, 1099s, K-1s, brokerage statements, and supporting
  schedules — to verify every income, deduction, credit, and withholding line
  ties back correctly.
trigger: |
  "review the 1040", "check the individual return", "1040 cross-reference",
  "tie out the 1040", "verify the individual return"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1040 Review: Individual Return Cross-Reference

## Purpose

Catch errors before a Form 1040 is filed. Verify that every material line on the return ties to a source document and that no income, deduction, or credit has been omitted or misstated.

## Required Inputs

- Completed Form 1040 (PDF or data export)
- All source documents: W-2s, 1099s (INT, DIV, B, R, SSA, MISC, NEC), K-1s, brokerage statements
- Any supporting workpapers or schedules

## Workflow

1. **Inventory source documents** — List all source docs provided. Flag any that appear to be missing based on the return (e.g., K-1 income on Schedule E with no K-1 provided).
2. **Verify wages and compensation** — Tie W-2 Box 1 wages to Line 1a. Check Box 12 codes for deferred comp, HSA, etc.
3. **Verify investment income** — Tie 1099-INT, 1099-DIV, and Schedule B. Verify 1099-B transactions on Schedule D / Form 8949.
4. **Verify retirement income** — Tie 1099-R distributions to Line 4 or 5. Verify taxable amount and any rollover exclusions.
5. **Verify pass-through income** — Tie each K-1 to the appropriate schedule (E, F, etc.). Verify basis limitations, at-risk rules, passive activity rules flagged where applicable.
6. **Verify deductions and credits** — Check Schedule A itemized deductions or standard deduction. Verify credits (child tax, EV, education, etc.) against supporting forms.
7. **Verify withholding and estimated payments** — Tie federal withholding to all W-2s and 1099s. Verify estimated tax payments against IRS records if available.
8. **Summarize findings** — Produce a findings list: confirmed items, variances, and items requiring preparer clarification.

## Control Points

- **Material variance** — Any discrepancy above the firm's materiality threshold requires preparer review and correction before filing.
- **Missing source documents** — Do not mark the review complete if source docs are missing for reported income.

## Red Flags

- Reported income doesn't match any source document on file
- K-1 shows a large loss but no basis worksheet is present
- Withholding on return exceeds withholding on source documents
- Prior-year carryforwards present but no supporting schedule
- QBI deduction taken without a supporting computation

## Output Format

A structured findings report:
- **Confirmed** — Line items that tie to source documents
- **Variances** — Discrepancies with amounts and source
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment or additional facts

## Safety Constraints

- Do not mark the return as reviewed-complete if material variances or missing documents remain.
- Do not draft a response to an IRS notice based on this review without preparer confirmation.
