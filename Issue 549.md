# Issue 549: print statement doesn't leave blank line in notebook

archive/issues_000549.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook, the following code:\n\n\n```\nprint \"abc\"\nprint\nprint \"def\"\n```\n\n\ndisplays\n\n\n```\nabc\ndef\n```\n\n\ninstead of\n\n\n```\nabc\n\ndef\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/549\n\n",
    "created_at": "2007-09-01T02:18:33Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "print statement doesn't leave blank line in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/549",
    "user": "dmharvey"
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

archive/issue_comments_002826.json:
```json
{
    "body": "This might be Bug Day 2 material, otherwise we will retag it for 2.9.x.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-05T16:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2826",
    "user": "mabshoff"
}
```

This might be Bug Day 2 material, otherwise we will retag it for 2.9.x.

Cheers,

Michael



---

archive/issue_comments_002827.json:
```json
{
    "body": "Fixed by patch:\n\n[http://128.208.160.195/home/boothby/notebook549.hg](http://128.208.160.195/home/boothby/notebook549.hg)",
    "created_at": "2007-09-06T18:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2827",
    "user": "boothby"
}
```

Fixed by patch:

[http://128.208.160.195/home/boothby/notebook549.hg](http://128.208.160.195/home/boothby/notebook549.hg)



---

archive/issue_comments_002828.json:
```json
{
    "body": "This is fixed -- but it caused #601.",
    "created_at": "2007-09-06T19:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2828",
    "user": "was"
}
```

This is fixed -- but it caused #601.



---

archive/issue_comments_002829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T19:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/549#issuecomment-2829",
    "user": "was"
}
```

Resolution: fixed
