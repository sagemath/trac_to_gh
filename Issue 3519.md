# Issue 3519: Update clisp to 2.45 release

archive/issues_003519.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe current clisp.spkg is broken on SLES 10/Itanium, i.e. does not compile. I could not find a ticket for this, so I am opening a new one.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3519\n\n",
    "created_at": "2008-06-27T04:13:27Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Update clisp to 2.45 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3519",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The current clisp.spkg is broken on SLES 10/Itanium, i.e. does not compile. I could not find a ticket for this, so I am opening a new one.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3519





---

archive/issue_comments_024741.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-27T04:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24741",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024742.json:
```json
{
    "body": "An updated clisp 2.46 spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/clisp-2.46.spkg\n\nIt is likely broken on Cygwin (but I will fix that) and builds and doctests fine on \n\n* 32 bit OSX 10.5\n* x86-64 Linux\n* Itanium SLES 10 and RHEL 5 Linux\n\nCheers,\n\nMichael",
    "created_at": "2008-07-04T07:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24742",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An updated clisp 2.46 spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/clisp-2.46.spkg

It is likely broken on Cygwin (but I will fix that) and builds and doctests fine on 

* 32 bit OSX 10.5
* x86-64 Linux
* Itanium SLES 10 and RHEL 5 Linux

Cheers,

Michael



---

archive/issue_comments_024743.json:
```json
{
    "body": "Builds OK on OS X 10.4, ppc, but something is wrong.  After rebuilding Maxima, all calculus doc tests with trig functions fail.  Running in maxima mode, trig functions seem OK, but in Sage when evaluated on symbolic variables a TypeError is raised: float required.",
    "created_at": "2008-07-05T23:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24743",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Builds OK on OS X 10.4, ppc, but something is wrong.  After rebuilding Maxima, all calculus doc tests with trig functions fail.  Running in maxima mode, trig functions seem OK, but in Sage when evaluated on symbolic variables a TypeError is raised: float required.



---

archive/issue_comments_024744.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-06T10:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024745.json:
```json
{
    "body": "Replying to [comment:3 mhampton]:\n> Builds OK on OS X 10.4, ppc, but something is wrong.  After rebuilding Maxima, all calculus doc tests with trig functions fail.  Running in maxima mode, trig functions seem OK, but in Sage when evaluated on symbolic variables a TypeError is raised: float required.\n\nFor the record: This was with Sage 2.11. With Sage 3.0.3 on OSX 10.5 PPC all the calculus doctest pass. I will dig out my OSX 10.4 iBook and test it there.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T11:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 mhampton]:
> Builds OK on OS X 10.4, ppc, but something is wrong.  After rebuilding Maxima, all calculus doc tests with trig functions fail.  Running in maxima mode, trig functions seem OK, but in Sage when evaluated on symbolic variables a TypeError is raised: float required.

For the record: This was with Sage 2.11. With Sage 3.0.3 on OSX 10.5 PPC all the calculus doctest pass. I will dig out my OSX 10.4 iBook and test it there.

Cheers,

Michael



---

archive/issue_events_008023.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-07T06:31:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3519#event-8023"
}
```



---

archive/issue_comments_024746.json:
```json
{
    "body": "it built on my test platforms, so positive review.",
    "created_at": "2008-07-07T18:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24746",
    "user": "https://github.com/williamstein"
}
```

it built on my test platforms, so positive review.



---

archive/issue_comments_024747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T21:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24747",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008024.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-07T21:56:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3519#event-8024"
}
```



---

archive/issue_comments_024748.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T22:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3519#issuecomment-24748",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.rc0
