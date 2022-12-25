# Issue 6114: symbolics -- fix removal of constants.so

archive/issues_006114.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nUpgrading from alpha0 on Fedora 10 failed somehow. I had to remove constants.so\nby hand.\n\n$ rm devel/sage/build/sage/symbolic/constants.so\n\nNow testing.\n\nOn Fedora 9 I'll do a fresh install.\n\n```\n\n\nI (=william) did remove enough constants.* files, which resulted in the above.  I will attach a patch to fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6114\n\n",
    "created_at": "2009-05-21T18:38:31Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "symbolics -- fix removal of constants.so",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6114",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin


```
Upgrading from alpha0 on Fedora 10 failed somehow. I had to remove constants.so
by hand.

$ rm devel/sage/build/sage/symbolic/constants.so

Now testing.

On Fedora 9 I'll do a fresh install.

```


I (=william) did remove enough constants.* files, which resulted in the above.  I will attach a patch to fix this.

Issue created by migration from https://trac.sagemath.org/ticket/6114





---

archive/issue_comments_048761.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T02:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48761",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048762.json:
```json
{
    "body": "Craig's sync-build at #5977 gives a cleaner way to do this.",
    "created_at": "2009-05-28T02:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48762",
    "user": "https://github.com/mwhansen"
}
```

Craig's sync-build at #5977 gives a cleaner way to do this.



---

archive/issue_comments_048763.json:
```json
{
    "body": "Changing assignee from @burcin to @mwhansen.",
    "created_at": "2009-05-28T02:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48763",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @burcin to @mwhansen.



---

archive/issue_comments_048764.json:
```json
{
    "body": "Actually, this won't work if there is a stale constants.cpp file sitting around in the directory.",
    "created_at": "2009-05-28T06:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48764",
    "user": "https://github.com/mwhansen"
}
```

Actually, this won't work if there is a stale constants.cpp file sitting around in the directory.



---

archive/issue_comments_048765.json:
```json
{
    "body": "Attachment [trac_6114.patch](tarball://root/attachments/some-uuid/ticket6114/trac_6114.patch) by @williamstein created at 2009-05-28 08:01:13",
    "created_at": "2009-05-28T08:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48765",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6114.patch](tarball://root/attachments/some-uuid/ticket6114/trac_6114.patch) by @williamstein created at 2009-05-28 08:01:13



---

archive/issue_comments_048766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T08:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48766",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006365.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-28T08:04:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6114#event-6365"
}
```



---

archive/issue_comments_048767.json:
```json
{
    "body": "Merged in 4.0.rc1.",
    "created_at": "2009-05-28T08:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6114#issuecomment-48767",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.rc1.
