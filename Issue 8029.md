# Issue 8029: Defect: Power series over a polynomial ring with real coefficients

Issue created by migration from https://trac.sagemath.org/ticket/8029

Original creator: eduenez

Original creation time: 2010-01-21 18:47:19

Assignee: AlexGhitza

CC:  mjo mhansen

Keywords: polynomial ring, power series

Sage 4.3 in a PowerPC Mac:

```
sage: A.<x> = RR['x']
sage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]]
sage: 1. + O(t)
1.00000000000000 + O(t)
sage: 1. + O(t^2)
1.00000000000000 + O(t^2)
sage: 1. + O(t^3)
1.00000000000000 + O(t^3)
sage: 1. + O(t^4)

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0xffffffe4
__pyx_f_4sage_5rings_10polynomial_26polynomial_real_mpfr_dense_19PolynomialRealDense__add_ (__pyx_v_left=0x14096f8, __pyx_v__right=0x10fc6260, __pyx_skip_dispatch=0) at sage/rings/polynomial/polynomial_real_mpfr_dense.c:5360
5360    sage/rings/polynomial/polynomial_real_mpfr_dense.c: No such file or directory.
        in sage/rings/polynomial/polynomial_real_mpfr_dense.c
```


NOTE: Bug was not present in Sage v2.9.1, but was already present in v3.4 (running on 64-bit Opteron). It is _not_ triggered over QQ as basefield.


---

Attachment

Add a doctest from the description


---

Comment by mjo created at 2011-12-16 06:19:14

I don't have a PowerPC Mac, but I do have 64-bit Linux. I believe this is fixed, so I've added a doctest for it.


---

Comment by mjo created at 2011-12-16 06:19:14

Changing status from new to needs_review.


---

Comment by mhansen created at 2011-12-18 10:10:44

We should probably double-check on PowerPC.


---

Comment by fwclarke created at 2011-12-20 12:29:48

Replying to [comment:4 mhansen]:
> We should probably double-check on PowerPC.

Mac OS X 105.8, Dual 2.5 GHz PowerPC G5

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A.<x> = RR['x'] 
sage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]] 
sage: 1. + O(t) 
1.00000000000000 + O(t)
sage: 1. + O(t^2) 
1.00000000000000 + O(t^2)
sage: 1. + O(t^3) 
1.00000000000000 + O(t^3)
sage: 1. + O(t^4) 
1.00000000000000 + O(t^4)
```



---

Comment by mhansen created at 2011-12-20 12:30:56

Changing keywords from "polynomial ring, power series" to "polynomial ring, power series, sd35".


---

Comment by mhansen created at 2011-12-20 12:30:56

Nice -- I'll give this a positive review then.


---

Comment by mhansen created at 2011-12-20 12:30:56

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-12-20 14:00:46

In private communication last night, Robert Campbell wrote to me and mjo:

```
Running Sage v 4.7.2 on a PowerMac G5 running OSX 10.5.8 it seems to work.  If desired I can take the time to compile and run one of the 4.8 alphas, but that may take a few days until I can find the time.

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A.<x> = RR['x']
sage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]]
sage: 1. + O(t)
1.00000000000000 + O(t)
sage: 1. + O(t^2)
1.00000000000000 + O(t^2)
sage: 1. + O(t^3)
1.00000000000000 + O(t^3)
sage: 1. + O(t^4)
1.00000000000000 + O(t^4)
sage:
```

That's a lot of confirmation.


---

Comment by jdemeyer created at 2011-12-24 01:04:23

Resolution: fixed
