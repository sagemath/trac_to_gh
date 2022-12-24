# Issue 688: conversion to Singular for QuotientRingElements broken

archive/issues_000688.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider:\n\n\n```\nsage: P.<x,y>  = PolynomialRing(GF(2),2)\nsage: I = sage.rings.ideal.FieldIdeal(P)\nsage: Q = P.quo(I)\nsage: Q._singular_()\n\n//   characteristic : 2\n//   number of vars : 2\n//        block   1 : ordering dp\n//                  : names    x y\n//        block   2 : ordering C\n// quotient ring from ideal\n_[1]=x2+x\n_[2]=y2+y\nsage: Q(x)\nxbar\nsage: Q(x)._singular_()\n--------------------------------------------------------------\n<type 'exceptions.TypeError'> Traceback (most recent call last)\n...\n<type 'exceptions.TypeError'>: Singular error:\n   ? `xbar` is undefined\n   ? error occurred in STDIN line 185: `def sage69=xbar;`\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/688\n\n",
    "created_at": "2007-09-18T13:09:54Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "conversion to Singular for QuotientRingElements broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/688",
    "user": "@malb"
}
```
Assignee: @williamstein

Consider:


```
sage: P.<x,y>  = PolynomialRing(GF(2),2)
sage: I = sage.rings.ideal.FieldIdeal(P)
sage: Q = P.quo(I)
sage: Q._singular_()

//   characteristic : 2
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
// quotient ring from ideal
_[1]=x2+x
_[2]=y2+y
sage: Q(x)
xbar
sage: Q(x)._singular_()
--------------------------------------------------------------
<type 'exceptions.TypeError'> Traceback (most recent call last)
...
<type 'exceptions.TypeError'>: Singular error:
   ? `xbar` is undefined
   ? error occurred in STDIN line 185: `def sage69=xbar;`
```


Issue created by migration from https://trac.sagemath.org/ticket/688





---

archive/issue_comments_003580.json:
```json
{
    "body": "Did this ever work?  Is this really a feature request?",
    "created_at": "2007-09-21T00:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3580",
    "user": "@williamstein"
}
```

Did this ever work?  Is this really a feature request?



---

archive/issue_comments_003581.json:
```json
{
    "body": "Attachment [qring.patch](tarball://root/attachments/some-uuid/ticket688/qring.patch) by @malb created at 2007-10-20 21:45:37",
    "created_at": "2007-10-20T21:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3581",
    "user": "@malb"
}
```

Attachment [qring.patch](tarball://root/attachments/some-uuid/ticket688/qring.patch) by @malb created at 2007-10-20 21:45:37



---

archive/issue_comments_003582.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-20T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3582",
    "user": "@malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003583.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-10-20T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3583",
    "user": "@malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_003584.json:
```json
{
    "body": "Fixed in attached patch.",
    "created_at": "2007-10-20T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3584",
    "user": "@malb"
}
```

Fixed in attached patch.



---

archive/issue_comments_003585.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T21:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3585",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003586.json:
```json
{
    "body": "inst.tex.hg is a bundle against hg_sage.  You accidently did hg_sage.send('...') instead of\nhg_doc.send('...').  Please create a bundle against the docs.",
    "created_at": "2007-10-20T21:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3586",
    "user": "@williamstein"
}
```

inst.tex.hg is a bundle against hg_sage.  You accidently did hg_sage.send('...') instead of
hg_doc.send('...').  Please create a bundle against the docs.



---

archive/issue_comments_003587.json:
```json
{
    "body": "That comment was meant for a different ticket. Sorry.",
    "created_at": "2007-10-20T21:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3587",
    "user": "@williamstein"
}
```

That comment was meant for a different ticket. Sorry.
