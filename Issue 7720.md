# Issue 7720: Digraph.reverse() should be rewritten more efficiently ( not hard )

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-12-17 12:47:49

Assignee: rlm

CC:  rlm

This function should be rewritten much more efficiently :

First, there should be a way to reverse the arcs "in place" ( without building a copy, by modifying the current graph -- I do not know if the expression used in frech translates in this case ). Such a function, for c_graphs, should be written in Cython and consist in the case of sparse graph in reverting the two copies kept of the graph.
In the end, this function should consist in an (optional) copy of the graph (=fast) and a call to the functionr reverting the arcs ( O(1) )

If possible and if deemed useful, the same should be made for NetworkX graphs.


---

Comment by rlm created at 2009-12-18 22:04:09

In case of a `SparseGraph`, the `SparseGraphBackend` has `self._cg` and `self._cg_rev`. They can merely be swapped. In the case of a `NetworkX` graph, I believe their digraphs have `succ` and `pred` dictionaries storing the adjacency information. These could also be swapped. For `DenseGraphs`, this is equivalent to switching between row ordering and column ordering in bitsets, which is inevitably costly.


---

Comment by jason created at 2010-03-17 05:27:05

Changing type from defect to enhancement.


---

Comment by ncohen created at 2010-06-06 11:00:56

Changing status from new to needs_work.
