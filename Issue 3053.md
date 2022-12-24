# Issue 3053: notebook -- new cell_resize doesn't respect %hide at the beginning of a cell

archive/issues_003053.json:
```json
{
    "body": "Assignee: boothby\n\nIf a cell starts with %hide, it should not be shown unless it is in focus.  The new cell_resize code doesn't respect this.  To see this:\n\n1. Load a fresh worksheet with %hide's -- none of them are hidden.  Click on input cells then out  hide them.\n\n2. Resize a web browser window with %hides -- suddenly all %hide inputs are shown.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3053\n\n",
    "created_at": "2008-04-29T06:23:58Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook -- new cell_resize doesn't respect %hide at the beginning of a cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3053",
    "user": "@williamstein"
}
```
Assignee: boothby

If a cell starts with %hide, it should not be shown unless it is in focus.  The new cell_resize code doesn't respect this.  To see this:

1. Load a fresh worksheet with %hide's -- none of them are hidden.  Click on input cells then out  hide them.

2. Resize a web browser window with %hides -- suddenly all %hide inputs are shown.

Issue created by migration from https://trac.sagemath.org/ticket/3053





---

archive/issue_comments_021080.json:
```json
{
    "body": "Attachment [sage-3053.patch](tarball://root/attachments/some-uuid/ticket3053/sage-3053.patch) by @williamstein created at 2008-05-11 01:59:00",
    "created_at": "2008-05-11T01:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3053#issuecomment-21080",
    "user": "@williamstein"
}
```

Attachment [sage-3053.patch](tarball://root/attachments/some-uuid/ticket3053/sage-3053.patch) by @williamstein created at 2008-05-11 01:59:00



---

archive/issue_comments_021081.json:
```json
{
    "body": "Attached patch does this:\n\ntrac #3053 --  new cell_resize doesn't respect %hide at the beginning of a cell\n1. Fix the listed problem. \n2. Fix the %hide styling a bit; make %hide be grey\n3. Make %hide work consistently on new page refresh versus in a running worksheet\n4. Make cell be resized when clicking on an input area.  This makes editing\n   a %hide much more natural.",
    "created_at": "2008-05-11T01:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3053#issuecomment-21081",
    "user": "@williamstein"
}
```

Attached patch does this:

trac #3053 --  new cell_resize doesn't respect %hide at the beginning of a cell
1. Fix the listed problem. 
2. Fix the %hide styling a bit; make %hide be grey
3. Make %hide work consistently on new page refresh versus in a running worksheet
4. Make cell be resized when clicking on an input area.  This makes editing
   a %hide much more natural.



---

archive/issue_comments_021082.json:
```json
{
    "body": "nice!",
    "created_at": "2008-05-12T06:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3053#issuecomment-21082",
    "user": "boothby"
}
```

nice!



---

archive/issue_comments_021083.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-12T11:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3053#issuecomment-21083",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_021084.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T11:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3053#issuecomment-21084",
    "user": "mabshoff"
}
```

Resolution: fixed
