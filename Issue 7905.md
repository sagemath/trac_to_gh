# Issue 7905: Sun Studio 12 64-bit mode on Solaris.  libgpg-error creates 32-bit binaries.

Issue created by migration from https://trac.sagemath.org/ticket/7905

Original creator: drkirkby

Original creation time: 2010-01-12 08:26:27

Assignee: drkirkby

CC:  jsp dimpase

## Build environment
 * Sun Blade 2000. 2 x UltraSPARC III+ CPUs at 1.2 GHz. 8 GB RAM
 * Solaris 10 update 7 (05/2009)
 * Sage 4.3 with numerous modifications, including updated sage-env to hopefully handle 64-bit builds properly. 
 * Sun Studio 12.1 
 * 64-bit build. SAGE64 was set to yes. 


```
CC=/opt/sunstudio12.1/bin/cc
CXX=/opt/sunstudio12.1/bin/CC
SAGE64=yes
SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.1-sun-linker/lib/libgfortran.so
SAGE_FORTRAN=/opt/sunstudio12.1/bin/f95
```


I'm not sure why I set SAGE_FORTRAN_LIB there, but I doubt it was doing anything. The build breaks with:


```
 /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sun-64/sage-4.3/local/include -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g -O2 -m64 -g -c ath.c  -KPIC -DPIC -o .libs/libgcrypt_la-ath.o
 /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sun-64/sage-4.3/local/include -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g -O2 -m64 -g -c ath.c -o libgcrypt_la-ath.o >/dev/null 2>&1
/bin/bash ../libtool --tag=CC   --mode=link /opt/sunstudio12.1/bin/cc -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g  -O2  -m64  -g      -version-info 16:2:5 -m64  -o libgcrypt.la -rpath /export/home/drkirkby/sun-64/sage-4.3/local/lib libgcrypt_la-visibility.lo libgcrypt_la-misc.lo libgcrypt_la-global.lo libgcrypt_la-sexp.lo libgcrypt_la-hwfeatures.lo libgcrypt_la-stdmem.lo libgcrypt_la-secmem.lo libgcrypt_la-missing-string.lo libgcrypt_la-module.lo libgcrypt_la-fips.lo libgcrypt_la-hmac256.lo libgcrypt_la-ath.lo ../cipher/libcipher.la ../random/librandom.la ../mpi/libmpi.la -L/export/home/drkirkby/sun-64/sage-4.3/local/lib -lgpg-error -lsocket -lsocket 
ld -G -h libgcrypt.so.11 -o .libs/libgcrypt.so.11.5.2  .libs/libgcrypt_la-visibility.o .libs/libgcrypt_la-misc.o .libs/libgcrypt_la-global.o .libs/libgcrypt_la-sexp.o .libs/libgcrypt_la-hwfeatures.o .libs/libgcrypt_la-stdmem.o .libs/libgcrypt_la-secmem.o .libs/libgcrypt_la-missing-string.o .libs/libgcrypt_la-module.o .libs/libgcrypt_la-fips.o .libs/libgcrypt_la-hmac256.o .libs/libgcrypt_la-ath.o -z allextract ../cipher/.libs/libcipher.a ../random/.libs/librandom.a ../mpi/.libs/libmpi.a -z defaultextract  -R/export/home/drkirkby/sun-64/sage-4.3/local/lib -R/export/home/drkirkby/sun-64/sage-4.3/local/lib -L/export/home/drkirkby/sun-64/sage-4.3/local/lib /export/home/drkirkby/sun-64/sage-4.3/local/lib/libgpg-error.so -lsocket -lc 
ld: fatal: file /export/home/drkirkby/sun-64/sage-4.3/local/lib/libgpg-error.so: wrong ELF class: ELFCLASS32
ld: fatal: File processing errors. No output written to .libs/libgcrypt.so.11.5.2
make[4]: *** [libgcrypt.la] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src'
failed to build libgcrypt

real    8m30.831s
user    2m9.479s
sys     1m35.707s
sage: An error occurred while installing libgcrypt-1.4.4.p1
```


Hence I need to resolve why 32-bit binaries are being built, when they should be 64-bit. 



---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mjo created at 2020-07-12 20:03:34

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2020-07-12 20:03:34

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
