# Issue 3898: Make an optional, self contained gcc 4.3.1.spkg

archive/issues_003898.json:
```json
{
    "body": "Assignee: mabshoff\n\nAs the title says. Make sure to first build static versions of gmp and mpfr to link against those instead of the Sage ones.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3898\n\n",
    "created_at": "2008-08-19T17:17:37Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make an optional, self contained gcc 4.3.1.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

As the title says. Make sure to first build static versions of gmp and mpfr to link against those instead of the Sage ones.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3898





---

archive/issue_comments_027819.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-23T01:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027820.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/gcc-4.3.1.spkg\n\nbuilds find on x86-64 Linux with recent enough glibcs. It should also work on x86 and Itanium.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-23T01:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/gcc-4.3.1.spkg

builds find on x86-64 Linux with recent enough glibcs. It should also work on x86 and Itanium.

Cheers,

Michael



---

archive/issue_comments_027821.json:
```json
{
    "body": "I have an updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p0.spkg\n\nthat is about half the size. It now installs into $SAGE_LOCAL/toolchain and needs a matching patch to set $PATH and $LD_LIBRARY_PATH correctly to work properly.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T09:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have an updated spkg at

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p0.spkg

that is about half the size. It now installs into $SAGE_LOCAL/toolchain and needs a matching patch to set $PATH and $LD_LIBRARY_PATH correctly to work properly.

Cheers,

Michael



---

archive/issue_comments_027822.json:
```json
{
    "body": "The above spkg will fail in case the Sage build directory is on another mount than the tmp dir since the symbolic link across mounts will fail. That is the reason that it failed on SkyNet with the same error across the board.\n\nI am working on gcc-4.3.1.p1.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T11:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27822",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The above spkg will fail in case the Sage build directory is on another mount than the tmp dir since the symbolic link across mounts will fail. That is the reason that it failed on SkyNet with the same error across the board.

I am working on gcc-4.3.1.p1.spkg.

Cheers,

Michael



---

archive/issue_comments_027823.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p0.spkg\n\nnow builds on various Skynet machines. I still need to add some magic to make the toolchain automatically integrated into sage-env.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T21:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p0.spkg

now builds on various Skynet machines. I still need to add some magic to make the toolchain automatically integrated into sage-env.

Cheers,

Michael



---

archive/issue_comments_027824.json:
```json
{
    "body": "The spkg is obviously\n\nhttp://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p1.spkg\n\nSorry :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T21:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is obviously

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p1.spkg

Sorry :)

Cheers,

Michael



---

archive/issue_comments_027825.json:
```json
{
    "body": "And now there is \n\nhttp://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p2.spkg\n\nI still need to provide an update with the toolchain env being copied into the right place to make this work automatically.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T04:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27825",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And now there is 

http://sage.math.washington.edu/home/mabshoff/gcc-4.3.1.p2.spkg

I still need to provide an update with the toolchain env being copied into the right place to make this work automatically.

Cheers,

Michael



---

archive/issue_comments_027826.json:
```json
{
    "body": "Gcc 4.3.2 is out, so update to latest upstream.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T19:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27826",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Gcc 4.3.2 is out, so update to latest upstream.

Cheers,

Michael



---

archive/issue_comments_027827.json:
```json
{
    "body": "\n```\n23:32 < wstein-682> there's no gcc-4.3.2 spkg, so why did you write \"neeeds review\"?\n23:32 < wstein-682> can I change 3898 to \"needs work\"?\n23:32 < mabshoff> It need to update.\n23:32 < mabshoff> Yes\n23:32 < wstein-682> since it's not done as stated inthe summary?\n23:33 < mabshoff> I need to do two things:\n23:33 < mabshoff> (a) update to gcc 4.3.2 (quick)\n23:33 < mabshoff> (b) create custom toolchain.sh scripts for x86, x86-64 and Itanium.\n23:33 < mabshoff> Next time I build on SkyNet I will do so.\n23:34 < mabshoff> And definitely before SD 12 due to obvious reasons :)\n```\n",
    "created_at": "2008-11-27T07:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27827",
    "user": "https://github.com/williamstein"
}
```


```
23:32 < wstein-682> there's no gcc-4.3.2 spkg, so why did you write "neeeds review"?
23:32 < wstein-682> can I change 3898 to "needs work"?
23:32 < mabshoff> It need to update.
23:32 < mabshoff> Yes
23:32 < wstein-682> since it's not done as stated inthe summary?
23:33 < mabshoff> I need to do two things:
23:33 < mabshoff> (a) update to gcc 4.3.2 (quick)
23:33 < mabshoff> (b) create custom toolchain.sh scripts for x86, x86-64 and Itanium.
23:33 < mabshoff> Next time I build on SkyNet I will do so.
23:34 < mabshoff> And definitely before SD 12 due to obvious reasons :)
```




---

archive/issue_comments_027828.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-02-15T07:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27828",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_027829.json:
```json
{
    "body": "gcc 4.3.3 is out, so this needs to be fixed anyway.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

gcc 4.3.3 is out, so this needs to be fixed anyway.

Cheers,

Michael



---

archive/issue_comments_027830.json:
```json
{
    "body": "Despite not being the latest release, 4.3.4 is arguably the most stable release to date. \n\nDave",
    "created_at": "2009-12-16T22:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27830",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Despite not being the latest release, 4.3.4 is arguably the most stable release to date. 

Dave



---

archive/issue_comments_027831.json:
```json
{
    "body": "Hi David, are you thinking of making an spkg?  I think it would be well worth making one.  I've changed the title to 4.3.4.",
    "created_at": "2009-12-19T07:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27831",
    "user": "https://github.com/williamstein"
}
```

Hi David, are you thinking of making an spkg?  I think it would be well worth making one.  I've changed the title to 4.3.4.



---

archive/issue_comments_027832.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-21T00:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27832",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027833.json:
```json
{
    "body": "This is really old and we are now adding a new gcc spkg, so this ticket should be closed.",
    "created_at": "2012-03-21T00:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27833",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

This is really old and we are now adding a new gcc spkg, so this ticket should be closed.



---

archive/issue_comments_027834.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-21T00:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27834",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027835.json:
```json
{
    "body": "I agree: this should be closed.",
    "created_at": "2012-03-21T00:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27835",
    "user": "https://github.com/roed314"
}
```

I agree: this should be closed.



---

archive/issue_events_004125.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-03-21T11:33:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3898#event-4125"
}
```



---

archive/issue_comments_027836.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-03-21T11:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3898#issuecomment-27836",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
