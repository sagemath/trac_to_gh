# Issue 8329: Missing copy() method in BipartiteGraph

Issue created by migration from https://trac.sagemath.org/ticket/8329

Original creator: rhinton

Original creation time: 2010-02-22 19:51:40

Assignee: rhinton

CC:  rlm jason

Keywords: BipartiteGraph

BipartiteGraph is missing a copy() method.


```
sage: bg = BipartiteGraph(graphs.CycleGraph(4))
sage: type(bg)
<class 'sage.graphs.bipartite_graph.BipartiteGraph'>
sage: bg2 = bg.copy()
sage: type(bg2)
<class 'sage.graphs.graph.Graph'>
```


The result is not horrendous because the base Graph class has a copy() method.  But the result is unexpected: copy() a BipartiteGraph and you get a Graph?



---

Comment by rhinton created at 2010-02-22 20:16:25

Changing status from new to needs_review.


---

Comment by rhinton created at 2010-02-22 20:35:36

Changing status from needs_review to needs_work.


---

Comment by rhinton created at 2010-02-22 20:35:36

Oops, bug in doctest, the patch doesn't work at all.


---

Comment by rhinton created at 2010-02-22 20:43:42

New patch (replaced old) should work, including fixed doctest.


---

Comment by rhinton created at 2010-02-22 20:43:42

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-02-23 01:24:22

This is item 9 on trac #1941.


---

Comment by rhinton created at 2010-02-23 01:59:27

Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  

Incidentally, I think I have a decent approach for add_vertex.  I was planning on opening another ticket.... :-)


---

Comment by rlm created at 2010-02-23 03:05:58

Replying to [comment:6 rhinton]:
> Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  

I was just linking the tickets to each other. Adding edges to trac I guess... Any way you want to improve bipartite graphs I'll gladly review once I get the time, I just wanted to make sure you were aware of that ticket.

> Incidentally, I think I have a decent approach for add_vertex.  I was planning on opening another ticket.... :-)

Go for it!


---

Comment by rhinton created at 2010-02-24 01:35:09

Note for someone who is more knowledgeable: the new BipartiteGraph.copy() method doesn't try to do anything tricky with vertex associations, boundaries, positions, etc.  It just tries the Graph constructor.  I haven't figured out a way to copy() the Graph part and get out a BipartiteGraph instance.  This way works for me, but I'm not sure if it does all the special stuff that Graph.copy() does.


---

Comment by rhinton created at 2010-02-24 21:11:33

I get it ... adding edges. :-)

Replying to [comment:7 rlm]:
> Replying to [comment:6 rhinton]:
> > Right, I had forgotten about this.  Obviously I'm fixing methods as I need them.  I don't have time right now for the complete overhaul.  Is the piecemeal approach OK?  
> 
> I was just linking the tickets to each other. Adding edges to trac I guess... Any way you want to improve bipartite graphs I'll gladly review once I get the time, I just wanted to make sure you were aware of that ticket.


---

Comment by rhinton created at 2010-03-02 02:36:42

Changing keywords from "BipartiteGraph" to "BipartiteGraph, copy".


---

Comment by rhinton created at 2010-03-02 02:36:42

The new patch to GenericGraph.__copy__() always creates a new object of the same class as the original object -- no special case code for Graph, DiGraph, or BipartiteGraph.  Any future subclasses will work as well assuming they can handle the same initializer arguments (by passing them to the superclass initializer).


---

Comment by rlm created at 2010-03-02 02:57:44

This patch exposes a bug in another seldom used extension of the `Graph` class, `GraphBundle`.


```
File "/Users/rlmill/sage-4.3.3/devel/sage-main/sage/graphs/graph_bundle.py", line 163:
    sage: B.plot()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        B.plot()###line 163:
    sage: B.plot()
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph_bundle.py", line 173, in plot
        total_pos = generic_graph_pyx.spring_layout_fast(self, iterations=iters)
      File "generic_graph_pyx.pyx", line 86, in sage.graphs.generic_graph_pyx.spring_layout_fast (sage/graphs/generic_graph_pyx.c:1361)
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph.py", line 2061, in to_undirected
        return copy(self)
      File "/Users/rlmill/sage-4.3.3/local/lib/python2.6/copy.py", line 79, in copy
        return copier(x)
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 483, in __copy__
        G = self.__class__(self, name=self.name(), pos=copy(self._pos), boundary=copy(self._boundary), implementation=implementation, sparse=sparse)
      File "/Users/rlmill/sage-4.3.3/local/lib/python/site-packages/sage/graphs/graph_bundle.py", line 73, in __init__
        if isinstance(args[0], (list, tuple)):
    IndexError: tuple index out of range
```



---

Comment by rlm created at 2010-03-02 03:06:49

I will offer the suggestion to disable the failing doctest, for discussion. I don't know of anyone who uses graph bundles in Sage. I've emailed Chris Godsil to see if he ever uses it.


---

Comment by rhinton created at 2010-03-02 16:27:18

Sounds great to me.  The new patch disables the "plot" doctest that was failing and adds a "known bugs" warning to the beginning of the graph_bundle.py.


---

Attachment

modifies copy() code in generic_graph.py and adds test to BipartiteGraph


---

Comment by rlm created at 2010-03-06 22:14:27

Anyone queasy about the `GraphBundle` doctest, Godsil tells me he has a student who is working on a bundle package, which I am assuming actually does something (unlike bundles in Sage). Look for this to appear in Sage at some point soon!


---

Comment by rlm created at 2010-03-06 22:14:27

Changing status from needs_review to positive_review.


---

Comment by rhinton created at 2010-03-24 18:36:57

Changing status from positive_review to needs_work.


---

Comment by rhinton created at 2010-03-24 18:36:57

Found a failing doctest in combinat/posets/posets.py due to this change.  Additional patch coming soon.


---

Attachment

Apply both patches, order does not matter


---

Comment by rhinton created at 2010-03-24 18:45:27

Changing status from needs_work to needs_review.


---

Comment by rhinton created at 2010-03-24 18:45:27

New patch fixes posets doctest failure.  Apply both patches; order does not matter.


---

Comment by ncohen created at 2010-04-01 11:55:17

Good patch ! Applies fine, does its job.. :-)

Nathann


---

Comment by ncohen created at 2010-04-01 11:55:17

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:09:01

Merged in 4.4.alpha0:

 - trac_8329-bipartite-graph-copy.patch
 - trac_8329-posets-repr.patch


---

Comment by jhpalmieri created at 2010-04-15 20:09:01

Resolution: fixed
