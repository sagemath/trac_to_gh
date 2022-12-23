# Issue 7425: I.variety() doesn't check that I is zero-dimensional

Issue created by migration from https://trac.sagemath.org/ticket/7425

Original creator: AlexGhitza

Original creation time: 2009-11-10 23:11:29

Assignee: malb

`I.variety()` should first check whether the ideal I is indeed 0-dimensional and refuse to continue otherwise.  This should be a fairly trivial fix.  Right now the following seems to run forever:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x, y, z> = QQ[]
sage: I = R.ideal([x^2-y^3*z, x+y*z])
sage: I.dimension()
1
sage: I.variety()
verbose 0 (1808: multi_polynomial_ideal.py, variety) Warning: falling back to very slow toy implementation.
```

| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |


---

Attachment


---

Comment by AlexGhitza created at 2009-11-11 13:34:15

Changing status from new to needs_review.


---

Comment by malb created at 2009-11-11 14:12:22

patch looks good, applies cleanly against 4.2, doctests pass, reference manual builds without any warnings.


---

Comment by malb created at 2009-11-11 14:12:22

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 07:21:33

Resolution: fixed
