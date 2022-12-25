# Issue 7767: PARI thinks C compiler is broken on Open Solaris.

archive/issues_007767.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  david.kirkby@onetel.net\n\nOn a Sun Ultra 27, running Open Solaris 06/2009 and gcc 4.3.4, I get the following error when trying to build PARI:\n\nI've not looked yet, but the chances are it some GNUism passing inappropriate flags to the compiler. It might be a problem with pari, or it might be a problem in something Sage does, so at this point in time, I've not reported this upstream, despite the fact it might be an upstream bug. \n\n```\npari-2.3.3.p5/src/CHANGES-2.2\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_111b i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4/ --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.3.4 (GCC) \n****************************************************\nConfiguring pari-2.3.3 (STABLE) \nChecking echo to see how to suppress newlines...\n...using \\c\nLooking for some tools first ...\n...ld is /usr/ccs/bin/ld\n...zcat is /usr/bin/zcat\n...gzip is /usr/bin/gzip\n...ranlib is /usr/ccs/bin/ranlib\n...perl is /usr/bin/perl\n...I could not find emacs.\n******************************************************************\n* C compiler does not work. PARI/GP requires an ANSI C compiler! *\n* Aborting.                                                      *\n******************************************************************\nCompiler was: gcc\nERROR - configure PARI with readline and gmp failed.\n\nreal\t0m0.145s\nuser\t0m0.047s\nsys\t0m0.053s\nsage: An error occurred while installing pari-2.3.3.p5\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7767\n\n",
    "closed_at": "2013-10-05T09:39:03Z",
    "created_at": "2009-12-26T03:39:14Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "PARI thinks C compiler is broken on Open Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7767",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  david.kirkby@onetel.net

On a Sun Ultra 27, running Open Solaris 06/2009 and gcc 4.3.4, I get the following error when trying to build PARI:

I've not looked yet, but the chances are it some GNUism passing inappropriate flags to the compiler. It might be a problem with pari, or it might be a problem in something Sage does, so at this point in time, I've not reported this upstream, despite the fact it might be an upstream bug. 

```
pari-2.3.3.p5/src/CHANGES-2.2
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_111b i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4/ --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
Configuring pari-2.3.3 (STABLE) 
Checking echo to see how to suppress newlines...
...using \c
Looking for some tools first ...
...ld is /usr/ccs/bin/ld
...zcat is /usr/bin/zcat
...gzip is /usr/bin/gzip
...ranlib is /usr/ccs/bin/ranlib
...perl is /usr/bin/perl
...I could not find emacs.
******************************************************************
* C compiler does not work. PARI/GP requires an ANSI C compiler! *
* Aborting.                                                      *
******************************************************************
Compiler was: gcc
ERROR - configure PARI with readline and gmp failed.

real	0m0.145s
user	0m0.047s
sys	0m0.053s
sage: An error occurred while installing pari-2.3.3.p5
```



Issue created by migration from https://trac.sagemath.org/ticket/7767





---

archive/issue_comments_066837.json:
```json
{
    "body": "Is this issue fixed by #9343?  If yes, we can close this ticket.",
    "created_at": "2010-08-01T16:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66837",
    "user": "https://github.com/jdemeyer"
}
```

Is this issue fixed by #9343?  If yes, we can close this ticket.



---

archive/issue_comments_066838.json:
```json
{
    "body": "Replying to [comment:1 jdemeyer]:\n> Is this issue fixed by #9343?  If yes, we can close this ticket.\n\nAt this point in time, #9343 has not been merged to any stable release (only alphas), so I think currently this ticket should stay open. \n\nIn theory  #9343 could be reverted, though I doubt that will happen.",
    "created_at": "2010-09-28T02:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66838",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:1 jdemeyer]:
> Is this issue fixed by #9343?  If yes, we can close this ticket.

At this point in time, #9343 has not been merged to any stable release (only alphas), so I think currently this ticket should stay open. 

In theory  #9343 could be reverted, though I doubt that will happen.



---

archive/issue_comments_066839.json:
```json
{
    "body": "Did you at least try it with PARI 2.3.**5** (which is e.g. included in Sage 4.5.3)?",
    "created_at": "2010-09-28T22:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66839",
    "user": "https://github.com/nexttime"
}
```

Did you at least try it with PARI 2.3.**5** (which is e.g. included in Sage 4.5.3)?



---

archive/issue_events_018582.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7767#event-18582"
}
```



---

archive/issue_comments_066840.json:
```json
{
    "body": "Assuming this is fixed.",
    "created_at": "2013-10-03T10:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66840",
    "user": "https://github.com/jdemeyer"
}
```

Assuming this is fixed.



---

archive/issue_events_018583.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-03T10:20:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7767#event-18583"
}
```



---

archive/issue_events_018584.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-03T10:20:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7767#event-18584"
}
```



---

archive/issue_comments_066841.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-10-03T10:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66841",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-10-03T10:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66842",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018585.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-05T09:39:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7767#event-18585"
}
```



---

archive/issue_comments_066843.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-10-05T09:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7767#issuecomment-66843",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
