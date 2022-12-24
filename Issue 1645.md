# Issue 1645: erf doesn't evaluate with intervals

archive/issues_001645.json:
```json
{
    "body": "Assignee: jkantor\n\nThis should either raise an error or give a result:\n\n\n\n```\na = RealInterval('2.3')\nerf(a)\n```\n\n\n\nCPU is at about 0%, so it is doing nothing.\n----\nmaybe there are other unsupported functions, should be checked out!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1645\n\n",
    "created_at": "2007-12-31T12:05:23Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "erf doesn't evaluate with intervals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1645",
    "user": "schilly"
}
```
Assignee: jkantor

This should either raise an error or give a result:



```
a = RealInterval('2.3')
erf(a)
```



CPU is at about 0%, so it is doing nothing.
----
maybe there are other unsupported functions, should be checked out!

Issue created by migration from https://trac.sagemath.org/ticket/1645





---

archive/issue_comments_010464.json:
```json
{
    "body": "Attachment [trac-1645.patch](tarball://root/attachments/some-uuid/ticket1645/trac-1645.patch) by was created at 2008-01-02 06:12:12\n\nThis actually has nothing to do with erf really -- it's that converting a real interval to Maxima (or any other system) should raise a TypeError, but doesn't.   \n\nOf course, erf could be implemented for intervals, but that's not done yet; that would be an enhancement not a bug.",
    "created_at": "2008-01-02T06:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1645#issuecomment-10464",
    "user": "was"
}
```

Attachment [trac-1645.patch](tarball://root/attachments/some-uuid/ticket1645/trac-1645.patch) by was created at 2008-01-02 06:12:12

This actually has nothing to do with erf really -- it's that converting a real interval to Maxima (or any other system) should raise a TypeError, but doesn't.   

Of course, erf could be implemented for intervals, but that's not done yet; that would be an enhancement not a bug.



---

archive/issue_comments_010465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T03:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1645#issuecomment-10465",
    "user": "cwitty"
}
```

Resolution: fixed



---

archive/issue_comments_010466.json:
```json
{
    "body": "Looks good to me; and this patch was already applied in 2.9.2.",
    "created_at": "2008-01-15T03:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1645#issuecomment-10466",
    "user": "cwitty"
}
```

Looks good to me; and this patch was already applied in 2.9.2.
