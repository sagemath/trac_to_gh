# Issue 1961: graph_isom bug

Issue created by migration from https://trac.sagemath.org/ticket/1961

Original creator: rlm

Original creation time: 2008-01-28 18:24:35

Assignee: rlm


```
g1 = graphs.EmptyGraph()
g2 = graphs.EmptyGraph()

g1.add_edges([(1, 17, None), (1, 21, None), (1, 25, None), (2, 17,
None), (2, 22, None), (2, 26, None), (3, 17, None), (3, 23, None), (3,
27, None), (4, 17, None), (4, 24, None), (4, 28, None), (5, 18, None),
(5, 21, None), (5, 26, None), (6, 18, None), (6, 22, None), (6, 27,
None), (7, 18, None), (7, 23, None), (7, 28, None), (8, 18, None), (8,
24, None), (8, 25, None), (9, 19, None), (9, 21, None), (9, 27, None),
(10, 19, None), (10, 22, None), (10, 28, None), (11, 19, None), (11,
23, None), (11, 25, None), (12, 19, None), (12, 24, None), (12, 26,
None), (13, 20, None), (13, 21, None), (13, 28, None), (14, 20, None),
(14, 22, None), (14, 25, None), (15, 20, None), (15, 23, None), (15,
26, None), (16, 20, None), (16, 24, None), (16, 27, None), (17, 29,
None), (18, 29, None), (19, 29, None), (20, 29, None), (21, 30, None),
(22, 30, None), (23, 30, None), (24, 30, None), (25, 31, None), (26,
31, None), (27, 31, None), (28, 31, None)])

g2.add_edges([(1, 17, None), (1, 21, None), (1, 28, None), (2, 17,
None), (2, 22, None), (2, 25, None), (3, 17, None), (3, 23, None), (3,
26, None), (4, 17, None), (4, 24, None), (4, 27, None), (5, 18, None),
(5, 21, None), (5, 26, None), (6, 18, None), (6, 22, None), (6, 27,
None), (7, 18, None), (7, 23, None), (7, 28, None), (8, 18, None), (8,
24, None), (8, 25, None), (9, 19, None), (9, 21, None), (9, 27, None),
(10, 19, None), (10, 22, None), (10, 28, None), (11, 19, None), (11,
23, None), (11, 25, None), (12, 19, None), (12, 24, None), (12, 26,
None), (13, 20, None), (13, 21, None), (13, 25, None), (14, 20, None),
(14, 22, None), (14, 26, None), (15, 20, None), (15, 23, None), (15,
27, None), (16, 20, None), (16, 24, None), (16, 28, None), (17, 29,
None), (18, 29, None), (19, 29, None), (20, 29, None), (21, 30, None),
(22, 30, None), (23, 30, None), (24, 30, None), (25, 31, None), (26,
31, None), (27, 31, None), (28, 31, None)])

perm = {0:0, 1: 13, 2: 14, 3: 15, 4: 16, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
10: 10, 11: 11, 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 20, 18: 18,
19: 19, 20: 17, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27:
27, 28: 28, 29: 29, 30: 30, 31: 31}

# This says no:
print g1.is_isomorphic(g2)

# But I can find a vertex relabelling...
g1.relabel(perm)
# ... and this says yes:
print g1.is_isomorphic(g2)
```



---

Comment by rlm created at 2008-01-28 19:11:16

Changing status from new to assigned.


---

Comment by rlm created at 2008-02-06 19:08:17

The real problem can be boiled down a little:

```
sage: G = Graph('^????????????????????{??N??@w??FaGa?PCO@CP?AGa?_QO?Q@G?CcA??cc????Bo????{????F_')
sage: G.relabel([i+1 for i in xrange(31)])
sage: perm = {4:16, 16:4}
sage: A = G.canonical_label()
sage: B = G.relabel(perm, inplace=False).canonical_label()
sage: A == B
False
```



---

Comment by rlm created at 2008-02-06 19:54:23

Slightly easier to digest still:

```
sage: G = Graph('^????????????????????{??N??@w??FaGa?PCO@CP?AGa?_QO?Q@G?CcA??cc????Bo????{????F_')
sage: perm = {3:15, 15:3}
sage: H = G.relabel(perm, inplace=False)
sage: G.canonical_label() == H.canonical_label()
False
```



---

Comment by rlm created at 2008-02-16 21:06:52

After applying the patches at #2085, and setting use_indicator_function to False, the example returns True! This is our first clue...


---

Attachment

After three weeks, the problem is solved. The patch should apply on top of #2186, which depends on a few things...


---

Comment by mabshoff created at 2008-02-18 21:04:48

The patch for this problem also fixes #1360, so make sure to close that ticket once this patch is applied.

Cheers,

Michael


---

Comment by rlm created at 2008-02-19 19:45:23

After applying this patch, the patch from #2211 should also be applied.


---

Comment by jason created at 2008-02-19 21:17:20

looks good.


---

Comment by mabshoff created at 2008-02-19 22:18:11

Resolution: fixed


---

Comment by mabshoff created at 2008-02-19 22:18:11

Merged in Sage 2.10.2.alpha2
