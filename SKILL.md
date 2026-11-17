---
description: Multi-Agent C-Suite Orchestrator. Manages a team of specialized AI agents (CMO, CTO, CFO, etc.) for cohesive business strategy.
license: MIT
metadata:
  last_deployed: "2026-04-25"
  version: "1.0.0"
  source: "https://www.accio.com/"
---

# Accio C-Suite Manager

This skill allows an agent to act as a Chief of Staff, orchestrating multiple specialized AI personas to solve complex business problems. It ensures that strategic advice is balanced across multiple domains (marketing, technology, finance).

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Instructions
1. **Agent Spawning:** Initialize and assign specific roles (CEO, CMO, CTO, CFO) based on the task complexity.
2. **Collaborative Brainstorming:** Facilitate a multi-turn dialogue between agents to refine a business proposal.
3. **Synthesis of Expertise:** Aggregate the output from various specialized agents into a single, comprehensive executive summary.
4. **Execution Delegation:** Assign specific sub-tasks to the most qualified agent in the virtual "C-suite."

## Examples
- "I want to launch a new software product. Have the CTO evaluate the tech stack and the CMO design the go-to-market strategy, then give me a combined report."
- "Sprout a CFO agent to analyze my projected burn rate and a CEO agent to suggest pivot strategies."
