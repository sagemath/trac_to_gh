# Issue 3026: multivariate polynomial ring with no variables do not print properly

Issue created by migration from https://trac.sagemath.org/ticket/3026

Original creator: broune

Original creation time: 2008-04-26 00:24:06

Assignee: malb

The following output from sage does not make too much sense.

sage: PolynomialRing(QQ, names=[])
Multivariate Polynomial Ring in  over Rational Field

wstein suggested that it might print something like the following.

Multivariate Polynomial Ring in no variables over Rational Field


---

Comment by broune created at 2008-05-07 20:15:55

Changing assignee from malb to broune.


---

Comment by broune created at 2008-05-07 20:16:10

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2008-05-10 23:06:29

Code looks good, doctests pass in sage/rings/polynomial.  Positive review.


---

Comment by mabshoff created at 2008-05-11 09:22:07

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 09:22:07

Merged in Sage 3.0.2.alpha0
