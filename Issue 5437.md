# Issue 5437: [with patch; needs review] pickle jar -- make it run through in order

archive/issues_005437.json:
```json
{
    "body": "Assignee: mabshoff\n\nCurrent when unpickling the pickle jar the files are run through in whatever order os.listdir gives them.  This patch instead unpickles in order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5437\n\n",
    "created_at": "2009-03-04T05:32:31Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] pickle jar -- make it run through in order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5437",
    "user": "was"
}
```
Assignee: mabshoff

Current when unpickling the pickle jar the files are run through in whatever order os.listdir gives them.  This patch instead unpickles in order.

Issue created by migration from https://trac.sagemath.org/ticket/5437





---

archive/issue_comments_042055.json:
```json
{
    "body": "Attachment [trac_5437.patch](tarball://root/attachments/some-uuid/ticket5437/trac_5437.patch) by was created at 2009-03-04 05:33:26",
    "created_at": "2009-03-04T05:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-42055",
    "user": "was"
}
```

Attachment [trac_5437.patch](tarball://root/attachments/some-uuid/ticket5437/trac_5437.patch) by was created at 2009-03-04 05:33:26



---

archive/issue_comments_042056.json:
```json
{
    "body": "Positive reiview.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-42056",
    "user": "mabshoff"
}
```

Positive reiview.

Cheers,

Michael



---

archive/issue_comments_042057.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-42057",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_042058.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-04T19:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5437#issuecomment-42058",
    "user": "mabshoff"
}
```

Resolution: fixed
