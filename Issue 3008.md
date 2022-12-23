# Issue 3008: first cell in notebook is undeletable

archive/issues_003008.json:
```json
{
    "body": "Assignee: somebody\n\nThe top cell in a notebook worksheet cannot be deleted by backspace.  A workaround is ctrl-backspace from the next cell, but that is annoyingly indirect.  I have tried this on both Safari and Firefox on OS X, but not other platforms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3008\n\n",
    "created_at": "2008-04-23T18:44:30Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "first cell in notebook is undeletable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3008",
    "user": "mhampton"
}
```
Assignee: somebody

The top cell in a notebook worksheet cannot be deleted by backspace.  A workaround is ctrl-backspace from the next cell, but that is annoyingly indirect.  I have tried this on both Safari and Firefox on OS X, but not other platforms.

Issue created by migration from https://trac.sagemath.org/ticket/3008





---

archive/issue_comments_020684.json:
```json
{
    "body": "Attachment\n\nThis patch:\n\n```\nFix trac #3008 -- Fix delete first cell bug. Also:\n  2. Make deleting/merging cells via control-backspace feel slightly snappier\n  3. Improve the documentation in js.py for the join_cell function.\n```\n",
    "created_at": "2008-05-10T23:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20684",
    "user": "was"
}
```

Attachment

This patch:

```
Fix trac #3008 -- Fix delete first cell bug. Also:
  2. Make deleting/merging cells via control-backspace feel slightly snappier
  3. Improve the documentation in js.py for the join_cell function.
```




---

archive/issue_comments_020685.json:
```json
{
    "body": "The attached patch works for me, looks good.  Positive review.",
    "created_at": "2008-05-11T12:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20685",
    "user": "mhampton"
}
```

The attached patch works for me, looks good.  Positive review.



---

archive/issue_comments_020686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T12:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20686",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020687.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T12:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20687",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0
