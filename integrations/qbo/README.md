# QuickBooks Online Integration

Skills that connect to the QuickBooks Online API.

## Setup

### Prerequisites
- QuickBooks Online account with API access
- Intuit Developer account with an app created at developer.intuit.com
- OAuth2 credentials (client ID and client secret)

### Configuration

```
QBO_CLIENT_ID=your_client_id
QBO_CLIENT_SECRET=your_client_secret
QBO_REALM_ID=your_company_realm_id
QBO_ACCESS_TOKEN=your_oauth_access_token
QBO_REFRESH_TOKEN=your_oauth_refresh_token
```

Then reference in your project's `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Active integrations: qbo
- GL system: QuickBooks Online
```

## Available Skills

| Skill | Purpose |
|---|---|
| `/integrations/qbo/pull-reports` | Pull P&L and balance sheet from QBO |

## Notes

- QBO uses OAuth2 — tokens expire after 1 hour. The skill will attempt to refresh automatically using the refresh token.
- QBO API base URL: `https://quickbooks.api.intuit.com/v3/company/{realmId}/`
- Sandbox available at `https://sandbox-quickbooks.api.intuit.com/`
