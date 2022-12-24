# Issue 3205: when the notebook scrolls to a new cell that is created, the jsmath box obscures the bottom cell

archive/issues_003205.json:
```json
{
    "body": "Assignee: boothby\n\nWhen scrolling through the notebook with the cursor keys (i.e., moving from cell to cell), if you move to a cell below the currently visible ones, the browser automatically scrolls down to let you see the new cell, but the jsmath box is sitting right there at the start of the cell, so you can't see what is in the start of the cell.\n\nFix 1: scroll a bit more than we do now\n\nFix 2: move the jsmath box to the bottom right instead of the bottom left\n\nFix 3: Get rid of the jsmath box and instead just make a menu option or some other way to access the jsmath controls.  Once the jsmath controls are set, they are very rarely accessed, at least for me.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3205\n\n",
    "created_at": "2008-05-14T21:55:56Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "when the notebook scrolls to a new cell that is created, the jsmath box obscures the bottom cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3205",
    "user": "jason"
}
```
Assignee: boothby

When scrolling through the notebook with the cursor keys (i.e., moving from cell to cell), if you move to a cell below the currently visible ones, the browser automatically scrolls down to let you see the new cell, but the jsmath box is sitting right there at the start of the cell, so you can't see what is in the start of the cell.

Fix 1: scroll a bit more than we do now

Fix 2: move the jsmath box to the bottom right instead of the bottom left

Fix 3: Get rid of the jsmath box and instead just make a menu option or some other way to access the jsmath controls.  Once the jsmath controls are set, they are very rarely accessed, at least for me.


Issue created by migration from https://trac.sagemath.org/ticket/3205





---

archive/issue_comments_022155.json:
```json
{
    "body": "Attachment [sage-3205-jsmath-button.patch](tarball://root/attachments/some-uuid/ticket3205/sage-3205-jsmath-button.patch) by jason created at 2008-05-14 22:21:28",
    "created_at": "2008-05-14T22:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3205#issuecomment-22155",
    "user": "jason"
}
```

Attachment [sage-3205-jsmath-button.patch](tarball://root/attachments/some-uuid/ticket3205/sage-3205-jsmath-button.patch) by jason created at 2008-05-14 22:21:28



---

archive/issue_comments_022156.json:
```json
{
    "body": "Works for me in FF and Opera.  Need review from IE / Safari.",
    "created_at": "2008-06-15T00:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3205#issuecomment-22156",
    "user": "boothby"
}
```

Works for me in FF and Opera.  Need review from IE / Safari.



---

archive/issue_comments_022157.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-15T21:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3205#issuecomment-22157",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_022158.json:
```json
{
    "body": "I tested this in IE and Safari and everything looks good.",
    "created_at": "2008-06-19T19:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3205#issuecomment-22158",
    "user": "mhansen"
}
```

I tested this in IE and Safari and everything looks good.



---

archive/issue_comments_022159.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T12:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3205#issuecomment-22159",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha0



---

archive/issue_comments_022160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T12:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3205#issuecomment-22160",
    "user": "mabshoff"
}
```

Resolution: fixed
