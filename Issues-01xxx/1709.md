# Issue 1709: [with patch, positive review] Make experimental jmol graph plotting work

archive/issues_001709.json:
```json
{
    "body": "Assignee: @rlmill\n\nFor example, you can do\n\n```\nsage: G = graphs.DodecahedralGraph()\nsage: G.plot3d_new()\n```\n\nThis still needs to be cleaned up, but at least now it works instead of giving confusing errors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1709\n\n",
    "closed_at": "2008-01-08T23:20:58Z",
    "created_at": "2008-01-07T09:09:18Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch, positive review] Make experimental jmol graph plotting work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1709",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

For example, you can do

```
sage: G = graphs.DodecahedralGraph()
sage: G.plot3d_new()
```

This still needs to be cleaned up, but at least now it works instead of giving confusing errors.

Issue created by migration from https://trac.sagemath.org/ticket/1709





---

archive/issue_comments_010809.json:
```json
{
    "body": "Attachment [jmol_graphs.patch](tarball://root/attachments/some-uuid/ticket1709/jmol_graphs.patch) by @robertwb created at 2008-01-08 23:05:26\n\nYep, I've been using this and it works great.",
    "created_at": "2008-01-08T23:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1709#issuecomment-10809",
    "user": "https://github.com/robertwb"
}
```

Attachment [jmol_graphs.patch](tarball://root/attachments/some-uuid/ticket1709/jmol_graphs.patch) by @robertwb created at 2008-01-08 23:05:26

Yep, I've been using this and it works great.



---

archive/issue_comments_010810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-08T23:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1709#issuecomment-10810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010811.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1.",
    "created_at": "2008-01-08T23:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1709#issuecomment-10811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha1.



---

archive/issue_events_004170.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-08T23:20:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1709",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1709#event-4170"
}
```
