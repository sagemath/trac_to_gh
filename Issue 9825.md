# Issue 9825: Memory corruption in polynomial complex_roots() method

archive/issues_009825.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mjo\n\nKeywords: complex root, polynomial, finite field\n\nObviously the following code should raise an error (which is correctly given at the end), but it shouldn't be trying to `free()` non-aligned pointers.\n\n```\nsage: k.<a> = GF(7^3)\nsage: P.<x> = PolynomialRing(k)\nsage: P.random_element().complex_roots()\npython(29941) malloc: *** error for object 0x5a45c: Non-aligned pointer being freed\n*** set a breakpoint in malloc_error_break to debug\npython(29941) malloc: *** error for object 0x2fffc: Non-aligned pointer being freed\n*** set a breakpoint in malloc_error_break to debug\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/hlaw/<ipython console> in <module>()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.complex_roots (sage/rings/polynomial/polynomial_element.c:32235)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:31226)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.change_ring (sage/rings/polynomial/polynomial_element.c:16456)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)\n    311                 x = x.Polrev()\n    312 \n--> 313         return C(self, x, check, is_gen, construct=construct, **kwds)\n    314 \n    315     def is_integral_domain(self, proof = True):\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_real_mpfr_dense.so in sage.rings.polynomial.polynomial_real_mpfr_dense.PolynomialRealDense.__init__ (sage/rings/polynomial/polynomial_real_mpfr_dense.c:3609)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealField_class._element_constructor_ (sage/rings/real_mpfr.c:5058)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8767)()\n\nTypeError: Unable to convert x (='2*a^2+6*a+6') to real number.\n```\n\nIf you run the code `P.random_element().complex_roots()` a few more times, you get a segfault:\n\n```\nsage: P.random_element().complex_roots()\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\nEnvironment: Sage 4.5.2 on Mac OS X 10.5.8 (32 bit).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9826\n\n",
    "created_at": "2010-08-27T22:58:22Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "Memory corruption in polynomial complex_roots() method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9825",
    "user": "hlaw"
}
```
Assignee: somebody

CC:  mjo

Keywords: complex root, polynomial, finite field

Obviously the following code should raise an error (which is correctly given at the end), but it shouldn't be trying to `free()` non-aligned pointers.

```
sage: k.<a> = GF(7^3)
sage: P.<x> = PolynomialRing(k)
sage: P.random_element().complex_roots()
python(29941) malloc: *** error for object 0x5a45c: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(29941) malloc: *** error for object 0x2fffc: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/hlaw/<ipython console> in <module>()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.complex_roots (sage/rings/polynomial/polynomial_element.c:32235)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:31226)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.change_ring (sage/rings/polynomial/polynomial_element.c:16456)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    311                 x = x.Polrev()
    312 
--> 313         return C(self, x, check, is_gen, construct=construct, **kwds)
    314 
    315     def is_integral_domain(self, proof = True):

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_real_mpfr_dense.so in sage.rings.polynomial.polynomial_real_mpfr_dense.PolynomialRealDense.__init__ (sage/rings/polynomial/polynomial_real_mpfr_dense.c:3609)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealField_class._element_constructor_ (sage/rings/real_mpfr.c:5058)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:8767)()

TypeError: Unable to convert x (='2*a^2+6*a+6') to real number.
```

If you run the code `P.random_element().complex_roots()` a few more times, you get a segfault:

```
sage: P.random_element().complex_roots()


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

Environment: Sage 4.5.2 on Mac OS X 10.5.8 (32 bit).

Issue created by migration from https://trac.sagemath.org/ticket/9826





---

archive/issue_comments_096916.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-04-07T14:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96916",
    "user": "johanbosman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096917.json:
```json
{
    "body": "The bug is caused by a deallocation method trying to clean up all coefficients of a polynomial, which segfaults if not all coefficients have been initialised, which in turn happens if the init gets wrong input.  The attached patch should fix this.\n\nBy the way, it is not clear to me why the milestone was set to sage-5.0.  I thought that was for Windows-related issues.  Please correct me if I'm wrong.",
    "created_at": "2011-04-07T14:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96917",
    "user": "johanbosman"
}
```

The bug is caused by a deallocation method trying to clean up all coefficients of a polynomial, which segfaults if not all coefficients have been initialised, which in turn happens if the init gets wrong input.  The attached patch should fix this.

By the way, it is not clear to me why the milestone was set to sage-5.0.  I thought that was for Windows-related issues.  Please correct me if I'm wrong.



