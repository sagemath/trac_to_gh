# Issue 5095: [with patch, needs review] AJAX requests don't work from the worksheet listing page

archive/issues_005095.json:
```json
{
    "body": "Assignee: boothby\n\nThis is because the TinyMCE patch made the AJAX requests dependent of jQuery, but the worksheet listing page did not include jQuery. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5095\n\n",
    "created_at": "2009-01-25T07:16:04Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] AJAX requests don't work from the worksheet listing page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5095",
    "user": "mhansen"
}
```
Assignee: boothby

This is because the TinyMCE patch made the AJAX requests dependent of jQuery, but the worksheet listing page did not include jQuery. 

Issue created by migration from https://trac.sagemath.org/ticket/5095





---

archive/issue_comments_038856.json:
```json
{
    "body": "Attachment [trac_5095.patch](tarball://root/attachments/some-uuid/ticket5095/trac_5095.patch) by mhansen created at 2009-01-25 07:17:09",
    "created_at": "2009-01-25T07:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38856",
    "user": "mhansen"
}
```

Attachment [trac_5095.patch](tarball://root/attachments/some-uuid/ticket5095/trac_5095.patch) by mhansen created at 2009-01-25 07:17:09



---

archive/issue_comments_038857.json:
```json
{
    "body": "works for me.",
    "created_at": "2009-01-25T16:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38857",
    "user": "jhpalmieri"
}
```

works for me.



---

archive/issue_comments_038858.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38858",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038859.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T13:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5095#issuecomment-38859",
    "user": "mabshoff"
}
```

Resolution: fixed
