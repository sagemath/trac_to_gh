# Issue 5349: [with patch, needs review] Make extensions linking against libSingular depend on $SAGE_LOCAL/include/libsingular.h

archive/issues_005349.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  georgsweber\n\nThe summary says it all. It causes the extensions to be automatically being rebuild when the singular.spkg has been rebuild.\n\nGeorg: Can you review this?\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5349\n\n",
    "created_at": "2009-02-23T15:07:57Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] Make extensions linking against libSingular depend on $SAGE_LOCAL/include/libsingular.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5349",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  georgsweber

The summary says it all. It causes the extensions to be automatically being rebuild when the singular.spkg has been rebuild.

Georg: Can you review this?

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5349





---

archive/issue_comments_041209.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-23T15:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5349#issuecomment-41209",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041210.json:
```json
{
    "body": "Attachment [trac_5349.patch](tarball://root/attachments/some-uuid/ticket5349/trac_5349.patch) by mabshoff created at 2009-02-23 19:02:24",
    "created_at": "2009-02-23T19:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5349#issuecomment-41210",
    "user": "mabshoff"
}
```

Attachment [trac_5349.patch](tarball://root/attachments/some-uuid/ticket5349/trac_5349.patch) by mabshoff created at 2009-02-23 19:02:24



---

archive/issue_comments_041211.json:
```json
{
    "body": "I tested it; it works.  Positive review.",
    "created_at": "2009-02-23T19:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5349#issuecomment-41211",
    "user": "cwitty"
}
```

I tested it; it works.  Positive review.



---

archive/issue_comments_041212.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5349#issuecomment-41212",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_041213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5349#issuecomment-41213",
    "user": "mabshoff"
}
```

Resolution: fixed
