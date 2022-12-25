# Issue 1112: [with patch] Integer.__pow__

archive/issues_001112.json:
```json
{
    "body": "Assignee: somebody\n\nthe attached patch makes this work:\n\n```\nsage: pow(10,20,17)\n4\nsage: pow?\n    pow(x, y[, z]) -> number\n\n    With two arguments, equivalent to x**y.  With three arguments,\n    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).\n```\n\nthis is required such that e.g. the Crypto.RSA module works with SAGE integers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1112\n\n",
    "closed_at": "2007-11-06T22:14:12Z",
    "created_at": "2007-11-06T16:22:17Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] Integer.__pow__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1112",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

the attached patch makes this work:

```
sage: pow(10,20,17)
4
sage: pow?
    pow(x, y[, z]) -> number

    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
```

this is required such that e.g. the Crypto.RSA module works with SAGE integers.

Issue created by migration from https://trac.sagemath.org/ticket/1112





---

archive/issue_comments_006703.json:
```json
{
    "body": "Attachment [pow.patch](tarball://root/attachments/some-uuid/ticket1112/pow.patch) by @malb created at 2007-11-06 16:22:27",
    "created_at": "2007-11-06T16:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1112#issuecomment-6703",
    "user": "https://github.com/malb"
}
```

Attachment [pow.patch](tarball://root/attachments/some-uuid/ticket1112/pow.patch) by @malb created at 2007-11-06 16:22:27



---

archive/issue_comments_006704.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1112#issuecomment-6704",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006705.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1112#issuecomment-6705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_events_002979.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T22:14:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1112#event-2979"
}
```
