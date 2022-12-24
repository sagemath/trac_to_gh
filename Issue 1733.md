# Issue 1733: notebook bug -- %foo (or anything else) in a cell by itself (with nothing else in the cell) does not give an error but it *should*

archive/issues_001733.json:
```json
{
    "body": "Assignee: boothby\n\nThis is probably easy to fix in server/notebook/worksheet.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/1733\n\n",
    "created_at": "2008-01-09T08:51:02Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook bug -- %foo (or anything else) in a cell by itself (with nothing else in the cell) does not give an error but it *should*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1733",
    "user": "@williamstein"
}
```
Assignee: boothby

This is probably easy to fix in server/notebook/worksheet.py

Issue created by migration from https://trac.sagemath.org/ticket/1733





---

archive/issue_comments_010971.json:
```json
{
    "body": "Attachment [sage-1733.patch](tarball://root/attachments/some-uuid/ticket1733/sage-1733.patch) by @williamstein created at 2008-05-10 22:55:51",
    "created_at": "2008-05-10T22:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10971",
    "user": "@williamstein"
}
```

Attachment [sage-1733.patch](tarball://root/attachments/some-uuid/ticket1733/sage-1733.patch) by @williamstein created at 2008-05-10 22:55:51



---

archive/issue_comments_010972.json:
```json
{
    "body": "The attached patch:\n\n1. Fixed the problem where %foobar with no input in the cell didn't give an error -- now it does, about\nfoobar not being defined.\n\n2. While I was at it I improved how %foo modes in the notebook work, so that they can have everything on one line, e.g., \n\n```\n   %magma Factorization(9038049823)\n```\n\non a single line works in the notebook.\n\n3. NOTE that the actual patch replaces a bunch of crappy hard to understand code with like 3 simple\n    lines that fix all of the above.",
    "created_at": "2008-05-10T22:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10972",
    "user": "@williamstein"
}
```

The attached patch:

1. Fixed the problem where %foobar with no input in the cell didn't give an error -- now it does, about
foobar not being defined.

2. While I was at it I improved how %foo modes in the notebook work, so that they can have everything on one line, e.g., 

```
   %magma Factorization(9038049823)
```

on a single line works in the notebook.

3. NOTE that the actual patch replaces a bunch of crappy hard to understand code with like 3 simple
    lines that fix all of the above.



---

archive/issue_comments_010973.json:
```json
{
    "body": "Great stuff!  Works well, and makes the code cleaner!",
    "created_at": "2008-05-12T05:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10973",
    "user": "boothby"
}
```

Great stuff!  Works well, and makes the code cleaner!



---

archive/issue_comments_010974.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T11:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10974",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_010975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T11:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10975",
    "user": "mabshoff"
}
```

Resolution: fixed
