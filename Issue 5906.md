# Issue 5906: "libpng error: Image width or height is zero in IHDR" when plotting CompleteGraph(2)

archive/issues_005906.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis came up in https://groups.google.com/group/sage-devel/t/d9b64b5ddc24bb6b\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: g = graphs.CompleteGraph(2)\nsage: g.show()\nlibpng error: Image width or height is zero in IHDR\n<SNIP>\n```\n\n| Sage Version 3.4.1, Release Date: 2009-04-21                       |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5906\n\n",
    "created_at": "2009-04-26T21:47:04Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "\"libpng error: Image width or height is zero in IHDR\" when plotting CompleteGraph(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5906",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @rlmill

This came up in https://groups.google.com/group/sage-devel/t/d9b64b5ddc24bb6b

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: g = graphs.CompleteGraph(2)
sage: g.show()
libpng error: Image width or height is zero in IHDR
<SNIP>
```

| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5906





---

archive/issue_comments_046596.json:
```json
{
    "body": "Attachment [trac_5906.patch](tarball://root/attachments/some-uuid/ticket5906/trac_5906.patch) by @rlmill created at 2009-04-27 16:10:10",
    "created_at": "2009-04-27T16:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5906#issuecomment-46596",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5906.patch](tarball://root/attachments/some-uuid/ticket5906/trac_5906.patch) by @rlmill created at 2009-04-27 16:10:10



---

archive/issue_comments_046597.json:
```json
{
    "body": "Ooops, I forgot to review this for 3.4.2, but positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T18:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5906#issuecomment-46597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, I forgot to review this for 3.4.2, but positive review.

Cheers,

Michael



---

archive/issue_comments_046598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T18:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5906#issuecomment-46598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046599.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T18:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5906#issuecomment-46599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_013856.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-04T18:41:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5906",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5906#event-13856"
}
```
