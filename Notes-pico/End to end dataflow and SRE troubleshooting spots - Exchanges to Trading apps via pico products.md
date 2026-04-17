---
categories:
  - "[[Topics]]"
  - "[[Jobs]]"
url:
created: 2026-04-15
last: 2026-04-15
type:
tags:
  - nutshell
---
# Background
Diagram the entire data flow from the exchanges through Pico's Inrush ticker plant and redline feed to trading applications and point out potential troubleshooting spots?

---

Pico’s own material says InRush terminates market data from multiple feed sources, maintains full-depth books, and RedlineFeed is distributed from a Pico-managed publishing hub to each subscriber server using a locally embedded InRush instance. Pico also positions PicoNet as the low-latency transport layer and Corvil as the cross-hop analytics layer.

---
[[End to end dataflow - pico]]

## The same flow in plain English

The exchange sends the raw feed. Pico provides venue access and transport over PicoNet. That traffic lands on the client-side server NIC. **InRush** is the **first major software hop that turns packet flow into usable market data state**: it sequences messages, detects gaps, arbitrates primary vs secondary, and builds full-depth books. Then RedlineFeed normalizes and republishes the data so client apps can consume it easily. On subscriber servers, a locally embedded InRush instance delivers normalized updates via the InRush API or bridges, and can also republish subsets downstream.

---

# Where an SRE troubleshoots

Think of it as **five main layers**:
## 1. Venue / source layer
Questions:
- Is the exchange feed healthy?
- Is the primary line clean?
- Is the secondary line better?
- Are sequence gaps starting at source or later?

What you check:
- feed status dashboards
- primary vs secondary quality
- gap counts
- Corvil latency from exchange publisher

How to say it:

> First I’d verify whether the problem starts at the venue handoff or later in the client path by comparing primary and secondary feeds and looking at latency from the exchange publisher.

This lines up directly with Pico’s “check for gaps on incoming multicast feeds,” “monitor latency from the exchange publisher,” and “compare the overall quality of the primary and secondary feeds.”

---
## 2. Network transport / PicoNet layer

Questions:
- Is the path healthy?
- Is there congestion or packet loss between colo sites?
- Did latency jump on one hop?

Commands:
```
ping <host>  
traceroute <host>  
mtr <host>  
ss -i  
netstat -i

```
What you look for:
- path instability
- rising RTT
- dropped packets
- interface errors

How to say it:

> On the transport side I’d isolate whether there’s a network issue by checking connectivity, hop latency, and interface health before blaming the application.

Pico describes PicoNet as the ultra-low-latency, resilient network carrying market data and order traffic across major financial markets.

---

## 3. NIC / kernel / host layer

This is where a lot of low-latency issues hide.

Questions:

- Are packets hitting the box?
- Is the NIC dropping?
- Are interrupts concentrated on the wrong CPU?
- Are buffers too small?
- Is the host swapping or CPU-starved?

Commands:

```
ip -s link  
ethtool -S eth0  
cat /proc/interrupts  
top  
htop  
free -h  
vmstat 1  
dmesg | tail  
sysctl -a | egrep 'rmem|wmem|net.core|somaxconn'

```
What you look for:

- `rx_dropped`, `rx_errors`
- IRQ imbalance
- CPU saturation
- memory pressure
- kernel buffer exhaustion

How to say it:

> If packets are not cleanly entering the host, InRush never gets a complete stream, so I’d inspect NIC counters, interrupt distribution, and kernel/network buffers early in the investigation.

---

## 4. InRush ticker plant layer

This is the **core feed-handler troubleshooting zone**.

Questions:
- Is InRush running?
- Is it receiving both lines?
- Are there sequence gaps?
- Is arbitration between primary/secondary behaving?
- Is it building a correct order book?
- Is CPU or thread contention delaying processing?

Commands:
```
ps -ef | grep -i inrush  
top -H -p <pid>  
taskset -cp <pid>  
numactl --show  
tail -f /path/to/inrush.log  
grep -i 'gap\|sequence\|retrans\|snapshot\|primary\|secondary' /path/to/inrush.log  
lsof -p <pid>

```
What you look for:

- process up/down
- thread hot spots
- sequence gap messages
- retransmission or snapshot recovery events
- primary/secondary arbitration anomalies
- stale or broken book state

How to say it:

> InRush is where raw feed becomes market state, so I’d check whether it is receiving a complete ordered stream, whether gap recovery is working, and whether CPU or thread contention is affecting deterministic processing.

Pico’s brochure explicitly says InRush maintains full-depth books with emphasis on low latency and determinism.

---
## 5. RedlineFeed / normalization / subscriber delivery

Questions:

