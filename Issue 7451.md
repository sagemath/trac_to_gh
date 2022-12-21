# Issue 7451: Setting SAGE_FAT_BINARY causes internal compiler error building pari

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-13 15:38:24

Assignee: tbd

On all 32-bit linux systems, if I set SAGE_FAT_BINARY in sage-4.2.1.rc0, I get an internal compiler error when building PARI.  Since PARI hasn't been upgraded in a while, I think this is the fault of MPIR:



```
gcc  -c -O1 -Wall -fno-strict-aliasing -fomit-frame-pointer    -I. -I../src/headers -I../src/graph -o
 plotport.o ../src/graph/plotport.c
../src/graph/plotport.c: In function 'rectticks':
../src/graph/plotport.c:469: internal compiler error: Segmentation fault
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-4.3/README.Bugs> for instructions.
make[3]: *** [plotport.o] Error 1
make[3]: Leaving directory `/tmp/wstein/farm/sage-4.2.1.rc0/spkg/build/pari-2.3.3.p5/src/Olinux-i686'
make[2]: *** [gp] Error 2
make[2]: Leaving directory `/tmp/wstein/farm/sage-4.2.1.rc0/spkg/build/pari-2.3.3.p5/src'
Error building GP

real    0m9.951s
```


Recommendation: we revert to

  http://wstein.org/home/wstein/patches/mpir-1.2.p8.spkg

so we can release sage-4.2.1.    This is a subtle error and should be reported to the MPIR dev's. 

Note though that I can *build* sage with SAGE_FAT_BINARY="no", then rebuild MPIR with SAGE_FAT_BINARY="yes", and that seems to get around the compiler error.  But I haven't tried running the full test suite, and the fact that upgrading or rebuilding PARI would then result in an internal compiler error is *not* encouraging. 

Another alternative would be to use GMP instead of MPIR for our general distribution version.   It might work better in this regard....


---

Comment by mhansen created at 2009-12-14 02:32:38

This should have been fixed by #7471


---

Comment by mhansen created at 2009-12-14 02:32:38

Resolution: fixed
