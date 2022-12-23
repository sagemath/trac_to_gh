# Issue 5480: R.quotient_by_principal_ideal() is self-contradictory

Issue created by migration from https://trac.sagemath.org/ticket/5480

Original creator: justin

Original creation time: 2009-03-11 05:23:45

Assignee: was

The following seems absurd:

```
sage: R.<x> = PolynomialRing(QQ)
sage: I = (x^2-1)*R
sage: S = R.quotient_by_principal_ideal(I)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/justin/.sage/temp/Hasse_2.local/32509/_tmp_z_sage_9.py in <module>()

/SandBox/Justin/sb/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in quotient_by_principal_ideal(self=Univariate Polynomial Ring in x over Rational Field, f=Principal ideal (x^2 - 1) of Univariate Polynomial Ring in x over Rational Field, names=None)
   1004         """
   1005         import sage.rings.polynomial.polynomial_quotient_ring
-> 1006         return sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing(self, f, names)
   1007 
   1008 

/SandBox/Justin/sb/sage-3.2.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in PolynomialQuotientRing(ring=Univariate Polynomial Ring in x over Rational Field, polynomial=Principal ideal (x^2 - 1) of Univariate Polynomial Ring in x over Rational Field, names=None)
    128         raise TypeError, "ring must be a polynomial ring"
    129     if not isinstance(polynomial, polynomial_element.Polynomial):
--> 130         raise TypeError, "must be a polynomial"
        global EXAMPLES = undefined
    131     if not polynomial.parent() == ring:
    132         raise TypeError, "polynomial must be in ring"

TypeError: must be a polynomial
```

Either the procedure should be ...by_polynomial(), or it should really accept an ideal as an argument.

Sheesh.




---

Attachment

The fix is to permit both a polynomial (for backward compatibility) and an ideal as the argument.  Doctested the rings/polynomial directory w/o problems.


---

Comment by cremona created at 2009-03-14 20:39:35

The patch looks ok but there should be doctests to illustrate the new behaviour, and the docstring should also say what input is valid.


---

Comment by justin created at 2009-03-16 03:14:26

Changing assignee from was to justin.


---

Comment by justin created at 2009-03-16 03:14:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-06 06:03:30

Justin,

any chance you can add some doctests here? I am marking this as "needs works" until then.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-11-15 11:51:59

Changing component from algebraic geometry to algebra.


---

Comment by AlexGhitza created at 2009-11-15 12:46:45

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2009-11-15 12:46:45

The new patch fixes the issue and has doctests.  It depends on the patch at #5482.

Apply only trac_5480.patch


---

Comment by AlexGhitza created at 2009-11-15 12:47:18

apply this patch only; depends on #5482


---

Comment by mhansen created at 2009-11-17 08:04:35

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-11-17 08:04:45

Resolution: fixed
