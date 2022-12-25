# Issue 8791: improve doctest coverage of libs/mpmath/ext_main.pyx

archive/issues_008791.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @fredrik-johansson @haraldschilly\n\nAs the subject says. As of Sage 4.4, the doctest coverage of `sage/libs/mpmath/ext_main.pyx` is:\n\n```\n[mvngu@sage mpmath]$ sage -coverage ext_main.pyx \n----------------------------------------------------------------------\next_main.pyx\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE ext_main.pyx: 0% (0 of 102)\n\nMissing documentation:\n\t * __cinit__(ctx):\n\t * default(ctx):\n\t * _get_prec(ctx):\n\t * _set_prec(ctx, prec):\n\t * _set_dps(ctx, n):\n\t * _get_dps(ctx):\n\t * _get_prec_rounding(ctx):\n\t * mpf make_mpf(ctx, tuple v):\n\t * mpc make_mpc(ctx, tuple v):\n\t * _convert_param(ctx, x):\n\t * _wrap_libmp_function(ctx, mpf_f, mpc_f=None, mpi_f=None, doc=\"<no doc>\"):\n\t * _wrap_specfun(cls, name, f, wrap):\n\t * __init__(self, mpf_f, mpc_f=None, mpi_f=None, doc=\"<no doc>\"):\n\t * __call__(self, x, **kwargs):\n\t * __init__(self, name, f):\n\t * __call__(self, *args, **kwargs):\n\t * __richcmp__(self, other, int op):\n\t * __add__(self, other):\n\t * __sub__(self, other):\n\t * __mul__(self, other):\n\t * __div__(self, other):\n\t * __mod__(self, other):\n\t * __pow__(self, other, mod):\n\t * ae(s, t, rel_eps=None, abs_eps=None):\n\t * __hash__(self):\n\t * __repr__(self):\n\t * __str__(self):\n\t * real(self):\n\t * imag(self):\n\t * conjugate(self):\n\t * man(self):\n\t * exp(self):\n\t * bc(self):\n\t * __int__(self):\n\t * __long__(self):\n\t * __float__(self):\n\t * __complex__(self):\n\t * to_fixed(self, prec):\n\t * __getstate__(self):\n\t * __setstate__(self, val):\n\t * __init__(self, x=0, **kwargs):\n\t * __reduce__(self):\n\t * _get_mpf(self):\n\t * _set_mpf(self, v):\n\t * __nonzero__(self):\n\t * __hash__(self):\n\t * real(self):\n\t * imag(self):\n\t * conjugate(self):\n\t * man(self):\n\t * exp(self):\n\t * bc(self):\n\t * to_fixed(self, long prec):\n\t * __int__(self):\n\t * __float__(self):\n\t * __getstate__(self):\n\t * __setstate__(self, val):\n\t * __cinit__(self):\n\t * __neg__(s):\n\t * __pos__(s):\n\t * __abs__(s):\n\t * sqrt(s):\n\t * __richcmp__(self, other, int op):\n\t * __init__(self, func, name, docname=''):\n\t * __call__(self, prec=None, dps=None, rounding=None):\n\t * _mpf_(self):\n\t * __repr__(self):\n\t * __nonzero__(self):\n\t * __neg__(self):\n\t * __pos__(self):\n\t * __abs__(self):\n\t * sqrt(self):\n\t * to_fixed(self, prec):\n\t * __getstate__(self):\n\t * __setstate__(self, val):\n\t * __hash__(self):\n\t * __richcmp__(self, other, int op):\n\t * __init__(self, real=0, imag=0):\n\t * __cinit__(self):\n\t * __reduce__(self):\n\t * __setstate__(self, val):\n\t * __repr__(self):\n\t * __str__(s):\n\t * __nonzero__(self):\n\t * __complex__(self):\n\t * _get_mpc(self):\n\t * _set_mpc(self, tuple v):\n\t * real(self):\n\t * imag(self):\n\t * __hash__(self):\n\t * __neg__(s):\n\t * conjugate(s):\n\t * __pos__(s):\n\t * __abs__(s):\n\t * __richcmp__(self, other, int op):\n\n\nMissing doctests:\n\t * convert(ctx, x, strings=True):\n\t * isnan(ctx, x):\n\t * isinf(ctx, x):\n\t * isint(ctx, x):\n\t * fsum(ctx, terms, bint absolute=False, bint squared=False):\n\t * fdot(ctx, A, B=None):\n\t * mag(ctx, x):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8791\n\n",
    "created_at": "2010-04-28T04:44:20Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "improve doctest coverage of libs/mpmath/ext_main.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @fredrik-johansson @haraldschilly

As the subject says. As of Sage 4.4, the doctest coverage of `sage/libs/mpmath/ext_main.pyx` is:

```
[mvngu@sage mpmath]$ sage -coverage ext_main.pyx 
----------------------------------------------------------------------
ext_main.pyx
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE ext_main.pyx: 0% (0 of 102)

