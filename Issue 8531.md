# Issue 8531: Optional package  ace-5.0.p0 fails to install on Solaris 10 SPARC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-13 23:12:44

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
 * Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional ace-5.0.p0 ==


```
ace-5.0.p0/.hg/undo.dirstate
ace-5.0.p0/.hgignore
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
mv: cannot rename ace to /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.10/pkg/: No such file or directory
./spkg-install: /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/gap-4.4.10/pkg//ace: does not exist

real    0m0.013s
user    0m0.004s
sys     0m0.009s
sage: An error occurred while installing ace-5.0.p0
```



---

Comment by mkoeppe created at 2020-06-19 18:07:10

solaris tickets should be closed as outdated


---

Comment by mkoeppe created at 2020-06-19 18:07:10

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-19 18:48:16

Resolution: invalid
