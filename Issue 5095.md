# Issue 5095: [with patch, needs review] AJAX requests don't work from the worksheet listing page

archive/issues_005095.json:
```json
{
    "body": "Assignee: boothby\n\nThis is because the TinyMCE patch made the AJAX requests dependent of jQuery, but the worksheet listing page did not include jQuery. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5095\n\n",
    "created_at": "2009-01-25T07:16:04Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] AJAX requests don't work from the worksheet listing page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5095",
    "user": "https://github.com/mwhansen"
}
```
Assignee: boothby

This is because the TinyMCE patch made the AJAX requests dependent of jQuery, but the worksheet listing page did not include jQuery. 

Issue created by migration from https://trac.sagemath.org/ticket/5095





---

archive/issue_comments_038782.json:
```json
{
    "body": "Attachment [trac_5095.patch](tarball://root/attachments/some-uuid/ticket5095/trac_5095.patch) by @mwhansen created at 2009-01-25 07:17:09",
    "created_at": "2009-01-25T07:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38782",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5095.patch](tarball://root/attachments/some-uuid/ticket5095/trac_5095.patch) by @mwhansen created at 2009-01-25 07:17:09



---

archive/issue_comments_038783.json:
```json
{
    "body": "works for me.",
    "created_at": "2009-01-25T16:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38783",
    "user": "https://github.com/jhpalmieri"
}
```

works for me.



---

archive/issue_comments_038784.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_events_005341.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T13:03:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5095#event-5341"
}
```



---

archive/issue_comments_038785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T13:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
