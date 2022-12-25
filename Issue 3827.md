# Issue 3827: finance.TimeSeries -- missng docstring input option

archive/issues_003827.json:
```json
{
    "body": "Assignee: @cswiercz\n\nCC:  @cswiercz\n\nKeywords: finance, timeseries\n\nTimeSeries.randomize has a lognormal distribution generator built in along with uniform, normal, and semicircle. However, there is no docstring that says so! Simply need to add a line that looks like\n\n\n```\nINPUT:\n    distribution -- 'lognormal': mean loc and standard deviation scale\n```\n\n\nSee patch below.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3827\n\n",
    "created_at": "2008-08-12T23:44:08Z",
    "labels": [
        "component: finance",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "finance.TimeSeries -- missng docstring input option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3827",
    "user": "https://github.com/cswiercz"
}
```
Assignee: @cswiercz

CC:  @cswiercz

Keywords: finance, timeseries

TimeSeries.randomize has a lognormal distribution generator built in along with uniform, normal, and semicircle. However, there is no docstring that says so! Simply need to add a line that looks like


```
INPUT:
    distribution -- 'lognormal': mean loc and standard deviation scale
```


See patch below.

Issue created by migration from https://trac.sagemath.org/ticket/3827





---

archive/issue_comments_027168.json:
```json
{
    "body": "Attachment [sage-randomize.patch](tarball://root/attachments/some-uuid/ticket3827/sage-randomize.patch) by @cswiercz created at 2008-08-12 23:44:22",
    "created_at": "2008-08-12T23:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3827#issuecomment-27168",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-randomize.patch](tarball://root/attachments/some-uuid/ticket3827/sage-randomize.patch) by @cswiercz created at 2008-08-12 23:44:22



---

archive/issue_comments_027169.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-12T23:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3827#issuecomment-27169",
    "user": "https://github.com/cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027170.json:
```json
{
    "body": "That's one trivial to review, patch works with 3.1-alpha2 (with 71 lines offset)...",
    "created_at": "2008-08-14T17:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3827#issuecomment-27170",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

That's one trivial to review, patch works with 3.1-alpha2 (with 71 lines offset)...



---

archive/issue_comments_027171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T06:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3827#issuecomment-27171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027172.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T06:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3827#issuecomment-27172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.rc0
