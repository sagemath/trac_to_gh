# Issue 3976: [with patch, needs review] improve doctests to expect.py, maxima.py, and lie.py

archive/issues_003976.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3976\n\n",
    "created_at": "2008-08-28T19:39:29Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] improve doctests to expect.py, maxima.py, and lie.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3976",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/3976





---

archive/issue_comments_028507.json:
```json
{
    "body": "Attachment [trac_3976.patch](tarball://root/attachments/some-uuid/ticket3976/trac_3976.patch) by @mwhansen created at 2008-08-28 19:39:49",
    "created_at": "2008-08-28T19:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3976#issuecomment-28507",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3976.patch](tarball://root/attachments/some-uuid/ticket3976/trac_3976.patch) by @mwhansen created at 2008-08-28 19:39:49



---

archive/issue_comments_028508.json:
```json
{
    "body": "After discussion with mhansen, we decided it would be better to use `os.popen` instead of `os.system`, in order to remove many `#not tested` bits.",
    "created_at": "2008-08-28T22:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3976#issuecomment-28508",
    "user": "https://github.com/rlmill"
}
```

After discussion with mhansen, we decided it would be better to use `os.popen` instead of `os.system`, in order to remove many `#not tested` bits.



---

archive/issue_comments_028509.json:
```json
{
    "body": "Attachment [trac_3976-2.patch](tarball://root/attachments/some-uuid/ticket3976/trac_3976-2.patch) by @mwhansen created at 2008-08-28 22:51:29",
    "created_at": "2008-08-28T22:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3976#issuecomment-28509",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3976-2.patch](tarball://root/attachments/some-uuid/ticket3976/trac_3976-2.patch) by @mwhansen created at 2008-08-28 22:51:29



---

archive/issue_comments_028510.json:
```json
{
    "body": "Attachment [trac_3976-3.patch](tarball://root/attachments/some-uuid/ticket3976/trac_3976-3.patch) by @rlmill created at 2008-08-28 22:55:13\n\nThe patches apply cleanly (with some light fuzz for the first patch), and pass all tests. Apply this.",
    "created_at": "2008-08-28T22:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3976#issuecomment-28510",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_3976-3.patch](tarball://root/attachments/some-uuid/ticket3976/trac_3976-3.patch) by @rlmill created at 2008-08-28 22:55:13

The patches apply cleanly (with some light fuzz for the first patch), and pass all tests. Apply this.



---

archive/issue_comments_028511.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T22:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3976#issuecomment-28511",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.2.alpha2



---

archive/issue_comments_028512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T22:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3976#issuecomment-28512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004206.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-28T22:57:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3976",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3976#event-4206"
}
```
