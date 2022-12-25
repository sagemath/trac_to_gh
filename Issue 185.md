# Issue 185: Firefox + Xorg (Linux) take way too much cputime while waiting for results from the notebook server

archive/issues_000185.json:
```json
{
    "body": "Assignee: boothby\n\nOn my P4 so as my P3 system whenever I undertake a long calculation using the notebook the polling for results takes way too much cputime. I guess it's caused by a very high polling frequency. top output follows:\n\n```\n XXXX martin    25   0  125m  36m 9.8m R   80  2.4   1:13.44 python\n XXXX root      16   0  285m 176m 2860 R   36 11.6 204:18.81 Xorg\n XXXX martin    15   0 95860  43m  19m S   30  2.8   3:50.28 firefox-bin\n```\nHow to reproduce: Calculate something difficult and monitor top.\n\nIssue created by migration from https://trac.sagemath.org/ticket/185\n\n",
    "created_at": "2006-12-18T00:00:39Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Firefox + Xorg (Linux) take way too much cputime while waiting for results from the notebook server",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/185",
    "user": "https://github.com/malb"
}
```
Assignee: boothby

On my P4 so as my P3 system whenever I undertake a long calculation using the notebook the polling for results takes way too much cputime. I guess it's caused by a very high polling frequency. top output follows:

```
 XXXX martin    25   0  125m  36m 9.8m R   80  2.4   1:13.44 python
 XXXX root      16   0  285m 176m 2860 R   36 11.6 204:18.81 Xorg
 XXXX martin    15   0 95860  43m  19m S   30  2.8   3:50.28 firefox-bin
```
How to reproduce: Calculate something difficult and monitor top.

Issue created by migration from https://trac.sagemath.org/ticket/185





---

archive/issue_comments_000837.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-19T09:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-837",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_000355.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-19T09:57:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "milestone": "sage-1.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/185#event-355"
}
```



---

archive/issue_comments_000838.json:
```json
{
    "body": "Please investigate the issue. The orignial milestone was 1.8 so it has been a while.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T02:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please investigate the issue. The orignial milestone was 1.8 so it has been a while.

Cheers,

Michael



---

archive/issue_events_000356.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T02:37:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "milestone": "sage-1.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/185#event-356"
}
```



---

archive/issue_events_000357.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T02:37:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/185#event-357"
}
```



---

archive/issue_comments_000839.json:
```json
{
    "body": "The issues has not been resolved, an truncated exponential backoff was discussed here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/f8f76d438163e546/110cf0c908689635?",
    "created_at": "2008-01-17T12:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-839",
    "user": "https://github.com/malb"
}
```

The issues has not been resolved, an truncated exponential backoff was discussed here:

http://groups.google.com/group/sage-devel/browse_thread/thread/f8f76d438163e546/110cf0c908689635?



---

archive/issue_comments_000840.json:
```json
{
    "body": "I've implemented something like exponential falloff.  Polling slows down gradually; after about 30 seconds, poll delay is 5 seconds.",
    "created_at": "2008-03-16T21:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-840",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I've implemented something like exponential falloff.  Polling slows down gradually; after about 30 seconds, poll delay is 5 seconds.



---

archive/issue_comments_000841.json:
```json
{
    "body": "Attachment [185-smartpoll.patch](tarball://root/attachments/some-uuid/ticket185/185-smartpoll.patch) by boothby created at 2008-03-16 21:23:36",
    "created_at": "2008-03-16T21:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-841",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [185-smartpoll.patch](tarball://root/attachments/some-uuid/ticket185/185-smartpoll.patch) by boothby created at 2008-03-16 21:23:36



---

archive/issue_events_000358.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-03-16T21:24:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/185#event-358"
}
```



---

archive/issue_events_000359.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-03-16T21:24:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/185#event-359"
}
```



---

archive/issue_comments_000842.json:
```json
{
    "body": "It works fine for me; the code makes sense.",
    "created_at": "2008-03-17T04:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-842",
    "user": "https://github.com/williamstein"
}
```

It works fine for me; the code makes sense.



---

archive/issue_events_000360.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-17T04:24:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/185#event-360"
}
```



---

archive/issue_comments_000843.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-17T04:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.final



---

archive/issue_comments_000844.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-17T04:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/185#issuecomment-844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
