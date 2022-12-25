# Issue 3650: [with patch, needs review] Infinite recursion in pbuild by recursive pxd imports

archive/issues_003650.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nIn some cases, having pxds with recursive imports may cause pbuild to use recursion to go to infinity.  This patch fixes this issue.  In many cases this will just cause Cython to throw an error later, but pbuild should still behave better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3650\n\n",
    "created_at": "2008-07-13T11:22:50Z",
    "labels": [
        "component: pbuild",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with patch, needs review] Infinite recursion in pbuild by recursive pxd imports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3650",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

In some cases, having pxds with recursive imports may cause pbuild to use recursion to go to infinity.  This patch fixes this issue.  In many cases this will just cause Cython to throw an error later, but pbuild should still behave better.

Issue created by migration from https://trac.sagemath.org/ticket/3650





---

archive/issue_comments_025762.json:
```json
{
    "body": "Attachment [trac_3650.patch](tarball://root/attachments/some-uuid/ticket3650/trac_3650.patch) by @garyfurnish created at 2008-07-13 11:33:05",
    "created_at": "2008-07-13T11:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25762",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3650.patch](tarball://root/attachments/some-uuid/ticket3650/trac_3650.patch) by @garyfurnish created at 2008-07-13 11:33:05



---

archive/issue_comments_025763.json:
```json
{
    "body": "Positive review. What could go wrong? ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-07-15T23:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. What could go wrong? ;)

Cheers,

Michael



---

archive/issue_comments_025764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-15T23:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025765.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-15T23:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_events_008369.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-15T23:38:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3650#event-8369"
}
```
