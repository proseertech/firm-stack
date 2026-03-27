---
name: tax-memo
version: 1.1.0
description: |
  Draft a client-facing tax memo from position notes, facts, and IRC citations.
  Translates technical tax analysis into a clear, professional memo the client
  can understand and act on. Distinguishes clear rules from gray areas and
  includes a quality check before finalizing.
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
3. **Calibrate depth** — Match the technical level to the client audience. Apply these rules:
   - **Clear rules** — Cite the IRC section and state the rule directly. Use confident language: "Under IRC §X, the rule is..."
   - **Gray areas** — Cite authority on both sides. State the firm's recommended position with appropriate hedging: "Based on [authority], the stronger position is... however, [contrary authority] could support an alternative reading."
   - In all cases, follow the citation with a plain-English explanation of what it means for the client.
4. **Draft output** — Produce the memo in the requested format with appropriate professional closing.
5. **Quality check** — Before presenting the final output, verify:
   - Technical accuracy of all citations (IRC §, Treas. Reg. §, Rev. Rul., court cases) — do not cite guidance that does not exist
   - Tone matches the stated audience (client vs. internal reviewer vs. technical memo)
   - Recommendations are practically actionable, not just legally correct
   - All cited authority is current (not superseded by recent legislation or guidance)

## Control Points

- **Gray areas** — If the position involves significant uncertainty, flag it explicitly and confirm the appropriate caveat language before drafting.
- **Gray-area positions** — Before finalizing any memo on a gray-area position, present: the strongest authority supporting the position, the strongest authority against it, and the firm's recommended approach.
- **Client-ready review** — Always note that the draft should be reviewed by the responsible CPA before sending.

## Red Flags

- Issue involves pending legislation or recent IRS guidance — verify currency before citing
- Position involves a listed transaction or reportable transaction — escalate before drafting
- Facts are incomplete or ambiguous — ask before drawing conclusions
- Position requires specialist input beyond general tax practice (international tax, ERISA, state nexus) — flag and identify the specialty area

## Output Format

- **Email draft format** (default): Subject line, professional greeting, executive summary, analysis, next steps, closing
- **Memo format** (when requested): Issue, Brief Answer, Facts, Analysis, Conclusion, Recommendations
- **Technical memo** (when requested): Full IRC/Reg citations, more formal structure

## Safety Constraints

- Do not fabricate IRC citations or invent guidance that does not exist.
- Include appropriate disclaimer language: "This memo is for informational purposes and reflects our analysis based on the facts provided. Please consult with us before taking any action."
- Do not finalize a memo on a gray-area position without noting the uncertainty.
