# Issue 7967: DeprecationWarning for popen3 in hg_sage

Issue created by migration from https://trac.sagemath.org/ticket/7967

Original creator: wjp

Original creation time: 2010-01-17 18:34:34

Assignee: tbd

Using `hg_sage` is raising a `DeprecationWarning`:


```
/data/sage/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
```



---

Comment by wjp created at 2010-01-17 18:36:08

Changing status from new to needs_review.


---

Attachment

Good job; looks good.


---

Comment by timdumol created at 2010-01-17 19:19:07

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 00:55:56

Resolution: fixed
