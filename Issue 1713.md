# Issue 1713: [with patch] fix SageElement._sage_

archive/issues_001713.json:
```json
{
    "body": "Assignee: @malb\n\nThis didn't work, now it does:\n\n\n```\nsage: sr = mq.SR(allow_zero_inversions=True)\nsage: F,s = sr.polynomial_system()\nsage: F == sage0(F)._sage_()\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1713\n\n",
    "created_at": "2008-01-07T14:01:39Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch] fix SageElement._sage_",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1713",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

This didn't work, now it does:


```
sage: sr = mq.SR(allow_zero_inversions=True)
sage: F,s = sr.polynomial_system()
sage: F == sage0(F)._sage_()
True
```


Issue created by migration from https://trac.sagemath.org/ticket/1713





---

archive/issue_comments_010833.json:
```json
{
    "body": "Attachment [SageElement_sage_.patch](tarball://root/attachments/some-uuid/ticket1713/SageElement_sage_.patch) by @malb created at 2008-01-17 12:46:58",
    "created_at": "2008-01-17T12:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1713#issuecomment-10833",
    "user": "https://github.com/malb"
}
```

Attachment [SageElement_sage_.patch](tarball://root/attachments/some-uuid/ticket1713/SageElement_sage_.patch) by @malb created at 2008-01-17 12:46:58



---

archive/issue_comments_010834.json:
```json
{
    "body": "Works for me.",
    "created_at": "2008-01-20T23:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1713#issuecomment-10834",
    "user": "https://github.com/mwhansen"
}
```

Works for me.



---

archive/issue_comments_010835.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T02:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1713#issuecomment-10835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_010836.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T02:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1713#issuecomment-10836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
