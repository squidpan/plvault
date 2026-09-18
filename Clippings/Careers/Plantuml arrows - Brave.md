---
categories:
  - "[[Clippings]]"
title: How to use plantuml arrows
source: https://search.brave.com/search?q=how+to+use+arrows+to+connect+things+in+plantuml+for+each+diagram+type+with+examples&source=web&summary=1&conversation=08e9095a7656e4b399954c9a5d219d112794
author:
  - "[[Plantuml arrows - Brave]]"
published:
created: 2026-03-31
description: How to use arrows to connect things in plantuml for each diagram type with examples
tags:
  - clippings
  - plantuml
url: https://search.brave.com/search?q=how+to+use+arrows+to+connect+things+in+plantuml+for+each+diagram+type+with+examples&source=web&summary=1&conversation=08e9095a7656e4b399954c9a5d219d112794
---
PlantUML uses different arrow syntaxes depending on the diagram type, but **directional arrows** (e.g., `-u->`, `-d->`, `-l->`, `-r->`) and **hidden links** (e.g., `- [hidden] >`) are the primary tools for controlling layout and connections across most diagrams.

### General Layout Arrows and Connections

For most diagram types (Class, Component, Deployment, etc.), arrows define both relationships and layout flow.

- **Directional Arrows**: Use specific prefixes to force a connection direction, overriding the default top-to-bottom or left-to-right flow.
	- `-u->` or `-up->`: Vertical bottom to top.
		- `-d->` or `-down->`: Vertical top to bottom.
		- `-l->` or `-left->`: Horizontal right to left.
		- `-r->` or `-right->`: Horizontal left to right.
		- `-->`: Default horizontal (left to right) or vertical (top to bottom) based on the global direction setting.
- **Hidden Connections**: To influence layout without drawing a visible line, use `-[hidden]>`. This connects elements to force positioning while remaining invisible in the final render.
- **Grouping**: Use `together { ... }` to force specific elements to stay adjacent, preventing other elements from appearing between them.

### Sequence Diagrams

Sequence diagrams rely on specific arrow heads to denote message types, lifelines, and message status.

- **Syntax**: `Sender -[type]-> Receiver : Message`
- **Arrow Styles**:
	- `-->`: Solid line (synchronous call).
		- `-->>`: Solid line with open arrow (asynchronous message).
		- `--|>`: Solid line with filled arrow (message to a specific target).
		- `..>`: Dashed line (return message).
		- `-x>`: Arrow with 'X' at the end (destruction message).
		- `-o>`: Arrow with 'o' at the end (lost message).
		- `<->`: Bidirectional arrow.
- **Short Arrow Syntax**: Using `?` allows shortening the arrow line to the label length (e.g., `?-> Receiver`).
- **Note**: In sequence diagrams, the **length** of the arrow line in code is ignored; Graphviz calculates the actual drawn length.

### Use Case Diagrams

Use case diagrams utilize arrows to connect actors to use cases and use cases to other use cases (include/extend).

- **Syntax**: `Actor -[style]-> UseCase` or `UseCase ..> UseCase`
- **Arrow Styles**:
	- `-up->`, `-down->`, etc.: Used to position use cases relative to actors.
		- `-[#color]-`: Specifies line color (e.g., `-[#blue]-`).
		- `..>`: Dashed line often used for relationships like `<<include>>` or `<<extend>>`.
- **Notes**: Notes can be linked using `note ... as N` followed by `N ..> Element`.

### State Diagrams

State diagrams use arrows to transition between states, with specific syntax for direction and stereotypes.

- **Syntax**: `State1 -- State2 : Transition Label`
- **Direction**: Can force direction using `-d-`, `-u-`, `-l-`, or `-r-` (shortened from `-down-`, etc.).
- **Special Points**:
	- `[*]`: Represents the start and end points.
		- `[H]` or `[H*]`: Represents history states (shallow and deep).
		- `||`: Separator for concurrent states within a composite state.

### Example: Combining Layout and Connection

To create a layout where element `A` is above `B` and `C` is hidden to the right:

