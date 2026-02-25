---
title: "How I Built an Open-Source Cybersecurity Skills Database for AI Agents (611+ Skills)"
published: true
tags: cybersecurity, opensource, ai, security
---

# How I Built an Open-Source Cybersecurity Skills Database for AI Agents (611+ Skills)

AI agents are transforming software engineering. Tools like Claude Code, GitHub Copilot, and Cursor can write code, debug issues, and refactor entire codebases. But ask one to analyze a memory dump from a compromised server, triage a SIEM alert, or assess an Active Directory attack path, and you get generic advice that no security practitioner would follow.

I built an open-source database of 611 cybersecurity skills structured for AI agent consumption. This post explains why, how, and what the skills actually look like.

## The Problem: AI Agents Lack Security Expertise

When a security analyst encounters a suspicious process on a compromised Windows host, they don't think in generalities. They immediately:

1. Check the process tree for parent-child anomalies
2. Run `vol3 -f memory.dmp windows.malfind` to detect injected code
3. Extract suspicious memory regions for YARA scanning
4. Cross-reference process network connections with known C2 indicators
5. Check for persistence mechanisms in registry run keys and scheduled tasks

An AI agent without structured security knowledge will tell you to "use a memory forensics tool" and "look for suspicious processes." That gap between generic advice and practitioner-level precision is the problem.

This isn't just about knowledge -- it's about structured, actionable knowledge. AI agents need to know not just WHAT to do, but WHEN to do it, WHICH specific tool to use, and in WHAT order.

## Why Existing Solutions Fail

| Approach | Problem |
|----------|---------|
| Training data (books, blogs) | Unstructured, no activation triggers, no tool-specific commands |
| RAG over documentation | Tool docs explain features, not workflows. No decision trees. |
| Prompt engineering | Doesn't scale. You can't encode 611 skills in a system prompt. |
| Fine-tuning | Expensive, needs retraining for every update, hard to audit |
| Wiki/cheat sheets | No machine-readable metadata, no activation conditions |
| Existing skill standards | Focused on human learning objectives, not agent execution |

What's needed is a format that gives AI agents two things:

1. **Routing information**: When should this skill activate? What keywords, domains, and contexts trigger it?
2. **Execution knowledge**: What exact commands, in what order, with what flags, and what to do when things go wrong?

## What agentskills.io Enables: Progressive Disclosure Architecture

Each skill follows a two-layer architecture that mirrors how human expertise works:

### Layer 1: YAML Frontmatter (The WHEN)

```yaml
---
name: analyzing-memory-dumps-with-volatility
description: >
  Analyzes RAM memory dumps from compromised systems using the Volatility
  framework to identify malicious processes, injected code, network
  connections, loaded modules, and extracted credentials.
domain: cybersecurity
subdomain: malware-analysis
tags: [malware, memory-forensics, Volatility, RAM-analysis, incident-response]
version: 1.0.0
author: mahipal
license: MIT
---
```

This frontmatter is what gets indexed. When a user asks an AI agent to "check this memory dump for malware," the agent matches against the description and tags, identifies this skill as relevant, and loads the full body.

### Layer 2: Markdown Body (The HOW)

The body contains the actual procedure:

- **When to Use / When Not to Use**: Clear activation and exclusion conditions
- **Prerequisites**: Specific tool versions, dependencies, required inputs
- **Step-by-Step Workflow**: Exact commands with flags, expected outputs, decision trees
- **Validation Steps**: How to verify results
- **References**: MITRE ATT&CK techniques, NIST controls, CVE numbers

The progressive disclosure is the key insight: the agent doesn't load 611 full skill bodies into context. It indexes the frontmatter, matches the right skill, and only then loads the detailed procedure.

## Skill Taxonomy: 24 Subdomains, 611 Skills

The database covers the full cybersecurity landscape:

