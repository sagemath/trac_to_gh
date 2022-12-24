# Issue 5739: zeta(CDF(1)) go boom!

archive/issues_005739.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb fredrik\n\n\n```\nwstein@bsd:~/build/sage-3.4.1.rc1$ uname -a\nDarwin bsd.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386\n\nwstein@bsd:~/build/sage-3.4.1.rc1$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: zeta(CDF(1))\n| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5739\n\n",
    "created_at": "2009-04-10T23:09:59Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "zeta(CDF(1)) go boom!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5739",
    "user": "was"
}
```
Assignee: was

CC:  robertwb fredrik


```
wstein@bsd:~/build/sage-3.4.1.rc1$ uname -a
Darwin bsd.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386

wstein@bsd:~/build/sage-3.4.1.rc1$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: zeta(CDF(1))
| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



Issue created by migration from https://trac.sagemath.org/ticket/5739





---

archive/issue_comments_044861.json:
```json
{
    "body": "I think Robert Bradshaw massively optimized CDF special functions, and that's where this comes from.  Changing the code for zeta in complex_double.pyx to:\n\n```\n        cdef pari_sp sp\n        sp = avma\n        _sig_on\n        x = self._new_from_gen_c(  gzeta(self._gen(), PREC),   sp)\n        _sig_off\n        return x\n```\n\nsomewhat fixes the problem, though doing \n\n```\nsage: zeta(CDF(0))\n```\n\nthen raises a RuntimeError.   Unfortunately, doing this doesn't work because the _sig_on/_sig_off stuff doesn't play well with Cython exceptions:\n\n```\n        cdef pari_sp sp\n        sp = avma\n        try:\n           _sig_on\n           x = self._new_from_gen_c(  gzeta(self._gen(), PREC),   sp)\n           _sig_off\n        except:\n           raise ValueError\n        return x\n```\n\n\nSo I'm not sure how to fix this in general in a nice way with the right exception, but definitely adding _sig_on/_sig_off's around all the calls to pari is a very very good idea.",
    "created_at": "2009-04-11T05:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44861",
    "user": "was"
}
```

I think Robert Bradshaw massively optimized CDF special functions, and that's where this comes from.  Changing the code for zeta in complex_double.pyx to:

```
        cdef pari_sp sp
        sp = avma
        _sig_on
        x = self._new_from_gen_c(  gzeta(self._gen(), PREC),   sp)
        _sig_off
        return x
```

somewhat fixes the problem, though doing 

```
sage: zeta(CDF(0))
```

then raises a RuntimeError.   Unfortunately, doing this doesn't work because the _sig_on/_sig_off stuff doesn't play well with Cython exceptions:

```
        cdef pari_sp sp
        sp = avma
        try:
           _sig_on
           x = self._new_from_gen_c(  gzeta(self._gen(), PREC),   sp)
           _sig_off
        except:
           raise ValueError
        return x
