# Issue 9034: flintqs builds as 32-bit despite SAGE64=yes on OpenSolaris x64

archive/issues_009034.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.4.2\n* gcc 4.4.4\n\n## How gcc 4.4.4 was configured\nSince the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n```\n\n\ngcc 4.3.4 was failing to build iconv on OpenSolaris x64, suggesting it may be essential to have a very recent gcc in order to build Sage on OpenSolaris. \n\n## How the Sage build was attempted\n* 64-bit build. SAGE64 was set to \"yes\"\n* #9008 update zlib to latest upstream release to allow a 64-bit library to be built. \n* #9009 update mercurial spkg to build 64-bit.\n* #7982 update sage_fortran so it can build 64-bit binaries.\n* Run 'make -k' to find as many issues as possible quickly on OpenSolaris - see #9026 for a list of the issues known to date. \n\n## The problem with flintqs\n\n```\nflintqs-20070817.p4/src/._TonelliShanks.h\nflintqs-20070817.p4/src/TonelliShanks.h\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n****************************************************\ng++ -ansi -c lprels.c -o lprels.o -I/export/home/drkirkby/sage-4.4.2/local/include -Wall -Wno-sign-compare -fomit-frame-pointer -O3\nlprels.c: In function \u2018FILE* flint_fopen(char*, char*)\u2019:\n<snip>\nSuccessfully installed flintqs-20070817.p4\n```\n\n\nSo no '-m64' flag is added to the g++ command line, so not surprisingly 'flintqs' does not build as a 64-bit binary. The output from the 'file' command confirms this:\n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file  local/bin/QuadraticSieve\nlocal/bin/QuadraticSieve:       ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available\n```\n\n\n## The likely reason for the flintqs problem\n\nspkg-install has this bit of code:\n\n\n```\nif [ `uname -m` = \"x86_64\" ]; then\n    $CP makefile.opteron makefile\nelse\n    if [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n        $CP makefile.osx64 makefile\n    else\n        $CP makefile.sage makefile\n    fi\nfi\n```\n\n\nA cursory glance would suggest the 'makefile.osx64' would work for OpenSolaris, Solaris or most other Unix operating systems, though this has not been tested yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9034\n\n",
    "created_at": "2010-05-24T11:54:06Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "flintqs builds as 32-bit despite SAGE64=yes on OpenSolaris x64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9034",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp

## Build environment
* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
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


gcc 4.3.4 was failing to build iconv on OpenSolaris x64, suggesting it may be essential to have a very recent gcc in order to build Sage on OpenSolaris. 

## How the Sage build was attempted
* 64-bit build. SAGE64 was set to "yes"
* #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
* #9009 update mercurial spkg to build 64-bit.
* #7982 update sage_fortran so it can build 64-bit binaries.
* Run 'make -k' to find as many issues as possible quickly on OpenSolaris - see #9026 for a list of the issues known to date. 

## The problem with flintqs

```
flintqs-20070817.p4/src/._TonelliShanks.h
flintqs-20070817.p4/src/TonelliShanks.h
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
g++ -ansi -c lprels.c -o lprels.o -I/export/home/drkirkby/sage-4.4.2/local/include -Wall -Wno-sign-compare -fomit-frame-pointer -O3
lprels.c: In function ‘FILE* flint_fopen(char*, char*)’:
<snip>
Successfully installed flintqs-20070817.p4
```


So no '-m64' flag is added to the g++ command line, so not surprisingly 'flintqs' does not build as a 64-bit binary. The output from the 'file' command confirms this:


```
drkirkby@hawk:~/sage-4.4.2$ file  local/bin/QuadraticSieve
local/bin/QuadraticSieve:       ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available
```


## The likely reason for the flintqs problem

spkg-install has this bit of code:


```
if [ `uname -m` = "x86_64" ]; then
    $CP makefile.opteron makefile
else
    if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
        $CP makefile.osx64 makefile
    else
        $CP makefile.sage makefile
    fi
fi
```


