# Issue 4280: Syntax error for a comment line, then help query in a notebook cell

archive/issues_004280.json:
```json
{
    "body": "Assignee: boothby\n\nIn Sage (up through 3.1.3rc0), paste this into a notebook cell:\n\n\n```\n#\ngraphs?\n```\n\n\nand you get a syntax error when evaluating.  Removing the comment makes it work fine.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4280\n\n",
    "created_at": "2008-10-14T10:02:49Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Syntax error for a comment line, then help query in a notebook cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4280",
    "user": "@jasongrout"
}
```
Assignee: boothby

In Sage (up through 3.1.3rc0), paste this into a notebook cell:


```
#
graphs?
```


and you get a syntax error when evaluating.  Removing the comment makes it work fine.

Issue created by migration from https://trac.sagemath.org/ticket/4280





---

archive/issue_comments_031307.json:
```json
{
    "body": "Attachment [trac_4820.patch](tarball://root/attachments/some-uuid/ticket4280/trac_4820.patch) by @mwhansen created at 2009-01-24 04:48:38",
    "created_at": "2009-01-24T04:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31307",
    "user": "@mwhansen"
}
```

Attachment [trac_4820.patch](tarball://root/attachments/some-uuid/ticket4280/trac_4820.patch) by @mwhansen created at 2009-01-24 04:48:38



---

archive/issue_comments_031308.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-24T04:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31308",
    "user": "@mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_031309.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T04:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31309",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031310.json:
```json
{
    "body": "This depends on #3326.",
    "created_at": "2009-01-24T04:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31310",
    "user": "@mwhansen"
}
```

This depends on #3326.



---

archive/issue_comments_031311.json:
```json
{
    "body": "This patch fixes the issue and looks correct.    Positive review.",
    "created_at": "2009-02-06T18:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31311",
    "user": "@jasongrout"
}
```

This patch fixes the issue and looks correct.    Positive review.



---

archive/issue_comments_031312.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T01:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31312",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_031313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-07T01:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4280#issuecomment-31313",
    "user": "mabshoff"
}
```

Resolution: fixed
