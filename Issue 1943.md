# Issue 1943: Sage 2.10.1.rc0: rpy fails to build on OSX 10.4

Issue created by migration from https://trac.sagemath.org/ticket/1943

Original creator: mabshoff

Original creation time: 2008-01-26 23:12:28

Assignee: mabshoff

Robert Bradshaw reported the following:

```
running build_ext
building '_rpy2061' extension
C compiler: gcc -g -Wall -I/Users/robert/sage/sage-2.10.1.rc0/local/
include -L/Users/robert/sage/sage-2.10.1.rc0/local/lib/

creating build/temp.macosx-10.3-i386-2.5
creating build/temp.macosx-10.3-i386-2.5/src
compile options: '-DWITH_NUMERIC=3 -DPY_ARRAY_TYPES_PREFIX=PyArray_ -
DRPY_SHNAME=_rpy2061 -DINIT_RPY=init_rpy2061 -UPRE_2_2 -I/Users/
robert/sage/sage-2.10.1.rc0/local/lib/R/include -Isrc -I/Users/robert/
sage/sage-2.10.1.rc0/local/lib/python2.5/site-packages/numpy/core/
include -I/Users/robert/sage/sage-2.10.1.rc0/local/include/python2.5 -c'
gcc: src/io2061.c
src/io2061.c: In function ‘RPy_ReadConsole’:
src/io2061.c:131: warning: pointer targets in passing argument 1 of  
‘snprintf’ differ in signedness
src/io2061.c: At top level:
/Users/robert/sage/sage-2.10.1.rc0/local/lib/python2.5/site-packages/
numpy/core/include/numpy/__multiarray_api.h:944: warning:  
‘_import_array’ defined but not used
gcc: src/R_eval2061.c
/Users/robert/sage/sage-2.10.1.rc0/local/lib/python2.5/site-packages/
numpy/core/include/numpy/__multiarray_api.h:944: warning:  
‘_import_array’ defined but not used
gcc: src/rpymodule2061.c
src/rpymodule2061.c:1488: warning: initialization from incompatible  
pointer type
src/rpymodule2061.c:1491: warning: ‘intargfunc’ is deprecated
src/rpymodule2061.c:1491: warning: initialization from incompatible  
pointer type
src/rpymodule2061.c:1493: warning: initialization from incompatible  
pointer type
gcc -bundle -undefined dynamic_lookup -L/Users/robert/sage/
sage-2.10.1.rc0/local/lib/ -I/Users/robert/sage/sage-2.10.1.rc0/local/
include -L/Users/robert/sage/sage-2.10.1.rc0/local/lib/ build/
temp.macosx-10.3-i386-2.5/src/rpymodule2061.o build/temp.macosx-10.3-
i386-2.5/src/R_eval2061.o build/temp.macosx-10.3-i386-2.5/src/
io2061.o -L/Users/robert/sage/sage-2.10.1.rc0/local/lib/R/bin -L/
Users/robert/sage/sage-2.10.1.rc0/local/lib/R/lib -L/Users/robert/
sage/sage-2.10.1.rc0/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/  
-L/Users/robert/sage/sage-2.10.1.rc0/local/lib/R/bin -L/Users/robert/
sage/sage-2.10.1.rc0/local/lib/R/lib -L/Users/robert/sage/
sage-2.10.1.rc0/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/ -lR -
llapack -lcblas -latlas -lf95 -o build/lib.macosx-10.3-i386-2.5/
_rpy2061.so
/usr/bin/ld: warning can't open dynamic library: libRblas.dylib  
referenced from: /Users/robert/sage/sage-2.10.1.rc0/local/lib/R/lib/
libR.dylib (checking for undefined symbols may be affected) (No such  
file or directory, errno = 2)
/usr/bin/ld: Undefined symbols:
_dgemm_ referenced from libR expected to be defined in libRblas.dylib
_dsyrk_ referenced from libR expected to be defined in libRblas.dylib
_zgemm_ referenced from libR expected to be defined in libRblas.dylib
_dcopy_ referenced from libR expected to be defined in libRblas.dylib
_dtrsm_ referenced from libR expected to be defined in libRblas.dylib
_daxpy_ referenced from libR expected to be defined in libRblas.dylib
_dswap_ referenced from libR expected to be defined in libRblas.dylib
_ddot_ referenced from libR expected to be defined in libRblas.dylib
__g95_sign_r8 referenced from libR expected to be defined in  
libRblas.dylib
_dasum_ referenced from libR expected to be defined in libRblas.dylib
_dscal_ referenced from libR expected to be defined in libRblas.dylib
_dnrm2_ referenced from libR expected to be defined in libRblas.dylib
_drot_ referenced from libR expected to be defined in libRblas.dylib
_drotg_ referenced from libR expected to be defined in libRblas.dylib
collect2: ld returned 1 exit status
/usr/bin/ld: warning can't open dynamic library: libRblas.dylib  
referenced from: /Users/robert/sage/sage-2.10.1.rc0/local/lib/R/lib/
libR.dylib (checking for undefined symbols may be affected) (No such  
file or directory, errno = 2)
/usr/bin/ld: Undefined symbols:
_dgemm_ referenced from libR expected to be defined in libRblas.dylib
_dsyrk_ referenced from libR expected to be defined in libRblas.dylib
_zgemm_ referenced from libR expected to be defined in libRblas.dylib
_dcopy_ referenced from libR expected to be defined in libRblas.dylib
_dtrsm_ referenced from libR expected to be defined in libRblas.dylib
_daxpy_ referenced from libR expected to be defined in libRblas.dylib
_dswap_ referenced from libR expected to be defined in libRblas.dylib
_ddot_ referenced from libR expected to be defined in libRblas.dylib
__g95_sign_r8 referenced from libR expected to be defined in  
libRblas.dylib
_dasum_ referenced from libR expected to be defined in libRblas.dylib
_dscal_ referenced from libR expected to be defined in libRblas.dylib
_dnrm2_ referenced from libR expected to be defined in libRblas.dylib
_drot_ referenced from libR expected to be defined in libRblas.dylib
_drotg_ referenced from libR expected to be defined in libRblas.dylib
collect2: ld returned 1 exit status
error: Command "gcc -bundle -undefined dynamic_lookup -L/Users/robert/
sage/sage-2.10.1.rc0/local/lib/ -I/Users/robert/sage/sage-2.10.1.rc0/
local/include -L/Users/robert/sage/sage-2.10.1.rc0/local/lib/ build/
temp.macosx-10.3-i386-2.5/src/rpymodule2061.o build/temp.macosx-10.3-
i386-2.5/src/R_eval2061.o build/temp.macosx-10.3-i386-2.5/src/
io2061.o -L/Users/robert/sage/sage-2.10.1.rc0/local/lib/R/bin -L/
Users/robert/sage/sage-2.10.1.rc0/local/lib/R/lib -L/Users/robert/
sage/sage-2.10.1.rc0/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/  
-L/Users/robert/sage/sage-2.10.1.rc0/local/lib/R/bin -L/Users/robert/
sage/sage-2.10.1.rc0/local/lib/R/lib -L/Users/robert/sage/
sage-2.10.1.rc0/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/ -lR -
llapack -lcblas -latlas -lf95 -o build/lib.macosx-10.3-i386-2.5/
_rpy2061.so" failed with exit status 1
Error building RPY -- Python interface to R.

real    0m2.094s
user    0m0.656s
sys     0m0.650s
sage: An error occurred while installing rpy-1.0.1.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/robert/sage/sage-2.10.1.rc0/install.log.  Describe your  
computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/robert/sage/sage-2.10.1.rc0/spkg/build/rpy-1.0.1.p0 and type  
'make'.
Instead type "/Users/robert/sage/sage-2.10.1.rc0/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/robert/sage/sage-2.10.1.rc0/spkg/build/rpy-1.0.1.p0
(When you are done debugging, you can type "exit" to leave the
subshell.)
Error installing rpy.

real    4m44.687s
user    2m17.993s
sys     1m33.051s
sage: An error occurred while installing r-2.6.1.p13
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/robert/sage/sage-2.10.1.rc0/install.log.  Describe your  
computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/robert/sage/sage-2.10.1.rc0/spkg/build/r-2.6.1.p13 and type  
'make'. 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 02:23:26

A working r.spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc1/r-2.6.1.p14.spkg

It builds fine on linux, OSX 10.5 & 10.4. I have also tested it on linux and OSX 10.5, but am waiting for the OSX 10.4 build to finish.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 03:36:35

The rpy test now also passes on OSX 10.4


---

Comment by mabshoff created at 2008-01-27 03:37:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 03:37:03

Merged in Sage 2.10.1.rc1
