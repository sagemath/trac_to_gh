# Issue 7841: Use NTL's ZZ_pEX for polynomial arithmetic over extension fields

archive/issues_007841.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe actual implementation is the generic one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7841\n\n",
    "created_at": "2010-01-04T13:28:16Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Use NTL's ZZ_pEX for polynomial arithmetic over extension fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7841",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @aghitza

The actual implementation is the generic one.

Issue created by migration from https://trac.sagemath.org/ticket/7841





---

archive/issue_comments_067794.json:
```json
{
    "body": "The attached patch defines a new class Polynomial_ZZ_pEX via templating (uses polynomial_template.pxi).\n\nThis class should be used for polynomials over GF(p^k) with p>NTL_SP_BOUND.\nFor smaller values of p, we should wrap NTL's lzz_pEX which is not done yet at all.\n\nFor the record, some comparisons:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: NTL\nsage: K.<a>=GF(next_prime(2**60)**3)\nsage: R.<x> = PolynomialRing(K,implementation='NTL')\nsage: S.<X>=PolynomialRing(K)\nsage: P=R.random_element(degree=100)\nsage: Q=S(list(P))\nsage: P2=R.random_element(degree=100)\nsage: Q2=S(list(P2))\nsage: %timeit P+P2\n10000 loops, best of 3: 68.7 \u00b5s per loop\nsage: %timeit Q+Q2\n1000 loops, best of 3: 1.53 ms per loop\nsage: %timeit P*P2\n100 loops, best of 3: 2.17 ms per loop\nsage: %timeit Q*Q2\n10 loops, best of 3: 298 ms per loop\nsage: %timeit P**30\n10 loops, best of 3: 79.8 ms per loop\nsage: time ll=Q**10\nCPU times: user 12.71 s, sys: 0.20 s, total: 12.91 s\nWall time: 13.15 s\nsage: %timeit P//(P2>>50)\n100 loops, best of 3: 4.85 ms per loop\nsage: %timeit Q//(Q2>>50)\n10 loops, best of 3: 203 ms per loop\nsage: time P.is_irreducible()\nCPU times: user 1.44 s, sys: 0.00 s, total: 1.44 s\nWall time: 1.44 s\nFalse\nsage: time Q.is_irreducible()\nCPU times: user 11.66 s, sys: 0.01 s, total: 11.67 s\nWall time: 11.79 s\nFalse\n```\n",
    "created_at": "2010-01-04T13:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67794",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

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

archive/issue_comments_067795.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-04T13:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67795",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067796.json:
```json
{
    "body": "I think that this is a good idea.\n\nThe patch applies fine to 4.3, and the tests in sage/libs/ntl and sage/rings/polynomial pass.\n\nI would like someone who has more experience in cython & wrapping C++ to look at this too.  Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.  Put yourself in the position of someone else a year or two in the future trying to debug something subtle -- they will need to have all the details!\n\nAnyway, I left it is \"needs review\" in the hope that someone else will take a look at the code too.",
    "created_at": "2010-01-05T22:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67796",
    "user": "https://github.com/JohnCremona"
}
```

I think that this is a good idea.

The patch applies fine to 4.3, and the tests in sage/libs/ntl and sage/rings/polynomial pass.

I would like someone who has more experience in cython & wrapping C++ to look at this too.  Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.  Put yourself in the position of someone else a year or two in the future trying to debug something subtle -- they will need to have all the details!

Anyway, I left it is "needs review" in the hope that someone else will take a look at the code too.



---

