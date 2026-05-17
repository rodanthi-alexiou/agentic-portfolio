---
title: "GenAI Observability"
category: work
status: in-progress
repo: "https://github.com/rodanthi-alexiou/roda-agentic-workshop"
demo: ""
tags: [observability, ai, agents, opentelemetry, app-insights, azure-foundry]
tech: [Python, OpenTelemetry, Azure Monitor, Application Insights, Azure AI Foundry]
skills:
  - app-insights
  - genai-telemetry
  - opentelemetry
  - azure-foundry-agents
  - agent-evaluation
  - prompt-optimization
summary: "End-to-end observability for Azure AI Foundry agents — distributed traces from invoke_agent to tool execution, visualized in Application Insights."
highlight: "Local MAF workflow that produces a full invoke_agent → chat → execute_tool span hierarchy in App Insights — proving GenAI semantic conventions work with Azure Monitor before any cloud infra."
audience: AI platform teams adding production observability to Foundry-based agent solutions
---

# GenAI Observability

## What It Is

A demonstration of how to instrument Azure AI Foundry (MAF) agent workflows with OpenTelemetry, following the [GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/). Produces parent/child spans across the full agent call chain — from the initial `invoke_agent` call through every `chat` completion and `execute_tool` step — and exports them to Azure Application Insights.

**Audience**: AI platform teams building with Foundry who want production-grade telemetry with minimal code changes.

## What I Built

- ✅ `demo-workflow.py` — single-file MAF demo that runs a hosted Foundry agent locally with full OpenTelemetry instrumentation
- ✅ Span hierarchy: `invoke_agent` → `chat` → `execute_tool` (full parent/child chain)
- ✅ `azure-monitor-opentelemetry` exporter wired to APPLICATIONINSIGHTS_CONNECTION_STRING
- ✅ `--mcp` flag: swap in HostedMCPTool to capture MCP tool spans alongside chat spans
- ✅ CLI-runnable: no backend infra required to see spans in App Insights
- ✅ GenAI attributes on spans: `gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.tool.name`

## Architecture

```
Python (local)
    │
    │  azure.ai.agents.AgentClient
    │  + OpenTelemetry tracing enabled
    ▼
Azure AI Foundry (hosted agent)
    │  Messages API + Tool execution
    ▼
Spans emitted via azure-monitor-opentelemetry
    │
    ▼
Azure Application Insights
    └─ invoke_agent
        ├─ chat (completion 1)
        │   └─ execute_tool (tool call 1)
        └─ chat (completion 2, after tool)
```

**Why spans matter for GenAI**:
- Cost visibility: sum `gen_ai.usage.input_tokens` + `output_tokens` per conversation
- Latency breakdown: time in LLM vs time in tool vs orchestration overhead  
- Debugging: trace which tool input caused a bad output
- Evaluation correlation: link eval results back to specific traces

## Skills Demonstrated

- [`app-insights`](../../SKILLS-CATALOG.md#app-insights)
- [`genai-telemetry`](../../SKILLS-CATALOG.md#genai-telemetry)
- [`opentelemetry`](../../SKILLS-CATALOG.md#opentelemetry)
- [`azure-foundry-agents`](../../SKILLS-CATALOG.md#azure-foundry-agents)

## Status & Next Steps

**Done:**
- [x] MAF agent with OpenTelemetry tracing
- [x] Full span hierarchy in App Insights
- [x] MCP tool variant with `--mcp` flag
- [x] GenAI semantic convention attributes on all spans

**Next:**
- [ ] Semantic caching metric (cache hit/miss as span event)
- [ ] Multi-agent demo: span correlation across agent-to-agent calls
- [ ] Dashboard template (Azure Workbook) for GenAI cost + latency breakdown
- [ ] Evaluation: trace-to-eval linkage via `gen_ai.conversation.id`

## Links

- **Repo**: [roda-agentic-workshop](https://github.com/rodanthi-alexiou/roda-agentic-workshop)
- **Main File**: [observability/demo-workflow.py](https://github.com/rodanthi-alexiou/roda-agentic-workshop/blob/main/observability/demo-workflow.py)
