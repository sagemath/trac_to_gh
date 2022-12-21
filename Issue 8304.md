# Issue 8304: Remove stray factors of 2 in Coleman integration

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2010-02-19 02:56:02

Assignee: was

CC:  jen robertwb

Keywords: Coleman integration, hyperelliptic curves

Jen discovered some stray factors of 2 buried in the Coleman integration code. (Apply patches at #7927 before trying these examples.)

On one hand, the invariant differential sometimes thinks it's dx/2y (as it should):

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3+1)
sage: K = Qp(5,8)
sage: HK = H.change_ring(K)
sage: w = HK.invariant_differential()
sage: P = HK(0,1)
sage: Q = HK.lift_x(5)
sage: x,y = HK.monsky_washnitzer_gens()
sage: (2*y*w).coleman_integral(P,Q)
5 + O(5^9)
```

but on the other hand, it sometimes behaves as if it were dx/y (as it shouldn't):

```
sage: x,y,z = HK.local_analytic_interpolation(P,Q)
sage: I1 = (x.derivative()/y).integral()
sage: I2 = (x.derivative()/(2*y)).integral()
sage: I1(1)-I1(0)
5 + 3*5^4 + 3*5^6 + 3*5^7 + O(5^9)
sage: I2(1)-I2(0)
3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
sage: HK.coleman_integral(w,P,Q)
5 + 3*5^4 + 3*5^6 + 3*5^7 + O(5^9)
```

The apparent fix is to insert an extra division by two in tiny_integrals (which then needs a corrected docstring and some doctests, and similarly for tiny_integrals_on_basis) and then remove the multiplication by 2 in coleman_integrals_on_basis. Then correct all the doctests which currently give answers which are off by a factor of 2.


---

Comment by jen created at 2010-02-19 20:38:50

Changing status from new to needs_review.


---

Attachment

The attached patch should fix these issues (+doctests), so that invariant differential always behaves as dx/2y:


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3+1)
sage: K = Qp(5,8)
sage: HK = H.change_ring(K)
sage: w = HK.invariant_differential()
sage: P = HK(0,1)
sage: Q = HK.lift_x(5)
sage: x,y = HK.monsky_washnitzer_gens()
sage: (2*y*w).coleman_integral(P,Q)
5 + O(5^9)
sage: x,y,z = HK.local_analytic_interpolation(P,Q)
sage: I2 = (x.derivative()/(2*y)).integral()
sage: I2(1)-I2(0)
3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
sage: HK.coleman_integral(w,P,Q)
3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
```



---

Attachment

added doctests for tiny_integrals


---

Comment by kedlaya created at 2010-02-20 14:53:07

Changing status from needs_review to positive_review.


---

Comment by kedlaya created at 2010-02-20 14:53:07

Looks good, passes long doctests in sage/schemes/ (after applying patches at #7927). Positive review.


---

Comment by mvngu created at 2010-03-03 15:02:11

Merged in this order:

 1. [13542.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8304/13542.patch)
 1. [13543.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8304/13543.patch)


---

Comment by mvngu created at 2010-03-03 15:02:11

Resolution: fixed
