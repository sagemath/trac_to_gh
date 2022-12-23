# Issue 8865: FractionFieldElement.__call__ doesn't handle keyword arguments

Issue created by migration from https://trac.sagemath.org/ticket/8865

Original creator: mguaypaq

Original creation time: 2010-05-03 22:35:47

Assignee: AlexGhitza

Keywords: FractionField, subs

PolynomialRing elements allow keyword arguments when substitute values for the variables (via !__call!__), but the corresponding method in FractionFieldElement doesn't handle keyword arguments properly.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x = PolynomialRing(RationalField(),'x',3).gens()
sage: f = x[0] + x[1] - 2*x[1]*x[2]
sage: h = f /(x[1] + x[2])
sage: h
(-2*x1*x2 + x0 + x1)/(x1 + x2)
sage: h(1,2,5)
-17/7
sage: h(x0=1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
/home/mguaypaq/sage/<ipython console> in <module>()

TypeError: __call__() got an unexpected keyword argument 'x0'
```



---

Attachment


---

Comment by mguaypaq created at 2010-05-04 12:29:12

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-05-04 14:27:46

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-05-04 14:27:46

Looks good to me.


---

Comment by mvngu created at 2010-05-08 21:35:17

Resolution: fixed
