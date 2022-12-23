# Issue 3678: Fractional powers for polynomial variables bug

Issue created by migration from https://trac.sagemath.org/ticket/3678

Original creator: wdj

Original creation time: 2008-07-19 06:00:37

Assignee: tbd

This was reported by Andrey Novoseltsev:


```
sage: pr = PolynomialRing(QQ, "u,v")
sage: pr.injvar()
Defining u, v
sage: u^(1/2)
1
sage: pr = PolynomialRing(QQ, "w")
sage: pr.injvar()
Defining w
sage: w^(1/2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)

/home/novoselt/<ipython console> in <module>()

/home/novoselt/polynomial_element.pyx in
sage.rings.polynomial.polynomial_element.Polynomial.__pow__ (sage/
rings/polynomial/polynomial_element.c:8179)()

/home/novoselt/element.pyx in
sage.structure.element.RingElement.__mul__ (sage/structure/element.c:
8814)()

/home/novoselt/coerce.pyx in
sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/
structure/coerce.c:5582)()

TypeError: unsupported operand parent(s) for '*': '<type 'list'>' and
'Rational Field'
sage: sqrt(w)
sqrt(w)
```



---

Comment by AlexGhitza created at 2008-12-21 05:29:00

The attached patch fixes this by introducing the same type-check as in the univariate polynomial case.


---

Attachment


---

Comment by cremona created at 2008-12-21 17:58:25

Positive review.  Patch applies cleanly to 3.2.2 and tests in sage/rings/polynomial pass.


---

Comment by mabshoff created at 2008-12-21 22:39:38

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 22:39:38

Merged in Sage 3.2.3.alpha0
