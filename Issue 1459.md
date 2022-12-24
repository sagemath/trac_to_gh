# Issue 1459: [with patch] make notebook ?? behavior like command line behavior

archive/issues_001459.json:
```json
{
    "body": "Assignee: mhansen\n\nOn the command-line, if a class docstring is not found, then the one from __init__ is used.  This does not happen in the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1459\n\n",
    "created_at": "2007-12-11T10:43:44Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "[with patch] make notebook ?? behavior like command line behavior",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1459",
    "user": "mhansen"
}
```
Assignee: mhansen

On the command-line, if a class docstring is not found, then the one from __init__ is used.  This does not happen in the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/1459





---

archive/issue_comments_009401.json:
```json
{
    "body": "Attachment [1267-2.patch](tarball://root/attachments/some-uuid/ticket1459/1267-2.patch) by rlm created at 2007-12-21 01:11:16\n\nThis fixes doctest formatting.",
    "created_at": "2007-12-21T01:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1459#issuecomment-9401",
    "user": "rlm"
}
```

Attachment [1267-2.patch](tarball://root/attachments/some-uuid/ticket1459/1267-2.patch) by rlm created at 2007-12-21 01:11:16

This fixes doctest formatting.



---

archive/issue_comments_009402.json:
```json
{
    "body": "Attachment [1459-doc.patch](tarball://root/attachments/some-uuid/ticket1459/1459-doc.patch) by rlm created at 2007-12-21 01:13:35\n\nYou should make sure to run doctests (no pun intended):\n\n```\n**********************************************************************\nFile \"sageinspect.py\", line 404:\n    sage: sage_getdoc(None)\nExpected:\n    ''\nGot:\n    'x.__init__(...) initializes x; see x.__class__.__doc__ for signature'\n**********************************************************************\n```\n",
    "created_at": "2007-12-21T01:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1459#issuecomment-9402",
    "user": "rlm"
}
```

Attachment [1459-doc.patch](tarball://root/attachments/some-uuid/ticket1459/1459-doc.patch) by rlm created at 2007-12-21 01:13:35

You should make sure to run doctests (no pun intended):

```
**********************************************************************
File "sageinspect.py", line 404:
    sage: sage_getdoc(None)
Expected:
    ''
Got:
    'x.__init__(...) initializes x; see x.__class__.__doc__ for signature'
**********************************************************************
```




---

archive/issue_comments_009403.json:
```json
{
    "body": "mhansen also speculates that the patch above should also fix #1565.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-22T15:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1459#issuecomment-9403",
    "user": "mabshoff"
}
```

mhansen also speculates that the patch above should also fix #1565.

Cheers,

Michael



---

archive/issue_comments_009404.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1459#issuecomment-9404",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_009405.json:
```json
{
    "body": "merged in 2.9.1 rc0\n\nadded\n`if obj is None: return ''`",
    "created_at": "2007-12-22T18:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1459#issuecomment-9405",
    "user": "rlm"
}
```

merged in 2.9.1 rc0

added
`if obj is None: return ''`
