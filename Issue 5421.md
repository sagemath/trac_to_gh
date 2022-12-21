# Issue 5421: Speedup is_isomorphic

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-03-02 18:36:52

Assignee: rlm

CC:  mhansen

Based on the thread at

http://groups.google.com/group/sage-devel/browse_thread/thread/1e3928bc2bffe9a6?pli=1

several speedups have been implemented:

 1. Graphs which can be switched to `c_graph` are automatically switched before isomorphism testing (see thread).

 1. Several cheap imports have been moved to module level.

 1. One unnecessary step was removed.

Benchmark: Take a list of all isomorphism classes of graphs on 7 vertices. Take one representative from each, and test each unordered pair for isomorphism. With underlying `c_graph` implementation, previously was 31.11 seconds, is now 10.71 seconds.

This patch also enables the `implementation` syntax in the graph generators.


---

Comment by rlm created at 2009-03-02 18:44:24

Changing status from new to assigned.


---

Comment by rlm created at 2009-03-02 18:47:10

One comment: note the deletion of the step checking whether the sorted degree sequences are the same. This is now an intrinsic part of the algorithm used for isomorphism checking, so this is redundant effort.


---

Comment by rlm created at 2009-03-02 19:27:42

Note: this is a patch based on Sage-3.3, so the documentation is still pre-reST


---

Comment by mabshoff created at 2009-03-02 19:59:13

Yep, the patch definitely needs a rebase:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.alpha1/devel/sage$ patch -p1 --dry-run < trac_5421.patch 
patching file sage/graphs/graph.py
Hunk #1 succeeded at 335 (offset 70 lines).
Hunk #2 succeeded at 7587 (offset 664 lines).
patching file sage/graphs/graph_generators.py
Hunk #1 FAILED at 242.
Hunk #2 FAILED at 258.
Hunk #3 succeeded at 3111 with fuzz 2 (offset 308 lines).
Hunk #4 FAILED at 3143.
Hunk #5 succeeded at 3199 (offset 325 lines).
Hunk #6 FAILED at 3324.
Hunk #7 FAILED at 3338.
Hunk #8 succeeded at 3660 with fuzz 2 (offset 386 lines).
Hunk #9 FAILED at 3686.
Hunk #10 succeeded at 3739 with fuzz 1 (offset 403 lines).
Hunk #11 succeeded at 3870 (offset 419 lines).
Hunk #12 succeeded at 3894 (offset 419 lines).
Hunk #13 succeeded at 3907 (offset 419 lines).
Hunk #14 succeeded at 3952 with fuzz 1 (offset 421 lines).
Hunk #15 succeeded at 4092 (offset 434 lines).
Hunk #16 succeeded at 4111 (offset 434 lines).
6 out of 16 hunks FAILED -- saving rejects to file sage/graphs/graph_generators.py.rej
```


Cheers,

Michael


---

Attachment

I rebased the patch to 3.4.alpha0, but I don't have a built copy yet, so I couldn't test. But I'm pretty sure it should work. What could go wrong?


---

Comment by mabshoff created at 2009-03-02 23:24:38

One doctest failure:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.alpha1$ ./sage -t -long devel/sage/sage/combinat/words/suffix_trees.py
sage -t -long "devel/sage/sage/combinat/words/suffix_trees.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.alpha1/devel/sage/sage/combinat/words/suffix_trees.py", line 1263:
    sage: t.uncompactify().is_isomorphic(s.to_digraph())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[6]>", line 1, in <module>
        t.uncompactify().is_isomorphic(s.to_digraph())###line 1263:
    sage: t.uncompactify().is_isomorphic(s.to_digraph())
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 7631, in is_isomorphic
        G2 = G2.copy(implementation='c_graph')
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 707, in copy
        G = DiGraph(self, name=self.name(), pos=copy(self._pos), boundary=copy(self._boundary), implementation=implementation, sparse=sparse)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 9859, in __init__
        self._backend.add_edge(u,v,l,True)
      File "sparse_graph.pyx", line 1171, in sage.graphs.base.sparse_graph.SparseGraphBackend.add_edge (sage/graphs/base/sparse_graph.c:9597)
      File "sparse_graph.pyx", line 515, in sage.graphs.base.sparse_graph.SparseGraph.add_arc_label (sage/graphs/base/sparse_graph.c:3980)
    TypeError: an integer is required
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_38
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.alpha1/tmp/.doctest_suffix_trees.py
         [2.9 s]
```


Cheers,

Michael


---

Comment by rlm created at 2009-03-03 07:23:22

Looks like that second patch is not ready yet...


---

Attachment


---

Comment by rlm created at 2009-03-04 20:03:22

I forgot one line in patch b, now all is well.


---

Comment by mabshoff created at 2009-03-08 05:20:27

Mike: Can you give this patch a review? 

Cheers,

Michael


---

Comment by ncalexan created at 2009-03-08 06:35:03

mabshoff has doctested.  I can't guarantee this speeds up {all,any} cases and I have only read over the modified code -- this is so deeply nested that I can only give a 3/4 thumbs up.


---

Comment by mabshoff created at 2009-03-08 06:52:58

Merged both patches in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 06:52:58

Resolution: fixed
