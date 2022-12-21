# Issue 7823: libgcrypt-1.4.4.p1 references incorrect shared library on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-01-03 01:53:05

Assignee: pjeremy

CC:  drkirby was

Chase shared library name difference on FreeBSD.  Otherwise the gnutls build fails similar to:

```
(cd /home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/libextra; /bin/sh ../libtool  --tag=CC --mode=relink gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -pipe -I/home/peter/sage/sage-4.3/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -no-undefined -L../lib/.libs -L/home/peter/sage/sage-4.3/local/lib -lopencdk -L/usr/local/lib -L/usr/local/lib -lgcrypt -L/usr/local/lib -lgpg-error -L/usr/local/lib -lintl -L/usr/local/lib -liconv -L/home/peter/sage/sage-4.3/local/lib -lz -R/home/peter/sage/sage-4.3/local/lib -R/usr/local/lib -version-info 27:2:1 -o libgnutls-extra.la -rpath /home/peter/sage/sage-4.3/local/lib gnutls_extra.lo gnutls_openpgp.lo gnutls_ia.lo openpgp/libgnutls_openpgp.la ../lgl/liblgnu.la ../lib/libgnutls.la minilzo/libminilzo.la )  
gcc -std=gnu99 -shared  .libs/gnutls_extra.o .libs/gnutls_openpgp.o .libs/gnutls_ia.o -Wl,--whole-archive openpgp/.libs/libgnutls_openpgp.a ../lgl/.libs/liblgnu.a minilzo/.libs/libminilzo.a -Wl,--no-whole-archive  -Wl,--rpath -Wl,/home/peter/sage/sage-4.3/local/lib -Wl,--rpath -Wl,/usr/local/lib -L/home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/lib/.libs -L/home/peter/sage/sage-4.3/local/lib -lopencdk -L/usr/local/lib -lz -lgcrypt -lintl -liconv -lgpg-error -lgnutls  -Wl,-soname -Wl,libgnutls-extra.so.27 -o .libs/libgnutls-extra.so.27
/usr/bin/ld: /home/peter/sage/sage-4.3/local/lib/libgcrypt.a(libgcrypt_la-visibility.o): relocation R_X86_64_32 can not be used when making a shared object; recompile with -fPIC
/home/peter/sage/sage-4.3/local/lib/libgcrypt.a: could not read symbols: Bad value
libtool: install: error: relink `libgnutls-extra.la' with the above command before installing it
*** Error code 1

Stop in /home/peter/sage/sage-4.3/spkg/build/gnutls-2.2.1.p4/src/libextra.
*** Error code 1
```




---

Attachment


---

Comment by pjeremy created at 2010-01-03 01:56:52

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-05 18:49:04

I'll trust you it worked on FreeBSD. Clearly it can have no impact on any other system, so its a positive from me. 

Dave


---

Comment by drkirkby created at 2010-01-05 18:49:12

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-24 14:18:47

Here is an updated spkg with pjeremy's patch: 

http://sage.math.washington.edu/home/mvngu/spkg/standard/libgcrypt/libgcrypt-1.4.4.p2.spkg

I took libgcrypt-1.4.4.p1.spkg and first checked in all outstanding changes by drkirby in his name. Then I applied pjeremy's patch and checked in changes in pjeremy's name.


---

Comment by mvngu created at 2010-01-24 14:18:47

Resolution: fixed
