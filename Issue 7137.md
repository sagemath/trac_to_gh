# Issue 7137: always building 32-bit on Solaris even when SAGE64="yes"

archive/issues_007137.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nLooking at the directory $SAGE_HOME/local/bin, we can see that *ratpoint* is being built as 32-bit binary, despite the fact that SAGE64 was set to \"yes\"\n\n```\ndrkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/bin] $ file ratpoint\nratpoint:       ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, stripped\n```\n\n\nThis is **far** from the only package building 32-bit when SAGE64 is set to \"yes\" on Solaris. All of the following do, and I suspect there are many others too.\n\n* zlib #7128\n* libgpg_error #7129\n* libpng #7130\n* libcliquer #7131\n* pari #7133\n* ntl #7134 \n* python #7135\n* gp #7136\n    \nmpir currently mixes 32 and 64-bit objects, so does not build at all #7132.\n\nI will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.\n\nAlthough there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.\n\nIBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nThe sensible way to resolve this is to add the correct flag on every platform.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7137\n\n",
    "created_at": "2009-10-06T01:01:17Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "always building 32-bit on Solaris even when SAGE64=\"yes\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7137",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Using

* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/bin, we can see that *ratpoint* is being built as 32-bit binary, despite the fact that SAGE64 was set to "yes"

```
drkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/bin] $ file ratpoint
ratpoint:       ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, stripped
```


This is **far** from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too.

* zlib #7128
* libgpg_error #7129
* libpng #7130
* libcliquer #7131
* pari #7133
* ntl #7134 
* python #7135
* gp #7136
    
mpir currently mixes 32 and 64-bit objects, so does not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.


Issue created by migration from https://trac.sagemath.org/ticket/7137





---

archive/issue_comments_059052.json:
```json
{
    "body": "This was fixed for OpenSolaris #8351. The fix also works for Solaris 10, so this can be closed. \n\nDave",
    "created_at": "2010-08-20T15:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7137#issuecomment-59052",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This was fixed for OpenSolaris #8351. The fix also works for Solaris 10, so this can be closed. 

Dave



---

archive/issue_comments_059053.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-20T15:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7137#issuecomment-59053",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Resolution: fixed



---

archive/issue_events_007357.json:
```json
{
    "actor": "drkirkby",
    "created_at": "2010-08-20T15:27:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7137",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7137#event-7357"
}
```
