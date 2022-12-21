# Issue 7950: factoring broken in 0 variable polynomial ring

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-01-16 17:52:56

Assignee: malb


```
sage: P = PolynomialRing(QQ,0,'')
sage: P
Multivariate Polynomial Ring in no variables over Rational Field
sage: t = P.random_element()
sage: t.factor()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/burcin/.sage/temp/karr/24426/_home_burcin__sage_init_sage_0.py in <module>()

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)
   1422         # try to use univariate factoring first

   1423         try:
-> 1424             F = self.univariate_polynomial().factor()
   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())
   1426         except TypeError:

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in univariate_polynomial(self, R)
   1055         #construct ring if None

   1056         if R is None:
-> 1057             R = self.base_ring()[str(self.variables()[0])]
   1058 
   1059         monomial_coefficients = self._MPolynomial_element__element.dict()

IndexError: tuple index out of range
```



---

Comment by burcin created at 2010-01-17 23:26:51

factor zero variable polynomials


---

Comment by burcin created at 2010-01-17 23:29:32

Changing status from new to needs_review.


---

Attachment

trivial review please?


---

Comment by was created at 2010-01-18 09:34:00

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-01-18 09:34:00

1. Factoring of 0 should raise an error like it does over ZZ, but doesn't right now:

```
sage: P = PolynomialRing(ZZ,0,'')
sage: P(10).factor()
10
sage: P(0).factor()
0
sage: factor(0)
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
```


2. The element 10 in the polynomial ring "ZZ[]" in 0-variables is actually *not* a unit.  So it is wrong that it is put in the "unit" slot of the factorization.   Notice how factoring 10 works:

```
sage: R.<x> = ZZ[]
sage: (10*x).factor()
2 * 5 * x
sage: list((10*x).factor())
[(2, 1), (5, 1), (x, 1)]
```

In particular, the 10 is *not* treated incorrectly as a unit.

So I think this patch needs work.


---

Attachment

only apply this patch


---

Comment by burcin created at 2010-01-18 17:53:11

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-01-18 17:53:11

Thanks for the review!

New patch addressing both points is available at attachment:trac_7950-zero_variable_factor.take2.patch. I hope it doesn't contain more stupid mistakes. :)


---

Comment by AlexGhitza created at 2010-01-23 01:12:41

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-01-23 01:12:41

Replying to [comment:3 burcin]:
> New patch addressing both points is available at attachment:trac_7950-zero_variable_factor.take2.patch. I hope it doesn't contain more stupid mistakes. :)

Not that I could find :)

Looks good to me.


---

Comment by mvngu created at 2010-01-23 09:32:29

Resolution: fixed


---

Comment by mvngu created at 2010-01-23 09:32:29

Merged [trac_7950-zero_variable_factor.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7950/trac_7950-zero_variable_factor.take2.patch).
