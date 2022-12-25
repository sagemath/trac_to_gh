# Issue 1917: [with patch; with positive review] linbox -- get rid of crazy OS X charpoly workaround, since linbox isn't broken anymore (also that workaround was buggy when minpoly != charpoly)

archive/issues_001917.json:
```json
{
    "body": "Assignee: @malb\n\nI've made this a blocker, since if not applied it could give wrong answers - notice that minpoly is called in *both* cases in the old version.   Also this should be easy to referee.  All it does is delete a workaround. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1917\n\n",
    "closed_at": "2008-01-25T03:21:13Z",
    "created_at": "2008-01-25T00:54:09Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch; with positive review] linbox -- get rid of crazy OS X charpoly workaround, since linbox isn't broken anymore (also that workaround was buggy when minpoly != charpoly)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1917",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

I've made this a blocker, since if not applied it could give wrong answers - notice that minpoly is called in *both* cases in the old version.   Also this should be easy to referee.  All it does is delete a workaround. 

Issue created by migration from https://trac.sagemath.org/ticket/1917





---

archive/issue_comments_012109.json:
```json
{
    "body": "Attachment [trac-1917-remove_linbox_workaround.patch](tarball://root/attachments/some-uuid/ticket1917/trac-1917-remove_linbox_workaround.patch) by @williamstein created at 2008-01-25 00:56:58",
    "created_at": "2008-01-25T00:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1917#issuecomment-12109",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1917-remove_linbox_workaround.patch](tarball://root/attachments/some-uuid/ticket1917/trac-1917-remove_linbox_workaround.patch) by @williamstein created at 2008-01-25 00:56:58



---

archive/issue_comments_012110.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-25T00:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1917#issuecomment-12110",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_012111.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T03:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1917#issuecomment-12111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_events_004617.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-25T03:21:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1917",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1917#event-4617"
}
```



---

archive/issue_comments_012112.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T03:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1917#issuecomment-12112",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_012113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T03:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1917#issuecomment-12113",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
