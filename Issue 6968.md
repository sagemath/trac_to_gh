# Issue 6968: [with patch, positive review] improve _vector_times_matrix

archive/issues_006968.json:
```json
{
    "body": "Assignee: @williamstein\n\nVery small patch avoiding multiple copies\n\nIssue created by migration from https://trac.sagemath.org/ticket/6968\n\n",
    "closed_at": "2009-09-24T16:45:51Z",
    "created_at": "2009-09-20T20:30:00Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] improve _vector_times_matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6968",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @williamstein

Very small patch avoiding multiple copies

Issue created by migration from https://trac.sagemath.org/ticket/6968





---

archive/issue_comments_057541.json:
```json
{
    "body": "Attachment [trac_6968_vector_times_matrix.patch](tarball://root/attachments/some-uuid/ticket6968/trac_6968_vector_times_matrix.patch) by ylchapuy created at 2009-09-20 20:31:15",
    "created_at": "2009-09-20T20:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6968#issuecomment-57541",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_6968_vector_times_matrix.patch](tarball://root/attachments/some-uuid/ticket6968/trac_6968_vector_times_matrix.patch) by ylchapuy created at 2009-09-20 20:31:15



---

archive/issue_comments_057542.json:
```json
{
    "body": "for the record:\n\nbefore:\n\n```\nsage: m=identity_matrix(1000,sparse=True)\nsage: v=vector([1]*1000,sparse=True)\nsage: time p = v*m\nCPU times: user 2.26 s, sys: 0.00 s, total: 2.26 s\nWall time: 2.26 s \n```\n\nafter:\n\n```\nsage: m=identity_matrix(1000,sparse=True)\nsage: v=vector([1]*1000,sparse=True) \nsage: time p = v*m \nCPU times: user 0.20 s, sys: 0.00 s, total: 0.20 s\nWall time: 0.21 s\n```",
    "created_at": "2009-09-20T20:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6968#issuecomment-57542",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

for the record:

before:

```
sage: m=identity_matrix(1000,sparse=True)
sage: v=vector([1]*1000,sparse=True)
sage: time p = v*m
CPU times: user 2.26 s, sys: 0.00 s, total: 2.26 s
Wall time: 2.26 s 
```

after:

```
sage: m=identity_matrix(1000,sparse=True)
sage: v=vector([1]*1000,sparse=True) 
sage: time p = v*m 
CPU times: user 0.20 s, sys: 0.00 s, total: 0.20 s
Wall time: 0.21 s
```



---

archive/issue_comments_057543.json:
```json
{
    "body": "Nice!!",
    "created_at": "2009-09-20T21:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6968#issuecomment-57543",
    "user": "https://github.com/williamstein"
}
```

Nice!!



---

archive/issue_comments_057544.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T16:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6968#issuecomment-57544",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016375.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T16:45:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6968",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6968#event-16375"
}
```



---

archive/issue_comments_057545.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6968#issuecomment-57545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
