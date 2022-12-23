# Issue 7571: use more dicts in graph.py

Issue created by migration from https://trac.sagemath.org/ticket/7571

Original creator: ylchapuy

Original creation time: 2009-12-01 15:10:38

Assignee: rlm

This patch improves 3 methods in graph.py:

 * connected_components: we use python set instead of lists to enable fast lookup
 * blocks_and_cut_vertices: using dicts instead of lists enable us to avoid relabeling
 * girth: idem


---

Comment by ylchapuy created at 2009-12-01 15:46:13

for the record:

Before:

```
sage: g=graphs.RandomGNP(10000,.00011)
sage: time g.girth()
CPU times: user 8.19 s, sys: 0.02 s, total: 8.20 s
Wall time: 8.21 s
33
sage: time g.connected_components_number()
CPU times: user 2.06 s, sys: 0.00 s, total: 2.07 s
Wall time: 2.09 s
4474
sage: g=g.connected_components_subgraphs()[0]
sage: len(g)
1784
sage: time b=g.blocks_and_cut_vertices()
CPU times: user 0.28 s, sys: 0.00 s, total: 0.28 s
Wall time: 0.28 s
```


After:

```
sage: g=graphs.RandomGNP(10000,.00011)
sage: time g.girth()
CPU times: user 5.00 s, sys: 0.00 s, total: 5.00 s
Wall time: 5.00 s
33
sage: time g.connected_components_number()
CPU times: user 0.20 s, sys: 0.00 s, total: 0.20 s
Wall time: 0.20 s
4487
sage: g=g.connected_components_subgraphs()[0]
sage: len(g)
2509
sage: time b=g.blocks_and_cut_vertices()
CPU times: user 0.16 s, sys: 0.00 s, total: 0.16 s
Wall time: 0.16 s
```


And more importantly:

```
sage: g = graphs.KrackhardtKiteGraph()
sage: g.relabel(map(lambda i: 'x'+str(i),range(len(g))))
```


before:

```
sage: g.blocks_and_cut_vertices()
([[9, 8], [8, 7], [7, 4, 6, 5, 2, 3, 1, 0]], [8, 7])
```


after:

```
sage: g.blocks_and_cut_vertices()

([['x9', 'x8'],
  ['x5', 'x4', 'x1', 'x0', 'x2', 'x3', 'x6', 'x7'],
  ['x7', 'x8']],
 ['x8', 'x7'])
```



---

Attachment


---

Comment by ylchapuy created at 2009-12-01 15:50:03

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2009-12-01 15:50:03

Changing priority from major to minor.


---

Comment by rlm created at 2009-12-01 16:15:20

Your benchmarks would be more convincing if you used `set_random_seed` beforehand, so you're actually testing the same "random" graph.

The changes to the code look good, and the speedups are impressive.


---

Comment by rlm created at 2009-12-01 16:15:20

Changing status from needs_review to positive_review.


---

Comment by ylchapuy created at 2009-12-01 16:30:55

that's true, benchmarks are not very convincing. Here are new ones:

before:

```
sage: set_random_seed(42)
sage: g=graphs.RandomGNP(20000,.00005)
sage: time g.girth()
CPU times: user 17.55 s, sys: 0.07 s, total: 17.62 s
Wall time: 17.83 s
16
sage: time g.connected_components_number()
CPU times: user 8.40 s, sys: 0.08 s, total: 8.48 s
Wall time: 8.72 s
9810
sage: set_random_seed(42)
sage: g=graphs.RandomGNP(10000,.005)
sage: time b=g.blocks_and_cut_vertices()
CPU times: user 17.19 s, sys: 0.44 s, total: 17.63 s
Wall time: 17.98 s
```


after:

```
sage: set_random_seed(42)
sage: g=graphs.RandomGNP(20000,.00005)
sage: time g.girth()
CPU times: user 2.15 s, sys: 0.00 s, total: 2.16 s
Wall time: 2.15 s
16
sage: time g.connected_components_number()
CPU times: user 0.32 s, sys: 0.00 s, total: 0.32 s
Wall time: 0.32 s
9810
sage: set_random_seed(42)
sage: g=graphs.RandomGNP(10000,.005)
sage: time b=g.blocks_and_cut_vertices()
CPU times: user 10.22 s, sys: 0.04 s, total: 10.27 s
Wall time: 10.57 s
```



---

Comment by mhansen created at 2009-12-02 08:13:47

Resolution: fixed