archive/issue_comments_067797.json:
```json
{
    "body": "Changing keywords from \"\" to \"NTL polynomials\".",
    "created_at": "2010-01-05T22:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67797",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "NTL polynomials".



---

archive/issue_comments_067798.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n\nThanks for looking at this!\n\n> Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.\n\nI just lazily adapted the files for GF2X. But I admit it's not perfect.\n\nYann",
    "created_at": "2010-01-06T21:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67798",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Replying to [comment:3 cremona]:

Thanks for looking at this!

> Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.

I just lazily adapted the files for GF2X. But I admit it's not perfect.

Yann



---

archive/issue_comments_067799.json:
```json
{
    "body": "Replying to [comment:4 ylchapuy]:\n> Replying to [comment:3 cremona]:\n> \n> Thanks for looking at this!\n> \n> > Meanwhile, I see that most functions do not have INPUT or OUTPUT blocks (though they do mostly have EXAMPLES), and these should be added.\n> \n> I just lazily adapted the files for GF2X. But I admit it's not perfect.\n\nThat makes my comments rather frustrating, I'm sure -- sorry about that.  I see that sage/libs/ntl has a good covereage score:\n\n```\njohn@ubuntu%sage -coverage ~/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl | grep SCORE\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_mat_ZZ.pyx: 86% (31 of 36)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pEX.pyx: 97% (44 of 45)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2.pyx: 92% (13 of 14)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pContext.pyx: 66% (6 of 9)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_lzz_p.pyx: 94% (16 of 17)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_lzz_pX.pyx: 97% (36 of 37)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ.pyx: 91% (21 of 23)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2E.pyx: 95% (19 of 20)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_lzz_pContext.pyx: 83% (5 of 6)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2EContext.pyx: 85% (6 of 7)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZX.pyx: 98% (52 of 53)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2X.pyx: 94% (36 of 38)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pX.pyx: 84% (50 of 59)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pE.pyx: 42% (6 of 14)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_GF2EX.pyx: 81% (9 of 11)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_pEContext.pyx: 80% (8 of 10)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_ZZ_p.pyx: 95% (19 of 20)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_mat_GF2E.pyx: 96% (25 of 26)\nSCORE /home/john/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl/ntl_mat_GF2.pyx: 96% (24 of 25)\n```\n\nbut that only measures which functoins have any kind of docstring, not what the docstrings contain.",
    "created_at": "2010-01-06T22:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67799",
    "user": "https://github.com/JohnCremona"
}
```

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
john@ubuntu%sage -coverage ~/sage-4.3.1.alpha1/devel/sage-main/sage/libs/ntl | grep SCORE
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

archive/issue_comments_067800.json:
```json
{
    "body": "Attachment [trac7841-ZZ_pEX_poly.patch](tarball://root/attachments/some-uuid/ticket7841/trac7841-ZZ_pEX_poly.patch) by ylchapuy created at 2010-01-27 21:54:54\n\nbased on 4.3.1",
    "created_at": "2010-01-27T21:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67800",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac7841-ZZ_pEX_poly.patch](tarball://root/attachments/some-uuid/ticket7841/trac7841-ZZ_pEX_poly.patch) by ylchapuy created at 2010-01-27 21:54:54

based on 4.3.1



---

archive/issue_comments_067801.json:
```json
{
    "body": "The patch is updated, it now makes NTL the default implementation.\nsage -testall -long without finishes without any failures.\n\nThe doc is still minimal though.",
    "created_at": "2010-01-27T21:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67801",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

The patch is updated, it now makes NTL the default implementation.
sage -testall -long without finishes without any failures.

The doc is still minimal though.



---

archive/issue_comments_067802.json:
```json
{
    "body": "Attachment [trac7841-fast_eval.patch](tarball://root/attachments/some-uuid/ticket7841/trac7841-fast_eval.patch) by ylchapuy created at 2010-02-01 20:11:42\n\n( see also #8109 )",
    "created_at": "2010-02-01T20:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67802",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac7841-fast_eval.patch](tarball://root/attachments/some-uuid/ticket7841/trac7841-fast_eval.patch) by ylchapuy created at 2010-02-01 20:11:42

( see also #8109 )



---

archive/issue_comments_067803.json:
```json
{
    "body": "I'll review this.",
    "created_at": "2010-02-08T22:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67803",
    "user": "https://github.com/roed314"
}
```

I'll review this.



---

archive/issue_comments_067804.json:
```json
{
    "body": "Looks good.  Here are some comments.  After a few changes, I'll be happy to give this a positive review.\n\n\n* sage/libs/ntl/ntl_ZZ_pEX_linkage.pxi\n  * Update the copyright to include a year and name.  You may just want to copy the header from another file and edit to change details.\n  * There's a strange indentation in `celement_pow` on the `ZZ_pEX_LeftShift` line.\n\n* sage/rings/polynomial/polynomial_ring.py\n  * `__modulus`: if you're going to access it outside the class use one underscore.  That way you don't have to use name mangling.\n\n* sage/rings/polynomial/polynomial_zz_pex.pyx\n  * Add a copyright and short docstring at the top of the file.\n  * In `__init__` documentation, `GF(2) -> GF(p^n)`\n  * Use `e = K.coerce(e)` rather than `e = K._coerce_(e)`\n  * `Polynomial_template.__init__` calls `Polynomial.__init__`: you shouldn't duplicate this earlier in your `__init__` function.\n  * In `__getitem__`, get rid of the second return line \n  * In `__call__`, why use coerce(K,a) and not K.coerce(a)?  It seems to work, but I can't find where coerce is defined.  Also, it's generally not a good idea to catch everything.  Presumably you want to catch `TypeError`, `ValueError`, `NotImplementedError`.\n  * In resultant, if you're going to coerce anyway, why use cython to enforce the type of other?  Just use `parent()` instead of `_parent`.  Again, use `self._parent.coerce(other)` not `self._parent._coerce_(other)`.\n  * In `is_irreducible`, have a way to pass in the number of iterations to `ProbIrredTest`.\n  * `_cmp_c_impl` should have doctests.  It's also probably better to do this by defining celement_cmp in the linkage file.",
    "created_at": "2010-02-09T03:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67804",
    "user": "https://github.com/roed314"
}
```

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

archive/issue_comments_067805.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-09T03:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67805",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067806.json:
```json
{
    "body": "Attachment [trac7841-review.patch](tarball://root/attachments/some-uuid/ticket7841/trac7841-review.patch) by ylchapuy created at 2010-02-09 17:32:29",
    "created_at": "2010-02-09T17:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67806",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac7841-review.patch](tarball://root/attachments/some-uuid/ticket7841/trac7841-review.patch) by ylchapuy created at 2010-02-09 17:32:29



---

archive/issue_comments_067807.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-09T17:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67807",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067808.json:
```json
{
    "body": "Replying to [comment:9 roed]:\n> Looks good.  Here are some comments.  After a few changes, I'll be happy to give this a positive review.\n>\n\nThanks a lot for looking at this. I've done almost all the requested changes, except:\n\n>   * `Polynomial_template.__init__` calls `Polynomial.__init__`: you shouldn't duplicate this earlier in your `__init__` function.\n\nIt's not duplicated. When I call it, the method returns before calling `Polynomial_template.__init__`\n\n>   * `_cmp_c_impl` (...) It's also probably better to do this by defining celement_cmp in the linkage file.\n\nI know it's quite ugly, but I need to compare the elements of the finite field with the Sage implementation. I don't know how to handle this inside celement_cmp. If you have an idea, please do it and I would be happy to review your patch.\n\nYann",
    "created_at": "2010-02-09T17:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67808",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

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

archive/issue_comments_067809.json:
```json
{
    "body": "Looks good.  I think it's possible to do _cmp_c_impl within the linkage file, but don't worry about it.\n\nAll tests pass.",
    "created_at": "2010-02-11T07:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67809",
    "user": "https://github.com/roed314"
}
```

Looks good.  I think it's possible to do _cmp_c_impl within the linkage file, but don't worry about it.

All tests pass.



---

archive/issue_comments_067810.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T07:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67810",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067811.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7841#issuecomment-67811",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
