# Issue 2875: notebook -- save_session is completely broken in the notebook

archive/issues_002875.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2875\n\n",
    "created_at": "2008-04-11T04:39:23Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "notebook -- save_session is completely broken in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2875",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/2875





---

archive/issue_comments_019749.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-12T03:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19749",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_019750.json:
```json
{
    "body": "Attachment [sage-2875.patch](tarball://root/attachments/some-uuid/ticket2875/sage-2875.patch) by was created at 2008-04-12 03:31:56",
    "created_at": "2008-04-12T03:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19750",
    "user": "was"
}
```

Attachment [sage-2875.patch](tarball://root/attachments/some-uuid/ticket2875/sage-2875.patch) by was created at 2008-04-12 03:31:56



---

archive/issue_comments_019751.json:
```json
{
    "body": "The code looks reasonable to me, but I don't know what to test.  Please add doctests to save_session() and do_sage_extensions_preparsing().",
    "created_at": "2008-04-12T07:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19751",
    "user": "boothby"
}
```

The code looks reasonable to me, but I don't know what to test.  Please add doctests to save_session() and do_sage_extensions_preparsing().



---

archive/issue_comments_019752.json:
```json
{
    "body": "See #2901 which provides the doctesting.",
    "created_at": "2008-04-13T05:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19752",
    "user": "was"
}
```

See #2901 which provides the doctesting.



---

archive/issue_comments_019753.json:
```json
{
    "body": "After deleting the first hunk from the patch (since it is deleted anyway via #2901 and I had to resolve that conflict manually) the patch applies cleanly.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T23:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19753",
    "user": "mabshoff"
}
```

After deleting the first hunk from the patch (since it is deleted anyway via #2901 and I had to resolve that conflict manually) the patch applies cleanly.

Cheers,

Michael



---

archive/issue_comments_019754.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-13T23:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19754",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_comments_019755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T23:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2875#issuecomment-19755",
    "user": "mabshoff"
}
```

Resolution: fixed
