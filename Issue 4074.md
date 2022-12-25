# Issue 4074: [with spkg, needs review] the notebook is totally broken in secure mode with the new twisted spkg

archive/issues_004074.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is because in the previous spkg the patches were applied directly to src/ rather than going through the standard patches/ mechanism.\n\nThe new spkg can be found here: http://sage.math.washington.edu/home/mhansen/twisted-8.1.0.p1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/4074\n\n",
    "created_at": "2008-09-07T20:05:37Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] the notebook is totally broken in secure mode with the new twisted spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4074",
    "user": "https://github.com/mwhansen"
}
```
Assignee: mabshoff

This is because in the previous spkg the patches were applied directly to src/ rather than going through the standard patches/ mechanism.

The new spkg can be found here: http://sage.math.washington.edu/home/mhansen/twisted-8.1.0.p1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4074





---

archive/issue_comments_029344.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-07T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29344",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029345.json:
```json
{
    "body": "Thanks to exarkun on #twisted (irc.freenode.net) for helping me track this down.",
    "created_at": "2008-09-07T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29345",
    "user": "https://github.com/mwhansen"
}
```

Thanks to exarkun on #twisted (irc.freenode.net) for helping me track this down.



---

archive/issue_comments_029346.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2008-09-07T20:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29346",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_029347.json:
```json
{
    "body": "I fixed two small issues:\n\n* remove old `._*` crap from OSX - they must have been in the original spkg\n* added diffs for the changed files to the patches directory\n\nPositive review. The new spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc1/twisted-8.1.0.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_029348.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T22:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029349.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-07T22:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029350.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T22:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4074#issuecomment-29350",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_events_009295.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-07T22:59:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4074",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4074#event-9295"
}
```
