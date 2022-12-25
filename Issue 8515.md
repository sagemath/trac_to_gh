# Issue 8515: Optional package frobby-0.7.6  fails to install on Solaris 10 SPARC

archive/issues_008515.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @slel @fchapoton\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n\nThis builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. \n\n == The problem with the optional frobby-0.7.6 ==\n\n```\nfrobby-0.7.6/src/test/transform/t3.gen.m2\nfrobby-0.7.6/src/test/transform/t3.gen.nm\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\ng++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /export/home/drkirkby/sage-4.3.4.alpha1/local/include -O3 -c src/main.cpp -o bin/release/main.o\nsrc/main.cpp: In function 'int main(int, const char**)':\nsrc/main.cpp:30: error: 'srand' was not declared in this scope\nmake: *** [bin/release/main.o] Error 1\nError building Frobby.\n\nreal    0m2.093s\nuser    0m1.446s\nsys     0m0.156s\nsage: An error occurred while installing frobby-0.7.6\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8515\n\n",
    "created_at": "2010-03-13T01:18:43Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package frobby-0.7.6  fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8515",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @slel @fchapoton

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.3.4.alpha1

This builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. 

 == The problem with the optional frobby-0.7.6 ==

```
frobby-0.7.6/src/test/transform/t3.gen.m2
frobby-0.7.6/src/test/transform/t3.gen.nm
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
g++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /export/home/drkirkby/sage-4.3.4.alpha1/local/include -O3 -c src/main.cpp -o bin/release/main.o
src/main.cpp: In function 'int main(int, const char**)':
src/main.cpp:30: error: 'srand' was not declared in this scope
make: *** [bin/release/main.o] Error 1
Error building Frobby.

real    0m2.093s
user    0m1.446s
sys     0m0.156s
sage: An error occurred while installing frobby-0.7.6
```


Issue created by migration from https://trac.sagemath.org/ticket/8515





---

archive/issue_comments_076789.json:
```json
{
    "body": "We now have a new version of Frobby at #13007.   Also, frobby is currently only experimental, not optional, due in part to this issue.",
    "created_at": "2012-06-05T14:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76789",
    "user": "https://github.com/kcrisman"
}
```

We now have a new version of Frobby at #13007.   Also, frobby is currently only experimental, not optional, due in part to this issue.



---

archive/issue_comments_076790.json:
```json
{
    "body": "Changing component from packages: optional to packages: experimental.",
    "created_at": "2017-09-13T12:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76790",
    "user": "https://github.com/koffie"
}
```

Changing component from packages: optional to packages: experimental.



---

archive/issue_comments_076791.json:
```json
{
    "body": "Changing keywords from \"\" to \"frobby, solaris\".",
    "created_at": "2018-11-30T21:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76791",
    "user": "https://github.com/slel"
}
```

Changing keywords from "" to "frobby, solaris".



---

archive/issue_comments_076792.json:
```json
{
    "body": "Changing component from packages: experimental to porting: Solaris.",
    "created_at": "2018-11-30T21:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76792",
    "user": "https://github.com/slel"
}
```

Changing component from packages: experimental to porting: Solaris.



---

archive/issue_comments_076793.json:
```json
{
    "body": "Is this still the case after the work in the following Frobby-related tickets?\n\n- #13007  Update to Frobby 0.9.0\n- #14841  Fixed and improved frobby interface and spkg\n- #20905  converting frobby into a new-style package\n- #21721  Standardize patches in fricas, frobby",
    "created_at": "2018-11-30T21:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76793",
    "user": "https://github.com/slel"
}
```

Is this still the case after the work in the following Frobby-related tickets?

- #13007  Update to Frobby 0.9.0
- #14841  Fixed and improved frobby interface and spkg
- #20905  converting frobby into a new-style package
- #21721  Standardize patches in fricas, frobby



---

archive/issue_comments_076794.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2018-11-30T21:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76794",
    "user": "https://github.com/slel"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_076795.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76795",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_076796.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76796",
    "user": "https://github.com/mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_076797.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-24T06:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8515#issuecomment-76797",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_008695.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-24T06:30:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8515",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8515#event-8695"
}
```
