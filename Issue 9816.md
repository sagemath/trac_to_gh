# Issue 9816: blas uses non-POSIX option -p to uname. This causes problems on HP-UX.

archive/issues_009816.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @peterjeremy @nexttime\n\nThe POSIX standard for Unix states the command `uname` must exist, and list the options it should take. See\n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html\n\nThe **only** options which should be given in code that can be run on any system is these:\n\n\n```\n    uname [-amnrsv]\n```\n\nbut the BLAS package ignores this, and calls `uname -p`, which screws up on systems like HP-UX where the -p option is not supported. \n\n```\nblas-20070724/src/ztrsm.f\nblas-20070724/src/ztrsv.f\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa2.0w-hp-hpux11.11\nConfigured with: ../gcc-4.3.4/configure --with-gnu-as --with-as=/home/dclarke/local/bin/as --without-gnu-ld --with-ld=/usr/bin/ld --enable-threads=posix --enable-nls --prefix=/home/dclarke/local --enable-shared --enable-multilib --with-included-gettext --with-libiconv-prefix=/home/dclarke/local --with-system-zlib --with-gmp=/home/dclarke/local --with-mpfr=/home/dclarke/local --enable-languages=c,c++,fortran,objc --enable-bootstrap\nThread model: posix\ngcc version 4.3.4 (GCC) \n****************************************************\nuname: illegal option -- p\nusage: uname [-amnrsvil] [-S nodename]\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9817\n\n",
    "created_at": "2010-08-27T09:52:35Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "blas uses non-POSIX option -p to uname. This causes problems on HP-UX.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9816",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @peterjeremy @nexttime

The POSIX standard for Unix states the command `uname` must exist, and list the options it should take. See

http://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html

The **only** options which should be given in code that can be run on any system is these:


```
    uname [-amnrsv]
```

but the BLAS package ignores this, and calls `uname -p`, which screws up on systems like HP-UX where the -p option is not supported. 

```
blas-20070724/src/ztrsm.f
blas-20070724/src/ztrsv.f
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa2.0w-hp-hpux11.11
Configured with: ../gcc-4.3.4/configure --with-gnu-as --with-as=/home/dclarke/local/bin/as --without-gnu-ld --with-ld=/usr/bin/ld --enable-threads=posix --enable-nls --prefix=/home/dclarke/local --enable-shared --enable-multilib --with-included-gettext --with-libiconv-prefix=/home/dclarke/local --with-system-zlib --with-gmp=/home/dclarke/local --with-mpfr=/home/dclarke/local --enable-languages=c,c++,fortran,objc --enable-bootstrap
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
uname: illegal option -- p
usage: uname [-amnrsvil] [-S nodename]

```

Issue created by migration from https://trac.sagemath.org/ticket/9817





---

archive/issue_comments_096645.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2010-09-13T12:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96645",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_comments_096646.json:
```json
{
    "body": "On seconds thoughts, this is a portability issue in general, not one specific to HP-UX. So changing the component back. \n\nDave",
    "created_at": "2010-09-13T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96646",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

On seconds thoughts, this is a portability issue in general, not one specific to HP-UX. So changing the component back. 

Dave



---

archive/issue_comments_096647.json:
```json
{
    "body": "Changing component from AIX or HP-UX ports to porting.",
    "created_at": "2010-09-13T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96647",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from AIX or HP-UX ports to porting.



---

archive/issue_events_024668.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24668"
}
```



---

archive/issue_events_024669.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24669"
}
```



---

archive/issue_events_024670.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24670"
}
```



---

archive/issue_events_024671.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24671"
}
```



---

archive/issue_events_024672.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24672"
}
```



---

archive/issue_events_024673.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24673"
}
```



---

archive/issue_events_024674.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24674"
}
```



---

archive/issue_comments_096648.json:
```json
{
    "body": "There is no longer a \"blas\" package.",
    "created_at": "2015-09-08T12:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96648",
    "user": "https://github.com/jdemeyer"
}
```

There is no longer a "blas" package.



---

archive/issue_events_024675.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-09-08T12:45:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24675"
}
```



---

archive/issue_events_024676.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-09-08T12:45:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24676"
}
```



---

archive/issue_comments_096649.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-08T12:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96649",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096650.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-08T12:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96650",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024677.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-09-12T13:58:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9816#event-24677"
}
```



---

archive/issue_comments_096651.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96651",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
