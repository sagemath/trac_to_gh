# Issue 6684: warnings when building reference manual in Sage 4.1.1.rc2

Issue created by migration from https://trac.sagemath.org/ticket/6684

Original creator: mvngu

Original creation time: 2009-08-07 10:39:55

Assignee: tba

CC:  jhpalmieri

I received the following warning messages when building the reference manual under Sage 4.1.1.rc2:

```
WARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.kirchhoff_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.laplacian_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.clique_number:19: (WARNING/2) Inline literal start-string without end-string.
```



---

Attachment

based on Sage 4.1.1.rc2


---

Comment by jhpalmieri created at 2009-08-07 16:15:24

This fixes the warnings and the rendering of this page of the reference manual.  All tests pass.


---

Comment by mvngu created at 2009-08-11 23:20:04

Resolution: fixed
