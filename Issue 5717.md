# Issue 5717: subdivide and matrices mod 2 -- printing broken

archive/issues_005717.json:
```json
{
    "body": "Assignee: @williamstein\n\nPrinting of subdivisions of matrices mod 2 is broken.  Also, lifting of matrices should preserve subdivision but doesn't, but that's a separate ticket (#5716)\n\n```\nsage: a = random_matrix(GF(2),4)\nsage: a.subdivide(2,2)\nsage: a\n[1 0 1 0]\n[1 0 1 0]\n[1 1 1 1]\n[1 1 0 1]\nsage: b = a.lift()\nsage: b.subdivide(2,2)\nsage: b\n[1 0|1 0]\n[1 0|1 0]\n[---+---]\n[1 1|1 1]\n[1 1|0 1]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5717\n\n",
    "created_at": "2009-04-08T19:19:01Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "subdivide and matrices mod 2 -- printing broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5717",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Printing of subdivisions of matrices mod 2 is broken.  Also, lifting of matrices should preserve subdivision but doesn't, but that's a separate ticket (#5716)

```
sage: a = random_matrix(GF(2),4)
sage: a.subdivide(2,2)
sage: a
[1 0 1 0]
[1 0 1 0]
[1 1 1 1]
[1 1 0 1]
sage: b = a.lift()
sage: b.subdivide(2,2)
sage: b
[1 0|1 0]
[1 0|1 0]
[---+---]
[1 1|1 1]
[1 1|0 1]
```

Issue created by migration from https://trac.sagemath.org/ticket/5717





---

archive/issue_comments_044597.json:
```json
{
    "body": "This is a dup of #5714.",
    "created_at": "2009-04-08T19:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5717#issuecomment-44597",
    "user": "https://github.com/williamstein"
}
```

This is a dup of #5714.



---

archive/issue_comments_044598.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-08T19:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5717#issuecomment-44598",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_013421.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-04-08T19:20:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5717#event-13421"
}
```
