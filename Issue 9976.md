# Issue 9976: Implement complex multiplication for points of CM elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/9977

Original creator: davidloeffler

Original creation time: 2010-09-23 12:11:05

Assignee: cremona

CC:  jdemeyer cremona lorenz

Keywords: CM

It would be great if we could do

```
sage: E = EllipticCurve([0,0,0,3,0]) # curve with CM by Q[I]
sage: (1 + I) * P([1,2])
```

This wouldn't be very hard for CM elliptic curves over QQ, since the necessary functionality is there in PARI's `ellpow`; see #6327. CM elliptic curves over number fields might be a bit harder. 


---

Comment by cremona created at 2010-09-23 16:29:38

Agreed!  See also #7368.


---

Comment by jdemeyer created at 2010-09-23 16:30:58

If we can do Q, then we can do number fields simply by adapting the PARI code.  I already have the proof-of-concept code for this.

I have an important mathematical question though: given an elliptic curve E, how can we see whether it has CM and if yes, for which discriminant?


---

Comment by jdemeyer created at 2010-09-23 16:41:56

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2010-09-23 16:41:56

Changing keywords from "CM" to "CM elliptic curve".


---

Comment by chapoton created at 2013-09-21 12:18:55

There are now methods `has_cm` and `cm_discriminant` available.


---

Comment by cremona created at 2013-09-21 14:16:45

The new code for isogenies should make it easy to implement endomorphisms for CM curves.  Then this sort of thing would be easy.  So I would say that the next step should be to implement endomorphism rings, as structures which know they are rings and also know how to act on points.


---

Comment by cremona created at 2018-04-13 09:02:14

Note that although some elliptic curves defined over Q are CM curves, the additional endomorphisms are not themselves defined over Q.  One needs to distinguish, for an elliptic curve E defined over a field k,  between End_k(E) (the ring of endomorphisms defined over k itself) and End(E) (the possibly larger ring of endomorphisms defined over an algebraic closure).  In the case where char(k)=0 and E has CM by the order of discriminant D<0, the endomorphisms are defined over k(sqrt(D)) which may be a quadratic extension of k.  This is always the case when k=Q.

In the original example, (1+I)*P will not be a rational point on the original curve.
