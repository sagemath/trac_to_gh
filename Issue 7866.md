# Issue 7866: zn_poly on Open Solaris reports  #error Not nails-safe yet

archive/issues_007866.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies\n\n## Build environment\n* Sun Ultra 27 3.333 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)\n* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. \n## The problem\n\n```\nzn_poly-0.9.p1/src/src/mul_fft.c\nzn_poly-0.9.p1/src/src/ks_support.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_111b i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.3.4 (GCC) \n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/invert.o -c src/invert.c\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/ks_support.o -c src/ks_support.c\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid.o -c src/mulmid.c\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c\nsrc/mulmid_ks.c:402:2: error: #error Not nails-safe yet\nmake[2]: *** [src/mulmid_ks.o] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\n./spkg-install: line 39: tune/tune: No such file or directory\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\ngcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/array-DEBUG.o -c src/array.c\ngcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/invert-DEBUG.o -c src/invert.c\ngcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/ks_support-DEBUG.o -c src/ks_support.c\ngcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/mulmid-DEBUG.o -c src/mulmid.c\ngcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/mulmid_ks-DEBUG.o -c src/mulmid_ks.c\nsrc/mulmid_ks.c:402:2: error: #error Not nails-safe yet\nmake[2]: *** [src/mulmid_ks-DEBUG.o] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c\nsrc/mulmid_ks.c:402:2: error: #error Not nails-safe yet\nmake[2]: *** [src/mulmid_ks.o] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c\nsrc/mulmid_ks.c:402:2: error: #error Not nails-safe yet\nmake[2]: *** [src/mulmid_ks.o] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'\nError building zn_poly shared library.\n\nreal\t0m1.026s\nuser\t0m0.860s\nsys\t0m0.144s\nsage: An error occurred while installing zn_poly-0.9.p1\n```\n\n\n == Likely explanation ==\nIt looks as though the -m64 bit flag is not passed properly, so that's the issue. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7866\n\n",
    "created_at": "2010-01-07T06:12:26Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "zn_poly on Open Solaris reports  #error Not nails-safe yet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7866",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies

## Build environment
* Sun Ultra 27 3.333 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
## The problem

```
zn_poly-0.9.p1/src/src/mul_fft.c
zn_poly-0.9.p1/src/src/ks_support.c
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
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/invert.o -c src/invert.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/ks_support.o -c src/ks_support.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid.o -c src/mulmid.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
./spkg-install: line 39: tune/tune: No such file or directory
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/array-DEBUG.o -c src/array.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/invert-DEBUG.o -c src/invert.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/ks_support-DEBUG.o -c src/ks_support.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/mulmid-DEBUG.o -c src/mulmid.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/mulmid_ks-DEBUG.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks-DEBUG.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
Error building zn_poly shared library.

real	0m1.026s
user	0m0.860s
sys	0m0.144s
sage: An error occurred while installing zn_poly-0.9.p1
```


 == Likely explanation ==
It looks as though the -m64 bit flag is not passed properly, so that's the issue. 

Issue created by migration from https://trac.sagemath.org/ticket/7866





---

archive/issue_comments_068094.json:
```json
{
    "body": "This can be closed. It was semi-fixed by #8178, but was not properly fixed until #9358 in sage-4.5.3.alpha1 \n\nDave",
    "created_at": "2011-04-02T13:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7866#issuecomment-68094",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This can be closed. It was semi-fixed by #8178, but was not properly fixed until #9358 in sage-4.5.3.alpha1 

Dave



---

archive/issue_comments_068095.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-04-05T15:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7866#issuecomment-68095",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_008081.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-04-05T15:50:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7866",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7866#event-8081"
}
```
