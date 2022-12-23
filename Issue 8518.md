# Issue 8518: Optional package extra_docs-20070208 fails to install on Solaris 10 SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8518

Original creator: drkirkby

Original creation time: 2010-03-13 01:33:43

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



---

Comment by mkoeppe created at 2020-06-19 18:07:10

solaris tickets should be closed as outdated


---

Comment by mkoeppe created at 2020-06-19 18:07:10

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-19 18:47:45

Resolution: invalid
