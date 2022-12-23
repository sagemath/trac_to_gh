# Issue 4063: properly escape the titles of worksheets

archive/issues_004063.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mhansen\n\nCurrently the :8102 server has several javascript popups that come up when viewing the list of published worksheets.  Apparently at least one of these worksheets includes javascript code as part of the title.  This is really annoying right now, but could be more dangerous in the future.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4063\n\n",
    "created_at": "2008-09-04T16:22:52Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "properly escape the titles of worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4063",
    "user": "jason"
}
```
Assignee: boothby

CC:  mhansen

Currently the :8102 server has several javascript popups that come up when viewing the list of published worksheets.  Apparently at least one of these worksheets includes javascript code as part of the title.  This is really annoying right now, but could be more dangerous in the future.


Issue created by migration from https://trac.sagemath.org/ticket/4063





---

archive/issue_comments_029305.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-08T13:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29305",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_029306.json:
```json
{
    "body": "Please remove sage-3076_1.patch",
    "created_at": "2008-09-08T13:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29306",
    "user": "TimothyClemans"
}
```

Please remove sage-3076_1.patch



---

archive/issue_comments_029307.json:
```json
{
    "body": "This should really be in 3.1.2. Mike: can you review this?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-16T04:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29307",
    "user": "mabshoff"
}
```

This should really be in 3.1.2. Mike: can you review this?

Cheers,

Michael



---

archive/issue_comments_029308.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-16T06:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29308",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_029309.json:
```json
{
    "body": "I added a few extra cases and added a doctest.  Otherwise, it looks good to me.",
    "created_at": "2008-09-16T06:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29309",
    "user": "mhansen"
}
```

I added a few extra cases and added a doctest.  Otherwise, it looks good to me.



---

archive/issue_comments_029310.json:
```json
{
    "body": "I also agree with Mike's patch. Similar issues might lurk in a couple other places, but this fixes at least one issue that has been known to be abused.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-16T06:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29310",
    "user": "mabshoff"
}
```

I also agree with Mike's patch. Similar issues might lurk in a couple other places, but this fixes at least one issue that has been known to be abused.

Cheers,

Michael



---

archive/issue_comments_029311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-16T06:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29311",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029312.json:
```json
{
    "body": "Merged trac_4063.patch in Sage 3.1.2.rc5",
    "created_at": "2008-09-16T06:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29312",
    "user": "mabshoff"
}
```

Merged trac_4063.patch in Sage 3.1.2.rc5
