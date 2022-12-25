# Issue 3326: trailing question marks in %html blocks are mistreated

archive/issues_003326.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: %html\n\nIn the notebook:\n\n\n```\nsage: %html  How are you?\n```\n\nreturns\n\n```\nNo object 'you' currently defined.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3326\n\n",
    "created_at": "2008-05-28T20:01:47Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "trailing question marks in %html blocks are mistreated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3326",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

Keywords: %html

In the notebook:


```
sage: %html  How are you?
```

returns

```
No object 'you' currently defined.
```



Issue created by migration from https://trac.sagemath.org/ticket/3326





---

archive/issue_comments_023017.json:
```json
{
    "body": "Attachment [trac_3326.patch](tarball://root/attachments/some-uuid/ticket3326/trac_3326.patch) by @mwhansen created at 2009-01-23 12:29:37",
    "created_at": "2009-01-23T12:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23017",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3326.patch](tarball://root/attachments/some-uuid/ticket3326/trac_3326.patch) by @mwhansen created at 2009-01-23 12:29:37



---

archive/issue_comments_023018.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T12:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23018",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023019.json:
```json
{
    "body": "Changing assignee from somebody to @mwhansen.",
    "created_at": "2009-01-23T12:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23019",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from somebody to @mwhansen.



---

archive/issue_comments_023020.json:
```json
{
    "body": "I'm fixing this by making sure that introspection is only done in a Sage cell.\n\nNote that this depends on #5050.",
    "created_at": "2009-01-23T12:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23020",
    "user": "https://github.com/mwhansen"
}
```

I'm fixing this by making sure that introspection is only done in a Sage cell.

Note that this depends on #5050.



---

archive/issue_comments_023021.json:
```json
{
    "body": "The patch fails to apply cleanly to 3.3.alpha1:\n\n```\npatching file sage/server/notebook/worksheet.py\nHunk #4 FAILED at 2575\n1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/worksheet.py.rej\n```\n\nand I can't figure how to fix it by hand to test it out.",
    "created_at": "2009-01-24T16:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23021",
    "user": "https://github.com/jhpalmieri"
}
```

The patch fails to apply cleanly to 3.3.alpha1:

```
patching file sage/server/notebook/worksheet.py
Hunk #4 FAILED at 2575
1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/worksheet.py.rej
```

and I can't figure how to fix it by hand to test it out.



---

archive/issue_comments_023022.json:
```json
{
    "body": "Sorry, I forgot to mention that this also depends on the patch at #3201.",
    "created_at": "2009-01-25T00:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23022",
    "user": "https://github.com/mwhansen"
}
```

Sorry, I forgot to mention that this also depends on the patch at #3201.



---

archive/issue_comments_023023.json:
```json
{
    "body": "This fixes the problem for me.",
    "created_at": "2009-01-25T00:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23023",
    "user": "https://github.com/jhpalmieri"
}
```

This fixes the problem for me.



---

archive/issue_comments_023024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23024",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023025.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
