# Issue 764: PolynomialRing returns an MPolynomialRing when the number of variables is explicitly set to be 1.

Issue created by migration from https://trac.sagemath.org/ticket/764

Original creator: mhansen

Original creation time: 2007-09-30 07:11:26

Assignee: mhansen


sage: type(PolynomialRing(ZZ, 1, 'x'))
<class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_domain'>

sage: type(PolynomialRing(ZZ, 'x'))
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_integral_domain'>



---

Comment by mhansen created at 2007-09-30 07:30:58

From William Stein:
> Wait!  This would an explicit intentional design choice, not a bug.
> I think it should be possible to create ZZ['x'] but as a multivariate
> polynomial ring instead of a univariate polynomial ring,
> since there are certain things one can do with multivariate
> polynomial rings that don't make sense with single variate rings.
> 
> Maybe I'm wrong, since things have been so well developed by now.
> I would like some further discussion and input (esp. from Martin Albrecht)
> on this before changing anything.


---

Comment by mhansen created at 2007-09-30 18:21:08

> sage: PolynomialRing(ZZ, 'x')
> Univariate Polynomial Ring in x over Integer Ring
> sage: PolynomialRing(ZZ, 1, 'x')
> Polynomial Ring in x over Integer Ring
>
> The second one is a bit ambiguous.  How do people feel about changing
> the reprs of multivariate polynomial rings so that the second one
> would be 'Multivariate Polynomial Ring in x over Integer Ring'?


---

Comment by mhansen created at 2007-09-30 18:22:47

Patches posted to change the repr of multivariate polynomials rings.  -testall passes, but the test for hash(P) in multi_polynomial_libsingular.pyx needs to be changed for 32 bit machines.


---

Attachment


---

Attachment


---

Comment by was created at 2007-10-04 18:21:35

Resolution: fixed
