# Issue 3248: [with patch; needs review] cygwin -- fix some sagelib setup.py issues and Sconstruct issues involving library includes

archive/issues_003248.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @craigcitro\n\n1. Something involving the python library in SConstruct that affect c_lib\n\n2. Something library ordering issues that break matrix_real_double_dense in setup.py\n\n3. Choosing ATLAS instead of GSL by default in setup.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/3248\n\n",
    "created_at": "2008-05-17T20:55:36Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch; needs review] cygwin -- fix some sagelib setup.py issues and Sconstruct issues involving library includes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3248",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @craigcitro

1. Something involving the python library in SConstruct that affect c_lib

2. Something library ordering issues that break matrix_real_double_dense in setup.py

3. Choosing ATLAS instead of GSL by default in setup.py

Issue created by migration from https://trac.sagemath.org/ticket/3248





---

archive/issue_comments_022430.json:
```json
{
    "body": "Attachment [sage-3248.patch](tarball://root/attachments/some-uuid/ticket3248/sage-3248.patch) by @williamstein created at 2008-05-17 20:56:29",
    "created_at": "2008-05-17T20:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3248#issuecomment-22430",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3248.patch](tarball://root/attachments/some-uuid/ticket3248/sage-3248.patch) by @williamstein created at 2008-05-17 20:56:29



---

archive/issue_comments_022431.json:
```json
{
    "body": "This patch as is exposes some bugs in the way we build python:\n\n```\ng++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os \nsrc/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os \n-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib \n-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config -lntl \n-lgmp -lpari -lpython2.5\n/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config\n/libpython2.5.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not \nbe used when making a shared object; recompile with -fPIC\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config/libpython2.5.a: \ncould not read symbols: Bad value\ncollect2: ld returned 1 exit status\nscons: *** [libcsage.so] Error 1\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\n\nInstalling c_lib\ng++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os \nsrc/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os \n-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib \n-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config -lntl \n-lgmp -lpari -lpython2.5\n/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config\n/libpython2.5.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not \nbe used when making a shared object; recompile with -fPIC\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config/libpython2.5.a: \ncould not read symbols: Bad value\ncollect2: ld returned 1 exit status\nscons: *** [libcsage.so] Error 1\nERROR: There was an error building c_lib.\n```\n\nThe likely solution is to force \"-fPIC\" on the python build, but I need to dig around.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-17T21:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3248#issuecomment-22431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch as is exposes some bugs in the way we build python:

```
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os 
src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config -lntl 
-lgmp -lpari -lpython2.5
/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config
/libpython2.5.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not 
be used when making a shared object; recompile with -fPIC
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config/libpython2.5.a: 
could not read symbols: Bad value
collect2: ld returned 1 exit status
scons: *** [libcsage.so] Error 1

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os 
src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib 
-L/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config -lntl 
-lgmp -lpari -lpython2.5
/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config
/libpython2.5.a(exceptions.o): relocation R_X86_64_32 against `_Py_NoneStruct' can not 
be used when making a shared object; recompile with -fPIC
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha1/local/lib/python/config/libpython2.5.a: 
could not read symbols: Bad value
collect2: ld returned 1 exit status
scons: *** [libcsage.so] Error 1
ERROR: There was an error building c_lib.
```

The likely solution is to force "-fPIC" on the python build, but I need to dig around.

Cheers,

Michael



---

archive/issue_comments_022432.json:
```json
{
    "body": "We need to track this down and fix it.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T17:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3248#issuecomment-22432",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We need to track this down and fix it.

Cheers,

Michael



---

archive/issue_comments_022433.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-20T04:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3248#issuecomment-22433",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_events_003467.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-01-17T12:03:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3248#event-3467"
}
```



---

archive/issue_comments_022434.json:
```json
{
    "body": "This is nearly 2 years old.  My work with Mike Hansen on Windows porting greatly supersedes this.  So I'm closing this.",
    "created_at": "2010-01-17T12:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3248#issuecomment-22434",
    "user": "https://github.com/williamstein"
}
```

This is nearly 2 years old.  My work with Mike Hansen on Windows porting greatly supersedes this.  So I'm closing this.



---

archive/issue_comments_022435.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-17T12:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3248#issuecomment-22435",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate
