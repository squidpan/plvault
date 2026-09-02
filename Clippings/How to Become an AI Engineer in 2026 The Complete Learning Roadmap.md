---
categories:
  - "[[Clippings]]"
title: "How to Become an AI Engineer in 2026: The Complete Learning Roadmap"
source: "https://code.likeagirl.io/how-to-become-an-ai-engineer-in-2026-the-complete-learning-roadmap-d21e5748a0aa?sk=9c05bf5ba27cc53294520790c61299d1"
author:
  - "[[Chandana]]"
published: 2026-07-22
created: 2026-08-28
description: "Whether you’re starting from scratch or transitioning from software engineering, here’s a structured roadmap to learn the skills companies actually expect from AI Engineers in 2026 - is published by Chandana in Code Like A Girl."
tags:
  - "clippings"
url: "https://code.likeagirl.io/how-to-become-an-ai-engineer-in-2026-the-complete-learning-roadmap-d21e5748a0aa?sk=9c05bf5ba27cc53294520790c61299d1"
---
very week, I receive messages that sound something like this:

**_How do I become an AI engineer?_**

The problem isn’t that there aren’t enough roadmaps, courses, or videos.

It’s that most of them were created before **AI Agents, Model Context Protocol (MCP), Context Engineering, and production LLM systems** became the skills companies actually hire for.

Today, even entry-level AI engineering roles expect you to understand concepts like **Retrieval-Augmented Generation (RAG), embeddings, vector databases, structured outputs, and agentic workflows**.

After mentoring learners, interviewing for AI roles, building production AI applications, and spending countless hours figuring out what actually matters, I decided to put everything into one roadmap. (_finally_)

Whether you’re:

- a **student starting from scratch,**
- a **software** **engineer transitioning into AI,**
- or an **AI engineer looking to level up,**

This roadmap is designed to help you learn the skills that matter in 2026. It differs very much from what mattered five years ago.

Let’s get started.

### AI Has Changed Faster Than Most Roadmaps

Most **AI roadmap** content on the internet is a Machine Learning Roadmap from 2019 with **LLM** pasted on top as an afterthought chapter.

It might work for a fresher or a beginner, but for an experienced engineer, much more is expected.

### What is expected from an AI Engineer Today?

In 2026, being an AI Engineer means something noticeably different from what it did even two years ago: (_if you’re already in the industry, you might’ve realised this_)

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*XsuNPPIQUDHGlOg18KYBCg.png)

image by author

### Should we be afraid of AI?

Do you need to be afraid that AI would take away the jobs in tech? My honest answer is no, if you try to keep trekking with it.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*XYSYTDDoJBfFAdfZ.png)

image by author

Because 3–4 years ago, there was not even a single prompt engineering job _(trust me)_, but look how many jobs are clustered around prompt engineering these days!

So if you’re going to spend months learning this kind of stuff, you deserve a roadmap that reflects what teams are actually hiring for right now, not a relic. That’s what this is.

> _Don’t chase tools. Build engineering fundamentals._

### ==Disclaimer: Before You Learn AI, Learn to Build Software==

Yes, I’ll say the unpopular part first.

Let me be frank: you are not going to skip straight to “**_I fine-tune LLMs for a living, build AI agents”_** by watching a weekend of YouTube videos about transformers.

Behind every AI Engineer I respect, the ones who’re actually shipping things, not just posting about them, is a solid software engineer underneath. They can:

- **Read a stack trace or understand a new one without panicking**
- **Write code that someone else (or future-them) can actually understand and maintain**
- **Use git like a tool**
- **Reason about what happens when 10,000 requests hit their endpoint instead of 1 _(for an experienced dev)_**

> **_AI Engineers are software engineers first._**

**Note**:

- For every phase concept, I tagged the respective resources (both the video tutorials and the reading guides, and relevant projects wherever required).
- Start with whatever best suits you. Always, the best way to learn is to put it into practice.

Let’s get into it!

## Phase 1: Python, Git, and Programming Fundamentals

> Already comfortable with Python? Skip to Git, virtual environments and debugging.

This is where **Python for AI** actually starts.

I spent months consuming tutorials before I realised implementation teaches far more than passive learning.

Only when I started practising DSA and implementing algorithms did I start to think clearly and see a dramatic improvement.

So my suggestion is, be fluent enough in plain Python or any programming language of your choice, like C++ _(if it’s easy for you for DSA to start with, but remember you might need to shift to Python later :))_

**Python** makes the AI-specific libraries stop feeling like an alien language. _(you’ll feel it later)_

Here’s what to actually get comfortable with:

### 1. Core Python

Data structures (lists, dicts, sets), functions, classes, list/dict comprehensions, generators, decorators (you’ll see these everywhere in AI frameworks)

### Resources 💻

