# Issue 5744: Solaris 10: use C99 mode to compile extensions instead of using clumsy extern declarations, properly work around _Complex_I problem in complex.h

archive/issues_005744.json:
```json
{
    "body": "Assignee: mabshoff\n\nisinf() and a bunch of friends we right now provide via solaris_fixes.h in various places is available in C99 mode with gcc via math_c99.h which is included in math.h. So building some extensions in C99 mode will allow us to get rid of nearly all Solaris specific workarounds. \n\nAt the same time we have a new problem with _Complex_I which is expected to be provided by the compiler since complex.h just defines _Complex_I to be _Complex_I on Solaris 10. Not good :(\n\nI have a patch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5744\n\n",
    "created_at": "2009-04-11T01:29:28Z",
    "labels": [
        "component: porting: solaris",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Solaris 10: use C99 mode to compile extensions instead of using clumsy extern declarations, properly work around _Complex_I problem in complex.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

isinf() and a bunch of friends we right now provide via solaris_fixes.h in various places is available in C99 mode with gcc via math_c99.h which is included in math.h. So building some extensions in C99 mode will allow us to get rid of nearly all Solaris specific workarounds. 

At the same time we have a new problem with _Complex_I which is expected to be provided by the compiler since complex.h just defines _Complex_I to be _Complex_I on Solaris 10. Not good :(

I have a patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5744





---

archive/issue_comments_044823.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-11T01:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044824.json:
```json
{
    "body": "Attachment [trac_5744.patch](tarball://root/attachments/some-uuid/ticket5744/trac_5744.patch) by mabshoff created at 2009-04-11 03:39:14",
    "created_at": "2009-04-11T03:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5744.patch](tarball://root/attachments/some-uuid/ticket5744/trac_5744.patch) by mabshoff created at 2009-04-11 03:39:14



---

archive/issue_comments_044825.json:
```json
{
    "body": "This patch removes some of the problems with C99, but some issues remain unresolved due to header issues when C99 and C++ is used.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T03:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44825",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch removes some of the problems with C99, but some issues remain unresolved due to header issues when C99 and C++ is used.

Cheers,

Michael



---

archive/issue_comments_044826.json:
```json
{
    "body": "This looks fine to me.  I give it a positive review if it works for mabshoff.  He's the only one right now with a full Solaris build setup to test this on.",
    "created_at": "2009-04-11T04:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44826",
    "user": "https://github.com/williamstein"
}
```

This looks fine to me.  I give it a positive review if it works for mabshoff.  He's the only one right now with a full Solaris build setup to test this on.



---

archive/issue_comments_044827.json:
```json
{
    "body": "It does not affect the build on non-Solaris and on Solaris it starts up, so I am making this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T04:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It does not affect the build on non-Solaris and on Solaris it starts up, so I am making this a positive review.

Cheers,

Michael



---

archive/issue_comments_044828.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T04:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44828",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T04:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5744#issuecomment-44829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005991.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-11T04:54:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5744",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5744#event-5991"
}
```
