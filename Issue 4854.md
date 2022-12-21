# Issue 4854: represent paths as lists of edges

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-12-22 19:24:26

Assignee: rlm

CC:  brunellus

From sage-devel:

```
While trying to model deterministic finite automata over Sage
(multi-)graphs,
I've run into the following: paths are represented as lists of vertices,
regardless
of edges. Superficial investigation shows that both sage.graph and
networkx are somewhat grounded on this notion of path.

But! For finite automata and other word-accepting machines to be correctly
represented paths should be considered as sequences of labeled edges, not
vertices, as far as two vertices may be connected by differently labeled
edges, and that is essential. 
```



---

Comment by AlexGhitza created at 2009-01-22 18:26:58

Changing type from defect to enhancement.


---

Comment by ncohen created at 2009-08-14 16:05:20

Hmmmm... As I have not met any Patch class in Sage, I assume you are using functions on graphs returning paths, which are not encoded as you may like.... Could you tell me which functions you are talking about, in case I made no mistake ? :-)


---

Comment by ncohen created at 2010-02-22 21:33:20

Changing status from new to needs_info.


---

Comment by mvngu created at 2010-04-19 03:18:27

What might be required is a keyword such as "as_edge" for methods that return paths. So if "as_edge=True", return the path as a list of edges. If "as_edge=False" (which is default), return the path as a list of vertices.
