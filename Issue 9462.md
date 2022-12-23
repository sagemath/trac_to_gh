# Issue 9462: warning in matrix_modn_dense.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9462

Original creator: wjp

Original creation time: 2010-07-09 08:31:52

Assignee: GeorgSWeber

cython gives a warning when compiling `matrix_modn_dense.pyx`:


```
warning: /data2/wpalenst/sage-4.5.alpha4/devel/sage-main/sage/matrix/matrix_modn_dense.pyx:105:8: Function signature does not match previous declaration
```


I'll upload a patch in an hour.


---

Attachment


---

Comment by wjp created at 2010-07-09 09:37:12

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-07-23 01:21:36

The patch makes the warning go away and all tests pass afterwards.  Since the declaration is already included via `include "../ext/cdefs.pxi"`, getting rid of the extra one looks fine.  Positive review.


---

Comment by jhpalmieri created at 2010-07-23 01:21:36

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-26 02:18:57

Resolution: fixed
