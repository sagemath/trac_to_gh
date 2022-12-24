# Issue 4707: magma/sage interface -- another trivial easy-to-fix failure hopefully

archive/issues_004707.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: E = EllipticCurve(GF(25,'a'), [0,0,1,4,0])\nsage: magma(E)\nboom\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4707\n\n",
    "created_at": "2008-12-05T02:28:26Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "magma/sage interface -- another trivial easy-to-fix failure hopefully",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4707",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: E = EllipticCurve(GF(25,'a'), [0,0,1,4,0])
sage: magma(E)
boom
```


Issue created by migration from https://trac.sagemath.org/ticket/4707





---

archive/issue_comments_035499.json:
```json
{
    "body": "Attachment [trac_4707.patch](tarball://root/attachments/some-uuid/ticket4707/trac_4707.patch) by @williamstein created at 2008-12-05 02:55:03",
    "created_at": "2008-12-05T02:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4707#issuecomment-35499",
    "user": "@williamstein"
}
```

Attachment [trac_4707.patch](tarball://root/attachments/some-uuid/ticket4707/trac_4707.patch) by @williamstein created at 2008-12-05 02:55:03



---

archive/issue_comments_035500.json:
```json
{
    "body": "Attachment [trac_4707_tiny_followup.patch](tarball://root/attachments/some-uuid/ticket4707/trac_4707_tiny_followup.patch) by @ncalexan created at 2008-12-06 23:49:58\n\nWorks for me.  Apply both patches.  We will open a separate ticket for the corresponding magma -> sage conversion.",
    "created_at": "2008-12-06T23:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4707#issuecomment-35500",
    "user": "@ncalexan"
}
```

Attachment [trac_4707_tiny_followup.patch](tarball://root/attachments/some-uuid/ticket4707/trac_4707_tiny_followup.patch) by @ncalexan created at 2008-12-06 23:49:58

Works for me.  Apply both patches.  We will open a separate ticket for the corresponding magma -> sage conversion.



---

archive/issue_comments_035501.json:
```json
{
    "body": "fix typo in title",
    "created_at": "2008-12-11T04:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4707#issuecomment-35501",
    "user": "@williamstein"
}
```

fix typo in title



---

archive/issue_comments_035502.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T11:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4707#issuecomment-35502",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.2.alpha2



---

archive/issue_comments_035503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T11:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4707#issuecomment-35503",
    "user": "mabshoff"
}
```

Resolution: fixed