Missing documentation:
	 * __cinit__(ctx):
	 * default(ctx):
	 * _get_prec(ctx):
	 * _set_prec(ctx, prec):
	 * _set_dps(ctx, n):
	 * _get_dps(ctx):
	 * _get_prec_rounding(ctx):
	 * mpf make_mpf(ctx, tuple v):
	 * mpc make_mpc(ctx, tuple v):
	 * _convert_param(ctx, x):
	 * _wrap_libmp_function(ctx, mpf_f, mpc_f=None, mpi_f=None, doc="<no doc>"):
	 * _wrap_specfun(cls, name, f, wrap):
	 * __init__(self, mpf_f, mpc_f=None, mpi_f=None, doc="<no doc>"):
	 * __call__(self, x, **kwargs):
	 * __init__(self, name, f):
	 * __call__(self, *args, **kwargs):
	 * __richcmp__(self, other, int op):
	 * __add__(self, other):
	 * __sub__(self, other):
	 * __mul__(self, other):
	 * __div__(self, other):
	 * __mod__(self, other):
	 * __pow__(self, other, mod):
	 * ae(s, t, rel_eps=None, abs_eps=None):
	 * __hash__(self):
	 * __repr__(self):
	 * __str__(self):
	 * real(self):
	 * imag(self):
	 * conjugate(self):
	 * man(self):
	 * exp(self):
	 * bc(self):
	 * __int__(self):
	 * __long__(self):
	 * __float__(self):
	 * __complex__(self):
	 * to_fixed(self, prec):
	 * __getstate__(self):
	 * __setstate__(self, val):
	 * __init__(self, x=0, **kwargs):
	 * __reduce__(self):
	 * _get_mpf(self):
	 * _set_mpf(self, v):
	 * __nonzero__(self):
	 * __hash__(self):
	 * real(self):
	 * imag(self):
	 * conjugate(self):
	 * man(self):
	 * exp(self):
	 * bc(self):
	 * to_fixed(self, long prec):
	 * __int__(self):
	 * __float__(self):
	 * __getstate__(self):
	 * __setstate__(self, val):
	 * __cinit__(self):
	 * __neg__(s):
	 * __pos__(s):
	 * __abs__(s):
	 * sqrt(s):
	 * __richcmp__(self, other, int op):
	 * __init__(self, func, name, docname=''):
	 * __call__(self, prec=None, dps=None, rounding=None):
	 * _mpf_(self):
	 * __repr__(self):
	 * __nonzero__(self):
	 * __neg__(self):
	 * __pos__(self):
	 * __abs__(self):
	 * sqrt(self):
	 * to_fixed(self, prec):
	 * __getstate__(self):
	 * __setstate__(self, val):
	 * __hash__(self):
	 * __richcmp__(self, other, int op):
	 * __init__(self, real=0, imag=0):
	 * __cinit__(self):
	 * __reduce__(self):
	 * __setstate__(self, val):
	 * __repr__(self):
	 * __str__(s):
	 * __nonzero__(self):
	 * __complex__(self):
	 * _get_mpc(self):
	 * _set_mpc(self, tuple v):
	 * real(self):
	 * imag(self):
	 * __hash__(self):
	 * __neg__(s):
	 * conjugate(s):
	 * __pos__(s):
	 * __abs__(s):
	 * __richcmp__(self, other, int op):


Missing doctests:
	 * convert(ctx, x, strings=True):
	 * isnan(ctx, x):
	 * isinf(ctx, x):
	 * isint(ctx, x):
	 * fsum(ctx, terms, bint absolute=False, bint squared=False):
	 * fdot(ctx, A, B=None):
	 * mag(ctx, x):
