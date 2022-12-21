# Issue 8515: Optional package frobby-0.7.6  fails to install on Solaris 10 SPARC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-13 01:18:43

Assignee: tbd

CC:  slelievre chapoton

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1

This builds fully on Solaris 10, and passes all doc tests. This is the first version of Sage to do this. 

 == The problem with the optional frobby-0.7.6 ==

```
frobby-0.7.6/src/test/transform/t3.gen.m2
frobby-0.7.6/src/test/transform/t3.gen.nm
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
g++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /export/home/drkirkby/sage-4.3.4.alpha1/local/include -O3 -c src/main.cpp -o bin/release/main.o
src/main.cpp: In function 'int main(int, const char**)':
src/main.cpp:30: error: 'srand' was not declared in this scope
make: *** [bin/release/main.o] Error 1
Error building Frobby.

real    0m2.093s
user    0m1.446s
sys     0m0.156s
sage: An error occurred while installing frobby-0.7.6
```



---

Comment by kcrisman created at 2012-06-05 14:06:17

We now have a new version of Frobby at #13007.   Also, frobby is currently only experimental, not optional, due in part to this issue.


---

Comment by mderickx created at 2017-09-13 12:30:32

Changing component from packages: optional to packages: experimental.


---

Comment by slelievre created at 2018-11-30 21:46:07

Changing keywords from "" to "frobby, solaris".


---

Comment by slelievre created at 2018-11-30 21:46:07

Changing component from packages: experimental to porting: Solaris.


---

Comment by slelievre created at 2018-11-30 21:46:07

Is this still the case after the work in the following Frobby-related tickets?

- #13007  Update to Frobby 0.9.0
- #14841  Fixed and improved frobby interface and spkg
- #20905  converting frobby into a new-style package
- #21721  Standardize patches in fricas, frobby


---

Comment by slelievre created at 2018-11-30 21:46:07

Changing status from new to needs_info.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from needs_info to needs_review.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by chapoton created at 2020-06-24 06:30:01

Resolution: invalid
