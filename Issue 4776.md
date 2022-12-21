# Issue 4776: random element of multivariate polynomial ring in one variable is totally broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-13 02:07:22

Assignee: malb


```
sage: R.<x> = PolynomialRing(Integers(3), 1)
sage: R.random_element()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/sage/build/sage-3.2.2.alpha0/devel/sage-main/sage/rings/<ipython console> in <module>()

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring_generic.so in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.random_element (sage/rings/polynomial/multi_polynomial_ring_generic.c:7404)()

TypeError: Cannot compute polynomial with more terms than exist.
```



---

Attachment


---

Comment by AlexGhitza created at 2008-12-20 17:01:05

Looks good to me.


---

Comment by mabshoff created at 2008-12-21 12:37:08

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 12:37:08

Merged in Sage 3.2.3.alpha0
