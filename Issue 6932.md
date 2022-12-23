# Issue 6932: jordan_form with transformation=true fails on a 1x1 matrix.

Issue created by migration from https://trac.sagemath.org/ticket/6932

Original creator: syazdani

Original creation time: 2009-09-15 05:54:37

Assignee: tbd

Keywords: jordan_form

The following code fails:

```
M=Matrix(1,1,[1])
M.jordan_form(transformation=True)
```




---

Comment by AlexGhitza created at 2009-11-15 13:10:30

Changing component from algebra to linear algebra.


---

Comment by spancratz created at 2010-01-19 12:29:10

Changing status from new to needs_review.


---

Comment by spancratz created at 2010-01-19 12:29:10

This is fixed by the patch at ticket #6942.  Once that ticket receives a positive review, this ticket can be closed.


---

Comment by zimmerma created at 2010-02-25 22:13:13

I checked with sage-4.3.3, and we indeed get the correct rank (7) for #6942, thus I guess we can
indeed close that ticket:

```
sage: M=Matrix(1,1,[1])
sage: M.jordan_form(transformation=True)
([1], [1])
```



---

Comment by zimmerma created at 2010-02-25 22:13:13

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 04:11:11

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 04:11:11

Close as fixed by #6942.
