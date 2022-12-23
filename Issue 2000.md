# Issue 2000: bug either in polynomial factorization or polynomial ring constructor

Issue created by migration from https://trac.sagemath.org/ticket/2000

Original creator: was

Original creation time: 2008-01-31 06:25:40

Assignee: malb


```
> ----------------------------------------------------------------------
> | SAGE Version 2.10, Release Date: 2008-01-18                        |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> 
> sage: R.<z> = PolynomialRing(CC,1)
> sage: f = z^4 - 6*z + 3
> sage: f.factor()

BOOM!


This is a bug.  Fortunately, there is an easy workaround (see below). 
Don't put PolynomialRing(CC, 1); instead put PolynomialRing(CC).

sage: R.<z> = PolynomialRing(CC)
sage: f = z^4 - 6*z + 3
sage: f.factor()
(1.00000000000000*z - 1.60443920904349) * (1.00000000000000*z - 0.511399619393097) * (1.00000000000000*z + 1.05791941421830 - 1.59281852704435*I) * (1.00000000000000*z + 1.05791941421830 + 1.59281852704435*I)

The problem is that PolynomialRing(CC,1) creates a *multivariate polynomial ring*
which happens to be in 1 variable, whereas PolynomialRing(CC) creates a 
univariate polynomial ring (which is implemented under the hood differently
than a multivariate polynomial ring).

The bug is that PolynomialRing(CC,1) should create a univariate ring,
whereas MPolynomialRing(CC,1) should be how one creates a multivariate
poly ring in 1 variable.   (I think.)

Alternatively, the bug is that factoring a multivariate polynomial in 1 variable
uses Singular instead of other better univariate code that we have. 
```




---

Comment by malb created at 2008-01-31 09:41:54

> The bug is that PolynomialRing(CC,1) should create a univariate ring,
> whereas MPolynomialRing(CC,1) should be how one creates a multivariate
> poly ring in 1 variable.

I agree.

> Alternatively, the bug is that factoring a multivariate polynomial in 1 variable
> uses Singular instead of other better univariate code that we have. 

Also, I agree.


---

Comment by malb created at 2008-08-18 13:31:14

Changing type from defect to enhancement.


---

Attachment

Replying to [comment:1 malb]:
> > The bug is that PolynomialRing(CC,1) should create a univariate ring,
> > whereas MPolynomialRing(CC,1) should be how one creates a multivariate
> > poly ring in 1 variable.
> 
> I agree.

Since MPolynomialRing is deprecated now, the reported behavior is indeed the correct behavior.
 
> > Alternatively, the bug is that factoring a multivariate polynomial in 1 variable
> > uses Singular instead of other better univariate code that we have. 

This is fixed in the attached patch.


---

Comment by cwitty created at 2008-08-23 17:48:42

Looks good; all tests pass.


---

Comment by mabshoff created at 2008-08-25 00:42:01

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-25 00:42:01

Resolution: fixed
