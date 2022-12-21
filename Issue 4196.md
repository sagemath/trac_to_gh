# Issue 4196: write a new coercion section for the developer's/programmer's guide

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-09-25 21:58:29

Assignee: somebody

Keywords: coercion, documentation

The coercion section of the developer's guide is completely out of date and needs to be rewritten.




---

Comment by jhpalmieri created at 2008-10-13 17:26:23

See also #4272.


---

Comment by jhpalmieri created at 2009-02-14 21:29:14

See also Robert Bradshaw's coercion docs on the [Sage wiki](http://wiki.sagemath.org/coercion).


---

Comment by jhpalmieri created at 2009-06-17 22:03:27

Changing assignee from somebody to jhpalmieri.


---

Comment by jhpalmieri created at 2009-06-17 22:03:27

Changing status from new to assigned.


---

Attachment

Here's a patch.  This basically just refers to the coercion section in the reference manual, added in #5454.


---

Comment by mvngu created at 2009-06-19 23:02:10

rebased against Sage 4.0.2


---

Attachment

When applying the patch `trac_4196.patch` against Sage 4.0.2, I received one hunk failure:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4196/trac_4196.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/4196/trac_4196.patch
Loading: [..]
cd "/scratch/mvngu/sage-4.0.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.2/devel/sage" && hg import   "/home/mvngu/.sage/temp/sage.math.washington.edu/5611/tmp_1.patch"
applying /home/mvngu/.sage/temp/sage.math.washington.edu/5611/tmp_1.patch
patching file doc/en/reference/coercion.rst
Hunk #3 FAILED at 244
1 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/coercion.rst.rej
abort: patch failed to apply
```

The patch `trac_4196.2.patch` is a rebase against Sage 4.0.2. It turns out that the cause of the failure was line 248 in the first patch. So the only difference between `trac_4196.patch` and `trac_4196.2.patch` is that in `trac_4196.2.patch` I left out line 248 in the original patch. Apart from the rebase, positive review.


---

Comment by rlm created at 2009-06-24 09:48:50

Resolution: fixed


---

Comment by robertwb created at 2009-06-25 10:20:41

Yes, you beat me to it, but positive review from me too.
