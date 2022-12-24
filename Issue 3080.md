# Issue 3080: testdoc.py hangs

archive/issues_003080.json:
```json
{
    "body": "Assignee: @yqiang\n\n\n```\nsage -t devel/sage/sage/dsage/tests/testdoc.py\n```\n\nnever finishes for me (even after 1hr +).  I have to Ctrl-C my doctests to get them to finish.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3080\n\n",
    "created_at": "2008-05-02T13:26:09Z",
    "labels": [
        "dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "testdoc.py hangs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3080",
    "user": "@garyfurnish"
}
```
Assignee: @yqiang


```
sage -t devel/sage/sage/dsage/tests/testdoc.py
```

never finishes for me (even after 1hr +).  I have to Ctrl-C my doctests to get them to finish.  

Issue created by migration from https://trac.sagemath.org/ticket/3080





---

archive/issue_comments_021241.json:
```json
{
    "body": "This is using 3.0.1.alpha1.  It happens about 75% of the time with both parallel and non-parallel testers using gcc-4.2.3 on gentoo.  The cpu utilization is near zero while this is happening.",
    "created_at": "2008-05-02T13:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3080#issuecomment-21241",
    "user": "@garyfurnish"
}
```

This is using 3.0.1.alpha1.  It happens about 75% of the time with both parallel and non-parallel testers using gcc-4.2.3 on gentoo.  The cpu utilization is near zero while this is happening.



---

archive/issue_comments_021242.json:
```json
{
    "body": "#3097 is the real issue here. Sorry I forgot to update this ticket, but I am closing this as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T17:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3080#issuecomment-21242",
    "user": "mabshoff"
}
```

#3097 is the real issue here. Sorry I forgot to update this ticket, but I am closing this as a dupe.

Cheers,

Michael



---

archive/issue_comments_021243.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-05-03T17:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3080#issuecomment-21243",
    "user": "mabshoff"
}
```

Resolution: duplicate
