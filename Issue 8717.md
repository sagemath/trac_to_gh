# Issue 8717: Precision problem in E2 for Tate Curve

Issue created by migration from https://trac.sagemath.org/ticket/8717

Original creator: roed

Original creation time: 2010-04-19 18:28:37

Assignee: AlexGhitza


```
sage: T = EllipticCurve('14').tate_curve(7)
sage: T.E2(30)
2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + O(7^20)
sage: T.E2(30)
2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + 2*7^20 + 7^21 + 5*7^22 + 4*7^23 + 4*7^24 + 3*7^25 + 6*7^26 + 3*7^27 + 6*7^28 + O(7^30)
```



---

Attachment


---

Comment by roed created at 2010-04-19 18:29:21

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-05-18 13:40:20

Looks good to me.


---

Comment by AlexGhitza created at 2010-05-18 13:40:20

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 08:22:02

Resolution: fixed
