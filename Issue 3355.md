# Issue 3355: invoke the libdir rewrite script on "sage -upgrade"

archive/issues_003355.json:
```json
{
    "body": "Assignee: cwitty\n\nAll the *.la files in $SAGE_LOCAL/lib have their libdir variable rewritten when Sage is moved. Do this also when installing any spkg since we might have moved the tree. This will likely cause a number of upgrade problems.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3355\n\n",
    "created_at": "2008-06-03T05:33:54Z",
    "labels": [
        "component: relocation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "invoke the libdir rewrite script on \"sage -upgrade\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

All the *.la files in $SAGE_LOCAL/lib have their libdir variable rewritten when Sage is moved. Do this also when installing any spkg since we might have moved the tree. This will likely cause a number of upgrade problems.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3355





---

archive/issue_comments_023276.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23276",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_023277.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23277",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_023278.json:
```json
{
    "body": "* **Priority** changed from *critical* to *major*\n\nIf we've released for years and years without fixing this, it doesn't make sense to keep it as critical.\n\n... just kidding!",
    "created_at": "2012-03-21T00:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23278",
    "user": "https://github.com/kini"
}
```

* **Priority** changed from *critical* to *major*

If we've released for years and years without fixing this, it doesn't make sense to keep it as critical.

... just kidding!



---

archive/issue_comments_023279.json:
```json
{
    "body": "`sage-location` actually does this now.",
    "created_at": "2013-03-28T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23279",
    "user": "https://github.com/jdemeyer"
}
```

`sage-location` actually does this now.



---

archive/issue_events_007530.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-28T22:57:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3355#event-7530"
}
```



---

archive/issue_comments_023280.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-28T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23280",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023281.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-28T22:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23281",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007531.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-29T19:00:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3355#event-7531"
}
```



---

archive/issue_comments_023282.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-29T19:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3355#issuecomment-23282",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
