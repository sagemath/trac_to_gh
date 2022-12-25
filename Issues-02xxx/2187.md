# Issue 2187: [with patch, with positive review] improve refman autogeneration; add and rewrite much reference manual text

archive/issues_002187.json:
```json
{
    "body": "Assignee: tba\n\nI have two patches.  One, for hg_doc, improves the consistency between the formatting of module docstrings, class docstrings, and function docstrings.  The main effect of this is that \"AUTHORS:\" blocks are now specially translated in class docstrings, to match the behavior of module and function docstrings.\n\nThe other patch, for hg_sage, adds and rewrites a fair bit of text: fixing typos, adding LaTeX formatting, etc.\n\nI also snuck in a bugfix: `IntegerMod_gmp` and `IntegerMod_int` had an `__index__` method, so that values could be used as array indices; but the method was missing from `IntegerMod_int64`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2187\n\n",
    "closed_at": "2008-02-17T13:04:56Z",
    "created_at": "2008-02-17T05:35:37Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, with positive review] improve refman autogeneration; add and rewrite much reference manual text",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2187",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: tba

I have two patches.  One, for hg_doc, improves the consistency between the formatting of module docstrings, class docstrings, and function docstrings.  The main effect of this is that "AUTHORS:" blocks are now specially translated in class docstrings, to match the behavior of module and function docstrings.

The other patch, for hg_sage, adds and rewrites a fair bit of text: fixing typos, adding LaTeX formatting, etc.

I also snuck in a bugfix: `IntegerMod_gmp` and `IntegerMod_int` had an `__index__` method, so that values could be used as array indices; but the method was missing from `IntegerMod_int64`.

Issue created by migration from https://trac.sagemath.org/ticket/2187





---

archive/issue_comments_014329.json:
```json
{
    "body": "Attachment [trac-2187-hg_doc.patch](tarball://root/attachments/some-uuid/ticket2187/trac-2187-hg_doc.patch) by cwitty created at 2008-02-17 05:37:04",
    "created_at": "2008-02-17T05:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2187#issuecomment-14329",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-2187-hg_doc.patch](tarball://root/attachments/some-uuid/ticket2187/trac-2187-hg_doc.patch) by cwitty created at 2008-02-17 05:37:04



---

archive/issue_comments_014330.json:
```json
{
    "body": "Attachment [trac-2187-hg_sage.patch](tarball://root/attachments/some-uuid/ticket2187/trac-2187-hg_sage.patch) by mabshoff created at 2008-02-17 13:04:43\n\nBoth patches looks good to me, they apply cleanly -> positive review.",
    "created_at": "2008-02-17T13:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2187#issuecomment-14330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-2187-hg_sage.patch](tarball://root/attachments/some-uuid/ticket2187/trac-2187-hg_sage.patch) by mabshoff created at 2008-02-17 13:04:43

Both patches looks good to me, they apply cleanly -> positive review.



---

archive/issue_comments_014331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T13:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2187#issuecomment-14331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014332.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T13:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2187#issuecomment-14332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_events_005225.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T13:04:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2187",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2187#event-5225"
}
```
