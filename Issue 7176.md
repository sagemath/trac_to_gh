# Issue 7176: sage-4.1.2.rc0 scripts should exit as soon as it can't find gmp.h

Issue created by migration from https://trac.sagemath.org/ticket/7176

Original creator: drkirkby

Original creation time: 2009-10-10 08:30:02

Assignee: tbd

CC:  david.kirkby@onetel.ne

Keywords: HP-UX gmp

MPIR failed to build on an HP machine. Despite the fact the code can't open gmp.h, it does not exit, but the touches other files


```

Deleting directories from past builds of previous/current versions of sage-4.1.2.rc0
Extracting package /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sage-4.1.2.rc0.spkg ...
-rw-r--r--   1 drkirkby   users      41860926 Oct  1 04:40 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sage-4.1.2.rc0.spkg

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
mv: /home/drkirkby/sage-4.1.2.rc0/devel/sage-main: cannot access: No such file or directory
cc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c
cpp: "include/convert.h", line 11: error 4036: Can't open include file 'gmp.h'.
cpp: "include/convert.h", line 12: error 4036: Can't open include file 'pari/pari.h'.
scons: *** [src/convert.os] Error 1

*** TOUCHING ALL CYTHON (.pyx) FILES ***
cc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c
cpp: "include/convert.h", line 11: error 4036: Can't open include file 'gmp.h'.
cpp: "include/convert.h", line 12: error 4036: Can't open include file 'pari/pari.h'.
scons: *** [src/convert.os] Error 1

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
cc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c
cpp: "include/convert.h", line 11: error 4036: Can't open include file 'gmp.h'.
cpp: "include/convert.h", line 12: error 4036: Can't open include file 'pari/pari.h'.
scons: *** [src/convert.os] Error 1
ERROR: There was an error building c_lib.

ERROR installing SAGE

```




---

Comment by jdemeyer created at 2014-02-05 13:00:10

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-02-05 13:00:10

Way outdated.


---

Comment by jdemeyer created at 2014-02-05 13:00:15

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-06 20:50:26

Resolution: wontfix