| Subdomain | Skills | Example Skill |
|-----------|--------|---------------|
| Cloud Security | 48 | Auditing AWS S3 Bucket Permissions |
| Threat Intelligence | 43 | Building Threat Feed Aggregation with MISP |
| Web Application Security | 41 | Exploiting Server-Side Request Forgery |
| Threat Hunting | 35 | Hunting for C2 Beaconing with Frequency Analysis |
| Malware Analysis | 34 | Analyzing Memory Dumps with Volatility |
| Digital Forensics | 34 | Performing Timeline Reconstruction with Plaso |
| SOC Operations | 33 | Building Detection Rules with Sigma |
| Network Security | 33 | Configuring Suricata for Network Monitoring |
| Identity & Access Management | 33 | Implementing Privileged Access Management with CyberArk |
| OT/ICS Security | 28 | Detecting Modbus Protocol Anomalies |
| API Security | 28 | Testing API for Broken Object Level Authorization |
| Container Security | 26 | Scanning Container Images with Grype |
| Vulnerability Management | 24 | Prioritizing Vulnerabilities with CVSS Scoring |
| Red Teaming | 24 | Building C2 Infrastructure with Sliver Framework |
| Incident Response | 24 | Conducting Malware Incident Response |
| Penetration Testing | 23 | Performing Active Directory Penetration Test |
| Zero Trust Architecture | 17 | Implementing BeyondCorp Zero Trust Access Model |
| Phishing Defense | 16 | Detecting Business Email Compromise with AI |
| Endpoint Security | 16 | Detecting Fileless Malware Techniques |
| DevSecOps | 16 | Integrating SAST into GitHub Actions Pipeline |
| Cryptography | 13 | Implementing AES Encryption for Data at Rest |
| Mobile Security | 12 | Reverse Engineering Android Malware with JADX |
| Ransomware Defense | 5 | Implementing Ransomware Backup Strategy |
| Compliance & Governance | 5 | Implementing ISO 27001 Information Security Management |

## Quick Demo: How Claude Code Uses a Skill

Here's a realistic interaction showing how an AI agent uses a skill file:

**User prompt:**
> "I have a memory dump from a potentially compromised Windows server. Can you help me analyze it for malware?"

**Without skills:** The agent gives a generic overview of memory forensics concepts and suggests "using Volatility."

**With the skill loaded:** The agent follows the structured workflow:

```bash
# Step 1: Identify the OS profile
vol3 -f memory.dmp windows.info

# Step 2: List all processes and check for anomalies
vol3 -f memory.dmp windows.pslist
vol3 -f memory.dmp windows.pstree

# Step 3: Detect process injection / hollowing
vol3 -f memory.dmp windows.malfind

# Step 4: Check network connections for C2
vol3 -f memory.dmp windows.netscan

# Step 5: Extract suspicious DLLs
vol3 -f memory.dmp windows.dlllist --pid <suspicious_pid>

# Step 6: Scan with YARA rules
vol3 -f memory.dmp yarascan.YaraScan --yara-file malware_rules.yar

# Step 7: Extract credentials if needed
vol3 -f memory.dmp windows.hashdump
```

The agent knows the exact plugin names, the order of operations, what to look for in the output, and how to pivot based on findings. That's the difference between "use Volatility" and actually using Volatility.

## File Structure

Each skill follows a consistent directory structure:

```
skills/{skill-name}/
  SKILL.md          # Skill definition (YAML frontmatter + Markdown body)
  references/
    standards.md    # NIST, MITRE ATT&CK, CIS references
    workflows.md    # Detailed technical procedure reference
  scripts/
    process.py      # Practitioner helper script
  assets/
    template.md     # Filled-in checklist or report template
```

The entire repository is pure Markdown and YAML. No build system, no dependencies, no runtime. Any tool that can read files can use these skills.

## Call for Contributors

The database is MIT licensed and open for contributions. Here's where help is most needed:

**Underrepresented subdomains:**
- Mobile Security (12 skills) -- iOS and Android security testing, mobile malware analysis
- Ransomware Defense (5 skills) -- detection, response, recovery procedures
- Compliance & Governance (5 skills) -- SOC 2, HIPAA, PCI DSS, GDPR controls

**Skill improvements:**
- Add real-world edge cases to existing skills
- Update tool commands for latest versions
- Add detection rules (Sigma, YARA, Splunk SPL) where applicable
- Improve decision trees for ambiguous scenarios

**New skill areas:**
- AI/ML security (adversarial ML, model security)
- Supply chain security
- Election security
- Healthcare-specific cybersecurity

If you write runbooks or procedure documents for your security team, you already know how to write a skill. The format is intentionally simple.

**Repo:** [github.com/mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

The future of cybersecurity involves AI agents that understand the domain with practitioner-level depth. This database is a step toward making that real -- not by replacing security professionals, but by giving AI agents the structured knowledge to be genuinely useful assistants.