- Is the publishing hub healthy?
- Is the normalized feed correct?
- Is synthetic BBO or conflation configured appropriately?
- Is striping causing a missing-symbol issue?
- Is the subscriber’s embedded InRush receiving the expected multicast channels?
- Is downstream republish working?

Commands:

```
ps -ef | grep -i redline  
ss -ulpn  
netstat -g  
tail -f /path/to/redlinefeed.log  
grep -i 'bbo\|conflat\|strip\|channel\|snapshot\|recovery' /path/to/redlinefeed.log  
tcpdump -i eth0 udp and host <multicast_or_source>
```

What you look for:

- missing multicast group membership
- wrong symbol/channel mapping
- quote conflation causing apparent staleness
- snapshot recovery after line gaps
- normalization/publisher errors

How to say it:

> If the raw feed looks clean in InRush but the application still sees a problem, I’d move up to RedlineFeed and verify normalization, channel striping, snapshots, and subscriber delivery.

Pico says RedlineFeed is a publishing hub managed by Pico, delivered via embedded InRush on subscriber servers, with redundancy, snapshots, synthetic BBO, conflation, configurable depth, striping, and downstream republish.

---

# How to tie the commands to the hops

## Scenario: “Client says market data is delayed”

1. **Check whether it’s broad or isolated**
    - one symbol, one app server, one client, or many?
2. **Check network and host ingress first**

```
ip -s link  
ethtool -S eth0  
netstat -i  
cat /proc/interrupts  
top
```

If the NIC is dropping or one CPU is buried under interrupts, the delay may be before InRush.

3. **Check InRush**

```
ps -ef | grep inrush  
tail -f inrush.log  
grep -i 'gap\|primary\|secondary\|snapshot' inrush.log  
top -H -p <pid>
```

If you see gaps, arbitration issues, or CPU hot threads, the delay is likely in feed handling.

4. **Check RedlineFeed**

```
tail -f redlinefeed.log  
netstat -g  
ss -ulpn  
tcpdump -i eth0 udp

```
If raw feed is good but normalized delivery is stale or incomplete, look at multicast subscription, channel mapping, striping, conflation, and snapshots.

5. **Correlate in Corvil / Grafana**
    - packet arrival time
    - exchange publisher latency
    - feed handler latency
    - app delivery latency
    - order-trigger correlation if needed

Pico’s materials explicitly emphasize measuring missing data and latency across the infrastructure en route to trading strategies, identifying congested network hops or overloaded middleware, and correlating orders with the triggering tick.

---
# Two concrete failure examples

## Example 1: Broken order book

Symptom:

- best bid/ask doesn’t match reference

Likely hops:

- NIC drop
- InRush gap recovery failure
- primary/secondary arbitration issue

Commands:

```
ethtool -S eth0  
grep -i 'gap\|sequence\|retrans\|snapshot' inrush.log  
tcpdump -i eth0 -w suspect.pcap udp

```
How you explain it:

> An order book inconsistency usually means missing or out-of-order updates. I’d first rule out packet loss at the NIC, then confirm whether InRush detected and recovered any sequence gaps, and finally compare primary versus secondary line behavior.

---

## Example 2: App sees stale data but feed is “up”

Symptom:
- no outage, but prices are stale

Likely hops:
- RedlineFeed conflation setting
- wrong striping/channel assignment
- subscriber not joined to correct multicast groups
- embedded InRush issue on app server

Commands:
```
netstat -g  
ss -ulpn  
tail -f redlinefeed.log  
grep -i 'conflat\|channel\|symbol\|strip' redlinefeed.log
```

How you explain it:

> If the raw feed is healthy but the app sees stale updates, I’d inspect the normalization and subscriber-delivery layer for conflation behavior, striping mismatches, or multicast group subscription issues.

---

# Where PCAP fits in

If you cannot prove whether the issue is network-side or application-side, capture packets.

Commands:

```
tcpdump -i eth0 -s 0 -w capture.pcap udp  
tcpdump -r capture.pcap | head
```

Use PCAP when you need to answer:

- Did the packet reach the box?
- Was sequence integrity already broken on ingress?
- Did the issue start before or after InRush?

Pico’s historical-data material says they store raw packet data in compressed PCAP, replay it with the InRush injection utility or tcpreplay, and use it for time-accurate analysis and testing.

---

# The 30-second answer to say in the interview

> I think about the Pico market-data path in layers: exchange handoff, PicoNet transport, NIC and kernel ingress, InRush feed handling and book building, RedlineFeed normalization and multicast distribution, and then the client trading application. In troubleshooting, I start where packets enter the environment and move upward. I use NIC and kernel commands like `ethtool`, `ip -s link`, and `/proc/interrupts`, then application checks and logs for InRush and RedlineFeed, and finally correlate packet and application timing in Corvil or Grafana to isolate whether the issue is network, feed handler, normalization, or subscriber delivery.

