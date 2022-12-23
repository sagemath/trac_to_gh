# Issue 7554: bug in multivariate polynomial factorization

Issue created by migration from https://trac.sagemath.org/ticket/7554

Original creator: was

Original creation time: 2009-11-29 08:49:16

Assignee: malb

This is suspicious:


```
sage: # define the coefficient field K and R=K[x,y]
sage: K.<a>=PolynomialRing(QQ,1)
sage: K=FractionField(K)
sage: R.<x,y>=PolynomialRing(K,2)
sage: factor(x^2-y^2)
(x - y) * (x + y)
sage: factor(x)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/Users/wstein/<ipython console> in <module>()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/arith.pyc in factor(n, proof, int_, algorithm, verbose, **kwds)
   2100         # this happens for example if n = x**2 + y**2 + 2*x*y
   2101         try:
-> 2102             return n.factor(proof=proof, **kwds)
   2103         except AttributeError:
   2104             raise TypeError, "unable to factor n"

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)
   1422         # try to use univariate factoring first
   1423         try:
-> 1424             F = self.univariate_polynomial().factor()
   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())
   1426         except TypeError:

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.factor (sage/rings/polynomial/polynomial_element.c:22319)()

NotImplementedError: 
```


See emails from Stefan Boettner in sage-support on Nov 28, 2009


---

Comment by darij created at 2013-06-22 12:51:27

Would it make sense to except not only `TypeError`, but also `AttributeError` (for the case when `univariate_polynomial` is not a method of `self`) and `NotImplementedError` (for exactly the reason that's happening here)?


---

Comment by tscrim created at 2014-06-23 01:18:36

I've implemented a fallback using singular for generic univariate polynomials (which is what the multivariate case did). I'm not 100% sure it is the best solution (in fact the factorization can be somewhat strange IMO), but it works:

```
sage: L.<q> = LaurentPolynomialRing(QQ)
sage: F = L.fraction_field()
sage: R.<x> = PolynomialRing(F)
sage: factor(x)
x
sage: factor(x^2 - q^2)
(-1) * (-x + q) * (x + q)
sage: factor(x^2 - q^-2)
(1/q^2) * (q*x - 1) * (q*x + 1)

sage: P.<a,b,c> = PolynomialRing(ZZ)
sage: R.<x> = PolynomialRing(FractionField(P))
sage: p = (x - a)*(b*x + c)*(a*b*x + a*c) / (a + 2)
sage: factor(p)
(a/(a + 2)) * (x - a) * (b*x + c)^2
```

----
New commits:


---

Comment by tscrim created at 2014-06-23 01:18:36

Changing status from new to needs_review.


---

Comment by tscrim created at 2014-06-23 01:18:36

Changing keywords from "" to "sd59".


---

Comment by malb created at 2014-06-26 17:36:38

Looks okay.


---

Comment by malb created at 2014-06-26 17:36:38

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-06-27 01:43:20

Resolution: fixed
