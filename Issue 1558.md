# Issue 1558: [with patch] more NTL wrapping, coefficient access and factoring

Issue created by migration from https://trac.sagemath.org/ticket/1558

Original creator: jbmohler

Original creation time: 2007-12-18 16:26:15

Assignee: somebody

The attached patch provides some more lines in ntl/decl.pxi to give direct access to some more of NTL.  The are two main functionality improvements:

1) !__getitem!__ now has one less copy of the coefficient.  This results in a noticable speed improvement for coefficients (and !__hash!__)

2) New _factor_ntl and _factor_pari in sage/rings/polynomial/polynomial_integer_dense_ntl.pyx enable us to have more fun with head-to-head comparisons of their factoring routines.  It really seems a mixed bag about who is faster.  I have a basic check in place that keeps the factoring all in NTL for small coefficients, but this really isn't the end of the story as far as the benchmarking goes.


```
# original
sage: R.<x>=ZZ[]
sage: f=x^2-1
sage: timeit f.factor()
1000 loops, best of 3: 784 µs per loop
```



```
# patched
sage: R.<x>=ZZ[]
sage: f=x^2-1
sage: timeit f.factor()
10000 loops, best of 3: 153 µs per loop
```



---

Attachment

a patch with better decision process for pari or ntl


---

Comment by mhansen created at 2007-12-22 23:11:04

The patch applies, builds, and passes tests for me.


---

Comment by rlm created at 2007-12-23 07:08:24

merged in 2.9.1 rc2


---

Comment by rlm created at 2007-12-23 07:08:24

Resolution: fixed
