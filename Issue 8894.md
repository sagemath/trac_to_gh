# Issue 8894: topological minor

Issue created by migration from https://trac.sagemath.org/ticket/8894

Original creator: ncohen

Original creation time: 2010-05-05 18:24:48

Assignee: jason, ncohen, rlm

Using #8893


---

Comment by ncohen created at 2010-06-06 11:01:00

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-09-19 00:40:05

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-09-19 00:41:16

Changing type from defect to enhancement.


---

Comment by lsampaio created at 2011-01-10 16:29:01

The patch seens to be correct and I believe it is ready to be merged to sage.


---

Comment by lsampaio created at 2011-01-10 16:29:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-18 13:44:38

Even though the patch applies (with fuzz and large offset), you should rebase it to sage-4.6.2.alpha0:

```
patching file sage/graphs/graph.py
Hunk #1 succeeded at 2960 with fuzz 2 (offset 461 lines).
```



---

Comment by jdemeyer created at 2011-01-18 13:44:38

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by ncohen created at 2011-01-18 17:24:34

Done !

Nathann


---

Comment by ncohen created at 2011-01-18 17:24:34

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:19:49

Resolution: fixed
