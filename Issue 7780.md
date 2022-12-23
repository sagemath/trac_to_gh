# Issue 7780: latex problems from underscores in docstrings

Issue created by migration from https://trac.sagemath.org/ticket/7780

Original creator: cremona

Original creation time: 2009-12-28 16:38:16

Assignee: mvngu

Keywords: latex

Building docs in 4.3, there are some latex errors:

```
WARNING: display latex u'\\mbox{min_bound} \\leq \\mbox{linear_function} \\leq \\mbox{max_bound}': latex exited with error:
```

caused by the underscores in min_bound, max_bound and linear_function.  These come from numerical/mip.pyx.



---

Comment by cremona created at 2009-12-28 16:57:16

Applies to 4.3


---

Attachment

Patch attached.  Review is trivial but requires waiting for docs to rebuild...


---

Comment by cremona created at 2009-12-28 16:58:31

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-12-28 17:15:54

Resolution: duplicate


---

Comment by mvngu created at 2009-12-28 17:15:54

This is a duplicate of #7768. The latter has already received positive review.


---

Comment by cremona created at 2009-12-28 17:18:37

Replying to [comment:2 mvngu]:
> This is a duplicate of #7768. The latter has already received positive review.

Fair enough, I wasted your (and my) time, sorry.  I did look for a ticket on this but obviously not well enough.
