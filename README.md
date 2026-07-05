# Evaluation Agent

[![CI](https://github.com/kogunlowo123/evaluation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/evaluation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI system evaluation agent that designs and runs evaluation suites for LLM applications, measuring accuracy, latency, cost, safety, and fairness with automated regression testing and benchmark comparison.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_eval_suite` | Create an evaluation suite with test cases and scoring rubrics |
| `run_evaluation` | Run an evaluation suite against a model or pipeline |
| `compare_models` | Compare multiple models on the same evaluation suite |
| `run_safety_eval` | Run safety and bias evaluation with adversarial test cases |
| `generate_report` | Generate a comprehensive evaluation report with visualizations |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/evals/create` | Create evaluation suite |
| `POST` | `/api/v1/evals/run` | Run evaluation |
| `POST` | `/api/v1/evals/compare` | Compare models |
| `POST` | `/api/v1/evals/safety` | Run safety evaluation |
| `POST` | `/api/v1/evals/report` | Generate evaluation report |

## Features

- Eval Design
- Benchmark Comparison
- Regression Testing
- Safety Evaluation
- Cost Analysis

## Integrations

- Promptfoo
- Langsmith
- Braintrust
- Humanloop
- Openai Evals

## Architecture

```
evaluation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── evaluation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Evaluation Frameworks + Benchmark Suites + Observability**

---

Built as part of the Enterprise AI Agent Platform.