```


So I'm not sure how to fix this in general in a nice way with the right exception, but definitely adding _sig_on/_sig_off's around all the calls to pari is a very very good idea.



---

archive/issue_comments_044862.json:
```json
{
    "body": "We should be able to replace the calls to pari with calls to mpmath.",
    "created_at": "2009-06-05T04:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44862",
    "user": "mhansen"
}
```

We should be able to replace the calls to pari with calls to mpmath.



---

archive/issue_comments_044863.json:
```json
{
    "body": "Changing assignee from was to fredrik.",
    "created_at": "2009-06-05T04:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44863",
    "user": "mhansen"
}
```

Changing assignee from was to fredrik.



---

archive/issue_comments_044864.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T06:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44864",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044865.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-18T16:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44865",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_044866.json:
```json
{
    "body": "Attachment [trac_5739.patch](tarball://root/attachments/some-uuid/ticket5739/trac_5739.patch) by kcrisman created at 2010-01-18 16:22:05\n\nThe patch looks fine, but results in zeta of a CDF being approximately fifty times slower.  This seems problematic, and perhaps also something that would happen a lot if we start switching things to mpmath?  Mpmath looks like a great package, but if it has the same issue as NetworkX versus C graphs, we might not want to move default behavior there quite yet. \n\nMarking as needs_info since there does not seem to be a Sage-wide policy on mpmath at this point, and I am reluctant to give positive review to such a marked slowdown.",
    "created_at": "2010-01-18T16:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44866",
    "user": "kcrisman"
}
```

Attachment [trac_5739.patch](tarball://root/attachments/some-uuid/ticket5739/trac_5739.patch) by kcrisman created at 2010-01-18 16:22:05

The patch looks fine, but results in zeta of a CDF being approximately fifty times slower.  This seems problematic, and perhaps also something that would happen a lot if we start switching things to mpmath?  Mpmath looks like a great package, but if it has the same issue as NetworkX versus C graphs, we might not want to move default behavior there quite yet. 

Marking as needs_info since there does not seem to be a Sage-wide policy on mpmath at this point, and I am reluctant to give positive review to such a marked slowdown.



---

archive/issue_comments_044867.json:
```json
{
    "body": "Attachment [5739-CDF-zeta.patch](tarball://root/attachments/some-uuid/ticket5739/5739-CDF-zeta.patch) by robertwb created at 2010-01-18 19:45:45",
    "created_at": "2010-01-18T19:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44867",
    "user": "robertwb"
}
```

Attachment [5739-CDF-zeta.patch](tarball://root/attachments/some-uuid/ticket5739/5739-CDF-zeta.patch) by robertwb created at 2010-01-18 19:45:45



---

archive/issue_comments_044868.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-01-18T19:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44868",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_044869.json:
```json
{
    "body": "I added an alternative patch that special cases the one pole at s=1 (returning the unsigned infinity, as gamma does).",
    "created_at": "2010-01-18T19:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44869",
    "user": "robertwb"
}
```

I added an alternative patch that special cases the one pole at s=1 (returning the unsigned infinity, as gamma does).



---

archive/issue_comments_044870.json:
```json
{
    "body": "I hate to send this back to the drawing board again, but let's just fix things once and for all...\n\n```\nsage: zeta(CDF(1))\nInfinity\nsage: zeta(CC(1))\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/Users/.../<ipython console> in <module>()\n\n/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/functions/transcendental.pyc in zeta(s)\n    153     \"\"\"\n    154     try:\n--> 155         return s.zeta()\n    156     except AttributeError:\n    157         return ComplexField()(s).zeta()\n\n/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/rings/complex_number.so in sage.rings.complex_number.ComplexNumber.zeta (sage/rings/complex_number.c:12174)()\n\n/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44110)()\n\nPariError:  (8)\n```\n\nCan we think of any other places where this needs to be checked?  For instance, zeta(1) returns this error too, though I think it inherits it from the CC example.  \n\nAlso, regarding whether it should be Infinity or some signed infinity:\n\n```\nsage: zeta(RR(1))\n+infinity\nsage: zeta(RDF(1))\n+infinity\n```\n\nI'm not saying which one is better, just what the current behavior is.  What do folks think?",
    "created_at": "2010-01-19T18:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44870",
    "user": "kcrisman"
}
```

I hate to send this back to the drawing board again, but let's just fix things once and for all...

```
sage: zeta(CDF(1))
Infinity
sage: zeta(CC(1))
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/Users/.../<ipython console> in <module>()

