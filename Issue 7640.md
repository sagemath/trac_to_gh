# Issue 7640: shortest_path should not use NetworkX if the underlying graph is a c_graph

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-09 17:00:58

Assignee: rlm

CC:  ncohen rlm jason mvngu


```
sage: G = graphs.CubeGraph(5)
sage: C = G.copy(implementation='c_graph')
sage: timeit("G.shortest_path('01001', '10100')")
625 loops, best of 3: 49.3 µs per loop
sage: timeit("C.shortest_path('01001', '10100')")
625 loops, best of 3: 992 µs per loop
```



---

Comment by rlm created at 2009-12-09 17:03:16

This is one of those functions that should probably be written in Cython, on as low a level as possible...


---

Comment by ncohen created at 2009-12-09 17:36:38

To be honest, I intended to write it as soon as your partch to make them the default format is merged :-)


---

Comment by rlm created at 2009-12-09 17:37:59

It should be the other order: this ticket needs to be dealt with before we switch over. There are probably other issues like this one lurking...


---

Comment by ylchapuy created at 2009-12-09 19:31:25

One problem IMHO with `c_graph` is that as is (correct me if I'm wrong)
we won't be able to have a fast `in_neighbors`.

At least the current implementation is to test all vertices in the graph.


---

Comment by rlm created at 2009-12-09 19:44:12

Replying to [comment:4 ylchapuy]:
> One problem IMHO with `c_graph` is that as is (correct me if I'm wrong)
> we won't be able to have a fast `in_neighbors`.
> 
> At least the current implementation is to test all vertices in the graph.

This belongs here: http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5

See my comments there.


---

Comment by ncohen created at 2009-12-12 17:46:11

One less between Sage and c_graphs :-)

Here is the result of the test given in the description of this ticket :


```
sage: sage: G = graphs.CubeGraph(5)
sage: sage: C = G.copy(implementation='c_graph')
sage: sage: timeit("G.shortest_path('01001', '10100')")
625 loops, best of 3: 51.6 µs per loop
sage: sage: timeit("C.shortest_path('01001', '10100')")
625 loops, best of 3: 30.4 µs per loop
```


Nathann


---

Comment by ncohen created at 2009-12-12 17:46:11

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-12 18:20:36

Great work!

A few comments:

1. You can use `if self._backend.hasattr('_cg')` to test whether self is a `c_graph` or a `networkx` graph. This seems cleaner than a try-except block.

2. It should be easy to implement something in the case `bidirectional=False`, and we should do this since the point is to replace NetworkX with our own functionality.

3. We also need to handle the case `by_weight=True`: this is only relevant for `SparseGraph`s, since `DenseGraph`s don't support edge labeling.


---

Comment by rlm created at 2009-12-12 18:20:36

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-12 18:28:32

Several answers, then :-)

1. That's why I wanted to use at first but Martin Albrecht told me in #7637 that this version should be more efficient

2. The version ``bidirectional = False`` is indeed very easy to write ( one only needs to remove variables ), but I wondered if this was useful... ``bidirectional=True`` is the default option, used in all the others call to it, and this second version is meant to be faster... :-)

3. I started by trying to write the Dijkstra algorithm, and ended up wondering whether there was a Heap structure already written in Cython. I needed to maintain a sorted list, and found no reference about it ... If you know how to do it, I'll begin immediately ! :-)

This version of shortest_path seems to be the most used ( bidirectional=True, weights=False ), so I thought the most urgent was to make your c_graphs the default ones.. I just created two tickets in the graph section about functions that should be moved from networkx to c_graphs, we could just add these two ! Anyway I intend to take care of them :-)

Nathann


---

Comment by rlm created at 2009-12-12 18:31:05

I applied the patch here, together with the patch at #7634, (to `4.3.rc0`) in order to fully test the new functionality, and here are the results of `-t -long sage/graphs` (files not listed passed):


```
sage -t -long "devel/sage-main/sage/graphs/graph.py"        
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/graph.py", line 5838:
    sage: H.is_isomorphic(graphs.CompleteGraph(n))
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/graph.py", line 7329:
    sage: g.transitive_reduction().size()
Expected:
    5
Got:
    6
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/graph.py", line 2206:
    sage: o.in_degree()
Expected:
    [2, 2, 2, 2, 1, 2, 1, 1, 1, 1]
Got:
    [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/graph.py", line 2208:
    sage: o.out_degree()
Expected:
    [1, 1, 1, 1, 2, 1, 2, 2, 2, 2]
Got:
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/graph.py", line 4736:
    sage: g.degree_sequence()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_96[3]>", line 1, in <module>
        g.degree_sequence()###line 4736:
    sage: g.degree_sequence()
      File "/Users/rlmill/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 4754, in degree_sequence
        return sorted(self.degree_iterator(), reverse=True)
      File "/Users/rlmill/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 4725, in degree_iterator
        yield filter(v, self)
      File "/Users/rlmill/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 4723, in <lambda>
        filter = lambda v, self: self._backend.degree(v, self._directed)
      File "c_graph.pyx", line 751, in sage.graphs.base.c_graph.CGraphBackend.degree (sage/graphs/base/c_graph.c:7480)
      File "c_graph.pyx", line 594, in sage.graphs.base.c_graph.CGraph._out_degree (sage/graphs/base/c_graph.c:6472)
    RuntimeError: Vertex (5) is not a vertex of the graph.
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/graph.py", line 4742:
    sage: g.degree_sequence()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_96[5]>", line 1, in <module>
        g.degree_sequence()###line 4742:
    sage: g.degree_sequence()
      File "/Users/rlmill/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 4754, in degree_sequence
        return sorted(self.degree_iterator(), reverse=True)
      File "/Users/rlmill/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 4725, in degree_iterator
        yield filter(v, self)
      File "/Users/rlmill/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 4723, in <lambda>
        filter = lambda v, self: self._backend.degree(v, self._directed)
      File "c_graph.pyx", line 749, in sage.graphs.base.c_graph.CGraphBackend.degree (sage/graphs/base/c_graph.c:7433)
      File "c_graph.pyx", line 580, in sage.graphs.base.c_graph.CGraph._in_degree (sage/graphs/base/c_graph.c:6372)
    RuntimeError: Vertex (6) is not a vertex of the graph.
**********************************************************************
```