```


Issue created by migration from https://trac.sagemath.org/ticket/8791





---

archive/issue_comments_080361.json:
```json
{
    "body": "Argh. Who wrote this code?\n\nThe actual code coverage, indirectly through mpmath's unit tests (which however aren't run automatically by Sage) is close to 99%, but writing Sage doctests slipped my mind entirely.\n\nSome of these functions have doctests, but they're added at runtime when importing mpmath. I'm considering whether statically duplicating them is a good idea, or whether it's better to just add static placeholders.\n\nMost of these are probably trivial to write, e.g.:\n\n```\nsage: import mpmath\nsage: mpmath.mpf(1).__add__(1)\nmpf('2.0')\n```\n\nBut I can't say when I'll have time to do this.",
    "created_at": "2010-04-28T07:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80361",
    "user": "https://github.com/fredrik-johansson"
}
```

Argh. Who wrote this code?

The actual code coverage, indirectly through mpmath's unit tests (which however aren't run automatically by Sage) is close to 99%, but writing Sage doctests slipped my mind entirely.

Some of these functions have doctests, but they're added at runtime when importing mpmath. I'm considering whether statically duplicating them is a good idea, or whether it's better to just add static placeholders.

Most of these are probably trivial to write, e.g.:

```
sage: import mpmath
sage: mpmath.mpf(1).__add__(1)
mpf('2.0')
```

But I can't say when I'll have time to do this.



---

archive/issue_comments_080362.json:
```json
{
    "body": "While I started to write some tests, I stumbled about `to_fixed()`. What does it do? Would be\n\n\n```\nsage: import mpmath\nsage: mpmath.mpf('88494.93').to_fixed(6)\n5663675\n```\n\n\nbe a doctest or a total abuse?!",
    "created_at": "2010-04-28T13:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80362",
    "user": "https://github.com/haraldschilly"
}
```

While I started to write some tests, I stumbled about `to_fixed()`. What does it do? Would be


```
sage: import mpmath
sage: mpmath.mpf('88494.93').to_fixed(6)
5663675
```


be a doctest or a total abuse?!



---

archive/issue_comments_080363.json:
```json
{
    "body": "Thanks a *lot*, Harald!\n\nto_fixed converts a number to binary fixed-point format. Perhaps for clarity something like the following could be used (1.25 is for exactness):\n\n\n```\nsage: mpmath.mpf(1.25).to_fixed(10)\n1280\nsage: int(1.25 * 2^10)\n1280\n```\n",
    "created_at": "2010-04-28T14:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80363",
    "user": "https://github.com/fredrik-johansson"
}
```

Thanks a *lot*, Harald!

to_fixed converts a number to binary fixed-point format. Perhaps for clarity something like the following could be used (1.25 is for exactness):


```
sage: mpmath.mpf(1.25).to_fixed(10)
1280
sage: int(1.25 * 2^10)
1280
```




---

archive/issue_comments_080364.json:
```json
{
    "body": "ok, i've done some more but i don't know how to really test init, cinit, call and some others.",
    "created_at": "2010-04-29T13:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80364",
    "user": "https://github.com/haraldschilly"
}
```

ok, i've done some more but i don't know how to really test init, cinit, call and some others.



---

archive/issue_comments_080365.json:
```json
{
    "body": "I have another question, is this a bug:\n\n```\nsage: mpmath.mpf(1) < 3\nTrue\nsage: 1 < mpmath.mpf(3)\nFalse\nsage: 4 == mpmath.mpf(4)\nFalse",
    "created_at": "2010-04-30T12:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80365",
    "user": "https://github.com/haraldschilly"
}
```

I have another question, is this a bug:

```
sage: mpmath.mpf(1) < 3
True
sage: 1 < mpmath.mpf(3)
False
sage: 4 == mpmath.mpf(4)
False



---

archive/issue_comments_080366.json:
```json
{
    "body": "I don't know how to test the remaining ones, but shouldn't be that hard to finish. Only 16 are still to go.",
    "created_at": "2010-04-30T13:26:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80366",
    "user": "https://github.com/haraldschilly"
}
```

I don't know how to test the remaining ones, but shouldn't be that hard to finish. Only 16 are still to go.



---

archive/issue_comments_080367.json:
```json
{
    "body": "Thanks! Very nice work.\n\nThe comparisons are definitely a bug. I created #8924 for this.",
    "created_at": "2010-05-07T19:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80367",
    "user": "https://github.com/fredrik-johansson"
}
```

Thanks! Very nice work.

The comparisons are definitely a bug. I created #8924 for this.



---

