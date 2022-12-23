# Issue 1541: [with patch] improve PolyBoRi integration

Issue created by migration from https://trac.sagemath.org/ticket/1541

Original creator: malb

Original creation time: 2007-12-16 21:38:51

Assignee: malb

CC:  burcin

The attached patch provides:
 * `mq.SR` can now construct PolyBoRi polynomial systems 
 * some comments added to `pbori.pyx`
 * `BooleanPolynomial.__hash__`
 * `BooleanPolynomial.variables`
 * coercion of GF(2) elements to `BooleanPolynomialRing`
 * `BooleanPolynomialRing.__call__` accepts strings
 * `_sig_on`/`_sig_off` around `groebner_basis` call


---

Comment by rlm created at 2007-12-21 22:24:08

On sage.math, applied to alpha2:

```
sage -t  devel/sage-main/sage/crypto/mq/sr.py               sh: line 1: 31648 Segmentation fault      /home/rlmill/release/sage-2.9.1.alpha3/local/bin/python .doctest_sr.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
```



---

Comment by rlm created at 2007-12-21 23:20:58

results of 
`./sage -t -valgrind devel/sage-main/sage/crypto/mq/sr.py`
are at
http://sage.math.washington.edu/home/rlmill/.sage/sage-memcheck.850


---

Comment by rlm created at 2007-12-22 00:50:54

Disregard those valgrind results- they are useless.


---

Comment by malb created at 2007-12-25 15:57:10

I think the negative review has been resolved, and the currRing patch attached to this ticket should be applied (given a positive review) soon.


---

Comment by burcin created at 2007-12-27 13:45:33

Make the methods of BooleanPolynomial in __getattr__ directly available.


---

Attachment

Following Martin's comments on the slowdown caused by using `__getattr__` in `BooleanPolynomial`, attached patch with file name `polybori_booleanpolynomial_getattr.patch` makes the methods directly available.

Some timings (using random polynomials in each case might not be a good idea, but it still demonstrates the point):

Without the patch:


```
sage: P = BooleanPolynomialRing(100,'x')
sage: from polybori.randompoly import gen_random_poly
sage: p = gen_random_poly(int(100))
sage: %timeit s = p.set()
100000 loops, best of 3: 2.85 µs per loop
sage: %timeit d = p.deg()
100000 loops, best of 3: 2.26 µs per loop
sage: %timeit m = p.lead()
100000 loops, best of 3: 6.7 µs per loop
sage: %timeit n = p.navigation()
100000 loops, best of 3: 2.82 µs per loop
sage: %timeit c = p.constant()
100000 loops, best of 3: 2.02 µs per loop
```


With the patch:


```
sage: %timeit s = p.set()
1000000 loops, best of 3: 540 ns per loop
sage: %timeit d = p.deg()
1000000 loops, best of 3: 382 ns per loop
sage: %timeit m = p.lead()
100000 loops, best of 3: 3.76 µs per loop
sage: %timeit n = p.navigation()
1000000 loops, best of 3: 453 ns per loop
sage: %timeit c = p.constant()
1000000 loops, best of 3: 305 ns per loop
```



---

Comment by burcin created at 2007-12-30 16:09:04

attachment:polybori-coercion.patch provides coercion enhancements and small fixes to `pbori.pyx`. It should be applied after attachment:polybori_booleanpolynomial_getattr.patch.

This patch adds coercion from `ZZ`, and `GF(2)` to `BooleanPolynomialRing`, so Martin's patch needs to be revised.


---

Comment by burcin created at 2008-01-03 15:05:13

attachment:polybori-coercion.patch is now ticket #1667.


---

Comment by malb created at 2008-01-06 13:20:37

Replying to [comment:6 burcin]:
> This patch adds coercion from `ZZ`, and `GF(2)` to `BooleanPolynomialRing`, so Martin's patch needs to be revised.

In the sense that the comments are outdated?


---

Comment by malb created at 2008-01-06 13:23:50

The `currRing.patch` is now #1701 because it doesn't logically belong here.


---

Comment by malb created at 2008-01-07 15:40:09

Deleted original patch, just use burcin's getattr patch.


---

Comment by mabshoff created at 2008-01-07 17:11:14

Resolution: fixed


---

Comment by mabshoff created at 2008-01-07 17:11:14

Merged in Sage 2.10.alpha0. 

Caution: when patching the offset was very large: `Hunk #1 succeeded at 1372 (offset 284 lines).` I did verify that indeed the section was moved that far down in the current sources.  

Cheers,

Michael
