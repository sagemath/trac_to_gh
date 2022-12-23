# Issue 2352: univariate homogenize is not the same as multivariate homogenize

Issue created by migration from https://trac.sagemath.org/ticket/2352

Original creator: ncalexan

Original creation time: 2008-02-29 08:24:09

Assignee: malb

CC:  ncalexan

Keywords: univariate polynomial homogenize

Ticket #2349 fixes the multivariate case.  This ticket is for the univariate case.  Some examples (these work after like this AFTER #2349 has been applied):


```
sage: x = Zmod(3)['x'].0; (x^2 + x).homogenize()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'
sage: x = PolynomialRing(Zmod(3), 1, 'x').0; (x^2 + x).homogenize()
x^2 + x*h
sage: x = GF(3)['x'].0; (x^2 + x).homogenize()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'
sage: x = PolynomialRing(GF(3), 1, 'x').0; (x^2 + x).homogenize()
x^2 + x*h
```



---

Comment by malb created at 2008-09-20 15:55:44

Changing status from new to assigned.


---

Comment by lftabera created at 2014-07-24 14:40:43

One step more to unify some methods of univariate and multivariate polynomials.
----
New commits:


---

Comment by lftabera created at 2014-07-24 14:40:43

Changing status from new to needs_review.


---

Comment by saraedum created at 2014-07-28 22:33:37

Should `(1+t).homogenize('t')` really be zero? The docstring says that setting this variable to one yields the original polynomial which does not seem to be the case. So should we clarify (also in the multivariate case) that strange things may happen if `var` is a variable which appears in the polynomial?


---

Comment by saraedum created at 2014-07-28 22:33:43

Changing status from needs_review to needs_info.


---

Comment by saraedum created at 2014-07-28 23:29:16

Changing status from needs_info to needs_review.


---

Comment by saraedum created at 2014-07-28 23:30:11

I tried to clarify the behaviour in the docstrings. I hope you do not mind my changes.
----
New commits:


---

Comment by lftabera created at 2014-07-29 09:08:43

Thanks, the documentation has improved, much clearer now.


---

Comment by lftabera created at 2014-07-29 09:08:43

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-07-29 21:39:08

Resolution: fixed
