# Issue 8518: Optional package extra_docs-20070208 fails to install on Solaris 10 SPARC

archive/issues_008518.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jhpalmieri chapoton dimpase\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n\nThis builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. \n\n == The problem with the optional extra_docs-20070208 ==\n\n```\nextra_docs-20070208/zodb/hylton-warsaw-zodb.pdf\nextra_docs-20070208/zodb/zodb3.html\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\n./spkg-install: /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.7/: does not exist\n\nreal    0m8.457s\nuser    0m0.143s\nsys     0m1.989s\nsage: An error occurred while installing extra_docs-20070208\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8518\n\n",
    "created_at": "2010-03-13T01:33:43Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package extra_docs-20070208 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8518",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  jhpalmieri chapoton dimpase

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.3.4.alpha1

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

archive/issue_comments_076937.json:
```json
{
    "body": "solaris tickets should be closed as outdated",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8518#issuecomment-76937",
    "user": "mkoeppe"
}
```

solaris tickets should be closed as outdated



---

archive/issue_comments_076938.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8518#issuecomment-76938",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076939.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-19T18:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8518#issuecomment-76939",
    "user": "chapoton"
}
```

Resolution: invalid
