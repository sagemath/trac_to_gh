# Issue 1520: prebuilt 2.9-alpha7 osx ppc binary has hardcoded paths

Issue created by migration from https://trac.sagemath.org/ticket/1520

Original creator: craigcitro

Original creation time: 2007-12-15 05:54:59

Assignee: mabshoff

File untars and runs just fine, but trying to change anything and build causes a lot of this:


```
g++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o -L/Users/craigcitro/bd7-sage/local//lib -lcsage -lcsage -lntl -lstdc++ -lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so
/usr/bin/ld: warning can't open dynamic library: /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib referenced from: /Users/craigcitro/bd7-sage/local//lib/libcsage.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/bin/ld: warning can't open dynamic library: libpari-gmp.dylib referenced from: /Users/craigcitro/bd7-sage/local//lib/libcsage.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/bin/ld: Undefined symbols:
___gmpn_add_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_addmul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_divrem_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_gcd referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_gcdext referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_lshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_mod_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_mul referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_mul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_rshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_sqrtrem referenced from libntl expected to be defined in /Users/was/sage
-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_sub_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_tdiv_qr referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.

```



---

Comment by mabshoff created at 2007-12-15 06:33:37

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2007-12-15 06:55:57

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 06:55:57

Resolution: fixed
