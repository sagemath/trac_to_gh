# Issue 8521: Optional package  libcocoa-0.9930 fails to install on Solaris 10 SPARC

Issue created by migration from https://trac.sagemath.org/ticket/8521

Original creator: drkirkby

Original creation time: 2010-03-13 14:29:38

Assignee: tbd

CC:  jhpalmieri chapoton dimpase

Keywords: GNUism

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1
 * Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional libcocoa-0.9930 ==
This looks at least partially, perhaps completely because of a GNUism, as a non-POSIX option to 'ar' is used. Instead, only POSIX options should be used for portability.

http://www.opengroup.org/onlinepubs/9699919799/


```
Compiling TmpFrobby.o
Compiling RegisterServerOpsFrobby.o
ar: bad option `S'
usage: ar -d[-vV] archive file ...
       ar -m[-abivV] [posname] archive file ...
       ar -p[-vV][-s] archive [file ...]
       ar -q[-cuvV] [-abi] [posname] [file ...]
       ar -r[-cuvV] [-abi] [posname] [file ...]
       ar -t[-vV][-s] archive [file ...]
       ar -x[-vV][-sCT] archive [file ...]
make[3]: *** [../../lib/libcocoa.a] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930/src/src/AlgebraicCore'
*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****
*****  Compilation failed in CoCoA library source subdirectory AlgebraicCore/  *****
*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****
make[2]: *** [library] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930/src/src'
make[1]: *** [library] Error 2
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930/src'
make: *** [default] Error 2
Doing the build in the following directory:
/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930
./configure  --with-libgmp=$SAGE_LOCAL/lib/libgmp.so
Now running Make
make
There are known test failures that should be listed above.
They are literally 'not yet implemented' errors from the
CoCOA library.   I.e., CoCOA releases purposely don't pass
their own test suite at present.
Error libcocoa.a did not build.

real    4m38.919s
user    4m13.797s
sys     0m21.777s
sage: An error occurred while installing libcocoa-0.9930
```




---

Comment by chapoton created at 2018-12-18 07:30:08

I confirm that there are still some "ar -S" in cocoalib 0.99600.

For example in /CoCoALib-0.99600/src/AlgebraicCore/Makefile

GNU doc about `ar S`:

```
S

Do not generate an archive symbol table. This can speed up building a large library 
in several steps. The resulting archive can not be used with the linker. In order 
to build a symbol table, you must omit the S modifier on the last execution of ar, 
or you must run ranlib on the archive.
```



---

Comment by mkoeppe created at 2020-06-19 18:07:10

solaris tickets should be closed as outdated


---

Comment by mkoeppe created at 2020-06-19 18:07:10

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-19 18:47:55

Resolution: invalid