- [**CS50’s Introduction to Programming with Python | Harvard University**](https://pll.harvard.edu/course/cs50s-introduction-programming-python)
- [**The Complete Python Bootcamp From Zero to Hero in Python**](https://www.udemy.com/course/complete-python-bootcamp/?srsltid=AfmBOoqt5mK3fr2V8flW7wbm0wqPJ8gZ2-KINfkwLgP88F2RP_7MIMs9&couponCode=25BBPMXNVD35) (best for certification)

Spend the least amount of time choosing the best resource and start with one.

I suggest you get started with a course or video. Once you gain a basic understanding, start doing DSA problems on platforms like [**LeetCode**](https://leetcode.com/problemset/?language=Python) , and improve on it.

### 2. Virtual environments & package management

`venv`, `pip`, and increasingly `uv.`you will waste hours of your life on dependency conflicts if you skip this!

- [**Git & GitHub:**](https://medium.com/the-tech-trek-by-tech-chick/git-isnt-hard-we-just-learnt-it-wrong-f52f04e90980?sharedUserId=theipocmwanderer) branches, commits, pull requests, resolving merge conflicts without crying. _(_[**_You don’t need to memorise_**](https://medium.com/the-tech-trek-by-tech-chick/git-isnt-hard-we-just-learnt-it-wrong-f52f04e90980?sharedUserId=theipocmwanderer)_; start implementing as you do and it becomes a practise)_
- [**Working with files & data:**](https://www.w3schools.com/python/python_file_handling.asp) reading/writing JSON, CSV, and plain text, since this is 80% of what **data** looks like before it becomes a fancy dataframe
- [**The terminal:**](https://www.codecademy.com/article/command-line-commands) basic bash, navigating directories, piping commands together
- [**Debugging:**](https://code.visualstudio.com/docs/debugtest/debugging) actually try reading the error message before pasting it into a chatbot. Try debugging with tools in whatever IDE you’re building in, too, e.g., breakpoints in VS Code. _(also, print statements are a saviour)_

A trap a lot of beginners fall into here is treating this phase as **_watching tutorials until it clicks_**. But it won’t click from watching alone. It clicks from typing, resolving, and doing it in a loop.

### Hands-on Time: Your First Real Project 🎯

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*NH7RNLYBeLKmU0OeSqIYNA.png)

[https://pybegin.pages.dev/](https://pybegin.pages.dev/)

Start with a simple project like BMI Calculator, Sudoku, or Tic-tac-toe to hone your beginner skills, and then build something with actual data or a real problem in it, something like:

- A CLI tool that scrapes and cleans data from a public API and saves it to a structured file
- A small script that parses your own bank statement CSV or Spliwise exports and categorizes spending
- A simple web scraper + data cleaner for a dataset you’re personally curious about

The goal of this project is less on output and more on forcing yourself through the unglamorous things like: malformed data, off-by-one errors, an API that changes its response shape halfway through your script.

You may use [this resource](https://pybegin.pages.dev/) for exploring beginner-friendly to real world project ideas

**Note**: Whatever math you are going to learn below in Phase 2, try to implement it through code. That way you’ll learn about what libraries to use and when to use them.

## Phase 2: The Math That Actually Matters

People get scared of AI by math way more than they should. We do not need all of linear algebra to start, but a specific, small slice of it. _(You can always expand on top of it !)_

### 1. Linear Algebra

- Vectors, matrices, tensors, and what multiplying them actually _does_ geometrically
- Dot products, matrix multiplications, eigenvalues, and vectors _(you’ll meet these again immediately in attention mechanisms and embeddings)_

### Resources 💻

[

## 3Blue1Brown

### Mathematics with a distinct visual perspective. Linear algebra, calculus, neural networks, topology, and more.

www.3blue1brown.com



](https://www.3blue1brown.com/?topic=linear-algebra&source=post_page-----d21e5748a0aa---------------------------------------)

**If you love learning with illustrations:**

[

## Introduction to Linear Algebra for Applied Machine Learning with Python

### Linear algebra is to machine learning as flour to bakery: every machine learning model is based in linear algebra, as…

pabloinsente.github.io







](https://pabloinsente.github.io/intro-linear-algebra?source=post_page-----d21e5748a0aa---------------------------------------)

### 2. Calculus

Most of us might’ve studied it all in high school. But here are the main topics and resources that might help you brush up on your concepts.

- Precalculus, Differential Calculus, Integral Calculus, Multivariate Calculus
- Derivatives, and specifically the idea of a gradient.

### Resources 💻

[

## 2.4. Calculus — Dive into Deep Learning 1.0.3 documentation

### For a long time, how to calculate the area of a circle remained a mystery. Then, in Ancient Greece, the mathematician…

d2l.ai







](https://d2l.ai/chapter_preliminaries/calculus.html?source=post_page-----d21e5748a0aa---------------------------------------)

[

## The Matrix Calculus You Need For Deep Learning

### Most of us last saw calculus in school, but derivatives are a critical part of machine learning, particularly deep…

explained.ai



](https://explained.ai/matrix-calculus/index.html?source=post_page-----d21e5748a0aa---------------------------------------)

### 3. Probability & Statistics

- Distributions, mean/variance, conditional probability
- This is the actual language that the model outputs, uncertainty, and evaluation metrics are written in.

### Resources 💻

[

## 2.6. Probability and Statistics — Dive into Deep Learning 1.0.3 documentation

### One way or another, machine learning is all about uncertainty. In supervised learning, we want to predict something…

d2l.ai







](https://d2l.ai/chapter_preliminaries/probability.html?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Probability & Statistics for Machine Learning & Data Science

### Offered by DeepLearning.AI. Newly updated for 2024! Mathematics for Machine Learning and Data Science is a foundational…

www.coursera.org



](https://www.coursera.org/learn/machine-learning-probability-and-statistics?source=post_page-----d21e5748a0aa---------------------------------------)

**4. Optimization**

- Gradient descent, learning rates, loss functions, the mechanism that turns **_wrong_** _into_ **_less wrong_** over time

### Resources 💻

[

## 12. Optimization Algorithms — Dive into Deep Learning 1.0.3 documentation

### To do well, however, some deeper knowledge is required. Optimization algorithms are important for deep learning. On the…

www.d2l.ai







](https://www.d2l.ai/chapter_optimization/?source=post_page-----d21e5748a0aa---------------------------------------)

**Fun fact:** _I loved doing sudoku since my 8th standard and couldn’t stop being in awe of mathematics since I began applying probabilities. (I used to hate math so much before that)_

> **_Note_**_: Do not overwhelm yourself and do not go too deep into it._

**If you’re still wondering where all the math becomes necessary:**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*h0hs05MB4gwnUup-Pqmhgg.png)

image by author

### Tools to work with data

- Learn popular libraries like Pandas and NumPy for data manipulation and analysis.
- Check data visualization tools like Matplotlib and Seaborn. _(Start with matplotlib; it’s easier)_

### Resources 💻

[

## Introduction to Pandas and NumPy | Codecademy

### pandas and NumPy are very useful libraries in Python. Let’s learn how to use them!

www.codecademy.com



](https://www.codecademy.com/article/introduction-to-numpy-and-pandas?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Research Guides: D-VELOP: Data Visualization using Python (Matplotlib and Seaborn)

### Includes workshop recordings and resources from past D-VELOP sessions.

guides.lib.purdue.edu







](https://guides.lib.purdue.edu/d-velop/data-viz/python1?source=post_page-----d21e5748a0aa---------------------------------------)

**Data Visualization can expand thinking and storytelling horizons:**

[

## What Data Reveals About Crimes Against Women in India?

### Have we ever wondered WHY these crimes keep happening, instead of just ACCEPTING that they do?

medium.com



](https://medium.com/data-kedavra/what-data-reveals-about-crimes-against-women-in-india-42c88c84f143?source=post_page-----d21e5748a0aa---------------------------------------)

### Hands-on Time: Build Linear Regression From Scratch 🎯

This is the highest-leverage exercise in this entire roadmap, and most people skip it because it feels too basic. Don’t skip it.

import numpy as np  
class LinearRegressionScratch:  
    def __init__(self, learning_rate=0.01, n_iterations=1000):  
        self.learning_rate = learning_rate  
        self.n_iterations = n_iterations  
        self.weights = None  
        self.bias = None  
    def fit(self, X, y):  
        n_samples, n_features = X.shape  
        self.weights = np.zeros(n_features)  
        self.bias = 0  
        for _ in range(self.n_iterations):  
            y_pred = np.dot(X, self.weights) + self.bias  
            # Gradients  
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))  
            db = (1 / n_samples) * np.sum(y_pred - y)  
            # Update  
            self.weights -= self.learning_rate * dw  
            self.bias -= self.learning_rate * db  
    def predict(self, X):  
        return np.dot(X, self.weights) + self.bias

Once this runs and produces compare it against `sklearn.linear_model.LinearRegression` on the same data.

When the numbers roughly match, you’ve just proven to yourself that you understand what’s happening under the hood of every model you’ll touch from here on.

Whenever you encounter similar techniques, try implementing the algorithm under the hood to understand it better.

> _Libraries might make it all easy, but it’s improtant to know the algorithm and math behind._

## Phase 3: Classical Machine Learning

Before you touch a neural network, you need to be familiar with the classical stuff like this because a huge share of real-world ML problems are still solved better and cheaper with these methods than with a deep learning model.

Understand why we use certain techniques over others, and how it solves a problem.

### Core topics

- **Supervised learning:** regression, classification, decision trees, random forests, gradient boosting (XGBoost/LightGBM)
- **Unsupervised learning:** clustering (k-means), dimensionality reduction (PCA)
- **Model evaluation** : train/test splits, cross-validation, precision/recall/F1, ROC-AUC, and critically knowing _which_ metric actually matters for a given business problem
- **Feature engineering:** this is the skill that determines whether your model is good or mediocre
- **scikit-learn** fluency, pipelines, preprocessing, model selection

### Resources 💻

**My friend introduced me to this course _(i loved how simple, interactive, and easy to understand this is, thankful to him)_:**

[

## Machine Learning | Google for Developers

### Google’s fast-paced, practical introduction to machine learning, featuring a series of animated videos, interactive…

developers.google.com



](https://developers.google.com/machine-learning/crash-course?source=post_page-----d21e5748a0aa---------------------------------------)

**If you want to go in depth:**

**I also used this Udemy course that covered all the above phases’ concepts:**

[

## Machine Learning A-Z [2026]: ML, DL, AI with AWS, Python & R

### Interested in the field of Machine Learning? Then this course is for you! This course has been designed by two AI &amp…

www.udemy.com



](https://www.udemy.com/course/machinelearning/?srsltid=AfmBOorIeDnIodsKHBXqjEGnqUWiUVrjuSbC7Pu4o_YBr31hw-XGJvRD&couponCode=UDEAFFHP22025&source=post_page-----d21e5748a0aa---------------------------------------)

### P[ortfolio Project #1: Customer Churn Prediction](https://www.geeksforgeeks.org/machine-learning/python-customer-churn-analysis-prediction/) 🎯

This project is a rite of passage for all for a reason: it forces you through the full lifecycle we get to see in the real world:

From messy tabular data, class imbalance, feature engineering, model comparison, to business-relevant evaluation _(a false negative here literally costs the company a customer)._

Here’s what a strong version of this project includes:

- A clear write-up of **_why_** you chose your evaluation metric (accuracy is almost always the wrong answer for churn)
- At least two model comparisons, not just “_I used XGBoost because it’s popular_”
- **Explainability**: SHAP values, confusion matrix, or feature importances, so you can say _why_ the model predicts what it predicts

### [Portfolio Project #2: Recommendation Systems](https://www.kaggle.com/discussions/general/231001) 🎯

This project teaches you to think in terms of _similarity,_ a concept you’ll lean on constantly once you get to embeddings and RAG later in this roadmap.

Build a simple content-based or collaborative-filtering recommender (movies, books, or products work well as datasets).

The point is to internalize the _idea_ of **_representing_** **_items_** as **vectors** and **_measuring distance_** between them, because that exact idea resurfaces in Phase 5 too.

I personally worked on the bookstore recommendation system, and the beginner learnings were very helpful in deciding what approach worked and what didn’t.

### For more projects 🚀

[

## 100+ Machine Learning Projects with Source Code — GeeksforGeeks

### Your All-in-One Learning Portal: GeeksforGeeks is a comprehensive educational platform that empowers learners across…

www.geeksforgeeks.org



](https://www.geeksforgeeks.org/machine-learning/machine-learning-projects/?source=post_page-----d21e5748a0aa---------------------------------------)

## Phase 4: Deep Learning

This stage actually decided if **Deep Learning** is for you. It’s where a lot of self-taught beginners or engineers either fall in love with the field or bounce off learning just the basics.

> Whatever it is, I suggest giving it a genuine shot before deciding which one you are!

### Core topics

- **Neural network fundamentals**: layers, activation functions, forward/backward pass
- **Training dynamics:** overfitting, regularization, dropout, batch normalization
- **Optimizers**: SGD, Adam, and why the choice actually matters in practice
- **GPUs:** not the theory, just enough to stop being confused about why your laptop is on fire when you run a billion-parameter model!

### Resources 💻

[

## Practical Deep Learning for Coders — Practical Deep Learning

### A free course designed for people with some coding experience, who want to learn how to apply deep learning and machine…

course.fast.ai



](https://course.fast.ai/?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Deep Learning A-Z [2026]: DL, AI in Python & AWS + LLM Prize

### Welcome to Deep Learning A-Z!

www.udemy.com



](https://www.udemy.com/course/deeplearning/?srsltid=AfmBOorGS0v7GCGvXxbt0WZignWFBqn435O18KyBJQRylrgbUveJ0gZl&source=post_page-----d21e5748a0aa---------------------------------------)

[

## Deep Learning with Python, Third Edition

### Deep Learning with Python is written for anyone who wishes to explore deep learning from scratch. This new edition adds…

deeplearningwithpython.io



](https://deeplearningwithpython.io/chapters/?source=post_page-----d21e5748a0aa---------------------------------------)

**To learn it in a fun way:** _(found his methodology intriguing)_

### Wait…PyTorch Or TensorFlow?

This is a genuinely fair question asked by every beginner, and it deserves a straightforward answer:

**PyTorch** has effectively become the default for **research**, for most modern open-source models, and for the majority of production AI engineering work you’ll encounter in 2026.

**TensorFlow** still has a footprint, particularly in some enterprise and mobile-deployment contexts via **TensorFlow** **Lite** , but if you can only learn one framework at a time deeply, then learn **PyTorch**.

It’s what almost every Hugging Face model, agent frameworks, and research code you’ll read are built on.

### Resources 💻

[

## Zero to Mastery Learn PyTorch for Deep Learning

### Learn important machine learning concepts hands-on by writing PyTorch code.

www.learnpytorch.io



](https://www.learnpytorch.io/?source=post_page-----d21e5748a0aa---------------------------------------)

### NLP, Computer Vision, and Transformers

You need _working_ _literacy_ in the following:

- **NLP fundamentals:** tokenization, embeddings, sequence models
- **Computer Vision fundamentals:** CNNs, image preprocessing, transfer learning
- **The Transformer architecture**: attention, self-attention, why this specific architecture is the reason every LLM you use today exists at all

### [Attention is all you need!](https://arxiv.org/abs/1706.03762) (literally)

Really understand how the Attention mechanism works in a Transformer architecture. Everything in Phase 5 sits on top of it. _(see resources below)_

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*QopbPn0vp0uPwmpDH2amig.png)

source: [https://www.kaggle.com/discussions/getting-started/587250](https://www.kaggle.com/discussions/getting-started/587250)

### [Portfolio Project #3: Sentiment Analysis](https://www.geeksforgeeks.org/nlp/fine-tuning-bert-model-for-sentiment-analysis/)

Fine-tune a pretrained transformer (a distilled BERT variant is a good, cheap starting point) on a sentiment classification dataset.

This project teaches you the entire modern fine-tuning workflow in a gist:

From loading a pretrained model, tokenizing data correctly, fine-tuning on top, to evaluating the exact same workflow at a larger scale that production teams use.

### P[ortfolio Project #4: Meeting Transcriber](https://www.freecodecamp.org/news/how-to-turn-audio-to-text-using-openai-whisper/)

Build an end-to-end pipeline: audio in, transcript out, summary out.

This combines speech-to-text (**Whisper** is the obvious, excellent choice here) with an LLM summarization step.

It makes this your first real AI application, not just a model. It’s also a genuinely useful tool you can actually keep using something you built by yourself!

### Resources 💻

**Explore this if you love interactive learning like i do:**

[

## Transformer Explainer: LLM Transformer Model Visually Explained

### An interactive visualization tool showing you how transformer models work in large language models (LLM) like GPT.

poloclub.github.io



](https://poloclub.github.io/transformer-explainer/?source=post_page-----d21e5748a0aa---------------------------------------)

[

## 📘 Beginner’s Guide to Transformer (with diagrams and real word embeddings) | Kaggle

### What is Transformer? Transformer is the backbone of modern NLP. Introduced in the paper “Attention is All You Need”, it…

www.kaggle.com



](https://www.kaggle.com/discussions/getting-started/587250?source=post_page-----d21e5748a0aa---------------------------------------)

## Phase 5: AI Engineer

This is the phase this entire roadmap has been building toward, and it’s where the real **AI Engineering** work relies.

**Note**: If you are preparing for ML domain roles, this is the part where the preparation diverges. Everything before this was foundational, common to both AI, ML domains, and whether you’re a fresher or an experienced developer, this is the frame you build on.

> **_Note:_** _You can start with AI evaluation part early. Define your eval set and success criteria before building the system. This makes it much easier to_ measure _progress and build reliable systems._

### Context Engineering

**Context Engineering** is the actual 2026 successor to **prompt engineering.**

A Prompt engineer asks: _what words do I put in the prompt?_

While a Context Engineer asks: _what is the complete set of information- retrieved documents, tool outputs, conversation history, system instructions, memory that the model needs in its context window to do this task well, and how do I structure and prioritize all of it?_

> That’s the whole scenario. Basically, thinking in terms of systems.

### Core concepts to focus on

- What **information** actually needs to be in **context** vs. what’s **noise** diluting the signal
- How to **structure** that context (ordering, formatting, compression) for the model to use it well
- **Context window budgeting:** you don’t have infinite tokens, and stuffing everything for just-in-case scenarios often makes outputs _worse_, not better
- **Structured Outputs:** Learn how to make LLMs generate responses in a predefined schema (JSON, Pydantic, etc.) instead of free-form text. This makes AI applications more reliable and easier to integrate with downstream systems.

### Resources 💻

[

## AI Context Windows: The Simplest Explanation You’ve Ever Had

### Everyone talks about 200K, 1M, and even 10M context windows. But what are they actually? Let’s make them finally click!

medium.com



](https://medium.com/the-tech-trek-by-tech-chick/ai-context-windows-the-simplest-explanation-youve-ever-had-c13ecf314d2c?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Context Engineering: The Skill Replacing Prompt Engineering

### AI didn’t suddenly become smarter. We just became better at giving it context!

medium.com



](https://medium.com/the-tech-trek-by-tech-chick/context-engineering-the-skill-replacing-prompt-engineering-609beae8ab36?source=post_page-----d21e5748a0aa---------------------------------------)

[

## The Ultimate Cheat Sheet of Prompt Engineering Techniques

### From Basics to Advanced

medium.com



](https://medium.com/the-tech-trek-by-tech-chick/the-ultimate-cheat-sheet-of-prompt-engineering-techniques-8629d3c8afb6?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Context Engineering (1/2) — Getting the best out of Agentic AI Systems

abvijaykumar.medium.com



](https://abvijaykumar.medium.com/context-engineering-1-2-getting-the-best-out-of-agentic-ai-systems-90e4fe036faf?source=post_page-----d21e5748a0aa---------------------------------------)

### Retrieval-Augmented Generation (RAG)

RAG is the technique that lets an LLM answer questions using information it was never trained on.

### Core topics

- **Chunking strategies:** naive fixed-size chunking vs. semantic chunking, and why this choice quietly determines your ceiling on retrieval quality
- **Embeddings & vector databases:** how text becomes a vector, and tools like Pinecone, Weaviate, Chroma, or pgvector for storing and searching them
- **Retrieval: s**imilarity search, hybrid search (combining keyword + semantic), and re-ranking
- **RAG techniques: Query Rewriting** (improving the user’s query before retrieval), **Agentic RAG** (allowing agents to plan and retrieve iteratively), and **Graph RAG** (using knowledge graphs to capture relationships between entities for richer retrieval)
- **Evaluation:** measuring retrieval quality, hallucinations (_not just does the final answer look okay_), using metrics like context precision and recall

### Resources 💻

[

## Your RAG System Isn’t Hallucinating, It’s Just Lazy

### this is why your RAG isn’t doing its best

medium.com



](https://medium.com/the-tech-trek-by-tech-chick/your-rag-system-isnt-hallucinating-it-s-just-lazy-b8f2a5caf72a?source=post_page-----d21e5748a0aa---------------------------------------)

**I personally found this course immensely helpful in understanding everything about RAG:**

**Later, dive into RAG strategies here:**

As a project, you can work on implementing RAG on your own set of personal journals you have; it’s a cool project indeed.

### Model Context Protocol (MCP)

**MCP** is, in one sentence, a standardized way for an LLM application to connect to **external** **tools** and **data** sources instead of every team writing a custom integration for every tool an agent needs to touch.

### Core topics

- Understanding the MCP client/server model
- Connecting an existing MCP server to an agent you build
- Building a minimal custom MCP server for a tool that doesn’t already have one

### Resources 💻

[

## The Beginner’s Guide to MCP (Model Context Protocol)

### Simple yet powerful protocol changing AI systems’ connectivity

medium.com



](https://medium.com/the-tech-trek-by-tech-chick/the-beginners-guide-to-mcp-model-context-protocol-9bf93b172c18?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Meet the MCP (Model Context Protocol) Team

### Leveling up to know about MCP Host, Client, Server and Message Transport

medium.com



](https://medium.com/the-tech-trek-by-tech-chick/meet-the-mcp-model-context-protocol-team-e5666cc185b9?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Model Context Protocol (MCP): A Guide With Demo Project

### Learn how to build an MCP server using Anthropic’s Model Context Protocol to connect Claude with GitHub and Notion.

www.datacamp.com



](https://www.datacamp.com/tutorial/mcp-model-context-protocol?source=post_page-----d21e5748a0aa---------------------------------------)

Every tool you work on with ChatGPT or Claude, either to write into or read from Canva, Notion, or any external tool, MCP is driving it.

### AI Agents

An AI Agent is a system where an LLM can reason about a **goal**, decide which **tool** to use, take an **action**, **observe** the result, and **loop** instead of just producing a single static text response like a chatbot.

### Core topics

- **The reasoning loop:** plan → act → observe → repeat (ReAct-style patterns)
- **Tool use/function calling:** how the model decides _when_ and _what_ to call
- **Memory**: short-term (within a session) vs. long-term (persisted across sessions)
- **Guardrails:** what stops an agent from doing something destructive, expensive, or wrong

Build at least one agent from raw API calls before reaching for a framework like LangChain or LangGraph.

It’s the difference between knowing what LangChain or a similar framework is _doing for you_ versus just knowing its API surface.

### Resources 💻

[

## Building an AI Agent from Scratch: No Magic, Just a Deterministic Loop

### I was using Claude, Codex, Cursor, Gemini, Copilot, or Junie every day, but I still could not point to the exact line…

levelup.gitconnected.com



](https://levelup.gitconnected.com/building-an-ai-agent-from-scratch-no-magic-just-a-deterministic-loop-a916161705fb?source=post_page-----d21e5748a0aa---------------------------------------)

**Found these very helpful:**

[

## Quickstart: LangChain Essentials — Python

### Learn the core elements of LangChain. Build with `create_agent`, a powerful and extensible agent building block. Learn…

academy.langchain.com



](https://academy.langchain.com/courses/langchain-essentials-python?source=post_page-----d21e5748a0aa---------------------------------------)

[

## Foundation: Introduction to LangGraph — Python

### Learn the basics of LangGraph — our framework for building agentic and multi-agent applications. Separate from the…

academy.langchain.com



](https://academy.langchain.com/courses/intro-to-langgraph?source=post_page-----d21e5748a0aa---------------------------------------)

While understanding agent concepts is more important than frameworks, it’s worth exploring modern frameworks like [**OpenAI Agents SDK**](https://developers.openai.com/api/docs/libraries), **LangGraph**, [**CrewAI**](https://crewai.com/), [**Google ADK**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk), [**Agno**](https://docs.agno.com/), [**AutoGen**](https://microsoft.github.io/autogen/stable//index.html), and [**Smolagents**](https://huggingface.co/docs/smolagents/index) to understand different approaches to building production-ready agentic systems.

### Multi-Agent Systems

Multi-Agent Systems take the single-agent pattern above and split a complex task across several specialized agents that coordinate.

This matters because single agents hit a real ceiling on complex, multi-step tasks such as: context gets overloaded, and one agent trying to be a generalist at everything tends to be mediocre at most of it!

**Specialized agents,** each with a narrow, well-defined job and its own context, tend to outperform a generalist agent trying to do everything! _(just like we humans specialise in a task and do it)_

Patterns worth knowing:

- **Orchestrator-worker:** one agent delegates subtasks to specialized workers
- **Sequential pipelines:** agent A’s output becomes agent B’s input
- **Debate/critique patterns:** one agent’s output gets reviewed and challenged by another before being finalized

### Resources 💻

[

## Multi-agent — Docs by LangChain

### Edit description

docs.langchain.com



](https://docs.langchain.com/oss/python/langchain/multi-agent?source=post_page-----d21e5748a0aa---------------------------------------)

[

## How to Build Your First Multi-Agent AI System in Python and LangGraph

### In this tutorial, I’ll show you how to build a multi-agent AI system in Python with no orchestration framework. We’ll…

www.freecodecamp.org



](https://www.freecodecamp.org/news/how-to-build-your-first-multi-agent-ai-system-in-python-and-langgraph/?source=post_page-----d21e5748a0aa---------------------------------------)

### AI Evaluation

As an AI Engineer, I can’t stress this enough. It’s arguably the thing that separates a demo from a production system.

### Core topics

- Building a test set of representative inputs _before_ you ship
- Defining what **good** means for your specific task (correctness? faithfulness to retrieved sources? tone? latency?)
- Using **LLM-as-judge** patterns where human evaluation doesn’t scale, while understanding the biases that come with that approach
- Evaluation frameworks such as **DeepEval**, **Promptfoo**, **LangSmith**, **Ragas**, and **Arize** **Phoenix** to benchmark and track regressions in prompts, RAG pipelines, and agentic workflows.
- Tracking **regressions** over time as you change prompts, models, or retrieval logic

### Resources 💻

The resources below cover metrics such as relevance score, precision, recall, ROUGE, and BLEU, as well as evaluation techniques, tools, and frameworks

[

## GitHub — hparreao/Awesome-AI-Evaluation-Guide: A comprehensive, implementation-focused guide to…

### A comprehensive, implementation-focused guide to evaluating Large Language Models, RAG systems, and Agentic AI in…

github.com



](https://github.com/hparreao/Awesome-AI-Evaluation-Guide?source=post_page-----d21e5748a0aa---------------------------------------)

[

## GitHub — Vvkmnn/awesome-ai-eval: ☑️ A curated list of tools, methods & platforms for evaluating AI…

### ☑️ A curated list of tools, methods & platforms for evaluating AI reliability in real applications …

github.com



](https://github.com/Vvkmnn/awesome-ai-eval?source=post_page-----d21e5748a0aa---------------------------------------)

## LLMOps

As AI systems become production applications, learning **LLMOps** becomes increasingly important.

### Core topics

- Prompt versioning
- model routing
- tracing, observability
- cost monitoring
- caching
- experiment tracking

LLMOps helps build reliable and scalable AI systems.

### Resources 💻

[

## Introduction

### LLMOPs Workshop

microsoft.github.io







](https://microsoft.github.io/llmops-workshop/?source=post_page-----d21e5748a0aa---------------------------------------)

[

## GitHub — tensorchord/Awesome-LLMOps: An awesome & curated list of best LLMOps tools for developers

### An awesome & curated list of best LLMOps tools for developers — tensorchord/Awesome-LLMOps

github.com



](https://github.com/tensorchord/Awesome-LLMOps?source=post_page-----d21e5748a0aa---------------------------------------)

### Deploying AI Applications

Deployment fundamentals worth having:

- **APIs**: wrapping your model/agent in FastAPI or similar
- **Containerization**: Docker, enough to know why it exists and how to use it
- **Inference and model-serving tools:** **vLLM** for high-throughput LLM serving and **LiteLLM** for routing requests across multiple model providers through a unified interface
- **Basic cloud deployment**: can be done with your most familiar cloud provider, deployment end-to-end
- **Monitoring & cost tracking:** LLM calls cost real money per token, and production systems need visibility into both latency and spend. This is the most looked-upon area
- **CI/CD basics:** to deploy and automate the pipelines

## Mistakes I See Every Beginner Make

- Jumping straight to LLMs and agents while skipping Phase 1–3
- Treating frameworks (LangChain, etc.) as something to learn instead of something built on top of concepts you should understand independently first
- Collecting tutorials instead of building projects, watching is not the same as doing, and the gap between the two is where most people quietly stall out
- Build an eval pipeline as part of the build, not later. Every minor change lets us know if the pipeline is performing better or worse.

## Final Thoughts

If you take just one thing from this roadmap, let it be this: becoming an AI Engineer isn’t about mastering every new tool, it’s about _building strong fundamentals and applying them consistently._

Don’t rush as you navigate through every phase. Build projects, experiment, make mistakes, and learn by doing. That’s where real growth happens.

I hope this roadmap gives you a clear direction and saves you the time I spent figuring out what to learn next.

> **_Bookmark it, share with your community, revisit as you progress, and most importantly, don’t just learn AI; build with it ❤️_**

### [AI Glossary Cheatsheet (2026)](https://gum.co/u/esxkxj3x) ☃️

**-> 150+ AI terms** explained in plain English, covering LLMs, RAG, AI Agents, MCP, Context Engineering, LLMOps, and more.

Perfect if you’re just starting your AI engineering journey.

[**→ Download it here**](https://gum.co/u/esxkxj3x)

### Ready to go beyond reading? Here’s how I can help ❤

**> Developers:** Explore the **Claude Code Ultimate Bundle** below to master Claude Code and ship production-ready AI systems.

**> Founders, Startups & Engineering Teams:** If you’re building AI products, AI agents, RAG systems, MCP servers, or internal AI tools and need engineering support, let’s connect. (details below)

### 1. [Claude Code Ultimate Bundle](https://moonpiecreates.gumroad.com/l/disyw?utm_source=medium_post_bottom_cta)

[

## Claude Code Ultimate Bundle | Master Claude Code & Ship Production-Ready AI Systems

### Claude Code Ultimate Bundle — The Complete Claude Code ToolkitThe Complete Field Manual + 7 AI Engineering Workspaces +…

moonpiecreates.gumroad.com



](https://moonpiecreates.gumroad.com/l/disyw?utm_source=medium_post_bottom_cta&source=post_page-----d21e5748a0aa---------------------------------------)

If you’re serious about building with Claude Code, this is the toolkit I wish I’d had from day one.

It includes:

- **Claude Code Mastery Guide (29 Chapters)**
- **7 Production AI Engineering Workspaces**
- **210+ Claude Code Prompts**
- **AI Agents**
- **Multi-Agent Systems**
- **RAG**
- **MCP Servers**
- **AI SaaS**
- **AI Evaluation**
- **Lifetime Updates**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*3CgBgUVa2mudIR8e)

table of contents of [**Claude Code Mastery Guide**](https://gum.co/u/n7e0yfd7)

Instead of starting every project from scratch, you’ll start with a production-ready engineering foundation. It’s to help you spend less time rebuilding your engineering foundation and more time **shipping** **products**.

### 2. Working on Something Bigger?

Over the past four years, I’ve worked on **production AI systems involving enterprise RAG, LLM applications, AI evaluation pipelines, AI workflow automation, and developer tooling** for **startups and large organisations.**

That experience has taught me what it takes to move AI systems beyond impressive demos into **reliable, production-ready software.**

I partner with **founders, startups, and engineering teams** to identify high-impact opportunities, design the right architecture, build production-ready AI solutions, automate critical workflows, and hand everything over with complete documentation so your team owns the system from day one.

**My Recent Engagements Include:**

- AI Agents & Multi-Agent Systems
- Enterprise RAG Platforms
- Internal AI Copilots
- MCP Servers
- Workflow Automation
- AI Evaluation Pipelines
- Claude Code Engineering
- AI Architecture Reviews

> Whether you need help designing the architecture, validating technical decisions, or building the system end-to-end, I’d be happy to discuss your project!

**→** [**Book a strategy call**](https://calendly.com/moonpie-creates/30min) **📞**

**→** [**View AI engineering services**](https://moonpiecreates.vercel.app/services) 🌐

**→** [**Connect with me**](https://www.linkedin.com/in/chandana-j-13b56520a/) 📤

**Happy building ❤️**