# Issue 7006: [with patch; needs review] os x 10.6 port -- update mpir to autodetect ABI on OS X since ABI=32 is *no* longer necessarily the default on 10.6

archive/issues_007006.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  palmieri mvngu\n\nThe spkg is up here:\n\n  http://sage.math.washington.edu/home/wstein/patches/mpir-1.2.p5.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/7006\n\n",
    "created_at": "2009-09-25T00:54:56Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch; needs review] os x 10.6 port -- update mpir to autodetect ABI on OS X since ABI=32 is *no* longer necessarily the default on 10.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7006",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  palmieri mvngu

The spkg is up here:

  http://sage.math.washington.edu/home/wstein/patches/mpir-1.2.p5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/7006





---

archive/issue_comments_057831.json:
```json
{
    "body": "This doesn't seem to build properly on OS X 10.5, 32-bit.  (As far as I can tell, it works with 10.5 64-bit and also with 10.6).  The problem occurs when starting to build ntl:\n\n```\nmv mach_desc.h ../include/NTL/mach_desc.h\nsh MakeGetTime \"gcc -I../include -I.  -O2 -g  -fno-common \" \"-lm\"\ndoes anybody really know what time it is?\ngcc -I../include -I. -O2 -g -fno-common -o TestGetTime TestGetTime.c GetTime1.c -lm\nrunning\nusing GetTime1.c\ngcc -I../include -I.  -O2 -g  -fno-common   -I/Applications/sage_builds/sage-4.1.2.alpha2/local/include -o gen_lip_gmp_aux gen_lip_gmp_aux.c -L/Applications/sage_builds/sage-4.1.2.alpha2/local/lib -lgmp -lm\nld warning: in /Applications/sage_builds/sage-4.1.2.alpha2/local/lib/libgmp.dylib, file is not of required architecture\n./gen_lip_gmp_aux > lip_gmp_aux_impl.h\nNTL_GMP_HACK flag not set.\ngcc -I../include -I.  -O2 -g  -fno-common   -I/Applications/sage_builds/sage-4.1.2.alpha2/local/include -o gen_gmp_aux gen_gmp_aux.c -L/Applications/sage_builds/sage-4.1.2.alpha2/local/lib -lgmp -lm\nld warning: in /Applications/sage_builds/sage-4.1.2.alpha2/local/lib/libgmp.dylib, file is not of required architecture\nUndefined symbols:\n  \"___gmp_bits_per_limb\", referenced from:\n      ___gmp_bits_per_limb$non_lazy_ptr in ccWvp3La.o\nld: symbol(s) not found\ncollect2: ld returned 1 exit status\nmake[2]: *** [setup3] Error 1\nFailed building setup3 of NTL\n```\n\nIf I install the old version of mpir using './sage -f mpir-1.2.p4.spkg', then ntl builds correctly.",
    "created_at": "2009-09-25T21:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7006#issuecomment-57831",
    "user": "https://github.com/jhpalmieri"
}
```

This doesn't seem to build properly on OS X 10.5, 32-bit.  (As far as I can tell, it works with 10.5 64-bit and also with 10.6).  The problem occurs when starting to build ntl:

```
mv mach_desc.h ../include/NTL/mach_desc.h
sh MakeGetTime "gcc -I../include -I.  -O2 -g  -fno-common " "-lm"
does anybody really know what time it is?
gcc -I../include -I. -O2 -g -fno-common -o TestGetTime TestGetTime.c GetTime1.c -lm
running
using GetTime1.c
gcc -I../include -I.  -O2 -g  -fno-common   -I/Applications/sage_builds/sage-4.1.2.alpha2/local/include -o gen_lip_gmp_aux gen_lip_gmp_aux.c -L/Applications/sage_builds/sage-4.1.2.alpha2/local/lib -lgmp -lm
ld warning: in /Applications/sage_builds/sage-4.1.2.alpha2/local/lib/libgmp.dylib, file is not of required architecture
./gen_lip_gmp_aux > lip_gmp_aux_impl.h
NTL_GMP_HACK flag not set.
gcc -I../include -I.  -O2 -g  -fno-common   -I/Applications/sage_builds/sage-4.1.2.alpha2/local/include -o gen_gmp_aux gen_gmp_aux.c -L/Applications/sage_builds/sage-4.1.2.alpha2/local/lib -lgmp -lm
ld warning: in /Applications/sage_builds/sage-4.1.2.alpha2/local/lib/libgmp.dylib, file is not of required architecture
Undefined symbols:
  "___gmp_bits_per_limb", referenced from:
      ___gmp_bits_per_limb$non_lazy_ptr in ccWvp3La.o
ld: symbol(s) not found
collect2: ld returned 1 exit status
make[2]: *** [setup3] Error 1
Failed building setup3 of NTL
```

If I install the old version of mpir using './sage -f mpir-1.2.p4.spkg', then ntl builds correctly.



---

archive/issue_comments_057832.json:
```json
{
    "body": "New version here that should behave as before on all older os x's:\n\n  http://sage.math.washington.edu/home/wstein/patches/mpir-1.2.p6.spkg",
    "created_at": "2009-09-25T21:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7006#issuecomment-57832",
    "user": "https://github.com/williamstein"
}
```

New version here that should behave as before on all older os x's:

  http://sage.math.washington.edu/home/wstein/patches/mpir-1.2.p6.spkg



---

archive/issue_comments_057833.json:
```json
{
    "body": "New MPIR package up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/mpir-1.2.p7.spkg\n\nThe only change from .p6 is:\n\n* Remove the junk file `spkg-install~`.",
    "created_at": "2009-09-27T01:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7006#issuecomment-57833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

New MPIR package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/mpir-1.2.p7.spkg

The only change from .p6 is:

* Remove the junk file `spkg-install~`.



---

archive/issue_events_016436.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-27T02:28:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7006",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7006#event-16436"
}
```



---

archive/issue_comments_057834.json:
```json
{
    "body": "See palmieri's and my reports at #6849.",
    "created_at": "2009-09-27T02:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7006#issuecomment-57834",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See palmieri's and my reports at #6849.



---

archive/issue_comments_057835.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-27T02:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7006#issuecomment-57835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
