# Issue 3402: Digraph.incoming_edges forgets labels

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-06-12 05:48:36

Assignee: tbd


```
sage: dg = DiGraph({0 : [1], 1 : [0]})
sage: dg.set_edge_label(0,1,5)
sage: dg.set_edge_label(1,0,9)
sage: dg.edges()
[(0, 1, 5), (1, 0, 9)]
sage: dg.outgoing_edges([1])
[(1, 0, 9)]
sage: dg.incoming_edges([1])
[(0, 1, None)]
sage: dg.outgoing_edges(0)
[(0, 1, 5)]
sage: dg.incoming_edges(0)
[(1, 0, None)]
```


As you can see, outgoing_edges remembers the labels but incoming_edges does not.


---

Comment by mhansen created at 2008-06-12 05:54:17

Changing assignee from tbd to rlm.


---

Comment by mhansen created at 2008-06-12 05:54:17

Changing component from algebra to graph theory.


---

Attachment


---

Comment by bump created at 2008-06-13 14:28:06

The incoming edge iterator depends on self._backend._nxg which is a NetworkX XDigraph. This digraph has separate iterators for incoming and outgoing edges that depend on dictionaries self._backend._nxg.succ and self._backend._nxg.pred. Before the patch, self._backend._nxg.pred was not getting initialized.

The patch is obviously correct and I've also tested it.


---

Comment by mabshoff created at 2008-06-16 04:30:01

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-16 04:30:01

Resolution: fixed
