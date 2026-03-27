---
name: client-email
version: 1.0.0
description: |
  Polish and improve a CPA-to-client email draft. Takes an email thread and a draft
  reply, returns a more professional, clear, and approachable response with improvement
  notes and suggested clarifying questions if appropriate.
trigger: |
  "improve this email", "polish my draft", "client email", "rewrite this email",
  "make this email better", "edit my reply"
allowed-tools:
  - AskUserQuestion
tier: all-staff
---

# Client Email: Polish CPA-to-Client Communications

## Purpose

Elevate the professionalism and clarity of email communications between accounting professionals and their clients. The audience is sophisticated but not technical in accounting or tax — write for that reader.

## Required Inputs

- The email thread (prior messages for context)
- The draft reply to improve

## Workflow

1. **Review context** — Read the full email thread to understand the client's question or concern, the history, and any outstanding items.
2. **Improve the draft** — Revise for professional but friendly tone, clarity, completeness, and appropriate level of explanation.
3. **Summarize improvements** — Provide 2-3 bullet points on what was changed and why.
4. **Flag gaps** — If anything in the draft or thread is unclear, ask one concise clarifying question.

## Control Points

- **Sensitive positions** — If the draft commits the firm to a specific tax position or includes financial figures, flag for partner review before sending.

## Red Flags

- Draft contains jargon the client likely won't understand without explanation
- Draft leaves a client question unanswered
- Draft includes a hard commitment the firm may not be able to stand behind

## Output Format

1. **Improved email** — Ready to copy/paste, with subject line if new thread
2. **What was improved** — 2-3 bullet points
3. **Clarifying questions** (if any) — at the end, clearly separated

## Safety Constraints

- Do not fabricate tax positions, numbers, or commitments not in the original draft.
- Do not remove caveats or professional liability language from the original.
