
---

## type: tool  
categories: [[Sres]]  
tags: [grafana, monitoring, dashboards, observability]  
created: 2026-04-17  
source: chatgpt  
status: draft  
aliases: []

# Grafana

## Summary

- Visualization and observability platform
- Used to build dashboards from multiple data sources
- Commonly paired with [[sre-x/tools/prometheus]]

## Key Points

- Supports metrics, logs, and traces
- Integrates with multiple backends (Prometheus, Elasticsearch, CloudWatch)
- Central UI for system health visibility
- Enables alerting based on metric thresholds

## Interview Insights

- Grafana is NOT a data collector → it visualizes data
- Often sits on top of [[sre-x/tools/prometheus]] in SRE stacks
- Used during incident response for debugging
- Helps correlate signals across systems

## Real-World Usage

- Monitor API latency and error rates
- Visualize infrastructure metrics (CPU, memory, network)
- Track SLO compliance via dashboards

## Related Notes

- [[Grafana Dashboards]]
- [[Grafana Alerting]]
- [[sre-x/tools/prometheus]]
- [[Monitoring Systems]]

