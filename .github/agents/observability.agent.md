---
description: >
  Agent scoped to the GenAI Observability project. Specializes in instrumenting
  Azure AI Foundry agents with OpenTelemetry, GenAI semantic conventions, and
  exporting distributed traces to Application Insights.
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

You are working on the **GenAI Observability** project — end-to-end observability for Azure AI Foundry (MAF) agents using OpenTelemetry, GenAI semantic conventions, and Azure Application Insights.
Repo: https://github.com/rodanthi-alexiou/roda-agentic-workshop

## Project architecture

```
Python (local)
    │  azure.ai.agents.AgentClient
    │  + OpenTelemetry tracing enabled
    ▼
Azure AI Foundry (hosted agent)
    │  Messages API + Tool execution
    ▼
azure-monitor-opentelemetry exporter
    │  (APPLICATIONINSIGHTS_CONNECTION_STRING)
    ▼
Azure Application Insights
    └─ invoke_agent
        ├─ chat (completion 1)
        │   └─ execute_tool (tool call 1)
        └─ chat (completion 2, after tool)
```

## Key files

- `demo-workflow.py` — single-file MAF demo, CLI-runnable, full OTel instrumentation
- `--mcp` flag — swaps in `HostedMCPTool` to capture MCP tool spans alongside chat spans

## GenAI span attributes (OpenTelemetry semantic conventions)

| Attribute | What it tracks |
|---|---|
| `gen_ai.system` | AI system name |
| `gen_ai.request.model` | Model name |
| `gen_ai.usage.input_tokens` | Input token count per span |
| `gen_ai.usage.output_tokens` | Output token count per span |
| `gen_ai.tool.name` | Tool invoked in execute_tool spans |

## Skills to use for this project

| Task | Skill |
|---|---|
| Query or diagnose App Insights | `appinsights-instrumentation`, `azure-diagnostics` |
| Inspect live telemetry / Log Analytics | `azure-resource-lookup` + Azure MCP log query tools |
| Check Foundry agent deployments | `microsoft-foundry` |
| Review AI model usage and costs | `azure-ai`, `azure-cost` |
| RBAC for App Insights / Monitor | `azure-rbac` |
| Add new Azure Monitor-backed infra | `azure-validate`, `azure-deploy` |

## Rules

- Always instrument at the `AgentClient` level, not at the HTTP layer — GenAI semantic conventions require semantic span names (`invoke_agent`, `chat`, `execute_tool`), not HTTP verbs.
- The `APPLICATIONINSIGHTS_CONNECTION_STRING` must come from Azure Key Vault or environment — never hardcoded.
- Parent/child span hierarchy is required: `invoke_agent` → `chat` → `execute_tool`. Flat traces miss the call chain.
- Use Azure MCP log query tools to validate that spans are arriving in App Insights before writing any analysis code.
- Token cost visibility: aggregate `gen_ai.usage.input_tokens` + `gen_ai.usage.output_tokens` per `invoke_agent` span to get conversation-level cost.
- When adding new tools to the agent, add corresponding `execute_tool` span assertions to the test suite.
