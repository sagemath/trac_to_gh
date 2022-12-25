# Issue 9100: scipy is probably building part 32-bit on OpenSolaris x64 when SAGE64=yes

archive/issues_009100.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @dimpase\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_134 X86\n* Sage 4.4.2\n* gcc 4.4.4\n\n## How gcc 4.4.4 was configured\nSince the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n```\n\n\ngcc 4.3.4 was failing to build iconv. \n\n## The problem\n\nThis is odd, as some temporary files created during the build are clearly 32-bit\n\n\n```\ndrkirkby@hawk:~/sage-4.4.2/spkg/build$ find . -exec file {} \\; | grep 32-bit\n./sage-4.4.2/c_lib/src/convert.pic.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/r1mach.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/i1mach.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/d1mach.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/xerror.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/d1mach.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/i1mach.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/xerror.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/r1mach.o:\tELF 32-bit LSB relocatable 80386 Version 1\n```\n\n\nHowever, parts of it are compiling 64-bit, as can be seen by the -m64 flag below:\n\n\n```\ncompiling C sources\nC compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -fPIC\n\ncreating build/temp.solaris-2.11-i86pc-2.6/build/src.solaris-2.11-i86pc-2.6/scipy/lib/lapack\ncompile options: '-DNO_ATLAS_INFO=2 -I/export/home/drkirkby/sage-4.4.2/local/include -Ibuild/src.solaris-2.11-i86pc-2.6 -I/export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -c'\ngcc: build/src.solaris-2.11-i86pc-2.6/scipy/lib/lapack/calc_lworkmodule.c\ncompiling Fortran sources\nFortran f77 compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -fPIC -O3 -funroll-loops\nFortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops\n```\n\n\nSo I'm amazed this builds at all, but it does:\n\n\n```\ncreating /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy/weave/doc\ncopying scipy/weave/doc/tutorial.txt -> /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy/weave/doc/\ncopying scipy/weave/doc/tutorial_original.html -> /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy/weave/doc/\nrunning install_egg_info\nRemoving /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy-0.7.0-py2.6.egg-info\nWriting /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy-0.7.0-py2.6.egg-info\n\nreal    4m9.963s\nuser    3m53.461s\nsys     0m13.687s\nSuccessfully installed scipy-0.7.p4\n```\n\n\nSo I'm somewhat puzzled by this!\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9100\n\n",
    "created_at": "2010-05-31T01:36:58Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "scipy is probably building part 32-bit on OpenSolaris x64 when SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9100",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @dimpase

## Build environment
* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_134 X86
* Sage 4.4.2
* gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby@hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv. 

## The problem

This is odd, as some temporary files created during the build are clearly 32-bit


```
drkirkby@hawk:~/sage-4.4.2/spkg/build$ find . -exec file {} \; | grep 32-bit
./sage-4.4.2/c_lib/src/convert.pic.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/r1mach.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/i1mach.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/d1mach.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/special/mach/xerror.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/d1mach.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/i1mach.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/xerror.o:	ELF 32-bit LSB relocatable 80386 Version 1
./scipy-0.7.p4/src/build/temp.solaris-2.11-i86pc-2.6/scipy/integrate/mach/r1mach.o:	ELF 32-bit LSB relocatable 80386 Version 1
```


However, parts of it are compiling 64-bit, as can be seen by the -m64 flag below:


```
compiling C sources
C compiler: gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -fPIC

creating build/temp.solaris-2.11-i86pc-2.6/build/src.solaris-2.11-i86pc-2.6/scipy/lib/lapack
compile options: '-DNO_ATLAS_INFO=2 -I/export/home/drkirkby/sage-4.4.2/local/include -Ibuild/src.solaris-2.11-i86pc-2.6 -I/export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/numpy/core/include -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -c'
gcc: build/src.solaris-2.11-i86pc-2.6/scipy/lib/lapack/calc_lworkmodule.c
compiling Fortran sources
Fortran f77 compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -fPIC -O3 -funroll-loops
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops
```


So I'm amazed this builds at all, but it does:


```
creating /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy/weave/doc
copying scipy/weave/doc/tutorial.txt -> /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy/weave/doc/
copying scipy/weave/doc/tutorial_original.html -> /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy/weave/doc/
running install_egg_info
Removing /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy-0.7.0-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.4.2/local/lib/python2.6/site-packages/scipy-0.7.0-py2.6.egg-info

real    4m9.963s
user    3m53.461s
sys     0m13.687s
Successfully installed scipy-0.7.p4
```


So I'm somewhat puzzled by this!

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9100





---

archive/issue_comments_084415.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9100#issuecomment-84415",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084416.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9100#issuecomment-84416",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_084417.json:
```json
{
    "body": "The goal of these tickets is laudable, but:\n\n* We need at least one user who is able to test.\n* The package/OS information on this ticket is outdated beyond usefulness.\n* Upstream is a better place to report portability issues these days.",
    "created_at": "2020-07-12T20:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9100#issuecomment-84417",
    "user": "https://github.com/orlitzky"
}
```

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.



---

archive/issue_comments_084418.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-12T20:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9100#issuecomment-84418",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084419.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9100#issuecomment-84419",
    "user": "https://github.com/fchapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.



---

archive/issue_comments_084420.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9100#issuecomment-84420",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
