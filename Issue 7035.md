# Issue 7035: R sends the correct Sun flags to C and C++ compilers, but not Fortran.

archive/issues_007035.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: solaris gfortran\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 \n\nCC was set to the Sun C compiler, and CXX to the Sun C++ compiler and SAGE_FORTRAN to the Sun Fortran 95 compiler. While R sends the correct flags (-KPIC) to make position independent code to the Sun C and C++ compilers, it does not do so with the Fortran compiler. Instead it used the GNU flag -fPIC. R is however picking up the correct Fortran compiler (f95 and not gfortran)\n\n\n```\n/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c tabulate.c -o tabulate.o\n/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c uncmin.c -o uncmin.o/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c zeroin.c -o zeroin.osage_fortran  -PIC  -g -c ch2inv.f -o ch2inv.o\nf95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\nsage_fortran  -PIC  -g -c chol.f -o chol.o\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7035\n\n",
    "created_at": "2009-09-27T15:16:37Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "R sends the correct Sun flags to C and C++ compilers, but not Fortran.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7035",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Keywords: solaris gfortran

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler and SAGE_FORTRAN to the Sun Fortran 95 compiler. While R sends the correct flags (-KPIC) to make position independent code to the Sun C and C++ compilers, it does not do so with the Fortran compiler. Instead it used the GNU flag -fPIC. R is however picking up the correct Fortran compiler (f95 and not gfortran)


```
/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c tabulate.c -o tabulate.o
/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c uncmin.c -o uncmin.o/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c zeroin.c -o zeroin.osage_fortran  -PIC  -g -c ch2inv.f -o ch2inv.o
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
sage_fortran  -PIC  -g -c chol.f -o chol.o
```


Issue created by migration from https://trac.sagemath.org/ticket/7035





---

archive/issue_comments_058143.json:
```json
{
    "body": "Changing component from build to packages: standard.",
    "created_at": "2015-09-08T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7035#issuecomment-58143",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to packages: standard.



---

archive/issue_events_016547.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-08-26T19:09:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7035#event-16547"
}
```



---

archive/issue_comments_058144.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-08-26T19:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7035#issuecomment-58144",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058145.json:
```json
{
    "body": "Outdated, should close",
    "created_at": "2021-08-26T19:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7035#issuecomment-58145",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should close



---

archive/issue_comments_058146.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-04T22:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7035#issuecomment-58146",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016548.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-04T23:44:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7035#event-16548"
}
```



---

archive/issue_comments_058147.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-04T23:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7035#issuecomment-58147",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
