# Issue 5935: graph theory docs -- sage: graphs_query.[tab]             # not tested

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 15:49:31

Assignee: rlm

Right at the top overview of graph theory the ref manual has the line

```
sage: graphs_query.[tab]             # not tested
```


http://www.sagemath.org/doc/reference/sage/graphs/graph.html

If it isn't tested it's broken, and that's the case here, since there is no graphs_query object available on the Sage command line.


---

Comment by ekirkman created at 2009-05-21 21:55:34

Changing assignee from rlm to ekirkman.


---

Comment by ekirkman created at 2009-05-21 21:55:34

Changing status from new to assigned.


---

Comment by ekirkman created at 2009-05-21 21:57:16

Marked as duplicate because this documentation change is covered in the patch for ticket #5936.


---

Comment by rlm created at 2009-07-08 20:30:52

Resolution: duplicate
