# Issue 450: clisp build fixes for Solaris

archive/issues_000450.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere is a bug in clisp's spkg-install that causes compilation\nfailures on Solaris:\n\nThe initial configure run has \"--without-dynamic-ffi\", the makemake\njob doesn't, this leads to the following definitions in clisp.h:\n\n  #define uint64_to_I(val)  uint64_to_I(val)\n  #define sint64_to_I(val)  sint64_to_I(val)\n\nAs you can imagine that doesn't go over too well at link-time. This\nshould also fix the compilation failure of clisp on Nexenta OS that\nDidier reported. With the added flag to makemake clisp builds, but\ncrashes in \"make check\". Even with the fix clisp doesn't compile with\ngcc 4.2.1 on Solaris, at the moment we use gcc 3.4.6.\n\nWe also have to make sure that we don't have \"-g\" in the build flags. \nThis is due to  due to an interaction between gcc's gas and the Sun\n ld when using dwarf2 debugging symbols are used.\n\nA detailed explainaition can be found at\nhttp://www.mail-archive.com/bug-binut...`@`gnu.org/msg00615.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/450\n\n",
    "created_at": "2007-08-19T07:54:42Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "clisp build fixes for Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

There is a bug in clisp's spkg-install that causes compilation
failures on Solaris:

The initial configure run has "--without-dynamic-ffi", the makemake
job doesn't, this leads to the following definitions in clisp.h:

  #define uint64_to_I(val)  uint64_to_I(val)
  #define sint64_to_I(val)  sint64_to_I(val)

As you can imagine that doesn't go over too well at link-time. This
should also fix the compilation failure of clisp on Nexenta OS that
Didier reported. With the added flag to makemake clisp builds, but
crashes in "make check". Even with the fix clisp doesn't compile with
gcc 4.2.1 on Solaris, at the moment we use gcc 3.4.6.

We also have to make sure that we don't have "-g" in the build flags. 
This is due to  due to an interaction between gcc's gas and the Sun
 ld when using dwarf2 debugging symbols are used.

A detailed explainaition can be found at
http://www.mail-archive.com/bug-binut...`@`gnu.org/msg00615.html

Issue created by migration from https://trac.sagemath.org/ticket/450





---

archive/issue_comments_002235.json:
```json
{
    "body": "Okay,\n\nthere is an updated spkg-install at \n\nhttp://sage.math.washington.edu/home/mabshoff/spkg-install-clisp_--without-dynamic-ffi-fix\n\nCaution: The CFLAGS are still \"-O0\", which makes it compile on Itanium, because if I remember correctly \"-O2\" caused crashes there. So the best solution might be to set the CFLAGS conditionally.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-19T18:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/450#issuecomment-2235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Okay,

there is an updated spkg-install at 

http://sage.math.washington.edu/home/mabshoff/spkg-install-clisp_--without-dynamic-ffi-fix

Caution: The CFLAGS are still "-O0", which makes it compile on Itanium, because if I remember correctly "-O2" caused crashes there. So the best solution might be to set the CFLAGS conditionally.

Cheers,

Michael



---

archive/issue_comments_002236.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/450#issuecomment-2236",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002237.json:
```json
{
    "body": "Sam Steingold, the current clisp maintainer, has gotten an account to neron, i.e. our Sun Sparc test platform. Hopefully this will fix all issues we are seeing with clisp :)\n\nCheers,\n\nMichael",
    "created_at": "2007-11-17T07:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/450#issuecomment-2237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sam Steingold, the current clisp maintainer, has gotten an account to neron, i.e. our Sun Sparc test platform. Hopefully this will fix all issues we are seeing with clisp :)

Cheers,

Michael



---

archive/issue_events_000477.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-22T21:07:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/450",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/450#event-477"
}
```



---

archive/issue_comments_002238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T21:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/450#issuecomment-2238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002239.json:
```json
{
    "body": "Clisp 2.44.1 now builds fine with clisp 2.44.1 on Solaris with gcc 3.4.6. Since the fix is upstream we can close this.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T21:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/450#issuecomment-2239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Clisp 2.44.1 now builds fine with clisp 2.44.1 on Solaris with gcc 3.4.6. Since the fix is upstream we can close this.

Cheers,

Michael
