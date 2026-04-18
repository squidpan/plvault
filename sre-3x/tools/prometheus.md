
---

## type: tool  
categories: [[Sres]]  
tags: [prometheus, monitoring, metrics]  
created: 2026-04-17  
source: chatgpt  
status: draft  
aliases: []

# Prometheus

## Summary

- Metrics collection and alerting system
- Stores time-series data
- Primary data source for [[sre-3x/tools/grafana]]

## Key Points

- Pull-based metrics scraping model
- Uses PromQL for querying data
- Stores metrics in time-series database
- Supports alerting rules

## Interview Insights

- Prometheus collects → Grafana visualizes
- Key differentiation:
    - Prometheus = backend
    - Grafana = frontend
- Widely used in Kubernetes environments

## Real-World Usage

- Collect application metrics
- Monitor infrastructure health
- Feed dashboards in [[sre-3x/tools/grafana]]

## Related Notes

- [[sre-3x/tools/grafana]]
- [[Monitoring Systems]]
- [[sre-x/concepts/observability]]

