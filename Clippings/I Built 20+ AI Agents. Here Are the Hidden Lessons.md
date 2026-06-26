---
categories:
  - "[[Clippings]]"
title: "I Built 20+ AI Agents. Here Are the Hidden Lessons"
source: "https://medium.com/@vndpal/i-built-20-ai-agents-here-are-the-hidden-lessons-15c1b2130749"
author:
  - "[[Vinod Pal]]"
published: 2026-04-05
created: 2026-06-23
description: "A plain-English guide to the concepts behind every AI agent"
tags:
  - "clippings"
url: "https://medium.com/@vndpal/i-built-20-ai-agents-here-are-the-hidden-lessons-15c1b2130749"
---
## A plain-English guide to the concepts behind every AI agent

I spent the last year building AI agents for everything. Customer support. Code review. Data pipelines. Lead scoring. Content generation.

==Some agents worked great. Others crashed in ways I never expected. Along the way, I learned concepts that every developer needs to understand.==

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*vvjxUwYNuzwwHkFP_r1twg.png)

> *Non-medium members* [*click here*](https://medium.com/@vndpal/i-built-20-ai-agents-here-are-the-hidden-lessons-15c1b2130749?sk=d726448c1ec5284ccf3d99ad6eee07ae) *to read for free.*

## 1\. Sometimes You Want a Robot. Sometimes You Want a Poet.

I built a data extraction agent that pulled invoice numbers from PDFs. It needed to be exact. No creativity. No surprises. Just the right number, every time.

Then I also built a marketing copy agent. It needed flair. Personality. Unexpected word choices.

**Same model. Opposite needs.** The first agent kept “getting creative” with invoice numbers. The second agent kept writing boring, safe copy.

The fix? One single setting. Temperature.

## So, What Is Temperature?

Temperature controls how safe vs. creative an AI’s answers are.

0 = Very predictable

0.5 = Balanced between predatibilty and creativity

1= Very creative

**Temperature 0:** *“Give me a black coffee. No milk. No sugar. The same one I get every day.”* The AI picks the most likely word every single time. Predictable and reliable.

**Temperature 1:** *“Surprise me. Something wild.”* The AI takes risks. It picks less obvious words. Creative. Unexpected. Sometimes a mess.

Here’s how different that one setting looks in code:

```hs
# Invoice agent: I need the EXACT number. No creativity.
invoice_agent = openai.chat.completions.create(
    model="gpt-4",
    temperature=0,        # Robot mode: same input = same output
    messages=[{"role": "user", "content": "Extract invoice number from this PDF"}]
)

# Copywriting agent: I need fresh, surprising copy.
copy_agent = openai.chat.completions.create(
    model="gpt-4",
    temperature=0.8,      # Poet mode: take creative risks
    messages=[{"role": "user", "content": "Write a tagline for our new sneaker"}]
)
```

For my invoice agent, I set the temperature to 0. It stopped improvising numbers.

For my copywriting agent, I cranked it to 0.8. It started writing lines that surprised me.

**Most agent failures I’ve seen come from using the wrong temperature.** Precision tasks need a robot. Creative tasks need a poet. The dial decides which one shows up.

## 2\. Memory Is the Hardest Problem

Most agent tutorials skip memory. Or they throw in a vector database and call it done.

Real memory is brutal. Handle contradictions in user statements. Adjust when their views change over time.

I burned two full weeks on memory for a single agent. Then I decided to use RAG. It solves the memory problem. It still isn’t perfect.

## So, What Is RAG?

Retrieval-Augmented Generation. Big words. Simple idea.

You ask a friend for directions.

Friend A: *“As far as I remember, you should turn left from the big tree.”*

Friend B: *“Let me check the map…Yes, first take right from the river, then take left from the big tree near the theatre.”*

RAG is Friend B.

Here’s the flow:

![](https://miro.medium.com/v2/resize:fit:1182/format:webp/1*GxOP5xSQZpGqOji6wRKAcg.png)

The AI doesn’t try to remember everything. Instead, it searches a knowledge base. Pulls the relevant info and generates an answer using that info.

**Without RAG:** *“Generally return polices are 30 days, yours should be the same”* (a guess)

**With RAG:** *“Your return policy is 14 days for electronics and 30 days for clothing, as per section 4.2 of your policy doc.”* (a fact)

That’s it. Search first, answer second. That’s RAG.

## 3\. Tools Break in Boring Ways

Giving an agent access to tools sounds exciting. Call APIs! Query databases! Send emails!

In practice, every tool needs its own integration. Notion has one API format. Slack has another. Gmail has a third. Each one needs custom auth, custom parsing, and custom error handling.

**I spent more time writing glue code than writing agent logic.**

Every new tool meant a new integration from scratch. Same boilerplate. Different API docs. It didn’t scale.

This is the exact problem MCP was built to solve.

## So, What Is MCP?

MCP stands for Model Context Protocol. Think of it as a universal adapter.

Your phone charger uses USB-C. One cable, every device. Before USB-C, you needed a different cable for every phone brand. Chaos.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pDUxUx4EaaeLoRjFZwNUgA.png)

Before MCP, if your agent needed to talk to Notion, Slack, and Gmail. You wrote three separate integrations. Each has its own format. Each is breaking in its own way.

With MCP, every tool speaks the same language. Your agent connects to an MCP server, and that server handles the messy details.

**One protocol. Any tool. Plug and play.** That’s MCP.

## 4\. Users Don’t Trust AI Agents (And They Shouldn’t)

I once shipped a support agent who resolved almost 80 percent of all the user queries. The team still didn’t trust it.

They checked every response. They overrode correct answers. They escalated the tickets that the agent had already solved.

Trust takes time. I learned to **start agents in “copilot mode”** before making them autonomous. Let humans watch the agent get things right, over and over.

## Human-in-the-Loop

The agent does the work. A human reviews it before it goes out. Over time, as trust builds, you loosen the leash.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*C3YM4BFd-i3NWlli_CG0Rw.png)

