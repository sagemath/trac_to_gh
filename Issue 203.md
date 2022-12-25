# Issue 203: more elliptic curve n*P problems

archive/issues_000203.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nArgh!  Curves over extension fields don't work?\n \nsage: E\nElliptic Curve defined by y^2  = x^3 + x over Finite Field in a of size 5^2\n \nsage: P\n(a : 2*a + 4 : 1)\n \nsage: P+P+P+P+P\n(2*a + 3 : 2*a : 1)\n \nsage: 5*P\n(0 : 1 : 0)\n\n \nsage: 5*P\n(0 : 1 : 0)\n \nsage: P*5\n(2*a + 3 : 2*a : 1)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/203\n\n",
    "created_at": "2007-01-21T03:44:16Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.9",
    "title": "more elliptic curve n*P problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/203",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
Argh!  Curves over extension fields don't work?
 
sage: E
Elliptic Curve defined by y^2  = x^3 + x over Finite Field in a of size 5^2
 
sage: P
(a : 2*a + 4 : 1)
 
sage: P+P+P+P+P
(2*a + 3 : 2*a : 1)
 
sage: 5*P
(0 : 1 : 0)

 
sage: 5*P
(0 : 1 : 0)
 
sage: P*5
(2*a + 3 : 2*a : 1)
```

Issue created by migration from https://trac.sagemath.org/ticket/203





---

archive/issue_comments_000912.json:
```json
{
    "body": "This is caused because\n\n  P.parent().base() \n\nis the finite field instead of ZZ.  But that base is supposed to be\nthe base ring for the module that P is in!  Ouch.\n\nWilliam",
    "created_at": "2007-01-23T22:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/203#issuecomment-912",
    "user": "https://github.com/williamstein"
}
```

This is caused because

  P.parent().base() 

is the finite field instead of ZZ.  But that base is supposed to be
the base ring for the module that P is in!  Ouch.

William



---

archive/issue_comments_000913.json:
```json
{
    "body": "Fixed for sage > 1.8.  Actually pretty subtle to fix...",
    "created_at": "2007-01-23T23:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/203#issuecomment-913",
    "user": "https://github.com/williamstein"
}
```

Fixed for sage > 1.8.  Actually pretty subtle to fix...



---

archive/issue_comments_000914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-23T23:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/203#issuecomment-914",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000406.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-23T23:30:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/203",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/203#event-406"
}
```