archive/issue_comments_080368.json:
```json
{
    "body": "Here is a new patch with almost full coverage: http://sage.math.washington.edu/home/fredrik/mpmath_doctests.patch\n\n(I did not use Harald's old patch as a base, though I think that one will mostly still be working. Perhaps they could be combined.)\n\nThe functions still missing doctests are pickling support for classes that shouldn't be pickable (not sure why they are there).",
    "created_at": "2011-11-14T20:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80368",
    "user": "https://github.com/fredrik-johansson"
}
```

Here is a new patch with almost full coverage: http://sage.math.washington.edu/home/fredrik/mpmath_doctests.patch

(I did not use Harald's old patch as a base, though I think that one will mostly still be working. Perhaps they could be combined.)

The functions still missing doctests are pickling support for classes that shouldn't be pickable (not sure why they are there).



---

archive/issue_comments_080369.json:
```json
{
    "body": "review this, not Harald's",
    "created_at": "2011-11-14T20:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80369",
    "user": "https://github.com/williamstein"
}
```

review this, not Harald's



---

archive/issue_comments_080370.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-14T20:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80370",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080371.json:
```json
{
    "body": "Attachment [mpmath_doctests.patch](tarball://root/attachments/some-uuid/ticket8791/mpmath_doctests.patch) by @williamstein created at 2011-11-14 20:10:02",
    "created_at": "2011-11-14T20:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80371",
    "user": "https://github.com/williamstein"
}
```

Attachment [mpmath_doctests.patch](tarball://root/attachments/some-uuid/ticket8791/mpmath_doctests.patch) by @williamstein created at 2011-11-14 20:10:02



---

archive/issue_comments_080372.json:
```json
{
    "body": "Apply mpmath_doctests.patch\n\n(for patchbot)",
    "created_at": "2012-03-11T15:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80372",
    "user": "https://github.com/loefflerd"
}
```

Apply mpmath_doctests.patch

(for patchbot)



---

archive/issue_comments_080373.json:
```json
{
    "body": "Wow -- this is a monumental piece of doctesting! It looks great. This will get us a long way towards the 90% doctest coverage goal.",
    "created_at": "2012-03-13T17:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80373",
    "user": "https://github.com/loefflerd"
}
```

Wow -- this is a monumental piece of doctesting! It looks great. This will get us a long way towards the 90% doctest coverage goal.



---

archive/issue_comments_080374.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-13T17:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80374",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080375.json:
```json
{
    "body": "This obviously fails on 32-bit systems:\n\n```\nsage -t  --long -force_lib devel/sage/sage/libs/mpmath/ext_main.pyx\n**********************************************************************\nFile \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-5.0.beta10/devel/sage-main/sage/libs/mpmath/ext_main.pyx\", line 2023:\n    sage: int(7.25 * 2**30)\nExpected:\n    7784628224\nGot:\n    7784628224L\n**********************************************************************\n```\n",
    "created_at": "2012-03-23T12:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80375",
    "user": "https://github.com/jdemeyer"
}
```

This obviously fails on 32-bit systems:

```
sage -t  --long -force_lib devel/sage/sage/libs/mpmath/ext_main.pyx
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-5.0.beta10/devel/sage-main/sage/libs/mpmath/ext_main.pyx", line 2023:
    sage: int(7.25 * 2**30)
Expected:
    7784628224
Got:
    7784628224L
**********************************************************************
```




---

archive/issue_comments_080376.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-23T12:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80376",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080377.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2012-03-25T14:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80377",
    "user": "https://github.com/loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_080378.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-25T15:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80378",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080379.json:
```json
{
    "body": "Attachment [trac_8791-fix.patch](tarball://root/attachments/some-uuid/ticket8791/trac_8791-fix.patch) by @loefflerd created at 2012-03-25 15:00:30\n\nApply mpmath_doctests.patch, trac_8791-fix.patch\n\nThis is a one-line fix -- anyone willing to quickly sign off on it?",
    "created_at": "2012-03-25T15:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80379",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8791-fix.patch](tarball://root/attachments/some-uuid/ticket8791/trac_8791-fix.patch) by @loefflerd created at 2012-03-25 15:00:30

Apply mpmath_doctests.patch, trac_8791-fix.patch

This is a one-line fix -- anyone willing to quickly sign off on it?



---

archive/issue_comments_080380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-27T15:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80380",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080381.json:
```json
{
    "body": "Good!",
    "created_at": "2012-03-27T15:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80381",
    "user": "https://github.com/jdemeyer"
}
```

Good!



---

archive/issue_events_021432.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-28T10:02:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8791#event-21432"
}
```



---

archive/issue_comments_080382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-28T10:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8791#issuecomment-80382",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
