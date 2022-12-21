# Issue 1047: graphs: Create the "visitor" concept in Boost

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-01 00:03:55

Assignee: was

Keywords: graphs

Boost has a "visitor" concept.  Basically, you pass a graph traversal method an object.  As the graph traversal function goes through the graph, it invokes functions from your object.  So it's easy to do a depth-first something, for example.  It applies to stuff beyond depth-first and breadth-first too, for example, creating a spanning tree, etc.

See [http://www.boost.org/libs/graph/doc/visitor_concepts.html](http://www.boost.org/libs/graph/doc/visitor_concepts.html)


---

Comment by rlm created at 2007-12-17 15:10:42

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:10:42

Changing component from combinatorics to graph theory.
