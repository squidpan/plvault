---
categories:
  - "[[Clippings]]"
title: "how to use arrows to connect things in plantuml for each diagram type with examples - Google Search"
source: "https://www.google.com/search?sca_esv=d115e34c1a0f1aef&sxsrf=ANbL-n5Nh08QnleoSQrDs5Lm9Wiwbdv0VA%3A1774996147639&q=how+to+use+arrows+to+connect+things+in+plantuml+for+each+diagram+type+with+examples&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3vxYI1tojT_24H7Q4iMwclTUnm45O_6Cq-1VJ9pZry9xEMzIPBDrFxV-NSKxJzs-M77-ccRsPybDHSD2iOW-ZnCP8-uKcZQj7xfXZpvYWiXyW_jb8T83oovWplcJt1MnbzYJNi_U4uKBWVnYE7MY-bagwv8_AeMe49FnZvz4RP3E8fENAw&sa=X&ved=2ahUKEwjP-Yz1osuTAxWWD1kFHXNKNUEQ0NsOegQIAxAB&biw=1920&bih=927&dpr=1&udm=50&aep=10&ntc=1&mstk=AUtExfAY7uTONEJEIP6bmtR-TZsjSKmWCmx3_xvNNQRyiH6DTe4wKR56-JXUensNvYVave11KX_1d_dreaW5Yd64h1lbT2CyjBKWj1f9UoOkjhHItZqwwEc_nQBZLlmUPmCEaPwWYfoxTTxAGLF4qGmpuCk0R54upKrp2xYJr3JowHOSIBACmR0FN3iOkxgqO7W80kShtdATIiI80XTQRESJl9edKpySf6JpjIx_cF-TV6kU1rn37GYDY6LfYsCRgyrYym3sLiwu7wbmH8NMxQBTkeMQdFt4VenYzLRy5qqc87H1LiMAd-wrXLX7Ifk66jDoQy3IBlzruArgOjUe3GydWRVgZvqqLU3Z2wsI77TqOH_w1HVXfQbynnRJtKYFj1ENY7YLcU0xNLVR4Dgh73I7Dtjjb9UBGeTFag&csuir=1&mtid=RVbMadyBLait5NoPx_2Y0AI"
author:
published:
created: 2026-03-31
description:
tags:
  - "clippings"
url: "https://www.google.com/search?sca_esv=d115e34c1a0f1aef&sxsrf=ANbL-n5Nh08QnleoSQrDs5Lm9Wiwbdv0VA%3A1774996147639&q=how+to+use+arrows+to+connect+things+in+plantuml+for+each+diagram+type+with+examples&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3vxYI1tojT_24H7Q4iMwclTUnm45O_6Cq-1VJ9pZry9xEMzIPBDrFxV-NSKxJzs-M77-ccRsPybDHSD2iOW-ZnCP8-uKcZQj7xfXZpvYWiXyW_jb8T83oovWplcJt1MnbzYJNi_U4uKBWVnYE7MY-bagwv8_AeMe49FnZvz4RP3E8fENAw&sa=X&ved=2ahUKEwjP-Yz1osuTAxWWD1kFHXNKNUEQ0NsOegQIAxAB&biw=1920&bih=927&dpr=1&udm=50&aep=10&ntc=1&mstk=AUtExfAY7uTONEJEIP6bmtR-TZsjSKmWCmx3_xvNNQRyiH6DTe4wKR56-JXUensNvYVave11KX_1d_dreaW5Yd64h1lbT2CyjBKWj1f9UoOkjhHItZqwwEc_nQBZLlmUPmCEaPwWYfoxTTxAGLF4qGmpuCk0R54upKrp2xYJr3JowHOSIBACmR0FN3iOkxgqO7W80kShtdATIiI80XTQRESJl9edKpySf6JpjIx_cF-TV6kU1rn37GYDY6LfYsCRgyrYym3sLiwu7wbmH8NMxQBTkeMQdFt4VenYzLRy5qqc87H1LiMAd-wrXLX7Ifk66jDoQy3IBlzruArgOjUe3GydWRVgZvqqLU3Z2wsI77TqOH_w1HVXfQbynnRJtKYFj1ENY7YLcU0xNLVR4Dgh73I7Dtjjb9UBGeTFag&csuir=1&mtid=RVbMadyBLait5NoPx_2Y0AI"
---
---

