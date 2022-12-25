# Issue 4055: [already fixed?] serious bug in polynomial multiplication

archive/issues_004055.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  boothby\n\nSeems to be something with the generic karatsuba, perhaps it should not be used for inexact rings?\n\n```\nsage: R.<x> = RR[]\nsage: (x-1e16)*(x-1e17)\n 1.00000000000000*x^2 + 1.00000000000000e33\n\nsage: R.<x> = RDF['y']['x']\nsage: (x-1e123)*(x-1e100)\n 1.0*x^2 + 1e+223\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4055\n\n",
    "closed_at": "2009-05-22T02:56:35Z",
    "created_at": "2008-09-04T00:06:57Z",
    "labels": [
        "component: algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[already fixed?] serious bug in polynomial multiplication",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4055",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

CC:  boothby

Seems to be something with the generic karatsuba, perhaps it should not be used for inexact rings?

```
sage: R.<x> = RR[]
sage: (x-1e16)*(x-1e17)
 1.00000000000000*x^2 + 1.00000000000000e33

sage: R.<x> = RDF['y']['x']
sage: (x-1e123)*(x-1e100)
 1.0*x^2 + 1e+223
```


Issue created by migration from https://trac.sagemath.org/ticket/4055





---

archive/issue_comments_029169.json:
```json
{
    "body": "I believe this got fixed by Tom Boothby at Sage Days 12, see #3056.  I'm ccing him so he can react.  In any case, this looks fine now:\n\n```\n[ghitza@artin ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: R.<x> = RR[]\nsage: sage: (x-1e16)*(x-1e17)\n1.00000000000000*x^2 - 1.10000000000000e17*x + 1.00000000000000e33\nsage: sage: R.<x> = RDF['y']['x']\nsage: sage: (x-1e123)*(x-1e100)\n1.0*x^2 + (-1e+123)*x + 1e+223\n```",
    "created_at": "2009-01-28T21:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4055#issuecomment-29169",
    "user": "https://github.com/aghitza"
}
```

I believe this got fixed by Tom Boothby at Sage Days 12, see #3056.  I'm ccing him so he can react.  In any case, this looks fine now:

```
[ghitza@artin ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: R.<x> = RR[]
sage: sage: (x-1e16)*(x-1e17)
1.00000000000000*x^2 - 1.10000000000000e17*x + 1.00000000000000e33
sage: sage: R.<x> = RDF['y']['x']
sage: sage: (x-1e123)*(x-1e100)
1.0*x^2 + (-1e+123)*x + 1e+223
```



---

archive/issue_comments_029170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-22T02:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4055#issuecomment-29170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009259.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-22T02:56:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4055#event-9259"
}
```



---

archive/issue_events_009260.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-22T02:56:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4055#event-9260"
}
```



---

archive/issue_comments_029171.json:
```json
{
    "body": "Fixed via #3056.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T02:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4055#issuecomment-29171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #3056.

Cheers,

Michael
