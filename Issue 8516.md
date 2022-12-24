# Issue 8516: Optional package ginv-1.9-20080723 fails to install on Solaris 10 SPARC

archive/issues_008516.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri @fchapoton @dimpase\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n\nThis builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. \n\n == The problem with the optional ginv-1.9-20080723 ==\nThis appears to be sending some x86 specific options to the compiler:\n\n\n```\nginv-1.9-20080723/patches/setup.py\nginv-1.9-20080723/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran\nThread model: posix\ngcc version 4.4.3 (GCC)\n****************************************************\nrunning build\nrunning build_ext\nbuilding 'ginv' extension\ncreating build\ncreating build/temp.solaris-2.10-sun4u-2.6\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/util\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/monom\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/coeff\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/poly\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/criteria\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/division\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/algorithm\ncreating build/temp.solaris-2.10-sun4u-2.6/ginv/gauss\ncreating build/temp.solaris-2.10-sun4u-2.6/modules\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DWORDS_BIGENDIAN -I/export/home/drkirkby/sage-4.3.4.alpha1/local/include/python2.6 -c ginv/util/iprime.cpp -o build/temp.solaris-2.10-sun4u-2.6/ginv/util/iprime.o -O3 -pipe -mmmx -msse -m3dnow -fomit-frame-pointer -I/export/home/drkirkby/sage-4.3.4.alpha1/local/include\ncc1plus: error: unrecognized command line option \"-mmmx\"\ncc1plus: error: unrecognized command line option \"-msse\"\ncc1plus: error: unrecognized command line option \"-m3dnow\"\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nerror: command 'gcc' failed with exit status 1\nError building GINV.\n\nreal    0m0.410s\nuser    0m0.251s\nsys     0m0.135s\nsage: An error occurred while installing ginv-1.9-20080723\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8516\n\n",
    "created_at": "2010-03-13T01:22:58Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package ginv-1.9-20080723 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8516",
    "user": "drkirkby"
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

This builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. 

 == The problem with the optional ginv-1.9-20080723 ==
This appears to be sending some x86 specific options to the compiler:


```
ginv-1.9-20080723/patches/setup.py
ginv-1.9-20080723/.hgignore
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
running build
running build_ext
building 'ginv' extension
creating build
creating build/temp.solaris-2.10-sun4u-2.6
creating build/temp.solaris-2.10-sun4u-2.6/ginv
creating build/temp.solaris-2.10-sun4u-2.6/ginv/util
creating build/temp.solaris-2.10-sun4u-2.6/ginv/monom
creating build/temp.solaris-2.10-sun4u-2.6/ginv/coeff
creating build/temp.solaris-2.10-sun4u-2.6/ginv/poly
creating build/temp.solaris-2.10-sun4u-2.6/ginv/criteria
creating build/temp.solaris-2.10-sun4u-2.6/ginv/division
creating build/temp.solaris-2.10-sun4u-2.6/ginv/algorithm
creating build/temp.solaris-2.10-sun4u-2.6/ginv/gauss
creating build/temp.solaris-2.10-sun4u-2.6/modules
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DWORDS_BIGENDIAN -I/export/home/drkirkby/sage-4.3.4.alpha1/local/include/python2.6 -c ginv/util/iprime.cpp -o build/temp.solaris-2.10-sun4u-2.6/ginv/util/iprime.o -O3 -pipe -mmmx -msse -m3dnow -fomit-frame-pointer -I/export/home/drkirkby/sage-4.3.4.alpha1/local/include
cc1plus: error: unrecognized command line option "-mmmx"
cc1plus: error: unrecognized command line option "-msse"
cc1plus: error: unrecognized command line option "-m3dnow"
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
error: command 'gcc' failed with exit status 1
Error building GINV.

real    0m0.410s
user    0m0.251s
sys     0m0.135s
sage: An error occurred while installing ginv-1.9-20080723
```


Issue created by migration from https://trac.sagemath.org/ticket/8516





---

archive/issue_comments_076925.json:
```json
{
    "body": "There's a new optional SPKG here http://sage.math.washington.edu/home/malb/spkgs/ginv-1.9-20080723.p0.spkg which should fix the issue.",
    "created_at": "2012-01-23T15:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76925",
    "user": "@malb"
}
```

There's a new optional SPKG here http://sage.math.washington.edu/home/malb/spkgs/ginv-1.9-20080723.p0.spkg which should fix the issue.



---

archive/issue_comments_076926.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-23T15:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76926",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076927.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-06-30T18:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76927",
    "user": "@malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076928.json:
```json
{
    "body": "Definitely way too old be \"needs review\"",
    "created_at": "2014-06-30T18:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76928",
    "user": "@malb"
}
```

Definitely way too old be "needs review"



---

archive/issue_comments_076929.json:
```json
{
    "body": "This is outdated and should be closed.",
    "created_at": "2019-11-23T16:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76929",
    "user": "@mkoeppe"
}
```

This is outdated and should be closed.



---

archive/issue_comments_076930.json:
```json
{
    "body": "solaris tickets should be closed as outdated",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76930",
    "user": "@mkoeppe"
}
```

solaris tickets should be closed as outdated



---

archive/issue_comments_076931.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76931",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076932.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-19T18:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8516#issuecomment-76932",
    "user": "@fchapoton"
}
```

Resolution: invalid
