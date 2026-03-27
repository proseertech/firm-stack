---
name: client-email
version: 1.1.0
description: |
  Polish and improve a CPA-to-client email draft. Takes an email thread and a draft
  reply, returns a more professional, clear, and approachable response with improvement
  notes and suggested clarifying questions if appropriate. Screens for technical accuracy
  before polishing — will not make incorrect advice sound authoritative.
trigger: |
  "improve this email", "polish my draft", "client email", "rewrite this email",
  "make this email better", "edit my reply"
allowed-tools:
  - AskUserQuestion
tier: all-staff
---

# Client Email: Polish CPA-to-Client Communications

## Purpose

Elevate the professionalism and clarity of email communications between accounting professionals and their clients. The audience is sophisticated but not technical in accounting or tax — write for that reader. Critically, this skill also screens for technical accuracy before polishing, ensuring that incorrect or unsupported claims are flagged rather than made more persuasive.

## Required Inputs

- The email thread (prior messages for context)
- The draft reply to improve

## Workflow

1. **Review context** — Read the full email thread to understand the client's question or concern, the history, and any outstanding items. Note every question or concern the client raised.
2. **Screen for technical claims** — Before touching tone or clarity, scan the draft for tax positions, dollar figures, deadlines, or regulatory statements. For each, determine whether the claim is (a) sourced from the email thread or a provided document, or (b) unsourced and potentially incorrect. Flag any unsourced technical claims — do not polish over them.
3. **Improve the draft** — Revise for:
   - Professional but friendly and approachable tone — not stuffy, never condescending
   - Clear, concise, jargon-free writing — when a technical term must be used (basis, passthrough, DNI, etc.), add a parenthetical plain-English explanation
   - Completeness — every question or concern the client raised in the thread is addressed, not just the ones the draft chose to answer
   - Appropriate level of explanation — provide context when concepts or decisions might be unclear to a non-expert, without over-explaining
   - Clear next steps and action items outlined at the end
   - Preserve the original format (brief reply vs. detailed explanation vs. formal letter) unless the user requests a change
4. **Summarize improvements** — Provide 2-3 bullet points on what was changed. Distinguish between:
   - **Tone/clarity edits** — phrasing, structure, readability
   - **Substantive changes** (marked with ⚠️) — added content, corrected information, or expanded explanations
5. **Flag gaps** — If anything in the draft or thread is unclear, or if a technical claim could not be verified, ask concise clarifying questions at the end.

## Control Points

- **Sensitive positions** — If the draft commits the firm to a specific tax position or includes financial figures, flag for partner review before sending.
- **Unsourced technical claims** — If Step 2 identifies tax positions, dollar figures, or deadlines not traceable to the email thread or provided documents, surface them to the user for verification before finalizing the improved draft.

## Red Flags

- Draft contains jargon the client likely won't understand without explanation
- Draft leaves a client question unanswered
- Draft includes a hard commitment the firm may not be able to stand behind
- Draft contains a specific tax position, deadline, or dollar figure not sourced from the email thread or a provided document
- Draft makes a commitment on behalf of the firm (timeline, deliverable, fee) without flagging it

## Output Format

1. **Improved email** — Ready to copy/paste, with subject line if new thread
2. **What was improved** — 2-3 bullet points, with ⚠️ marker on any substantive (non-cosmetic) changes
3. **Clarifying questions** (if any) — at the end, clearly separated

## Safety Constraints

- Do not fabricate tax positions, numbers, or commitments not in the original draft.
- Do not remove caveats or professional liability language from the original.
- Do not polish language that contains a potentially incorrect technical statement — flag it for review instead of improving its readability.
