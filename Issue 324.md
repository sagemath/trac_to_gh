# Issue 324: NTL builds in 32-bit mode on G5 powerpc

archive/issues_000324.json:
```json
{
    "body": "Assignee: @williamstein\n\nI'm just building sage on a dual core G5 powerpc and noticed that NTL seems to get built in 32-bit mode, even though it's a 64-bit machine... here's part of the build log:\n\n\n```\nThis is NTL version 5.4\n\nGOOD NEWS: compatible machine.\nsummary of machine characteristics:\nbits per long = 32\nbits per int = 32\nbits per size_t = 32\narith right shift = yes\ndouble precision = 53\nNBITS (maximum) = 30\nsingle mul ok = yes\nregister double precision = 53\ndouble rounding detected = no\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/324\n\n",
    "created_at": "2007-03-20T15:57:14Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "title": "NTL builds in 32-bit mode on G5 powerpc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/324",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

I'm just building sage on a dual core G5 powerpc and noticed that NTL seems to get built in 32-bit mode, even though it's a 64-bit machine... here's part of the build log:


```
This is NTL version 5.4

GOOD NEWS: compatible machine.
summary of machine characteristics:
bits per long = 32
bits per int = 32
bits per size_t = 32
arith right shift = yes
double precision = 53
NBITS (maximum) = 30
single mul ok = yes
register double precision = 53
double rounding detected = no
```



Issue created by migration from https://trac.sagemath.org/ticket/324





---

archive/issue_events_000346.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-03-21T22:40:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/324#event-346"
}
```



---

archive/issue_comments_001532.json:
```json
{
    "body": "All of SAGE (and pretty much everything else) gets built in 32-bit mode under OSX, since OS X is a 32-bit OS.  When Leopard comes out (OS X 10.5) this is supposed to change.  There was a lot of  discussion of this on the sage-devel list, especially by Jason Martin, who made a heroic but ultimately failed attempt to build SAGE 64-bit on OS X.",
    "created_at": "2007-03-21T22:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/324#issuecomment-1532",
    "user": "https://github.com/williamstein"
}
```

All of SAGE (and pretty much everything else) gets built in 32-bit mode under OSX, since OS X is a 32-bit OS.  When Leopard comes out (OS X 10.5) this is supposed to change.  There was a lot of  discussion of this on the sage-devel list, especially by Jason Martin, who made a heroic but ultimately failed attempt to build SAGE 64-bit on OS X.



---

archive/issue_comments_001533.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-21T22:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/324#issuecomment-1533",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid
