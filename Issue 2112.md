# Issue 2112: __contains__ sometimes fails with SR elements due to == returning an equation

archive/issues_002112.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: SR(2) in ZZ\nFalse\n```\n\n\nThis is easy to fix by having __contains__ use bool(foo==bar) rather than just foo == bar.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2112\n\n",
    "created_at": "2008-02-08T13:02:59Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "__contains__ sometimes fails with SR elements due to == returning an equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2112",
    "user": "mhansen"
}
```
Assignee: somebody


```
sage: SR(2) in ZZ
False
```


This is easy to fix by having __contains__ use bool(foo==bar) rather than just foo == bar.

Issue created by migration from https://trac.sagemath.org/ticket/2112





---

archive/issue_comments_013768.json:
```json
{
    "body": "Changing assignee from somebody to mhansen.",
    "created_at": "2008-02-08T13:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2112#issuecomment-13768",
    "user": "mhansen"
}
```

Changing assignee from somebody to mhansen.



---

archive/issue_comments_013769.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-08T13:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2112#issuecomment-13769",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013770.json:
```json
{
    "body": "Attachment [2112.patch](tarball://root/attachments/some-uuid/ticket2112/2112.patch) by mhansen created at 2008-02-08 14:21:50\n\nCause no problems with -testall on my machine.",
    "created_at": "2008-02-08T14:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2112#issuecomment-13770",
    "user": "mhansen"
}
```

Attachment [2112.patch](tarball://root/attachments/some-uuid/ticket2112/2112.patch) by mhansen created at 2008-02-08 14:21:50

Cause no problems with -testall on my machine.



---

archive/issue_comments_013771.json:
```json
{
    "body": "So small, I say apply.",
    "created_at": "2008-02-15T04:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2112#issuecomment-13771",
    "user": "ncalexan"
}
```

So small, I say apply.



---

archive/issue_comments_013772.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2112#issuecomment-13772",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013773.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2112#issuecomment-13773",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