```plantuml
@startuml
left to right direction
rectangle A
rectangle B
rectangle C
A -u-> B  ' Forces A above B
A --[hidden]> C  ' Hides C to the right of A
@enduml
```

### Styling Arrows

You can customize arrow appearance using `skinparam` or inline styles.

- **Thickness**: `skinparam ArrowThickness 3`
- **Color**: `-[#color]-` (e.g., `-[#red]-`)
- **Line Style**: `skinparam linetype ortho` (straight lines) or `polyline`.
- **Alignment**: `skinparam MessageAlignment left` to align text on the arrow.

[Can I change arrow color in PlantUML without affecting the diagram style?](https://search.brave.com/ask?q=Can%20I%20change%20arrow%20color%20in%20PlantUML%20without%20affecting%20the%20diagram%20style%3F&source=llmFollowup&quickAnswerKey=08e9095a7656e4b399954c9a5d219d112794&quickAnswerQuery=how%20to%20use%20arrows%20to%20connect%20things%20in%20plantuml%20for%20each%20diagram%20type%20with%20examples) 

[How do I make arrows bend or curve in PlantUML diagrams?](https://search.brave.com/ask?q=How%20do%20I%20make%20arrows%20bend%20or%20curve%20in%20PlantUML%20diagrams%3F&source=llmFollowup&quickAnswerKey=08e9095a7656e4b399954c9a5d219d112794&quickAnswerQuery=how%20to%20use%20arrows%20to%20connect%20things%20in%20plantuml%20for%20each%20diagram%20type%20with%20examples) 

[What does a dashed arrow mean in sequence diagrams?](https://search.brave.com/ask?q=What%20does%20a%20dashed%20arrow%20mean%20in%20sequence%20diagrams%3F&source=llmFollowup&quickAnswerKey=08e9095a7656e4b399954c9a5d219d112794&quickAnswerQuery=how%20to%20use%20arrows%20to%20connect%20things%20in%20plantuml%20for%20each%20diagram%20type%20with%20examples)

[Class Diagram syntax and features](https://plantuml.com/class-diagram)

For cardinality, you can use double-quotes "" on each side of the relation. You can **add an extra arrow pointing at one object showing which object acts on the other object, using < or > at the begin or at the end of the label**.

[Sequence Diagram syntax and features](https://plantuml.com/sequence-diagram)

In PlantUML sequence diagrams, the -> sequence denotes a message sent between two participants, which are automatically recognized and do not need to be declared beforehand. **Utilize dotted arrows by employing the --> sequence**, offering a distinct visualization in your diagrams.

[Component Diagram syntax and features](https://plantuml.com/component-diagram)

Links between elements are made using combinations of dotted line (..), straight line (--), and **arrows (-->) symbols**.

[6\. Layout — The Hitchhiker's Guide to PlantUML documentation](https://crashedmind.github.io/PlantUMLHitchhikersGuide/layout/layout.html)

Wrangling diagram elements to an exact position or layout is not what PlantUML is for. However, there are some layout tweak mechanisms that should be used sparingly. These are described here. We can specify a connection direction as follows and this affects the diagram layout:... The order in which diagram elements are defined can also impact how they are laid out.... Arrow head stypes per https://plantuml.com/sequence-diagram are for sequence diagrams only i.e.

[Drawing UML with PlantUML PlantUML Language Reference Guide (Version 1.2025.0)](https://pdf.plantuml.net/PlantUML_Language_Reference_Guide_en.pdf)

In PlantUML sequence diagrams, the -> sequence denotes a message sent between two participants, which · are automatically recognized and do not need to be declared beforehand. **Utilize dotted arrows by employing the --> sequence**, offering a distinct visualization in your diagrams.[graphviz - PlantUML: control arrow shape and direction - Stack Overflow](https://stackoverflow.com/questions/37702453/plantuml-control-arrow-shape-and-direction)[To answer the original question for future readers:](https://stackoverflow.com/questions/37702453/plantuml-control-arrow-shape-and-direction)

[**In order to have only horizontal or vertical straight lines drawn, you can use `skinparam linetype ortho`.**

In order to make all lines straight (but not necessarily horizontal or vertical) you can use `skinparam linetype polyline`.

(source)

](https://stackoverflow.com/questions/37702453/plantuml-control-arrow-shape-and-direction)[

PlantUML has not been designed to provide nice straight arrows when many directions are imposed. Using default layout provides cleanest and most readable result to me.

Here is an example with the same meaning, but without layout issues:

```
@startuml

state Powered {
  [*] --> Starting
  Starting --> Operational
}
[*] --> Powered : Power On
Powered --> [*] : Power Off
Powered --> Powered : Reset
Powered --> Powered : Fatal Error

@enduml
```

EDIT: I also changed your `Powered --> Starting : Fatal Error` transition to: `Powered --> Powered : Fatal Error`, which better expresses that from any state within Powered, a Fatal Error event will restart at the Starting substate.

Alternatively the two statements:

```
Powered --> Powered : Reset
Powered --> Powered : Fatal Error
```

can be merged in:

```
Powered --> Powered : Reset, Fatal Error
```

see OMG UML 2.5 format specification section 14.2.4.9 page 329

```
[<trigger> [‘,’ <trigger>]* [‘[‘ <guard>’]’] [‘/’ <behavior-expression>]]
```

](https://stackoverflow.com/questions/37702453/plantuml-control-arrow-shape-and-direction)

[

PlantUML layout and styles tutorial | AugmentedMind.de

](https://www.augmentedmind.de/2021/01/17/plantuml-layout-tutorial-styles/)

February 15, 2021 - For instance, imagine a diagram... this is the top to bottom direction. This is why a statement such as **A --> B produces an arrow going from top to bottom**....

[![](https://imgs.search.brave.com/4YSmia2fhTiuxbkVLI0gOz0JMcDH_vv8qDcmEfTn7as/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly93d3cu/YXVnbWVudGVkbWlu/ZC5kZS93cC1jb250/ZW50L3VwbG9hZHMv/MjAyMS8wMS9wbGFu/dHVtbC1sYXlvdXQt/ZmVhdHVyZS5wbmc)](https://www.augmentedmind.de/2021/01/17/plantuml-layout-tutorial-styles/)

[![](https://imgs.search.brave.com/4YSmia2fhTiuxbkVLI0gOz0JMcDH_vv8qDcmEfTn7as/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly93d3cu/YXVnbWVudGVkbWlu/ZC5kZS93cC1jb250/ZW50L3VwbG9hZHMv/MjAyMS8wMS9wbGFu/dHVtbC1sYXlvdXQt/ZmVhdHVyZS5wbmc)](https://www.augmentedmind.de/2021/01/17/plantuml-layout-tutorial-styles/)

[

Activity Diagram syntax and features

](https://plantuml.com/activity-diagram-legacy)

It is possible to force arrow's direction using the following syntax:... You can use if/then/else keywords to define branches. Unfortunately, you will have to sometimes repeat the same activity in the diagram text: By default, a branch is connected to the last defined activity, but it is possible to override this and to define a link with the if keywords.[Is it possible to draw standalone arrows with PlantUML? - Stack Overflow](https://stackoverflow.com/questions/73403791/is-it-possible-to-draw-standalone-arrows-with-plantuml)> [
> 
> Is there a way to tell PlantUML to simply draw a small segment of a specific arrow type?
> 
> ](https://stackoverflow.com/questions/73403791/is-it-possible-to-draw-standalone-arrows-with-plantuml)

[

Generally speaking, no, especially not in a legend.

However, I can think of a way (it's somewhat complicated). A legend will let you include images, and you can use PlantUML to generate each arrow image.

Here's one example to get a regular arrow (I'm making the classes small and hiding them with some magic):

```
skinparam style strictuml
scale 0.5
hide empty members
skinparam Class {
    BorderColor transparent
    BackgroundColor transparent
    FontColor transparent
}
class " " as A
class " " as B
A -> B
```

If you render that, you get a URL of https://www.plantuml.com/plantuml/png/ROpB2i9034Nt-OhWNd7ZLkWK\_8yu4tJeF4gIBahntmqAWcWk10udkJhbDfDGHRMri6\_9qPPQG2Cv7mydkEV4o7Ms5IlNAuk2Vjx6Gggu0Vg4BebbxAKBcb1JF-5cRqTnkabVMlhlBxtPhtb0VFNlFAGuV6E00VTd34y0 which looks like

Next, you plug that URL into an `<img:>` tag in a legend of another diagram:

```
@startuml test
legend
    | <img:https://www.plantuml.com/plantuml/png/ROpB2i9034Nt-OhWNd7ZLkWK_8yu4tJeF4gIBahntmqAWcWk10udkJhbDfDGHRMri6_9qPPQG2Cv7mydkEV4o7Ms5IlNAuk2Vjx6Gggu0Vg4BebbxAKBcb1JF-5cRqTnkabVMlhlBxtPhtb0VFNlFAGuV6E00VTd34y0> | regular arrow |
end legend
@enduml
```

The result is

](https://stackoverflow.com/questions/73403791/is-it-possible-to-draw-standalone-arrows-with-plantuml)[Plantuml several arrows between two classes - Stack Overflow](https://stackoverflow.com/questions/71811493/plantuml-several-arrows-between-two-classes)[I don’t know how to directly reach your goal of a more legible arrow layout but you could avoid the problem by using Person as a generalisation for four sub-classes such as Actor, Director, Producer and ScreenplayWriter. Each of these would have separate arrows and it might make your diagramme also generally clearer (the latter is, of course, subject to your taste and the diagramme’s purpose)](https://stackoverflow.com/questions/71811493/plantuml-several-arrows-between-two-classes)[

You have to make class appear bigger, so there will be more space for associations to render. There is no skinparam for that (the only one is for minWidth). But with a trick, you can make class body bigger.

planuml example

planuml code:

```js
@startuml

skinparam ranksep 150
skinparam linetype ortho
left to right direction
hide methods
skinparam style strictuml

class Movie {
    genres: String[]
    minutes: Integer
    movie_id: String
    rating: Float
    title: String
    type: String
    votes: Integer
    year: Integer
    \n\n\n\n\n\n
}

class Person {
    birthYear: Integer
    deathYear: Integer
    name: String
    person_id: String
    \n\n\n\n\n\n\n
}

(Person,Movie) . Role
Person "0..*" - " 1..* " Movie : acted_in
Person "0..*" -> " 1..* " Movie : directed
Person "0..*" -> " 1..* " Movie : produced
Person "\n\n0..*" - "\n\n1..*" Movie : wrote

class Role {
    name: String
}
@enduml
```

](https://stackoverflow.com/questions/71811493/plantuml-several-arrows-between-two-classes)[uml - How to realize direct arrows with PlantUML? - Stack Overflow](https://stackoverflow.com/questions/60615999/how-to-realize-direct-arrows-with-plantuml)[you cannot have several flows starting from an action nor several flows going to an action](https://stackoverflow.com/questions/60615999/how-to-realize-direct-arrows-with-plantuml)

[

for the UML point of view so you need to add:

1. a decision node after the action "to solve" to have your two flows, each with a guard
2. a decision node after the action "erledigt" to have your two flows, each with a guard
3. a merge node before the action "to solve" to receive the flows from the decision node "check successful" and the action "erledigt".

For (1) use a "if-else" or a "split" in PlantUML

> ```
> start
> 
> :new - please check;
> 
> while (check sucessful?) is (is an error)
>   :to solve;
>   if (duration) then (long)
>     :in progress;
>   else (immediat)
>   endif
>   :solved;
> endwhile (not an error)
> 
> :erledigt;
> note left
>     reason:
>      * done
>      * not an error
>      * not fixable
> end note
> stop
> 
> @enduml
> ```

For (3) may be you can use a "repeat while" also managing (2), but not sure you can in PlantUML without duplicating the three actions (to solve - in progress - solved) or doing them in an other activity you call. In PlantUML the code is drawn from control-structure except "goto", that allows to not cross lines, but you need a "goto" crossing lines. Note there is no problem going to the decision "check sucessfull" rather than to the action "to solve"

](https://stackoverflow.com/questions/60615999/how-to-realize-direct-arrows-with-plantuml)

[

IMHO you are using the wrong diagram here: If you are using a StateDiagram instead of an ActivityDiagram you can add multiple connections between the nodes. That's at least what I think you want to express with the initial diagram.

The necessary activities are usually placed at the arrows then.

](https://stackoverflow.com/questions/60615999/how-to-realize-direct-arrows-with-plantuml)

[

UML Use Case Diagram — Ashley's PlantUML Doc 0.2.01 documentation

](https://plantuml-documentation.readthedocs.io/en/latest/diagrams/usecase.html)

Here is a very ugly example that uses differen kinds of arrows to connect a note. (It’s shortened from the above diagram)... @startuml '!include../../plantuml-styles/plantuml-ae.iuml skinparam ActorBorderColor SaddleBrown skinparam NoteFontStyle normal skinparam Shadowing false title Usecase Diagrams: Connecting Notes to Objects (Use the application) as (Use) User -\[#LightSlateGray\]-> (Start) User -\[#LightSlateGray\]-> (Use) note "This note is connected to \\n two use cases \\n and the User actor." as N2 #white (Start) <<-\[#orange\]- N2 N2.\[#magenta\].|> (Use) User <==\[#DeepSkyBlue\]==> N2 '!include../../plantuml-styles/ae-copyright-footer.txt @enduml[graph - plantuml - better disposition of arrows and text - Stack Overflow](https://stackoverflow.com/questions/65631447/plantuml-better-disposition-of-arrows-and-text)[When a diagram is complex, it can be a nondeterministic struggle to make it more readable. Some suggestions:](https://stackoverflow.com/questions/65631447/plantuml-better-disposition-of-arrows-and-text)

[
- make the associations wider with `skinparam ArrowThickness 3` or change the font for the text on the arrows to bold in a similar way.
- try `skinparam linetype polyline`
- put the names at the start or the end of an arrow, e.g. instead of `panel --> eee : run` use `panel "run" --> eee` (for the name at the start) or `panel --> "run" eee` (for the name at the end)
- group two packages inside a `together {...}` (it's like a hidden rectangle, and will perhaps add more space).
- toggle the `left to right direction` instruction (with a comment).

Here are a few of things applied to your diagram, but it could be better:

```
@startuml
skinparam linetype polyline
'left to right direction

skinparam Arrow {
    MessageAlignment left
    Thickness 3
    FontStyle Bold
    Color Blue
}

folder BASE {
    folder foo {
        component aaa
    }
    folder bar {
        component bbb
        folder ENV {
              artifact ccc <<config>>
              artifact ddd <<db>>
        }
    }

}

folder lorem {
    folder ipsum {
        component eee
        component fff
        component ggg
    }
    folder amet {
        component panel <<jar>>
    }
    folder dolor {
        artifact hhh <<config>>
    }
}

folder fox {
    folder jumps {
    artifact jjj <<document>>
    artifact kkk <<document>>
    artifact mmm<<document>>

    }
    folder lazy {
        artifact context.txt
    }
}

aaa --> "write" context.txt
aaa --> "launch" bbb 
bbb --> "read" hhh
bbb --> panel : launch
panel --> ccc : read
panel --> ddd : read

panel --> eee : run
panel --> fff : run
panel --> ggg : run

panel --> kkk : write
eee --> jjj : read
eee --> mmm: write

ggg --> jjj : write
ggg --> mmm: read
@enduml
```
](https://stackoverflow.com/questions/65631447/plantuml-better-disposition-of-arrows-and-text)

[

UML Sequence Diagram — Ashley's PlantUML Doc 0.2.01 documentation

](https://plantuml-documentation.readthedocs.io/en/latest/diagrams/sequence.html)

@startuml title The length you make arrow lines is ignored in Sequence Diagrams. end title A ----------------------------------->> B A <<----------> C A <- D caption: \\nEven though you made the arrow line\\n from A to B the longest,\\n their lengths are calculated and this\\n calculated length is what's drawn. '!include../../plantuml-styles/ae-copyright-footer.txt @enduml

[

Use case Diagram syntax and features

](https://plantuml.com/use-case-diagram)

To link actors and use cases, the **arrow -->** is used.

[

State Diagram syntax and features

](https://plantuml.com/state-diagram)

You can use \[\*\] for the starting point and ending point of the state diagram. **Use --> for arrows**.

[

Quick Guide to PlantUML: Diagrams, Syntax & Best Practices | Miro

](https://miro.com/diagramming/what-is-plantuml/)

This tells the PlantUML parser where your diagram begins and ends. Entities and relationships: Use keywords like class, interface, and entity to define elements, and **arrows to show relationships**.

[

Understanding Use Case Diagrams - PlantText

](https://blog.planttext.com/2024/10/14/understanding-use-case-diagrams/)

January 21, 2025 - This sample shows the PlantUML for a variety of associations (connectors) you can use in your Use Case Diagram – solid or dashed – as well as how to point the arrow in the desired direction. Often dashed lines are used to note extends/includes types of associations, where solid lines note simple association (although that is not reflected in the sample below).

[![](https://imgs.search.brave.com/gjuqBZL3m2R2fUFQac_SBALKhptkMs2GfJBGsoOYTU0/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly9ibG9n/LnBsYW50dGV4dC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MjQvMTAvVXNlQ2Fz/ZS1yZXZpc2VkLnBu/Zw)](https://blog.planttext.com/2024/10/14/understanding-use-case-diagrams/)

[![](https://imgs.search.brave.com/gjuqBZL3m2R2fUFQac_SBALKhptkMs2GfJBGsoOYTU0/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly9ibG9n/LnBsYW50dGV4dC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MjQvMTAvVXNlQ2Fz/ZS1yZXZpc2VkLnBu/Zw)](https://blog.planttext.com/2024/10/14/understanding-use-case-diagrams/)

[

how to create straight or rectangular arrows within mindmaps · plantuml/plantuml · Discussion #1017

](https://github.com/plantuml/plantuml/discussions/1017)

According to plantuml's mindmap docs, I can generally adjust the arrow style like this (there are styling options for line style, line thickness and line color): **<style> arrow { LineStyle 4 LineThickness 0.5 LineColor green } </style>**... \* Hi...

[![](https://imgs.search.brave.com/bi6zHXo4vqas5L1AV6DFdkH91hoKS3_22gA_d6dB33k/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly9vcGVu/Z3JhcGguZ2l0aHVi/YXNzZXRzLmNvbS9h/MzE5MTJlZGRmZWMz/NjI2ZTU4NmI3MzVl/YTNiZDIwYjNmZmI2/N2YzMjQ5NGI2YjI5/M2ZhOGM3MTA2Y2Iz/MzY0L3BsYW50dW1s/L3BsYW50dW1sL2Rp/c2N1c3Npb25zLzEw/MTc)](https://github.com/plantuml/plantuml/discussions/1017)

**Author** plantuml

[![](https://imgs.search.brave.com/bi6zHXo4vqas5L1AV6DFdkH91hoKS3_22gA_d6dB33k/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly9vcGVu/Z3JhcGguZ2l0aHVi/YXNzZXRzLmNvbS9h/MzE5MTJlZGRmZWMz/NjI2ZTU4NmI3MzVl/YTNiZDIwYjNmZmI2/N2YzMjQ5NGI2YjI5/M2ZhOGM3MTA2Y2Iz/MzY0L3BsYW50dW1s/L3BsYW50dW1sL2Rp/c2N1c3Npb25zLzEw/MTc)](https://github.com/plantuml/plantuml/discussions/1017)

[

arrows between shapes in different sub-diagrams · Issue #2251 · plantuml/plantuml

](https://github.com/plantuml/plantuml/issues/2251)

June 21, 2025 - It'd be useful to be able to draw connectors between shapes in different sub-diagrams. The line c -> d in the code below currently creates 2 new participants, c and d, and draws a line betwe...

**Author** GavinPen

[Next](https://search.brave.com/search?q=how%20to%20use%20arrows%20to%20connect%20things%20in%20plantuml%20for%20each%20diagram%20type%20with%20examples&offset=1&spellcheck=0)