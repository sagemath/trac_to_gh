# Issue 1522: more 2.9-alpha7 ppc osx prebuilt problems

Issue created by migration from https://trac.sagemath.org/ticket/1522

Original creator: craigcitro

Original creation time: 2007-12-15 07:03:06

Assignee: mabshoff

More problems:


```
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/craigcitro/bd7-sage/local/lib -lntl -lgmp -lpari
ld: warning can't open dynamic library: /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib referenced from: /Users/craigcitro/bd7-sage/local/lib/libntl.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
ld: Undefined symbols:
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
___gmpn_sqrtrem referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_sub_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_tdiv_qr referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
/usr/bin/libtool: internal link edit command failed
scons: *** [libcsage.dylib] Error 1
ERROR: There was an error building c_lib.

```


The file libntl.dylib in local/lib mentions /Users/was/ when you do a "strings -" on it, which may or may not be fishy.


---

Comment by mabshoff created at 2007-12-15 07:39:01

Singular might need similar linker flags like the updated NTL, so that the paths to various libraries aren't hardcoded.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 06:43:49

This was fixed either late in the 2.8.x or in the 2.9.x cycle.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 06:43:49

Resolution: fixed


---

Comment by mabshoff created at 2008-01-10 06:44:34

D'oh - this was fixed in 2.9.x [see summary] - need sleep soon ;)
