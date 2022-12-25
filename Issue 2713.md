# Issue 2713: [with patch, needs review] sage-doctest applies backslash handling to expected outputs

archive/issues_002713.json:
```json
{
    "body": "Assignee: failure\n\nsage-doctest applies \"backslash handling\" to doctests, where a line that ends with a single backslash is merged with the next line (with the backslash removed).  As far as I can tell, this makes it impossible to doctest something with an expected output having a line ending with a backslash.\n\nThis patch to the \"hg_scripts\" repository removes the behavior for expected outputs (but keeps backslash handling for inputs; that is, for lines beginning \"sage:\").  There was one doctest in Sage that depended on the previous behavior; the second patch modifies that doctest to pass with the new sage-doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2713\n\n",
    "created_at": "2008-03-29T01:02:51Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] sage-doctest applies backslash handling to expected outputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2713",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: failure

sage-doctest applies "backslash handling" to doctests, where a line that ends with a single backslash is merged with the next line (with the backslash removed).  As far as I can tell, this makes it impossible to doctest something with an expected output having a line ending with a backslash.

This patch to the "hg_scripts" repository removes the behavior for expected outputs (but keeps backslash handling for inputs; that is, for lines beginning "sage:").  There was one doctest in Sage that depended on the previous behavior; the second patch modifies that doctest to pass with the new sage-doctest.

Issue created by migration from https://trac.sagemath.org/ticket/2713





---

archive/issue_comments_018663.json:
```json
{
    "body": "Attachment [trac2713-hg_scripts-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_scripts-backslash-handling.patch) by cwitty created at 2008-03-29 01:05:00",
    "created_at": "2008-03-29T01:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18663",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2713-hg_scripts-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_scripts-backslash-handling.patch) by cwitty created at 2008-03-29 01:05:00



---

archive/issue_comments_018664.json:
```json
{
    "body": "Attachment [trac2713-hg_sage-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_sage-backslash-handling.patch) by cwitty created at 2008-03-29 01:06:56",
    "created_at": "2008-03-29T01:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18664",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2713-hg_sage-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_sage-backslash-handling.patch) by cwitty created at 2008-03-29 01:06:56



---

archive/issue_comments_018665.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T20:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18665",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_018666.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_events_006335.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T21:54:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2713#event-6335"
}
```



---

archive/issue_comments_018667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
