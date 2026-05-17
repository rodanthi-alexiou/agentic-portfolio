# Skills Catalog

> Master index of every skill in this portfolio — what it enables, which projects use it, and where to find the reference implementation.  
> Skills map directly to project frontmatter `skills:` tags, so the [README atlas](README.md) stays in sync.

**Quick filter**: [🔒 Security](#-security--identity) · [🤖 AI & Agents](#-ai--agents) · [📡 Observability](#-observability--telemetry) · [🏗️ Infrastructure](#️-infrastructure--deployment) · [🌐 API & Protocol](#-api--protocol) · [🔍 Operations](#-operations--resource-management)

---

## 🔒 Security & Identity

### `mcp-oauth`
**What it enables**: Full MCP OAuth 2.0 gateway — OAuth discovery (RFC 8414/8707), PKCE auth code flow, OBO token exchange, dynamic client registration via Cosmos DB.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/mcp-server-auth-implementation`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `mcp-apim-oauth`, APIM policy set (8 policy XML files)

---

### `apim-gateway`
**What it enables**: Azure API Management as a secure gateway — JWT validation, rate limiting, AI gateway patterns, MCP proxy, content safety.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/infra/modules/apim-mcp.bicep`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `azure-aigateway`, Bicep module `apim.bicep`

---

### `entra-id`
**What it enables**: Microsoft Entra ID app registrations — M2M Client Credentials, user-delegated OBO flows, MSAL integration, multi-app registration patterns with Bicep.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/infra/modules/entra-app.bicep`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `entra-app-registration`, Bicep modules `entra-app.bicep`, `entra-obo-stack.bicep`

---

### `managed-identity`
**What it enables**: Passwordless authentication between Azure services; RBAC role assignment automation via Bicep; eliminates credentials in application code.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/infra/modules/aca.bicep`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `azure-rbac`

---

### `azure-compliance`
**What it enables**: Azure compliance and security audits using `azqr`, Key Vault expiration checks, best-practice assessment.  
**Used in**: _(available, not yet applied to a project)_  
**Reusable as**: Copilot skill `azure-compliance`

---

## 🤖 AI & Agents

### `azure-foundry-agents`
**What it enables**: End-to-end Azure AI Foundry agent lifecycle — create hosted agents, invoke with AzureAIAgentClient, batch evaluation, prompt optimization.  
**Used in**: [GenAI Observability](projects/work/observability.md)  
**Reference**: [`roda-agentic-workshop/observability/demo-workflow.py`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `microsoft-foundry`, `vscode-microsoft-foundry`

---

### `agent-evaluation`
**What it enables**: Dataset curation from traces, batch eval runs, KPI definition, eval trending over time.  
**Used in**: [GenAI Observability](projects/work/observability.md)  
**Reusable as**: Copilot skill `microsoft-foundry` (evaluation commands)

---

### `prompt-optimization`
**What it enables**: Automated prompt optimizer workflows; A/B comparison against eval datasets; system prompt improvement using Foundry.  
**Used in**: [GenAI Observability](projects/work/observability.md)  
**Reusable as**: Copilot skill `microsoft-foundry` (prompt optimizer workflow)

---

### `azure-ai`
**What it enables**: Azure AI Search (vector/hybrid/semantic), Azure Speech (STT/TTS), Document Intelligence, Azure OpenAI.  
**Used in**: _(available, not yet applied to a project)_  
**Reusable as**: Copilot skill `azure-ai`

---

### `azure-hosted-copilot-sdk`
**What it enables**: Build and deploy GitHub Copilot SDK apps to Azure — `CopilotClient`, session management, BYOM with Azure OpenAI.  
**Used in**: _(available, not yet applied to a project)_  
**Reusable as**: Copilot skill `azure-hosted-copilot-sdk`

---

## 📡 Observability & Telemetry

### `app-insights`
**What it enables**: Application Insights SDK setup, custom event tracking, dependency tracking, alert rules, App Insights Agents blade integration.  
**Used in**: [GenAI Observability](projects/work/observability.md)  
**Reference**: [`roda-agentic-workshop/observability/demo-workflow.py`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `appinsights-instrumentation`

---

### `genai-telemetry`
**What it enables**: OpenTelemetry GenAI semantic conventions — `invoke_agent` → `chat` → `execute_tool` span hierarchy; full local span emission with MAF.  
**Used in**: [GenAI Observability](projects/work/observability.md)  
**Reference**: [`roda-agentic-workshop/observability/demo-workflow.py`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Code pattern in `demo-workflow.py` (switch `--mcp` for HostedMCPTool spans)

---

### `opentelemetry`
**What it enables**: Distributed tracing across agents, tools, and Azure backends; trace correlation; `azure-monitor-opentelemetry` exporter setup.  
**Used in**: [GenAI Observability](projects/work/observability.md)  
**Reusable as**: Copilot skill `azure-diagnostics`

---

### `azure-kusto`
**What it enables**: KQL queries against Azure Data Explorer for log analytics, IoT telemetry, time series, anomaly detection.  
**Used in**: _(available, not yet applied to a project)_  
**Reusable as**: Copilot skill `azure-kusto`

---

## 🏗️ Infrastructure & Deployment

### `bicep-iac`
**What it enables**: Modular Bicep infrastructure — APIM, Container Apps, Cosmos DB, Key Vault, Azure OpenAI, Storage, Monitor, Entra app registrations.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/infra/modules/`](https://github.com/rodanthi-alexiou/roda-agentic-workshop) (8 modules)  
**Reusable as**: Copilot skill `azure-prepare`, `azure-deploy`, Bicep modules directly

---

### `azure-container-apps`
**What it enables**: Azure Container Apps deployment — Consumption tier, scale-to-zero, system-assigned Managed Identity, CI/CD via azd.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/infra/modules/aca.bicep`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `azure-prepare`

---

### `azure-prepare`
**What it enables**: Full app-to-Azure scaffolding — Bicep/Terraform, `azure.yaml`, Dockerfiles, environment setup.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reusable as**: Copilot skill `azure-prepare`

---

### `azure-validate`
**What it enables**: Pre-deployment validation — configuration checks, Bicep/Terraform lint, permission preflight, readiness assessment.  
**Reusable as**: Copilot skill `azure-validate`

---

### `azure-kubernetes`
**What it enables**: Production AKS clusters — SKU selection (Automatic vs Standard), networking, security, autoscaling, upgrade strategy.  
**Reusable as**: Copilot skill `azure-kubernetes`

---

### `azure-enterprise-infra`
**What it enables**: Enterprise-scale Azure infrastructure — hub-spoke networking, landing zones, VNets, firewalls, private endpoints, multi-region DR.  
**Reusable as**: Copilot skill `azure-enterprise-infra-planner`

---

### `azure-cloud-migrate`
**What it enables**: Cross-cloud workload migration to Azure — AWS Lambda → Azure Functions, GCP → Azure, migration readiness reports.  
**Reusable as**: Copilot skill `azure-cloud-migrate`

---

## 🌐 API & Protocol

### `mcp-protocol`
**What it enables**: Stateless MCP server design, Streamable HTTP transport (MCP 2025-11-25), Foundry tool integration, server/tool auth separation.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/src/server.py`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Copilot skill `mcp-apim-oauth`, `mcpserverapim.agent.md`

---

### `graph-api-tools`
**What it enables**: MS Graph API integration via MCP tools — delegated permissions, OBO flow, user profile/calendar/mail access.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reference**: [`roda-agentic-workshop/src/tools/graph_tools.py`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Code module `graph_tools.py`

---

### `azure-messaging`
**What it enables**: Azure Event Hubs and Service Bus SDK — connection troubleshooting, AMQP, event processor, dead letter.  
**Reusable as**: Copilot skill `azure-messaging`

---

## 🔍 Operations & Resource Management

### `azure-diagnostics`
**What it enables**: Production issue debugging — AppLens, Azure Monitor, resource health, KQL log analysis, container crash diagnosis.  
**Reusable as**: Copilot skill `azure-diagnostics`

---

### `azure-cost-optimization`
**What it enables**: Azure cost analysis, orphaned resource detection, rightsizing recommendations, cost reduction reports.  
**Reusable as**: Copilot skill `azure-cost-optimization`

---

### `azure-resource-visualizer`
**What it enables**: Mermaid architecture diagrams auto-generated from Azure resource groups — topology, relationships, component tables.  
**Reusable as**: Copilot skill `azure-resource-visualizer`

---

### `azure-rbac`
**What it enables**: Least-privilege RBAC role selection, role assignment Bicep generation, managed identity permission design.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reusable as**: Copilot skill `azure-rbac`

---

### `azure-storage`
**What it enables**: Azure Blob Storage, File Shares, Queue Storage, Data Lake — object storage, lifecycle management, access tiers.  
**Reusable as**: Copilot skill `azure-storage`

---

## 🛠️ Agent & Copilot Tooling

### `copilot-agents`
**What it enables**: Multi-stage GitHub Copilot agent pipelines — Onboarding → Architect → Builder pattern; `.agent.md` definition files; skills library.  
**Used in**: [roda-agentic-workshop](https://github.com/rodanthi-alexiou/roda-agentic-workshop) (meta-skill of the workshop itself)  
**Reference**: [`roda-agentic-workshop/.github/agents/`](https://github.com/rodanthi-alexiou/roda-agentic-workshop)  
**Reusable as**: Agent definition files, skills library (26 skills)

---

### `foundry-demo-usecase`
**What it enables**: Scaffold and maintain partner demo use case folders with README, technical-docs, architecture, and demo-action-plan.  
**Used in**: [MCP Server Auth](projects/work/mcp-server-auth.md)  
**Reusable as**: Copilot skill `foundry-demo-usecase`

---

## Skill Count by Category

| Category | Skills | Applied to Projects |
|----------|--------|-------------------|
| 🔒 Security & Identity | 5 | 4 |
| 🤖 AI & Agents | 5 | 3 |
| 📡 Observability | 4 | 3 |
| 🏗️ Infrastructure | 6 | 2 |
| 🌐 API & Protocol | 3 | 2 |
| 🔍 Operations | 5 | 1 |
| 🛠️ Agent Tooling | 2 | 2 |
| **Total** | **30** | |
