# Issue 2713: [with patch, needs review] sage-doctest applies backslash handling to expected outputs

archive/issues_002713.json:
```json
{
    "body": "Assignee: failure\n\nsage-doctest applies \"backslash handling\" to doctests, where a line that ends with a single backslash is merged with the next line (with the backslash removed).  As far as I can tell, this makes it impossible to doctest something with an expected output having a line ending with a backslash.\n\nThis patch to the \"hg_scripts\" repository removes the behavior for expected outputs (but keeps backslash handling for inputs; that is, for lines beginning \"sage:\").  There was one doctest in Sage that depended on the previous behavior; the second patch modifies that doctest to pass with the new sage-doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2713\n\n",
    "created_at": "2008-03-29T01:02:51Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] sage-doctest applies backslash handling to expected outputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2713",
    "user": "cwitty"
}
```
Assignee: failure

sage-doctest applies "backslash handling" to doctests, where a line that ends with a single backslash is merged with the next line (with the backslash removed).  As far as I can tell, this makes it impossible to doctest something with an expected output having a line ending with a backslash.

This patch to the "hg_scripts" repository removes the behavior for expected outputs (but keeps backslash handling for inputs; that is, for lines beginning "sage:").  There was one doctest in Sage that depended on the previous behavior; the second patch modifies that doctest to pass with the new sage-doctest.

Issue created by migration from https://trac.sagemath.org/ticket/2713





---

archive/issue_comments_018702.json:
```json
{
    "body": "Attachment [trac2713-hg_scripts-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_scripts-backslash-handling.patch) by cwitty created at 2008-03-29 01:05:00",
    "created_at": "2008-03-29T01:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18702",
    "user": "cwitty"
}
```

Attachment [trac2713-hg_scripts-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_scripts-backslash-handling.patch) by cwitty created at 2008-03-29 01:05:00



---

archive/issue_comments_018703.json:
```json
{
    "body": "Attachment [trac2713-hg_sage-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_sage-backslash-handling.patch) by cwitty created at 2008-03-29 01:06:56",
    "created_at": "2008-03-29T01:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18703",
    "user": "cwitty"
}
```

Attachment [trac2713-hg_sage-backslash-handling.patch](tarball://root/attachments/some-uuid/ticket2713/trac2713-hg_sage-backslash-handling.patch) by cwitty created at 2008-03-29 01:06:56



---

archive/issue_comments_018704.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T20:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18704",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_018705.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18705",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_018706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T21:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2713#issuecomment-18706",
    "user": "mabshoff"
}
```

Resolution: fixed
