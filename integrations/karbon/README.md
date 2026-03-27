# Karbon Integration

Skills that connect to the Karbon practice management API.

## Setup

### Prerequisites
- Karbon account with API access enabled
- API key from Karbon (Settings → API)

### Configuration

```
KARBON_ACCESS_TOKEN=your_access_token
KARBON_BEARER_KEY=your_bearer_key
```

Then reference in your project's `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Active integrations: karbon
```

## Available Skills

| Skill | Purpose |
|---|---|
| `/integrations/karbon/work-status` | Query and update Karbon work item status |

## Notes

- Karbon API base URL: `https://app.karbon.co/api/v3/`
- Authentication: Bearer token in the Authorization header
- Rate limits apply — the skill batches requests where possible
- Work items are referenced by their `WorkItemKey`
