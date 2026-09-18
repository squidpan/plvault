
# INPUT

## NOTE TYPE
Skill

## TEMPLATE
Skill Template

## TITLE
SRE Low Latency Monitoring and Alerting for Market Data Systems

## INPUT PROMPT ID
sre-pico-low-latency-monitoring-skill-vng1

## CATEGORY
SRE

## CONTEXT
Pico.net financial infrastructure, market data systems (e.g., Redline feed, ticker plant), and low latency trading environments where performance and reliability are critical.

## TOPIC
Monitoring, alerting, and observability for low latency market data systems

## SCOPE
- Grafana dashboards for real-time visibility
- Prometheus metrics collection and querying
- latency monitoring (microseconds to milliseconds)
- throughput and message rate tracking
- data loss detection and gap analysis
- alerting strategies and thresholds
- reliability and availability metrics (SLOs/SLIs)
- performance tuning and optimization
- correlation of system, network, and application metrics

## TEMPLATE PROPERTY VALUES
description: Monitoring and alerting strategies for low latency trading systems using Grafana and Prometheus, with a focus on reliability and data integrity.
source: chatgpt
tags:
  - sre
  - grafana
  - prometheus
  - monitoring
  - alerting
  - low-latency
  - market-data
created: 2026-04-17
last: 2026-04-17
status: draft

## OUTPUT STRUCTURE
- Generate one Skill note as the primary entry point
- Generate supporting notes:
  - Concepts (observability, latency, alerting)
  - Tools (Grafana, Prometheus)
  - Usecases (latency spike, data loss, throughput bottleneck)
  - Processes (monitoring workflow)
  - Runbooks (incident response for latency/data loss)
- Ensure Skill note links to all supporting notes
- Ensure supporting notes link back to the Skill where relevant

## OUTPUT INSTRUCTIONS
- Follow MASTER SKILL exactly
- Use templates as the source of truth for frontmatter
- Generate atomic notes where appropriate
- Add meaningful [[links]] between notes
- Avoid duplication across notes

## BODY INSTRUCTIONS
- Emphasize real-world SRE scenarios in trading environments
- Focus on low latency constraints and tradeoffs
- Include interview-relevant insights (what matters to SRE hiring managers)
- Highlight how monitoring helps detect and mitigate data loss
- Keep explanations concise, structured, and practical