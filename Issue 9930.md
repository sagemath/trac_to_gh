# Issue 9930: Implement conversion from EllipticCurvePoint to PARI

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-09-17 09:50:24

Assignee: cremona

Keywords: elliptic curve point pari

Currently, points on elliptic curves cannot automatically be converted to PARI:


```
sage: E = EllipticCurve([0,0,0,3,0])
sage: P = E.point([1,2]); P
(1 : 2 : 1)
sage: pari(P)
Traceback (most recent call last):
...
RuntimeError: evaluating PARI string
```



---

Comment by jdemeyer created at 2010-09-19 12:18:04

Changing status from new to needs_review.


---

Attachment


---

Comment by jdemeyer created at 2010-09-19 14:07:07

Note that the patch removes `_pari_` for elliptic curves over p-adic and finite fields.  This is justified because the general case covers these special cases (and doctests have been copied to check that).


---

Comment by davidloeffler created at 2010-09-23 11:53:32

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-23 11:53:32

Looks fine to me.


---

Comment by mpatel created at 2010-09-29 04:24:46

Resolution: fixed