```
sage -t -long "devel/sage-main/sage/graphs/linearextensions.py"
**********************************************************************
File "/Users/rlmill/sage-4.3.rc0/devel/sage-main/sage/graphs/linearextensions.py", line 360:
    sage: l.incomparable(1,2)
Expected:
    True
Got:
    False
**********************************************************************
```



---

Comment by rlm created at 2009-12-12 18:35:32

Replying to [comment:9 ncohen]:
> Several answers, then :-)
> 
> 1. That's why I wanted to use at first but Martin Albrecht told me in #7637 that this version should be more efficient

Great!

> 2. The version ``bidirectional = False`` is indeed very easy to write ( one only needs to remove variables ), but I wondered if this was useful... ``bidirectional=True`` is the default option, used in all the others call to it, and this second version is meant to be faster... :-)

This is indeed a good point. I wonder if anyone ever in the history of Sage has used bidirectional=False.

> 3. I started by trying to write the Dijkstra algorithm, and ended up wondering whether there was a Heap structure already written in Cython. I needed to maintain a sorted list, and found no reference about it ... If you know how to do it, I'll begin immediately ! :-)

I'm not sure...

> This version of shortest_path seems to be the most used ( bidirectional=True, weights=False ), so I thought the most urgent was to make your c_graphs the default ones.. I just created two tickets in the graph section about functions that should be moved from networkx to c_graphs, we could just add these two ! Anyway I intend to take care of them :-)

I don't think `bidirectional=False` is a showstopper at all (in fact we should ping sage-devel about removing this option, since it seems silly). However, `by_weights=True` is going to be necessary to make the switch. I also just noticed that the function `shortest_paths` needs to be implemented for `c_graph`s too.


---

Comment by ncohen created at 2009-12-12 18:37:31

I'll take a look at those errors immediately. 

shortest_paths is but a slight modification of this function, but as it needs to be very fast I wondered about copying most of the code and adding the necessary details.. What's you advice ?

Nathann


---

Comment by rlm created at 2009-12-12 18:39:41

Replying to [comment:12 ncohen]:
> I'll take a look at those errors immediately. 
> 
> shortest_paths is but a slight modification of this function, but as it needs to be very fast I wondered about copying most of the code and adding the necessary details.. What's you advice ?
> 
> Nathann

I would think about using the same code. Or factoring it out so that the redundant parts get written only once. (I don't know how familiar you are with Cython, but you can use `inline` in situations like these!)


---

Comment by rlm created at 2009-12-12 18:42:22

Replying to [comment:12 ncohen]:
> I'll take a look at those errors immediately. 
 
Not remembering whether I tested #7634 with `-long` by itself, I'm checking to see how #7634 does on its own (on top of alpha0 of course, since rc0 has distance_graphs, which time out...)


---

Comment by rlm created at 2009-12-12 19:01:10

Replying to [comment:14 rlm]:
> Replying to [comment:12 ncohen]:
> > I'll take a look at those errors immediately. 
>  
> Not remembering whether I tested #7634 with `-long` by itself, I'm checking to see how #7634 does on its own (on top of alpha0 of course, since rc0 has distance_graphs, which time out...)

All tests pass here, so it looks like all the issues above are relevant.


---

Comment by ncohen created at 2009-12-12 19:03:19

The first (test of isomorphism) error was a mistake in the algorithm and is fixed already. I am dealing with the second one (transitive_reduction) which is related to the fact that we are dealing with a digraph... I am not worried by the RuntimeErrors that follow... I will update this patch as soon as possible :-)


---

Comment by ncohen created at 2009-12-12 19:33:26

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-12 19:33:26

Well, in the end I corrected the first two errors, which were directly errors in the algorithm ( I ignored the direction of arcs, which is now fixed ).

The following ones are created by the enumeration of degree ( for example the error in eulerian_orientation is not really one. The result given is correct, but there is one inversion due to the fact that the order in the listing of neighbors is not the same when you patch is applied :-)

This reminded me that your patch for c_graphs had not actually been tested against the new Sage because of the slowness in the distance function.. As eulerian_orientation does not care about distances ( I wrote this one :-) ), I do not think shortest_path is responsible for this one... Could you take a look at the last bugs to see if it could come from the switching process ( it it for sure in the case of eulerian_orientation ) ?

Actually, as it is not possible to test your switching patch without the shortest)path functiom, perhaps we should merge the two in just one patch....

We're almost there !!!!!!!!!! :-)

Nathann


---

Attachment


---

Comment by rlm created at 2009-12-12 19:39:51

Replying to [comment:17 ncohen]:
> Actually, as it is not possible to test your switching patch without the shortest)path functiom, perhaps we should merge the two in just one patch....

Absolutely not! There is *much* work that needs to be done before #7634 gets merged (this is just one piece). Once this patch is finalized, we can say #7634 depends on this, and then the testing issue will be moot.

Review of the current patch coming shortly...


---

Comment by rlm created at 2009-12-12 20:02:19

I've created #7673 to deal with the `by_weight=True` case. I like this patch as it is, since it makes it possible to test #7634. Also, by itself it passes long tests in sage/graphs. Nice work!


---

Comment by rlm created at 2009-12-12 20:02:19

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-14 16:41:40

Resolution: fixed
