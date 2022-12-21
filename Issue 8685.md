# Issue 8685: evaluation of Monsky-Washnitzer objects

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2010-04-14 06:20:29

Assignee: was

CC:  robertwb kedlaya roed jpflori

The following should raise an error since f0 has a singularity at P  (and isn't necessarily 0 at all finite Weierstrass points):

```
sage: R.<x> = QQ['x']
sage: H= HyperellipticCurve(x^3-10*x+9)
sage: K = Qp(5,10)
sage: HK = H.change_ring(K)
sage: P = HK(1,0)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: Mfrob,forms=mw.matrix_of_frobenius_hyperelliptic(HK)
sage: f0 = forms[0]
sage: f0(P[0],P[1])
0
sage: f0(x,K(0))
0

```

In fact, Sage seems to knows this...just not when the y-coordinate is 0 in the p-adic field. So, a coercion error?

```
sage: f0(x,0)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

ZeroDivisionError: Rational division by zero
```




---

Comment by kedlaya created at 2010-04-15 20:27:45

This appears to be a problem with (surprise) power series over p-adic fields:

```
sage: R.<y> = LaurentSeriesRing(Rationals())
sage: K = Qp(5, 10)
sage: u = y^(-1)
sage: u(K(0)) ## Should blow up but doesn't
0
sage: u(0) ## Should blow up and does
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

ZeroDivisionError: Rational division by zero
```



---

Comment by kedlaya created at 2016-03-23 22:40:52

I just tried the test cases and (modulo the fact that monsky_washnitzer moved to hyperelliptic_curves) they no longer return the claimed errors. Probably this is due to some bug in p-adic power series getting fixed (perhaps #9457).

In light of that, I propose to resolve this ticket as "fixed".


---

Comment by roed created at 2016-03-24 20:50:36

Changing status from new to needs_review.


---

Comment by roed created at 2016-03-24 20:51:20

Changing status from needs_review to positive_review.


---

Comment by roed created at 2016-03-24 20:51:20

Works for me.


---

Comment by vbraun created at 2016-03-26 12:02:11

Resolution: worksforme


---

Comment by jen created at 2016-03-26 12:47:16

Changing keywords from "" to "days71".
