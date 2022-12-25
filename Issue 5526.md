# Issue 5526: [with patch; positive review] get rid of including sse4_1 in local/lib/sage-flags.txt

archive/issues_005526.json:
```json
{
    "body": "Assignee: mabshoff\n\nJustification: evidently we don't use this and it's on our box that builds binaries. \n\nThe attached patch refactors the code in sage-location slightly to only *include* known flags we care about. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5526\n\n",
    "closed_at": "2009-03-24T23:30:04Z",
    "created_at": "2009-03-15T17:40:32Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; positive review] get rid of including sse4_1 in local/lib/sage-flags.txt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5526",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Justification: evidently we don't use this and it's on our box that builds binaries. 

The attached patch refactors the code in sage-location slightly to only *include* known flags we care about. 

Issue created by migration from https://trac.sagemath.org/ticket/5526





---

archive/issue_comments_042907.json:
```json
{
    "body": "Attachment [trac-local_bin_repo-5526.patch](tarball://root/attachments/some-uuid/ticket5526/trac-local_bin_repo-5526.patch) by mabshoff created at 2009-03-16 04:36:54\n\nI can live with this patch. We do not technically need the 'ssse3' flag since the Sage library does not use it.\n\nCheers,\n\nMihcael",
    "created_at": "2009-03-16T04:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5526#issuecomment-42907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-local_bin_repo-5526.patch](tarball://root/attachments/some-uuid/ticket5526/trac-local_bin_repo-5526.patch) by mabshoff created at 2009-03-16 04:36:54

I can live with this patch. We do not technically need the 'ssse3' flag since the Sage library does not use it.

Cheers,

Mihcael



---

archive/issue_comments_042908.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-24T23:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5526#issuecomment-42908",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_events_012957.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-24T23:30:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5526",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5526#event-12957"
}
```



---

archive/issue_comments_042909.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-24T23:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5526#issuecomment-42909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
