# Issue 926: [with patch] MPolynomial Iterator

archive/issues_000926.json:
```json
{
    "body": "Assignee: @robertwb\n\nSAGE should support iterating over sparse multivariate polynomials like this:\n\n```\nsage: P.<x,y,z> = PolynomialRing(QQ,3)\nsage: f= 3*x^3*y + 16*x + 7\nsage: for c,m in f:\n....:     print c,m\n....:\n3, x^3*y\n16, x\n7,1\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/926\n\n",
    "closed_at": "2007-10-21T03:24:11Z",
    "created_at": "2007-10-19T09:59:18Z",
    "labels": [
        "component: commutative algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "[with patch] MPolynomial Iterator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/926",
    "user": "https://github.com/malb"
}
```
Assignee: @robertwb

SAGE should support iterating over sparse multivariate polynomials like this:

```
sage: P.<x,y,z> = PolynomialRing(QQ,3)
sage: f= 3*x^3*y + 16*x + 7
sage: for c,m in f:
....:     print c,m
....:
3, x^3*y
16, x
7,1
```

Issue created by migration from https://trac.sagemath.org/ticket/926





---

archive/issue_comments_005656.json:
```json
{
    "body": "Changing assignee from @malb to @robertwb.",
    "created_at": "2007-10-20T20:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/926#issuecomment-5656",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @malb to @robertwb.



---

archive/issue_comments_005657.json:
```json
{
    "body": "Attachment [926.diff](tarball://root/attachments/some-uuid/ticket926/926.diff) by @robertwb created at 2007-10-20 20:25:27",
    "created_at": "2007-10-20T20:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/926#issuecomment-5657",
    "user": "https://github.com/robertwb"
}
```

Attachment [926.diff](tarball://root/attachments/some-uuid/ticket926/926.diff) by @robertwb created at 2007-10-20 20:25:27



---

archive/issue_events_002543.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T03:24:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/926#event-2543"
}
```



---

archive/issue_comments_005658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T03:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/926#issuecomment-5658",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
