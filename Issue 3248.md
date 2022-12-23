# Issue 3248: [with patch; needs review] cygwin -- fix some sagelib setup.py issues and Sconstruct issues involving library includes

Issue created by migration from https://trac.sagemath.org/ticket/3248

Original creator: was

Original creation time: 2008-05-17 20:55:36

Assignee: mabshoff

CC:  craigcitro

1. Something involving the python library in SConstruct that affect c_lib

2. Something library ordering issues that break matrix_real_double_dense in setup.py

3. Choosing ATLAS instead of GSL by default in setup.py


---

Attachment


---

Comment by mabshoff created at 2008-05-17 21:50:13

This patch as is exposes some bugs in the way we build python:

```
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os 
src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config -lntl 
-lgmp -lpari -lpython2.5
/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config
/libpython2.5.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not 
be used when making a shared object; recompile with -fPIC
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config/libpython2.5.a: 
could not read symbols: Bad value
collect2: ld returned 1 exit status
scons: *** [libcsage.so] Error 1

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os 
src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config -lntl 
-lgmp -lpari -lpython2.5
/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config
/libpython2.5.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not 
be used when making a shared object; recompile with -fPIC
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config/libpython2.5.a: 
could not read symbols: Bad value
collect2: ld returned 1 exit status
scons: *** [libcsage.so] Error 1
ERROR: There was an error building c_lib.
```

The likely solution is to force "-fPIC" on the python build, but I need to dig around.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-13 17:46:07

We need to track this down and fix it.

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 04:54:45

Changing keywords from "" to "editor_wstein".


---

Comment by was created at 2010-01-17 12:03:43

This is nearly 2 years old.  My work with Mike Hansen on Windows porting greatly supersedes this.  So I'm closing this.


---

Comment by was created at 2010-01-17 12:03:43

Resolution: duplicate
