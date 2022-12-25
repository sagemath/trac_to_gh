# Issue 688: conversion to Singular for QuotientRingElements broken

archive/issues_000688.json:
```json
{
    "body": "Assignee: @malb\n\nConsider:\n\n```\nsage: P.<x,y>  = PolynomialRing(GF(2),2)\nsage: I = sage.rings.ideal.FieldIdeal(P)\nsage: Q = P.quo(I)\nsage: Q._singular_()\n\n//   characteristic : 2\n//   number of vars : 2\n//        block   1 : ordering dp\n//                  : names    x y\n//        block   2 : ordering C\n// quotient ring from ideal\n_[1]=x2+x\n_[2]=y2+y\nsage: Q(x)\nxbar\nsage: Q(x)._singular_()\n--------------------------------------------------------------\n<type 'exceptions.TypeError'> Traceback (most recent call last)\n...\n<type 'exceptions.TypeError'>: Singular error:\n   ? `xbar` is undefined\n   ? error occurred in STDIN line 185: `def sage69=xbar;`\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/688\n\n",
    "closed_at": "2007-10-20T21:48:59Z",
    "created_at": "2007-09-18T13:09:54Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "conversion to Singular for QuotientRingElements broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/688",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

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

archive/issue_comments_003567.json:
```json
{
    "body": "Did this ever work?  Is this really a feature request?",
    "created_at": "2007-09-21T00:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3567",
    "user": "https://github.com/williamstein"
}
```

Did this ever work?  Is this really a feature request?



---

archive/issue_events_001837.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-21T02:05:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1837"
}
```



---

archive/issue_comments_003568.json:
```json
{
    "body": "Attachment [qring.patch](tarball://root/attachments/some-uuid/ticket688/qring.patch) by @malb created at 2007-10-20 21:45:37",
    "created_at": "2007-10-20T21:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3568",
    "user": "https://github.com/malb"
}
```

Attachment [qring.patch](tarball://root/attachments/some-uuid/ticket688/qring.patch) by @malb created at 2007-10-20 21:45:37



---

archive/issue_comments_003569.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-20T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3569",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003570.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-10-20T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3570",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_003571.json:
```json
{
    "body": "Fixed in attached patch.",
    "created_at": "2007-10-20T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3571",
    "user": "https://github.com/malb"
}
```

Fixed in attached patch.



---

archive/issue_comments_003572.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T21:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3572",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001838.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:48:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1838"
}
```



---

archive/issue_events_001839.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:49:57Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1839"
}
```



---

archive/issue_events_001840.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:49:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1840"
}
```



---

archive/issue_events_001841.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:52:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1841"
}
```



---

archive/issue_events_001842.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:52:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1842"
}
```



---

archive/issue_comments_003573.json:
```json
{
    "body": "inst.tex.hg is a bundle against hg_sage.  You accidently did hg_sage.send('...') instead of\nhg_doc.send('...').  Please create a bundle against the docs.",
    "created_at": "2007-10-20T21:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3573",
    "user": "https://github.com/williamstein"
}
```

inst.tex.hg is a bundle against hg_sage.  You accidently did hg_sage.send('...') instead of
hg_doc.send('...').  Please create a bundle against the docs.



---

archive/issue_comments_003574.json:
```json
{
    "body": "That comment was meant for a different ticket. Sorry.",
    "created_at": "2007-10-20T21:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/688#issuecomment-3574",
    "user": "https://github.com/williamstein"
}
```

That comment was meant for a different ticket. Sorry.



---

archive/issue_events_001843.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:52:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1843"
}
```



---

archive/issue_events_001844.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-20T21:52:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/688",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/688#event-1844"
}
```
