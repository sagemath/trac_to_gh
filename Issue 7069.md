# Issue 7069: tachyon-0.98beta.p9 ignores CC and uses gcc, so can't build with Sun Studio.

Issue created by migration from https://trac.sagemath.org/ticket/7069

Original creator: drkirkby

Original creation time: 2009-09-29 13:06:53

Assignee: tbd

CC:  mjo dimpase

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used #7021 


```
tachyon-0.98beta.p9/patches/
tachyon-0.98beta.p9/patches/Make-arch.patch
tachyon-0.98beta.p9/patches/Make-arch
tachyon-0.98beta.p9/spkg-install
tachyon-0.98beta.p9/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'
make all \
"ARCH = solaris-pthreads-gcc" \
"CC = gcc" \
"CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS" \
"AR = ar" \
"ARFLAGS = r" \
"STRIP = strip" \
"LIBS = -L. -ltachyon  -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib -lpng12 -lz  -lm -lpthread"
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'
Building Tachyon Parallel Ray Tracing library
Copyright 1994-2007, John E. Stone
All Rights Reserveed
Making architecture directory ../compile/solaris-pthreads-gcc
Making library directory ../compile/solaris-pthreads-gcc/libtachyon
make ../compile ../compile/solaris-pthreads-gcc ../compile/solaris-pthreads-gcc/libtachyon  ../compile/solaris-pthreads-gcc/libtachyon.a  ../compile/solaris-pthreads-gcc/tachyon
make[4]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'
make[4]: Nothing to be done for `../compile'.
make[4]: Nothing to be done for `../compile/solaris-pthreads-gcc'.
make[4]: Nothing to be done for `../compile/solaris-pthreads-gcc/libtachyon'.
gcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/api.c -o ../compile/solaris-pthreads-gcc/libtachyon/api.o
gcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/apigeom.c -o ../compile/solaris-pthreads-gcc/libtachyon/apigeom.o
gcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/box.c -o ../compile/solaris-pthreads-gcc/libtachyon/box.o
```



---

Comment by drkirkby created at 2009-11-09 14:05:08

Changing component from algebra to solaris.


---

Comment by mjo created at 2012-02-25 22:43:33

I think all `$CC` issues were fixed by #9379 and #10681. Can you test on Solaris?


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by chapoton created at 2020-07-14 16:30:16

Resolution: invalid
