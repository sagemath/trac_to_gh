# Issue 7299: show() regression: Picture cropped too much

Issue created by migration from Trac.

Original creator: AJonsson

Original creation time: 2009-10-25 18:26:25

Assignee: was

CC:  rlm rbeezer

In sage 4.1.2 and later, the show() function shows graphs so cropped that their vertices are partially missing.

This is a regression in 4.1.2 and later, Sage 4.1.1 is fine.

Attaching the figures from

```
G=graphs.CycleGraph(3);G.show()
```

to show the issue.


---

Attachment

Triangle graph in 4.1.1


---

Attachment

Triangle graph in 4.1.2


---

Attachment


---

Comment by jason created at 2010-01-20 10:54:19

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-20 10:54:52

The attached patch is a one-line fix that makes graph vertices not be cut off now.


---

Comment by robertwb created at 2010-01-20 10:58:02

LGTM. Such a small change for a big impact.


---

Comment by robertwb created at 2010-01-20 10:58:02

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 22:45:47

Resolution: fixed


---

Comment by mvngu created at 2010-01-23 22:45:47

Merged [trac-7299-graph-pad.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7299/trac-7299-graph-pad.patch).
