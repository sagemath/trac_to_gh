# Issue 3986: notebook -- a doc browser bug

archive/issues_003986.json:
```json
{
    "body": "Assignee: boothby\n\n1. Go to any interactive help sheet in the notebook.\n\n2. Go the very very bottom cell, below the text.\n\n3. Press shift enter.\n\n4. I get this traceback in the server log:\n\n```\n...\n\t    cell.evaluate(username = self.username)\n\texceptions.AttributeError: TextCell instance has no attribute 'evaluate'\n```\n\n\nIt's bad form getting tracebacks in the server log, though everything continues\nto work fine.   The fix is to figure out why a text cell is having evaluate called\non it.  Is the bottom cell somehow incorrectly set to be a text cell?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3986\n\n",
    "created_at": "2008-08-29T04:58:19Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- a doc browser bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3986",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

1. Go to any interactive help sheet in the notebook.

2. Go the very very bottom cell, below the text.

3. Press shift enter.

4. I get this traceback in the server log:

```
...
	    cell.evaluate(username = self.username)
	exceptions.AttributeError: TextCell instance has no attribute 'evaluate'
```


It's bad form getting tracebacks in the server log, though everything continues
to work fine.   The fix is to figure out why a text cell is having evaluate called
on it.  Is the bottom cell somehow incorrectly set to be a text cell?

Issue created by migration from https://trac.sagemath.org/ticket/3986





---

archive/issue_comments_028610.json:
```json
{
    "body": "Is this still a problem?",
    "created_at": "2009-08-10T09:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3986#issuecomment-28610",
    "user": "https://github.com/qed777"
}
```

Is this still a problem?



---

archive/issue_comments_028611.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-10-15T18:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3986#issuecomment-28611",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_028612.json:
```json
{
    "body": "This doesn't seem to be a problem in sagenb-0.6.",
    "created_at": "2010-01-19T11:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3986#issuecomment-28612",
    "user": "https://github.com/TimDumol"
}
```

This doesn't seem to be a problem in sagenb-0.6.



---

archive/issue_comments_028613.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-19T11:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3986#issuecomment-28613",
    "user": "https://github.com/TimDumol"
}
```

Resolution: invalid
