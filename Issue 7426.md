# Issue 7426: fix mpir spkg to correctly detect OS X 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-11 01:39:28

Assignee: tbd

The attached patched spkg change the OS X 10.6 detection to the following:

```
            if [ `uname -r | sed 's/\..*//'` != "10" ]; then
```


Before, I just had it do

```
              if [ `uname -r` != "10.0.0" ]; then
```

which is silly, given that 10.6.2 is called 10.0.2.  




---

Comment by was created at 2009-11-11 01:47:24

Changing status from new to needs_review.


---

Comment by was created at 2009-11-11 01:47:24

SPKG Here:   http://wstein.org/home/wstein/patches/mpir-1.2.p8.spkg


---

Comment by mvngu created at 2009-11-13 05:01:10

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-11-13 05:01:10

On bsd.math which now runs OS X 10.6.2, Sage 4.2.1.alpha0 fails to compile with the message (full [install log](http://sage.math.washington.edu/home/mvngu/doc/sage/install/sage-4.2.1/4.2.1.alpha0/install-4.2.1.alpha0-intel-osx-10.6.2.log.bz2) is up on sage.math):

```
mv mach_desc.h ../include/NTL/mach_desc.h
sh MakeGetTime "gcc -I../include -I.  -O2 -g  -fno-common " "-lm"
does anybody really know what time it is?
gcc -I../include -I. -O2 -g -fno-common -o TestGetTime TestGetTime.c GetTime1.c -lm
running
using GetTime1.c
gcc -I../include -I.  -O2 -g  -fno-common   -I/scratch/mvngu/sandbox/sage-4.2.1.alpha0/local/include -o gen_lip_gmp_aux gen_lip_gmp_aux.c -L/scratch/mvngu/sandbox/sage-4.2.1.alpha0/local/lib -lgmp -lm
ld: warning: in /scratch/mvngu/sandbox/sage-4.2.1.alpha0/local/lib/libgmp.dylib, file is not of required architecture
./gen_lip_gmp_aux > lip_gmp_aux_impl.h
NTL_GMP_HACK flag not set.
gcc -I../include -I.  -O2 -g  -fno-common   -I/scratch/mvngu/sandbox/sage-4.2.1.alpha0/local/include -o gen_gmp_aux gen_gmp_aux.c -L/scratch/mvngu/sandbox/sage-4.2.1.alpha0/local/lib -lgmp -lm
ld: warning: in /scratch/mvngu/sandbox/sage-4.2.1.alpha0/local/lib/libgmp.dylib, file is not of required architecture
Undefined symbols:
  "___gmp_bits_per_limb", referenced from:
      _main in ccgka6B4.o
ld: symbol(s) not found
collect2: ld returned 1 exit status
make[2]: *** [setup3] Error 1
Failed building setup3 of NTL

real    0m0.775s
user    0m0.457s
sys     0m0.206s
sage: An error occurred while installing ntl-5.4.2.p9
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/mvngu/sandbox/sage-4.2.1.alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/scratch/mvngu/sandbox/sage-4.2.1.alpha0/spkg/build/ntl-5.4.2.p9 and type 'make'.
Instead type "/scratch/mvngu/sandbox/sage-4.2.1.alpha0/sage -sh"
in order to set all environment variables correctly, then cd to
/scratch/mvngu/sandbox/sage-4.2.1.alpha0/spkg/build/ntl-5.4.2.p9
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/ntl-5.4.2.p9] Error 1

real    13m10.576s
user    7m49.302s
sys     5m4.192s
Error building Sage.
```

I took Sage 4.2.1.alpha0 and replaced its MPIR package mpir-1.2.p7.spkg with the updated package mpir-1.2.p8.spkg. I then compiled this modified source tarball and doctested the whole Sage library. Here are the results of my tests:
 * bsd.math, MacIntel OS X 10.6.2 --- compiled OK; many more doctest failures than on OS X 10.6.1. Full [doctest log](http://sage.math.washington.edu/home/mvngu/doc/sage/doctest/sage-4.2.1/sage-4.2.1.alpha0/doctest-4.2.1.alpha0-7426-intel-osx-10.6.2.log) is up on sage.math.
 * 32-bit openSUSE 11.0, AMD Opteron(tm) Processor 148 --- compiled OK; all doctests passed.
 * 32-bit Ubuntu 9.10, Intel(R) Pentium(R) 4 CPU 3.00GHz --- compiled OK; all doctests passed.
 * 64-bit Ubuntu 8.04.3 LTS, Intel(R) Xeon(R) CPU X7460  `@` 2.66GHz --- compiled OK; all doctests passed.
 * 32-bit Fedora 9, Intel(R) Pentium(R) 4 CPU 2.66GHz --- compiled OK; the following tests failed (full [doctest log](http://sage.math.washington.edu/home/mvngu/doc/sage/doctest/sage-4.2.1/sage-4.2.1.alpha0/doctest-4.2.1.alpha0-7426-cicero.log) up on sage.math):

```
sage -t -long "devel/sage/sage/misc/randstate.pyx"
sage -t -long "devel/sage/sage/interfaces/expect.py"
sage -t -long "devel/sage/sage/interfaces/sage0.py"
```

 * 64-bit Red Hat Enterprise Linux Server 5.4, Intel(R) Xeon(R) CPU X7460  `@` 2.66GHz --- compiled OK; all doctests passed.
 * 64-bit Fedora 9, Intel(R) Core(TM)2 Quad CPU Q6600  `@` 2.40GHz --- compiled OK; all doctests passed.
 * 64-bit Red Hat Enterprise Linux Server 5.3, AMD Phenom(tm) II X4 940 Processor --- compiled OK; all doctests passed.
 * 64-bit openSUSE 11.1, Intel(R) Core(TM)2 Quad CPU Q6600  `@` 2.40GHz, menas --- compiled OK; one doctest failure:

```
[mvngu`@`menas sage-4.2.1.alpha0-7426]$ ./sage -t -long -verbose devel/sage-main/sage/interfaces/ecm.py 
sage -t -long -verbose "devel/sage-main/sage/interfaces/ecm.py"
Traceback (most recent call last):
  File "/home/mvngu/.sage//tmp/.doctest_ecm.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/home/mvngu/usr/menas/sandbox/sage-4.2.1.alpha0-7426/local/lib/python/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/home/mvngu/usr/menas/sandbox/sage-4.2.1.alpha0-7426/local/lib/python/site-packages/sage/all.py", line 68, in <module>
    from sage.libs.all       import *
  File "/home/mvngu/usr/menas/sandbox/sage-4.2.1.alpha0-7426/local/lib/python/site-packages/sage/libs/all.py", line 3, in <module>
    import sage.libs.ntl.all  as ntl
  File "/home/mvngu/usr/menas/sandbox/sage-4.2.1.alpha0-7426/local/lib/python/site-packages/sage/libs/ntl/all.py", line 26, in <module>
    from sage.libs.ntl.ntl_ZZ import (
ImportError: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.11' not found (required by /home/mvngu/usr/menas/sandbox/sage-4.2.1.alpha0-7426/local/lib/libgmpxx.so.3)
         [0.9 s]
exit code: 1024
```

 * MacIntel OS X 10.4.11 --- compiled OK; the following doctest failed ([doctest log](http://sage.math.washington.edu/home/mvngu/doc/sage/doctest/sage-4.2.1/sage-4.2.1.alpha0/doctest-4.2.1.alpha0-7426-intel-osx-10.4.11.log) up on sage.math):

```
sage -t -long -verbose "devel/sage-main/sage/interfaces/maxima.py"
Trying:
    f**g###line 2625:_sage_    >>> f^g
Expecting:
    1/sin(*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
	 [1800.5 s]
exit code: 768
```

Since the updated MPIR package now allows Sage 4.2.1.alpha0 to build on OS X 10.6.2, I give it a positive review.


---

Comment by mhansen created at 2009-11-13 06:32:45

Resolution: fixed


---

Comment by mhansen created at 2009-11-13 06:32:45

Merged the mpir spkg at #6246 which contains this fix.
