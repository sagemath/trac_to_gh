# Issue 7088: factoring certain polynomials over ZZ gets all mixed up (wrong constant) via our PARI wrapper

archive/issues_007088.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nHi all,\n\nFound this simple bug in a simple Z[x] factoring example.\n\nR.<x>=PolynomialRing(ZZ)\nf = 12*x^10 + x^9 + 432*x^3 + 9011\ng = 13*x^11 + 89*x^3 + 1\nF = f^2 * g^3\nG = F.factor()\nshould_be_zero = F - G.prod()\nshould_be_zero == 0\n\nThe problem was that F.factor returns\n\n2028 * (12*x^10 + x^9 + 432*x^3 + 9011)^2 * (13*x^11 + 89*x^3 + 1)^3\n\nNot 1 * (12*x^10 + x^9 + 432*x^3 + 9011)^2 * (13*x^11 + 89*x^3 + 1)^3\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7088\n\n",
    "created_at": "2009-10-01T03:23:39Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "factoring certain polynomials over ZZ gets all mixed up (wrong constant) via our PARI wrapper",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7088",
    "user": "@williamstein"
}
```
Assignee: somebody


```
Hi all,

Found this simple bug in a simple Z[x] factoring example.

R.<x>=PolynomialRing(ZZ)
f = 12*x^10 + x^9 + 432*x^3 + 9011
g = 13*x^11 + 89*x^3 + 1
F = f^2 * g^3
G = F.factor()
should_be_zero = F - G.prod()
should_be_zero == 0

The problem was that F.factor returns

2028 * (12*x^10 + x^9 + 432*x^3 + 9011)^2 * (13*x^11 + 89*x^3 + 1)^3

Not 1 * (12*x^10 + x^9 + 432*x^3 + 9011)^2 * (13*x^11 + 89*x^3 + 1)^3

```


Issue created by migration from https://trac.sagemath.org/ticket/7088





---

archive/issue_comments_058584.json:
```json
{
    "body": "Changing assignee from somebody to @robertwb.",
    "created_at": "2009-10-01T06:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7088#issuecomment-58584",
    "user": "@robertwb"
}
```

Changing assignee from somebody to @robertwb.



---

archive/issue_comments_058585.json:
```json
{
    "body": "Attachment [7088-poly-factor-bug.patch](tarball://root/attachments/some-uuid/ticket7088/7088-poly-factor-bug.patch) by @mwhansen created at 2009-10-01 07:47:59",
    "created_at": "2009-10-01T07:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7088#issuecomment-58585",
    "user": "@mwhansen"
}
```

Attachment [7088-poly-factor-bug.patch](tarball://root/attachments/some-uuid/ticket7088/7088-poly-factor-bug.patch) by @mwhansen created at 2009-10-01 07:47:59



---

archive/issue_comments_058586.json:
```json
{
    "body": "I attached a patch with a one character change: ( TESTS:: to TESTS:).\n\nOther than that, it looks good to me.",
    "created_at": "2009-10-01T07:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7088#issuecomment-58586",
    "user": "@mwhansen"
}
```

I attached a patch with a one character change: ( TESTS:: to TESTS:).

Other than that, it looks good to me.



---

archive/issue_comments_058587.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-02T17:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7088#issuecomment-58587",
    "user": "@williamstein"
}
```

Resolution: fixed
