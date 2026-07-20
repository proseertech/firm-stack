---
name: tax-memo
version: 1.2.0
description: |
  Write a polished, client-facing tax memo from an already-worked position — the
  facts, the conclusion, and the IRC/reg citations behind it. This is the drafting
  step: you have (or the user hands you) the analysis, and you turn it into a memo
  the client can read and act on. Use it whenever someone wants a position written
  up for a client — "draft a memo on this", "put this in a client memo", "write this
  up for the client", "turn my notes into a memo", "summarize this position for the
  client" — even if they don't say the word "memo." Keeps clear rules confident and
  gray areas honestly hedged, and quality-checks every citation before finalizing.
  For the underlying research, or a technical read of whether the position actually
  holds up, that's tax-advisor — this skill formats the deliverable.
trigger: |
  "tax memo", "client memo", "write a memo", "draft a memo", "memo to client",
  "put this in a memo", "write this up for the client", "turn these notes into a memo",
  "write up this position for the client", "client-facing summary of this position"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Tax Memo: Client-Facing Tax Position Memo

## Purpose

Convert a tax position or analysis into a professional memo suitable for client delivery. The memo should be technically accurate with appropriate citations while remaining accessible to a non-tax audience.

## Scope & Handoffs

This skill is the **writing step**, not the research step. It assumes the position has already been worked — the facts, conclusion, and authority exist and are supplied. If the substantive question is still open ("how *should* we treat this", "is this defensible", "check whether this holds up"), that analysis belongs to **`tax-advisor`**; run that first, then bring the conclusion here to draft the client memo. Don't re-litigate the position while formatting it — but if a citation looks wrong or a gap appears while drafting, stop and flag it rather than papering over it.

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

- **Gray-area positions** — Before finalizing any memo on a position involving significant uncertainty, stop and present: the strongest authority supporting the position, the strongest authority against it, and the firm's recommended approach — and confirm the caveat language with the user before drafting. Overstated certainty on a judgment call is what turns a memo into a malpractice exposure.
- **Client-ready review** — Note that the draft must be reviewed and owned by the responsible CPA before it goes to the client; the memo is a draft until that happens.

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

- Never fabricate IRC citations or invent guidance that does not exist. A memo goes to the client under the firm's name; an invented citation is a client-facing misstatement that can survive into a filing. If you cannot stand behind a cite, leave it out and flag the gap.
- Include appropriate disclaimer language: "This memo is for informational purposes and reflects our analysis based on the facts provided. Please consult with us before taking any action."
- Do not finalize a memo on a gray-area position without noting the uncertainty.
