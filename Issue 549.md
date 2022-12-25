# Issue 549: print statement doesn't leave blank line in notebook

archive/issues_000549.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook, the following code:\n\n\n```\nprint \"abc\"\nprint\nprint \"def\"\n```\n\n\ndisplays\n\n\n```\nabc\ndef\n```\n\n\ninstead of\n\n\n```\nabc\n\ndef\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/549\n\n",
    "created_at": "2007-09-01T02:18:33Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "print statement doesn't leave blank line in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/549",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: boothby

In the notebook, the following code:


```
print "abc"
print
print "def"
```


displays


```
abc
def
```


instead of


```
abc

def
```



Issue created by migration from https://trac.sagemath.org/ticket/549





---

archive/issue_comments_002814.json:
```json
{
    "body": "This might be Bug Day 2 material, otherwise we will retag it for 2.9.x.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-05T16:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2814",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This might be Bug Day 2 material, otherwise we will retag it for 2.9.x.

Cheers,

Michael



---

archive/issue_events_001460.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-05T16:59:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/549#event-1460"
}
```



---

archive/issue_comments_002815.json:
```json
{
    "body": "Fixed by patch:\n\n[http://128.208.160.195/home/boothby/notebook549.hg](http://128.208.160.195/home/boothby/notebook549.hg)",
    "created_at": "2007-09-06T18:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2815",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Fixed by patch:

[http://128.208.160.195/home/boothby/notebook549.hg](http://128.208.160.195/home/boothby/notebook549.hg)



---

archive/issue_comments_002816.json:
```json
{
    "body": "This is fixed -- but it caused #601.",
    "created_at": "2007-09-06T19:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2816",
    "user": "https://github.com/williamstein"
}
```

This is fixed -- but it caused #601.



---

archive/issue_events_001461.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-06T19:03:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/549#event-1461"
}
```



---

archive/issue_comments_002817.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T19:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2817",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
