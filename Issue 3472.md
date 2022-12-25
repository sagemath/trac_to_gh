# Issue 3472: Running sage from a non-existent directory pretends to work

archive/issues_003472.json:
```json
{
    "body": "Assignee: @craigcitro\n\nRunning sage from a directory that doesn't exist thinks it's working, but really just fails. I'm attaching a new `$SAGE_ROOT/sage` replacement that checks this on startup.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3472\n\n",
    "created_at": "2008-06-19T21:13:49Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Running sage from a non-existent directory pretends to work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3472",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

Running sage from a directory that doesn't exist thinks it's working, but really just fails. I'm attaching a new `$SAGE_ROOT/sage` replacement that checks this on startup.

Issue created by migration from https://trac.sagemath.org/ticket/3472





---

archive/issue_comments_024428.json:
```json
{
    "body": "Attachment [sage-root.sage](tarball://root/attachments/some-uuid/ticket3472/sage-root.sage) by mabshoff created at 2008-06-26 06:37:36",
    "created_at": "2008-06-26T06:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-root.sage](tarball://root/attachments/some-uuid/ticket3472/sage-root.sage) by mabshoff created at 2008-06-26 06:37:36



---

archive/issue_events_007880.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-26T06:37:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3472#event-7880"
}
```



---

archive/issue_comments_024429.json:
```json
{
    "body": "Positive review to the changes made by Craig. As it turned out `sage -upgrade` does not fix (this is now #3517)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-27T00:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review to the changes made by Craig. As it turned out `sage -upgrade` does not fix (this is now #3517)

Cheers,

Michael



---

archive/issue_events_007881.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-27T00:14:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3472#event-7881"
}
```



---

archive/issue_events_007882.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-27T00:14:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3472#event-7882"
}
```



---

archive/issue_comments_024430.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-27T00:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-27T00:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-27T00:14:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3472#event-7883"
}
```
