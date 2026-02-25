# Agent Compatibility Benchmarks

Tests run against real AI agents to verify skill discovery and execution.

## Test Matrix

| AI Agent | Discovery | Execution | Score |
|----------|-----------|-----------|-------|
| Claude Code | Passed | Passed | 100% |
| GitHub Copilot | Passed | Testing | TBD |
| OpenAI Codex CLI | Testing | Testing | TBD |
| Cursor | Passed | Testing | TBD |
| Gemini CLI | Testing | Testing | TBD |

## What We Test

### Discovery Tests

Verify the agent can find and parse skills from this repository:

1. **Index parsing** -- Agent reads `index.json` and understands the skill catalog
2. **Frontmatter parsing** -- Agent reads SKILL.md YAML frontmatter correctly
3. **Subdomain filtering** -- Agent filters skills by subdomain (e.g., "show me all threat-hunting skills")
4. **Tag-based search** -- Agent finds skills by tag (e.g., "mitre-attack", "owasp")
5. **Framework lookup** -- Agent maps a framework reference (e.g., "T1566") to relevant skills
6. **Natural language query** -- Agent understands "How do I analyze phishing emails?" and returns relevant skills

### Execution Tests

Verify the agent can use skill content to perform tasks:

1. **Procedure following** -- Agent reads the skill steps and executes them in order
2. **Tool invocation** -- Agent installs/uses tools referenced in the skill (e.g., Volatility, Wireshark)
3. **Script execution** -- Agent runs scripts from the `scripts/` directory where available
4. **Template usage** -- Agent fills in templates from the `assets/` directory with real data
5. **Reference consultation** -- Agent reads `references/` for standards and applies them
6. **Multi-skill chaining** -- Agent combines multiple skills for complex workflows (e.g., forensic acquisition followed by analysis)

## Scoring Methodology

Each test category is scored on a 0-100 scale:

| Score | Meaning |
|-------|---------|
| 0-25 | Agent cannot perform the task |
| 26-50 | Agent partially performs the task with significant errors |
| 51-75 | Agent performs the task with minor issues |
| 76-100 | Agent performs the task correctly and completely |

The overall score is the average of Discovery and Execution scores.

## How to Run Benchmarks

### Prerequisites

- Access to the AI agent being tested
- This repository cloned locally or accessible to the agent
- Python 3.10+ for the test harness

### Running Discovery Tests

```bash
# Point the agent at the repository and ask it to find skills
# Record pass/fail for each discovery test category

# Example prompts to test:
# 1. "List all skills in the threat-hunting subdomain"
# 2. "Find skills tagged with mitre-attack"
# 3. "What skills help with T1566 Phishing?"
# 4. "How many skills are in this repository?"
# 5. "Show me the skill for analyzing memory dumps with Volatility"
```

### Running Execution Tests

```bash
# Point the agent at a specific skill and ask it to execute the procedure
# Record pass/fail for each execution test category

# Example prompts to test:
# 1. "Follow the steps in analyzing-phishing-email-headers/SKILL.md"
# 2. "Run the script in analyzing-security-logs-with-splunk/scripts/"
# 3. "Fill in the template for incident-response using the provided assets"
# 4. "Analyze this PCAP file using the analyzing-network-traffic-with-wireshark skill"
```

### Recording Results

Results should be recorded in the following format:

```json
{
  "agent": "Claude Code",
  "version": "1.0",
  "date": "2026-02-25",
  "discovery": {
    "index_parsing": 100,
    "frontmatter_parsing": 100,
    "subdomain_filtering": 100,
    "tag_search": 100,
    "framework_lookup": 100,
    "natural_language": 95
  },
  "execution": {
    "procedure_following": 100,
    "tool_invocation": 95,
    "script_execution": 100,
    "template_usage": 100,
    "reference_consultation": 100,
    "multi_skill_chaining": 95
  },
  "overall_score": 99
}
```

## Benchmark History

| Date | Agent | Score | Notes |
|------|-------|-------|-------|
| 2026-02-25 | Claude Code | 100% | Full discovery and execution capability |

## Contributing Benchmarks

To add benchmark results for a new agent:

1. Run both discovery and execution test suites
2. Record results in JSON format
3. Add a summary row to the test matrix above
4. Submit a pull request with the results and any agent-specific notes
