# Issue 3932: Should we merge the "generate size n trees in linear time" code from  	  Ryan Dingman

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-22 18:17:46

Assignee: rlm

See http://wiki.wstein.org/2008/480a/theprojects


---

Comment by mabshoff created at 2008-08-22 20:03:08

Hi Jason,

this question is not for trac, but should be discussed in [sage-devel].

Cheers,

Michael


---

Comment by rlm created at 2009-01-22 17:37:28

Changing type from defect to enhancement.


---

Comment by rlm created at 2009-04-16 21:33:26

YES we should!


---

Comment by mabshoff created at 2009-04-16 21:46:10

Well, someone ought to change the subject of the tickets Jason opened analog to this, i.e. the 480 tickets, a while ago since they kind of suck (no offense Jason :)). A ticket should have a clear goal and discussions about whether to merge code or not do not belong into trac.

Cheers,

Michael


---

Comment by rlm created at 2009-04-16 22:02:23

Replying to [comment:4 mabshoff]:
> Well, someone ought to change the subject of the tickets Jason opened analog to this, i.e. the 480 tickets, a while ago since they kind of suck (no offense Jason :)). A ticket should have a clear goal and discussions about whether to merge code or not do not belong into trac.

+1

I was just touching the ticket, since Ryan is about to post a patch here.


---

Comment by jason created at 2009-04-16 22:31:40

Yep, +1 to mabshoff's comments.  Sorry for the noise.  I'm glad the work is getting done, though.


---

Comment by rdingman created at 2009-04-29 04:56:20

Resolution: fixed


---

Comment by rdingman created at 2009-04-29 04:58:09

Resolution changed from fixed to 


---

Comment by rdingman created at 2009-04-29 04:58:09

Mistakenly closed this enhancement. Only intended to submit a patch.


---

Comment by rdingman created at 2009-04-29 04:58:09

Changing status from closed to reopened.


---

Comment by rlm created at 2009-04-29 15:09:08

1. Please change the `cdef void` functions to `cdef int` so that exceptions can be passed through them.

2. You can add a `cdef object G` to `__next__`. Since that's the iteration step, the speed might make a sliver of difference (maybe not).

3. `fixit = True` should probably be `fixit = 1` since `True` would inherit Python noise. You also don't need `if fixit == 1:`, just `if fixit:`

4. This is a great patch. I'll post another patch later today which will tie this into the main tree generator, and we'll see what kind of speedups you get.


---

Comment by rdingman created at 2009-04-29 15:54:11

I've made the changes noted above and replaced the patch with the new patch.


---

Comment by rlm created at 2009-04-29 16:21:54

Here's the timing improvement:


```
N   OLD   NEW
6   .11   .00
8   .87   .00
10  58.   .01
12  ???   .04
15  ???   .67
```



---

Comment by rlm created at 2009-04-29 16:24:58

Apply this patch after trac_3932_tree_generation.patch


---

Attachment

Positive review to Ryan's patch. All we need now is someone to check mine.


---

Comment by mabshoff created at 2009-04-30 03:46:03

`__init__`, `__dealloc__` and `__iter__` are missing docstrings and (indirect) doctests. It would also be a good idea if some of the cdef methods got some docstrings, too. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 03:51:15

While I am in pedantic mode:

```
106	        self.l = <int *>sage_malloc(self.n * sizeof(int)) 
107	        self.w = <int *>sage_malloc(self.n * sizeof(int)) 
```

should verify that the allocation actually worked. If either one of them fails for whatever reason we will have the code go *boom*.

And `__next__` also needs a doctest ;)

Cheers,

Michael


---

Comment by rdingman created at 2009-05-05 02:28:49

- Raise a MemoryError if memory allocation fails.
- Added more docstrings and doctest. Hopefully, the doctests are adequate as I'm still learning my way in Sage wrt doctests ;)


---

Comment by mabshoff created at 2009-05-13 18:47:24

This patch set causes two doctest failures for me:

```
        sage -t -long devel/sage/sage/graphs/graph.py # 1 doctests failed
        sage -t -long devel/sage/sage/graphs/graph_plot.py # 1 doctests failed
```

Specifically:

```
sage -t -long "devel/sage/sage/graphs/graph.py"
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/graphs/graph.py", line 6415:
    sage: t.set_edge_label(0,1,-7)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_134[57]>", line 1, in <module>
        t.set_edge_label(Integer(0),Integer(1),-Integer(7))###line 6415:
    sage: t.set_edge_label(0,1,-7)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 3571, in set_edge_label
        self._backend.set_edge_label(u, v, l, self._directed)
      File "sparse_graph.pyx", line 1485, in sage.graphs.base.sparse_graph.SparseGraphBackend.set_edge_label (sage/graphs/base/sparse_graph.c:15129)
      File "sparse_graph.pyx", line 547, in sage.graphs.base.sparse_graph.SparseGraph.add_arc_label (sage/graphs/base/sparse_graph.c:4373)
    RuntimeError: Label (-7) must be a nonnegative integer.
**********************************************************************
1 items had failures:
   1 of  84 in __main__.example_134
```

and

```
sage -t -long "devel/sage/sage/graphs/graph_plot.py"        
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/graphs/graph_plot.py", line 729:
    sage: t.set_edge_label(0,1,-7)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[53]>", line 1, in <module>
        t.set_edge_label(Integer(0),Integer(1),-Integer(7))###line 729:
    sage: t.set_edge_label(0,1,-7)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 3571, in set_edge_label
        self._backend.set_edge_label(u, v, l, self._directed)
      File "sparse_graph.pyx", line 1485, in sage.graphs.base.sparse_graph.SparseGraphBackend.set_edge_label (sage/graphs/base/sparse_graph.c:15129)
      File "sparse_graph.pyx", line 547, in sage.graphs.base.sparse_graph.SparseGraph.add_arc_label (sage/graphs/base/sparse_graph.c:4373)
    RuntimeError: Label (-7) must be a nonnegative integer.
```


Cheers,

Michael


---

Attachment


---

Comment by rdingman created at 2009-05-17 03:51:29

Robert let me know that the c_graph backend for graphs isn't as functional as the networkx backend. I switched to the tree generation code to use the networkx backend. This change fixes the doctests, but takes is about 2 times slower.


---

Comment by rlm created at 2009-05-17 05:52:00

I like the approach here. With luck, our sprint at Sage Days will allow us to use `c_graph` as default, and get that factor of 2 back.


---

Comment by mabshoff created at 2009-05-18 23:14:27

Merged both patches in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 23:14:27

Resolution: fixed


---

Comment by mvngu created at 2009-06-01 16:30:33

Replying to [comment:11 rlm]:
> Here's the timing improvement:
> 
> {{{
> N   OLD   NEW
> 6   .11   .00
> 8   .87   .00
> 10  58.   .01
> 12  ???   .04
> 15  ???   .67
> }}}


Hi Robert. I'm writing the release tour for Sage 4.0. To showcase the feature introduced by this ticket, is it possible for you to show me the code you used to obtain the above timing statistics?


---

Comment by rlm created at 2009-06-01 17:37:25


```
sage: L = list(graphs.trees(n))
```

or something very similar.