## Search Results

how to use arrows to connect things in plantuml for each diagram type with examples

**Searching**

In

[PlantUML](https://plantuml.com/deployment-diagram), arrows are the primary way to define relationships and flow. While the basic syntax `->` and `-->` is consistent, different diagram types interpret these arrows to represent specific UML concepts.

General Arrow Rules

Across most diagrams, you can modify arrows with these common patterns:

- **Directional Control**: Force layout by adding directions: `-up->`, `-down->`, `-left->`, or `-right->` (or shorthands `-u->`, `-d->`, `-l->`, `-r->`).
- **Length**: Adding more dashes (e.g., `--->`) suggests a longer path to the layout engine.
- **Styling**: Use brackets to change color or style: `-[#red]->`, `-[bold]->`, or `-[dashed]->`.

---

1\. Sequence Diagrams

Arrows represent **messages** between participants. They are horizontal by default.

- **Synchronous Message**: `A -> B` (Solid line, filled head).
- **Asynchronous/Reply**: `A --> B` (Dashed line).
- **Lost/Found Messages**: `A ->x B` (Lost) or `?-> A` (Found).
- **Head Styles**: Use `->>` for thin heads, `-\\` or `-//` for half-heads, and `->o` for a circle head.

**Example:**

```
Alice -> Bob: Hello
Bob -->> Alice: Responding (thin/dashed)
Alice ->x Bob: Failed message
```

2\. Class Diagrams

Arrows represent **relationships** like inheritance, composition, and association.

- **Association**: `ClassA -- ClassB` (Solid line) or `ClassA --> ClassB` (One-way).
- **Inheritance/Extension**: `Parent <|-- Child` (Solid line, hollow triangle).
- **Composition**: `Whole *-- Part` (Solid line, filled diamond).
- **Aggregation**: `Whole o-- Part` (Solid line, hollow diamond).
- **Dependency**: `ClassA <.. ClassB` (Dashed arrow).

**Example:**

```
Vehicle <|-- Car
Car *-- Wheel : 4
Driver -> Car : drives
```

3\. State & Activity Diagrams

Arrows represent **transitions** between states or actions.

- **Standard Transition**: `State1 -> State2`.
- **Initial/End State**: Use `[*]` as the starting or ending point: `[*] -> State1`.
- **Horizontal Transitions**: Use a single dash `->` for horizontal and double dash `-->` for vertical flow.

**Example:**

```
[*] -> Idle
Idle -> Processing : Start
Processing --> [*] : Success
```

4\. Component & Deployment Diagrams

Arrows represent **interfaces** or **dependencies** between physical/logical pieces.

- **Dependency**: `[Component A] ..> [Component B]`.
- **Interface (Lollipop)**: `Component -() Interface`.
- **Assembly**: `Component1 --( Interface2`.

**Example:**

```
[Web App] ..> [API] : HTTP
[API] --( Database_Interface
[DB] - Database_Interface
```

Would you like a specific example of how to **group elements** using the `together` keyword to fix layout issues with these arrows?

Creating a public link...

- Sequence Diagram - PlantUML
	You can change the color of individual arrows using the following notation: -\[#red\]> Alice incrementing number to messages. You ca...
	PlantUML
	![](data:image/png;base64,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)
- Quick Guide to PlantUML: Diagrams, Syntax & Best Practices - Miro
	Oct 14, 2025 — Entities and relationships: Use keywords like class, interface, and entity to define elements, and arrows to show relationships. A...
	Miro
	![](data:image/png;base64,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)
- UML Sequence Diagram - Ashley's PlantUML Doc
	Dashed lines represent reply messages. An object creation Message has a dashed line with an open arrow head. - creates a solid lin...
	Read the Docs
	![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABSCAMAAAD0B6OUAAAAsVBMVEX////+/s7//9Ht2t389PjNhYL0573Tj57ox6jRkYDerrz36O/t2Nzx2uLYoI3U1NSdnZ22trby8sTx4uXc3Nzt7e28vLzny9D19fXk5OSoqKjDw8ORkZGFhYX/+vt2dl+kpIWcnH6Tk3fOzqh4eHiBgWjf37f//9i6upfCwqFubm6uro3o6MC+WmddXUxublrGcWnXna1cXFymmZ3CYnrkvMaoADKxMk+lACK7U2q6TlB78b1HAAADwUlEQVRYhe1Yi3ajNhAVctp0a1xJgAR6EAMyGAKNu9u6r///sI6I1488jiOHnvXu2WsZjUajixjP6OBByAM3b4APX/zrD+fhQ7j4BZ+HJ2FwFr6E0fACCajhcxFhVLeFW46jkQI6GDX90K+LaJQjX8JltFwvy6IrH5plVNtq2dRtV9tNt8G2bLtl7Uu46Uv80Nki6Js6qoqiG9rS9lGFK1y3VWc77x2uy6YurK0emrqsm6qP2trWXbmu8LK6gDDYfTAu7NjB4LHt1N6/8tRhM3Fg//bTefgQ3vz8Cm4/HmQfwlcRxpPQHBB7HVpfApPvMJ3ah34H/5dAOJ+YcHIfZncTE06OyVNv+ji8eh8+fWSS7cWMHNTZiRFP3k7IOEK5dJLidK/M5I5Jj12ikVbq9CbOyl3vjn1IibnnKFGMK64+6XtDKNU5VStBZc44o3pFTC5NThBTRsIkpYYiqg1lJlmxZ4RKJYojxfJESW0yKlUuhEEU1hCGiLonQlAwIhoxYMgFo+OkYSphhGbPHllLajKkkIQ7J1QLTgSTDAktBKdMKyqNVCyjJkE6SbSbVEZTJZVOlNa/v+RDb6iDePPH9slhOAtnszB0bTYbvw6zcFQ/zuxFNzELd8Y7Md7++dftyek1ex/ij3//s91OmHpzt70pD4f/J4snPxyehk2W8Z3w2EFUcPnaYkKQ5GDJE73XnfgwkTIHC5IlSbZK4HDICOTziglEnJaP14zIcQg3plxBwlCtUP7yHY0SJoGMldLoPFspQwlY3sMKtWJK5pCzxGijdE4YXXFkZI4k/WRg5Z7jxIeaCAqEkrtk57kmcIEdEqUgywRsBk4GKjTRkG5MZ7DDnDORU320wxMfSs6FlPAlWiaQrFIKOBMJPKcmXEsjSMYIl+CyBDTOhxnwEkjsIx8ep8qdC6Wx3e3bvkdI3O0Vo022F49XHCON0zBOZ4s0DsN5mM7TRZzGMFqANpyDNgUtzIFN7EZOCzmcLmaPI2eeXv3r3PdX4vdj/t2H78b1+/D6/1Zc/ytxeOmvPH8F2/Qg+/At/v1wHl6EX0VBcr1+Top3NbCLCpJV2eJgcJVHV9V0BcnIFSRb3AdDFFxSkMTLdVW0tqyHKiqbAi5tu7RVUGNbWltXvoSbogwebFvgvqmBueibHlq0sRtctOVFBclqWFrb9q5WWtuii7qqrexYkGzrCwqSA/gsaiLcVM3QDLhpgqbBzTDgIYBx5O3Dz2XmAAOp63bVzc9q/7A5ipUJ4vDDj+fhQ3hz+wb4EH4j+A/Xxmr99FsFOwAAAABJRU5ErkJggg==)

Show all

Search Labs

Google apps

Google Account

paul lyu

paulchlyu@gmail.com