# Issue 2055: [with patch, needs review] MPolynomialRing(BooleanPolynomial)

archive/issues_002055.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\n\n```\nsage: B.<x,y,z> = BooleanPolynomialRing(3)\nsage: P.<x,y,z> = MPolynomialRing(QQ,3)\nsage: P(B.gen(0))\nx\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2055\n\n",
    "created_at": "2008-02-05T15:09:15Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] MPolynomialRing(BooleanPolynomial)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2055",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @burcin


```
sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage: P.<x,y,z> = MPolynomialRing(QQ,3)
sage: P(B.gen(0))
x
```


Issue created by migration from https://trac.sagemath.org/ticket/2055





---

archive/issue_comments_013306.json:
```json
{
    "body": "Attachment [trac_2055_mpolyring_call.patch](tarball://root/attachments/some-uuid/ticket2055/trac_2055_mpolyring_call.patch) by @malb created at 2008-02-05 15:09:35",
    "created_at": "2008-02-05T15:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2055#issuecomment-13306",
    "user": "@malb"
}
```

Attachment [trac_2055_mpolyring_call.patch](tarball://root/attachments/some-uuid/ticket2055/trac_2055_mpolyring_call.patch) by @malb created at 2008-02-05 15:09:35



---

archive/issue_comments_013307.json:
```json
{
    "body": "fixes an exposed sigsegv in libsingular interface",
    "created_at": "2008-02-14T23:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2055#issuecomment-13307",
    "user": "@malb"
}
```

fixes an exposed sigsegv in libsingular interface



---

archive/issue_comments_013308.json:
```json
{
    "body": "Attachment [sigsegv.patch](tarball://root/attachments/some-uuid/ticket2055/sigsegv.patch) by @ncalexan created at 2008-02-14 23:36:14\n\nThis should be applied.\n\nThe `__call__` method is not as general as it could be.  See ticket #2165 for an enhancement.",
    "created_at": "2008-02-14T23:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2055#issuecomment-13308",
    "user": "@ncalexan"
}
```

Attachment [sigsegv.patch](tarball://root/attachments/some-uuid/ticket2055/sigsegv.patch) by @ncalexan created at 2008-02-14 23:36:14

This should be applied.

The `__call__` method is not as general as it could be.  See ticket #2165 for an enhancement.



---

archive/issue_comments_013309.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T00:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2055#issuecomment-13309",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013310.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T00:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2055#issuecomment-13310",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
