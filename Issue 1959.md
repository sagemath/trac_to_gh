# Issue 1959: [with spkg, positive review ] Solaris 9 fixes for rubiks

archive/issues_001959.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc2/rubiks-20070912.p1.spkg\n\nbuilds fine on Solaris 9, OSX and Linux.\n\nCheers,\n\nMichael \n\nIssue created by migration from https://trac.sagemath.org/ticket/1959\n\n",
    "closed_at": "2008-01-28T05:06:11Z",
    "created_at": "2008-01-28T04:37:36Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with spkg, positive review ] Solaris 9 fixes for rubiks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1959",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc2/rubiks-20070912.p1.spkg

builds fine on Solaris 9, OSX and Linux.

Cheers,

Michael 

Issue created by migration from https://trac.sagemath.org/ticket/1959





---

archive/issue_comments_012617.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-28T04:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012618.json:
```json
{
    "body": "Spkg compiles fine, tested cube, works ok.",
    "created_at": "2008-01-28T04:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12618",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Spkg compiles fine, tested cube, works ok.



---

archive/issue_events_004746.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-28T05:06:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1959#event-4746"
}
```



---

archive/issue_comments_012619.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-28T05:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12619",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012620.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-28T05:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc2



---

archive/issue_comments_012621.json:
```json
{
    "body": "Has this fix been reported upstream?",
    "created_at": "2008-01-28T19:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12621",
    "user": "https://github.com/robertwb"
}
```

Has this fix been reported upstream?



---

archive/issue_comments_012622.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Has this fix been reported upstream?\n\n\nNope, not yet. It is mostly a work around for neron since the Sun compiler on there is busted. In fact, Sun stopped shipping their compiler suit for free [as in beer] many years ago, but recently started to offer them again for free [as in beer]. I can send a patch upstream, but the fix is trivial, i.e. replacing a hard coded `cc` in the makefile of the dik solver with `$(CC)`.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-28T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> Has this fix been reported upstream?


Nope, not yet. It is mostly a work around for neron since the Sun compiler on there is busted. In fact, Sun stopped shipping their compiler suit for free [as in beer] many years ago, but recently started to offer them again for free [as in beer]. I can send a patch upstream, but the fix is trivial, i.e. replacing a hard coded `cc` in the makefile of the dik solver with `$(CC)`.

Cheers,

Michael



---

archive/issue_comments_012623.json:
```json
{
    "body": "That sounds pretty trivial. I just emailed the author, with a link to this page.",
    "created_at": "2008-01-28T22:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12623",
    "user": "https://github.com/robertwb"
}
```

That sounds pretty trivial. I just emailed the author, with a link to this page.
