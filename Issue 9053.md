# Issue 9053: Sage's new generic HNF doesn't quite work right wrt the free modules code

archive/issues_009053.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  minz\n\nThe last output below should obviously be True, but it is False.\n\n```\nsage: R.<x> = GF(7)[]\nsage: A = R^3\nsage: L = A.span([x*A.0 + (x^3 + 1)*A.1, x*A.2]); L\nFree module of degree 3 and rank 2 over Univariate Polynomial Ring in x over Finite Field of size 7\nEchelon basis matrix:\n[      x x^3 + 1       0]\n[      0       0       x]\nsage: M = A.span([x*L.0]); M\nFree module of degree 3 and rank 1 over Univariate Polynomial Ring in x over Finite Field of size 7\nEchelon basis matrix:\n[    x^2 x^4 + x       0]\nsage: M.0 in L\nFalse\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9053\n\n",
    "created_at": "2010-05-26T08:41:23Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Sage's new generic HNF doesn't quite work right wrt the free modules code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9053",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  minz

The last output below should obviously be True, but it is False.

```
sage: R.<x> = GF(7)[]
sage: A = R^3
sage: L = A.span([x*A.0 + (x^3 + 1)*A.1, x*A.2]); L
Free module of degree 3 and rank 2 over Univariate Polynomial Ring in x over Finite Field of size 7
Echelon basis matrix:
[      x x^3 + 1       0]
[      0       0       x]
sage: M = A.span([x*L.0]); M
Free module of degree 3 and rank 1 over Univariate Polynomial Ring in x over Finite Field of size 7
Echelon basis matrix:
[    x^2 x^4 + x       0]
sage: M.0 in L
False
```

Issue created by migration from https://trac.sagemath.org/ticket/9053





---

archive/issue_comments_083707.json:
```json
{
    "body": "Changing assignee from @aghitza to jason, was.",
    "created_at": "2010-09-02T10:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83707",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to jason, was.



---

archive/issue_comments_083708.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-09-02T10:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83708",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_083709.json:
```json
{
    "body": "Attachment [trac_9053_fixes_pivots.patch](tarball://root/attachments/some-uuid/ticket9053/trac_9053_fixes_pivots.patch) by minz created at 2011-03-18 10:47:06\n\nThe bug was a single line in _echelon_form_PID which returned the wrong pivot element for matrices of one row. The attached patch should fix that.\n\nWhile doctesting all of Sage I received two errors (that seem unrelated?):\n\n```\nThe following tests failed:\n\n        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/gal_reps.py # Time out\n        sage -t  -long -force_lib devel/sage/sage/interfaces/sage0.py # 2 doctests failed\n```\n\nThe first apparently also came up during discussions on [#9390](http://trac.sagemath.org/sage_trac/ticket/9390). The doctest failure in sage0.py \"randomly\" appeared or not when I reran the test mutiple times. I'm not quite sure what to make of this...",
    "created_at": "2011-03-18T10:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83709",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

Attachment [trac_9053_fixes_pivots.patch](tarball://root/attachments/some-uuid/ticket9053/trac_9053_fixes_pivots.patch) by minz created at 2011-03-18 10:47:06

The bug was a single line in _echelon_form_PID which returned the wrong pivot element for matrices of one row. The attached patch should fix that.

While doctesting all of Sage I received two errors (that seem unrelated?):

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/schemes/elliptic_curves/gal_reps.py # Time out
        sage -t  -long -force_lib devel/sage/sage/interfaces/sage0.py # 2 doctests failed
```

The first apparently also came up during discussions on [#9390](http://trac.sagemath.org/sage_trac/ticket/9390). The doctest failure in sage0.py "randomly" appeared or not when I reran the test mutiple times. I'm not quite sure what to make of this...



---

archive/issue_comments_083710.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-18T10:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83710",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083711.json:
```json
{
    "body": "I just reran the above two doctests on a different machine and receieved no doctest failures. *shrug*",
    "created_at": "2011-03-21T23:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83711",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

I just reran the above two doctests on a different machine and receieved no doctest failures. *shrug*



---

archive/issue_comments_083712.json:
```json
{
    "body": "line wrapping",
    "created_at": "2011-03-22T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83712",
    "user": "https://github.com/kini"
}
```

line wrapping



---

archive/issue_comments_083713.json:
```json
{
    "body": "Attachment [trac_9053_fixes_pivots.v2.patch](tarball://root/attachments/some-uuid/ticket9053/trac_9053_fixes_pivots.v2.patch) by @kini created at 2011-03-22 00:06:10\n\nI can't replicate your doctest failures. Everything passes on sage.math, except the ever-troublesome devel/sage/sage/tests/startup.py , which I tried again individually with no problems. The fix itself looks good. Reference builds, though how that could be affected I don't know. IIRC all code should be within 79 columns, so I split some lines in this function for you while you're at it. Feel free to rewrite it if it looks ugly, haha.",
    "created_at": "2011-03-22T00:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83713",
    "user": "https://github.com/kini"
}
```

Attachment [trac_9053_fixes_pivots.v2.patch](tarball://root/attachments/some-uuid/ticket9053/trac_9053_fixes_pivots.v2.patch) by @kini created at 2011-03-22 00:06:10

I can't replicate your doctest failures. Everything passes on sage.math, except the ever-troublesome devel/sage/sage/tests/startup.py , which I tried again individually with no problems. The fix itself looks good. Reference builds, though how that could be affected I don't know. IIRC all code should be within 79 columns, so I split some lines in this function for you while you're at it. Feel free to rewrite it if it looks ugly, haha.



---

archive/issue_comments_083714.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-22T00:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83714",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083715.json:
```json
{
    "body": "(for patchbot...)",
    "created_at": "2011-03-22T00:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83715",
    "user": "https://github.com/kini"
}
```

(for patchbot...)



---

archive/issue_comments_083716.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T13:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9053#issuecomment-83716",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022177.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-07T13:48:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9053",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9053#event-22177"
}
```
