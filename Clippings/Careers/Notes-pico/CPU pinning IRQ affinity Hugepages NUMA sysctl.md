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
Explain these UNIX topics: 
- CPU pinning / taskset
- IRQ affinity
- HugePages
- NUMA
- Kernel tuning (`sysctl`)

Perfect—this is **exactly the level Pico’s Quant team cares about**. You don’t need to be a kernel engineer, but you **must understand why these matter for low-latency systems**.

I’ll keep it:

- Clear
- Practical
- Interview-ready

---

# 🧠 1. CPU Pinning / `taskset`

## ✅ What it is

> CPU pinning binds a process or thread to a specific CPU core.

---

## 🔧 Example

taskset -c 2 ./inrush_process

👉 Runs process only on CPU core 2

---

## 🎯 Why it matters (VERY IMPORTANT)

- Prevents CPU switching (context switching)
- Improves **cache locality**
- Reduces latency jitter

---

## What CPU pinning ensures

> CPU pinning ensures that **latency-sensitive processes like feed handlers run on dedicated cores**, reducing context switching and improving performance consistency.

---

# 🔥 2. IRQ Affinity

## ✅ What it is

> Assigns hardware interrupts (like NIC interrupts) to specific CPU cores.

---

## 🔧 Example

echo 2 > /proc/irq/XX/smp_affinity

---

## 🎯 Why it matters

- Controls which CPU handles network packets
- Prevents:
    - Interrupt storms
    - CPU contention

---

## 💡 Key idea

> You can separate:

- NIC interrupts → CPU 1
- Application (InRush) → CPU 2

---

## IRQ affinity allows

> IRQ affinity allows control over which CPU processes network interrupts, helping isolate packet handling from application processing and reducing latency interference.

---

# 🧠 3. HugePages

## ✅ What it is

> Large memory pages (e.g., 2MB instead of 4KB)

---

## 🎯 Why it matters

- Reduces:
    - TLB misses
    - Memory lookup overhead

---

## 💡 In trading systems

- Used for:
    - High-throughput data processing
    - Low-latency apps

---

## HugePages - what does it do

> HugePages reduce memory management overhead and improve performance for applications processing large volumes of data, which is important in market data systems.

---

# 🔥 4. NUMA (Non-Uniform Memory Access)

## ✅ What it is

> System where CPUs have **local and remote memory**

---

## 💡 Key idea

- Accessing:
    - Local memory → fast
    - Remote memory → slower

---

## 🔧 Example

numactl --cpunodebind=0 --membind=0 ./app

---

## 🎯 Why it matters

- If process runs on CPU 0 but uses memory from CPU 1 → slower

---

## NUMA affects

> NUMA affects memory access latency, so binding processes to the same CPU and memory node improves performance in low-latency systems.

---

# 🔥 5. Kernel tuning (`sysctl`)

## ✅ What it is

> Adjusting Linux kernel parameters for performance

---

## 🔧 Example

sysctl -w net.core.rmem_max=26214400

---

## 🎯 What you tune

### Network buffers

- `net.core.rmem_max`
- `net.core.wmem_max`

---

### TCP settings

- `net.ipv4.tcp_tw_reuse`

---

### File descriptors

- `fs.file-max`

---

## 💡 Why it matters

- Prevent:
    - Packet drops
    - Buffer overflow
    - Connection issues

---

## Kernel tuning allows

> Kernel tuning allows optimization of network buffers and system limits to handle high-throughput, low-latency workloads typical in trading systems.

---

# 🔗 6. How ALL of this connects (THIS is GOLD)

NIC → IRQ → CPU → Process → Memory

---

## 🔥 What you’re doing:

- IRQ affinity → control packet handling
- CPU pinning → isolate process
- NUMA → ensure local memory
- HugePages → optimize memory
- sysctl → optimize kernel/network

---

# 💥 7. SRE-level explanation (USE THIS)

> These optimizations are used to reduce latency, minimize jitter, and ensure predictable performance in high-throughput systems like market data feed handlers.

---

# 🎯 8. If they ask “Do you have experience?”

## 💬 Say:

> While I haven’t directly configured all of these at a deep level, I understand their purpose in optimizing low-latency systems and how they impact CPU, memory, and network performance. I’ve worked closely with systems where these optimizations were critical and I’m comfortable troubleshooting within that environment.

👉 This is **perfect honesty + confidence**

---

# 🧠 One-line cheat sheet

- CPU pinning → lock process to core
- IRQ affinity → control packet handling CPU
- HugePages → faster memory
- NUMA → keep CPU + memory local
- sysctl → tune kernel/network

---

# 🚀 Final tip

If you say:

> “These are used to reduce latency and jitter in real-time systems like market data feeds”

🔥 You sound like **you belong there**

---

If you want:

- A **final 3-minute rapid drill before your interview**
- Or quick recap of EVERYTHING

Just say:  
👉 “final drill”