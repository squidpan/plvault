---
categories:
  - "[[Clippings]]"
title: "I Thought I Knew Python. Then These 7 Features Humbled Me Completely."
source: "https://python.plainenglish.io/i-thought-i-knew-python-then-these-7-features-humbled-me-completely-8a2c6b5862ce"
author:
  - "[[inprogrammer]]"
published: 2026-05-27
created: 2026-06-29
description: "Discover 7 advanced Python features most developers never use walrus operator, structural pattern matching, __slots__, and more. Real code examples included."
tags:
  - "clippings"
url: "https://python.plainenglish.io/i-thought-i-knew-python-then-these-7-features-humbled-me-completely-8a2c6b5862ce"
---
I Thought I Knew Python. Then These 7 Features Humbled Me Completely.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*phXzAx0kRRAegrKeuz-k8Q.png)

ChatGpt Image

*I had 4 years of Python experience. These features made me feel like a beginner again.*

I have been writing Python professionally for over four years. FastAPI services, async pipelines, CLI tools, data processing scripts the full spectrum.

If you dont have a subscription [read here](https://medium.com/@inprogrammer/8a2c6b5862ce?sk=891b4618f68a20006cba4f0aea449883).

I thought I had a solid grip on the language.

Then I started reading CPython source code. Then I started reviewing code from engineers who had been writing Python since 2.7. And one by one, I ran into features that stopped me cold.

Not obscure academic curiosities. Features that are in the standard library, available in Python 3.10+, and actively used in production codebases at companies you have heard of.

I just had never needed them — until I did.

Here are the 7 that humbled me the most.

## 1\. The Walrus Operator Does More Than You Think

You probably know `:=` exists. You might have used it in a `while` loop. But its real power shows up in list comprehensions with expensive operations.

**What most developers write:**

```hs
results = []
for user_id in user_ids:
    data = fetch_user(user_id)      # expensive call
    if data and data["active"]:
        results.append(data)
```

**What the walrus operator enables:**

```hs
results = [
    data
    for user_id in user_ids
    if (data := fetch_user(user_id)) and data["active"]
]
```

The fetch happens exactly once per user, inside the comprehension, with no intermediate variable leaking into scope. Clean, readable, and no performance penalty.

Where it truly shines is regex:

```hs
import re
```
```hs
lines = ["Error: disk full", "Info: started", "Error: timeout"]
```
```hs
errors = [
    match.group(1)
    for line in lines
    if (match := re.search(r"Error: (.+)", line))
]
# ['disk full', 'timeout']
```

Without the walrus operator, you either call `re.search` twice (once in the `if`, once to get the value) or you restructure the whole thing into a regular loop. The walrus operator collapses both into one pass.

**The lesson:** It is not just syntactic sugar. It eliminates redundant computation inside comprehensions.

## 2\. Structural Pattern Matching Is Not a Switch Statement

Python 3.10 introduced `match/case` and everyone wrote blog posts comparing it to switch statements in other languages. That framing missed the point entirely.

This is not a switch statement. It is structural decomposition.

```hs
def process_event(event: dict):
    match event:
        case {"type": "click", "button": "left", "x": x, "y": y}:
            handle_left_click(x, y)
        case {"type": "click", "button": "right"}:
            handle_right_click()
        case {"type": "keypress", "key": str(k)} if k.isupper():
            handle_uppercase_key(k)
        case {"type": "keypress", "key": k}:
            handle_key(k)
        case _:
            log_unknown_event(event)
```

Notice what is happening: it is matching the *shape* of the data, extracting values into variables (`x`, `y`, `k`), and applying guards (`if k.isupper()`). In one expression.

The alternative is a deeply nested chain of `if isinstance()`, `if "type" in event`, `if event["type"] == "click"` — code that is fragile, verbose, and hard to extend.

Pattern matching also works on class instances:

```hs
from dataclasses import dataclass
```
```hs
@dataclass
class Point:
    x: float
    y: float
```
```hs
def describe(shape):
    match shape:
        case Point(x=0, y=0):
            return "origin"
        case Point(x=0, y=y):
            return f"on y-axis at {y}"
        case Point(x=x, y=0):
            return f"on x-axis at {x}"
        case Point(x=x, y=y):
            return f"point at ({x}, {y})"
```

This is pattern matching in the Haskell/Rust sense. It is a fundamentally different way of writing conditional logic that scales to complex data without becoming unreadable.

**The lesson:** Stop thinking of it as a switch. Start thinking of it as a shape inspector.

## 3\. \_\_slots\_\_ Can Cut Your Memory Usage in Half

Every Python object stores its attributes in a `__dict__` — a dictionary that lives on the heap and carries significant overhead. For objects you create thousands of times, this adds up fast.

`__slots__` tells Python to skip the dictionary and use a fixed-size array instead.

```hs
# Without __slots__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```
```hs
# With __slots__
class PointSlotted:
    __slots__ = ("x", "y")
```
```hs
def __init__(self, x, y):
    self.x = x
    self.y = y
```

The difference in practice:

```hs
import sys
```
```hs
p1 = Point(1, 2)
p2 = PointSlotted(1, 2)
```
```hs
print(sys.getsizeof(p1.__dict__))   # 232 bytes
print(sys.getsizeof(p2))            # 56 bytes
```

That is a 4x reduction in memory per object. At 100,000 instances, the difference is ~17 MB.

Attribute access is also faster with `__slots__` because Python skips the dictionary lookup entirely.

The trade-off: slotted objects cannot have arbitrary attributes added at runtime, and they do not work cleanly with multiple inheritance in some edge cases. For data-heavy classes where you know the attribute set upfront, the trade-off is almost always worth it.

**The lesson:** If you are instantiating a class more than a few thousand times, benchmark `__slots__`. The memory savings are real.

## 4\. functools.cache Is Not the Same as functools.lru\_cache

Most developers know `lru_cache`. Fewer know that `functools.cache` exists in Python 3.9+ — and it is faster.

```hs
from functools import cache, lru_cache
```
```hs
@lru_cache(maxsize=None)
def fib_lru(n):
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)
```
```hs
@cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)
```

`functools.cache` is equivalent to `lru_cache(maxsize=None)`, but with one key difference: it has no overhead for tracking the LRU eviction order. It is a pure unbounded cache with a simpler, faster implementation.

For pure functions with hashable arguments and no need for eviction, `@cache` is always the better choice.

There is also `cached_property`, which is underused:

```hs
from functools import cached_property
```
```hs
class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
```
```hs
@cached_property
def data(self):
    print("Loading data...")      # runs only once
    return load_large_file(self.filepath)
```
```hs
p = DataProcessor("data.csv")
_ = p.data    # loads file
_ = p.data    # returns cached result, no reload
```

The property computes once on first access, then stores the result directly on the instance. No decorator needed on every call, no external cache dictionary to manage.

**The lesson:** Know the difference between `cache`, `lru_cache`, and `cached_property`. Each is optimal in different situations.

## 5\. Context Managers Are Not Just for File Handling

Almost every Python tutorial shows `with open("file.txt") as f` and calls it a day. Context managers are one of the most underused tools in Python for managing *any* kind of state.

The `contextlib.contextmanager` decorator turns a generator into a context manager with almost no boilerplate:

```hs
from contextlib import contextmanager
import time
```
```hs
@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")
```
```hs
with timer("database query"):
    results = db.execute("SELECT * FROM users")
```

You can use this for database transactions, temporary directory changes, mocking, feature flags, and connection pooling — anywhere you need guaranteed setup and teardown.

`contextlib.suppress` is another gem that most developers write manually:

```hs
# What most people write
try:
    os.remove("temp.txt")
except FileNotFoundError:
    pass
```
```hs
# What contextlib gives you
from contextlib import suppress
```
```hs
with suppress(FileNotFoundError):
    os.remove("temp.txt")
```

Same semantics, half the lines, zero cognitive overhead.

**The lesson:** Any time you write `try/finally` for setup and teardown, ask if a context manager would be cleaner.

## 6\. Generator Pipelines Can Replace Entire Data Processing Chains

This one took me the longest to internalize. Generators are not just a memory optimization. They are a composition model.

Consider a data processing pipeline:

```hs
import csv
```
```hs
def read_rows(filepath):
    with open(filepath) as f:
        yield from csv.DictReader(f)
```
```hs
def filter_active(rows):
    return (row for row in rows if row["status"] == "active")
```
```hs
def parse_amount(rows):
    return (
        {**row, "amount": float(row["amount"])}
        for row in rows
    )
```
```hs
def above_threshold(rows, threshold):
    return (row for row in rows if row["amount"] > threshold)
```
```hs
# Compose the pipeline
rows = read_rows("transactions.csv")
rows = filter_active(rows)
rows = parse_amount(rows)
rows = above_threshold(rows, 1000.0)
```
```hs
for row in rows:
    process(row)
```

Nothing is loaded into memory until the final `for` loop. Each stage processes one row at a time and passes it to the next stage. You could run this pipeline on a 10 GB CSV file on a machine with 512 MB of RAM.

More importantly, each stage is independently testable, independently replaceable, and independently readable. This is a pipeline architecture — not a scripting pattern.

**The lesson:** When you find yourself building a list just to iterate over it once, consider whether a generator pipeline would serve you better.

## 7\. dataclasses Have Features Nobody Talks About

Everyone knows `@dataclass` generates `__init__`, `__repr__`, and `__eq__`. Almost nobody uses `field()` to its full potential.

```hs
from dataclasses import dataclass, field
from typing import ClassVar
```
```hs
@dataclass
class Order:
    id: int
    items: list = field(default_factory=list)      # mutable default, done right
    _total: float = field(default=0.0, repr=False) # excluded from __repr__
    tax_rate: ClassVar[float] = 0.08               # class-level, not per-instance
```
```hs
def add_item(self, price: float):
    self.items.append(price)
    self._total = sum(self.items) * (1 + self.tax_rate)
```

Three things in that example that most developers miss:

- `default_factory=list` — the correct way to have a mutable default. Using `items: list = []` is a bug waiting to happen (shared between instances).
- `repr=False` — exclude internal state from the string representation without writing a custom `__repr__`.
- `ClassVar` — tells the dataclass machinery to skip this field entirely. It is a class attribute, not an instance attribute.

There is also `__post_init__` for validation:

```hs
@dataclass
class PositiveInt:
    value: int
```
```hs
def __post_init__(self):
    if self.value <= 0:
        raise ValueError(f"value must be positive, got {self.value}")
```

And `frozen=True` for immutable dataclasses that are hashable and safe to use as dictionary keys:

```hs
@dataclass(frozen=True)
class Point:
    x: float
    y: float
```
```hs
p = Point(1.0, 2.0)
cache = {p: "some result"}   # works because Point is now hashable
```

**The lesson:** `@dataclass` is not just a shortcut for `__init__`. It is a complete object modeling toolkit when you use all of `field()`, `ClassVar`, `frozen`, and `__post_init__`.

## The Pattern Behind All 7

Looking back at this list, there is a common thread: each feature exists because a simpler, more obvious approach has a hidden cost — performance, memory, correctness, or readability at scale.

The walrus operator eliminates redundant function calls. `__slots__` eliminates dictionary overhead. Generator pipelines eliminate unnecessary memory allocation. The `field()` API eliminates shared mutable defaults.

Python is not a language you learn once. It is a language you keep discovering, even after years of daily use.

The features that humbled me were not the flashy ones. They were the quietly powerful ones that have been sitting in the standard library the whole time, waiting for the moment I finally needed them.

That moment always comes.

## Conclusion

Feature Why It Matters Walrus operator `:=` Eliminates redundant calls inside comprehensions Structural pattern matching Shape-based decomposition, not a switch statement `__slots__` 4x memory reduction for high-volume instances `functools.cache` vs `lru_cache` Faster for unbounded caches with no eviction needed Context managers via `contextlib` Clean setup/teardown beyond file handling Generator pipelines Process unlimited data with constant memory `dataclasses` with `field()` Full object modeling, not just `__init__` shorthand

*Which of these did you already know? Which one surprised you? Drop a comment I read every one.*

**Tags:** Python, Python Programming, Software Engineering, Programming, Backend Development, Python Tips, Advanced Python