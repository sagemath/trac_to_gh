# Issue 4074: [with spkg, needs review] the notebook is totally broken in secure mode with the new twisted spkg

archive/issues_004074.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is because in the previous spkg the patches were applied directly to src/ rather than going through the standard patches/ mechanism.\n\nThe new spkg can be found here: http://sage.math.washington.edu/home/mhansen/twisted-8.1.0.p1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/4074\n\n",
    "created_at": "2008-09-07T20:05:37Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] the notebook is totally broken in secure mode with the new twisted spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4074",
    "user": "mhansen"
}
```
Assignee: mabshoff

This is because in the previous spkg the patches were applied directly to src/ rather than going through the standard patches/ mechanism.

The new spkg can be found here: http://sage.math.washington.edu/home/mhansen/twisted-8.1.0.p1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4074





---

archive/issue_comments_029403.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-07T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29403",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029404.json:
```json
{
    "body": "Thanks to exarkun on #twisted (irc.freenode.net) for helping me track this down.",
    "created_at": "2008-09-07T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29404",
    "user": "mhansen"
}
```

Thanks to exarkun on #twisted (irc.freenode.net) for helping me track this down.



---

archive/issue_comments_029405.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2008-09-07T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29405",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_029406.json:
```json
{
    "body": "I fixed two small issues:\n\n* remove old `._*` crap from OSX - they must have been in the original spkg\n* added diffs for the changed files to the patches directory\n\nPositive review. The new spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/twisted-8.1.0.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29406",
    "user": "mabshoff"
}
```

I fixed two small issues:

* remove old `._*` crap from OSX - they must have been in the original spkg
* added diffs for the changed files to the patches directory

Positive review. The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/twisted-8.1.0.p1.spkg

Cheers,

Michael



---

archive/issue_comments_029407.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T22:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29407",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-07T22:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29408",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029409.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T22:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29409",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1
