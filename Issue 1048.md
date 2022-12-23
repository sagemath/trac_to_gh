# Issue 1048: graphs: Create filtered views of graphs

Issue created by migration from https://trac.sagemath.org/ticket/1048

Original creator: jason

Original creation time: 2007-11-01 00:11:33

Assignee: was

Keywords: graphs

Boost has a nice concept of "filters" of a graph.  They provide views into subsets of the vertices and/or edges of the graph, based on predicate functions.  That would be nice to have.

See [http://www.boost.org/libs/graph/doc/filtered_graph.html](http://www.boost.org/libs/graph/doc/filtered_graph.html)




---

Comment by jason created at 2007-11-01 12:36:41

This maybe best implemented by creating another "XGraph" or "XDiGraph" class which holds the basic graph information.


---

Comment by rlm created at 2007-12-17 15:10:59

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:10:59

Changing keywords from "graphs" to "".
