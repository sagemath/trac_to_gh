# Issue 1542: R package doesn't notice if rpy fails to build

archive/issues_001542.json:
```json
{
    "body": "Assignee: craigcitro\n\nI think the title says it all; the issue is that no return value is checked, so R doesn't know that anything is wrong. The attached patch just adds a check in spkg-install to make sure everything went okay with the rpy install.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1542\n\n",
    "created_at": "2007-12-17T02:49:05Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "R package doesn't notice if rpy fails to build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1542",
    "user": "craigcitro"
}
```
Assignee: craigcitro

I think the title says it all; the issue is that no return value is checked, so R doesn't know that anything is wrong. The attached patch just adds a check in spkg-install to make sure everything went okay with the rpy install.

Issue created by migration from https://trac.sagemath.org/ticket/1542





---

archive/issue_comments_009848.json:
```json
{
    "body": "The patch is against r-2.6.1.p6.spkg (I forgot to mention that above, though it probably goes without saying).",
    "created_at": "2007-12-17T02:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1542#issuecomment-9848",
    "user": "craigcitro"
}
```

The patch is against r-2.6.1.p6.spkg (I forgot to mention that above, though it probably goes without saying).



---

archive/issue_comments_009849.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-17T02:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1542#issuecomment-9849",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009850.json:
```json
{
    "body": "Attachment\n\nPosted new version of the patch, which reflects the updated name for the rpy-1.0.1.p0.spkg. (I also added a variable so that the rpy spkg name only appears once, instead of twice, making it less likely that someone would accidentally change one and not the other.)",
    "created_at": "2007-12-17T05:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1542#issuecomment-9850",
    "user": "craigcitro"
}
```

Attachment

Posted new version of the patch, which reflects the updated name for the rpy-1.0.1.p0.spkg. (I also added a variable so that the rpy spkg name only appears once, instead of twice, making it less likely that someone would accidentally change one and not the other.)



---

archive/issue_comments_009851.json:
```json
{
    "body": "Merged in 2.9.1.alpha1",
    "created_at": "2007-12-18T02:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1542#issuecomment-9851",
    "user": "rlm"
}
```

Merged in 2.9.1.alpha1



---

archive/issue_comments_009852.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-18T02:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1542#issuecomment-9852",
    "user": "rlm"
}
```

Resolution: fixed
