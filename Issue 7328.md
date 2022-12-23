# Issue 7328: latex doesn't handle python floats correctly

Issue created by migration from https://trac.sagemath.org/ticket/7328

Original creator: jason

Original creation time: 2009-10-28 00:35:44

Assignee: cwitty

CC:  kcrisman

Compare:


```
sage: latex(float(3e-10))
3e-10
sage: latex(RR(3e-10))
3.00000000000000 \times 10^{-10}
```




---

Attachment


---

Comment by jason created at 2009-10-28 03:45:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-29 18:37:25

This seems good and consistent with the rest of the latex_table, and certainly makes sense for the notebook!  Unless there are other obvious places to put doctests for this (notebook?), positive review.


---

Comment by kcrisman created at 2009-10-29 18:37:25

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 15:59:36

Resolution: fixed
