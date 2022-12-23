# Issue 9970: Build problem in boehm_gc found with randomised testing

Issue created by migration from https://trac.sagemath.org/ticket/9971

Original creator: drkirkby

Original creation time: 2010-09-22 22:42:46

Assignee: GeorgSWeber

CC:  leif

In an attempt to uncover race conditions in Makefiles, a shell script called "gcc" was written which calls the normal "gcc" after some random time interval. This was done in response to build problems in Singular (see #9946), were the source code of the file for generating the random delay can be found. 

When I tried to build the whole of Sage, there's a failure of boehm_gc-7.1.p6. 

Despite the package name, this would appear to be an unstable snapshot taken from CVS, as the latest stable release is 6.8 - see http://www.hpl.hp.com/personal/Hans_Boehm/gc/

Here's the build failure, though a full log is attached in the file `boehm_gc-7.1.p6.log.nfg.txt` 

I'll try the latest CVS and see if this is the latest version, but its difficult to report this upstream when we use a non-stable release. 


```
 gcc "-DPACKAGE_NAME=\"gc\"" "-DPACKAGE_TARNAME=\"gc\"" "-DPACKAGE_VERSION=\"7.1\"" "-DPACKAGE_STRING=\"gc 7.1\"" "-DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\"" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 "-DPACKAGE=\"gc\"" "-DVERSION=\"7.1\"" -DGC_SOLARIS_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DSOLARIS25_PROC_VDB_BUG_FIXED=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -g -O2 -MT finalize.lo -MD -MP -MF .deps/finalize.Tpo -c finalize.c  -fPIC -DPIC -o .libs/finalize.o
 gcc "-DPACKAGE_NAME=\"gc\"" "-DPACKAGE_TARNAME=\"gc\"" "-DPACKAGE_VERSION=\"7.1\"" "-DPACKAGE_STRING=\"gc 7.1\"" "-DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\"" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 "-DPACKAGE=\"gc\"" "-DVERSION=\"7.1\"" -DGC_SOLARIS_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DSOLARIS25_PROC_VDB_BUG_FIXED=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -g -O2 -MT dyn_load.lo -MD -MP -MF .deps/dyn_load.Tpo -c dyn_load.c  -fPIC -DPIC -o .libs/dyn_load.o
 gcc "-DPACKAGE_NAME=\"gc\"" "-DPACKAGE_TARNAME=\"gc\"" "-DPACKAGE_VERSION=\"7.1\"" "-DPACKAGE_STRING=\"gc 7.1\"" "-DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\"" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 "-DPACKAGE=\"gc\"" "-DVERSION=\"7.1\"" -DGC_SOLARIS_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DSOLARIS25_PROC_VDB_BUG_FIXED=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -g -O2 -MT blacklst.lo -MD -MP -MF .deps/blacklst.Tpo -c blacklst.c  -fPIC -DPIC -o .libs/blacklst.o
 gcc "-DPACKAGE_NAME=\"gc\"" "-DPACKAGE_TARNAME=\"gc\"" "-DPACKAGE_VERSION=\"7.1\"" "-DPACKAGE_STRING=\"gc 7.1\"" "-DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\"" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 "-DPACKAGE=\"gc\"" "-DVERSION=\"7.1\"" -DGC_SOLARIS_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DSOLARIS25_PROC_VDB_BUG_FIXED=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -g -O2 -MT dbg_mlc.lo -MD -MP -MF .deps/dbg_mlc.Tpo -c dbg_mlc.c  -fPIC -DPIC -o .libs/dbg_mlc.o
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [dyn_load.lo] Error 1
make[3]: *** Waiting for unfinished jobs....
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [alloc.lo] Error 1
make[3]: *** [mallocx.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [finalize.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [gcj_mlc.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [checksums.lo] Error 1
make[3]: *** [allchblk.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [headers.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [gc_dlopen.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [dbg_mlc.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [blacklst.lo] Error 1
gcc: 7.1": No such file or directory
<command-line>:0:16: warning: missing terminating " character
make[3]: *** [malloc.lo] Error 1
make[3]: Leaving directory `/export/home/drkirkby/slow/sage-4.6.alpha1/spkg/build/boehm_gc-7.1.p6/src'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/export/home/drkirkby/slow/sage-4.6.alpha1/spkg/build/boehm_gc-7.1.p6/src'
Error building BoehmGC.

real	8m38.373s
user	0m4.844s
sys	0m5.826s
sage: An error occurred while installing boehm_gc-7.1.p6
```



---

Comment by drkirkby created at 2010-09-22 22:44:17

Build failure obseved when random delays were inserted into the build process of boehm_gc-7.1.p6


---

Attachment


---

Comment by leif created at 2010-09-22 23:45:24

Looks more like an error in your script, not like a race condition. ;-)


---

Attachment

gcc script, which calls the real gcc after some delay


---

Comment by drkirkby created at 2010-09-23 00:14:33

I've attached the script. How would you change it? 

Dave


---

Comment by leif created at 2010-09-23 01:33:31

Replying to [comment:3 drkirkby]:
> I've attached the script. How would you change it? 


```diff
--- gcc.orig	2010-09-23 03:29:02.000000000 +0200
+++ gcc	2010-09-23 03:30:15.000000000 +0200
@@ -1,3 +1,3 @@
 #!/bin/sh 
 /usr/local/bin/randomsleep
-/usr/local/gcc-4.5.0/bin/gcc $@
+/usr/local/gcc-4.5.0/bin/gcc "$@"
```


So should I set it to "needs work" or "won't fix / invalid"? ;-)


---

Comment by drkirkby created at 2010-09-23 06:49:50

Changing status from new to needs_info.


---

Comment by drkirkby created at 2010-09-23 06:49:50

Yes, I should have quoted it. 

Since at this point we don't know if there's an issue with this boehm_gc, I've stuck it to "needs info". I'll test it with the revised scrpt, then either set either set the ticket to "new" or "invalid". 

Dave


---

Comment by jdemeyer created at 2014-02-04 08:12:19

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2014-02-04 08:12:19

Close as invalid.


---

Comment by vbraun created at 2014-02-04 21:10:56

Resolution: invalid
