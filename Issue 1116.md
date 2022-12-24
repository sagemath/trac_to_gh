# Issue 1116: sage -sdist recreates certain empty files in local/bin

archive/issues_001116.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/bin$ hg status\n? sage-cleaner.orig\n? sage-clone.orig\n? sage-lo\n? sage-make\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1116\n\n",
    "created_at": "2007-11-06T22:26:03Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage -sdist recreates certain empty files in local/bin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1116",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/bin$ hg status
? sage-cleaner.orig
? sage-clone.orig
? sage-lo
? sage-make
```


Issue created by migration from https://trac.sagemath.org/ticket/1116





---

archive/issue_comments_006748.json:
```json
{
    "body": "This annoys me and causes the $SAGE_LOCAL/bin/ repo to report files with unclear status.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1116#issuecomment-6748",
    "user": "mabshoff"
}
```

This annoys me and causes the $SAGE_LOCAL/bin/ repo to report files with unclear status.

Cheers,

Michael



---

archive/issue_comments_006749.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-15T22:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1116#issuecomment-6749",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006750.json:
```json
{
    "body": "I removed the offending files from the sage_scripts repo. Once 2.10.2.alpha1 is out we ought to verify that the problem is really gone.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1116#issuecomment-6750",
    "user": "mabshoff"
}
```

I removed the offending files from the sage_scripts repo. Once 2.10.2.alpha1 is out we ought to verify that the problem is really gone.

Cheers,

Michael



---

archive/issue_comments_006751.json:
```json
{
    "body": "I did some testing and it seems to work. I will reopen in case it turns out to be an incomplete fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T04:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1116#issuecomment-6751",
    "user": "mabshoff"
}
```

I did some testing and it seems to work. I will reopen in case it turns out to be an incomplete fix.

Cheers,

Michael



---

archive/issue_comments_006752.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T04:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1116#issuecomment-6752",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006753.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T04:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1116#issuecomment-6753",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
