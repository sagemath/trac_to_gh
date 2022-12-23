# Issue 9816: blas uses non-POSIX option -p to uname. This causes problems on HP-UX.

Issue created by migration from https://trac.sagemath.org/ticket/9817

Original creator: drkirkby

Original creation time: 2010-08-27 09:52:35

Assignee: drkirkby

CC:  pjeremy leif

The POSIX standard for Unix states the command `uname` must exist, and list the options it should take. See

http://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html

The *only* options which should be given in code that can be run on any system is these:



```
    uname [-amnrsv]
```


but the BLAS package ignores this, and calls `uname -p`, which screws up on systems like HP-UX where the -p option is not supported. 


```
blas-20070724/src/ztrsm.f
blas-20070724/src/ztrsv.f
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa2.0w-hp-hpux11.11
Configured with: ../gcc-4.3.4/configure --with-gnu-as --with-as=/home/dclarke/local/bin/as --without-gnu-ld --with-ld=/usr/bin/ld --enable-threads=posix --enable-nls --prefix=/home/dclarke/local --enable-shared --enable-multilib --with-included-gettext --with-libiconv-prefix=/home/dclarke/local --with-system-zlib --with-gmp=/home/dclarke/local --with-mpfr=/home/dclarke/local --enable-languages=c,c++,fortran,objc --enable-bootstrap
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
uname: illegal option -- p
usage: uname [-amnrsvil] [-S nodename]

```



---

Comment by drkirkby created at 2010-09-13 12:14:33

Changing component from porting to AIX or HP-UX ports.


---

Comment by drkirkby created at 2010-09-13 12:17:15

On seconds thoughts, this is a portability issue in general, not one specific to HP-UX. So changing the component back. 

Dave


---

Comment by drkirkby created at 2010-09-13 12:17:15

Changing component from AIX or HP-UX ports to porting.


---

Comment by jdemeyer created at 2015-09-08 12:45:00

There is no longer a "blas" package.


---

Comment by jdemeyer created at 2015-09-08 12:45:00

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-08 12:45:04

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:58:48

Resolution: fixed
