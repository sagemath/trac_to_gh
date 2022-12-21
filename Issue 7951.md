# Issue 7951: coercion problem with 0 variable polynomials

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-01-16 17:56:27

Assignee: AlexGhitza

CC:  malb


```
sage: R.<x,y> = QQ[]
sage: P = PolynomialRing(QQ,0,'')
sage: P
Multivariate Polynomial Ring in no variables over Rational Field
sage: t = P.random_element()
sage: t
-1
sage: t*x
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/burcin/.sage/temp/karr/24426/_home_burcin__sage_init_sage_0.py in <module>()

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10153)()

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6988)()

TypeError: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in no variables over Rational Field' and 'Multivariate Polynomial Ring in x, y over Rational Field'



---

Attachment


---

Comment by burcin created at 2010-01-17 22:54:04

Changing status from new to needs_review.


---

Comment by burcin created at 2010-01-17 22:54:04

Here is the cause:


```
sage: P = PolynomialRing(QQ,0,'')
sage: P('pi')
pi
sage: type(P('pi'))
<type 'sage.symbolic.expression.Expression'>
```


attachment:trac_7951-zero_variable_poly_coercion.patch has the fix.


---

Comment by robertwb created at 2010-01-20 09:24:31

Doesn't apply cleanly to 4.3.1, maybe I don't have a new enough alpha?


---

Comment by robertwb created at 2010-01-20 09:24:41

But the code looks good.


---

Comment by burcin created at 2010-01-20 20:01:52

It applies without problems to 4.3.1.rc1 for me.


---

Comment by AlexGhitza created at 2010-01-23 00:36:21

Applies cleanly for me on 4.3.1, passes tests, looks good.


---

Comment by AlexGhitza created at 2010-01-23 00:36:21

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 06:37:21

Resolution: fixed