If you want, I can turn this into a **one-page printable cheat sheet** for tomorrow morning.

please turn this into a one-page printable cheat sheet for tomorrow morning.

Here’s your **one-page Pico SRE cheat sheet** — designed to be skimmed in ~2–3 minutes before your interview.

---
---

# 🧠 PICO SRE – MARKET DATA FLOW & TROUBLESHOOTING CHEAT SHEET

---

# 🔗 END-TO-END DATA FLOW

Exchange → PicoNet → NIC → Kernel → InRush → RedlineFeed → App

---

# 🎯 LAYER-BY-LAYER TROUBLESHOOTING

---

## 🔵 1. EXCHANGE / SOURCE

**Check:**

- Primary vs secondary feed quality
- Missing data / gaps
- Latency from publisher

**Say:**

> First isolate whether issue starts at source or downstream.

---

## 🌐 2. NETWORK (PicoNet)

**Check:**

```
ping <host>  
traceroute <host>  
mtr <host>  
netstat -i
```

**Look for:**

- Packet loss
- High latency
- Path instability

**Say:**

> Verify transport health before blaming application.

---

## 🖥️ 3. NIC / OS / KERNEL

**Check:**

```
ip -s link  
ethtool -S eth0  
cat /proc/interrupts  
top  
free -h

```
**Look for:**

- RX drops / errors
- CPU saturation
- IRQ imbalance

**Say:**

> If packets don’t enter cleanly, everything upstream breaks.

---

## ⚙️ 4. INRUSH (FEED HANDLER)

**Check:**

```
ps -ef | grep inrush  
top -H -p <pid>  
tail -f inrush.log  
grep -i 'gap\|sequence\|snapshot' inrush.log
```

**Look for:**

- Sequence gaps
- Gap recovery events
- CPU bottlenecks
- Primary vs secondary arbitration

**Say:**

> InRush turns packets into order books—must be complete & ordered.

---

## 🟡 5. REDLINEFEED (NORMALIZATION)

**Check:**

```
netstat -g  
ss -ulpn  
tail -f redlinefeed.log  
tcpdump -i eth0 udp
```

**Look for:**

- Missing multicast groups
- Wrong channel/striping
- Conflation (stale data)
- Snapshot recovery

**Say:**

> If raw feed is good but app is wrong → check normalization layer.

---

## 🟢 6. APPLICATION

**Check:**

- Data latency
- Missing symbols
- Incorrect BBO / order book

**Say:**

> Validate against external reference to confirm issue.

---

# 🧠 CORE CONCEPTS (MUST SAY)

---

## 📡 Multicast

- One-to-many data delivery
- No guaranteed delivery → packet loss possible

---

## 📉 Packet Loss

- Missing packets → gaps → broken order book

---

## 🔁 Gap Recovery

- Retransmission
- Snapshot rebuild
- Primary/secondary failover

---

## 📊 Quotes vs Trades

- Quotes = intent (bid/ask)
- Trades = execution

---

## ⚡ Latency

- Exchange → NIC → InRush → App
- Must isolate where delay occurs

---

# 🔥 GOLDEN TROUBLESHOOTING FLOW

Packets → Network → NIC → InRush → Redline → App

---

# 💥 KEY SCENARIOS

---

## ❗ Latency Issue

Check in order:

1. Network latency
2. NIC drops
3. CPU load
4. InRush processing
5. Redline delivery

---

## ❗ Order Book Wrong

Check:

- Packet loss (`ethtool`)
- Gaps (`inrush.log`)
- Recovery (snapshot)
- Primary vs secondary

---

## ❗ Data Missing / Stale

Check:

- Multicast groups (`netstat -g`)
- Channel mapping
- Conflation settings

---

# 🧪 PCAP (WHEN TO USE)

tcpdump -i eth0 -w capture.pcap

Use to:

- Confirm packet arrival
- Detect gaps
- Debug at packet level

---

# 💬 FINAL INTERVIEW LINE

> I approach issues layer by layer—from packet ingress at the NIC, through network and kernel, into InRush feed handling, and finally Redline normalization and application delivery—to isolate where latency or data integrity issues occur.

---

# 🧠 5-SECOND MEMORY

- InRush = raw feed + order book
- Redline = normalized feed
- PicoNet = network
- Corvil = visibility
- Problem = latency OR packet loss OR misconfiguration

---

# 🚀 LAST MENTAL NOTE

👉 You don’t need perfect answers  
👉 You need **structured thinking**

---

If you want a **super fast confidence boost right before the interview**, I can give you a 60-second “tell me about yourself” tailored to Pico.