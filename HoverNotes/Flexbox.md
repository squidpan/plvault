---
title: "Course: The Complete Full-Stack Web Development Bootcamp | Udemy"
description: >-
  Become a Full-Stack Web Developer with just ONE course. HTML, CSS, Javascript,
  Node, React, PostgreSQL, Web3 and DApps
author: Stack Web Development Bootcamp | Udemy
source: >-
  https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368230#overview
created: "2026-04-03"
tags:
  - hover-notes
  - udemy
categories: "[[Clippings]]"
---
[00:09:06](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368230#overview)

![00:09:15](hover-notes-images/screenshot-01KN9Z66SKTEPPS2YQ0Q9PSH7T.png)
[00:09:15](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368230#overview)

![00:09:40](hover-notes-images/screenshot-01KN9Z6YVW0M9WXVHV6RD0GFGN.png)
[00:09:40](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368230#overview)

![00:10:04](hover-notes-images/screenshot-01KN9Z7PNCMEZCTZ5WAPKBTAWP.png)
[00:10:04](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368230#overview)

![00:12:25](hover-notes-images/screenshot-01KN9ZC099D1YNCPMVS1PBDF2M.png)
[00:12:25](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368230#overview)

# Flex direction

[00:02:10](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)

![00:02:30](hover-notes-images/screenshot-01KN9ZYRGAHPJANEY3C0WY0VJN.png)
[00:02:30](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)
[00:03:06](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)

![00:03:12](hover-notes-images/screenshot-01KNA001R6W6W2M6SWCMB5QTBH.png)
[00:03:44](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)

![00:03:48](hover-notes-images/screenshot-01KNA014G4D7FHQ0FC61RQX7Q0.png)
[00:03:48](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)

![00:04:27](hover-notes-images/screenshot-01KNA02BBDTSZBCV3S0G233ZKP.png)
[00:04:27](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)

width is changed for row

![00:06:07](hover-notes-images/screenshot-01KNA05WR1WGQS6MSS9H2WDRM3.png)
[00:06:07](https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37368266#overview)

flex-basis is set on child items and not on the container

use only css to target divs look at hint in index.html

## Child combinator

The **child combinator** (`>`) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the direct children of elements matched by the first. Descendant elements further down the hierarchy don't match. For example, to select only `<p>` elements that are direct children of `<article>` elements:

```javascript
article > p {
  /* … */
}
```

# Universal selectors

```javascript
/* Selects all elements */
* {
  color: green;
}
```

by default, display: flex; will occupy the full width

inline-flex will occupy widest bit of content as width

flex-basis need to apply to flex items and not the parent container. So need to target all of div's children. so use combinators direct children