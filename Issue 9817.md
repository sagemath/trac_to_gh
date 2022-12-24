# Issue 9817: boehm_gc installs OK on HP-UX, but fails one of 6 tests if SAGE_CHECK=yes

archive/issues_009817.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  dimpase\n\n## Hardware/Software\n* HP C3600 workstation\n* 1 x 552 MHz PA-RISC CPU\n* 8 GB RAM\n* HP-UX 11.11B\n* Sage 4.5.3.alpha2\n* boehm_gc-7.1.p6 (that's boehm_gc-7.1 patched 7 times in Sage)\n\n == The failure ==\n\n\n```\n\tif gcc -DPACKAGE_NAME=\\\"gc\\\" -DPACKAGE_TARNAME=\\\"gc\\\" -DPACKAGE_VERSION=\\\"7.1\\\" -DPACKAGE_STRING=\\\"gc\\ 7.1\\\" -DPACKAGE_BUGREPORT=\\\"Hans.Boehm@hp.com\\\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\\\"gc\\\" -DVERSION=\\\"7.1\\\" -DGC_HPUX_THREADS=1 -D_POSIX_C_SOURCE=199506L -DTHREAD_LOCAL_ALLOC=1 -D_REENTRANT=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1  -I./include   -fexceptions -I libatomic_ops/src -g -O2 -MT tests/smash_test.o -MD -MP -MF \"$depbase.Tpo\" -c -o tests/smash_test.o tests/smash_test.c; \\\n\tthen mv -f \"$depbase.Tpo\" \"$depbase.Po\"; else rm -f \"$depbase.Tpo\"; exit 1; fi\n/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o smashtest  tests/smash_test.o ./libgc.la  \nlibtool: link: warning: this platform does not like uninstalled shared libraries\nlibtool: link: `smashtest' will be relinked during installation\ngcc -fexceptions -I libatomic_ops/src -g -O2 -o .libs/smashtest tests/smash_test.o  ./.libs/libgc.sl -lpthread -lrt -Wl,+b -Wl,/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src/.libs:/home/drkirkby/sage-4.5.3.alpha2/local/lib\ncreating smashtest\ndepbase=`echo tests/huge_test.o | sed 's|[^/]*$|.deps/&|;s|\\.o$||'`; \\\n\tif gcc -DPACKAGE_NAME=\\\"gc\\\" -DPACKAGE_TARNAME=\\\"gc\\\" -DPACKAGE_VERSION=\\\"7.1\\\" -DPACKAGE_STRING=\\\"gc\\ 7.1\\\" -DPACKAGE_BUGREPORT=\\\"Hans.Boehm@hp.com\\\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\\\"gc\\\" -DVERSION=\\\"7.1\\\" -DGC_HPUX_THREADS=1 -D_POSIX_C_SOURCE=199506L -DTHREAD_LOCAL_ALLOC=1 -D_REENTRANT=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1  -I./include   -fexceptions -I libatomic_ops/src -g -O2 -MT tests/huge_test.o -MD -MP -MF \"$depbase.Tpo\" -c -o tests/huge_test.o tests/huge_test.c; \\\n\tthen mv -f \"$depbase.Tpo\" \"$depbase.Po\"; else rm -f \"$depbase.Tpo\"; exit 1; fi\n/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o hugetest  tests/huge_test.o ./libgc.la  \nlibtool: link: warning: this platform does not like uninstalled shared libraries\nlibtool: link: `hugetest' will be relinked during installation\ngcc -fexceptions -I libatomic_ops/src -g -O2 -o .libs/hugetest tests/huge_test.o  ./.libs/libgc.sl -lpthread -lrt -Wl,+b -Wl,/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src/.libs:/home/drkirkby/sage-4.5.3.alpha2/local/lib\ncreating hugetest\ndepbase=`echo tests/thread_leak_test.o | sed 's|[^/]*$|.deps/&|;s|\\.o$||'`; \\\n\tif gcc -DPACKAGE_NAME=\\\"gc\\\" -DPACKAGE_TARNAME=\\\"gc\\\" -DPACKAGE_VERSION=\\\"7.1\\\" -DPACKAGE_STRING=\\\"gc\\ 7.1\\\" -DPACKAGE_BUGREPORT=\\\"Hans.Boehm@hp.com\\\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\\\"gc\\\" -DVERSION=\\\"7.1\\\" -DGC_HPUX_THREADS=1 -D_POSIX_C_SOURCE=199506L -DTHREAD_LOCAL_ALLOC=1 -D_REENTRANT=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PERMISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DLARGE_CONFIG=1  -I./include   -fexceptions -I libatomic_ops/src -g -O2 -MT tests/thread_leak_test.o -MD -MP -MF \"$depbase.Tpo\" -c -o tests/thread_leak_test.o tests/thread_leak_test.c; \\\n\tthen mv -f \"$depbase.Tpo\" \"$depbase.Po\"; else rm -f \"$depbase.Tpo\"; exit 1; fi\n/bin/sh ./libtool --tag=CC --mode=link gcc -fexceptions -I libatomic_ops/src -g -O2   -o threadleaktest  tests/thread_leak_test.o ./libgc.la  \nlibtool: link: warning: this platform does not like uninstalled shared libraries\nlibtool: link: `threadleaktest' will be relinked during installation\ngcc -fexceptions -I libatomic_ops/src -g -O2 -o .libs/threadleaktest tests/thread_leak_test.o  ./.libs/libgc.sl -lpthread -lrt -Wl,+b -Wl,/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src/.libs:/home/drkirkby/sage-4.5.3.alpha2/local/lib\ncreating threadleaktest\nmake[4]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'\nmake  check-TESTS\nmake[4]: Entering directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'\npthread_default_stacksize_np failed.\n/bin/sh[9]: 7458 Bus error(coredump)\nFAIL: gctest\nLeaked composite object at 400a0fd0 (tests/leak_test.c:19, sz=4, NORMAL)\n\nPASS: leaktest\nFinal heap size is 262144\nPASS: middletest\nGC_check_heap_block: found smashed heap objects:\n400a0ff8 in or near object at 400a0fd0(tests/smash_test.c:21, sz=40)\nGC_check_heap_block: found smashed heap objects:\n400fa4b8 in or near object at 400fa490(tests/smash_test.c:21, sz=40)\n400a0ff8 in or near object at 400a0fd0(tests/smash_test.c:21, sz=40)\nPASS: smashtest\nGC Warning: Out of Memory!  Returning NIL!\nGC Warning: Out of Memory!  Returning NIL!\nGC Warning: Out of Memory!  Returning NIL!\nPASS: hugetest\nLeaked composite object at 400a2fe8 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at 400a2fd0 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at 400a2fe8 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at 400a2fd0 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at 400a2fe8 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nPASS: threadleaktest\n==================================\n1 of 6 tests failed\nPlease report to Hans.Boehm@hp.com\n==================================\nmake[4]: *** [check-TESTS] Error 1\nmake[4]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'\nmake[3]: *** [check-am] Error 2\nmake[3]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'\nmake[2]: *** [check-recursive] Error 1\nmake[2]: Leaving directory `/home/drkirkby/sage-4.5.3.alpha2/spkg/build/boehm_gc-7.1.p6/src'\nAn error occured while testing BoehmGC.\n*************************************\nError testing package ** boehm_gc-7.1.p6 **\n*************************************\nsage: An error occurred while testing boehm_gc-7.1.p6\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9818\n\n",
    "created_at": "2010-08-27T10:06:51Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "boehm_gc installs OK on HP-UX, but fails one of 6 tests if SAGE_CHECK=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9817",
    "user": "drkirkby"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/9818





---

archive/issue_comments_096811.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2010-09-13T12:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9817#issuecomment-96811",
    "user": "drkirkby"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_comments_096812.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9817#issuecomment-96812",
    "user": "embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_096813.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-04-27T17:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9817#issuecomment-96813",
    "user": "mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_096814.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-27T17:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9817#issuecomment-96814",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096815.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-27T19:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9817#issuecomment-96815",
    "user": "chapoton"
}
```

Resolution: invalid
