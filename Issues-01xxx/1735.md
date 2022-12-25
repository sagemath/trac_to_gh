# Issue 1735: [with patch] do not mark a spkg as installed if sage-check fails

archive/issues_001735.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf `SAGE_CHECK` is exported as a non-empty string we run spkg-check per default if it is available. But if spkg-check fails we still mark the spkg as installed. This should obviously not happen.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1735\n\n",
    "closed_at": "2008-01-13T02:01:09Z",
    "created_at": "2008-01-09T11:16:51Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch] do not mark a spkg as installed if sage-check fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1735",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

If `SAGE_CHECK` is exported as a non-empty string we run spkg-check per default if it is available. But if spkg-check fails we still mark the spkg as installed. This should obviously not happen.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1735





---

archive/issue_comments_010954.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch](tarball://root/attachments/some-uuid/ticket1735/Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch) by mabshoff created at 2008-01-13 01:37:15",
    "created_at": "2008-01-13T01:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch](tarball://root/attachments/some-uuid/ticket1735/Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch) by mabshoff created at 2008-01-13 01:37:15



---

archive/issue_comments_010955.json:
```json
{
    "body": "+1 -- this should be applied.  Perhaps the error message could be abstracted to a function, for future use?",
    "created_at": "2008-01-13T01:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10955",
    "user": "https://github.com/ncalexan"
}
```

+1 -- this should be applied.  Perhaps the error message could be abstracted to a function, for future use?



---

archive/issue_comments_010956.json:
```json
{
    "body": "The wording is slightly different, but it would still be a good idea to factor it out.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T02:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The wording is slightly different, but it would still be a good idea to factor it out.

Cheers,

Michael



---

archive/issue_comments_010957.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3.",
    "created_at": "2008-01-13T02:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha3.



---

archive/issue_comments_010958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T02:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004212.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-13T02:01:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1735#event-4212"
}
```
