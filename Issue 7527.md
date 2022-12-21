# Issue 7527: include graph_coloring in the reference manual.

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-11-25 08:44:39

Assignee: rlm

CC:  mvngu

As mentionned in #6679 the file graph_coloring is not included in the docstrings. Apply this patch, and this is fixed :-)

Nathann


---

Comment by ncohen created at 2009-11-25 08:45:29

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2009-11-25 10:30:24

Changing component from graph theory to documentation.


---

Comment by mvngu created at 2009-12-08 19:00:25

rebased; based on Sage 4.3.alpha1


---

Attachment

reviewer patch


---

Attachment

The patch `trac_7527.patch` doesn't apply cleanly on top of Sage 4.3.alpha1:

```
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7527/trac_7527.patch
adding trac_7527.patch to series file
[mvngu`@`sage sage-main]$ hg qpush
applying trac_7527.patch
patching file sage/graphs/graph_coloring.py
Hunk #3 FAILED at 143
Hunk #4 succeeded at 175 with fuzz 1 (offset 14 lines).
Hunk #7 succeeded at 651 with fuzz 1 (offset 416 lines).
1 out of 7 hunks FAILED -- saving rejects to file sage/graphs/graph_coloring.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7527.patch
```

The rejected hunk is

```
[mvngu`@`sage ~]$ cat graph_coloring.py.rej 
--- graph_coloring.py
+++ graph_coloring.py
`@``@` -142,11 +144,12 `@``@`
         raise RuntimeError, "Too much recursion!  Graph coloring failed."
 
 def first_coloring(G,n=0):
-    """
-    Given a graph, and optionally a natural number n, returns
-    the first coloring we find with at least n colors.
+    r"""
+    Given a graph, and optionally a natural number `n`, returns
+    the first coloring we find with at least `n` colors.
 
-    EXAMPLES:
+    EXAMPLES::
+
         sage: from sage.graphs.graph_coloring import first_coloring
         sage: G = Graph({0:[1,2,3],1:[2]})
         sage: first_coloring(G,3)
```

which fails to apply because #6679 already takes care of that hunk. I have rebased ncohen's patch using Sage 4.3.alpha1; see `trac_7527-rebased.patch` which doesn't include the rejected hunk. I'm OK with ncohen's original patch, so only the rebased patch and my patch `trac_7527-reviewer.patch` needs reviewing. Patches should be applied in this order:

 1. `trac_7527-rebased.patch`
 1. `trac_7527-reviewer.patch`


---

Comment by ncohen created at 2009-12-09 13:57:23

Perfect job, as usual... Thank you very much, and positive review to your added patch !

Nathann


---

Comment by ncohen created at 2009-12-09 13:57:23

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-14 15:57:49

Resolution: fixed
