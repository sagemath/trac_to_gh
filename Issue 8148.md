# Issue 8148: looking at the dual of a poset: IndexError

Issue created by migration from https://trac.sagemath.org/ticket/8148

Original creator: jhpalmieri

Original creation time: 2010-02-02 04:52:34

Assignee: sage-combinat

CC:  sage-combinat brunellus mjo

In Sage 4.3.2.alpha0:

```
sage: Q = Poset({1: [], 3: [], 2: [1, 3]})
sage: Q.show()  # works fine
sage: Q.dual().show()
...
IndexError: list index out of range
```

Note that the following works, and is what I'm using in my code right now:

```
sage: Poset(Q.hasse_diagram().reverse()).show()
```

Actually, though, this fails if Q is defined instead to be

```
sage: Q = Poset({1: [], 2: [1]})
sage: Q.show()  # works fine, although the picture looks a little funny
sage: Poset(Q.hasse_diagram().reverse()).show()
...
RuntimeError: Error building image
```



---

Comment by brunellus created at 2011-12-13 23:54:25


```
sage:Poset({1: [], 3: [], 2: [1, 3]}).dual().relations()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/root/<ipython console> in <module>()

/root/Sage/sage/local/lib/python2.6/site-packages/sage/combinat/posets/posets.pyc in relations(self)
    717         - Rob Beezer (2011-05-04)
    718         """
--> 719         return list(self.relations_iterator())
    720 
    721     def relations_iterator(self):

/root/Sage/sage/local/lib/python2.6/site-packages/sage/combinat/posets/posets.pyc in relations_iterator(self)
    745         # Relies on vertices the fact that _elements correspond to the rows and
    746         # columns of the lequal matrix
--> 747         leq_mat = self.lequal_matrix()
    748         n = leq_mat.nrows()
    749         elements = self._elements

/root/Sage/sage/local/lib/python2.6/site-packages/sage/combinat/posets/posets.pyc in lequal_matrix(self, **kwds)
   1282             False
   1283         """
-> 1284         return self._hasse_diagram.lequal_matrix(**kwds)
   1285 
   1286     def meet_matrix(self):

/root/Sage/sage/local/lib/python2.6/site-packages/sage/combinat/posets/hasse_diagram.pyc in lequal_matrix(self, ring, sparse)
    867         D = {}
    868         for i in range(n):
--> 869             for v in self.breadth_first_search(i):
    870                 D[(i,v)] = 1
    871         self._leq_matrix = matrix(ring, n, n, D, sparse=sparse)

/root/Sage/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in breadth_first_search(self, start, ignore_direction, distance, neighbors)
  11565         # Preferably use the Cython implementation 
  11566         if neighbors is None and not isinstance(start,list) and distance is None and hasattr(self._backend,"breadth_first_search"): 
> 11567             for v in self._backend.breadth_first_search(start, ignore_direction = ignore_direction): 
  11568                 yield v 
  11569         else: 

/root/Sage/sage/local/lib/python2.6/site-packages/sage/graphs/base/c_graph.so in sage.graphs.base.c_graph.Search_iterator.__next__ (sage/graphs/base/c_graph.c:19732)()

/root/Sage/sage/local/lib/python2.6/site-packages/sage/graphs/base/sparse_graph.so in sage.graphs.base.sparse_graph.SparseGraph.out_neighbors (sage/graphs/base/sparse_graph.c:8007)()

/root/Sage/sage/local/lib/python2.6/site-packages/sage/graphs/base/sparse_graph.so in sage.graphs.base.sparse_graph.SparseGraph.out_neighbors (sage/graphs/base/sparse_graph.c:7841)()

/root/Sage/sage/local/lib/python2.6/site-packages/sage/graphs/base/c_graph.so in sage.graphs.base.c_graph.CGraph.check_vertex (sage/graphs/base/c_graph.c:5697)()

RuntimeError: Vertex (0) is not a vertex of the graph.
```



---

Attachment


---

Comment by brunellus created at 2011-12-14 00:51:53

I guess this fix should help -- dual() created new Poset using FinitePoset constructor that requires a DiGraph in its argument to be rather refined one. Especially that the range(n) should be a linear extension of poset defined by a DiGraph. That wasn't true, because dual() reversed the orientation of edges. Poset constructor is much more liberal.


---

Comment by brunellus created at 2011-12-14 00:51:53

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-07 22:45:57

This is probably the best fix at the moment (although it would be nice if FinitePoset() could be used by itself).

For the patch, can you add the ticket number to the doctest somewhere?

I would also create a "TESTS:" section under examples, since this isn't really a useful example independent of the fact that it demonstrates this bug.

You can give the doctest a little introduction, too. For example,


```
TESTS:

We should get a valid FinitePoset back if we call dual() on a finite poset (trac #8148)::

    sage: ...
```


It's the double-colon that says "here comes a doctest."


---

Attachment

Thanks! I tried to rewrite this to use FinitePoset immediately. Does it make sense? I tried to run it to few examples, but maybe there is something I overlooked.


---

Comment by nthiery created at 2012-01-08 20:09:39

Hi!

Sorry, I should have been more reactive to spare you this patch. In principle, this is fixed by #10998 which is almost finished, and I hope to get in soon. Could you double check this?

Cheers,
                   Nicolas


---

Comment by brunellus created at 2012-01-08 20:25:33

Hi, I guess such situations are inevitable in distributed projects. :-) Your patch really solves this issue.


---

Comment by ncohen created at 2012-01-29 15:48:54

(the procedure for closing tickets... positive review + milestone to wontfix)


---

Comment by ncohen created at 2012-01-29 15:48:54

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-31 09:38:20

Resolution: duplicate