---

archive/issue_comments_096918.json:
```json
{
    "body": "The patch also fixes #10901.",
    "created_at": "2011-04-11T18:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96918",
    "user": "johanbosman"
}
```

The patch also fixes #10901.



---

archive/issue_comments_096919.json:
```json
{
    "body": "Refreshed patch, with a doctest.",
    "created_at": "2012-01-02T14:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96919",
    "user": "mjo"
}
```

Refreshed patch, with a doctest.



---

archive/issue_comments_096920.json:
```json
{
    "body": "Attachment\n\nThe fix works and makes sense to me (positive review for that). I've added a doctest (needs review), and rebased the original patch against 4.8.alpha5.\n\nUnfortunately, something is wrong with exceptions at the moment:\n\n\n```\nsage: (a*x).complex_roots()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1731, 0))\n...\n```\n\n\nand that's fixed by Simon King's patch in #11900, so I've added a dependency there. The milestone update is to match #11900.",
    "created_at": "2012-01-02T14:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96920",
    "user": "mjo"
}
```

Attachment

The fix works and makes sense to me (positive review for that). I've added a doctest (needs review), and rebased the original patch against 4.8.alpha5.

Unfortunately, something is wrong with exceptions at the moment:


```
sage: (a*x).complex_roots()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1731, 0))
...
```


and that's fixed by Simon King's patch in #11900, so I've added a dependency there. The milestone update is to match #11900.



---

archive/issue_comments_096921.json:
```json
{
    "body": "Nevermind that; the ERRORs still happen in 4.8.alpha6, but the doctests don't seem bothered.",
    "created_at": "2012-01-05T02:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96921",
    "user": "mjo"
}
```

Nevermind that; the ERRORs still happen in 4.8.alpha6, but the doctests don't seem bothered.



---

archive/issue_comments_096922.json:
```json
{
    "body": "In sage-5.0.beta4 this all works fine, so if you're okay with this, I suggest we give this ticket a positive review.",
    "created_at": "2012-02-29T15:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96922",
    "user": "johanbosman"
}
```

In sage-5.0.beta4 this all works fine, so if you're okay with this, I suggest we give this ticket a positive review.



---

archive/issue_comments_096923.json:
```json
{
    "body": "Well, we should definitely keep the doctest since this was a bug that was somehow fixed.\n\nIt looks to me like your original fix is still valid, though, from my not-too-deep understanding of mpfr. I'll ask on sage-devel.",
    "created_at": "2012-02-29T19:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96923",
    "user": "mjo"
}
```

Well, we should definitely keep the doctest since this was a bug that was somehow fixed.

It looks to me like your original fix is still valid, though, from my not-too-deep understanding of mpfr. I'll ask on sage-devel.



---

archive/issue_comments_096924.json:
```json
{
    "body": "Do you mean \"uninitialized\" instead of \"ininitialized\"?",
    "created_at": "2012-02-29T20:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96924",
    "user": "fbissey"
}
```

Do you mean "uninitialized" instead of "ininitialized"?



---

archive/issue_comments_096925.json:
```json
{
    "body": "Apply sage-trac_9826.patch\n\n(for patchbot)",
    "created_at": "2012-03-11T19:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96925",
    "user": "davidloeffler"
}
```

Apply sage-trac_9826.patch

(for patchbot)



---

archive/issue_comments_096926.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-04-24T04:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96926",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096927.json:
```json
{
    "body": "This should have been merged a while ago!",
    "created_at": "2012-04-24T04:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96927",
    "user": "vbraun"
}
```

This should have been merged a while ago!



---

archive/issue_comments_096928.json:
```json
{
    "body": "Same patch with my typo fixed.",
    "created_at": "2012-04-24T04:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96928",
    "user": "mjo"
}
```

Same patch with my typo fixed.



---

archive/issue_comments_096929.json:
```json
{
    "body": "Attachment\n\nI guess I should finally fix that typo, huh. The only change is to spell \"uninitialized\" correctly, but I'm uploading a separate patch since it's got a positive review.",
    "created_at": "2012-04-24T04:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96929",
    "user": "mjo"
}
```

Attachment

I guess I should finally fix that typo, huh. The only change is to spell "uninitialized" correctly, but I'm uploading a separate patch since it's got a positive review.



---

archive/issue_comments_096930.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-26T20:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9825#issuecomment-96930",
    "user": "jdemeyer"
}
```

Resolution: fixed
