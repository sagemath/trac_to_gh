# Issue 8843: fix c_lib on Cygwin

archive/issues_008843.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wstein\n\nCygwin can't load shared libraries via symlinks.  Therefore, we have to actually copy libcsage.so/csage.dll over to $SAGE_LOCAL/lib/.  Note that currently the \"install\" target in SConstruct does nothing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8843\n\n",
    "created_at": "2010-05-03T04:50:09Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "fix c_lib on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8843",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  wstein

Cygwin can't load shared libraries via symlinks.  Therefore, we have to actually copy libcsage.so/csage.dll over to $SAGE_LOCAL/lib/.  Note that currently the "install" target in SConstruct does nothing.

Issue created by migration from https://trac.sagemath.org/ticket/8843





---

archive/issue_comments_081159.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T13:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81159",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081160.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-25T06:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81160",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081161.json:
```json
{
    "body": "Unfortunately, after applying this, libcsage just doesn't build anymore.",
    "created_at": "2010-05-25T06:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81161",
    "user": "https://github.com/williamstein"
}
```

Unfortunately, after applying this, libcsage just doesn't build anymore.



---

archive/issue_comments_081162.json:
```json
{
    "body": "Attachment [trac_8843-c_lib.patch](tarball://root/attachments/some-uuid/ticket8843/trac_8843-c_lib.patch) by @mwhansen created at 2010-05-25 18:21:15",
    "created_at": "2010-05-25T18:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81162",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8843-c_lib.patch](tarball://root/attachments/some-uuid/ticket8843/trac_8843-c_lib.patch) by @mwhansen created at 2010-05-25 18:21:15



---

archive/issue_comments_081163.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T18:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81163",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081164.json:
```json
{
    "body": "I've posted a new patch which should work.",
    "created_at": "2010-05-25T18:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81164",
    "user": "https://github.com/mwhansen"
}
```

I've posted a new patch which should work.



---

archive/issue_comments_081165.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-26T00:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81165",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081166.json:
```json
{
    "body": "Doesn't work:\n\n\n```\nInstalling c_lib\ng++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib -L/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/python/config -lntl -lgmp -lpari -lpython2.6\n/usr/bin/ld: /mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/libpython2.6.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not be used when making a shared object; recompile with -fPIC\n/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/libpython2.6.a: could not read symbols: Bad value\ncollect2: ld returned 1 exit status\nscons: *** [libcsage.so] Error 1\nERROR: There was an error building c_lib.\n```\n\n\nHowever, Mike says there is a Python spkg that may fix this...",
    "created_at": "2010-05-26T00:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81166",
    "user": "https://github.com/williamstein"
}
```

Doesn't work:


```
Installing c_lib
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib -L/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
/usr/bin/ld: /mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/libpython2.6.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not be used when making a shared object; recompile with -fPIC
/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha0/local/lib/libpython2.6.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
scons: *** [libcsage.so] Error 1
ERROR: There was an error building c_lib.
```


However, Mike says there is a Python spkg that may fix this...



---

archive/issue_comments_081167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T01:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8843#issuecomment-81167",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_009008.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-26T01:00:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8843",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8843#event-9008"
}
```
