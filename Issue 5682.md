# Issue 5682: Quotient for univariate Laurent polynomials

Issue created by migration from https://trac.sagemath.org/ticket/5682

Original creator: kedlaya

Original creation time: 2009-04-04 14:55:46

Assignee: tbd

Keywords: Laurent polynomial, quotient, division

It would be nice if this worked rather than returning an error:

```
sage: F.<t> = LaurentPolynomialRing(GF(2))
sage: t // t
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/kedlaya/.sage/temp/kedlaya_laptop/18179/_home_kedlaya__sage_init_sage_0.py in <module>()

TypeError: unsupported operand type(s) for //: 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair' and 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'
```

As it stands, I don't think univariate Laurent polynomial rings over a field support any division operation that stays within the ring:

```
sage: (t/t).parent()
Fraction Field of Univariate Laurent Polynomial Ring in t over Finite Field of size 2
```

except maybe if I access the internal representation (as a quotient ring) and implement it by hand.



---

Comment by tscrim created at 2014-04-09 04:21:12

Changing status from new to needs_review.


---

Comment by tscrim created at 2014-04-09 04:21:12

This is done in #11726.


---

Comment by kedlaya created at 2014-04-09 17:11:27

Agreed, thanks!


---

Comment by kedlaya created at 2014-04-09 17:11:27

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-09 19:42:23

Resolution: duplicate
