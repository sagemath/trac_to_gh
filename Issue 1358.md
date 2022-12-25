# Issue 1358: update libtool's la files upon detection of a moved Sage install

archive/issues_001358.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following just happened to me on OSX 10.5.1:\n\n```\nMaking all in src\ng++ -DPACKAGE_NAME=\\\"libfplll\\\" -DPACKAGE_TARNAME=\\\"libfplll\\\" -DPACKAGE_VERSION=\\\"2.0.0\\\" -DPACKAGE_STRING=\\\"libfplll\\ 2.0.0\\\" -DPACKAGE_BUGREPORT=\\\"\\\" -DPACKAGE=\\\"\\\" -DVERSION=\\\"\\\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_LIBMPFR=1 -DHAVE_LIBGMP=1  -I. -I.    -I/Users/mabshoff/sage-2.8.14-moved/local/include/  -fPIC -I/Users/mabshoff/sage-2.8.14-moved/local/include/ -L/Users/mabshoff/sage-2.8.14-moved/local/lib -c main.cpp\n/bin/sh ../libtool --mode=link g++  -fPIC -I/Users/mabshoff/sage-2.8.14-moved/local/include/ -L/Users/mabshoff/sage-2.8.14-moved/local/lib  -o fplll  main.o  -lgmp -lmpfr\nmkdir .libs\nlibtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libgmp.la' was moved.\nlibtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libmpfr.la' was moved.\nlibtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libgmp.la' was moved.\nlibtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libmpfr.la' was moved.\nlibtool: link: cannot find the library `/Users/mabshoff/sage-2.8.14/local/lib/libgmp.la' or unhandled argument `/Users/mabshoff/sage-2.8.14/local/lib/libgmp.la'\nmake[3]: *** [fplll] Error 1\nmake[2]: *** [all-recursive] Error 1\nError building libfplll\n```\n\nThe fix is to correct the paths in the libtool files.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1358\n\n",
    "created_at": "2007-12-02T02:01:04Z",
    "labels": [
        "component: relocation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "update libtool's la files upon detection of a moved Sage install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1358",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The following just happened to me on OSX 10.5.1:

```
Making all in src
g++ -DPACKAGE_NAME=\"libfplll\" -DPACKAGE_TARNAME=\"libfplll\" -DPACKAGE_VERSION=\"2.0.0\" -DPACKAGE_STRING=\"libfplll\ 2.0.0\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"\" -DVERSION=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_LIBMPFR=1 -DHAVE_LIBGMP=1  -I. -I.    -I/Users/mabshoff/sage-2.8.14-moved/local/include/  -fPIC -I/Users/mabshoff/sage-2.8.14-moved/local/include/ -L/Users/mabshoff/sage-2.8.14-moved/local/lib -c main.cpp
/bin/sh ../libtool --mode=link g++  -fPIC -I/Users/mabshoff/sage-2.8.14-moved/local/include/ -L/Users/mabshoff/sage-2.8.14-moved/local/lib  -o fplll  main.o  -lgmp -lmpfr
mkdir .libs
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libgmp.la' was moved.
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libmpfr.la' was moved.
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libgmp.la' was moved.
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libmpfr.la' was moved.
libtool: link: cannot find the library `/Users/mabshoff/sage-2.8.14/local/lib/libgmp.la' or unhandled argument `/Users/mabshoff/sage-2.8.14/local/lib/libgmp.la'
make[3]: *** [fplll] Error 1
make[2]: *** [all-recursive] Error 1
Error building libfplll
```

The fix is to correct the paths in the libtool files.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1358





---

archive/issue_comments_008657.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-03T05:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008658.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-06-03T05:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_008659.json:
```json
{
    "body": "This is actually an issue that causes a lot of problems when updating an install that has been moved, i.e. installed directly or via some binary.",
    "created_at": "2008-06-03T05:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is actually an issue that causes a lot of problems when updating an install that has been moved, i.e. installed directly or via some binary.



---

archive/issue_comments_008660.json:
```json
{
    "body": "Changing assignee from mabshoff to wstein.",
    "created_at": "2008-06-03T05:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to wstein.



---

archive/issue_comments_008661.json:
```json
{
    "body": "This was fixed by William Stein a while back.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-03T05:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This was fixed by William Stein a while back.

Cheers,

Michael



---

archive/issue_comments_008662.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-06-03T05:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_008663.json:
```json
{
    "body": "Fixed prior to Sage 3.0.3.alpha1",
    "created_at": "2008-06-03T05:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8663",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed prior to Sage 3.0.3.alpha1



---

archive/issue_comments_008664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-03T05:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1358#issuecomment-8664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
