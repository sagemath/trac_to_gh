# Issue 6980: [with patch, positive review] add _nonzero_positions_by_column to sparse integer matrices

archive/issues_006980.json:
```json
{
    "body": "Assignee: @williamstein\n\nwe still use the dense version:\n\n```\nsage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()\nCPU times: user 5.12 s, sys: 0.01 s, total: 5.14 s\nWall time: 5.19 s\n[]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6980\n\n",
    "closed_at": "2009-09-25T06:32:20Z",
    "created_at": "2009-09-21T22:20:34Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] add _nonzero_positions_by_column to sparse integer matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6980",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @williamstein

we still use the dense version:

```
sage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()
CPU times: user 5.12 s, sys: 0.01 s, total: 5.14 s
Wall time: 5.19 s
[]
```

Issue created by migration from https://trac.sagemath.org/ticket/6980





---

archive/issue_comments_057621.json:
```json
{
    "body": "Attachment [trac6980_nonzero_positions_by_column.patch](tarball://root/attachments/some-uuid/ticket6980/trac6980_nonzero_positions_by_column.patch) by ylchapuy created at 2009-09-21 22:24:32\n\nAfter patching, we obtain what is expected:\n\n```\nsage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01 s\n[]\n```",
    "created_at": "2009-09-21T22:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6980#issuecomment-57621",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac6980_nonzero_positions_by_column.patch](tarball://root/attachments/some-uuid/ticket6980/trac6980_nonzero_positions_by_column.patch) by ylchapuy created at 2009-09-21 22:24:32

After patching, we obtain what is expected:

```
sage: time matrix(ZZ,5000,sparse=True)._nonzero_positions_by_column()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
[]
```



---

archive/issue_events_016397.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-25T06:32:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6980#event-16397"
}
```



---

archive/issue_comments_057622.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T06:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6980#issuecomment-57622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057623.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6980#issuecomment-57623",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
