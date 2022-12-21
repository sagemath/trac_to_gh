# Issue 1962: set_edge_label creates edges when multiple edges are allowed

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-01-28 19:49:16

Assignee: rlm


```
sage: g = Graph({0: [0,1,1,2]}, loops=True, multiedges=True)
sage: g.set_edge_label(0,0,'test')
sage: g.edges()

[(0, 0, 'e'),
 (0, 0, 's'),
 (0, 0, 't'),
 (0, 0, 't'),
 (0, 1, None),
 (0, 1, None),
 (0, 2, None)]
```


I suggest that set_edge_labels should *never* create an edge or the function name should be changed.


---

Comment by rlm created at 2008-02-17 00:07:50

This is not a bug in `set_edge_label` itself:

```
sage: g._nxg.adj
{0: {0: 'test', 1: [None, None], 2: [None]},
 1: {0: [None, None]},
 2: {0: [None]}}
```

It is in fact a bug in NetworkX's `edges` function:

```
sage: g._nxg.edges()
[(0, 0, 't'),
 (0, 0, 'e'),
 (0, 0, 's'),
 (0, 0, 't'),
 (0, 1, None),
 (0, 1, None),
 (0, 2, None)]
```



---

Comment by rlm created at 2008-02-17 00:09:28

My mistake: when multiple edges is True, the representation is slightly different:

```
sage: G = Graph({0:[1]})
sage: G._nxg.adj
{0: {1: None}, 1: {0: None}}
sage: G = Graph({0:[1]}, multiedges=True)
sage: G._nxg.adj
{0: {1: [None]}, 1: {0: [None]}}
```



---

Comment by rlm created at 2008-02-17 00:11:27

In fact, `set_edge_label` only makes sense when there is only one possible edge whose label is to be set: if there is more than one, which label to set?


---

Attachment


---

Attachment

After discussion on IRC, this looks good to me.  Apply.  Needs both patches, -ref second.


---

Comment by mabshoff created at 2008-02-26 01:08:26

Merged both patches in Sage 2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-26 01:08:26

Resolution: fixed
