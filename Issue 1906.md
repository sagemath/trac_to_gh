# Issue 1906: [with patch, needs review] eisenstein_series_qexp does not pay attention to the field parameter

Issue created by migration from https://trac.sagemath.org/ticket/1906

Original creator: AlexGhitza

Original creation time: 2008-01-24 03:34:38

Assignee: AlexGhitza

The function eisenstein_series_qexp() has a parameter K which is supposed to say what field the coefficients of the series should live in, but it always returns rational coefficients:


```
sage: eisenstein_series_qexp(10,6,GF(5))
-1/264 + q + 513*q^2 + 19684*q^3 + 262657*q^4 + 1953126*q^5 + O(q^6)
sage: eisenstein_series_qexp(10,6,QQ)
-1/264 + q + 513*q^2 + 19684*q^3 + 262657*q^4 + 1953126*q^5 + O(q^6)
```



---

Attachment


---

Comment by AlexGhitza created at 2008-01-24 03:37:51

Easy fix and new doctest -- see the attached patch.


---

Comment by craigcitro created at 2008-01-25 18:07:30

Looks good -- clearly I didn't even read the docstring to notice there was supposed to be a base_ring argument when rewriting this! :)

On a completely insignificant note, I'm not sure why you did a0inv = ..., and then K(1/a0inv) -- K(a0) would raise a ZeroDivisionError all the same. (It still works just fine, of course, it just confused me for a sec.)


---

Comment by mabshoff created at 2008-01-25 18:13:00

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-25 18:13:00

Resolution: fixed


---

Comment by AlexGhitza created at 2008-01-25 23:13:09

Craig: you're completely right about the a0inv thing, of course.  It's just that in the error message that we're raising I wanted to print the value of a0inv, and I couldn't think of a better way of doing it.