But the control is always there. **Full autonomy sounds cool. Supervised autonomy actually works in production.**

## 5\. Guardrails Are Not Optional

One of my early agents went rogue during a demo. A customer asked a product question. ==The agent started giving legal advice==.

I assumed the system prompt would keep it in line. It didn’t.

System prompts are suggestions, not fences.

## Hallucinations Are Real

You know how AI chatbots sometimes just… make stuff up? That’s called hallucination.

There was this lawyer in New York who used AI to do his legal research. It handed him court cases, complete with judge names and rulings.

Problem? Every single one was fake. Made up out of thin air. And he submitted it to the ==real court== without even checking it once.

They fined him $5000.

The model generates text that sounds right but is completely wrong. It’s not lying on purpose. It’s a pattern-completion machine. It completes the pattern even when it shouldn’t.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2IQJHyWByPOpWeVQTCcuaQ.png)

**Guardrails exist because hallucinations aren’t a bug. They’re a feature of how language models work.**

You can reduce them. You can’t eliminate them.

## 6\. One Agent Can’t Do Everything. Build a Workflow.

I once tried to build a single agent that handled an entire hiring pipeline. It screened resumes, sent emails, scheduled interviews, and scored candidates.

I didn’t go well. Context windows overflowed. The agent forgot instructions mid-task.

So I broke it apart. One step per agent. Connected them in sequence. Everything started working. This is where I discovered complex AI workflows.

## What Is AI Workflow Anyway?

In a car factory, no single worker builds an entire car. One team welds the frame. Another paints it. Another installs the engine. Each station does one thing well, then passes the car to the next station.

An AI workflow is that assembly line.

Instead of asking one AI agent to do all 10 things. You break it down into many smaller pieces. You form a chain of all those pieces. Each piece has a clear input, a simple job, and a clear output.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*z3nt89FxCNWiX6PfVOs1WQ.png)

Each step can use a different model, or even a different tool. The workflow engine connects them all.

**A single all-in-one agent sounds elegant. A workflow of focused steps actually works.**

Tools like n8n, LangChain, and CrewAI exist because this pattern wins every time.

## 7\. Orchestration > Individual Agent Quality

Once you have multiple agents, the challenge shifts. It’s no longer about making one agent smart. It’s about making them work together.

Which agent handles the request? How do they pass context? What happens when two agents disagree?

I spent more time on orchestration than on any single agent. Routing logic and context handoffs matter more than any individual prompt.

## So, What Is Agent Orchestration?

Think of a restaurant. You have a chef who creates salads. Then one who works with bread. Another one who cooks meat. Then a saucier. Each one is great at their job.

But without the head chef, everything falls apart. The main dish comes out before the starter. Dessert shows up with the appetizer.

Agent orchestration is the head chef.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ejzJ6icx4XCnraiZJznfng.png)

It decides which agent handles each task. It passes context between agents. It makes sure the final output makes sense as a whole.

One smart agent is useful. Five smart agents without orchestration is chaos. The orchestrator is what turns individual agents into a team.

## 8\. The Agent Doesn’t Need to Be Smart. It Needs to Know When It’s Dumb.

The best AI agents that I have built are not the ones that gave all the answers. They are the ones who fail gracefully if they don’t know something.

==Users forgive uncertainty. They don’t forgive confident wrong answers.==

Build escalation paths**.** Teach the agent to recognize its own limits. A graceful handoff to a human beats a hallucinated response every time.

## So, What Is a Confidence Score?

When an AI gives you an answer, it also has an internal sense of how sure it is. That’s the confidence score.

A high score: *“I’m 95% sure this is right.”* Ship it.

A low score: *“I’m 40% sure. Could be wrong.”* Flag it. Send it to a human.

```hs
def handle_response(agent_answer, confidence):
if confidence > 0.85:
        return send_to_user(agent_answer)
    elif confidence > 0.50:
        return flag_for_review(agent_answer)
    else:
        return escalate_to_human(
            "I'm not confident enough to answer this. "
            "Let me connect you with someone who can help."
        )
```

Smart agents don’t just generate answers. They know when to fold.

You can build an AI agent in a weekend. But building a reliable and production-grade AI agent takes months of effort.

The models keep getting better. But the hard problems aren’t model problems. They’re engineering problems. Memory. Cost. Trust. Orchestration.

> Stop picking better models. Start building better systems. That’s the only shortcut that exists.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xcaO-UTYUd0iFM5fVVl_ug.png)