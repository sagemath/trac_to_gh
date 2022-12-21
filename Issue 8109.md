# Issue 8109: wrap NTL's lzz_pE and lzz_pEX and use them

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-01-28 08:02:42

Assignee: AlexGhitza

This should fasten polynomial arithmetic over finite fields of small characteristic.


---

Attachment

needs #7841 (I guess)


---

Comment by ylchapuy created at 2010-01-29 23:31:59

Changing keywords from "" to "ntl".


---

Comment by ylchapuy created at 2010-01-29 23:31:59

Preliminary version.

note: this is mostly a copy of existing files for wrapping ZZ_pE and ZZ_pEX with
'sed s/ZZ/zz/g' applied.

warning: there is no test (yet) for checking that the modulus is < NTL_SP_BOUND

still, doctests pass and here are some results:

```
sage: c=ntl.zz_pEContext(ntl.zz_pX([1,1,1,1,1], 19800713)) 
sage: a = ntl.zz_pE([3,2], c); b = ntl.zz_pE([1,2], c)
sage: f = ntl.zz_pEX([a, b, b])
sage: p = f**123
sage: q = p+f**77+f
sage: 
sage: C=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1,1,1], 19800713)) 
sage: A = ntl.ZZ_pE([3,2], C); B = ntl.ZZ_pE([1,2], C)
sage: F = ntl.ZZ_pEX([A, B, B])
sage: P = F**123
sage: Q = P+F**77+F
sage: 
sage: %timeit p+q
625 loops, best of 3: 59.6 µs per loop
sage: %timeit P+Q
625 loops, best of 3: 180 µs per loop
sage: 
sage: %timeit p*q
125 loops, best of 3: 2.62 ms per loop
sage: %timeit P*Q
125 loops, best of 3: 5.65 ms per loop
sage: 
sage: %timeit p.gcd(q)
125 loops, best of 3: 7.28 ms per loop
sage: %timeit P.gcd(Q)
5 loops, best of 3: 62.5 ms per loop
sage: 
sage: %timeit p**17
5 loops, best of 3: 58 ms per loop
sage: %timeit P**17
5 loops, best of 3: 129 ms per loop
```



---

Comment by ylchapuy created at 2010-01-29 23:42:53

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-01-29 23:42:53

Replying to [comment:1 ylchapuy]:

> warning: there is no test (yet) for checking that the modulus is < NTL_SP_BOUND

I must be tired... there is a check, it's done in the lzz_p class.

I guess this one is ready for review then. I will open another ticket to do the same as #7841 latter.


---

Comment by ylchapuy created at 2010-02-01 19:47:05

use both patches


---

Attachment

Finally, this is such a small patch that I add it here.
With both patches applied, the default implementation for polynomial ring is now based on NTL, and uses type ZZ or lzz depending on the characteristic (tested against NTL_SP_BOUND).


---

Comment by roed created at 2010-02-08 22:32:47

I'll review this.  I'm working on multiple related things actually: improving finite fields (which I'm thinking of doing with a new templating class) and p-adic polynomials.


---

Comment by ylchapuy created at 2010-02-09 17:40:07

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-02-09 22:49:30

I see that you changed it to "needs work."  One thing I noticed looking at the patch was that sage/libs/ntl/ntl_lzz_decl.pxd seems generally broken: shouldn't those be zz_p and lzz_p, not zz and lzz?


---

Attachment


---

Comment by ylchapuy created at 2010-02-10 18:38:32

replacing all previous ones


---

Attachment

Replying to [comment:6 roed]:
> I see that you changed it to "needs work."  One thing I noticed looking at the patch was that sage/libs/ntl/ntl_lzz_decl.pxd seems generally broken: shouldn't those be zz_p and lzz_p, not zz and lzz?

It's even worse than that, this file just shouldn't exist :)
The last patch replaces all previous ones and should be almost ready for review. I will just check and address the comments made on #7841 before.


---

Attachment


---

Comment by ylchapuy created at 2010-03-10 11:45:32

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2010-03-10 11:45:32

Apply only:

 * trac_8109-lzz_pEX-all_in_one.patch
 * trac_8109-lzz_pEX-copyrights.patch

in this order.


---

Comment by malb created at 2010-04-14 10:48:04

I get doctest failures on sage.math:


```
sage -t  devel/sage/sage/graphs/graph_list.py # 0 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py # Killed/crashed
sage -t  devel/sage/sage/libs/ntl/ntl_lzz_pX.pyx # 5 doctests failed
sage -t  devel/sage/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi # 3 doctests failed
```


Looks like a 64-bit thing?


```
sage -t  devel/sage/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi", line 178:
    sage: (1+a+a^2)*x - (1+x+x^2)
Expected:
    1152921504606847008*x^2 + (a^2 + a)*x + 1152921504606847008
Got:
    1030*x^2 + (a^2 + a)*x + 1030
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi", line 189:
    sage: -x
Expected:
    1152921504606847008*x
Got:
    1030*x
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi", line 308:
    sage: (a+1+x).xgcd(a+x)
Expected:
    (1, 1, 1152921504606847008)
Got:
    (1, 1, 1030)
**********************************************************************
```



---

Comment by malb created at 2010-04-14 10:48:04

Changing status from needs_review to needs_work.


---

Comment by johanbosman created at 2011-08-19 12:05:13

The patch needs to be rebased as well.
