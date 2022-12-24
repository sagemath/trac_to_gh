# Issue 1783: fix latex errors with fraction field elements

archive/issues_001783.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nsage:             sage: R = PolynomialRing(QQ, 'x').fraction_field()\nsage:             sage: x = R.gen()\nsage:             sage: a = 1/x\nsage:             sage: a._FractionFieldElement__numerator = R(0)\nsage:             sage: latex(a)\n\\frac{0}{x}\n```\n\n\nIt should instead give 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1783\n\n",
    "created_at": "2008-01-15T19:06:52Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "title": "fix latex errors with fraction field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1783",
    "user": "mhansen"
}
```
Assignee: malb


```
sage:             sage: R = PolynomialRing(QQ, 'x').fraction_field()
sage:             sage: x = R.gen()
sage:             sage: a = 1/x
sage:             sage: a._FractionFieldElement__numerator = R(0)
sage:             sage: latex(a)
\frac{0}{x}
```


It should instead give 0.

Issue created by migration from https://trac.sagemath.org/ticket/1783





---

archive/issue_comments_011288.json:
```json
{
    "body": "Attachment [1783.patch](tarball://root/attachments/some-uuid/ticket1783/1783.patch) by mhansen created at 2008-01-15 19:08:09",
    "created_at": "2008-01-15T19:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11288",
    "user": "mhansen"
}
```

Attachment [1783.patch](tarball://root/attachments/some-uuid/ticket1783/1783.patch) by mhansen created at 2008-01-15 19:08:09



---

archive/issue_comments_011289.json:
```json
{
    "body": "Attachment [1783-doctests.patch](tarball://root/attachments/some-uuid/ticket1783/1783-doctests.patch) by mhansen created at 2008-01-15 19:22:39",
    "created_at": "2008-01-15T19:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11289",
    "user": "mhansen"
}
```

Attachment [1783-doctests.patch](tarball://root/attachments/some-uuid/ticket1783/1783-doctests.patch) by mhansen created at 2008-01-15 19:22:39



---

archive/issue_comments_011290.json:
```json
{
    "body": "This should go in.",
    "created_at": "2008-01-15T19:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11290",
    "user": "ncalexan"
}
```

This should go in.



---

archive/issue_comments_011291.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T19:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11291",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011292.json:
```json
{
    "body": "Both patches merged in Sage 2.10.alpha4",
    "created_at": "2008-01-15T19:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11292",
    "user": "mabshoff"
}
```

Both patches merged in Sage 2.10.alpha4
