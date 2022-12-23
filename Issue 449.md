# Issue 449: lrank Solaris build fixes

archive/issues_000449.json:
```json
{
    "body": "Assignee: mabshoff\n\n* spkg-install: needs sh compability fix: DEFINES=\"\"; export DEFINES\n* llrint workaround needed for SunOS:\n  #define llrint(d) ((long long)rint(d))\n* ./include/getopt.h: line 147: do not define \"extern int getopt ();\"\non Solaris\n* needs -liberty for symbol getopt_long when __sun is defined\n\nIn general: The Makefile sucks:\n\ng++  -DINCLUDE_PARI   \\\n      -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include/pari \\\n      -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include \\\n      -I ../include/ -L/extra/home/mabshoff/SAGE-build/sage-2.8/local/\nlib \\\n      cmdline.c \\\n      Lcommandline.cc Lcommandline_elliptic.cc Lcommandline_globals.cc\n\\\n      Lcommandline_misc.cc Lcommandline_numbertheory.cc \\\n      Lcommandline_twist.cc Lcommandline_values_zeros.cc \\\n      Lgamma.cc Lglobals.cc Lmisc.cc Lriemannsiegel.cc \\\n            -o lcalc -lpari -lmpfr -lgmpxx -lgmp -liberty\n\nCleanup:\n* compile each file individually\n* crush gcc 4.2 warnings about const string to char*\n\nIssue created by migration from https://trac.sagemath.org/ticket/449\n\n",
    "created_at": "2007-08-19T07:49:45Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "lrank Solaris build fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/449",
    "user": "mabshoff"
}
```
Assignee: mabshoff

* spkg-install: needs sh compability fix: DEFINES=""; export DEFINES
* llrint workaround needed for SunOS:
  #define llrint(d) ((long long)rint(d))
* ./include/getopt.h: line 147: do not define "extern int getopt ();"
on Solaris
* needs -liberty for symbol getopt_long when __sun is defined

In general: The Makefile sucks:

g++  -DINCLUDE_PARI   \
      -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include/pari \
      -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include \
      -I ../include/ -L/extra/home/mabshoff/SAGE-build/sage-2.8/local/
lib \
      cmdline.c \
      Lcommandline.cc Lcommandline_elliptic.cc Lcommandline_globals.cc
\
      Lcommandline_misc.cc Lcommandline_numbertheory.cc \
      Lcommandline_twist.cc Lcommandline_values_zeros.cc \
      Lgamma.cc Lglobals.cc Lmisc.cc Lriemannsiegel.cc \
            -o lcalc -lpari -lmpfr -lgmpxx -lgmp -liberty

Cleanup:
* compile each file individually
* crush gcc 4.2 warnings about const string to char*

Issue created by migration from https://trac.sagemath.org/ticket/449





---

archive/issue_comments_002239.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/449#issuecomment-2239",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002240.json:
```json
{
    "body": "See also #932 and #1626.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T17:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/449#issuecomment-2240",
    "user": "mabshoff"
}
```

See also #932 and #1626.

Cheers,

Michael



---

archive/issue_comments_002241.json:
```json
{
    "body": "There are now patches at #1626 which fix the issue. This ticket can be closed once #1626 is merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T00:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/449#issuecomment-2241",
    "user": "mabshoff"
}
```

There are now patches at #1626 which fix the issue. This ticket can be closed once #1626 is merged.

Cheers,

Michael



---

archive/issue_comments_002242.json:
```json
{
    "body": "Fixed since #1626 has been merged in Sage 3.0.alpha5.",
    "created_at": "2008-04-14T03:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/449#issuecomment-2242",
    "user": "mabshoff"
}
```

Fixed since #1626 has been merged in Sage 3.0.alpha5.



---

archive/issue_comments_002243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T03:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/449#issuecomment-2243",
    "user": "mabshoff"
}
```

Resolution: fixed
