---
name: client-email
version: 1.3.0
description: |
  Polish a CPA-to-client email draft into a clear, professional, approachable reply.
  Use this whenever someone has written (or half-written) an email to a client and wants
  it improved, tightened, softened, or made more professional before sending — "clean up
  this reply", "does this sound okay to send", "make this less blunt", "help me respond to
  this client". Works from the email thread plus the draft, and screens for technical
  accuracy first so it never makes an unsupported claim sound more authoritative. This is
  for short client correspondence — for a formal, standalone position write-up, use
  `tax-memo` instead.
trigger: |
  "improve this email", "polish my draft", "client email", "rewrite this email",
  "make this email better", "edit my reply", "clean up this email", "help me respond",
  "reply to this client", "does this sound okay to send", "make this sound more professional",
  "soften this email", "how should I respond to this client"
allowed-tools:
  - AskUserQuestion
tier: all-staff
---

# Client Email: Polish CPA-to-Client Communications

## Purpose

Turn a CPA's rough email draft into a reply that is clear, professional, and approachable —
warm without being casual, precise without being dense. The client is sophisticated but not
a tax or accounting specialist, so write for an intelligent non-expert reader. Before any
polishing, the skill screens the draft for technical claims: making a wrong or unsupported
statement read more fluently makes it more dangerous, not less, so accuracy is checked first
and polish comes second.

This skill handles short correspondence — replies, status updates, gentle nudges. For a
formal, standalone write-up of a tax position, hand off to `tax-memo`.

## Required Inputs

- **The email thread** — prior messages, so the reply answers what the client actually asked
- **The draft reply** to improve

If the draft is missing, ask for it. Polishing a reply without the thread it responds to risks
leaving a client question unanswered — request the thread when it isn't provided.

## Workflow

1. **Review context** — Read the full thread to understand the client's question, the history,
   and any open items. Note *every* question or concern the client raised, so none gets dropped
   in the rewrite.
2. **Screen for technical claims first** — Before touching tone, scan the draft for tax positions,
   dollar figures, deadlines, and regulatory statements. For each, decide whether it is (a) sourced
   from the thread or a provided document, or (b) unsourced and possibly wrong. An unsourced claim
   that reads smoothly is worse than one that reads awkwardly, because it's more likely to be sent
   and believed — so flag these rather than polishing over them (see Control Points).
3. **Improve the draft** — Revise for:
   - **Tone** — professional but friendly and approachable; not stuffy, never condescending
   - **Clarity** — concise and jargon-free; when a technical term is unavoidable (basis, passthrough,
     DNI, etc.), add a short plain-English gloss in parentheses
   - **Completeness** — every question or concern the client raised is addressed, not only the ones
     the draft chose to answer
   - **Right level of explanation** — add context where a concept or decision might be unclear to a
     non-expert, without over-explaining what they already understand
   - **Clear next steps** — action items laid out at the end
   - **Format** — preserve the original shape (brief reply vs. detailed explanation vs. formal letter)
     unless the user asks to change it
4. **Summarize improvements** — 2-3 bullets on what changed, separating:
   - **Tone/clarity edits** — phrasing, structure, readability
   - **Substantive changes** (marked ⚠️) — added content, corrected information, or expanded explanation
5. **Flag gaps** — If anything in the draft or thread is unclear, or a technical claim couldn't be
   verified, ask concise clarifying questions at the end.

## Control Points

- **Sensitive positions** — If the draft commits the firm to a specific tax position or states
  financial figures, flag it for director review before sending. A polished email carries more
  weight; a firm commitment should be one someone signed off on.
- **Unsourced technical claims** — If Step 2 finds tax positions, dollar figures, or deadlines not
  traceable to the thread or a provided document, do not return the polished draft yet. List each
  unsourced claim and ask the user to confirm or correct it, then polish using the verified version.
  The whole point of screening first is that a fluent, confident email makes an error harder to catch.

## Red Flags

Pause and surface to the user when the draft:

- Uses jargon the client likely won't understand without explanation
- Leaves a client question unanswered
- Makes a hard commitment the firm may not be able to stand behind
- States a tax position, deadline, or dollar figure not sourced from the thread or a provided document
- Commits the firm to a timeline, deliverable, or fee without flagging it

## Output Format

1. **Improved email** — ready to copy/paste, with a subject line if it's a new thread
2. **What was improved** — 2-3 bullets, with a ⚠️ marker on any substantive (non-cosmetic) change
3. **Clarifying questions** (if any) — at the end, clearly separated

## Safety Constraints

- Do not fabricate tax positions, numbers, or commitments that aren't in the original draft.
- Do not remove caveats or professional-liability language from the original — those are there on purpose.
- Do not polish language that contains a possibly incorrect technical statement. Fluency makes an error
  more convincing, so flag it for review instead of improving its readability.
