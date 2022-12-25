# Issue 1733: [with patch; positive review] notebook bug -- %foo (or anything else) in a cell by itself (with nothing else in the cell) does not give an error but it *should*

archive/issues_001733.json:
```json
{
    "body": "Assignee: boothby\n\nThis is probably easy to fix in server/notebook/worksheet.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/1733\n\n",
    "closed_at": "2008-05-12T11:03:18Z",
    "created_at": "2008-01-09T08:51:02Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; positive review] notebook bug -- %foo (or anything else) in a cell by itself (with nothing else in the cell) does not give an error but it *should*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1733",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

This is probably easy to fix in server/notebook/worksheet.py

Issue created by migration from https://trac.sagemath.org/ticket/1733





---

archive/issue_comments_010944.json:
```json
{
    "body": "Attachment [sage-1733.patch](tarball://root/attachments/some-uuid/ticket1733/sage-1733.patch) by @williamstein created at 2008-05-10 22:55:51",
    "created_at": "2008-05-10T22:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10944",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-1733.patch](tarball://root/attachments/some-uuid/ticket1733/sage-1733.patch) by @williamstein created at 2008-05-10 22:55:51



---

archive/issue_comments_010945.json:
```json
{
    "body": "The attached patch:\n\n1. Fixed the problem where %foobar with no input in the cell didn't give an error -- now it does, about\nfoobar not being defined.\n\n2. While I was at it I improved how %foo modes in the notebook work, so that they can have everything on one line, e.g., \n\n```\n   %magma Factorization(9038049823)\n```\non a single line works in the notebook.\n\n3. NOTE that the actual patch replaces a bunch of crappy hard to understand code with like 3 simple\n    lines that fix all of the above.",
    "created_at": "2008-05-10T22:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10945",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_010946.json:
```json
{
    "body": "Great stuff!  Works well, and makes the code cleaner!",
    "created_at": "2008-05-12T05:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10946",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Great stuff!  Works well, and makes the code cleaner!



---

archive/issue_events_004210.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-12T11:03:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1733#event-4210"
}
```



---

archive/issue_comments_010947.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T11:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10947",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_010948.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T11:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1733#issuecomment-10948",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
