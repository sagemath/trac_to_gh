# Issue 5376: [with patch, needs review] minor problems with ReST in plot.py

archive/issues_005376.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThis fixes the last few issues from #4923.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5376\n\n",
    "created_at": "2009-02-26T00:32:42Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] minor problems with ReST in plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5376",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

This fixes the last few issues from #4923.


Issue created by migration from https://trac.sagemath.org/ticket/5376





---

archive/issue_comments_041321.json:
```json
{
    "body": "Attachment [plot-rst.patch](tarball://root/attachments/some-uuid/ticket5376/plot-rst.patch) by mvngu created at 2009-02-27 08:24:50\n\nREFEREE REPORT\n\n\n\nThe patch **plot-rst.patch** applied OK against 3.4.alpha0 and all doctests passed with the options\n\n```\n-t -long -optional\n```\n\nThe reference manual built OK with the command\n\n```\nsage -docbuild reference html\n```\n\nChecking the relevant HTML file\n\n```\n/path/to/html/en/reference/sage/plot/plot.html\n```\n\nI see that the patch fixes the formatting and typo issues. Positive review.",
    "created_at": "2009-02-27T08:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5376#issuecomment-41321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [plot-rst.patch](tarball://root/attachments/some-uuid/ticket5376/plot-rst.patch) by mvngu created at 2009-02-27 08:24:50

REFEREE REPORT



The patch **plot-rst.patch** applied OK against 3.4.alpha0 and all doctests passed with the options

```
-t -long -optional
```

The reference manual built OK with the command

```
sage -docbuild reference html
```

Checking the relevant HTML file

```
/path/to/html/en/reference/sage/plot/plot.html
```

I see that the patch fixes the formatting and typo issues. Positive review.



---

archive/issue_events_005631.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-28T16:25:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5376",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5376#event-5631"
}
```



---

archive/issue_comments_041322.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5376#issuecomment-41322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041323.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5376#issuecomment-41323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
