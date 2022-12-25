# Issue 2976: get rid of /home/jec/sage-3.0.rc0/tmp/test-dsage.log error at the end of tests

archive/issues_002976.json:
```json
{
    "body": "Assignee: failure\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2976\n\n",
    "created_at": "2008-04-20T22:07:38Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "get rid of /home/jec/sage-3.0.rc0/tmp/test-dsage.log error at the end of tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2976",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure



Issue created by migration from https://trac.sagemath.org/ticket/2976





---

archive/issue_comments_020460.json:
```json
{
    "body": "This bug is caused by the commenting out of dsage unit tests. The fix is\n\n1) Someone (was?) reviews #2553\n2) Uncomment line 15 of sage-maketest",
    "created_at": "2008-04-20T22:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2976#issuecomment-20460",
    "user": "https://github.com/yqiang"
}
```

This bug is caused by the commenting out of dsage unit tests. The fix is

1) Someone (was?) reviews #2553
2) Uncomment line 15 of sage-maketest



---

archive/issue_comments_020461.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-20T23:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2976#issuecomment-20461",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_comments_020462.json:
```json
{
    "body": "This will be fixed by #2553... Closed as a dup.",
    "created_at": "2008-04-20T23:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2976#issuecomment-20462",
    "user": "https://github.com/williamstein"
}
```

This will be fixed by #2553... Closed as a dup.
