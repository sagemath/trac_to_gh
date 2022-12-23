# Issue 3472: Running sage from a non-existent directory pretends to work

archive/issues_003472.json:
```json
{
    "body": "Assignee: craigcitro\n\nRunning sage from a directory that doesn't exist thinks it's working, but really just fails. I'm attaching a new `$SAGE_ROOT/sage` replacement that checks this on startup.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3472\n\n",
    "created_at": "2008-06-19T21:13:49Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Running sage from a non-existent directory pretends to work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3472",
    "user": "craigcitro"
}
```
Assignee: craigcitro

Running sage from a directory that doesn't exist thinks it's working, but really just fails. I'm attaching a new `$SAGE_ROOT/sage` replacement that checks this on startup.

Issue created by migration from https://trac.sagemath.org/ticket/3472





---

archive/issue_comments_024477.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-26T06:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24477",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_024478.json:
```json
{
    "body": "Positive review to the changes made by Craig. As it turned out `sage -upgrade` does not fix (this is now #3517)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-27T00:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24478",
    "user": "mabshoff"
}
```

Positive review to the changes made by Craig. As it turned out `sage -upgrade` does not fix (this is now #3517)

Cheers,

Michael



---

archive/issue_comments_024479.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-27T00:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24479",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024480.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-27T00:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3472#issuecomment-24480",
    "user": "mabshoff"
}
```

Resolution: fixed
