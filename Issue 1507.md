# Issue 1507: [with patch] plotting -- document how to use pylab / matlab style plotting from sage

archive/issues_001507.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1507\n\n",
    "created_at": "2007-12-14T17:53:05Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] plotting -- document how to use pylab / matlab style plotting from sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1507",
    "user": "@williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/1507





---

archive/issue_comments_009648.json:
```json
{
    "body": "this is *only* a documentation addition -- no code, so should be easy to referee.",
    "created_at": "2007-12-14T17:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9648",
    "user": "@williamstein"
}
```

this is *only* a documentation addition -- no code, so should be easy to referee.



---

archive/issue_comments_009649.json:
```json
{
    "body": "Attachment [trac-1507.patch](tarball://root/attachments/some-uuid/ticket1507/trac-1507.patch) by @williamstein created at 2007-12-14 17:58:26",
    "created_at": "2007-12-14T17:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9649",
    "user": "@williamstein"
}
```

Attachment [trac-1507.patch](tarball://root/attachments/some-uuid/ticket1507/trac-1507.patch) by @williamstein created at 2007-12-14 17:58:26



---

archive/issue_comments_009650.json:
```json
{
    "body": "If the second hunk fails, no problem.  That's not relevant.  Only the first big\nhunk is.",
    "created_at": "2007-12-14T17:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9650",
    "user": "@williamstein"
}
```

If the second hunk fails, no problem.  That's not relevant.  Only the first big
hunk is.



---

archive/issue_comments_009651.json:
```json
{
    "body": "Looks good to me.  \n\nTo apply: Attempt to apply the patch as usual.  Ignore the error message:\n\n```\nHunk #2 FAILED at 127\n1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\nabort: patch failed to apply\n```\n\n\nThen do `hg_sage.ci()`, to check in the half-applied patch.",
    "created_at": "2007-12-15T06:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9651",
    "user": "cwitty"
}
```

Looks good to me.  

To apply: Attempt to apply the patch as usual.  Ignore the error message:

```
Hunk #2 FAILED at 127
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```


Then do `hg_sage.ci()`, to check in the half-applied patch.



---

archive/issue_comments_009652.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T06:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9652",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009653.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T06:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1507#issuecomment-9653",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.
