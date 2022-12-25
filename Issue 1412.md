# Issue 1412: creating directory in notebook cell #x makes evaluation of cell #x hang

archive/issues_001412.json:
```json
{
    "body": "Assignee: @williamstein\n\nExecuting the following in a notebook cell works exactly once.  If one tries to re-evaluate the cell, an OSError is hit by the server, the evaluation never terminates nor does any work.\n\n\n```\nos.mkdir(\"tmp\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1412\n\n",
    "created_at": "2007-12-06T19:25:23Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "creating directory in notebook cell #x makes evaluation of cell #x hang",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1412",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @williamstein

Executing the following in a notebook cell works exactly once.  If one tries to re-evaluate the cell, an OSError is hit by the server, the evaluation never terminates nor does any work.


```
os.mkdir("tmp")
```


Issue created by migration from https://trac.sagemath.org/ticket/1412





---

archive/issue_comments_009082.json:
```json
{
    "body": "Attachment [trac-1412.patch](tarball://root/attachments/some-uuid/ticket1412/trac-1412.patch) by boothby created at 2007-12-06 21:01:03\n\npatch works for me",
    "created_at": "2007-12-06T21:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1412#issuecomment-9082",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac-1412.patch](tarball://root/attachments/some-uuid/ticket1412/trac-1412.patch) by boothby created at 2007-12-06 21:01:03

patch works for me



---

archive/issue_comments_009083.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T15:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1412#issuecomment-9083",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009084.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T15:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1412#issuecomment-9084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha2.



---

archive/issue_events_001560.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-09T15:08:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1412",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1412#event-1560"
}
```
