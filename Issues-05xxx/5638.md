# Issue 5638: [with patch, positive review] deprecate jsmath from the command line

archive/issues_005638.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nFrom the command line, jsmath is kind of broken and is also superfluous: `jsmath('blah', mode='inline')` is basically equivalent to `html('$blah$')`, and similarly if mode='display': just use '$$blah$$'.  This patch removes jsmath from import into the global name space at the command line, rewrites the code to make it just call html, and adds a deprecation warning.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5638\n\n",
    "closed_at": "2009-03-31T08:32:07Z",
    "created_at": "2009-03-30T01:02:42Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] deprecate jsmath from the command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5638",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

From the command line, jsmath is kind of broken and is also superfluous: `jsmath('blah', mode='inline')` is basically equivalent to `html('$blah$')`, and similarly if mode='display': just use '$$blah$$'.  This patch removes jsmath from import into the global name space at the command line, rewrites the code to make it just call html, and adds a deprecation warning.


Issue created by migration from https://trac.sagemath.org/ticket/5638





---

archive/issue_comments_043941.json:
```json
{
    "body": "Attachment [deprecate-jsmath.patch](tarball://root/attachments/some-uuid/ticket5638/deprecate-jsmath.patch) by @williamstein created at 2009-03-30 01:22:29\n\nThis works, looks good, and also works with #5636.",
    "created_at": "2009-03-30T01:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5638#issuecomment-43941",
    "user": "https://github.com/williamstein"
}
```

Attachment [deprecate-jsmath.patch](tarball://root/attachments/some-uuid/ticket5638/deprecate-jsmath.patch) by @williamstein created at 2009-03-30 01:22:29

This works, looks good, and also works with #5636.



---

archive/issue_events_013259.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-31T08:32:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5638",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5638#event-13259"
}
```



---

archive/issue_comments_043942.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T08:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5638#issuecomment-43942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_043943.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T08:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5638#issuecomment-43943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
