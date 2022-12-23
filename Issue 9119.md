# Issue 9119: Cython variables used then later declared

Issue created by migration from https://trac.sagemath.org/ticket/9119

Original creator: jason

Original creation time: 2010-06-03 02:23:06

Assignee: jason, was

CC:  robertwb wcauchois

This patch takes care of a minor issue with variables being used, and then later declared.  This takes care of these warnings:


```
warning: /Users/grout/sage-4.4.2/devel/sage-main/sage/plot/plot3d/parametric_surface.pyx:355:20: cdef variable 'u' declared after it is used
warning: /Users/grout/sage-4.4.2/devel/sage-main/sage/plot/plot3d/parametric_surface.pyx:355:23: cdef variable 'v' declared after it is used
```




---

Attachment

This ticket is a trivial one to review!


---

Comment by jason created at 2010-06-03 02:25:02

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-06-03 03:01:55

Yep.


---

Comment by robertwb created at 2010-06-03 03:01:55

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 00:57:03

Resolution: fixed
