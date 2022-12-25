# Issue 5286: python 2.5.4 breaks -sdist due to missing .hg repo in the sage-3.3.rc1.spkg (followup to #5218)

archive/issues_005286.json:
```json
{
    "body": "Assignee: @mwhansen\n\nWhen merging the python-2.5.4.spkg from #5218 everything goes fine, but -sdist. In that case the .hg repo is copied into the tmp directory in spkg-dist, but it is not copied into the tar.gz created by distutils. Until this is resolved we cannot update to the latest python-2.5.4.spkg.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5286\n\n",
    "closed_at": "2009-05-29T13:38:32Z",
    "created_at": "2009-02-16T16:03:38Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "python 2.5.4 breaks -sdist due to missing .hg repo in the sage-3.3.rc1.spkg (followup to #5218)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5286",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @mwhansen

When merging the python-2.5.4.spkg from #5218 everything goes fine, but -sdist. In that case the .hg repo is copied into the tmp directory in spkg-dist, but it is not copied into the tar.gz created by distutils. Until this is resolved we cannot update to the latest python-2.5.4.spkg.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5286





---

archive/issue_events_012285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:25:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5286#event-12285"
}
```



---

archive/issue_comments_040545.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040546.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-05-28T20:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40546",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_040547.json:
```json
{
    "body": "This is caused by http://bugs.python.org/issue1725737\n\nThere is a fix in the new spkg at #5218.",
    "created_at": "2009-05-28T20:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40547",
    "user": "https://github.com/mwhansen"
}
```

This is caused by http://bugs.python.org/issue1725737

There is a fix in the new spkg at #5218.



---

archive/issue_comments_040548.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T20:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40548",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_events_012286.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-28T20:24:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5286#event-12286"
}
```



---

archive/issue_events_012287.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-28T20:24:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5286#event-12287"
}
```



---

archive/issue_events_012288.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-05-29T13:38:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5286#event-12288"
}
```



---

archive/issue_comments_040549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-29T13:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5286#issuecomment-40549",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
