# Issue 3388: Fix gmp 4.2.2 speed regression on Core2

archive/issues_003388.json:
```json
{
    "body": "Assignee: tbd\n\nIn http://groups.google.com/group/sage-devel/t/ba359f3b1ba435d David wrote:\n\n```\nOkay, I can confirm that with sage 3.0.1, sage -gp has the same speed  \nas my standalone GP build. So mostly likely the change to GMP 4.2.2  \nintroduced a speed regression (probably the core 2 patches not being  \napplied properly).\n\ndavid \n```\n\nFix this!\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3388\n\n",
    "created_at": "2008-06-10T02:35:04Z",
    "labels": [
        "component: algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix gmp 4.2.2 speed regression on Core2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tbd

In http://groups.google.com/group/sage-devel/t/ba359f3b1ba435d David wrote:

```
Okay, I can confirm that with sage 3.0.1, sage -gp has the same speed  
as my standalone GP build. So mostly likely the change to GMP 4.2.2  
introduced a speed regression (probably the core 2 patches not being  
applied properly).

david 
```

Fix this!

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3388





---

archive/issue_comments_023667.json:
```json
{
    "body": "Yeah, I went back and looked at the log, and found this:\n\n\n```\nDo we have a Core2 CPU?... Yes\nDetected Intel Core 2 CPU\nFound GMP at /home/dmharvey/sage-3.0.2/spkg/build/gmp-4.2.2/src\nERROR: Incorrect GMP Version.  Found GMP version: 4.2.2\n       needed version 4.2.1\n```\n\n\nSo it's simply that jason's script knows not to try patching the wrong version of GMP.\n\nWe should probably ignore this, since MPIR should be here soonish.",
    "created_at": "2008-06-21T22:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23667",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Yeah, I went back and looked at the log, and found this:


```
Do we have a Core2 CPU?... Yes
Detected Intel Core 2 CPU
Found GMP at /home/dmharvey/sage-3.0.2/spkg/build/gmp-4.2.2/src
ERROR: Incorrect GMP Version.  Found GMP version: 4.2.2
       needed version 4.2.1
```


So it's simply that jason's script knows not to try patching the wrong version of GMP.

We should probably ignore this, since MPIR should be here soonish.



---

archive/issue_comments_023668.json:
```json
{
    "body": "Ok, we might want to ask Jason about whether there are any issues with gmp 4.2.2, but I would assume they would not be. I agree that MPIR should arrive soon enough to make this a non-issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-21T22:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, we might want to ask Jason about whether there are any issues with gmp 4.2.2, but I would assume they would not be. I agree that MPIR should arrive soon enough to make this a non-issue.

Cheers,

Michael



---

archive/issue_comments_023669.json:
```json
{
    "body": "I will ping Jason and ask him if there is a quick fix for sage, in case MPIR takes longer than we expect.",
    "created_at": "2008-06-21T22:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23669",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I will ping Jason and ask him if there is a quick fix for sage, in case MPIR takes longer than we expect.



---

archive/issue_comments_023670.json:
```json
{
    "body": "Further developments:\n\nJason updated his patch to a 4.2.2 version, now available from his website.\n\nI tested it and it does work against a vanilla 4.2.2 build.\n\nHowever, when I put it in the 4.2.2 spkg, it doesn't work. Specifically: it copies the core 2 files, but then GMP's configure script doesn't link to the files, in fact it uses GENERIC code for all the mpn routines.\n\nI dug a little further and discovered the probable culprit: the configure script is from 4.2.1, not 4.2.2!!! And this appears to be because we *overwrite* the configure script when installing the fast gcd patch.\n\nGrrrr. I will try to fix this later today.",
    "created_at": "2008-06-22T16:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23670",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Further developments:

Jason updated his patch to a 4.2.2 version, now available from his website.

I tested it and it does work against a vanilla 4.2.2 build.

However, when I put it in the 4.2.2 spkg, it doesn't work. Specifically: it copies the core 2 files, but then GMP's configure script doesn't link to the files, in fact it uses GENERIC code for all the mpn routines.

I dug a little further and discovered the probable culprit: the configure script is from 4.2.1, not 4.2.2!!! And this appears to be because we *overwrite* the configure script when installing the fast gcd patch.

Grrrr. I will try to fix this later today.



---

archive/issue_comments_023671.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2008-06-22T16:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23671",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing component from algebra to build.



---

archive/issue_comments_023672.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-06-22T16:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23672",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_023673.json:
```json
{
    "body": "What's the current status of this ticket? Presumably, the 4.2.1 vs. 4.2.2 issue was fixed or wasn't it?",
    "created_at": "2008-08-16T23:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23673",
    "user": "https://github.com/malb"
}
```

What's the current status of this ticket? Presumably, the 4.2.1 vs. 4.2.2 issue was fixed or wasn't it?



---

archive/issue_events_003604.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-30T07:06:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3388#event-3604"
}
```



---

archive/issue_comments_023674.json:
```json
{
    "body": "Since we will switch to eMPIRe this is invalid.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T07:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since we will switch to eMPIRe this is invalid.

Cheers,

Michael



---

archive/issue_comments_023675.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-30T07:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_023676.json:
```json
{
    "body": "Well it's been three months since the ticket was created. If there is no serious plan to get MPIR out soon, I'd like to see this ticket reinstated.",
    "created_at": "2008-09-15T18:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23676",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Well it's been three months since the ticket was created. If there is no serious plan to get MPIR out soon, I'd like to see this ticket reinstated.



---

archive/issue_comments_023677.json:
```json
{
    "body": "Replying to [comment:7 dmharvey]:\n> Well it's been three months since the ticket was created. If there is no serious plan to get MPIR out soon, I'd like to see this ticket reinstated.\n\nWe are working on a spkg that will be merged this month.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T20:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3388#issuecomment-23677",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:7 dmharvey]:
> Well it's been three months since the ticket was created. If there is no serious plan to get MPIR out soon, I'd like to see this ticket reinstated.

We are working on a spkg that will be merged this month.

Cheers,

Michael
