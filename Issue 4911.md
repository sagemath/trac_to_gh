# Issue 4911: convert sage.games.* docstrings to Sphinx

archive/issues_004911.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4911\n\n",
    "created_at": "2009-01-01T22:51:10Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.games.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4911",
    "user": "@mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4911





---

archive/issue_comments_037270.json:
```json
{
    "body": "Attachment [trac_4911.patch](tarball://root/attachments/some-uuid/ticket4911/trac_4911.patch) by @mwhansen created at 2009-01-02 02:24:45",
    "created_at": "2009-01-02T02:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4911#issuecomment-37270",
    "user": "@mwhansen"
}
```

Attachment [trac_4911.patch](tarball://root/attachments/some-uuid/ticket4911/trac_4911.patch) by @mwhansen created at 2009-01-02 02:24:45



---

archive/issue_comments_037271.json:
```json
{
    "body": "line 56: \"`contains the :math:`i`,:math:`j` position`\" is not being rendered properly.  Maybe replace it with \"`contains the :math:`i,j` position`\".\n\nActually, why do you need :math: here at all?  I don't remember seeing it in the other files that I've looked at...",
    "created_at": "2009-01-07T22:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4911#issuecomment-37271",
    "user": "@jhpalmieri"
}
```

line 56: "`contains the :math:`i`,:math:`j` position`" is not being rendered properly.  Maybe replace it with "`contains the :math:`i,j` position`".

Actually, why do you need :math: here at all?  I don't remember seeing it in the other files that I've looked at...



---

archive/issue_comments_037272.json:
```json
{
    "body": "Attachment [trac_4911-2.patch](tarball://root/attachments/some-uuid/ticket4911/trac_4911-2.patch) by @mwhansen created at 2009-01-08 21:16:25\n\nI've posted a patch which fixes this issue.  The :math: was there because I had forgot to go through this file and remove them.",
    "created_at": "2009-01-08T21:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4911#issuecomment-37272",
    "user": "@mwhansen"
}
```

Attachment [trac_4911-2.patch](tarball://root/attachments/some-uuid/ticket4911/trac_4911-2.patch) by @mwhansen created at 2009-01-08 21:16:25

I've posted a patch which fixes this issue.  The :math: was there because I had forgot to go through this file and remove them.



---

archive/issue_comments_037273.json:
```json
{
    "body": "Great, positive review.",
    "created_at": "2009-01-08T23:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4911#issuecomment-37273",
    "user": "@jhpalmieri"
}
```

Great, positive review.



---

archive/issue_comments_037274.json:
```json
{
    "body": "Attachment [sage.games-final.patch](tarball://root/attachments/some-uuid/ticket4911/sage.games-final.patch) by mabshoff created at 2009-02-24 18:01:53\n\nMerged sage.games-final.patch in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4911#issuecomment-37274",
    "user": "mabshoff"
}
```

Attachment [sage.games-final.patch](tarball://root/attachments/some-uuid/ticket4911/sage.games-final.patch) by mabshoff created at 2009-02-24 18:01:53

Merged sage.games-final.patch in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_037275.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4911#issuecomment-37275",
    "user": "mabshoff"
}
```

Resolution: fixed
