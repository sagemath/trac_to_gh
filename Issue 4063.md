# Issue 4063: properly escape the titles of worksheets

archive/issues_004063.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @mwhansen\n\nCurrently the :8102 server has several javascript popups that come up when viewing the list of published worksheets.  Apparently at least one of these worksheets includes javascript code as part of the title.  This is really annoying right now, but could be more dangerous in the future.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4063\n\n",
    "created_at": "2008-09-04T16:22:52Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "properly escape the titles of worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4063",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @mwhansen

Currently the :8102 server has several javascript popups that come up when viewing the list of published worksheets.  Apparently at least one of these worksheets includes javascript code as part of the title.  This is really annoying right now, but could be more dangerous in the future.


Issue created by migration from https://trac.sagemath.org/ticket/4063





---

archive/issue_comments_029246.json:
```json
{
    "body": "Attachment [sage-4063_1.patch](tarball://root/attachments/some-uuid/ticket4063/sage-4063_1.patch) by TimothyClemans created at 2008-09-08 13:56:07",
    "created_at": "2008-09-08T13:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29246",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4063_1.patch](tarball://root/attachments/some-uuid/ticket4063/sage-4063_1.patch) by TimothyClemans created at 2008-09-08 13:56:07



---

archive/issue_comments_029247.json:
```json
{
    "body": "Please remove sage-3076_1.patch",
    "created_at": "2008-09-08T13:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29247",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Please remove sage-3076_1.patch



---

archive/issue_comments_029248.json:
```json
{
    "body": "This should really be in 3.1.2. Mike: can you review this?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-16T04:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This should really be in 3.1.2. Mike: can you review this?

Cheers,

Michael



---

archive/issue_comments_029249.json:
```json
{
    "body": "Attachment [trac_4063.patch](tarball://root/attachments/some-uuid/ticket4063/trac_4063.patch) by @mwhansen created at 2008-09-16 06:30:14",
    "created_at": "2008-09-16T06:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29249",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4063.patch](tarball://root/attachments/some-uuid/ticket4063/trac_4063.patch) by @mwhansen created at 2008-09-16 06:30:14



---

archive/issue_comments_029250.json:
```json
{
    "body": "I added a few extra cases and added a doctest.  Otherwise, it looks good to me.",
    "created_at": "2008-09-16T06:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29250",
    "user": "https://github.com/mwhansen"
}
```

I added a few extra cases and added a doctest.  Otherwise, it looks good to me.



---

archive/issue_comments_029251.json:
```json
{
    "body": "I also agree with Mike's patch. Similar issues might lurk in a couple other places, but this fixes at least one issue that has been known to be abused.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-16T06:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I also agree with Mike's patch. Similar issues might lurk in a couple other places, but this fixes at least one issue that has been known to be abused.

Cheers,

Michael



---

archive/issue_comments_029252.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-16T06:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029253.json:
```json
{
    "body": "Merged trac_4063.patch in Sage 3.1.2.rc5",
    "created_at": "2008-09-16T06:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4063#issuecomment-29253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_4063.patch in Sage 3.1.2.rc5
