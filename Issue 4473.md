# Issue 4473: [with patch; needs review] loading file.sage that has a line "load foo.py" is broken due to a missing import

archive/issues_004473.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4473\n\n",
    "created_at": "2008-11-09T03:13:41Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "title": "[with patch; needs review] loading file.sage that has a line \"load foo.py\" is broken due to a missing import",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4473",
    "user": "was"
}
```
Assignee: was

CC:  mhansen



Issue created by migration from https://trac.sagemath.org/ticket/4473





---

archive/issue_comments_033039.json:
```json
{
    "body": "Attachment [sage-4473.patch](tarball://root/attachments/some-uuid/ticket4473/sage-4473.patch) by was created at 2008-11-09 03:17:47",
    "created_at": "2008-11-09T03:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4473#issuecomment-33039",
    "user": "was"
}
```

Attachment [sage-4473.patch](tarball://root/attachments/some-uuid/ticket4473/sage-4473.patch) by was created at 2008-11-09 03:17:47



---

archive/issue_comments_033040.json:
```json
{
    "body": "To test this, make a file foo.sage with\n\n```\nload a.py\n```\n\nin it, and make a.py an empty file.   Then try\n\n\n```\nsage: load foo.sage\n```\n\n\nand see that you don't get a big nasty printout.",
    "created_at": "2008-11-09T03:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4473#issuecomment-33040",
    "user": "was"
}
```

To test this, make a file foo.sage with

```
load a.py
```

in it, and make a.py an empty file.   Then try


```
sage: load foo.sage
```


and see that you don't get a big nasty printout.



---

archive/issue_comments_033041.json:
```json
{
    "body": "Nice catch. Positive review, we had to fix similar issues once we had updated to IPython 0.8.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T07:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4473#issuecomment-33041",
    "user": "mabshoff"
}
```

Nice catch. Positive review, we had to fix similar issues once we had updated to IPython 0.8.4.

Cheers,

Michael



---

archive/issue_comments_033042.json:
```json
{
    "body": "Merged in Sage 3.2.rc0",
    "created_at": "2008-11-09T08:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4473#issuecomment-33042",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc0



---

archive/issue_comments_033043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-09T08:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4473#issuecomment-33043",
    "user": "mabshoff"
}
```

Resolution: fixed
