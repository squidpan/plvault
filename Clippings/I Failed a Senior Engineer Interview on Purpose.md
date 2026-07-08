---
categories:
  - "[[Clippings]]"
title: "I Failed a Senior Engineer Interview on Purpose"
source: "https://medium.com/@noahblogwriter2025/71dd704cebea"
author:
  - "[[Noah Byteforge]]"
published: 2026-01-16
created: 2026-06-29
description: "You're reading for free via Noah Byteforge's Friend Link. Upgrade to access the best of Medium."
tags:
  - "clippings"
url: "https://medium.com/@noahblogwriter2025/71dd704cebea"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pVTDwYGTSX21uykbjaRErg.png)

> **Not a member of Medium? Read the full story for free: \[**[**Link**](https://medium.com/@noahblogwriter2025/71dd704cebea?sk=0915d2d3e237ca302324871c17045920)**\]**

The third round was the system design interview. The question was a classic: “Design a URL shortener.”

I had practiced this. I knew the script. I could talk about hashing algorithms, database schemas for fast lookups, handling custom URLs, and the trade-offs between Redis and Postgres for the hot path. I could draw the boxes for the load balancer, the application servers, and the distributed database. I could have given them the textbook “correct” answer.

Instead, I said:

“First, I’d ask why we’re building this. Is this a feature for paying customers, or an internal tool? Because if it’s internal, we don’t need a distributed database. We need a single SQLite file on a cheap VPS and a 50-line Go service.”

The interviewer, a principal engineer with a look of profound patience, blinked. “Assume it’s for a global user base, high availability, low latency.”

“Okay,” I said. “In that case, I wouldn’t build it at all. I’d pay a company like Bitly or Rebrandly a few hundred dollars a month and have their team worry about it. Our engineering time is more valuable.”

He smiled, but it was the kind of smile you give a clever child before telling them to answer the…

I spent the next forty minutes giving him the textbook answer he wanted. I drew the boxes. I talked about consistent hashing. I got the offer.

And I turned it down.

This isn’t a story about being a contrarian. It’s the story of a single interview that revealed a deep, uncomfortable truth about our industry: we’re often hiring for the ability to solve complex, hypothetical problems, while the real job is about having the judgment to avoid them entirely.

## The Autopsy of a “Correct” Answer

Why did my initial, pragmatic answer fail the interview, even though it was arguably the better business decision?

Because the system design interview, in its common form, isn’t a test of engineering judgment. It’s a performance. It’s a ritual where we pretend that every problem is a greenfield project with infinite resources, where the most complex technical solution is always the most impressive.

The “correct” answer to “Design a URL shortener” involves demonstrating your knowledge of:

- **Distributed Systems:** You’re expected to talk about sharding, replication, and consistency models.
- **Scalable Caching:** You need to discuss caching layers, eviction policies, and CDNs.
- **Algorithmic Nuances:** You should mention hash collisions and the trade-offs of different encoding schemes.

The subtext is clear: *Show me you can build the Google-scale version, even if the real job is maintaining a simple CRUD app.*

I realized that by playing along, I was validating a culture that celebrates complexity over simplicity. A culture that rewards building things over solving problems.

## The Counter-Intuitive Truth: Senior Engineering Is About Deletion

The journey from junior to senior engineer isn’t about learning more algorithms. It’s about learning what *not* to build.

- **A junior engineer** sees a problem and asks, “What code can I write to solve this?”
- **A mid-level engineer** asks, “What design pattern can I use to solve this elegantly?”
- **A senior engineer** asks, “Does this problem even need to be solved by us? Can we delete the feature? Can we buy a solution? Can we simplify the business process so the problem disappears?”

The most powerful engineering decision is often saying “no” to a new system. It’s the pull request that deletes 10,000 lines of code. It’s the architectural decision to use a managed, off-the-shelf service instead of building a bespoke one.

This mindset is almost impossible to test for in a standard interview loop. The interview process is optimized to measure addition, not subtraction. It filters for builders, not necessarily for editors.

## The Code I “Should” Have Written vs. The Code That Ships

Let’s be honest about the code that runs the world. It’s not always the “perfect” system design answer.

**The Interview Answer:** A globally distributed, multi-region, active-active service with a sophisticated caching layer and a custom sharding strategy.

**The Production Reality:** A surprisingly simple monolith running on two servers, with most of the “hard problems” outsourced to AWS services like S3, RDS, and Cloudflare.

The interview process selects for people who can design the first system. The actual job requires people who have the wisdom and restraint to build the second.

This disconnect creates teams that are brilliant at solving hypothetical scaling problems but struggle to ship simple features on time because they’re over-engineering the solution. They build systems that can handle a million requests per second, for a feature that gets a hundred requests a day.

## A Sanity Checklist for Your Next Interview (From Both Sides of the Table)

If you’re tired of the performance, whether you’re the interviewer or the candidate, here are a few ways to inject a dose of reality into the process.

**If you’re the candidate:**

1. **Answer the “Real” Question First.** Before you draw a single box, ask about the business context. “Who is this for? What’s the budget? What’s the team size? What’s the real-world success metric?” This demonstrates that you think like a business partner, not just a code generator.
2. **Present the “Boring” Solution.** Start with the simplest possible thing that could work. “For phase one, we could probably run this on a single server with SQLite. It would take a day to build and would validate if anyone even uses it.” This shows you value iterative development.
3. **Frame the “Complex” Solution as a Trade-off.** When you do present the big, scalable answer, frame it in terms of cost. “We *could* build a globally distributed system, but it would require a dedicated team of three engineers and a significant infrastructure budget. We should only consider this if we hit X million users.”
4. **Ask About Deletion.** Ask your interviewers: “Tell me about a time you decided *not* to build something, or when you deleted a major feature or service. What was the process like?” Their answer will tell you everything you need to know about their engineering culture.

**If you’re the interviewer:**

1. **Reward the “Why” Question.** If a candidate immediately starts drawing boxes without asking about the business context, it’s a red flag. The best candidates push back on the premise of the question first.
2. **Explicitly Ask for the “Boring” Solution.** Start the interview with: “First, describe the simplest, cheapest, and fastest solution that could possibly work, even if it doesn’t scale.” This tests for pragmatism.
3. **Frame the Problem with Real-World Constraints.** Instead of “Design Twitter,” try “You have a team of two engineers and a budget of $500 a month. You need to build a system for sharing internal company updates. What do you build?”
4. **Ask a “Deletion” Question.** “Tell me about a piece of code you’ve written that you’re most proud of, and then tell me about a piece of code you successfully argued to have deleted.” The second answer is often more telling.

I didn’t get that job because I failed the interview. I didn’t get it because I passed a different, more important test: I identified a company that valued the performance of engineering over the practice of it.

The real work of a senior engineer isn’t to have all the answers. It’s to ask the right questions. And the most important question is often, “Are we even solving the right problem?” The day I was willing to fail an interview to ask that question was the day I truly started thinking like a senior engineer.