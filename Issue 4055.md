# Issue 4055: serious bug in polynomial multiplication

archive/issues_004055.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  boothby\n\nSeems to be something with the generic karatsuba, perhaps it should not be used for inexact rings?\n\n\n```\nsage: R.<x> = RR[]\nsage: (x-1e16)*(x-1e17)\n 1.00000000000000*x^2 + 1.00000000000000e33\n\nsage: R.<x> = RDF['y']['x']\nsage: (x-1e123)*(x-1e100)\n 1.0*x^2 + 1e+223\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4055\n\n",
    "created_at": "2008-09-04T00:06:57Z",
    "labels": [
        "algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "serious bug in polynomial multiplication",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4055",
    "user": "robertwb"
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

archive/issue_comments_029227.json:
```json
{
    "body": "I believe this got fixed by Tom Boothby at Sage Days 12, see #3056.  I'm ccing him so he can react.  In any case, this looks fine now:\n\n\n```\n[ghitza@artin ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: R.<x> = RR[]\nsage: sage: (x-1e16)*(x-1e17)\n1.00000000000000*x^2 - 1.10000000000000e17*x + 1.00000000000000e33\nsage: sage: R.<x> = RDF['y']['x']\nsage: sage: (x-1e123)*(x-1e100)\n1.0*x^2 + (-1e+123)*x + 1e+223\n```\n",
    "created_at": "2009-01-28T21:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4055#issuecomment-29227",
    "user": "AlexGhitza"
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

archive/issue_comments_029228.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-22T02:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4055#issuecomment-29228",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029229.json:
```json
{
    "body": "Fixed via #3056.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T02:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4055#issuecomment-29229",
    "user": "mabshoff"
}
```

Fixed via #3056.

Cheers,

Michael
