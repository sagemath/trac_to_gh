# Issue 2130: Question about list( FACTORS) command

archive/issues_002130.json:
```json
{
    "body": "Assignee: @malb\n\nGiven a factorization of a polynomial formed by ans.factor(); list(ans.factor()) does not change * symbols to commas, but ignores constants.\n\n\n```\nsage: t = PolynomialRing(QQ,'t',20).gens();\nans =  -t[1]^4*t[10]^3*t[13]*t[12] + t[1]^4*t[10]^2*t[12] + t[1]^2*t[11]*t[10]^2*t[13]*t[12] + t[1]^2*t[10]^2*t[13] - t[1]^2*t[11]*t[10]*t[12] - t[1]^2*t[10] - t[11]*t[10]*t[13] + t[11]; ans;\nfactt = ans.factor(); factt\n\n(-1) * (x0*x3 - 1) * (t1^2*x0 - x1) * (t1^2*x0*x2 - 1)\n```\n\n\n\n``` \nsage: list(factt)\n[(x0*x3 - 1, 1), (t1^2*x0 - x1, 1), (t1^2*x0*x2 - 1, 1)]\n```\n\n\nCan this be corrected, or is there a different command I can use?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2130\n\n",
    "created_at": "2008-02-09T20:04:40Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Question about list( FACTORS) command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2130",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoose05"
}
```
Assignee: @malb

Given a factorization of a polynomial formed by ans.factor(); list(ans.factor()) does not change * symbols to commas, but ignores constants.


```
sage: t = PolynomialRing(QQ,'t',20).gens();
ans =  -t[1]^4*t[10]^3*t[13]*t[12] + t[1]^4*t[10]^2*t[12] + t[1]^2*t[11]*t[10]^2*t[13]*t[12] + t[1]^2*t[10]^2*t[13] - t[1]^2*t[11]*t[10]*t[12] - t[1]^2*t[10] - t[11]*t[10]*t[13] + t[11]; ans;
factt = ans.factor(); factt

(-1) * (x0*x3 - 1) * (t1^2*x0 - x1) * (t1^2*x0*x2 - 1)
```



``` 
sage: list(factt)
[(x0*x3 - 1, 1), (t1^2*x0 - x1, 1), (t1^2*x0*x2 - 1, 1)]
```


Can this be corrected, or is there a different command I can use?


Issue created by migration from https://trac.sagemath.org/ticket/2130





---

archive/issue_comments_013945.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-09T22:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2130#issuecomment-13945",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002292.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2008-02-09T22:38:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2130",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2130#event-2292"
}
```



---

archive/issue_comments_013946.json:
```json
{
    "body": "Use `f.unit()`\n\n```\nsage:  t = PolynomialRing(QQ,'t',20).gens();\nsage: ans= -t[1]^4*t[10]^3*t[13]*t[12] + t[1]^4*t[10]^2*t[12] + t[1]^2*t[11]*t[10]^2*t[13]*t[12] + t[1]^2*t[10]^2*t[13] - t[1]^2*t[11]*t[10]*t[12] - t[1]^2*t[10] - t[11]*t[10]*t[13] + t[11]; ans;\nsage: f = ans.factor()\nsage: list(f)\n[(t10*t13 - 1, 1), (t1^2*t10 - t11, 1), (t1^2*t10*t12 - 1, 1)]\nsage: f.unit()\n-1\n```\n\n\nFor future reference this should have been a question asked in sage-support, not a trac ticket.",
    "created_at": "2008-02-09T22:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2130#issuecomment-13946",
    "user": "https://github.com/williamstein"
}
```

Use `f.unit()`

```
sage:  t = PolynomialRing(QQ,'t',20).gens();
sage: ans= -t[1]^4*t[10]^3*t[13]*t[12] + t[1]^4*t[10]^2*t[12] + t[1]^2*t[11]*t[10]^2*t[13]*t[12] + t[1]^2*t[10]^2*t[13] - t[1]^2*t[11]*t[10]*t[12] - t[1]^2*t[10] - t[11]*t[10]*t[13] + t[11]; ans;
sage: f = ans.factor()
sage: list(f)
[(t10*t13 - 1, 1), (t1^2*t10 - t11, 1), (t1^2*t10*t12 - 1, 1)]
sage: f.unit()
-1
```


For future reference this should have been a question asked in sage-support, not a trac ticket.
