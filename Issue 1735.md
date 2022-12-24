# Issue 1735: do not mark a spkg as installed if sage-check fails

archive/issues_001735.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf `SAGE_CHECK` is exported as a non-empty string we run spkg-check per default if it is available. But if spkg-check fails we still mark the spkg as installed. This should obviously not happen.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1735\n\n",
    "created_at": "2008-01-09T11:16:51Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "do not mark a spkg as installed if sage-check fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1735",
    "user": "mabshoff"
}
```
Assignee: mabshoff

If `SAGE_CHECK` is exported as a non-empty string we run spkg-check per default if it is available. But if spkg-check fails we still mark the spkg as installed. This should obviously not happen.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1735





---

archive/issue_comments_010981.json:
```json
{
    "body": "Attachment [Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch](tarball://root/attachments/some-uuid/ticket1735/Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch) by mabshoff created at 2008-01-13 01:37:15",
    "created_at": "2008-01-13T01:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10981",
    "user": "mabshoff"
}
```

Attachment [Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch](tarball://root/attachments/some-uuid/ticket1735/Sage-2.10.alpha2-do-not-mark-a-spkg-as-installed-if-sage-check-fails.patch) by mabshoff created at 2008-01-13 01:37:15



---

archive/issue_comments_010982.json:
```json
{
    "body": "+1 -- this should be applied.  Perhaps the error message could be abstracted to a function, for future use?",
    "created_at": "2008-01-13T01:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10982",
    "user": "ncalexan"
}
```

+1 -- this should be applied.  Perhaps the error message could be abstracted to a function, for future use?



---

archive/issue_comments_010983.json:
```json
{
    "body": "The wording is slightly different, but it would still be a good idea to factor it out.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T02:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10983",
    "user": "mabshoff"
}
```

The wording is slightly different, but it would still be a good idea to factor it out.

Cheers,

Michael



---

archive/issue_comments_010984.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3.",
    "created_at": "2008-01-13T02:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10984",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha3.



---

archive/issue_comments_010985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T02:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1735#issuecomment-10985",
    "user": "mabshoff"
}
```

Resolution: fixed
