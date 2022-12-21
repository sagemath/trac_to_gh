# Issue 9302: Heegner point_exact is wrong for 5077a with discriminant -7

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-22 00:28:56

Assignee: cremona


```
sage: E = EllipticCurve('5077a')
sage: E.heegner_discriminants(100)
[-3, -4, -7, -19, -40, -47, -55, -59, -71, -79, -84, -88]
sage: P = E.heegner_point(-7)
sage: P.numerical_approx(prec=100)
(0 : 1.0000000000000000000000000000 : 0)
sage: P.point_exact(prec=100)
(0 : 2 : 1)
```


But point_exact should be the point at infinity. 


---

Attachment


---

Comment by robertwb created at 2010-06-23 04:01:50

Changing status from new to needs_review.


---

Comment by was created at 2010-06-23 04:05:55

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:13:19

Resolution: fixed
