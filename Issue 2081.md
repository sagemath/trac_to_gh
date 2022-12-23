# Issue 2081: Add .coefficients() and .exponents() to univariate polynomials and power series

Issue created by migration from https://trac.sagemath.org/ticket/2081

Original creator: jbandlow

Original creation time: 2008-02-07 07:39:15

Assignee: somebody

This should work:


```
sage: R.<x> = QQ[]
sage: f = x^2+2*x
sage: f.exponents()
[1, 2]
sage: f.coefficients()
[2, 1]
```



---

Comment by mhansen created at 2008-02-07 07:47:50

Changing status from new to assigned.


---

Comment by mhansen created at 2008-02-07 07:47:50

Changing assignee from somebody to mhansen.


---

Comment by malb created at 2008-02-14 23:43:14

The patch looks good, one thing though: every parent is supposed to provide a `zero_element()` method, this could be used (but that isn't really important)


---

Attachment

Updated patch to use .zero_element()


---

Comment by malb created at 2008-02-15 00:37:13

`make test` passes, patch looks good, apply!


---

Comment by mabshoff created at 2008-02-15 02:16:11

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-15 02:16:11

Resolution: fixed
