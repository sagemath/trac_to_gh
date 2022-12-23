# Issue 8966: Polynomial reduce causes segmentation fault

Issue created by migration from https://trac.sagemath.org/ticket/8966

Original creator: mariah

Original creation time: 2010-05-14 18:18:46

Assignee: AlexGhitza

CC:  malb polybori


```
eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R=BooleanPolynomialRing(20,'x','lex')
sage: a=R.random_element()
sage: a.reduce([None,None])
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

eno%
```



---

Comment by burcin created at 2010-06-04 11:54:28

Changing priority from minor to critical.


---

Comment by burcin created at 2010-06-04 11:54:28

Changing status from new to needs_review.


---

Comment by burcin created at 2010-06-04 11:54:28

This was a simple input checking problem in our interface to polybori. I would have expected Cython not to accept `None` as a `BooleanPolynomial` though.


---

Comment by malb created at 2010-06-04 12:37:12

Patch looks good, doctests pass.


---

Comment by malb created at 2010-06-04 12:37:12

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by was created at 2010-06-04 14:59:45

Looks good.  Note I changed it from ValueError to TypeError, since it is really a TypeError, and that's what Cython should raise.


---

Comment by mhansen created at 2010-06-06 00:59:23

Resolution: fixed
