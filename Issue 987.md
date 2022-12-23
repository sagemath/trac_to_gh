# Issue 987: integrate(1/sqrt(9+x^2)) fails

Issue created by migration from https://trac.sagemath.org/ticket/987

Original creator: mhansen

Original creation time: 2007-10-25 01:03:00

Assignee: mhansen

integrate(1/sqrt(9+x^2))
x/3

I tried this at home and numerous times on sagenb.org.  Every other
plausible syntax of this integral I tried (-1 power, more parentheses,
switch the summands, etc.) yields the same result

Here's the reason

```
(%i1) integrate(1/sqrt(9+x^2),x)
;
                                         x
(%o1)                              asinh(-)
                                         3


```



---

Comment by was created at 2007-10-25 01:16:15

Changing priority from major to blocker.


---

Comment by was created at 2007-10-25 01:45:52

fixes this problem.


---

Attachment


---

Attachment


---

Comment by was created at 2007-10-25 06:44:35

Resolution: fixed
