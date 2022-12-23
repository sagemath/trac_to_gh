# Issue 5026: numerical noise doctest failure in rings/polynomial/complex_roots.py

Issue created by migration from https://trac.sagemath.org/ticket/5026

Original creator: mhampton

Original creation time: 2009-01-19 16:11:44

Assignee: jkantor

Keywords: complex roots, polynomial

On sage-3.3.alpha0 I get this doctest failure on an intel mac:


```
**********************************************************************
File ".../devel/sage/sage/rings/polynomial/complex_roots.py", line
270:
    sage: complex_roots(x^2 + 27*x + 181)
Expected:
    [(-14.61803398874990?..., 1), (-12.38196601125010? + 0.?e-27*I,
1)]
Got:
    [(-14.61803398874990? + 0.?e-27*I, 1), (-12.38196601125011? + 0.?
e-27*I, 1)]
********************************************************************** 
```



---

Attachment

Attached patch fixes the doctest.


---

Comment by craigcitro created at 2009-01-23 13:19:56

Changing assignee from jkantor to craigcitro.


---

Comment by craigcitro created at 2009-01-23 13:19:56

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-23 16:17:28

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 13:18:27

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 13:18:27

Resolution: fixed