A cursory glance would suggest the 'makefile.osx64' would work for OpenSolaris, Solaris or most other Unix operating systems, though this has not been tested yet.

Issue created by migration from https://trac.sagemath.org/ticket/9034





---

archive/issue_comments_083637.json:
```json
{
    "body": "Note that the Debian 'dist' subdirectory also exists on this package, and should be removed - see #5903",
    "created_at": "2010-05-24T13:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83637",
    "user": "drkirkby"
}
```

Note that the Debian 'dist' subdirectory also exists on this package, and should be removed - see #5903



---

archive/issue_comments_083638.json:
```json
{
    "body": "Attachment\n\nMercurial patch to build 64-bit",
    "created_at": "2010-05-24T15:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83638",
    "user": "drkirkby"
}
```

Attachment

Mercurial patch to build 64-bit



---

archive/issue_comments_083639.json:
```json
{
    "body": "The attached patch resolves this issue. A new package can be found at:\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/flintqs-20070817.p5.spkg\n\nNow the -m64 flag is added to the compiler\n\n\n```\ng++ -ansi -m64 lprels.o ModuloArith.o TonelliShanks.o F2matrix.o lanczos.o QS.o  -o \"QuadraticSieve\" -L/export/home/drkirkby/sage-4.4.2/local/lib -lgmp\n\nreal    0m0.952s\nuser    0m0.737s\nsys     0m0.108s\nSuccessfully installed flintqs-20070817.p5\n```\n\n\nand the binary is built as 64-bit. \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file  local/bin/QuadraticSieve\nlocal/bin/QuadraticSieve:       ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available\ndrkirkby@hawk:~/sage-4.4.2$ \n```\n",
    "created_at": "2010-05-24T15:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83639",
    "user": "drkirkby"
}
```

The attached patch resolves this issue. A new package can be found at:

http://boxen.math.washington.edu/home/kirkby/patches/flintqs-20070817.p5.spkg

Now the -m64 flag is added to the compiler


```
g++ -ansi -m64 lprels.o ModuloArith.o TonelliShanks.o F2matrix.o lanczos.o QS.o  -o "QuadraticSieve" -L/export/home/drkirkby/sage-4.4.2/local/lib -lgmp

real    0m0.952s
user    0m0.737s
sys     0m0.108s
Successfully installed flintqs-20070817.p5
```


and the binary is built as 64-bit. 


```
drkirkby@hawk:~/sage-4.4.2$ file  local/bin/QuadraticSieve
local/bin/QuadraticSieve:       ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby@hawk:~/sage-4.4.2$ 
```




---

archive/issue_comments_083640.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T15:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83640",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083641.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83641",
    "user": "drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083642.json:
```json
{
    "body": "This is quite an old version of flintqs, so I'm not going to report this upstream as a bug. Someone who wants a later version and has the expertese to test it, is welcome to update the version of flintqs in Sage, but for now, I just want to get it working properly on OpenSolaris. \n\nDave",
    "created_at": "2010-05-24T23:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83642",
    "user": "drkirkby"
}
```

This is quite an old version of flintqs, so I'm not going to report this upstream as a bug. Someone who wants a later version and has the expertese to test it, is welcome to update the version of flintqs in Sage, but for now, I just want to get it working properly on OpenSolaris. 

Dave



---

archive/issue_comments_083643.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T16:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83643",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083644.json:
```json
{
    "body": "It is not strictly needed, but it works ok when SAGE64=yes. Looks ok.\n\nPositive review.\n\nJaap",
    "created_at": "2010-06-10T16:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83644",
    "user": "jsp"
}
```

It is not strictly needed, but it works ok when SAGE64=yes. Looks ok.

Positive review.

Jaap



---

archive/issue_comments_083645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9034#issuecomment-83645",
    "user": "rlm"
}
```

Resolution: fixed
