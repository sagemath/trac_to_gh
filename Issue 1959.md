# Issue 1959: [with spkg] Solaris 9 fixes for rubiks

archive/issues_001959.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc2/rubiks-20070912.p1.spkg\n\nbuilds fine on Solaris 9, OSX and Linux.\n\nCheers,\n\nMichael \n\nIssue created by migration from https://trac.sagemath.org/ticket/1959\n\n",
    "created_at": "2008-01-28T04:37:36Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with spkg] Solaris 9 fixes for rubiks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1959",
    "user": "mabshoff"
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

archive/issue_comments_012648.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-28T04:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12648",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012649.json:
```json
{
    "body": "Spkg compiles fine, tested cube, works ok.",
    "created_at": "2008-01-28T04:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12649",
    "user": "jkantor"
}
```

Spkg compiles fine, tested cube, works ok.



---

archive/issue_comments_012650.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-28T05:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12650",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012651.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-28T05:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12651",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc2



---

archive/issue_comments_012652.json:
```json
{
    "body": "Has this fix been reported upstream?",
    "created_at": "2008-01-28T19:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12652",
    "user": "@robertwb"
}
```

Has this fix been reported upstream?



---

archive/issue_comments_012653.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Has this fix been reported upstream?\n\nNope, not yet. It is mostly a work around for neron since the Sun compiler on there is busted. In fact, Sun stopped shipping their compiler suit for free [as in beer] many years ago, but recently started to offer them again for free [as in beer]. I can send a patch upstream, but the fix is trivial, i.e. replacing a hard coded `cc` in the makefile of the dik solver with `$(CC)`.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-28T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12653",
    "user": "mabshoff"
}
```

Replying to [comment:4 robertwb]:
> Has this fix been reported upstream?

Nope, not yet. It is mostly a work around for neron since the Sun compiler on there is busted. In fact, Sun stopped shipping their compiler suit for free [as in beer] many years ago, but recently started to offer them again for free [as in beer]. I can send a patch upstream, but the fix is trivial, i.e. replacing a hard coded `cc` in the makefile of the dik solver with `$(CC)`.

Cheers,

Michael



---

archive/issue_comments_012654.json:
```json
{
    "body": "That sounds pretty trivial. I just emailed the author, with a link to this page.",
    "created_at": "2008-01-28T22:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1959#issuecomment-12654",
    "user": "@robertwb"
}
```

That sounds pretty trivial. I just emailed the author, with a link to this page.
