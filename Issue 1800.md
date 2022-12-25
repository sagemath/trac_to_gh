# Issue 1800: bug with RealIntervalField / MPFI

archive/issues_001800.json:
```json
{
    "body": "Assignee: jkantor\n\n\n```\nsage: a = factorial(100)/exp(2)\nsage: bits = 427; RealIntervalField(bits)(a).upper() - RealIntervalField(bits)(a).lower()\n7.9228162514264337593543950336000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e28\nsage: bits = 428; RealIntervalField(bits)(a).upper() - RealIntervalField(bits)(a).lower()\n0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1800\n\n",
    "created_at": "2008-01-17T06:08:25Z",
    "labels": [
        "component: numerical",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "bug with RealIntervalField / MPFI",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1800",
    "user": "https://github.com/mwhansen"
}
```
Assignee: jkantor


```
sage: a = factorial(100)/exp(2)
sage: bits = 427; RealIntervalField(bits)(a).upper() - RealIntervalField(bits)(a).lower()
7.9228162514264337593543950336000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e28
sage: bits = 428; RealIntervalField(bits)(a).upper() - RealIntervalField(bits)(a).lower()
0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```


Issue created by migration from https://trac.sagemath.org/ticket/1800





---

archive/issue_comments_011356.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-17T07:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11356",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011357.json:
```json
{
    "body": "Changing assignee from jkantor to cwitty.",
    "created_at": "2008-01-17T07:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11357",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from jkantor to cwitty.



---

archive/issue_comments_011358.json:
```json
{
    "body": "It looks like coercion from symbolic expressions to intervals is broken (because nobody ever wrote the code to do it, and the generic code that happens to be used doesn't work).",
    "created_at": "2008-01-17T07:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11358",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

It looks like coercion from symbolic expressions to intervals is broken (because nobody ever wrote the code to do it, and the generic code that happens to be used doesn't work).



---

archive/issue_comments_011359.json:
```json
{
    "body": "Attachment [trac-1800.patch](tarball://root/attachments/some-uuid/ticket1800/trac-1800.patch) by cwitty created at 2008-01-19 14:53:31",
    "created_at": "2008-01-19T14:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11359",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-1800.patch](tarball://root/attachments/some-uuid/ticket1800/trac-1800.patch) by cwitty created at 2008-01-19 14:53:31



---

archive/issue_comments_011360.json:
```json
{
    "body": "Solution seems correct.",
    "created_at": "2008-01-19T18:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11360",
    "user": "https://github.com/ncalexan"
}
```

Solution seems correct.



---

archive/issue_comments_011361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T19:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004399.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-19T19:56:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1800#event-4399"
}
```



---

archive/issue_comments_011362.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-19T19:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1800#issuecomment-11362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0
