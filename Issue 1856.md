# Issue 1856: [with patch; positive review] 3d graphics -- bug in setting options via the show command

archive/issues_001856.json:
```json
{
    "body": "Assignee: @williamstein\n\nTry this:\n\n```\nsage: sphere((0,0,0), figsize=2).show(viewer='tachyon', figsize=10)\n```\nA tiny picture of a sphere appears.  It should be that the second figsize overwrites the first.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1856\n\n",
    "closed_at": "2008-01-21T04:19:50Z",
    "created_at": "2008-01-19T23:45:50Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch; positive review] 3d graphics -- bug in setting options via the show command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1856",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Try this:

```
sage: sphere((0,0,0), figsize=2).show(viewer='tachyon', figsize=10)
```
A tiny picture of a sphere appears.  It should be that the second figsize overwrites the first.

Issue created by migration from https://trac.sagemath.org/ticket/1856





---

archive/issue_comments_011712.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T23:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11712",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011713.json:
```json
{
    "body": "Attachment [trac-1856.patch](tarball://root/attachments/some-uuid/ticket1856/trac-1856.patch) by @williamstein created at 2008-01-20 00:07:59",
    "created_at": "2008-01-20T00:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11713",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1856.patch](tarball://root/attachments/some-uuid/ticket1856/trac-1856.patch) by @williamstein created at 2008-01-20 00:07:59



---

archive/issue_comments_011714.json:
```json
{
    "body": "This fixes the problem mentioned above in a simple clean way, adds the ability to globally override the defaults, and adds an unrelated doctest.",
    "created_at": "2008-01-20T00:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11714",
    "user": "https://github.com/williamstein"
}
```

This fixes the problem mentioned above in a simple clean way, adds the ability to globally override the defaults, and adds an unrelated doctest.



---

archive/issue_comments_011715.json:
```json
{
    "body": "Attachment [1856.patch](tarball://root/attachments/some-uuid/ticket1856/1856.patch) by @mwhansen created at 2008-01-21 03:55:29",
    "created_at": "2008-01-21T03:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11715",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1856.patch](tarball://root/attachments/some-uuid/ticket1856/1856.patch) by @mwhansen created at 2008-01-21 03:55:29



---

archive/issue_comments_011716.json:
```json
{
    "body": "The patch I posted applies (after #1854) and passes tests.",
    "created_at": "2008-01-21T03:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11716",
    "user": "https://github.com/mwhansen"
}
```

The patch I posted applies (after #1854) and passes tests.



---

archive/issue_comments_011717.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011718.json:
```json
{
    "body": "Merged trac-1856.patch in Sage 2.10.1.alpha. mhansen's patch gave rejects.",
    "created_at": "2008-01-21T04:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-1856.patch in Sage 2.10.1.alpha. mhansen's patch gave rejects.



---

archive/issue_events_004498.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T04:19:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1856#event-4498"
}
```
