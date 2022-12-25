# Issue 3066: empty matrices: gram_schmidt() throws a NameError

archive/issues_003066.json:
```json
{
    "body": "Assignee: @williamstein\n\nLooks like an explicit import is the only thing missing on this one:\n\n\n```\nsage: a = matrix([])\nsage: m.gram_schmidt()\n<type 'exceptions.NameError'>: global name 'ZZ' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3066\n\n",
    "created_at": "2008-04-30T15:20:39Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "empty matrices: gram_schmidt() throws a NameError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3066",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein

Looks like an explicit import is the only thing missing on this one:


```
sage: a = matrix([])
sage: m.gram_schmidt()
<type 'exceptions.NameError'>: global name 'ZZ' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/3066





---

archive/issue_comments_021120.json:
```json
{
    "body": "Attachment [3066.patch](tarball://root/attachments/some-uuid/ticket3066/3066.patch) by @dfdeshom created at 2008-04-30 17:35:01",
    "created_at": "2008-04-30T17:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21120",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [3066.patch](tarball://root/attachments/some-uuid/ticket3066/3066.patch) by @dfdeshom created at 2008-04-30 17:35:01



---

archive/issue_comments_021121.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2008-04-30T17:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21121",
    "user": "https://github.com/dfdeshom"
}
```

Patch attached.



---

archive/issue_comments_021122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021123.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3066#issuecomment-21123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_events_006935.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-01T05:47:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3066",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3066#event-6935"
}
```
