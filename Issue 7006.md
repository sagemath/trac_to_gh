# Issue 7006: [with patch; needs review] os x 10.6 port -- update mpir to autodetect ABI on OS X since ABI=32 is *no* longer necessarily the default on 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-25 00:54:56

Assignee: tbd

CC:  palmieri mvngu

The spkg is up here:

  http://sage.math.washington.edu/home/wstein/patches/mpir-1.2.p5.spkg


---

Comment by jhpalmieri created at 2009-09-25 21:31:27

This doesn't seem to build properly on OS X 10.5, 32-bit.  (As far as I can tell, it works with 10.5 64-bit and also with 10.6).  The problem occurs when starting to build ntl:

```
mv mach_desc.h ../include/NTL/mach_desc.h
sh MakeGetTime "gcc -I../include -I.  -O2 -g  -fno-common " "-lm"
does anybody really know what time it is?
gcc -I../include -I. -O2 -g -fno-common -o TestGetTime TestGetTime.c GetTime1.c -lm
running
using GetTime1.c
gcc -I../include -I.  -O2 -g  -fno-common   -I/Applications/sage_builds/sage-4.1.2.alpha2/local/include -o gen_lip_gmp_aux gen_lip_gmp_aux.c -L/Applications/sage_builds/sage-4.1.2.alpha2/local/lib -lgmp -lm
ld warning: in /Applications/sage_builds/sage-4.1.2.alpha2/local/lib/libgmp.dylib, file is not of required architecture
./gen_lip_gmp_aux > lip_gmp_aux_impl.h
NTL_GMP_HACK flag not set.
gcc -I../include -I.  -O2 -g  -fno-common   -I/Applications/sage_builds/sage-4.1.2.alpha2/local/include -o gen_gmp_aux gen_gmp_aux.c -L/Applications/sage_builds/sage-4.1.2.alpha2/local/lib -lgmp -lm
ld warning: in /Applications/sage_builds/sage-4.1.2.alpha2/local/lib/libgmp.dylib, file is not of required architecture
Undefined symbols:
  "___gmp_bits_per_limb", referenced from:
      ___gmp_bits_per_limb$non_lazy_ptr in ccWvp3La.o
ld: symbol(s) not found
collect2: ld returned 1 exit status
make[2]: *** [setup3] Error 1
Failed building setup3 of NTL
```

If I install the old version of mpir using './sage -f mpir-1.2.p4.spkg', then ntl builds correctly.


---

Comment by was created at 2009-09-25 21:51:32

New version here that should behave as before on all older os x's:

  http://sage.math.washington.edu/home/wstein/patches/mpir-1.2.p6.spkg


---

Comment by mvngu created at 2009-09-27 01:21:21

New MPIR package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/mpir-1.2.p7.spkg

The only change from .p6 is:

 * Remove the junk file `spkg-install~`.


---

Comment by mvngu created at 2009-09-27 02:28:15

See palmieri's and my reports at #6849.


---

Comment by mvngu created at 2009-09-27 02:28:15

Resolution: fixed
