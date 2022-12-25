# Issue 1783: [with patch, with positive review] fix latex errors with fraction field elements

archive/issues_001783.json:
```json
{
    "body": "Assignee: @malb\n\n```\nsage:             sage: R = PolynomialRing(QQ, 'x').fraction_field()\nsage:             sage: x = R.gen()\nsage:             sage: a = 1/x\nsage:             sage: a._FractionFieldElement__numerator = R(0)\nsage:             sage: latex(a)\n\\frac{0}{x}\n```\n\nIt should instead give 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1783\n\n",
    "closed_at": "2008-01-15T19:47:56Z",
    "created_at": "2008-01-15T19:06:52Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, with positive review] fix latex errors with fraction field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1783",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @malb

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

archive/issue_comments_011260.json:
```json
{
    "body": "Attachment [1783.patch](tarball://root/attachments/some-uuid/ticket1783/1783.patch) by @mwhansen created at 2008-01-15 19:08:09",
    "created_at": "2008-01-15T19:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11260",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1783.patch](tarball://root/attachments/some-uuid/ticket1783/1783.patch) by @mwhansen created at 2008-01-15 19:08:09



---

archive/issue_comments_011261.json:
```json
{
    "body": "Attachment [1783-doctests.patch](tarball://root/attachments/some-uuid/ticket1783/1783-doctests.patch) by @mwhansen created at 2008-01-15 19:22:39",
    "created_at": "2008-01-15T19:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11261",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1783-doctests.patch](tarball://root/attachments/some-uuid/ticket1783/1783-doctests.patch) by @mwhansen created at 2008-01-15 19:22:39



---

archive/issue_comments_011262.json:
```json
{
    "body": "This should go in.",
    "created_at": "2008-01-15T19:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11262",
    "user": "https://github.com/ncalexan"
}
```

This should go in.



---

archive/issue_comments_011263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T19:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11263",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004358.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-15T19:47:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1783#event-4358"
}
```



---

archive/issue_comments_011264.json:
```json
{
    "body": "Both patches merged in Sage 2.10.alpha4",
    "created_at": "2008-01-15T19:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1783#issuecomment-11264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Both patches merged in Sage 2.10.alpha4
