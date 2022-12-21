# Issue 8843: fix c_lib on Cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-05-03 04:50:09

Assignee: tbd

CC:  wstein

Cygwin can't load shared libraries via symlinks.  Therefore, we have to actually copy libcsage.so/csage.dll over to $SAGE_LOCAL/lib/.  Note that currently the "install" target in SConstruct does nothing.


---

Comment by mhansen created at 2010-05-03 13:26:00

Changing status from new to needs_review.


---

Comment by was created at 2010-05-25 06:43:06

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-05-25 06:43:06

Unfortunately, after applying this, libcsage just doesn't build anymore.


---

Attachment


---

Comment by mhansen created at 2010-05-25 18:21:38

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-05-25 18:21:38

I've posted a new patch which should work.


---

Comment by was created at 2010-05-26 00:14:41

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-05-26 00:14:41

Doesn't work:


```
Installing c_lib
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib -L/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
/usr/bin/ld: /mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/libpython2.6.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not be used when making a shared object; recompile with -fPIC
/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/libpython2.6.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
scons: *** [libcsage.so] Error 1
ERROR: There was an error building c_lib.
```


However, Mike says there is a Python spkg that may fix this...


---

Comment by was created at 2010-05-26 01:00:10

Resolution: fixed
