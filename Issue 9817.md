# Issue 9817: boehm_gc installs OK on HP-UX, but fails one of 6 tests if SAGE_CHECK=yes

Issue created by migration from https://trac.sagemath.org/ticket/9818

Original creator: drkirkby

Original creation time: 2010-08-27 10:06:51

Assignee: drkirkby

CC:  dimpase

## Hardware/Software
 * HP C3600 workstation
 * 1 x 552 MHz PA-RISC CPU
 * 8 GB RAM
 * HP-UX 11.11B
 * Sage 4.5.3.alpha2
 * boehm_gc-7.1.p6 (that's boehm_gc-7.1 patched 7 times in Sage)

 == The failure ==


```
	if gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=\"7.1\" -DPACKAGE_STRING=\"gc\ 7.1\" -DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\"gc\" -DVERSION=\"7.1\" -DGC_HPUX_THREADS=1 -D_POSIX_C_SOURCE=199506L -DTHREAD_LOCAL_ALLOC=1 -D_REENTRANT=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1  -I./include   -fexceptions -I libatomic_ops/src -g -O2 -MT tests/smash_test.o -MD -MP -MF "$depbase.Tpo" -c -o tests/smash_test.o tests/smash_test.c; \
	then mv -f "$depbase.Tpo" "$depbase.Po"; else rm -f "$depbase.Tpo"; exit 1; fi
/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o smashtest  tests/smash_test.o ./libgc.la  
libtool: link: warning: this platform does not like uninstalled shared libraries
libtool: link: `smashtest' will be relinked during installation
gcc -fexceptions -I libatomic_ops/src -g -O2 -o .libs/smashtest tests/smash_test.o  ./.libs/libgc.sl -lpthread -lrt -Wl,+b -Wl,/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src/.libs:/home/drkirkby/sage-4.5.3.alpha2/local/lib
creating smashtest
depbase=`echo tests/huge_test.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`; \
	if gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=\"7.1\" -DPACKAGE_STRING=\"gc\ 7.1\" -DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\"gc\" -DVERSION=\"7.1\" -DGC_HPUX_THREADS=1 -D_POSIX_C_SOURCE=199506L -DTHREAD_LOCAL_ALLOC=1 -D_REENTRANT=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1  -I./include   -fexceptions -I libatomic_ops/src -g -O2 -MT tests/huge_test.o -MD -MP -MF "$depbase.Tpo" -c -o tests/huge_test.o tests/huge_test.c; \
	then mv -f "$depbase.Tpo" "$depbase.Po"; else rm -f "$depbase.Tpo"; exit 1; fi
/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o hugetest  tests/huge_test.o ./libgc.la  
libtool: link: warning: this platform does not like uninstalled shared libraries
libtool: link: `hugetest' will be relinked during installation
gcc -fexceptions -I libatomic_ops/src -g -O2 -o .libs/hugetest tests/huge_test.o  ./.libs/libgc.sl -lpthread -lrt -Wl,+b -Wl,/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src/.libs:/home/drkirkby/sage-4.5.3.alpha2/local/lib
creating hugetest
depbase=`echo tests/thread_leak_test.o | sed 's|[^/]*$|.deps/&|;s|\.o$||'`; \
	if gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=\"7.1\" -DPACKAGE_STRING=\"gc\ 7.1\" -DPACKAGE_BUGREPORT=\"Hans.Boehm@hp.com\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\"gc\" -DVERSION=\"7.1\" -DGC_HPUX_THREADS=1 -D_POSIX_C_SOURCE=199506L -DTHREAD_LOCAL_ALLOC=1 -D_REENTRANT=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1  -I./include   -fexceptions -I libatomic_ops/src -g -O2 -MT tests/thread_leak_test.o -MD -MP -MF "$depbase.Tpo" -c -o tests/thread_leak_test.o tests/thread_leak_test.c; \
	then mv -f "$depbase.Tpo" "$depbase.Po"; else rm -f "$depbase.Tpo"; exit 1; fi
/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o threadleaktest  tests/thread_leak_test.o ./libgc.la  
libtool: link: warning: this platform does not like uninstalled shared libraries
libtool: link: `threadleaktest' will be relinked during installation
gcc -fexceptions -I libatomic_ops/src -g -O2 -o .libs/threadleaktest tests/thread_leak_test.o  ./.libs/libgc.sl -lpthread -lrt -Wl,+b -Wl,/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src/.libs:/home/drkirkby/sage-4.5.3.alpha2/local/lib
creating threadleaktest
make[4]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'
make  check-TESTS
make[4]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'
pthread_default_stacksize_np failed.
/bin/sh[9]: 7458 Bus error(coredump)
FAIL: gctest
Leaked composite object at 400a0fd0 (tests/leak_test.c:19, sz=4, NORMAL)

PASS: leaktest
Final heap size is 262144
PASS: middletest
GC_check_heap_block: found smashed heap objects:
400a0ff8 in or near object at 400a0fd0(tests/smash_test.c:21, sz=40)
GC_check_heap_block: found smashed heap objects:
400fa4b8 in or near object at 400fa490(tests/smash_test.c:21, sz=40)
400a0ff8 in or near object at 400a0fd0(tests/smash_test.c:21, sz=40)
PASS: smashtest
GC Warning: Out of Memory!  Returning NIL!
GC Warning: Out of Memory!  Returning NIL!
GC Warning: Out of Memory!  Returning NIL!
PASS: hugetest
Leaked composite object at 400a2fe8 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at 400a2fd0 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at 400a2fe8 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at 400a2fd0 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at 400a2fe8 (tests/thread_leak_test.c:14, sz=4, NORMAL)

PASS: threadleaktest
==================================
1 of 6 tests failed
Please report to Hans.Boehm@hp.com
==================================
make[4]: *** [check-TESTS] Error 1
make[4]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'
make[3]: *** [check-am] Error 2
make[3]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'
make[2]: *** [check-recursive] Error 1
make[2]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'
An error occured while testing BoehmGC.
*************************************
Error testing package ** boehm_gc-7.1.p6 **
*************************************
sage: An error occurred while testing boehm_gc-7.1.p6
```



---

Comment by drkirkby created at 2010-09-13 12:11:13

Changing component from porting to AIX or HP-UX ports.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-04-27 17:56:32

Outdated, should be closed


---

Comment by mkoeppe created at 2020-04-27 17:56:32

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-04-27 19:36:22

Resolution: invalid
