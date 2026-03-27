---
name: tax-memo
version: 1.0.0
description: |
  Draft a client-facing tax memo from position notes, facts, and IRC citations.
  Translates technical tax analysis into a clear, professional memo the client
  can understand and act on.
trigger: |
  "tax memo", "client memo", "write a memo", "draft a memo", "memo to client",
  "summarize this tax position", "client summary"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Tax Memo: Client-Facing Tax Position Memo

## Purpose

Convert a tax position or analysis into a professional memo suitable for client delivery. The memo should be technically accurate with appropriate citations while remaining accessible to a non-tax audience.

## Required Inputs

- The tax issue or position (facts and conclusion)
- Relevant IRC sections, Treasury Regulations, or IRS guidance
- Client name and entity type (individual, S-corp, partnership, trust, etc.)
- Preferred output format (email body, attached memo, or brief summary)

## Workflow

1. **Clarify scope** — Confirm the issue, the client audience, and the desired format. Ask if not provided.
2. **Structure the memo** — Issue → Brief answer → Facts → Analysis → Conclusion → Recommendations → Next steps.
3. **Calibrate depth** — Match the technical level to the client. Cite authority but explain it in plain English.
4. **Draft output** — Produce the memo in the requested format with appropriate professional closing.

## Control Points

- **Gray areas** — If the position involves significant uncertainty, flag it explicitly and confirm the appropriate caveat language before drafting.
- **Client-ready review** — Always note that the draft should be reviewed by the responsible CPA before sending.

## Red Flags

- Issue involves pending legislation or recent IRS guidance — verify currency before citing
- Position involves a listed transaction or reportable transaction — escalate before drafting
- Facts are incomplete or ambiguous — ask before drawing conclusions

## Output Format

- **Email draft format** (default): Subject line, professional greeting, executive summary, analysis, next steps, closing
- **Memo format** (when requested): Issue, Brief Answer, Facts, Analysis, Conclusion, Recommendations
- **Technical memo** (when requested): Full IRC/Reg citations, more formal structure

## Safety Constraints

- Do not fabricate IRC citations or invent guidance that does not exist.
- Include appropriate disclaimer language: "This memo is for informational purposes and reflects our analysis based on the facts provided. Please consult with us before taking any action."
- Do not finalize a memo on a gray-area position without noting the uncertainty.
