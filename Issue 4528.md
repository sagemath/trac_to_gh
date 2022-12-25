# Issue 4528: [with patch, needs review] Implement Krull dimension for orders in number fields

archive/issues_004528.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: number fields, orders\n\nThis is a triviality, but I noticed it while doing something else. All order in number fields have Krull dimension 1, but this was not implemented -- not even for the maximal order.  Now it is.\n\nPatch based on 3.2.rc1, touches rings/ring.pyx and rings/number_field/order.py\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4528\n\n",
    "created_at": "2008-11-15T16:56:35Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] Implement Krull dimension for orders in number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4528",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: number fields, orders

This is a triviality, but I noticed it while doing something else. All order in number fields have Krull dimension 1, but this was not implemented -- not even for the maximal order.  Now it is.

Patch based on 3.2.rc1, touches rings/ring.pyx and rings/number_field/order.py


Issue created by migration from https://trac.sagemath.org/ticket/4528





---

archive/issue_comments_033558.json:
```json
{
    "body": "Attachment [krull.patch](tarball://root/attachments/some-uuid/ticket4528/krull.patch) by @JohnCremona created at 2008-11-15 16:56:56",
    "created_at": "2008-11-15T16:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33558",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [krull.patch](tarball://root/attachments/some-uuid/ticket4528/krull.patch) by @JohnCremona created at 2008-11-15 16:56:56



---

archive/issue_comments_033559.json:
```json
{
    "body": "This looks good.\n\nAs a really trivial issue, someone should add a `.` at the end of line 754 of `ring.pyx`. It didn't seem worth another patch.",
    "created_at": "2008-11-21T10:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33559",
    "user": "https://github.com/craigcitro"
}
```

This looks good.

As a really trivial issue, someone should add a `.` at the end of line 754 of `ring.pyx`. It didn't seem worth another patch.



---

archive/issue_comments_033560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T11:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033561.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T11:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_events_010301.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-21T11:26:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4528#event-10301"
}
```
