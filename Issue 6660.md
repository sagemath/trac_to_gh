# Issue 6660: Error in chromatic_number() and coloring() in the Graph class

Issue created by migration from https://trac.sagemath.org/ticket/6660

Original creator: ncohen

Original creation time: 2009-07-30 12:40:05

Assignee: rlm

The following code creates a Graph and computes its chromatic number :

sage: h=Graph(":I`ASWCaG`WaJC{afP")

sage: h.chromatic_number()

4

sage: h.coloring()

[[6, 8], [9], [0, 4, 7, 3], [1, 2, 5]]

Meanwhile, you can check that the coloring [[3, 9, 1], [9, 4, 0, 3], [3, 8, 5]] is valid with this code that checks that each class is actually an independent set.
:

for c in [[3, 9, 1], [9, 4, 0, 3], [3, 8, 5]]:

      print h.subgraph(c).connected_components_number()==len(c)


---

Comment by ncohen created at 2009-07-30 16:54:26

Answer from Rob Beezer on Sage-devel :

  It appears to me that this graph has chromatic number 4.  The three
  classes given for a 3-coloring do not include every vertex and have
  repeated vertices (namely 3 and 9).  Try the following:
  
  * Color the 4-5-6 triangle with three colors.
  
  * Color the 7-8-9 triangle with three colors where you will be forced to color vertex 8 the same color as vertex 5.
  
  * Vertex 1 is adjacent to 4, 6, 8, which now all have different colors, forcing a fourth color for vertex 1.
  
  * The coloring from  h.coloring()  seems to check as a legitimate 4-coloring.
  
  As an aside, maybe the graph6 format doesn't work so well in Trac? The back-ticks seem to have disappeared, leading to quite a different
graph.  ;-)
  
  Rob 

... which is perfectly right ! It came from a mistake I made in the LP relaxation... now fixed ! ;-)

This ticket can be deleted.

Nathann


---

Comment by rlm created at 2009-07-30 16:55:48

Resolution: invalid
