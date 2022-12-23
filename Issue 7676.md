# Issue 7676: shortest_path_all pairs in Cython through Floyd Warshall

Issue created by migration from https://trac.sagemath.org/ticket/7676

Original creator: ncohen

Original creation time: 2009-12-13 16:33:51

Assignee: rlm

Everything is explained there :

http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm


---

Comment by ncohen created at 2010-06-06 11:00:50

Changing status from new to needs_work.


---

Comment by embray created at 2019-01-07 13:11:35

According to https://ask.sagemath.org/question/44823/sage-floyd-algorithm-in-cython/ SciPy already includes an implementation of this that is quite fast, and should probably be used over any implementation in Sage.


---

Comment by @vipul79321 created at 2020-02-06 18:47:42

If nobody else is currently working on this can I go ahead and implement shortest_path_all pair using Floyd warshall algorithm ?


---

Comment by dcoudert created at 2020-02-07 07:58:46

The first step is to survey the many algorithms we already have with data structures and specific conditions (e.g., weighted, multi edges, loops, etc.).


---

Comment by @vipul79321 created at 2020-02-08 08:30:13

I have surveyed all the algorithm and data structure sage has. All pair shortest path works only for an unweighted graph. Although we can use boost interface for this purpose. But I think sage should have its own implementation of Floyd Warshall algorithm[https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) for a weighted graph with positive or negative edge weights(but with no negative cycles).


---

Comment by dcoudert created at 2020-02-08 11:39:10

I don't think sage should have it's own implementation if the one of Boost is fast enough. 
You can give it a try, but I'm not sure you can produce something faster than `'Floyd-Warshall_Boost'`.

Note that we already have a (slow) Python implementation `'Floyd-Warshall-Python'` for weighted graphs, and a Cython implementation `'Floyd-Warshall-Cython'` but for unweighted graphs only.


---

Comment by @vipul79321 created at 2020-02-08 13:37:27

Thanks for your helpful suggestion. I will look into it.


---

Comment by dcoudert created at 2021-10-16 16:15:49

I added the `Floyd-Warshall` implementation of `SciPy`. It's working well but it's not as fast as expected. In fact, most of the time is wasted in turning the graph to a Numpy array and then turning the results to required dict of dicts.


```
sage: D = digraphs.RandomDirectedGNP(30, .33)
sage: for u, v in D.edges(labels=False):
....:     D.set_edge_label(u, v, randrange(100))
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_Boost')
CPU times: user 6.44 ms, sys: 517 µs, total: 6.96 ms
Wall time: 6.56 ms
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_SciPy')
CPU times: user 30.2 ms, sys: 1.85 ms, total: 32 ms
Wall time: 30.6 ms
```


```
sage: D = digraphs.RandomDirectedGNP(300, .33)
sage: for u, v in D.edges(labels=False):
....:     D.set_edge_label(u, v, randrange(100))
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_Boost')
CPU times: user 2.73 s, sys: 18.6 ms, total: 2.75 s
Wall time: 2.76 s
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_SciPy')
CPU times: user 1.95 s, sys: 61.6 ms, total: 2.01 s
Wall time: 2.13 s
```

----
New commits:


---

Comment by dcoudert created at 2021-10-16 16:15:49

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2021-12-04 12:32:23

So scipy thinks of graphs as matrices, there no special format/backend?


---

Comment by dcoudert created at 2021-12-04 12:53:20

When you look at the code of scipy (for instance, https://github.com/scipy/scipy/blob/master/scipy/sparse/csgraph/_shortest_path.pyx), the input parameter is always

```
    csgraph : array, matrix, or sparse matrix, 2 dimensions
        The N x N array of distances representing the input graph.
```

You can also check method `validate_graph` in https://github.com/scipy/scipy/blob/master/scipy/sparse/csgraph/_validation.py. It may convert from one matrix format to another.


---

Comment by dcoudert created at 2021-12-04 14:25:41

So now the question is whether we finalize this ticket or move it to wontfix. Both options are OK for me.


---

Comment by dimpase created at 2021-12-04 14:59:37

let us merge it


---

Comment by dimpase created at 2021-12-04 15:00:08

Changing status from needs_review to positive_review.


---

Comment by dcoudert created at 2021-12-04 15:05:45

Thanks.


---

Comment by vbraun created at 2021-12-12 15:09:08

Resolution: fixed
