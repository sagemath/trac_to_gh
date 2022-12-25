# Issue 1502: calculus -- bug in argument ordering for formal functions

archive/issues_001502.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is wrong:\n\n\n```\nsage: f = function('Gamma', var('z'), var('w')); f\nGamma(z, w)\nsage: f(2)\nGamma(z, 2)\nsage: f(2,5)\nGamma(5, 2)\n```\n\n\nIt should be\n\n\n```\nsage: f = function('Gamma', var('z'), var('w')); f\nGamma(z, w)\nsage: f(2)\nGamma(2, w)\nsage: f(2,5)\nGamma(2, 5)\n```\n\n\nNote that this works:\n\n\n```\nsage: f(z,w) = function('Gamma'); f\n(z, w) |--> Gamma(z, w)\nsage: f(2)\nGamma(2, w)\nsage: f(2,5)\nGamma(2, 5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1502\n\n",
    "created_at": "2007-12-14T05:41:19Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "calculus -- bug in argument ordering for formal functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1502",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is wrong:


```
sage: f = function('Gamma', var('z'), var('w')); f
Gamma(z, w)
sage: f(2)
Gamma(z, 2)
sage: f(2,5)
Gamma(5, 2)
```


It should be


```
sage: f = function('Gamma', var('z'), var('w')); f
Gamma(z, w)
sage: f(2)
Gamma(2, w)
sage: f(2,5)
Gamma(2, 5)
```


Note that this works:


```
sage: f(z,w) = function('Gamma'); f
(z, w) |--> Gamma(z, w)
sage: f(2)
Gamma(2, w)
sage: f(2,5)
Gamma(2, 5)
```


Issue created by migration from https://trac.sagemath.org/ticket/1502





---

archive/issue_comments_009602.json:
```json
{
    "body": "Attachment [1502.patch](tarball://root/attachments/some-uuid/ticket1502/1502.patch) by @mwhansen created at 2007-12-14 06:42:08",
    "created_at": "2007-12-14T06:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9602",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1502.patch](tarball://root/attachments/some-uuid/ticket1502/1502.patch) by @mwhansen created at 2007-12-14 06:42:08



---

archive/issue_comments_009603.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-14T06:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9603",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009604.json:
```json
{
    "body": "Apply after #553 .",
    "created_at": "2007-12-14T06:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9604",
    "user": "https://github.com/mwhansen"
}
```

Apply after #553 .



---

archive/issue_comments_009605.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-14T06:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9605",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_009606.json:
```json
{
    "body": "Was reviewed this positively in IRC during BD7. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-15T11:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Was reviewed this positively in IRC during BD7. 

Cheers,

Michael



---

archive/issue_comments_009607.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009608.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T12:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009609.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T12:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_001656.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T12:20:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1502#event-1656"
}
```
