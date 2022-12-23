# Issue 419: row reduction for matrices over multivariate polynomial rings

archive/issues_000419.json:
```json
{
    "body": "Assignee: was\n\nConsider\n\n\n```\nsage: P.<x,y> = PolynomialRing(GF(2),2)\nsage: A = Matrix(P,2,2,[1,x,x,x+1]); A\n\n[    1     x]\n[    x x + 1]\n\n```\n\n\n`A.echelon_form()` returns the identity matrix because it computes the reduced echelon form over a fraction field and not over the polynomial ring.  However, SINGULAR has a (educational == slow) `rowred` command to perform row reduction as far as this is possible over the polynomial ring. This behaviour is desired in several applications and thus it should be ported to SAGE.\n\nIn fact, I've got an implementation/port of this already (c.f. https://sage.math.washington.edu:8102/home/pub/35/) it just needs to be named and included with SAGE.\n\nIssue created by migration from https://trac.sagemath.org/ticket/419\n\n",
    "created_at": "2007-08-10T15:26:18Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "row reduction for matrices over multivariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/419",
    "user": "malb"
}
```
Assignee: was

Consider


```
sage: P.<x,y> = PolynomialRing(GF(2),2)
sage: A = Matrix(P,2,2,[1,x,x,x+1]); A

[    1     x]
[    x x + 1]

```


`A.echelon_form()` returns the identity matrix because it computes the reduced echelon form over a fraction field and not over the polynomial ring.  However, SINGULAR has a (educational == slow) `rowred` command to perform row reduction as far as this is possible over the polynomial ring. This behaviour is desired in several applications and thus it should be ported to SAGE.

In fact, I've got an implementation/port of this already (c.f. https://sage.math.washington.edu:8102/home/pub/35/) it just needs to be named and included with SAGE.

Issue created by migration from https://trac.sagemath.org/ticket/419





---

archive/issue_comments_002108.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-10T19:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/419#issuecomment-2108",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002109.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2007-08-10T19:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/419#issuecomment-2109",
    "user": "malb"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_002110.json:
```json
{
    "body": "fixed in 2.8.3",
    "created_at": "2007-09-03T13:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/419#issuecomment-2110",
    "user": "malb"
}
```

fixed in 2.8.3



---

archive/issue_comments_002111.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-03T13:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/419#issuecomment-2111",
    "user": "malb"
}
```

Resolution: fixed
