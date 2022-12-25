# Issue 3675: upgrade to valgrind 3.3.1

archive/issues_003675.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n[12:50pm] rlm: __Pyx_ImportType?\n[12:51pm] rlm: sound familiar? i'm valgrinding, and this\nseems to be many of 13,030 loss records...\n[12:51pm] mabshoff: Yes.\n[12:51pm] mabshoff: It is Cython dictionaries and I plan\nto suppress them in the future.\n...\n[12:52pm] mabshoff: Can you make a ticket for it? I also\nwant to upgrade the optional valgrind.spkg to 3.3.1 and\nalso change some of the default options, i.e. no more\n--follow-children\n```\n\n\nAnother suggestion- an optional python spkg which has valgrind-friendly compile options set, perhaps even just a replacement `spkg-install` which uses the standard spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3675\n\n",
    "created_at": "2008-07-18T20:03:58Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "upgrade to valgrind 3.3.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3675",
    "user": "https://github.com/rlmill"
}
```
Assignee: mabshoff


```
[12:50pm] rlm: __Pyx_ImportType?
[12:51pm] rlm: sound familiar? i'm valgrinding, and this
seems to be many of 13,030 loss records...
[12:51pm] mabshoff: Yes.
[12:51pm] mabshoff: It is Cython dictionaries and I plan
to suppress them in the future.
...
[12:52pm] mabshoff: Can you make a ticket for it? I also
want to upgrade the optional valgrind.spkg to 3.3.1 and
also change some of the default options, i.e. no more
--follow-children
```


Another suggestion- an optional python spkg which has valgrind-friendly compile options set, perhaps even just a replacement `spkg-install` which uses the standard spkg.

Issue created by migration from https://trac.sagemath.org/ticket/3675





---

archive/issue_comments_025961.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-15T10:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3675#issuecomment-25961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_008415.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-15T10:52:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3675#event-8415"
}
```



---

archive/issue_comments_025962.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc4/valgrind_3.3.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T10:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3675#issuecomment-25962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc4/valgrind_3.3.1.spkg

Cheers,

Michael



---

archive/issue_comments_025963.json:
```json
{
    "body": "Suppression good!",
    "created_at": "2008-09-15T10:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3675#issuecomment-25963",
    "user": "https://github.com/rlmill"
}
```

Suppression good!



---

archive/issue_comments_025964.json:
```json
{
    "body": "Merged in the optional spkg repo in Sage 3.1.2.rc4.",
    "created_at": "2008-09-15T11:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3675#issuecomment-25964",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in the optional spkg repo in Sage 3.1.2.rc4.



---

archive/issue_events_008416.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-15T11:28:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3675#event-8416"
}
```



---

archive/issue_comments_025965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T11:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3675#issuecomment-25965",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
