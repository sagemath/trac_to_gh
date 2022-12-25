# Issue 1873: [with patch, with positive review] elementary function expansion returns result in the wrong ring

archive/issues_001873.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nI'm using Sage 2.10 now. Expansion for elements in SFAElementary works\ngreat now, but there is another problem: the expansion lies in the\nwrong ring.\n\n```\nsage: e=SFAElementary(QQ)\nsage: f=e([2]).expand(2)\nsage: f\nx0*x1\nsage: f.parent()\nMultivariate Polynomial Ring in x0, x1, x2 over Rational Field\n```\n\nThe same code but for SFASchur results in:\n\n```\nsage: s=SFASchur(QQ)\nsage: f=s([2]).expand(2)\nsage: f\nx0^2 + x0*x1 + x1^2\nsage: f.parent()\nMultivariate Polynomial Ring in x0, x1 over Rational Field\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1873\n\n",
    "closed_at": "2008-01-23T04:06:25Z",
    "created_at": "2008-01-20T22:22:55Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, with positive review] elementary function expansion returns result in the wrong ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1873",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat

I'm using Sage 2.10 now. Expansion for elements in SFAElementary works
great now, but there is another problem: the expansion lies in the
wrong ring.

```
sage: e=SFAElementary(QQ)
sage: f=e([2]).expand(2)
sage: f
x0*x1
sage: f.parent()
Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
```

The same code but for SFASchur results in:

```
sage: s=SFASchur(QQ)
sage: f=s([2]).expand(2)
sage: f
x0^2 + x0*x1 + x1^2
sage: f.parent()
Multivariate Polynomial Ring in x0, x1 over Rational Field
```

Issue created by migration from https://trac.sagemath.org/ticket/1873





---

archive/issue_comments_011832.json:
```json
{
    "body": "Attachment [1873.patch](tarball://root/attachments/some-uuid/ticket1873/1873.patch) by @mwhansen created at 2008-01-20 22:27:07",
    "created_at": "2008-01-20T22:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11832",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1873.patch](tarball://root/attachments/some-uuid/ticket1873/1873.patch) by @mwhansen created at 2008-01-20 22:27:07



---

archive/issue_comments_011833.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T22:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11833",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011834.json:
```json
{
    "body": "Looks fine to me, and appears to fix the ticket.\n\nmhansen has the super-commit-bit in this area anyway, in my opinion :)",
    "created_at": "2008-01-22T19:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11834",
    "user": "https://github.com/ncalexan"
}
```

Looks fine to me, and appears to fix the ticket.

mhansen has the super-commit-bit in this area anyway, in my opinion :)



---

archive/issue_comments_011835.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-23T04:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011836.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-23T04:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_events_004523.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-23T04:06:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1873#event-4523"
}
```
