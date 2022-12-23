# Issue 8428: Problem with rational_points over plane curves

Issue created by migration from https://trac.sagemath.org/ticket/8428

Original creator: cturner

Original creation time: 2010-03-03 10:51:06

Assignee: AlexGhitza

CC:  cremona

The newly "improved" rational_points function for plane curves (#8193) has a bug; if for some (Y,Z) the polynomial defining the curve becomes identically 0, it returns a ValueError caused by the function trying to factorise 0 as a polynomial.

Here is an example


```
sage: F = GF(2)
sage: P2.<X,Y,Z> = ProjectiveSpace(F,2)
sage: C = Curve(X*Y)
sage: a = C.rational_points_iterator()
sage: a.next()
(1 : 0 : 0)
sage: a.next()
(0 : 1 : 0)
sage: a.next()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/charlie/<ipython console> in <module>()

/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/schemes/plane_curves/projective_curve.pyc
in rational_points_iterator(self)
   353         # points with Z = 1
   354         for y in K:
--> 355             for x in R(g(X,y,one)).roots(multiplicities=False):
   356                 yield(self.point([x,y,one]))
   357

/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so
in sage.rings.polynomial.polynomial_element.Polynomial.roots
(sage/rings/polynomial/polynomial_element.c:30111)()

/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so
in sage.rings.polynomial.polynomial_element.Polynomial.factor
(sage/rings/polynomial/polynomial_element.c:18463)()
ValueError: factorization of 0 not defined
```


A patch to improve this is on its way.


---

Comment by cturner created at 2010-03-04 10:25:44

Applies to 4.3.3


---

Attachment

Applies to 4.3.3


---

Comment by cturner created at 2010-03-04 10:27:11

Changing status from new to needs_review.


---

Attachment


---

Comment by cturner created at 2010-03-04 10:29:52

Apologies; both copies of the patch are the same, I double-clicked and am unable to remove the 2nd copy.


---

Comment by cturner created at 2010-03-04 10:29:52

Changing assignee from AlexGhitza to cturner.


---

Comment by cturner created at 2010-03-04 10:31:13

Changing assignee from cturner to AlexGhitza.


---

Comment by roed created at 2010-03-13 02:04:15

Fixes the bug, doctested and doctests pass.  Positive review.


---

Comment by roed created at 2010-03-13 02:04:15

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:51:33

Merged "trac_8428_rational_points_iterator.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:51:33

Resolution: fixed
