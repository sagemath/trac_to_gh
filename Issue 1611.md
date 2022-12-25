# Issue 1611: polybori should use the m4ri library from libm4ri spkg

archive/issues_001611.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  polybori\n\nPolyBoRi comes with its own copy of m4ri libraries. After #1505, Sage provides these libraries through a package.\n\nThe PolyBoRi build process should be changed to use the library and headers provided by libm4ri-*.spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1611\n\n",
    "created_at": "2007-12-27T10:54:50Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "polybori should use the m4ri library from libm4ri spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1611",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  polybori

PolyBoRi comes with its own copy of m4ri libraries. After #1505, Sage provides these libraries through a package.

The PolyBoRi build process should be changed to use the library and headers provided by libm4ri-*.spkg.

Issue created by migration from https://trac.sagemath.org/ticket/1611





---

archive/issue_comments_010219.json:
```json
{
    "body": "Michael Brickenstein wrote:\n\n> If you can wait until the end of my holidays, which will begin  \n> tomorrow and end at 6th of January, I will do the switch myself.",
    "created_at": "2007-12-27T12:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10219",
    "user": "https://github.com/malb"
}
```

Michael Brickenstein wrote:

> If you can wait until the end of my holidays, which will begin  
> tomorrow and end at 6th of January, I will do the switch myself.



---

archive/issue_events_004007.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2008-01-03T15:07:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1611#event-4007"
}
```



---

archive/issue_comments_010220.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-03T15:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10220",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010221.json:
```json
{
    "body": "The issue might be resolved during the update to PolyBoRi 0.2.rcX during Bug Day 10.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue might be resolved during the update to PolyBoRi 0.2.rcX during Bug Day 10.

Cheers,

Michael



---

archive/issue_comments_010222.json:
```json
{
    "body": "This should be done while updating PolyBori - see #2060.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T19:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This should be done while updating PolyBori - see #2060.

Cheers,

Michael



---

archive/issue_comments_010223.json:
```json
{
    "body": "`PolyBoRi` requires some changes in the m4ri libraries. They are waiting for changes upstream (in m4ri) to switch over, so newer versions of `PolyBoRi` don't support this.",
    "created_at": "2008-03-08T13:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10223",
    "user": "https://github.com/burcin"
}
```

`PolyBoRi` requires some changes in the m4ri libraries. They are waiting for changes upstream (in m4ri) to switch over, so newer versions of `PolyBoRi` don't support this.



---

archive/issue_comments_010224.json:
```json
{
    "body": "I guess I am upstream so I should diff their m4ri against ours (upstream).",
    "created_at": "2008-03-09T15:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10224",
    "user": "https://github.com/malb"
}
```

I guess I am upstream so I should diff their m4ri against ours (upstream).



---

archive/issue_comments_010225.json:
```json
{
    "body": "Fixing this bug is planned for the PolyBoRi 0.5 release.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-12T00:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixing this bug is planned for the PolyBoRi 0.5 release.

Cheers,

Michael



---

archive/issue_comments_010226.json:
```json
{
    "body": "#3264 does not fix the problem yet. Are there any options to make this happen with PolyBoRi 0.5?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T00:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#3264 does not fix the problem yet. Are there any options to make this happen with PolyBoRi 0.5?

Cheers,

Michael



---

archive/issue_comments_010227.json:
```json
{
    "body": "There is some movement w.r.t. this issue in PolyBoRi, but I wouldn't suspect it to be available in 0.5.",
    "created_at": "2008-09-07T00:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10227",
    "user": "https://github.com/malb"
}
```

There is some movement w.r.t. this issue in PolyBoRi, but I wouldn't suspect it to be available in 0.5.



---

archive/issue_comments_010228.json:
```json
{
    "body": "it will be available in 0.5. However, you should make sure, that\nmalloc work also for allocating zero bytes in M4RI, else it will crash\n(doesn't work with mm_malloc on Mac OS X 10.5).",
    "created_at": "2008-09-08T06:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10228",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

it will be available in 0.5. However, you should make sure, that
malloc work also for allocating zero bytes in M4RI, else it will crash
(doesn't work with mm_malloc on Mac OS X 10.5).



---

archive/issue_events_004008.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2009-09-29T08:08:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1611#event-4008"
}
```



---

archive/issue_comments_010229.json:
```json
{
    "body": "This is fixed with #6177",
    "created_at": "2009-09-29T08:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10229",
    "user": "https://github.com/malb"
}
```

This is fixed with #6177



---

archive/issue_comments_010230.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T08:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10230",
    "user": "https://github.com/malb"
}
```

Resolution: fixed
