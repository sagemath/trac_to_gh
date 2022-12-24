# Issue 3326: trailing question marks in %html blocks are mistreated

archive/issues_003326.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: %html\n\nIn the notebook:\n\n\n```\nsage: %html  How are you?\n```\n\nreturns\n\n```\nNo object 'you' currently defined.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3326\n\n",
    "created_at": "2008-05-28T20:01:47Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "trailing question marks in %html blocks are mistreated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3326",
    "user": "jhpalmieri"
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

archive/issue_comments_023065.json:
```json
{
    "body": "Attachment [trac_3326.patch](tarball://root/attachments/some-uuid/ticket3326/trac_3326.patch) by mhansen created at 2009-01-23 12:29:37",
    "created_at": "2009-01-23T12:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23065",
    "user": "mhansen"
}
```

Attachment [trac_3326.patch](tarball://root/attachments/some-uuid/ticket3326/trac_3326.patch) by mhansen created at 2009-01-23 12:29:37



---

archive/issue_comments_023066.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T12:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23066",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023067.json:
```json
{
    "body": "Changing assignee from somebody to mhansen.",
    "created_at": "2009-01-23T12:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23067",
    "user": "mhansen"
}
```

Changing assignee from somebody to mhansen.



---

archive/issue_comments_023068.json:
```json
{
    "body": "I'm fixing this by making sure that introspection is only done in a Sage cell.\n\nNote that this depends on #5050.",
    "created_at": "2009-01-23T12:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23068",
    "user": "mhansen"
}
```

I'm fixing this by making sure that introspection is only done in a Sage cell.

Note that this depends on #5050.



---

archive/issue_comments_023069.json:
```json
{
    "body": "The patch fails to apply cleanly to 3.3.alpha1:\n\n```\npatching file sage/server/notebook/worksheet.py\nHunk #4 FAILED at 2575\n1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/worksheet.py.rej\n```\n\nand I can't figure how to fix it by hand to test it out.",
    "created_at": "2009-01-24T16:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23069",
    "user": "jhpalmieri"
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

archive/issue_comments_023070.json:
```json
{
    "body": "Sorry, I forgot to mention that this also depends on the patch at #3201.",
    "created_at": "2009-01-25T00:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23070",
    "user": "mhansen"
}
```

Sorry, I forgot to mention that this also depends on the patch at #3201.



---

archive/issue_comments_023071.json:
```json
{
    "body": "This fixes the problem for me.",
    "created_at": "2009-01-25T00:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23071",
    "user": "jhpalmieri"
}
```

This fixes the problem for me.



---

archive/issue_comments_023072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23072",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023073.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T15:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3326#issuecomment-23073",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
