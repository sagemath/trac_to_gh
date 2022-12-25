# Issue 4263: elliptic curves -- point height serious stupid bug in raising error

archive/issues_004263.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is dumb (first thing I tried broke):\n\n```\nsage: E = EllipticCurve('5077a1')\nsage: F = E.change_ring(QuadraticField(-3,'a'))\nsage: P = F([-2,3,1])\nsage: s = P.height(); s\nsage: type(s)\n<type 'NoneType'>\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4263\n\n",
    "created_at": "2008-10-11T08:46:08Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "elliptic curves -- point height serious stupid bug in raising error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4263",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is dumb (first thing I tried broke):

```
sage: E = EllipticCurve('5077a1')
sage: F = E.change_ring(QuadraticField(-3,'a'))
sage: P = F([-2,3,1])
sage: s = P.height(); s
sage: type(s)
<type 'NoneType'>
```




Issue created by migration from https://trac.sagemath.org/ticket/4263





---

archive/issue_comments_031028.json:
```json
{
    "body": "Attachment [sage-4263.patch](tarball://root/attachments/some-uuid/ticket4263/sage-4263.patch) by @williamstein created at 2008-10-11 08:51:49",
    "created_at": "2008-10-11T08:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4263#issuecomment-31028",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4263.patch](tarball://root/attachments/some-uuid/ticket4263/sage-4263.patch) by @williamstein created at 2008-10-11 08:51:49



---

archive/issue_comments_031029.json:
```json
{
    "body": "looks good to me.",
    "created_at": "2008-10-11T10:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4263#issuecomment-31029",
    "user": "https://github.com/malb"
}
```

looks good to me.



---

archive/issue_comments_031030.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-11T12:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4263#issuecomment-31030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031031.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-11T12:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4263#issuecomment-31031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.rc0
