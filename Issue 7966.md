# Issue 7966: Giving some punch to distance computations

Issue created by migration from https://trac.sagemath.org/ticket/7966

Original creator: ncohen

Original creation time: 2010-01-17 14:34:20

Assignee: rlm

This patch creates a function shortest_path_all_vertices in c_graphs which, given a vertex v, computes a shortest path for each other vertex.

With small other modifications, it improves the speed of many functions ( which were all calling each other )

Before :

```
sage: g = graphs.RandomGNP(50,.3)
sage: %timeit g.shortest_path_lengths(0)
100 loops, best of 3: 3.72 ms per loop
sage: %timeit g.average_distance()
10 loops, best of 3: 383 ms per loop
sage: %timeit g.wiener_index()
10 loops, best of 3: 384 ms per loop
sage: %timeit g.szeged_index()
10 loops, best of 3: 325 ms per loop
sage: %timeit g.eccentricity()
10 loops, best of 3: 189 ms per loop
sage: g.sparse6_string()
':q_OW_CCBb?WcOL@@`_{CGDB@pCGIF``@[WQK_`?w_QIDoo_WSJEBWGOKIDbG?CZ?@@Owwb?@?o_SOMba@X?bA@`OpKhBB@p?kX@Caq@YAACAphWn@B@po{j?@`?o_]QIeGOWMGDCqheEDB@pXMAEBa@GscYLoo__QJEBaxcvBECAPWqYNQ`gwgTKERX}?@@@@Gg[QHdBXt@?BAa@WmYNGWo[OLFCQhqCLFCRPky]POow_SLGCRHw}ca@_w_SLHCq`_u[OGg?GEDBAP_{iUJeBiYKGCbPp_qYMFbyLIea``WoYMFcA`SkXMGS[?MIFCahgw\\NP`Ww]VLfSskYMHDApcs[NHSy`R?A@pOkWMGcb@oy]TjGGKOJIEBh|QjUOox?mWLEryHIh___WOaRIDr@cu[MhTauCCBa@Gk]PHdax_w]NhCq\\Sm'
```


After

```
sage: %timeit g.shortest_path_lengths(0)
10 loops, best of 3: 430 µs per loop
sage: %timeit g.average_distance()
10 loops, best of 3: 22 ms per loop
sage: %timeit g.wiener_index()
10 loops, best of 3: 22.1 ms per loop
sage: %timeit g.szeged_index()
10 loops, best of 3: 41.5 ms per loop
sage: %timeit g.eccentricity()
10 loops, best of 3: 22 ms per loop
```


Nathann


---

Comment by ncohen created at 2010-01-17 14:36:01

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-01-17 15:36:04

Small modification to distance_graph too:

Before :

```
sage: %timeit g.distance_graph([2,8,9])
10 loops, best of 3: 127 ms per loop
```

After

```
sage: %timeit g.distance_graph([2,8,9])
10 loops, best of 3: 49 ms per loop
```


Nathann


---

Comment by zimmerma created at 2010-02-26 08:14:59

The speedups are great, but I got one extra failure (against 4.3.3 on Fedora 12):

```
sage -t  graphs/base/c_graph.pyx
File "/usr/local/sage-4.3.3/sage/devel/sage-trac/sage/graphs/base/c_graph.pyx",\
 line 1427:
    sage: all([ len(paths[v]) == 0 or len(paths[v])-1 == g.distance(0,v) for v \
in g])
Exception raised:
    Traceback (most recent call last):
      File "/usr/local/sage-4.3.3/sage/local/bin/ncadoctest.py", line 1231, in \
run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/local/sage-4.3.3/sage/local/bin/sagedoctest.py", line 38, in r\
un_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compil\
eflags)
      File "/usr/local/sage-4.3.3/sage/local/bin/ncadoctest.py", line 1172, in \
run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_43[7]>", line 1, in <module>
        all([ len(paths[v]) == Integer(0) or len(paths[v])-Integer(1) == g.dist\
ance(Integer(0),v) for v in g])###line 1427:
    sage: all([ len(paths[v]) == 0 or len(paths[v])-1 == g.distance(0,v) for v \
in g])
    KeyError: 20
```

Please could you look at this?


---

Comment by zimmerma created at 2010-02-26 08:14:59

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-02-26 10:46:02

At first, the function associated a path from v to each other vertex, possibly empty if there was none. Then I noticed the other functions in Sage expected the dictionary to only contain keys corresponding to the vertices reachable from v (which was sound, too), and changed the original function, forgetting the docstrings... Fixed now ! 

And I also removed the (commented) loop which was associating empty paths when needed...

Thank you again ! :-)

Nathann


---

Comment by ncohen created at 2010-02-26 10:46:02

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-02-26 11:02:06

Changing status from needs_review to positive_review.


---

Attachment

with the new patch `c_graph.pyx` works again:

```
[zimmerma@coing sage]$ sage -t  graphs/base/c_graph.pyx
sage -t  "devel/sage-7966/sage/graphs/base/c_graph.pyx"     
         [2.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.5 seconds
```

Thus a positive review.

Paul


---

Comment by mvngu created at 2010-03-03 14:20:00

Resolution: fixed
