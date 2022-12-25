# Issue 3291: [with patch, needs review] pbuild doesn't properly compile mwrank.so on some systems

archive/issues_003291.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nOn some systems pbuild seems to leave out wrap.o of mwrank.so, resulting in a undefined symbol error\n\nIssue created by migration from https://trac.sagemath.org/ticket/3291\n\n",
    "created_at": "2008-05-23T22:38:03Z",
    "labels": [
        "component: pbuild",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] pbuild doesn't properly compile mwrank.so on some systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3291",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

On some systems pbuild seems to leave out wrap.o of mwrank.so, resulting in a undefined symbol error

Issue created by migration from https://trac.sagemath.org/ticket/3291





---

archive/issue_comments_022722.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-23T22:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22722",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022723.json:
```json
{
    "body": "Attachment [trac_3291_extcode.patch](tarball://root/attachments/some-uuid/ticket3291/trac_3291_extcode.patch) by @garyfurnish created at 2008-05-23 22:41:11",
    "created_at": "2008-05-23T22:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22723",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3291_extcode.patch](tarball://root/attachments/some-uuid/ticket3291/trac_3291_extcode.patch) by @garyfurnish created at 2008-05-23 22:41:11



---

archive/issue_comments_022724.json:
```json
{
    "body": "The patch fixed the issue with build on Fedora 9, 32 bits, 2 cpu's\n\nJaap",
    "created_at": "2008-05-23T23:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22724",
    "user": "https://github.com/jaapspies"
}
```

The patch fixed the issue with build on Fedora 9, 32 bits, 2 cpu's

Jaap



---

archive/issue_events_003510.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-24T00:27:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3291#event-3510"
}
```



---

archive/issue_comments_022725.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc3",
    "created_at": "2008-05-24T00:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22725",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc3



---

archive/issue_comments_022726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-24T00:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22726",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
