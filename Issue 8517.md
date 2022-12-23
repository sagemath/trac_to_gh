# Issue 8517: Optional package gmpy-1.0.1 fails to install on Solaris 10 SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8517

Original creator: drkirkby

Original creation time: 2010-03-13 01:27:07

Assignee: tbd

CC:  vdelecroix vklein

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




---

Comment by mkoeppe created at 2018-03-05 00:07:33

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2018-03-05 00:07:33

This is outdated and should be closed.


---

Comment by chapoton created at 2018-03-14 16:07:30

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2018-03-14 16:12:48

Resolution: invalid
