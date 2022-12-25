# Issue 2408: MPolynomial_libsingular.factor does not set units

archive/issues_002408.json:
```json
{
    "body": "Assignee: @malb\n\nMPolynomial_libsingular.factor does not set units.\n\nWe now have\n\n```\nsage: R.<x,y,z> = QQ[]\nsage: p = -1*(x*y+z)  \nsage: F = p.factor(); F\n(-1) * (x*y + z)\nsage: F.unit()\n1\nsage: len(F)\n2\n```\n\nIt should be\n\n```\nsage: F = p.factor(); F\nx*y + z\nsage: F.unit()\n-1\nsage: len(F)\n1\n\nIssue created by migration from https://trac.sagemath.org/ticket/2408\n\n",
    "closed_at": "2008-03-06T18:07:03Z",
    "created_at": "2008-03-06T17:36:30Z",
    "labels": [
        "component: commutative algebra",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "MPolynomial_libsingular.factor does not set units",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2408",
    "user": "https://github.com/burcin"
}
```
Assignee: @malb

MPolynomial_libsingular.factor does not set units.

We now have

```
sage: R.<x,y,z> = QQ[]
sage: p = -1*(x*y+z)  
sage: F = p.factor(); F
(-1) * (x*y + z)
sage: F.unit()
1
sage: len(F)
2
```

It should be

```
sage: F = p.factor(); F
x*y + z
sage: F.unit()
-1
sage: len(F)
1

Issue created by migration from https://trac.sagemath.org/ticket/2408





---

archive/issue_comments_016227.json:
```json
{
    "body": "This works on 2.10.2, I was using 2.10 at the time. Sorry for the noise.",
    "created_at": "2008-03-06T18:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2408#issuecomment-16227",
    "user": "https://github.com/burcin"
}
```

This works on 2.10.2, I was using 2.10 at the time. Sorry for the noise.



---

archive/issue_events_005680.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2008-03-06T18:07:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2408",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2408#event-5680"
}
```



---

archive/issue_comments_016228.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-06T18:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2408#issuecomment-16228",
    "user": "https://github.com/burcin"
}
```

Resolution: invalid
