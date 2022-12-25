# Issue 3063: empty matrices: norm() returns a ValueError

archive/issues_003063.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: a = matrix([])\n\nsage: a.norm()\n---------------------------------------------------------------------------\n\n<type 'exceptions.ValueError'>: max() arg is an empty sequence\n```\n\n\nI think the answer in this case should be 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3063\n\n",
    "created_at": "2008-04-30T15:10:44Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "empty matrices: norm() returns a ValueError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3063",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein


```
sage: a = matrix([])

sage: a.norm()
---------------------------------------------------------------------------

<type 'exceptions.ValueError'>: max() arg is an empty sequence
```


I think the answer in this case should be 0.

Issue created by migration from https://trac.sagemath.org/ticket/3063





---

archive/issue_comments_021104.json:
```json
{
    "body": "Attachment [3063.patch](tarball://root/attachments/some-uuid/ticket3063/3063.patch) by @dfdeshom created at 2008-04-30 17:54:13",
    "created_at": "2008-04-30T17:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21104",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [3063.patch](tarball://root/attachments/some-uuid/ticket3063/3063.patch) by @dfdeshom created at 2008-04-30 17:54:13



---

archive/issue_comments_021105.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2008-04-30T17:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21105",
    "user": "https://github.com/dfdeshom"
}
```

Patch attached.



---

archive/issue_comments_021106.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21106",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003273.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-01T05:46:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3063#event-3273"
}
```



---

archive/issue_comments_021107.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3063#issuecomment-21107",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
