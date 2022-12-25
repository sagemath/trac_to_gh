# Issue 4280: [with patch, positive review] Syntax error for a comment line, then help query in a notebook cell

archive/issues_004280.json:
```json
{
    "body": "Assignee: @mwhansen\n\nIn Sage (up through 3.1.3rc0), paste this into a notebook cell:\n\n```\n#\ngraphs?\n```\n\nand you get a syntax error when evaluating.  Removing the comment makes it work fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4280\n\n",
    "closed_at": "2009-02-07T01:37:18Z",
    "created_at": "2008-10-14T10:02:49Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] Syntax error for a comment line, then help query in a notebook cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4280",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

In Sage (up through 3.1.3rc0), paste this into a notebook cell:

```
#
graphs?
```

and you get a syntax error when evaluating.  Removing the comment makes it work fine.

Issue created by migration from https://trac.sagemath.org/ticket/4280





---

archive/issue_comments_031245.json:
```json
{
    "body": "Attachment [trac_4820.patch](tarball://root/attachments/some-uuid/ticket4280/trac_4820.patch) by @mwhansen created at 2009-01-24 04:48:38",
    "created_at": "2009-01-24T04:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31245",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4820.patch](tarball://root/attachments/some-uuid/ticket4280/trac_4820.patch) by @mwhansen created at 2009-01-24 04:48:38



---

archive/issue_comments_031246.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-24T04:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31246",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_031247.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T04:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31247",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031248.json:
```json
{
    "body": "This depends on #3326.",
    "created_at": "2009-01-24T04:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31248",
    "user": "https://github.com/mwhansen"
}
```

This depends on #3326.



---

archive/issue_comments_031249.json:
```json
{
    "body": "This patch fixes the issue and looks correct.    Positive review.",
    "created_at": "2009-02-06T18:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31249",
    "user": "https://github.com/jasongrout"
}
```

This patch fixes the issue and looks correct.    Positive review.



---

archive/issue_events_009667.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-07T01:37:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4280#event-9667"
}
```



---

archive/issue_comments_031250.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T01:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_031251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-07T01:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009668.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-07T01:37:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4280#event-9668"
}
```
