# Issue 3617: LarentPolynomial.__call__ is broken for Laurent polynomial's that have negative exponents

Issue created by migration from https://trac.sagemath.org/ticket/3617

Original creator: mhansen

Original creation time: 2008-07-08 21:35:22

Assignee: malb


```
sage: P.<q> = LaurentPolynomialRing(QQ)
sage: qi = q^(-1)
sage: qi in P
False
sage: q in P
True
sage: P(qi)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mike/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/laurent_polynomial_ring.py in __call__(self, x)
    679             sage: L(1/2)
    680             1/2
    681         """
--> 682         return LaurentPolynomial_mpair(self, x)
    683     

/home/mike/laurent_polynomial.pyx in sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair.__init__ (sage/rings/polynomial/laurent_polynomial.c:1889)()

/home/mike/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:5984)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    216             return x
    217 
--> 218         return sage.rings.rational.Rational(x, base)
    219         
    220     def construction(self):

/home/mike/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3321)()

/home/mike/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4494)()

TypeError: Unable to coerce q^-1 (<type 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'>) to Rational
```



---

Comment by mhansen created at 2010-01-19 22:56:19

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-01-19 22:58:12

This also fixes #5468.


---

Attachment


---

Comment by spancratz created at 2010-01-20 06:09:50

Changing status from needs_review to positive_review.


---

Comment by spancratz created at 2010-01-20 06:09:50

This seems fine to me, and applies and passes all doctests on 4.3.

Sebastian


---

Comment by mvngu created at 2010-01-23 08:13:13

Resolution: fixed
