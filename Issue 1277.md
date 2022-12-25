# Issue 1277: two further flint spkg problems

archive/issues_001277.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nOn Nov 25, 2007 9:52 PM, Bill Hart <goodwillhart@googlemail.com> wrote:\n> \n> This is a compiler bug which we've seen before. On Itanium the build\n> should not be using the -funroll-loops flag.\n> \n> I guess we need to check for ia64 when setting the compiler flags?\n\nThe culprit is this line, which is now in patches/makefile:\n\nCFLAGS = $(INCS) -funroll-loops -fexpensive-optimizations $(FLINT_TUNE) -O3^M\n\nOn ia64 FLINT_TUNE is properly set to not include funroll-loops, but for some dumb\nreason -funroll-loops is put in the CFLAGS explicitly in the patches/makefile included\nin Sage.  \n\nChanging the above line to \n\nCFLAGS = $(INCS)  -fexpensive-optimizations $(FLINT_TUNE) -O3^M\n\ncompletely fixes the problem. \n\nAs an aside, I don't think the .svn subdirectories should be included with\nwith flint-*.spkg.  \n\nA new flint spkg is at \n```\n\n\n  http://sage.math.washington.edu/home/was/tmp/flint-0.9-r1075.p2.spkg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1277\n\n",
    "created_at": "2007-11-26T06:06:45Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "two further flint spkg problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1277",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
On Nov 25, 2007 9:52 PM, Bill Hart <goodwillhart@googlemail.com> wrote:
> 
> This is a compiler bug which we've seen before. On Itanium the build
> should not be using the -funroll-loops flag.
> 
> I guess we need to check for ia64 when setting the compiler flags?

The culprit is this line, which is now in patches/makefile:

CFLAGS = $(INCS) -funroll-loops -fexpensive-optimizations $(FLINT_TUNE) -O3^M

On ia64 FLINT_TUNE is properly set to not include funroll-loops, but for some dumb
reason -funroll-loops is put in the CFLAGS explicitly in the patches/makefile included
in Sage.  

Changing the above line to 

CFLAGS = $(INCS)  -fexpensive-optimizations $(FLINT_TUNE) -O3^M

completely fixes the problem. 

As an aside, I don't think the .svn subdirectories should be included with
with flint-*.spkg.  

A new flint spkg is at 
```


  http://sage.math.washington.edu/home/was/tmp/flint-0.9-r1075.p2.spkg


Issue created by migration from https://trac.sagemath.org/ticket/1277





---

archive/issue_comments_007986.json:
```json
{
    "body": "The new FLINT.spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/flint-1.0.spkg\n\nshould solve the problem.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T20:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1277#issuecomment-7986",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new FLINT.spkg at

http://sage.math.washington.edu/home/mabshoff/flint-1.0.spkg

should solve the problem.

Cheers,

Michael



---

archive/issue_comments_007987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T17:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1277#issuecomment-7987",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001421.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-09T17:23:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1277",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1277#event-1421"
}
```



---

archive/issue_comments_007988.json:
```json
{
    "body": "This was fixed in the Sage 2.9.x time frame, as confirmed by Kate in https://groups.google.com/group/sage-devel/t/40538e2d4e6742dd\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T17:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1277#issuecomment-7988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This was fixed in the Sage 2.9.x time frame, as confirmed by Kate in https://groups.google.com/group/sage-devel/t/40538e2d4e6742dd

Cheers,

Michael
