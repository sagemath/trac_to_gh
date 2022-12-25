# Issue 1268: [with spkg] new version of MPFI

archive/issues_001268.json:
```json
{
    "body": "Assignee: @williamstein\n\nI've built a new MPFI spkg that switches to using the current MPFI CVS.  (They have all the bug fixes from the previous Sage spkg, and more.)  Plus, they've started installing shared and static libraries, so we end up using the shared library version.\n\nThe new spkg is at http://sage.math.washington.edu/home/cwitty/mpfi-1.3.4-cvs20071125.spkg\n\ntestall passes on 32-bit x86 linux with the new spkg.\n\nBy the way, if you're going to test it, you can't just install the new spkg, because the old library will still be statically linked in to the relevant extension modules.  You also need to do:\n\n```\ntouch devel/sage/sage/rings/mpfi.pxi\nsage -b\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1268\n\n",
    "created_at": "2007-11-25T15:26:58Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with spkg] new version of MPFI",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1268",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

I've built a new MPFI spkg that switches to using the current MPFI CVS.  (They have all the bug fixes from the previous Sage spkg, and more.)  Plus, they've started installing shared and static libraries, so we end up using the shared library version.

The new spkg is at http://sage.math.washington.edu/home/cwitty/mpfi-1.3.4-cvs20071125.spkg

testall passes on 32-bit x86 linux with the new spkg.

By the way, if you're going to test it, you can't just install the new spkg, because the old library will still be statically linked in to the relevant extension modules.  You also need to do:

```
touch devel/sage/sage/rings/mpfi.pxi
sage -b
```

Issue created by migration from https://trac.sagemath.org/ticket/1268





---

archive/issue_comments_007928.json:
```json
{
    "body": "As mentioned above, simply installing the new spkg isn't enough; we need to ensure that extensions depending on the library get rebuilt.  One way to do this for upgrades to 2.8.15 is to apply the patch from #1270 (or any other patch that touches mpfi.pxi).",
    "created_at": "2007-11-25T17:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1268#issuecomment-7928",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

As mentioned above, simply installing the new spkg isn't enough; we need to ensure that extensions depending on the library get rebuilt.  One way to do this for upgrades to 2.8.15 is to apply the patch from #1270 (or any other patch that touches mpfi.pxi).



---

archive/issue_comments_007929.json:
```json
{
    "body": "```\n(cd .libs && rm -f libmpfi.0 && ln -s libmpfi.0.0.0 libmpfi.0)\n(cd .libs && rm -f libmpfi && ln -s libmpfi.0.0.0 libmpfi)\nar cru .libs/libmpfi.a  mpfi.o mpfi_io.o mpfi_trigo.o~ranlib .libs/libmpfi.a\nar: mpfi_trigo.o~ranlib: No such file or directory\nmake[1]: *** [libmpfi.la] Error 1\nmake: *** [install-recursive] Error 1\nAn error occurred while building mpfi.\n\nreal    0m19.460s\nuser    0m4.463s\nsys     0m8.673s\nsage: An error occurred while installing mpfi-1.3.4-cvs20071125\n```\n\nOS X 10.4, Intel (core duo)",
    "created_at": "2007-11-29T22:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1268#issuecomment-7929",
    "user": "https://github.com/robertwb"
}
```

```
(cd .libs && rm -f libmpfi.0 && ln -s libmpfi.0.0.0 libmpfi.0)
(cd .libs && rm -f libmpfi && ln -s libmpfi.0.0.0 libmpfi)
ar cru .libs/libmpfi.a  mpfi.o mpfi_io.o mpfi_trigo.o~ranlib .libs/libmpfi.a
ar: mpfi_trigo.o~ranlib: No such file or directory
make[1]: *** [libmpfi.la] Error 1
make: *** [install-recursive] Error 1
An error occurred while building mpfi.

real    0m19.460s
user    0m4.463s
sys     0m8.673s
sage: An error occurred while installing mpfi-1.3.4-cvs20071125
```

OS X 10.4, Intel (core duo)



---

archive/issue_comments_007930.json:
```json
{
    "body": "I edited the Description to point at a new version of the spkg, that may fix the above OSX compilation failure.",
    "created_at": "2007-11-30T03:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1268#issuecomment-7930",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I edited the Description to point at a new version of the spkg, that may fix the above OSX compilation failure.



---

archive/issue_comments_007931.json:
```json
{
    "body": "Installs fine on Intel OS X 10.5.1.",
    "created_at": "2007-11-30T05:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1268#issuecomment-7931",
    "user": "https://github.com/rlmill"
}
```

Installs fine on Intel OS X 10.5.1.



---

archive/issue_events_003336.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T11:03:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1268#event-3336"
}
```



---

archive/issue_comments_007932.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1268#issuecomment-7932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_007933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1268#issuecomment-7933",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
