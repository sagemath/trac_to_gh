# Issue 1507: [with patch, with positive review] plotting -- document how to use pylab / matlab style plotting from sage

archive/issues_001507.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1507\n\n",
    "closed_at": "2007-12-15T06:47:58Z",
    "created_at": "2007-12-14T17:53:05Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch, with positive review] plotting -- document how to use pylab / matlab style plotting from sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1507",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/1507





---

archive/issue_events_003816.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-14T17:53:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1507#event-3816"
}
```



---

archive/issue_comments_009623.json:
```json
{
    "body": "this is *only* a documentation addition -- no code, so should be easy to referee.",
    "created_at": "2007-12-14T17:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9623",
    "user": "https://github.com/williamstein"
}
```

this is *only* a documentation addition -- no code, so should be easy to referee.



---

archive/issue_comments_009624.json:
```json
{
    "body": "Attachment [trac-1507.patch](tarball://root/attachments/some-uuid/ticket1507/trac-1507.patch) by @williamstein created at 2007-12-14 17:58:26",
    "created_at": "2007-12-14T17:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9624",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1507.patch](tarball://root/attachments/some-uuid/ticket1507/trac-1507.patch) by @williamstein created at 2007-12-14 17:58:26



---

archive/issue_comments_009625.json:
```json
{
    "body": "If the second hunk fails, no problem.  That's not relevant.  Only the first big\nhunk is.",
    "created_at": "2007-12-14T17:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9625",
    "user": "https://github.com/williamstein"
}
```

If the second hunk fails, no problem.  That's not relevant.  Only the first big
hunk is.



---

archive/issue_comments_009626.json:
```json
{
    "body": "Looks good to me.  \n\nTo apply: Attempt to apply the patch as usual.  Ignore the error message:\n\n```\nHunk #2 FAILED at 127\n1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\nabort: patch failed to apply\n```\n\nThen do `hg_sage.ci()`, to check in the half-applied patch.",
    "created_at": "2007-12-15T06:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9626",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good to me.  

To apply: Attempt to apply the patch as usual.  Ignore the error message:

```
Hunk #2 FAILED at 127
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```

Then do `hg_sage.ci()`, to check in the half-applied patch.



---

archive/issue_comments_009627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T06:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009628.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T06:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_003817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T06:47:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1507#event-3817"
}
```
