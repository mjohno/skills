---
name: collect
description: Gathers resources, landscape scans, and competitive data. Use when you need to collect information from multiple sources into a structured resource inventory.
metadata:
  category: extract
---

# collect

Goal: Gather resources, landscape scan, and competitive data from multiple sources into a structured resource inventory.
Non-Goals: Analyzing data, writing final reports, or making recommendations.
Use-When: You need to collect information from multiple sources into a structured resource inventory.

## 0. Prerequisites
- Clear topic or domain to research
- User provides or confirms research scope and targets

## 1. Inputs
- Research topic and scope (from user)
- Target sources (URLs, databases, repositories, or domains)

## 2. Processes
1. Parse user prompt to extract topic, scope, and target sources
2. Fetch content from each source (web, repos, docs)
3. Deduplicate and normalize findings
4. Structure into resource inventory with metadata (title, source, type, summary, URL)

## 3. Outputs
- Structured resource inventory in the prompt (title, source, type, summary, URL per entry)
- If user specifies an output file, write to that path instead

## 4. Next Steps
- `analyze` — find patterns, contradictions, gaps in collected resources
- `ideate` — generate solutions from collected resources
- `define` — frame problem from collected resources

## 5. Examples

### Example 1: Landscape scan

**Prompt:** Collect resources about zero-trust architecture for a mid-size SaaS company.

**Outcome:** Prompt output with 15+ entries covering NIST docs, vendor whitepapers, and case studies.

### Example 2: Competitive data

**Prompt:** Gather competitive intelligence on project management tools for remote teams and save to `competitive.md`.

**Outcome:** `competitive.md` with feature comparison data, pricing, and user reviews from 8 competitors.
