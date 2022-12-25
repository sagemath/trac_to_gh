# Issue 8518: Optional package extra_docs-20070208 fails to install on Solaris 10 SPARC

archive/issues_008518.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri @fchapoton @dimpase\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n* Patch #8509 removing the -o option to grep to allow optional packages to install. \n\nThis builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. \n\n == The problem with the optional extra_docs-20070208 ==\n\n```\nextra_docs-20070208/zodb/hylton-warsaw-zodb.pdf\nextra_docs-20070208/zodb/zodb3.html\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\n./spkg-install: /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.7/: does not exist\n\nreal    0m8.457s\nuser    0m0.143s\nsys     0m1.989s\nsage: An error occurred while installing extra_docs-20070208\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8518\n\n",
    "closed_at": "2020-06-19T18:47:45Z",
    "created_at": "2010-03-13T01:33:43Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package extra_docs-20070208 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8518",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @jhpalmieri @fchapoton @dimpase

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.3.4.alpha1
* Patch #8509 removing the -o option to grep to allow optional packages to install. 

This builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. 

 == The problem with the optional extra_docs-20070208 ==

```
extra_docs-20070208/zodb/hylton-warsaw-zodb.pdf
extra_docs-20070208/zodb/zodb3.html
Finished extraction
****************************************************
Host system
uname -a:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.4.3 (GCC)
****************************************************
./spkg-install: /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.7/: does not exist

real    0m8.457s
user    0m0.143s
sys     0m1.989s
sage: An error occurred while installing extra_docs-20070208
```


Issue created by migration from https://trac.sagemath.org/ticket/8518





---

archive/issue_events_020473.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20473"
}
```



---

archive/issue_events_020474.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20474"
}
```



---

archive/issue_events_020475.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20475"
}
```



---

archive/issue_events_020476.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20476"
}
```



---

archive/issue_events_020477.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20477"
}
```



---

archive/issue_events_020478.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20478"
}
```



---

archive/issue_events_020479.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20479"
}
```



---

archive/issue_events_020480.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-19T18:07:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20480"
}
```



---

archive/issue_events_020481.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-19T18:07:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20481"
}
```



---

archive/issue_comments_076810.json:
```json
{
    "body": "solaris tickets should be closed as outdated",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8518#issuecomment-76810",
    "user": "https://github.com/mkoeppe"
}
```

solaris tickets should be closed as outdated



---

archive/issue_comments_076811.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8518#issuecomment-76811",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_020482.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-19T18:47:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8518#event-20482"
}
```



---

archive/issue_comments_076812.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-19T18:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8518#issuecomment-76812",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
