# Issue 6585: [with patch, needs review] trivial change to a few docstrings in partition.py

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-22 05:04:28

Assignee: jhpalmieri

CC:  sage-combinat

This patch changes a few docstrings in partition.py which contain backslashes from

```
"""
blah
"""
```

to

```
r"""
blah
"""
```

(I've been playing with version 0.6.2 of Sphinx, and it barfs without making this change.)



---

Attachment


---

Attachment

fix warning when building HTML version of sage/combinat/partition.py


---

Comment by mvngu created at 2009-07-24 08:22:34

Resolution: fixed


---

Comment by mvngu created at 2009-07-24 08:22:34

Positive review for the patch `trac_6585-backslash.patch`. After importing the changes in that patch and rebuilding the HTML version of the reference manual, I got the following warning:

```
WARNING: /scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/combinat/partition.py:docstring of sage.combinat.partition.Partition_class.conjugate:1: (WARNING/2) Inline literal start-string without end-string.
```

This is fixed by `trac_6585-fix-warnings.patch`. Merged both patches.
