# Issue 8516: Optional package ginv-1.9-20080723 fails to install on Solaris 10 SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8516

Original creator: drkirkby

Original creation time: 2010-03-13 01:22:58

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



---

Comment by malb created at 2012-01-23 15:23:38

There's a new optional SPKG here http://sage.math.washington.edu/home/malb/spkgs/ginv-1.9-20080723.p0.spkg which should fix the issue.


---

Comment by malb created at 2012-01-23 15:23:38

Changing status from new to needs_review.


---

Comment by malb created at 2014-06-30 18:45:54

Changing status from needs_review to needs_work.


---

Comment by malb created at 2014-06-30 18:45:54

Definitely way too old be "needs review"


---

Comment by mkoeppe created at 2019-11-23 16:29:10

This is outdated and should be closed.


---

Comment by mkoeppe created at 2020-06-19 18:07:10

solaris tickets should be closed as outdated


---

Comment by mkoeppe created at 2020-06-19 18:07:10

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2020-06-19 18:47:38

Resolution: invalid
