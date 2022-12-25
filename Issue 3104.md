# Issue 3104: pbori.pyx: Make some doctest long since it uses a lot of RAM

archive/issues_003104.json:
```json
{
    "body": "Assignee: failure\n\nCC:  polybori\n\n\n```\n[13:32] <wstein> Is there a ticket up for pbori.pyx not passing?\n[13:32] <mabshoff> nope.\n[13:33] <wstein> I propose that we put a --long in there to mean \"need more ram\".\n[13:33] <mabshoff> You mean because it uses so much RAM?\n[13:33] <mabshoff> yes\n[13:33] <wstein> Yes.\n[13:33] <wstein> --long meaning \"--big\" or something.\n[13:33] <mabshoff> :)\n[13:33] <wstein> It's annoying that pbori.pyx fails on so many of my test machines.\n[13:33] <mabshoff> yep\n[13:34] <mabshoff> I usually just ignore pbori.pyx failures, which is somewhat dangerous.\n[13:34] <mabshoff> fixed\n[13:34] <wstein> exactly.\n[13:34] <wstein> Can you make a ticket?\n[13:34] <mabshoff> sure\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3104\n\n",
    "created_at": "2008-05-05T12:16:16Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "pbori.pyx: Make some doctest long since it uses a lot of RAM",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

CC:  polybori


```
[13:32] <wstein> Is there a ticket up for pbori.pyx not passing?
[13:32] <mabshoff> nope.
[13:33] <wstein> I propose that we put a --long in there to mean "need more ram".
[13:33] <mabshoff> You mean because it uses so much RAM?
[13:33] <mabshoff> yes
[13:33] <wstein> Yes.
[13:33] <wstein> --long meaning "--big" or something.
[13:33] <mabshoff> :)
[13:33] <wstein> It's annoying that pbori.pyx fails on so many of my test machines.
[13:33] <mabshoff> yep
[13:34] <mabshoff> I usually just ignore pbori.pyx failures, which is somewhat dangerous.
[13:34] <mabshoff> fixed
[13:34] <wstein> exactly.
[13:34] <wstein> Can you make a ticket?
[13:34] <mabshoff> sure
```


Issue created by migration from https://trac.sagemath.org/ticket/3104





---

archive/issue_comments_021402.json:
```json
{
    "body": "Attachment [sage-3104.patch](tarball://root/attachments/some-uuid/ticket3104/sage-3104.patch) by @williamstein created at 2008-05-05 12:29:04",
    "created_at": "2008-05-05T12:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21402",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3104.patch](tarball://root/attachments/some-uuid/ticket3104/sage-3104.patch) by @williamstein created at 2008-05-05 12:29:04



---

archive/issue_comments_021403.json:
```json
{
    "body": "Patch looks good to me. I will do some testing to see how much less RAM we need with the patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-05T15:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. I will do some testing to see how much less RAM we need with the patch applied.

Cheers,

Michael



---

archive/issue_comments_021404.json:
```json
{
    "body": "I don't think that this strategy is right: If simple substitution takes too much RAM this is a serious bug not just something to be dealt with by adding `#long`.",
    "created_at": "2008-05-05T19:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21404",
    "user": "https://github.com/malb"
}
```

I don't think that this strategy is right: If simple substitution takes too much RAM this is a serious bug not just something to be dealt with by adding `#long`.



---

archive/issue_comments_021405.json:
```json
{
    "body": "There are know memory leaks in this code in the order of 0.5GB in PolyBoRi. Making those doctests long will avoid people hitting the issue. I normally run *every* doctest as long, so the test coverage is still there. It is certainly a workaround until we fix the real issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-05T19:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are know memory leaks in this code in the order of 0.5GB in PolyBoRi. Making those doctests long will avoid people hitting the issue. I normally run *every* doctest as long, so the test coverage is still there. It is certainly a workaround until we fix the real issue.

Cheers,

Michael



---

archive/issue_comments_021406.json:
```json
{
    "body": "Hi Martin,\n\nafter discussing the issue with William in IRC: How about first upgrading to the PolyBoRi 0.4 release that Alexander just mentioned, check out the result with valdring. If there still is a large memory leak we apply this patch, open a new ticket to fix the memory leak and then revert the longs once the leaks are plugged.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-05T21:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Martin,

after discussing the issue with William in IRC: How about first upgrading to the PolyBoRi 0.4 release that Alexander just mentioned, check out the result with valdring. If there still is a large memory leak we apply this patch, open a new ticket to fix the memory leak and then revert the longs once the leaks are plugged.

Cheers,

Michael



---

archive/issue_comments_021407.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-05-21T13:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_021408.json:
```json
{
    "body": "Because this continues to be a problem with 3.0.2.alpha1 we will apply this patch to 3.0.2. Once #3264 has been merged [the upgrade to PolyBoRi 0.4] we will revisit the issue. \n\nCheers,\n\nMichael",
    "created_at": "2008-05-21T13:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Because this continues to be a problem with 3.0.2.alpha1 we will apply this patch to 3.0.2. Once #3264 has been merged [the upgrade to PolyBoRi 0.4] we will revisit the issue. 

Cheers,

Michael



---

archive/issue_comments_021409.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-21T13:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-21T13:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003320.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-21T13:23:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3104#event-3320"
}
```



---

archive/issue_comments_021411.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-21T13:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3104#issuecomment-21411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc0
