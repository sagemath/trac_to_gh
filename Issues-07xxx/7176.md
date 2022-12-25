# Issue 7176: sage-4.1.2.rc0 scripts should exit as soon as it can't find gmp.h

archive/issues_007176.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.ne\n\nKeywords: HP-UX gmp\n\nMPIR failed to build on an HP machine. Despite the fact the code can't open gmp.h, it does not exit, but the touches other files\n\n```\n\nDeleting directories from past builds of previous/current versions of sage-4.1.2.rc0\nExtracting package /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sage-4.1.2.rc0.spkg ...\n-rw-r--r--   1 drkirkby   users      41860926 Oct  1 04:40 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sage-4.1.2.rc0.spkg\n\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa1.1-hp-hpux11.11\nConfigured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11\nThread model: posix\ngcc version 4.4.0 (GCC)\n****************************************************\nmv: /home/drkirkby/sage-4.1.2.rc0/devel/sage-main: cannot access: No such file or directory\ncc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c\ncpp: \"include/convert.h\", line 11: error 4036: Can't open include file 'gmp.h'.\ncpp: \"include/convert.h\", line 12: error 4036: Can't open include file 'pari/pari.h'.\nscons: *** [src/convert.os] Error 1\n\n*** TOUCHING ALL CYTHON (.pyx) FILES ***\ncc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c\ncpp: \"include/convert.h\", line 11: error 4036: Can't open include file 'gmp.h'.\ncpp: \"include/convert.h\", line 12: error 4036: Can't open include file 'pari/pari.h'.\nscons: *** [src/convert.os] Error 1\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\ncc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c\ncpp: \"include/convert.h\", line 11: error 4036: Can't open include file 'gmp.h'.\ncpp: \"include/convert.h\", line 12: error 4036: Can't open include file 'pari/pari.h'.\nscons: *** [src/convert.os] Error 1\nERROR: There was an error building c_lib.\n\nERROR installing SAGE\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7176\n\n",
    "closed_at": "2014-02-06T20:50:26Z",
    "created_at": "2009-10-10T08:30:02Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-4.1.2.rc0 scripts should exit as soon as it can't find gmp.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7176",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.ne

Keywords: HP-UX gmp

MPIR failed to build on an HP machine. Despite the fact the code can't open gmp.h, it does not exit, but the touches other files

```

Deleting directories from past builds of previous/current versions of sage-4.1.2.rc0
Extracting package /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sage-4.1.2.rc0.spkg ...
-rw-r--r--   1 drkirkby   users      41860926 Oct  1 04:40 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sage-4.1.2.rc0.spkg

Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.4.0 (GCC)
****************************************************
mv: /home/drkirkby/sage-4.1.2.rc0/devel/sage-main: cannot access: No such file or directory
cc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c
cpp: "include/convert.h", line 11: error 4036: Can't open include file 'gmp.h'.
cpp: "include/convert.h", line 12: error 4036: Can't open include file 'pari/pari.h'.
scons: *** [src/convert.os] Error 1

*** TOUCHING ALL CYTHON (.pyx) FILES ***
cc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c
cpp: "include/convert.h", line 11: error 4036: Can't open include file 'gmp.h'.
cpp: "include/convert.h", line 12: error 4036: Can't open include file 'pari/pari.h'.
scons: *** [src/convert.os] Error 1

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
cc -o src/convert.os -c +Z -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -I/home/drkirkby/sage-4.1.2.rc0/local/include/NTL -Iinclude src/convert.c
cpp: "include/convert.h", line 11: error 4036: Can't open include file 'gmp.h'.
cpp: "include/convert.h", line 12: error 4036: Can't open include file 'pari/pari.h'.
scons: *** [src/convert.os] Error 1
ERROR: There was an error building c_lib.

ERROR installing SAGE

```


Issue created by migration from https://trac.sagemath.org/ticket/7176





---

archive/issue_comments_059339.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-05T13:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7176#issuecomment-59339",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_016972.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-02-05T13:00:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7176",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7176#event-16972"
}
```



---

archive/issue_comments_059340.json:
```json
{
    "body": "Way outdated.",
    "created_at": "2014-02-05T13:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7176#issuecomment-59340",
    "user": "https://github.com/jdemeyer"
}
```

Way outdated.



---

archive/issue_comments_059341.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-05T13:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7176#issuecomment-59341",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016973.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-06T20:50:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7176",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7176#event-16973"
}
```



---

archive/issue_comments_059342.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-02-06T20:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7176#issuecomment-59342",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
