# Issue 6659: cores() is broken for some digraphs, and is *way* too slow

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-07-30 08:38:51

Assignee: rlm

CC:  rlm rbeezer hartke

Here is a patch, based on the networkx code, which implements some of the optimizations noted in the paper referenced in the networkx documentation.  This leads to what I think are asymptotic speedups.

As for the bug, before, the doctest added would fail from an error in the networkx code.  Now it does not.


---

Comment by jason created at 2009-07-30 09:35:49

I fixed a bug (the doctest I added used to fail), implemented some optimizations that massively sped things up, and cleaned up the documentation.

Robert or Rob, can one of you review this so it can go into 4.1.1?


---

Comment by jason created at 2009-07-30 09:39:24

An example of a speedup:

BEFORE:


```
sage: a=random_matrix(GF(2), 50000, density=0.0001,sparse=True)
sage: len(a.nonzero_positions())
125063
sage: c=DiGraph(50000)
sage: c.add_edges(a.nonzero_positions())
sage: %time
sage: e=c.cores(with_labels=True)
CPU time: 429.14 s,  Wall time: 430.89 s
```


AFTER:


```
sage: d=c.cores(with_labels=True)
CPU time: 1.86 s,  Wall time: 1.86 s
sage: e==d
True
```



---

Attachment

I added a couple of comments to help the reader see what is happening in the source code.


---

Comment by mvngu created at 2009-08-25 02:21:13

reviewer patch; typo fix


---

Attachment

The patch `trac_6659-reviewer.patch` fixes a typo found in `trac_6659-graph-cores.patch`.


---

Comment by mvngu created at 2009-08-25 03:04:27

Resolution: fixed


---

Comment by mvngu created at 2009-08-25 03:05:01

Merged both patches.
