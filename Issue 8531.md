# Issue 8531: Optional package  ace-5.0.p0 fails to install on Solaris 10 SPARC

archive/issues_008531.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri @fchapoton @dimpase\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n* Patch #8509 removing the -o option to grep to allow packages to install. \n\n == The problem with the optional ace-5.0.p0 ==\n\n\n```\nace-5.0.p0/.hg/undo.dirstate\nace-5.0.p0/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\nmv: cannot rename ace to /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.10/pkg/: No such file or directory\n./spkg-install: /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.10/pkg//ace: does not exist\n\nreal    0m0.013s\nuser    0m0.004s\nsys     0m0.009s\nsage: An error occurred while installing ace-5.0.p0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8531\n\n",
    "created_at": "2010-03-13T23:12:44Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package  ace-5.0.p0 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8531",
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
* Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional ace-5.0.p0 ==


```
ace-5.0.p0/.hg/undo.dirstate
ace-5.0.p0/.hgignore
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
mv: cannot rename ace to /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.10/pkg/: No such file or directory
./spkg-install: /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.10/pkg//ace: does not exist

real    0m0.013s
user    0m0.004s
sys     0m0.009s
sage: An error occurred while installing ace-5.0.p0
```


Issue created by migration from https://trac.sagemath.org/ticket/8531





---

archive/issue_comments_076977.json:
```json
{
    "body": "solaris tickets should be closed as outdated",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8531#issuecomment-76977",
    "user": "https://github.com/mkoeppe"
}
```

solaris tickets should be closed as outdated



---

archive/issue_comments_076978.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8531#issuecomment-76978",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_008710.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2020-06-19T18:48:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8531",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8531#event-8710"
}
```



---

archive/issue_comments_076979.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-19T18:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8531#issuecomment-76979",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
