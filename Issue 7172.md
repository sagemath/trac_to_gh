# Issue 7172: ratpoints should check for gmp is installed, before including it.

Issue created by migration from https://trac.sagemath.org/ticket/7172

Original creator: drkirkby

Original creation time: 2009-10-10 08:03:17

Assignee: tbd

CC:  david.kirkby@onetel.ne

On HP-UX, where there is no gmp.h (the build of that failed), ratpoints is not handling this very elegently - it should check for a program like gmp before trying to use it. 

A ratpoints developer can be given access to this machine, but it seems to me a more general fix is required.  

```
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.4.0 (GCC)
****************************************************
        gcc sift.c -c -o sift.o -I/home/drkirkby/sage-4.1.2.rc0/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops
In file included from rp-private.h:52,
                 from sift.c:29:
ratpoints.h:29:17: error: gmp.h: No such file or directory
In file included from rp-private.h:52,
                 from sift.c:29:
ratpoints.h:41: error: expected specifier-qualifier-list before 'mpz_t'
ratpoints.h:81: warning: type defaults to 'int' in declaration of 'mpz_t'
ratpoints.h:86: warning: type defaults to 'int' in declaration of 'mpz_t'
In file included from sift.c:29:
rp-private.h:150: warning: type defaults to 'int' in declaration of 'mpz_t'
rp-private.h:156: warning: type defaults to 'int' in declaration of 'mpz_t'
sift.c:82: warning: type defaults to 'int' in declaration of 'mpz_t'
sift.c: In function '_ratpoints_sift0':
sift.c:86: error: 'ratpoints_args' has no member named 'sp1'
sift.c:87: error: 'ratpoints_args' has no member named 'sp2'
*** Error exit code 1

Stop.
Build failed. Trying without SSE2 instructions.
        gcc sift.c -c -o sift.o -I/home/drkirkby/sage-4.1.2.rc0/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -funroll-loops
In file included from rp-private.h:52,
                 from sift.c:29:
ratpoints.h:29:17: error: gmp.h: No such file or directory
In file included from rp-private.h:52,
                 from sift.c:29:
ratpoints.h:41: error: expected specifier-qualifier-list before 'mpz_t'
ratpoints.h:81: warning: type defaults to 'int' in declaration of 'mpz_t'
ratpoints.h:86: warning: type defaults to 'int' in declaration of 'mpz_t'
In file included from sift.c:29:
rp-private.h:150: warning: type defaults to 'int' in declaration of 'mpz_t'
rp-private.h:156: warning: type defaults to 'int' in declaration of 'mpz_t'
sift.c:82: warning: type defaults to 'int' in declaration of 'mpz_t'
sift.c: In function '_ratpoints_sift0':
sift.c:86: error: 'ratpoints_args' has no member named 'sp1'
sift.c:87: error: 'ratpoints_args' has no member named 'sp2'
*** Error exit code 1

Stop.
Error building ratpoints

real    0m0.427s
user    0m0.330s
sys     0m0.080s
sage: An error occurred while installing ratpoints-2.1.2.p2

```




---

Comment by jdemeyer created at 2013-06-03 15:03:28

Resolution: wontfix


---

Comment by jdemeyer created at 2013-06-03 15:03:28

Since Sage ships `gmp.h` (by MPIR), this is a non-issue.
