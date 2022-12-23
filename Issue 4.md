# Issue 4: py3: change sorting of neighbors labels in static_sparse_graph.pyx

CC:  tscrim chapoton

Many doctests are failing in Python 3 due to the operation `neighbor_label.sort()` in method `init_short_digraph` of `static_sparse_graph.pyx`.

In the `short_digraph` data structure, the neighbors of a vertex are sorted by increasing integer value. This can be useful for some algorithms... 

`neighbor_label` is a list of tuples `(int, object)` used only when edges are labeled and that we want to store these labels. Clearly, when the graph has no multiple edges, is suffices to sort `neighbor_label` according the integer values. When the graph has multiple edges, there is so far no need for sorting the labels of the edges between a given pair of vertices, and furthermore no assumption is documented on this ordering.
Also, this patch changes the sorting to sort using the integer values only.


Issue created by migration from https://trac.sagemath.org/ticket/26801




---

Changing status from new to needs_review.


---

Applying this patch over 8.5.beta6 compiled for Python3, we reduce the number of failing doctests in `connectivity.pyx` from 49 to 5. The files for which progresses are observed are:

```
sage -t --long --warn-long 119.6 src/sage/graphs/generic_graph.py  # 77 doctests failed
sage -t --long --warn-long 119.6 src/sage/graphs/connectivity.pyx  # 5 doctests failed
sage -t --long --warn-long 119.6 src/sage/graphs/digraph.py  # 8 doctests failed
sage -t --long --warn-long 119.6 src/sage/graphs/base/graph_backends.pyx  # 1 doctest failed
```

Without this patch, we get

```
sage -t --long src/sage/graphs/generic_graph.py  # 78 doctests failed
sage -t --long src/sage/graphs/connectivity.pyx  # 49 doctests failed
sage -t --long src/sage/graphs/digraph.py  # 15 doctests failed
sage -t --long src/sage/graphs/base/graph_backends.pyx  # 5 doctests failed
```

----
New commits:


---

Changing keywords from "" to "py3, graph".


---

Green bot => positive review (unless Frédéric has some other comments).


---

Changing status from needs_review to positive_review.


---

ok, looks good to me too


---

Resolution: fixed
