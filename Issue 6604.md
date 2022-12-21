# Issue 6604: Polish the use of iterators in C graphs

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-07-23 15:56:41

Assignee: rlm

CC:  @kliem tscrim




---

Comment by rlm created at 2010-01-09 00:08:48

I am right now watching a talk on closures in Cython, which are all but finished. Then, yield statements in Cython will soon follow! So don't work on this ticket for now...


---

Comment by jason created at 2010-03-17 05:26:22

Changing type from defect to enhancement.


---

Comment by dcoudert created at 2021-12-03 17:39:45

Changing status from new to needs_review.


---

Comment by dcoudert created at 2021-12-03 17:39:45

It seems there is little remaining to do for iterators in backends now, so let's do it.

Before

```
sage: a = DiGraph(graphs.CompleteGraph(100))
sage: b = a._backend
sage: %timeit L = list(b.iterator_nbrs(30))
28.3 µs ± 1.44 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```


After

```
sage: a = DiGraph(graphs.CompleteGraph(100))
sage: b = a._backend
sage: %timeit L = list(b.iterator_nbrs(30))
18.6 µs ± 698 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

----
New commits:


---

Comment by tscrim created at 2021-12-04 04:47:56

That is quite a decent speedup and will likely have effects in other methods. Looks like some trivial failures due to slight differences in how the iteration is done:

```
sage -t --long --random-seed=210304412354021215508062896360889570175 src/sage/graphs/generic_graph.py
**********************************************************************
File "src/sage/graphs/generic_graph.py", line 10654, in sage.graphs.generic_graph.GenericGraph.neighbor_iterator
Failed example:
    list(D.neighbor_iterator(0))
Expected:
    [1, 2, 3]
Got:
    [3, 1, 2]
**********************************************************************
File "src/sage/graphs/generic_graph.py", line 17591, in sage.graphs.generic_graph.GenericGraph.?
Failed example:
    list(D.depth_first_search(1, ignore_direction=True, edges=True))
Expected:
    [(1, 4), (4, 5), (5, 6), (5, 2), (4, 3)]
Got:
    [(1, 3), (3, 4), (4, 5), (5, 6), (5, 2)]
```

This one I am not sure if it is because of the random seed or this ticket:

```
sage -t --long --random-seed=210304412354021215508062896360889570175 src/sage/schemes/toric/sheaf/klyachko.py
**********************************************************************
File "src/sage/schemes/toric/sheaf/klyachko.py", line 950, in sage.schemes.toric.sheaf.klyachko.KlyachkoBundle_class.random_deformation
Failed example:
    Vtilde.cohomology(dim=True, weight=(0,))
Expected:
    (1, 0)
Got:
    (0, 0)
```

in either case, it should be a trivial fix.


---

Comment by git created at 2021-12-04 10:09:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2021-12-04 10:14:54

I fixed the doctests in `generic_graph.py`. 

I cannot reproduce the error in `klyachko.py`. It occurs in method `random_deformation`. Some help might be helpful here.


---

Comment by dcoudert created at 2021-12-04 11:28:22

Actually, this random error in `klyachko.py` has already been reported in #32773.


---

Comment by tscrim created at 2021-12-05 07:28:56

Thank you. LGTM.


---

Comment by tscrim created at 2021-12-05 07:28:56

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2021-12-12 15:09:10

Resolution: fixed
