# Issue 5936: result of graph query should be iterable -- make more pythonic

Issue created by migration from https://trac.sagemath.org/ticket/5936

Original creator: was

Original creation time: 2009-04-29 15:59:37

Assignee: rlm

Currently we have this:

```
sage: Q = GraphQuery(
       display_cols=['graph6','num_vertices','degree_sequence'],
       num_edges=['<=',5],min_degree=1)
sage: for G in Q: print G
```

outputs

```
Traceback (click to the left for traceback)
...
TypeError: 'GraphQuery' object is not iterable
```


Why not have it Q.__iter__() return an iterator over `Q.get_graphs_list()`, which would easily work?



---

Comment by ekirkman created at 2009-05-21 22:01:16

Patch covers docstring updates (see #5935) and adds an iterator for GraphQuery.


---

Attachment

Referee edit of Emily's patch


---

Comment by mhansen created at 2009-06-01 04:57:05

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 04:57:05

Resolution: fixed
