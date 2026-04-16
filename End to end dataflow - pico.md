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
[1] Exchange matching engine / publisher  
      | **raw** native exchange feed / **UDP multicast**
      v  
[2] Exchange handoff / venue port  
      | primary line + secondary line  
      v  
[3] Pico colo edge / venue access  
      |  
      |  captured / transported over PicoNet  
      v  
[4] PicoNet / low-latency backbone  
      |  
      |  market data crosses regional / client connectivity hops  
      v  
[5] Client colo / subscriber server NIC  
      |  
      |  packets hit NIC, IRQs, kernel buffers  
      v  
[6] InRush Ticker Plant  
      |  
      |  feed handling, sequencing, gap detection,  arbitrate prim v sec, book building
      v  
[7] RedlineFeed publisher / normalization layer  
      |  
      |  N0 feed, synthetic BBO, conflation, configurable depth, strip to multicast channels
      v  
[8] Embedded InRush on subscribing app server  
      |  
      |  local delivery / API bridge / republish to edge cache  
      v  
[9] Trading application / strategy / OMS / EMS  
      |  
      |  consumes quotes, trades, order book updates  
      v  
[10] Optional OEG / FIX / order execution path