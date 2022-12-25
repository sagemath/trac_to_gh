# Issue 1981: NTL fails to build with DEB_BUILD_HARDENING=1

archive/issues_001981.json:
```json
{
    "body": "Assignee: mabshoff\n\nError message:\n\n```\nld.real: FFT.o: relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC\nFFT.o: could not read symbols: Bad value\ncollect2: ld returned 1 exit status\nmake[3]: *** [libntl.so] Error 1\nmake[3]: Leaving directory `/tmp/sage-2.10.1.rc2-hardening-wrapper/spkg/build/ntl-5.4.1.p10/src/src'\nmake[2]: *** [lib] Error 2\nmake[2]: Leaving directory `/tmp/sage-2.10.1.rc2-hardening-wrapper/spkg/build/ntl-5.4.1.p10/src/src'\nError creating ntl shared library.\n```\n\nHow to reproduce (Debian only!):\n\n```\napt-get install hardening-wrapper\nexport DEB_BUILD_HARDENING=1\ncd <SAGE_ROOT>\nmake\n```\n\nSee http://wiki.debian.org/Hardening and http://lists.debian.org/debian-devel-announce/2008/01/msg00006.html for rationale of hardening. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1981\n\n",
    "created_at": "2008-01-30T10:34:24Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "NTL fails to build with DEB_BUILD_HARDENING=1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1981",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff

Error message:

```
ld.real: FFT.o: relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
FFT.o: could not read symbols: Bad value
collect2: ld returned 1 exit status
make[3]: *** [libntl.so] Error 1
make[3]: Leaving directory `/tmp/sage-2.10.1.rc2-hardening-wrapper/spkg/build/ntl-5.4.1.p10/src/src'
make[2]: *** [lib] Error 2
make[2]: Leaving directory `/tmp/sage-2.10.1.rc2-hardening-wrapper/spkg/build/ntl-5.4.1.p10/src/src'
Error creating ntl shared library.
```

How to reproduce (Debian only!):

```
apt-get install hardening-wrapper
export DEB_BUILD_HARDENING=1
cd <SAGE_ROOT>
make
```

See http://wiki.debian.org/Hardening and http://lists.debian.org/debian-devel-announce/2008/01/msg00006.html for rationale of hardening. 


Issue created by migration from https://trac.sagemath.org/ticket/1981





---

archive/issue_comments_012809.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-13T12:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1981#issuecomment-12809",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012810.json:
```json
{
    "body": "Very outdated.",
    "created_at": "2013-06-13T12:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1981#issuecomment-12810",
    "user": "https://github.com/jdemeyer"
}
```

Very outdated.



---

archive/issue_events_004784.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-13T12:33:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1981",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1981#event-4784"
}
```



---

archive/issue_comments_012811.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-13T12:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1981#issuecomment-12811",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012812.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-06-19T12:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1981#issuecomment-12812",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_004785.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-19T12:21:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1981",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1981#event-4785"
}
```
