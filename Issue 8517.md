# Issue 8517: Optional package gmpy-1.0.1 fails to install on Solaris 10 SPARC

archive/issues_008517.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @videlec @vinklein\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n\nThis builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. \n\n == The problem with the optional gmpy-1.0.1 ==\n\n```\ngmpy-1.0.1/doc/index.html\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\n./spkg-install: CFLAGS=-I/export/home/drkirkby/sage-4.3.4.alpha1/local/include: is not an identifier\n\nreal    0m0.008s\nuser    0m0.002s\nsys     0m0.005s\nsage: An error occurred while installing gmpy-1.0.1\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8517\n\n",
    "created_at": "2010-03-13T01:27:07Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package gmpy-1.0.1 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8517",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  @videlec @vinklein

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.3.4.alpha1

This builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. 

 == The problem with the optional gmpy-1.0.1 ==

```
gmpy-1.0.1/doc/index.html
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
./spkg-install: CFLAGS=-I/export/home/drkirkby/sage-4.3.4.alpha1/local/include: is not an identifier

real    0m0.008s
user    0m0.002s
sys     0m0.005s
sage: An error occurred while installing gmpy-1.0.1
```



Issue created by migration from https://trac.sagemath.org/ticket/8517





---

archive/issue_comments_076933.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-03-05T00:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8517#issuecomment-76933",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076934.json:
```json
{
    "body": "This is outdated and should be closed.",
    "created_at": "2018-03-05T00:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8517#issuecomment-76934",
    "user": "@mkoeppe"
}
```

This is outdated and should be closed.



---

archive/issue_comments_076935.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-03-14T16:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8517#issuecomment-76935",
    "user": "@fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076936.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2018-03-14T16:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8517#issuecomment-76936",
    "user": "@jdemeyer"
}
```

Resolution: invalid
