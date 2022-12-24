# Issue 926: MPolynomial Iterator

archive/issues_000926.json:
```json
{
    "body": "Assignee: malb\n\nSAGE should support iterating over sparse multivariate polynomials like this:\n\n```\nsage: P.<x,y,z> = PolynomialRing(QQ,3)\nsage: f= 3*x^3*y + 16*x + 7\nsage: for c,m in f:\n....:     print c,m\n....:\n3, x^3*y\n16, x\n7,1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/926\n\n",
    "created_at": "2007-10-19T09:59:18Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "title": "MPolynomial Iterator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/926",
    "user": "malb"
}
```
Assignee: malb

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

archive/issue_comments_005674.json:
```json
{
    "body": "Changing assignee from malb to robertwb.",
    "created_at": "2007-10-20T20:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/926#issuecomment-5674",
    "user": "robertwb"
}
```

Changing assignee from malb to robertwb.



---

archive/issue_comments_005675.json:
```json
{
    "body": "Attachment [926.diff](tarball://root/attachments/some-uuid/ticket926/926.diff) by robertwb created at 2007-10-20 20:25:27",
    "created_at": "2007-10-20T20:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/926#issuecomment-5675",
    "user": "robertwb"
}
```

Attachment [926.diff](tarball://root/attachments/some-uuid/ticket926/926.diff) by robertwb created at 2007-10-20 20:25:27



---

archive/issue_comments_005676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T03:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/926#issuecomment-5676",
    "user": "was"
}
```

Resolution: fixed
