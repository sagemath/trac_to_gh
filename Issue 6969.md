# Issue 6969: port boehm gc to os x 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-20 22:05:59

Assignee: tbd

The error:


```
 gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=\"7.1\" "-DPACKAGE_STRING=\"gc 7.1\"" -DPACKAGE_BUGREPORT=\"Hans.Boehm`@`hp.com\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\"gc\" -DVERSION=\"7.1\" -DGC_DARWIN_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DHAS_X86_THREAD_STATE32___EAX=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -O2 -g -fPIC -m64 -MT mach_dep.lo -MD -MP -MF .deps/mach_dep.Tpo -c mach_dep.c  -fno-common -DPIC -o .libs/mach_dep.o
In file included from mach_dep.c:163:
/usr/include/ucontext.h:42:2: error: #error ucontext routines are deprecated, and require _XOPEN_SOURCE to be defined
make[1]: *** [mach_dep.lo] Error 1
make: *** [all-recursive] Error 1
bash-3.2$ 
```




---

Comment by was created at 2009-09-20 22:06:10

This page is relevant:

http://duriansoftware.com/joe/PSA:-avoiding-the-%22ucontext-routines-are-deprecated%22-error-on-Mac-OS-X-Snow-Leopard.html


---

Comment by was created at 2009-09-20 22:22:25

Patch up here:

     http://sage.math.washington.edu/home/wstein/patches/boehm_gc-7.1.p2.spkg


---

Comment by mvngu created at 2009-09-27 01:48:43

Positive review. See palmieri's and my report at #6849.


---

Comment by mvngu created at 2009-09-27 01:53:48

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:54:29

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
