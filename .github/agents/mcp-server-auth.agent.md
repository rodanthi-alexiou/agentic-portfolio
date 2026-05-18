---
description: >
  Agent scoped to the MCP Server Auth project. Specializes in securing hosted
  MCP servers on Azure using OAuth 2.0, Entra ID, APIM, Managed Identity,
  Container Apps, and Bicep IaC.
tools:
  - changes
  - codebase
  - editFiles
  - fetch
  - problems
  - runCommands
  - search
  - usages
---

You are working on the **MCP Server Auth** project — a reference implementation for securing hosted MCP servers on Azure using OAuth 2.0, Entra ID, APIM, and Managed Identity.
Repo: https://github.com/rodanthi-alexiou/roda-agentic-workshop

## Project architecture

```
Client (Foundry Agent)
    │  OAuth 2.0 Bearer Token (Entra ID)
    ▼
Azure API Management  ← validate-azure-ad-token policy, client-app allowlist
    ▼
Azure Container Apps  ← FastAPI MCP Server, System-assigned Managed Identity
    ▼
Azure Backends (OpenAI, Storage, Graph)  ← IMDS token, RBAC role assignments
```

Two auth layers:
1. **Server-level auth** — who can call the MCP server (APIM + Entra ID)
2. **Tool-level auth** — how the server calls Azure backends (Managed Identity + OBO)

## Skills to use for this project

| Task | Skill |
|---|---|
| Review or update infra | `azure-enterprise-infra-planner`, `azure-validate`, `azure-deploy` |
| Debug auth failures | `azure-diagnostics`, `azure-rbac` |
| Review APIM policies | `azure-diagnostics` + read the 8 policy XML files |
| Update Bicep modules | `azure-validate` before applying any change |
| Entra ID app registrations | `entra-app-registration` |
| RBAC role assignments | `azure-rbac` |
| Container Apps config | `azure-diagnostics`, `azure-deploy` |
| OBO / token flow questions | `entra-app-registration`, `azure-rbac` |

## Key components

- **8 APIM policy XML files**: authorize, consent, oauth-callback, token, register, protected-resource-metadata, oauthmetadata-get, mcp-api
- **8 Bicep modules**: APIM, Container Apps, Cosmos DB, Key Vault, Azure OpenAI, Storage, Monitor, Entra OBO stack
- **Test scripts**: `get-token.py` (token acquisition), `mcp-auth.py` (MCP auth validation)
- **MCP endpoints**: `/mcp` (Streamable HTTP), `/healthz`

## Rules

- Token passthrough is an anti-pattern — always validate tokens at the gateway (APIM), not in application code.
- System-assigned Managed Identity on Container Apps — no credentials stored in code or environment variables.
- JWKS validation and RFC 8414/8707 discovery endpoints must be present for spec-compliant OAuth 2.0.
- OBO (On-Behalf-Of) token exchange is required when the MCP server needs delegated MS Graph permissions.
- Before changing any Bicep module, run `azure-validate` and check APIM policy dependencies.
- Use Azure MCP tools to inspect live APIM policies, Container Apps health, and Key Vault secrets status.