/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/functions/transcendental.pyc in zeta(s)
    153     """
    154     try:
--> 155         return s.zeta()
    156     except AttributeError:
    157         return ComplexField()(s).zeta()

/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/rings/complex_number.so in sage.rings.complex_number.ComplexNumber.zeta (sage/rings/complex_number.c:12174)()

/Users/.../sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44110)()

PariError:  (8)
```

Can we think of any other places where this needs to be checked?  For instance, zeta(1) returns this error too, though I think it inherits it from the CC example.  

Also, regarding whether it should be Infinity or some signed infinity:

```
sage: zeta(RR(1))
+infinity
sage: zeta(RDF(1))
+infinity
```

I'm not saying which one is better, just what the current behavior is.  What do folks think?



---

archive/issue_comments_044871.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-19T18:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44871",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_044872.json:
```json
{
    "body": "kcrisman:\n\nStarting with the next version, mpmath uses the Riemann-Siegel formula, so it should be much faster than Pari for large imaginary parts near the critical strip. Right now I even get a segmentation fault if I try to compute zeta(CDF(1/2+10000000*I)) in Sage.\n\nFor CDF, zeta could also use mpmath.fp.zeta that will be available in the next version of mpmath. This function is currently typically 10-50 times faster than mpmath.mp.zeta. However, fp.zeta loses accuracy proportional to the magnitude of the imaginary part near the critical strip, so the question is whether this loss would be acceptable. For small imaginary parts, it's quite accurate.\n\nBoth functions could be accelerated in Sage by overriding the base case of an internal function (mpmath/functions/zeta.py/_zetasum in the svn trunk, if anyone wants a go). This should require just few lines of Cython.\n\nOther than that, I would recommend keeping Pari where it's faster.",
    "created_at": "2010-01-23T08:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44872",
    "user": "fredrik.johansson"
}
```

kcrisman:

Starting with the next version, mpmath uses the Riemann-Siegel formula, so it should be much faster than Pari for large imaginary parts near the critical strip. Right now I even get a segmentation fault if I try to compute zeta(CDF(1/2+10000000*I)) in Sage.

For CDF, zeta could also use mpmath.fp.zeta that will be available in the next version of mpmath. This function is currently typically 10-50 times faster than mpmath.mp.zeta. However, fp.zeta loses accuracy proportional to the magnitude of the imaginary part near the critical strip, so the question is whether this loss would be acceptable. For small imaginary parts, it's quite accurate.

Both functions could be accelerated in Sage by overriding the base case of an internal function (mpmath/functions/zeta.py/_zetasum in the svn trunk, if anyone wants a go). This should require just few lines of Cython.

Other than that, I would recommend keeping Pari where it's faster.



---

archive/issue_comments_044873.json:
```json
{
    "body": "Attachment [5739-CC-RR.patch](tarball://root/attachments/some-uuid/ticket5739/5739-CC-RR.patch) by robertwb created at 2010-01-24 11:11:05\n\napply this and 5739-CDF-zeta.patch",
    "created_at": "2010-01-24T11:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44873",
    "user": "robertwb"
}
```

Attachment [5739-CC-RR.patch](tarball://root/attachments/some-uuid/ticket5739/5739-CC-RR.patch) by robertwb created at 2010-01-24 11:11:05

apply this and 5739-CDF-zeta.patch



---

archive/issue_comments_044874.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T11:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44874",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_044875.json:
```json
{
    "body": "I fixed CC. As to whether it should be a signed or unsigned infinity, I went with unsigned because it has a simple pole there. \n\n\n```\n10000.5772229475\nsage: zeta(.9999)\n-9999.42279161783\n```\n\n\nWhen the new mpmath gets released, we could open a ticket with timings and accuracy comparison. Generally we favor correctness over speed.",
    "created_at": "2010-01-24T11:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44875",
    "user": "robertwb"
}
```

I fixed CC. As to whether it should be a signed or unsigned infinity, I went with unsigned because it has a simple pole there. 


```
10000.5772229475
sage: zeta(.9999)
-9999.42279161783
```


When the new mpmath gets released, we could open a ticket with timings and accuracy comparison. Generally we favor correctness over speed.



---

archive/issue_comments_044876.json:
```json
{
    "body": "Patch applies cleanly to 4.5.alpha1 and builds fine, but some doctests fail:\n\n```\nsage -t  sage/rings/real_mpfr.pyx\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/real_mpfr.pyx\", line 4487:\n    sage: R(1).zeta()\nExpected:\n    Infinity\nGot:\n    +infinity\n**********************************************************************\n1 items had failures:\n   1 of  12 in __main__.example_149\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_real_mpfr.py\n         [10.2 s]\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/complex_number.pyx\", line 2093:\n    sage: zeta(1)\nExpected:\n    Infinity\nGot:\n    zeta(1)\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_72\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_complex_number.py\n         [8.6 s]\n```\n\n\nMoreover, it doesn't seem to live up to the promise in the title of making the return value of zeta(1) consistent:\n\n\n```\nsage: zeta(RR(1))\n+infinity\nsage: zeta(RDF(1))\nInfinity\n```\n",
    "created_at": "2010-07-02T19:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44876",
    "user": "davidloeffler"
}
```

Patch applies cleanly to 4.5.alpha1 and builds fine, but some doctests fail:

```
sage -t  sage/rings/real_mpfr.pyx
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/real_mpfr.pyx", line 4487:
    sage: R(1).zeta()
Expected:
    Infinity
Got:
    +infinity
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_149
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_real_mpfr.py
         [10.2 s]
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/complex_number.pyx", line 2093:
    sage: zeta(1)
Expected:
    Infinity
Got:
    zeta(1)
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_72
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_complex_number.py
         [8.6 s]
```


Moreover, it doesn't seem to live up to the promise in the title of making the return value of zeta(1) consistent:


```
sage: zeta(RR(1))
+infinity
sage: zeta(RDF(1))
Infinity
```




---

archive/issue_comments_044877.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-02T19:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44877",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_044878.json:
```json
{
    "body": "Since #8864, `zeta(1)` returns the answer given by GiNaC, which leaves it unevaluated because it doesn't know about infinity. I'll change this in the next pynac release to return unsigned infinity.",
    "created_at": "2010-07-02T22:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44878",
    "user": "burcin"
}
```

Since #8864, `zeta(1)` returns the answer given by GiNaC, which leaves it unevaluated because it doesn't know about infinity. I'll change this in the next pynac release to return unsigned infinity.



---

archive/issue_comments_044879.json:
```json
{
    "body": "Attachment [5739-complex-zeta.patch](tarball://root/attachments/some-uuid/ticket5739/5739-complex-zeta.patch) by robertwb created at 2010-07-29 06:49:38\n\napply only this patch",
    "created_at": "2010-07-29T06:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44879",
    "user": "robertwb"
}
```

Attachment [5739-complex-zeta.patch](tarball://root/attachments/some-uuid/ticket5739/5739-complex-zeta.patch) by robertwb created at 2010-07-29 06:49:38

apply only this patch



---

archive/issue_comments_044880.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-29T06:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44880",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_044881.json:
```json
{
    "body": "It's really sad we still have this trivial-to-fix hard crash after over a year!\n\nI've attached a patch that fixes the behavior of CDF(1).zeta() and CC(1).zeta(). It leaves the real fields alone, which I think is fine 'cause they have reasonable representations of (an) infinity, and we usually try to return something of the same type. (IN the complex case, infinity is a lot messier without a lot of special casing that's beyond the scope of this ticket...)\n\n\n```\nsage: RR(1).zeta(), RDF(1).zeta(), CC(1).zeta(), CDF(1).zeta()\n(+infinity, +infinity, Infinity, Infinity)\n```\n",
    "created_at": "2010-07-29T06:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44881",
    "user": "robertwb"
}
```

It's really sad we still have this trivial-to-fix hard crash after over a year!

I've attached a patch that fixes the behavior of CDF(1).zeta() and CC(1).zeta(). It leaves the real fields alone, which I think is fine 'cause they have reasonable representations of (an) infinity, and we usually try to return something of the same type. (IN the complex case, infinity is a lot messier without a lot of special casing that's beyond the scope of this ticket...)


```
sage: RR(1).zeta(), RDF(1).zeta(), CC(1).zeta(), CDF(1).zeta()
(+infinity, +infinity, Infinity, Infinity)
```




---

archive/issue_comments_044882.json:
```json
{
    "body": "OK, that looks fine. I'd still argue that it should be an unsigned infinity in the real field cases as well, but (as you say) more or less anything is better than the current behaviour! Let's get this in.",
    "created_at": "2010-09-23T10:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44882",
    "user": "davidloeffler"
}
```

OK, that looks fine. I'd still argue that it should be an unsigned infinity in the real field cases as well, but (as you say) more or less anything is better than the current behaviour! Let's get this in.



---

archive/issue_comments_044883.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T10:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44883",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044884.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T08:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44884",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_044885.json:
```json
{
    "body": "The patch is missing a Mercurial header.  Could someone add this and restore the positive review?",
    "created_at": "2010-09-28T08:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44885",
    "user": "mpatel"
}
```

The patch is missing a Mercurial header.  Could someone add this and restore the positive review?



---

archive/issue_comments_044886.json:
```json
{
    "body": "Version with Mercurial header",
    "created_at": "2010-09-28T08:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44886",
    "user": "davidloeffler"
}
```

Version with Mercurial header



---

archive/issue_comments_044887.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T08:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44887",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_044888.json:
```json
{
    "body": "Attachment [5739-complex-zeta-with-header.patch](tarball://root/attachments/some-uuid/ticket5739/5739-complex-zeta-with-header.patch) by davidloeffler created at 2010-09-28 08:26:27\n\nDone",
    "created_at": "2010-09-28T08:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44888",
    "user": "davidloeffler"
}
```

Attachment [5739-complex-zeta-with-header.patch](tarball://root/attachments/some-uuid/ticket5739/5739-complex-zeta-with-header.patch) by davidloeffler created at 2010-09-28 08:26:27

Done



---

archive/issue_comments_044889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5739#issuecomment-44889",
    "user": "mpatel"
}
```

Resolution: fixed
