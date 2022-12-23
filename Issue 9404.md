# Issue 9404: Assembler reports  junk buidling Singular on OpenSolaris x64 (disk.math)

Issue created by migration from https://trac.sagemath.org/ticket/9404

Original creator: drkirkby

Original creation time: 2010-07-02 01:26:47

Assignee: drkirkby

CC:  was dimpase

An error occurs when building sage-4.5.alpha1 (with some patches) on disk.math, an OpenSolaris machine running !openSolaros 2008.11 (snv_101b_rc2)

The exact same source builds fine on OpenSolaris 2009.06 which has been updated to build 134. I suspect some of the tools on this system need updating. 

## Hardware
 * disk.math.washington.edu x64 hardware of some sort. 
 * OpenSolaris 2008.11 (snv_101b)
 * 32 GB RAM
 * 2 x quad core 2.3 GHz CPUs

## GCC Configuration
The configuration of gcc on OpenSolaris is quite critical. This is the GCC included with OpenSolaris 11.2008. 

```
-bash-3.2$ gcc -v
Reading specs from /opt/sfw/lib/gcc/i386-pc-solaris2.11/4.3.2/specs
Target: i386-pc-solaris2.11
Configured with: ./configure --prefix=/opt/sfw --enable-shared --with-gmp=/opt/sfw --with-mpfr=/opt/sfw --with-gnu-as --with-as=/usr/sfw/bin/gas --without-gnu-ld --with-ld=/usr/ccs/bin/ld --enable-stage1-languages=c,c++ --enable-languages=c,c++,objc,fortran
Thread model: posix
gcc driver version 4.3.2 (GCC) executing gcc version 4.2.3
```


GCC is configured to use a rather old version (version 2.15 from 2002) version of the GNU assembler /usr/sfw/bin/gas. I suspect an upgrade of gcc and/or the assembler might cure this. 

## The error message


```
ck.c -o omDebugTrack.o_ndebug
gcc -m64 -O2 -g -m64  -fPIC -I. -I/export/home/kirkby/sage-4.5.alpha1/local/include -I/export/home/kirkby/sage-4.5.alpha1/local/include -O2 -g -m64 -DHAVE_CONFIG_H -DOM_NDEBUG -c omalloc_provide.c -o omalloc_provide.o_ndebug
gcc -m64 -O2 -g -m64  -fPIC -I. -I/export/home/kirkby/sage-4.5.alpha1/local/include -I/export/home/kirkby/sage-4.5.alpha1/local/include -O2 -g -m64 -DHAVE_CONFIG_H -DOM_NDEBUG -c omAllocFunc.c -o omAllocFunc.o_ndebug
rm -f libomalloc_ndebug.a
ar cr libomalloc_ndebug.a omBinPage.o_ndebug omList.o_ndebug omAllocEmulate.o_ndebug omDebug.o_ndebug om_Alloc.o_ndebug omDebugCheck.o_ndebug omOpts.o_ndebug omGetBackTrace.o_ndebug omAllocSystem.o_ndebug omError.o_ndebug omStats.o_ndebug omRet2Info.o_ndebug omBin.o_ndebug omFindExec.o_ndebug omDebugTrack.o_ndebug omalloc_provide.o_ndebug omAllocFunc.o_ndebug 
ranlib libomalloc_ndebug.a
gcc -m64 -O2 -g -m64  -fPIC -I. -I/export/home/kirkby/sage-4.5.alpha1/local/include -I/export/home/kirkby/sage-4.5.alpha1/local/include -O2 -g -m64 -DHAVE_CONFIG_H -DOM_NDEBUG -c omalloc.c -o omalloc.o
gcc -m64 -O2 -g -m64  -fPIC -I. -I/export/home/kirkby/sage-4.5.alpha1/local/include -I/export/home/kirkby/sage-4.5.alpha1/local/include -O2 -g -m64 -DHAVE_CONFIG_H -c omalloc_debug.c -o omalloc_debug.o
gcc -m64 -g -pg -O3 -I. -I/export/home/kirkby/sage-4.5.alpha1/local/include -I/export/home/kirkby/sage-4.5.alpha1/local/include -O2 -g -m64 -DHAVE_CONFIG_H -c omBinPage.c -o omBinPage.op
/var/tmp//cc1HaW.a.s: Assembler messages:
/var/tmp//cc1HaW.a.s:26: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:101: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:170: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:268: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:482: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:824: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:1254: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:1730: Error: junk `@' after expression
/var/tmp//cc1HaW.a.s:2031: Error: junk `@' after expression
make[4]: *** [omBinPage.op] Error 1
make[4]: Leaving directory `/export/home/kirkby/sage-4.5.alpha1/spkg/build/singular-3.1.0.4.p8/src/omalloc'
make[3]: *** [install] Error 1
make[3]: Leaving directory `/export/home/kirkby/sage-4.5.alpha1/spkg/build/singular-3.1.0.4.p8/src'
make[2]: *** [/export/home/kirkby/sage-4.5.alpha1/local/bin/Singular-3-1-0] Error 2
make[2]: Leaving directory `/export/home/kirkby/sage-4.5.alpha1/spkg/build/singular-3.1.0.4.p8/src'
Unable to build Singular.

real	0m53.374s
user	0m8.135s
sys	0m8.073s
sage: An error occurred while installing singular-3.1.0.4.p8
```





---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by chapoton created at 2020-07-14 16:30:26

Resolution: invalid
