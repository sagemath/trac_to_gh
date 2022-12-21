# Issue 8211: bug in multiplication of polynomials over RR

Issue created by migration from Trac.

Original creator: dimpase

Original creation time: 2010-02-08 05:32:29

Assignee: malb

Keywords: RealField, PolynomialRing

as reported on sage-devel [Segfault: Polynomials over RealField]
sage: P.<x> = PolynomialRing(RealField()) 
sage: P(0)*P(0)+P(0) 
Program received signal SIGSEGV, Segmentation fault. 

it can be traced down to a bug in _mul_ that computes the degree
of the polynomial P(0)*P(0) wrongly (-2 istead of -1 !)
Patch is trivial, and attached.


---

Attachment


---

Comment by dimpase created at 2010-02-08 05:34:32

Changing status from new to needs_review.


---

Comment by malb created at 2010-02-08 10:33:17

Looks good.


---

Comment by malb created at 2010-02-08 10:33:17

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 14:21:14

The ticket number is missing from the commit string.  I've refreshed the patch I've applied to 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 14:44:14

Resolution: fixed
