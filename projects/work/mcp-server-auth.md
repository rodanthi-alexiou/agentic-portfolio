---
title: "MCP Server Auth"
category: work
status: in-progress
repo: "https://github.com/rodanthi-alexiou/roda-agentic-workshop"
demo: ""
tags: [security, mcp, azure, oauth, api-management, identity, bicep]
tech: [Python, Bicep, FastAPI, Azure Container Apps, Azure API Management, Entra ID]
skills:
  - mcp-oauth
  - apim-gateway
  - entra-id
  - managed-identity
  - bicep-iac
  - azure-container-apps
  - mcp-protocol
  - graph-api-tools
  - azure-rbac
summary: "Reference implementation for securing hosted MCP servers on Azure using OAuth 2.0, Entra ID, Managed Identity, and APIM — designed for ISV partners."
highlight: "Full MCP OAuth 2.0 gateway with Entra ID including JWKS validation, OBO token exchange, and RFC 8414/8707 discovery endpoints — plus proof that token passthrough is an anti-pattern."
audience: ISV partners building hosted MCP servers on Azure for production
---

# MCP Server Auth

## What It Is

A complete reference implementation demonstrating how to secure a hosted MCP (Model Context Protocol) server on Azure. Covers two distinct auth layers: **server-level auth** (who can call the MCP server) and **tool-level auth** (how the server calls Azure backends). Built as a partner demo for Microsoft Foundry.

**Audience**: ISV partners who need to host MCP servers securely and integrate them with Azure AI Foundry agents.

## What I Built

- ✅ FastAPI-based MCP server with `/mcp` (Streamable HTTP) and `/healthz` endpoints
- ✅ Azure API Management as OAuth 2.0 authorization gateway with `validate-azure-ad-token` policy
- ✅ Entra ID app registration automation in Bicep (client app + API app + OBO stack)
- ✅ System-assigned Managed Identity on Container Apps — no credentials in code
- ✅ 8 APIM policy XML files: authorize, consent, oauth-callback, token, register, protected-resource-metadata, oauthmetadata-get, mcp-api
- ✅ 8 Bicep infrastructure modules: APIM, Container Apps, Cosmos DB, Key Vault, Azure OpenAI, Storage, Monitor, Entra OBO stack
- ✅ MS Graph API tools via MCP using delegated OBO permissions
- ✅ Test suite: token acquisition (`get-token.py`), MCP auth validation (`mcp-auth.py`)

## Architecture

```
Client (Foundry Agent)
    │
    │  OAuth 2.0 Bearer Token (Entra ID)
    ▼
Azure API Management (Developer tier)
    │  validate-azure-ad-token policy
    │  client-application-ids allowlist
    ▼
Azure Container Apps (Consumption)
    │  FastAPI MCP Server
    │  System-assigned Managed Identity
    ▼
Azure Backends (OpenAI, Storage, Graph)
    │  Managed Identity token (IMDS)
    │  RBAC role assignments
    ▼
Resources
```

**Key Security Decisions**:
1. Entra ID for server-level authentication (not key-based)
2. Managed Identity for tool-level auth (zero credentials in code)
3. `validate-azure-ad-token` APIM policy (not generic JWT)
4. Stateless MCP design (session ID generation disabled)
5. Token passthrough prohibited — MCP server uses its own MI token, never forwards caller token

**Authentication Modes**:
| Mode | Use Case | Production-Ready |
|------|---------|-----------------|
| Microsoft Entra M2M | Machine-to-machine | ✅ Yes |
| OAuth Identity Passthrough | User-delegated with consent | ✅ Yes |
| Key-based | Development only | ❌ No |
| Unauthenticated | Development only | ❌ No |

## Skills Demonstrated

- [`mcp-oauth`](../../SKILLS-CATALOG.md#mcp-oauth)
- [`apim-gateway`](../../SKILLS-CATALOG.md#apim-gateway)
- [`entra-id`](../../SKILLS-CATALOG.md#entra-id)
- [`managed-identity`](../../SKILLS-CATALOG.md#managed-identity)
- [`bicep-iac`](../../SKILLS-CATALOG.md#bicep-iac)
- [`azure-container-apps`](../../SKILLS-CATALOG.md#azure-container-apps)
- [`mcp-protocol`](../../SKILLS-CATALOG.md#mcp-protocol)
- [`graph-api-tools`](../../SKILLS-CATALOG.md#graph-api-tools)

## Status & Next Steps

**Done:**
- [x] MCP server with Managed Identity tool auth
- [x] APIM OAuth gateway with `validate-azure-ad-token`
- [x] Entra ID Bicep modules (client app, API app, OBO stack)
- [x] 8 APIM policy files (full OBO flow)
- [x] Test scripts for token + MCP auth validation

**Next (MCP spec compliance gaps):**
- [ ] `/.well-known/oauth-protected-resource` endpoint
- [ ] `/.well-known/oauth-authorization-server` endpoint  
- [ ] `POST /register` — dynamic client registration via Cosmos DB
- [ ] `GET /authorize` with PKCE (RFC 7636)
- [ ] `POST /token` with encrypted session key issuance
- [ ] Consent management flow with UI

## Links

- **Repo**: [roda-agentic-workshop](https://github.com/rodanthi-alexiou/roda-agentic-workshop)
- **Architecture**: [architecture.md](https://github.com/rodanthi-alexiou/roda-agentic-workshop/blob/main/mcp-server-auth-usecase/architecture.md)
- **Technical Docs**: [technical-docs.md](https://github.com/rodanthi-alexiou/roda-agentic-workshop/blob/main/mcp-server-auth-usecase/technical-docs.md)
- **One-Pager**: [APIM-OBO-ONEPAGER.md](https://github.com/rodanthi-alexiou/roda-agentic-workshop/blob/main/mcp-server-auth-usecase/mcp-server-auth-implementation/APIM-OBO-ONEPAGER.md)
