# Issue 7032: symmetrica ignores CC

archive/issues_007032.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jaapspies\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used  (#7021)\n\nCC was set to the Sun C compiler, and CXX to the Sun C++ compiler. It's apparent that singular is ignoring CC and using gcc instead. \n\n```\nsymmetrica-2.0.p4/src/zyk.c\nsymmetrica-2.0.p4/src/zyk.doc\nsymmetrica-2.0.p4/src/zykelind.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/symmetrica-2.0.p4/src'\ngcc -c -O1 -fPIC -g -DFAST -DALLTRUE bar.c\ngcc -c -O1 -fPIC -g -DFAST -DALLTRUE bi.c\n```\n\nIt does build ok with gcc, even though CC is set to the Sun compiler. There is no C++ code, so I can't immediately tell whether CXX is ignored too, but I suspect it is. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7032\n\n",
    "closed_at": "2010-01-14T02:01:31Z",
    "created_at": "2009-09-27T14:44:54Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "symmetrica ignores CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7032",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @jaapspies

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used  (#7021)

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler. It's apparent that singular is ignoring CC and using gcc instead. 

```
symmetrica-2.0.p4/src/zyk.c
symmetrica-2.0.p4/src/zyk.doc
symmetrica-2.0.p4/src/zykelind.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/symmetrica-2.0.p4/src'
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE bar.c
gcc -c -O1 -fPIC -g -DFAST -DALLTRUE bi.c
```

It does build ok with gcc, even though CC is set to the Sun compiler. There is no C++ code, so I can't immediately tell whether CXX is ignored too, but I suspect it is. 

Issue created by migration from https://trac.sagemath.org/ticket/7032





---

archive/issue_comments_058127.json:
```json
{
    "body": "I've created a fix for this long standing bug. Basically replacing 'gcc' with '$(CC)' in the makefile. \n\nI also changed spkg-install so SAGE64 was respected at the same time (in fact, that was my main motivation for fixing this ticket, as the failure to observe CC is not fatal, but a failure to observe SAGE64 is). \n\nThe symmetica package is odd, in that the SPKG.txt makes it clear that fixes are applied to the source directly, not via patches. I find that a bit odd, but followed in the same way. I needed to fix the 'makefile' but left a copy of what I think is the original makefile as /src/makefile.original \n\nThe package now add -m64 with SAGE64 set to yes, and fully respects CC. \n\n**This must be updated as a package, and not simply a patch applied, due to the fact that changes are made directly in the src directory.**\n\nI've put everything at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/symmetrica-2.0.p5/",
    "created_at": "2010-01-07T01:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7032#issuecomment-58127",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've created a fix for this long standing bug. Basically replacing 'gcc' with '$(CC)' in the makefile. 

I also changed spkg-install so SAGE64 was respected at the same time (in fact, that was my main motivation for fixing this ticket, as the failure to observe CC is not fatal, but a failure to observe SAGE64 is). 

The symmetica package is odd, in that the SPKG.txt makes it clear that fixes are applied to the source directly, not via patches. I find that a bit odd, but followed in the same way. I needed to fix the 'makefile' but left a copy of what I think is the original makefile as /src/makefile.original 

The package now add -m64 with SAGE64 set to yes, and fully respects CC. 

**This must be updated as a package, and not simply a patch applied, due to the fact that changes are made directly in the src directory.**

I've put everything at 

http://boxen.math.washington.edu/home/kirkby/portability/symmetrica-2.0.p5/



---

archive/issue_comments_058128.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-07T01:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7032#issuecomment-58128",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058129.json:
```json
{
    "body": "Looks good, works on Fedora and Open Solaris.\n\nPositive review.\n\nJaap",
    "created_at": "2010-01-10T22:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7032#issuecomment-58129",
    "user": "https://github.com/jaapspies"
}
```

Looks good, works on Fedora and Open Solaris.

Positive review.

Jaap



---

archive/issue_comments_058130.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-10T22:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7032#issuecomment-58130",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016526.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T02:01:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7032#event-16526"
}
```



---

archive/issue_comments_058131.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7032#issuecomment-58131",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
