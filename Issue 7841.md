# Issue 7841: Use NTL's ZZ_pEX for polynomial arithmetic over extension fields

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-01-04 13:28:16

Assignee: AlexGhitza

The actual implementation is the generic one.


---

Comment by ylchapuy created at 2010-01-04 13:51:37

The attached patch defines a new class Polynomial_ZZ_pEX via templating (uses polynomial_template.pxi).

This class should be used for polynomials over GF(p^k) with p>NTL_SP_BOUND.
For smaller values of p, we should wrap NTL's lzz_pEX which is not done yet at all.

For the record, some comparisons:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: NTL
sage: K.<a>=GF(next_prime(2**60)**3)
sage: R.<x> = PolynomialRing(K,implementation='NTL')
sage: S.<X>=PolynomialRing(K)
sage: P=R.random_element(degree=100)
sage: Q=S(list(P))
sage: P2=R.random_element(degree=100)
sage: Q2=S(list(P2))
sage: %timeit P+P2
10000 loops, best of 3: 68.7 µs per loop
sage: %timeit Q+Q2
1000 loops, best of 3: 1.53 ms per loop
sage: %timeit P*P2
100 loops, best of 3: 2.17 ms per loop
sage: %timeit Q*Q2
10 loops, best of 3: 298 ms per loop
sage: %timeit P**30
10 loops, best of 3: 79.8 ms per loop
sage: time ll=Q**10
CPU times: user 12.71 s, sys: 0.20 s, total: 12.91 s
Wall time: 13.15 s
sage: %timeit P//(P2>>50)
100 loops, best of 3: 4.85 ms per loop
sage: %timeit Q//(Q2>>50)
10 loops, best of 3: 203 ms per loop
sage: time P.is_irreducible()
CPU times: user 1.44 s, sys: 0.00 s, total: 1.44 s
Wall time: 1.44 s
False
sage: time Q.is_irreducible()
CPU times: user 11.66 s, sys: 0.01 s, total: 11.67 s
Wall time: 11.79 s
False
```



---

Comment by ylchapuy created at 2010-01-04 13:51:54

Changing status from new to needs_review.


---

Comment by cremona created at 2010-01-05 22:51:44

I think that this is a good idea.

The patch applies fine to 4.3, and the tests in sage/libs/ntl and sage/rings/polynomial pass.

I would like someone who has more experience in cython & wrapping C++ to look at this too.  Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.  Put yourself in the position of someone else a year or two in the future trying to debug something subtle -- they will need to have all the details!

Anyway, I left it is "needs review" in the hope that someone else will take a look at the code too.


---

Comment by cremona created at 2010-01-05 22:51:44

Changing keywords from "" to "NTL polynomials".


---

Comment by ylchapuy created at 2010-01-06 21:43:23

Replying to [comment:3 cremona]:

Thanks for looking at this!

> Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.

I just lazily adapted the files for GF2X. But I admit it's not perfect.

Yann


---

Comment by cremona created at 2010-01-06 22:42:05

Replying to [comment:4 ylchapuy]:
> Replying to [comment:3 cremona]:
> 
> Thanks for looking at this!
> 
> > Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.
> 
> I just lazily adapted the files for GF2X. But I admit it's not perfect.

That makes my comments rather frustrating, I'm sure -- sorry about that.  I see that sage/libs/ntl has a good covereage score:

```
john`@`ubuntu%sage -coverage ~/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl | grep SCORE
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_mat_ZZ.pyx: 86% (31 of 36)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pEX.pyx: 97% (44 of 45)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2.pyx: 92% (13 of 14)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pContext.pyx: 66% (6 of 9)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_lzz_p.pyx: 94% (16 of 17)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_lzz_pX.pyx: 97% (36 of 37)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ.pyx: 91% (21 of 23)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2E.pyx: 95% (19 of 20)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_lzz_pContext.pyx: 83% (5 of 6)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2EContext.pyx: 85% (6 of 7)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZX.pyx: 98% (52 of 53)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2X.pyx: 94% (36 of 38)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pX.pyx: 84% (50 of 59)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pE.pyx: 42% (6 of 14)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2EX.pyx: 81% (9 of 11)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pEContext.pyx: 80% (8 of 10)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_p.pyx: 95% (19 of 20)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_mat_GF2E.pyx: 96% (25 of 26)
SCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_mat_GF2.pyx: 96% (24 of 25)
```

but that only measures which functoins have any kind of docstring, not what the docstrings contain.


---

Attachment

based on 4.3.1


---

Comment by ylchapuy created at 2010-01-27 21:56:51

The patch is updated, it now makes NTL the default implementation.
sage -testall -long without finishes without any failures.

The doc is still minimal though.


---

Attachment

( see also #8109 )


---

Comment by roed created at 2010-02-08 22:33:22

I'll review this.


---

Comment by roed created at 2010-02-09 03:06:07

Looks good.  Here are some comments.  After a few changes, I'll be happy to give this a positive review.


 * sage/libs/ntl/ntl_ZZ_pEX_linkage.pxi
  * Update the copyright to include a year and name.  You may just want to copy the header from another file and edit to change details.
  * There's a strange indentation in `celement_pow` on the `ZZ_pEX_LeftShift` line.

 * sage/rings/polynomial/polynomial_ring.py
  * `__modulus`: if you're going to access it outside the class use one underscore.  That way you don't have to use name mangling.

 * sage/rings/polynomial/polynomial_zz_pex.pyx
  * Add a copyright and short docstring at the top of the file.
  * In `__init__` documentation, `GF(2) -> GF(p^n)`
  * Use `e = K.coerce(e)` rather than `e = K._coerce_(e)`
  * `Polynomial_template.__init__` calls `Polynomial.__init__`: you shouldn't duplicate this earlier in your `__init__` function.
  * In `__getitem__`, get rid of the second return line 
  * In `__call__`, why use coerce(K,a) and not K.coerce(a)?  It seems to work, but I can't find where coerce is defined.  Also, it's generally not a good idea to catch everything.  Presumably you want to catch `TypeError`, `ValueError`, `NotImplementedError`.
  * In resultant, if you're going to coerce anyway, why use cython to enforce the type of other?  Just use `parent()` instead of `_parent`.  Again, use `self._parent.coerce(other)` not `self._parent._coerce_(other)`.
  * In `is_irreducible`, have a way to pass in the number of iterations to `ProbIrredTest`.
  * `_cmp_c_impl` should have doctests.  It's also probably better to do this by defining celement_cmp in the linkage file.


---

Comment by roed created at 2010-02-09 03:06:07

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by ylchapuy created at 2010-02-09 17:39:32

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2010-02-09 17:39:32

Replying to [comment:9 roed]:
> Looks good.  Here are some comments.  After a few changes, I'll be happy to give this a positive review.
>

Thanks a lot for looking at this. I've done almost all the requested changes, except:

>   * `Polynomial_template.__init__` calls `Polynomial.__init__`: you shouldn't duplicate this earlier in your `__init__` function.

It's not duplicated. When I call it, the method returns before calling `Polynomial_template.__init__`

>   * `_cmp_c_impl` (...) It's also probably better to do this by defining celement_cmp in the linkage file.

I know it's quite ugly, but I need to compare the elements of the finite field with the Sage implementation. I don't know how to handle this inside celement_cmp. If you have an idea, please do it and I would be happy to review your patch.

Yann


---

Comment by roed created at 2010-02-11 07:59:48

Looks good.  I think it's possible to do _cmp_c_impl within the linkage file, but don't worry about it.

All tests pass.


---

Comment by roed created at 2010-02-11 07:59:48

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:05:46

Resolution: fixed
