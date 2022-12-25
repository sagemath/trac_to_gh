# Issue 5011: [with patch, needs review] Solaris: fix get_memory_usage() to use top

archive/issues_005011.json:
```json
{
    "body": "Assignee: mabshoff\n\nget_memory_usage() falls back to using top when not on Linux. The OSX case is hard coded, but on Solaris we need this patch to make it work.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5011\n\n",
    "created_at": "2009-01-18T06:45:58Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] Solaris: fix get_memory_usage() to use top",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

get_memory_usage() falls back to using top when not on Linux. The OSX case is hard coded, but on Solaris we need this patch to make it work.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5011





---

archive/issue_comments_038124.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-18T06:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5011#issuecomment-38124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038125.json:
```json
{
    "body": "Attachment [trac_5011_get_memory.patch](tarball://root/attachments/some-uuid/ticket5011/trac_5011_get_memory.patch) by @craigcitro created at 2009-01-18 12:36:35\n\nI don't have a Sun to test this on, so I'm taking for granted that the actual command being run is correct. However, I can verify that it will only be run on a Sun, which is the goal. So positive review with Michael's assurance that it's the correct usage. :)",
    "created_at": "2009-01-18T12:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5011#issuecomment-38125",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_5011_get_memory.patch](tarball://root/attachments/some-uuid/ticket5011/trac_5011_get_memory.patch) by @craigcitro created at 2009-01-18 12:36:35

I don't have a Sun to test this on, so I'm taking for granted that the actual command being run is correct. However, I can verify that it will only be run on a Sun, which is the goal. So positive review with Michael's assurance that it's the correct usage. :)



---

archive/issue_comments_038126.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T13:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5011#issuecomment-38126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038127.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T13:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5011#issuecomment-38127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_events_005255.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T13:57:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5011",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5011#event-5255"
}
```
