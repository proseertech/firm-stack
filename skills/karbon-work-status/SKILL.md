---
name: karbon-work-status
version: 1.0.0
description: |
  Query and update Karbon work item status. Look up work items by client,
  work type, or assignee; check current status; and update status or
  add notes via the Karbon API.
trigger: |
  "Karbon status", "check work item", "update Karbon", "what's the status in Karbon",
  "Karbon work item", "close out Karbon"
allowed-tools:
  - Bash
  - AskUserQuestion
tier: developer
---

# Karbon Work Status: Query and Update Work Items

## Purpose

Check the status of Karbon work items and update them without leaving Claude Code. Useful during month-end close for status checks and progress tracking.

## Required Inputs

- Query scope: client name, work type (e.g., "Monthly Accounting"), assignee, or due date range
- Action: read-only status check, or update (status change, note addition)
- Karbon credentials configured in environment variables

## Workflow

1. **Confirm query** — What work items to look up (client, work type, period, assignee).
2. **Query Karbon API** — Fetch matching work items with their current status, assignee, and due date.
3. **Display results** — Show a table of matching work items with status.
4. **If updating** — Confirm the target work item and the new status/note with the user before making the API call.
5. **Execute update** — PATCH the work item status or POST a note. Return confirmation.

## Control Points

- **Confirm before updating** — Always show the user the target work item and proposed change before executing a status update or adding a note.

## Output Format

Status check:
```
Client          | Work Type          | Period  | Status        | Assignee  | Due
Acme Corp       | Monthly Accounting | Feb '26 | In Progress   | Maria C.  | Mar 7
Smith Trust     | 1041 Return        | 2025    | Ready Review  | Larry B.  | Apr 15
```

## Safety Constraints

- Never update a work item without explicit user confirmation.
- Never delete work items.
