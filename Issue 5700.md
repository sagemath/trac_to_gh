# Issue 5700: [with patch, needs review] 3.4.1.rc1: reference manual fixes

archive/issues_005700.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nSince #5555 is not part of Sage, strings like \\ZZ, \\GF{q}, or \\QQ in docstrings lead to errors when processing the PDF version of the reference manual (and lead to strings like \\ZZ, etc., appearing as is in the html version).  This patch changes \\ZZ to \\mathbf{Z}, etc.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5700\n\n",
    "created_at": "2009-04-06T20:41:19Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] 3.4.1.rc1: reference manual fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5700",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Since #5555 is not part of Sage, strings like \ZZ, \GF{q}, or \QQ in docstrings lead to errors when processing the PDF version of the reference manual (and lead to strings like \ZZ, etc., appearing as is in the html version).  This patch changes \ZZ to \mathbf{Z}, etc.


Issue created by migration from https://trac.sagemath.org/ticket/5700





---

archive/issue_comments_044551.json:
```json
{
    "body": "Attachment [5700.patch](tarball://root/attachments/some-uuid/ticket5700/5700.patch) by jhpalmieri created at 2009-04-06 20:42:02",
    "created_at": "2009-04-06T20:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5700#issuecomment-44551",
    "user": "jhpalmieri"
}
```

Attachment [5700.patch](tarball://root/attachments/some-uuid/ticket5700/5700.patch) by jhpalmieri created at 2009-04-06 20:42:02



---

archive/issue_comments_044552.json:
```json
{
    "body": "Does this patch conflict in any way with #5555 or can that patch then be applied later over this one?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T22:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5700#issuecomment-44552",
    "user": "mabshoff"
}
```

Does this patch conflict in any way with #5555 or can that patch then be applied later over this one?

Cheers,

Michael



---

archive/issue_comments_044553.json:
```json
{
    "body": "I intended this one as a stopgap -- use it until #5555 is applied (although the code here will work fine whether #5555 is applied or not -- the two are independent).\n\nIf #5555 gets into Sage first, then this ticket can be ignored.\n\nAlso, #5610 will need to undo the changes in this ticket: part 2 of the patch there contains lots of changes of the sort \\mathbf{Z} --> \\ZZ, to allow users to choose which style of bold face they want.",
    "created_at": "2009-04-06T22:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5700#issuecomment-44553",
    "user": "jhpalmieri"
}
```

I intended this one as a stopgap -- use it until #5555 is applied (although the code here will work fine whether #5555 is applied or not -- the two are independent).

If #5555 gets into Sage first, then this ticket can be ignored.

Also, #5610 will need to undo the changes in this ticket: part 2 of the patch there contains lots of changes of the sort \mathbf{Z} --> \ZZ, to allow users to choose which style of bold face they want.



---

archive/issue_comments_044554.json:
```json
{
    "body": "Ignore this ticket; work on #5555 instead.",
    "created_at": "2009-04-06T23:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5700#issuecomment-44554",
    "user": "jhpalmieri"
}
```

Ignore this ticket; work on #5555 instead.



---

archive/issue_comments_044555.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-04-09T20:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5700#issuecomment-44555",
    "user": "jhpalmieri"
}
```

Resolution: wontfix



---

archive/issue_comments_044556.json:
```json
{
    "body": "As mentioned above, this ticket will be superseded by #5555, so this ticket should not be fixed.  After discussing it with mabshoff on irc, we decided to close this one.",
    "created_at": "2009-04-09T20:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5700#issuecomment-44556",
    "user": "jhpalmieri"
}
```

As mentioned above, this ticket will be superseded by #5555, so this ticket should not be fixed.  After discussing it with mabshoff on irc, we decided to close this one.
