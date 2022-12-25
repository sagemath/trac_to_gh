# Issue 2580: [with patch, needs review] Implement backends for graphs

archive/issues_002580.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis abstracts the layer between NetworkX and Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2580\n\n",
    "created_at": "2008-03-18T01:56:35Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] Implement backends for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2580",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

This abstracts the layer between NetworkX and Sage.

Issue created by migration from https://trac.sagemath.org/ticket/2580





---

archive/issue_comments_017610.json:
```json
{
    "body": "Attachment [2580-graph_backends.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends.patch) by @rlmill created at 2008-03-18 02:00:07",
    "created_at": "2008-03-18T02:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17610",
    "user": "https://github.com/rlmill"
}
```

Attachment [2580-graph_backends.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends.patch) by @rlmill created at 2008-03-18 02:00:07



---

archive/issue_comments_017611.json:
```json
{
    "body": "Attachment [2580-graph_backends_added_files.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends_added_files.patch) by @rlmill created at 2008-03-18 02:01:14\n\nMake sure to apply both patches before building. :)",
    "created_at": "2008-03-18T02:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17611",
    "user": "https://github.com/rlmill"
}
```

Attachment [2580-graph_backends_added_files.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends_added_files.patch) by @rlmill created at 2008-03-18 02:01:14

Make sure to apply both patches before building. :)



---

archive/issue_comments_017612.json:
```json
{
    "body": "Also,\n`./sage -t -long sage/graphs`\npasses all tests after these patches...",
    "created_at": "2008-03-18T02:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17612",
    "user": "https://github.com/rlmill"
}
```

Also,
`./sage -t -long sage/graphs`
passes all tests after these patches...



---

archive/issue_comments_017613.json:
```json
{
    "body": "Applies, passes tests, and looks good to me.  I'm not too concerned about the doctests in the new file.",
    "created_at": "2008-03-18T10:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17613",
    "user": "https://github.com/mwhansen"
}
```

Applies, passes tests, and looks good to me.  I'm not too concerned about the doctests in the new file.



---

archive/issue_comments_017614.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T11:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017615.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-18T11:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_events_006032.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T11:04:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2580#event-6032"
}
```
