---
categories:
  - "[[Clippings]]"
title: "I Tested 5 Python Testing Frameworks. One Changed How I Write Code."
source: "https://blog.stackademic.com/i-tested-5-python-testing-frameworks-one-changed-how-i-write-code-a262647a0eea"
author:
  - "[[inprogrammer]]"
published: 2026-04-16
created: 2026-08-18
description: "I Tested 5 Python Testing Frameworks. One Changed How I Write Code. A hands-on comparison of unittest, pytest, nose2, doctest, and Hypothesis, and why one of them made me a better developer before …"
tags:
  - "clippings"
url: "https://blog.stackademic.com/i-tested-5-python-testing-frameworks-one-changed-how-i-write-code-a262647a0eea"
---
## A hands-on comparison of unittest, pytest, nose2, doctest, and Hypothesis, and why one of them made me a better developer before the tests even ran.

![I Tested 5 Python Testing Frameworks. One Changed How I Write Code.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Fd3oDYawVN0SfpTpYba5HA.png)

I Tested 5 Python Testing Frameworks. One Changed How I Write Code.

I used to write tests just to say I wrote them. Pick a few inputs. Check the output. Done. I thought I was doing it right.

Then I spent a month using five different Python testing frameworks on the same project. Not just reading about them. Actually building with them.

What I found surprised me. One of them did not just change how I test. It changed how I think when I write code.

Here is everything I learned.

**Friend link for nonmembers** [**https://medium.com/@inprogrammer/i-tested-5-python-testing-frameworks-one-changed-how-i-write-code-a262647a0eea?sk=834954fb74222d61c25b97c4a5747e87**](https://medium.com/@inprogrammer/i-tested-5-python-testing-frameworks-one-changed-how-i-write-code-a262647a0eea?sk=834954fb74222d61c25b97c4a5747e87)

## The Project I Used

To keep things fair, I used the same project for all five frameworks. It was a simple Flask API that handled user accounts and a task list. Small enough to move fast, but real enough to find actual problems.

## 1\. unittest: Already on Your Computer

**What it is:** Python’s built-in testing tool. No installation needed.

This one comes with Python. You do not need to install anything. Just import it and start writing tests.

```hs
import unittest
```
```hs
class TestTaskCreation(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()    def test_create_task_returns_201(self):
        response = self.client.post('/tasks', json={"title": "Buy milk"})
        self.assertEqual(response.status_code, 201)if __name__ == '__main__':
    unittest.main()
```

It works fine. But the style feels old. You have to write a class for every group of tests. You have to use `self` everywhere. It is a lot of extra typing for simple things.

If you are working somewhere that does not allow you to install new packages, unittest is your friend. Otherwise, there are better options.

**Bottom line:** Gets the job done. But writing tests in it feels slow.

## 2\. pytest: The One Most Developers Use

**What it is:** The most popular Python testing tool out there.

pytest lets you skip the class and just write a simple function. That alone makes a big difference.

```hs
import pytest
```
```hs
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client@pytest.mark.parametrize("title,expected_status", [
    ("Buy milk", 201),
    ("", 400),
    (None, 400),
])
def test_create_task(client, title, expected_status):
    response = client.post('/tasks', json={"title": title})
    assert response.status_code == expected_status
```

See that `parametrize` part? Instead of writing three separate tests, you write one. pytest runs it three times with different inputs. That saves a lot of time.

Fixtures are also great. You write your setup code once and use it anywhere you need it.

On top of that, pytest has a huge collection of plugins. Need to check test coverage? There is a plugin. Need to run tests faster in parallel? There is a plugin for that too.

**Bottom line:** If you only learn one testing tool, make it pytest.

## 3\. nose2: Good for Old Code

**What it is:** A tool that runs your old unittest tests with extra features on top.

I will be honest. nose2 did not excite me much. But it does solve one specific problem really well.

If you have an old project full of unittest tests and you do not want to rewrite everything, nose2 lets you run those same tests with better output and more options. No rewriting needed.

```hs
# nose2 runs your old unittest tests without any changes
# You just set it up in a config file
[unittest]
start-dir = tests
```

The problem is that not many people use it anymore. The docs are thin. Finding help online is harder than with pytest.

**Bottom line:** Useful if you are working with an old codebase. Not worth starting fresh with it.

## 4\. doctest: Tests Hidden Inside Your Docs

**What it is:** A tool that turns the examples in your code comments into real tests.

This one is clever. You write an example in your function’s description, like you are showing someone how to use it. Then doctest checks if that example actually works.

```hs
def add_task(title: str) -> dict:
    """
    Creates a new task.
```
```hs
>>> add_task("Buy milk")
{'title': 'Buy milk', 'done': False}    >>> add_task("")
Traceback (most recent call last):
    ...
ValueError: Title cannot be empty
"""
if not title:
    raise ValueError("Title cannot be empty")
return {"title": title, "done": False}
```

Run `python -m doctest yourfile.py` and Python checks that the output matches what you wrote.

The big benefit here is that your documentation stays accurate. How many times have you read a code example in the docs and it just did not work? doctest fixes that because the example has to work or the test fails.

It breaks down quickly with complex functions though. It is not a replacement for a full test suite.

**Bottom line:** Great for simple functions where you want your docs and your code to always agree.

## 5\. Hypothesis: The One That Changed How I Think

**What it is:** A tool that makes up its own test cases to try and break your code.

This is the one that changed everything for me.

Every test I had written before was the same. I would think of a few examples, test those exact examples, and move on. The problem is that we only think of inputs we already had in mind when we wrote the code. We miss the weird stuff.

Hypothesis works differently. Instead of you picking the inputs, you tell it the rules your function should follow. Then it makes up hundreds of different inputs on its own to try and prove those rules wrong.

```hs
from hypothesis import given, strategies as st
```
```hs
@given(st.text(min_size=1, max_size=100))
def test_task_title_always_stored_correctly(title):
    task = add_task(title)
    assert task["title"] == title
    assert task["done"] is False
```

Ten minutes after running Hypothesis on my project, it found a real bug.

A task title made of only spaces was passing my check. That is because I wrote `if not title` instead of `if not title.strip()`. I had never thought to try a title like `" "`. Hypothesis did.

That one bug made me realize something. The bugs in your code live in the inputs you never thought to try. And Hypothesis has no such blind spots.

It also has a feature called shrinking. When it finds a bad input, it automatically tries to make it as simple as possible. So instead of getting a huge messy string that broke your function, it finds the smallest version that still causes the problem. Much easier to debug.

The biggest change was not in my tests though. It was in how I started thinking before I wrote any code. Now I ask myself: what should always be true about this function, no matter what gets passed in? That question makes you write cleaner code from the start.

**Bottom line:** Start using this. It will find bugs you did not know you had.

## Quick Comparison

Framework Best For Hard to Learn? Community unittest No extra installs needed No Built-in pytest Most projects No Very large nose2 Old unittest projects No Small doctest Keeping docs accurate No Minimal Hypothesis Finding hidden bugs A little Growing

## What I Actually Recommend

Use pytest as your main tool. It is simple, powerful, and has a solution for almost any problem you run into.

Add Hypothesis when you have functions that take user input, handle data, or need to work correctly across many different values.

Use doctest for small utility functions where you want the examples in your comments to always stay correct.

The thing that changed most for me was not which tool I picked. It was the question I now ask before writing code: “What should always be true here, no matter what?” Hypothesis taught me to ask that. And asking it made my code better before any test ever ran.

*If you only try one new thing after reading this, try Hypothesis. Run it on something you already tested and thought was solid. There is a good chance it finds something.*