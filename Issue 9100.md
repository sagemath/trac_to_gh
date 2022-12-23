# Issue 9100: scipy is probably building part 32-bit on OpenSolaris x64 when SAGE64=yes

Issue created by migration from https://trac.sagemath.org/ticket/9100

Original creator: drkirkby

Original creation time: 2010-05-31 01:36:58

Assignee: drkirkby

CC:  dimpase

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


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mjo created at 2020-07-12 20:04:07

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by mjo created at 2020-07-12 20:04:07

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
