# Issue 7173: zn_poly does not handle the case of missing gmp.h very elegantly.

Issue created by migration from https://trac.sagemath.org/ticket/7173

Original creator: drkirkby

Original creation time: 2009-10-10 08:09:30

Assignee: tbd

CC:  david.kirkby@onetel.ne

This is on HP-UX, where MPIR failed to build. Whilst I can undertand zn_poly failing to build, it would be useful if it checked for the presence of gmp.h, like many programs do.

A developer could have access to an HP-UX box, but I doubt it is needed to fix this issue. 


```
-rw-r--r--   1 drkirkby   users       185851 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/zn_poly-0.9.p1.spkg
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
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.4.0 (GCC)
****************************************************
        gcc -fPIC -O3 -L. -I/home/drkirkby/sage-4.1.2.rc0/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c
In file included from src/array.c:23:
./include/zn_poly_internal.h:38:17: error: gmp.h: No such file or directory
In file included from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/zn_poly.h:33:20: error: stdint.h: No such file or directory
In file included from ./include/zn_poly.h:75,
                 from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wide multiplication available for this machine; using generic C code instead.
In file included from src/array.c:23:
./include/zn_poly_internal.h:133: error: expected ')' before '*' token
./include/zn_poly_internal.h:258: error: expected ')' before '*' token
./include/zn_poly_internal.h:278: error: expected ';', ',' or ')' before '*' token
./include/zn_poly_internal.h:1410: error: expected ')' before '*' token
./include/zn_poly_internal.h:1421: error: expected ')' before '*' token
./include/zn_poly_internal.h:1433: error: expected ')' before '*' token
./include/zn_poly_internal.h:1445: error: expected ')' before '*' token
./include/zn_poly_internal.h:1464: error: expected ')' before '*' token
./include/zn_poly_internal.h:1473: error: expected ')' before '*' token
*** Error exit code 1

Stop.
./spkg-install: tune/tune: No such file or directory
        gcc -g -fPIC -O3 -L. -I/home/drkirkby/sage-4.1.2.rc0/local/include -I./include -DDEBUG -o src/array-DEBUG.o -c src/array.c
In file included from src/array.c:23:
./include/zn_poly_internal.h:38:17: error: gmp.h: No such file or directory
In file included from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/zn_poly.h:33:20: error: stdint.h: No such file or directory
In file included from ./include/zn_poly.h:75,
                 from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wide multiplication available for this machine; using generic C code instead.
In file included from src/array.c:23:
./include/zn_poly_internal.h:133: error: expected ')' before '*' token
./include/zn_poly_internal.h:258: error: expected ')' before '*' token
./include/zn_poly_internal.h:278: error: expected ';', ',' or ')' before '*' token
./include/zn_poly_internal.h:1410: error: expected ')' before '*' token
./include/zn_poly_internal.h:1421: error: expected ')' before '*' token
./include/zn_poly_internal.h:1433: error: expected ')' before '*' token
./include/zn_poly_internal.h:1445: error: expected ')' before '*' token
./include/zn_poly_internal.h:1464: error: expected ')' before '*' token
./include/zn_poly_internal.h:1473: error: expected ')' before '*' token
*** Error exit code 1

Stop.
        gcc -fPIC -O3 -L. -I/home/drkirkby/sage-4.1.2.rc0/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c
In file included from src/array.c:23:
./include/zn_poly_internal.h:38:17: error: gmp.h: No such file or directory
In file included from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/zn_poly.h:33:20: error: stdint.h: No such file or directory
In file included from ./include/zn_poly.h:75,
                 from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wide multiplication available for this machine; using generic C code instead.
In file included from src/array.c:23:
./include/zn_poly_internal.h:133: error: expected ')' before '*' token
./include/zn_poly_internal.h:258: error: expected ')' before '*' token
./include/zn_poly_internal.h:278: error: expected ';', ',' or ')' before '*' token
./include/zn_poly_internal.h:1410: error: expected ')' before '*' token
./include/zn_poly_internal.h:1421: error: expected ')' before '*' token
./include/zn_poly_internal.h:1433: error: expected ')' before '*' token
./include/zn_poly_internal.h:1445: error: expected ')' before '*' token
./include/zn_poly_internal.h:1464: error: expected ')' before '*' token
./include/zn_poly_internal.h:1473: error: expected ')' before '*' token
*** Error exit code 1

Stop.
        gcc -fPIC -O3 -L. -I/home/drkirkby/sage-4.1.2.rc0/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c
In file included from src/array.c:23:
./include/zn_poly_internal.h:38:17: error: gmp.h: No such file or directory
In file included from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/zn_poly.h:33:20: error: stdint.h: No such file or directory
In file included from ./include/zn_poly.h:75,
                 from ./include/zn_poly_internal.h:41,
                 from src/array.c:23:
./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wide multiplication available for this machine; using generic C code instead.
In file included from src/array.c:23:
./include/zn_poly_internal.h:133: error: expected ')' before '*' token
./include/zn_poly_internal.h:258: error: expected ')' before '*' token
./include/zn_poly_internal.h:278: error: expected ';', ',' or ')' before '*' token
./include/zn_poly_internal.h:1410: error: expected ')' before '*' token
./include/zn_poly_internal.h:1421: error: expected ')' before '*' token
./include/zn_poly_internal.h:1433: error: expected ')' before '*' token
./include/zn_poly_internal.h:1445: error: expected ')' before '*' token
./include/zn_poly_internal.h:1464: error: expected ')' before '*' token
./include/zn_poly_internal.h:1473: error: expected ')' before '*' token
*** Error exit code 1

Stop.
Error building zn_poly shared library.

real    0m1.450s
user    0m1.050s
sys     0m0.200s
sage: An error occurred while installing zn_poly-0.9.p1

```



---

Comment by Snark created at 2012-06-16 20:13:47

At ticket #12433, I ask about writing an autotools build system for zn_poly and push it upstream. Wouldn't that fix that report too?


---

Comment by jdemeyer created at 2014-02-14 12:45:55

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-02-14 12:45:55

If `mpir` fails to build, then Sage will not even attempt to build `zn_poly`. Close as wontfix.


---

Comment by jdemeyer created at 2014-02-14 12:46:01

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-19 18:57:29

Resolution: wontfix
