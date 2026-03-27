# Sage Intacct Integration

Skills that connect directly to the Sage Intacct REST API.

## Setup

### Prerequisites
- Sage Intacct company with Web Services enabled
- A Web Services user with appropriate permissions
- Your Intacct Sender ID and password (from your Web Services subscription)

### Configuration

Add the following to your project's `.env` file (never commit this):

```
INTACCT_SENDER_ID=your_sender_id
INTACCT_SENDER_PASSWORD=your_sender_password
INTACCT_COMPANY_ID=your_company_id
INTACCT_USER_ID=your_ws_user_id
INTACCT_USER_PASSWORD=your_ws_user_password
```

Then reference these in your project's `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Active integrations: sage-intacct
- GL system: Sage Intacct
```

## Available Skills

| Skill | Purpose |
|---|---|
| `/integrations/sage-intacct/import-je` | Import journal entries via Intacct REST API |
| `/integrations/sage-intacct/pull-tb` | Pull trial balance from Intacct |

## Notes

- Intacct's REST API uses XML-based requests via HTTPS POST to `https://api.intacct.com/ia/xml/xmlgw.phtml`
- Multi-entity companies: specify the entity ID in your config or the skill will prompt for it
- Rate limits: Intacct limits API calls per session — batch operations where possible
