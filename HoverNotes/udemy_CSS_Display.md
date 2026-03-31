---
title: "Course: The Complete Full-Stack Web Development Bootcamp | Udemy"
description: >-
  Become a Full-Stack Web Developer with just ONE course. HTML, CSS, Javascript,
  Node, React, PostgreSQL, Web3 and DApps
author: Stack Web Development Bootcamp | Udemy
source: >-
  https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368052#content
created: "2026-03-28"
tags:
  - hover-notes
  - udemy
categories: "[[Hovernotes]]"
---

### Paragraph Element Behavior

- `<p>` is a **block-level** element
    - Takes up the **full width** of the webpage (border spans entire container)
    - Causes text to wrap to new lines based on content length and container width

### Span Element Introduction

- `<span>` is an **inline** element
    - Used when you don't want full-width spanning
    - Allows short text to stay on the same line without forcing wraps

### Span Element Usage in Paragraph

- Span nests **inside** other elements like `<p>` to target specific inline content
    - Example code:

```html
<p> Hello <span> Beautiful </span> World </p>
```

    - Structure: open `<span>`, content ("Beautiful"), close `</span>`, surrounded by paragraph text and tags
- Result: "Hello Beautiful World" renders on one line, with span wrapping just the highlighted word

### Span Element Display Property

- Span elements default to `display: inline`
    - Allows content to stay on the **same line** without forcing new lines (unlike block elements like `<p>` or default `<h2>`)
- Example: Two `<h2>` elements with `display: inline` render side-by-side

```html
<h2>Harry</h2>
<h2>Potter</h2>
```

```css
h2 {
  display: inline;
}
```

- Rendered result: **Harry Potter** (on one line)
    - Without `display: inline`, each `<h2>` stacks on a new line

### Default Display Values

- Most elements default to `display: block`
    - Creates **full-width blocks** that stack vertically (each on new line)
    - Explains why `<p>` and default `<h2>` take full width and force line breaks
- `display: inline` (like `<span>` default) flows elements **side-by-side**
    - No new lines needed; content stays on same line
    - Can override block defaults via CSS to change layout

```css
h2 {
  display: inline;
}
```

- Result: Multiple block elements render inline when changed

### CSS Display Property Introduction

- `display` property has **many possible values**
- Three main ones covered: **block**, **inline**, **inline-block** (mixture of block + inline behaviors)

### Inline-Block Display

- Hybrid value combining block and inline characteristics (details to follow)

### Block Display Behavior

- `display: block` forces subsequent elements **below** the current one
    - No sharing of the same line
    - Visual: full-width block followed by next block underneath

### Inline Display Behavior

- `display: inline` allows multiple elements to flow **side-by-side** on the same line
    - Example: span "Hello" + span "World" render next to each other
    - Continues until no more space fits
    - Visual: two side-by-side boxes on one line

```css
span {
  display: inline;
}
```

### Inline Display Limitations

- Inline elements **cannot set width or height**
    - They default to the **size of their content**
    - Reason: Browser sizes box exactly to fit text (e.g. span with 'Hello' only as wide as 'Hello' needs)
    - Visual: Tight-fitting boxes around 'Hello' | 'World' with no extra space

```css
span {
  display: inline;
  /* width: 100px; → ignored */
  /* height: 50px; → ignored */
}
```

- Contrast with block: Block elements respect explicit width/height settings

### Inline Display Behavior (Continued)

- Inline elements stretch to fit the size of their content.

### Inline-Block Display

- A hybrid between `inline` and `block` display types.
- Allows setting both **height** and **width**.
- `display: inline-block` allows elements to be on the same line. Elements can go in the same line.
- You can set height and width.

### Inline-Block Display Characteristics

- **Hybrid behavior**: Halfway point between `inline` and `block`
    - Like **inline**: Multiple elements flow **side-by-side** on the same line (e.g. two `inline-block` elements stay on one line)
    - Like **block**: Allows setting explicit **width** and **height** (ignored by pure `inline`)

```css
/* Example context */
element {
  display: inline-block;
  width: 100px;   /* Respected */
  height: 50px;   /* Respected */
}
```

- Visual: Two boxes `[ Hello ] [ World ]` next to each other, each with controllable dimensions
    - Arrows show **set height & width** and **elements on same line**

### Inline-Block Side-by-Side Placement

- Inline-block elements with **different sizes** flow onto the **same horizontal line** if enough webpage width available
    - Example: One `200 x 200` box next to one `20 x 100` box
    - Visual: Two boxes side-by-side with independent dimensions

```css
/* Both elements: */
element1 {
  display: inline-block;
  width: 200px;
  height: 200px;
}
element2 {
  display: inline-block;
  width: 20px;   /* Narrower */
  height: 100px; /* Shorter */
}
```

- Key: **Sizing respected** + **inline flow** = flexible layout on one line

### Display: None

- **`display: none`** completely removes element from screen (invisible and takes no space)
    - Use case: Buttons that hide/show elements (e.g. toggle visibility)

```css
display: none;
```

- Visual: Yellow square disappears entirely when set to `none`
    - Before: Visible box on page
    - After: Nothing renders (no box, no space occupied)
- Summary: `block`/`inline`/`inline-block` control **layout**; `none` controls **visibility**

### Display Property Demo Site

- Example website: `appru.github.io/css-display`
    - Features **two elements** (Red Box, Blue Box)
    - Includes **box model controls**:
        - Box-sizing, Box-margin, Box-padding, Box-height, Box-width, Box-border, Box-border-width
- **Purpose**: Hands-on exploration of display property values and effects

### Display Property Interactive Demo on Paragraphs

- Demo uses **three paragraph elements** all set to different displays:
    - Block paragraph
    - Inline paragraph
    - Inline-block paragraph
- **Controls** adjust height/width for all three:
    - Block Height: slider
    - Block Width: slider
    - Inter-block Margin: slider
    - Inter-block Height: slider
    - Inter-block Width: slider
- **Block behavior confirmation**:
    - Height/width changes respected
    - **No line flow impact**: Shrinking width doesn't pull next line up (stays stacked vertically)
- **Inline behavior confirmation**:
    - Height/width settings **ignored** (size locked to content)

```css
/* Visualized via sliders */
p.block-para { display: block; }
p.inline-para { display: inline; }
p.inline-block-para { display: inline-block; }
```

- Visual: Red box ('1'), Blue box ('2' & '3'), sliders below for real-time experimentation