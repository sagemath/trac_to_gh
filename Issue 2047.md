# Issue 2047: [with patch] new fast float evaluation framework does not work with multivariate polynomials

Issue created by migration from https://trac.sagemath.org/ticket/2047

Original creator: cwitty

Original creation time: 2008-02-05 02:42:26

Assignee: jkantor

Trying to use fast float evaluation with multivariate polynomials gives error messages like:

```
    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute '_fast_float_'
```


The attached patch fixes this, so that fast float evaluation works with multivariate polynomials.


---

Attachment

Works, massively speeds things up (easily a factor of 100), and looks good.

```
sage: R.<x,y,z> = QQ[]
sage: f = (x+y+z+1)^20
sage: h = f._fast_float_()
sage: time for _ in xrange(100): k = f(1,2,3)
CPU times: user 3.81 s, sys: 0.02 s, total: 3.84 s
Wall time: 3.87
sage: time for _ in xrange(100): k = h(1,2,3)
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.05
sage: 3.84 / 0.04
96.0000000000000
```



---

Comment by malb created at 2008-02-05 11:33:09

My five cents:
 * shouldn't this be restricted to polynomials over QQ? To me it doesn't make sense to have a `_fast_float_` for polynomials over say GF(2).
 * because speed is so important, please note that using `f.dict()` is a quite slow way of getting the (coefficient,monomial) pairs.

I am not objecting this patch goes in, but maybe a follow-up patch could address these?


---

Comment by mabshoff created at 2008-02-07 05:25:42

Merged in trac-2047.patch in Sage 2.10.2.alpha0. Please open another ticket for malb's five cents ;)


---

Comment by mabshoff created at 2008-02-07 05:25:42

Resolution: fixed
