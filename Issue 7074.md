# Issue 7074: cvxopt-0.9.p8 sends GNU options to Sun Fortran compiler and has bad C code.

archive/issues_007074.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  dimpase\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha4\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used #7021 \n\n\n```\ncvxopt-0.9.p8/spkg-install\ncvxopt-0.9.p8/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nf95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\nf95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise\nUsage: f95 [ options ] files.  Use 'f95 -flags' for details\nUsing gfortran\nrunning install\nrunning build\nrunning build_py\ncreating build\ncreating build/lib.solaris-2.10-sun4u-2.6\ncreating build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/__init__.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/misc.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/cvxprog.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/modeling.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/info.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/coneprog.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\ncopying python/solvers.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt\nrunning build_ext\nbuilding 'base' extension\ncreating build/temp.solaris-2.10-sun4u-2.6\ncreating build/temp.solaris-2.10-sun4u-2.6/C\n/opt/xxxsunstudio12.1/bin/cc -DNDEBUG -O -xcode=pic32 -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.10-sun4u-2.6/C/base.o\n\"C/sun_complex.h\", line 30: invalid type combination\n\"C/sun_complex.h\", line 30: incomplete _Imaginary type specifier\n\"C/sun_complex.h\", line 30: warning: useless declaration\n\"C/sun_complex.h\", line 30: warning: typedef declares no type name\n\"C/misc.h\", line 29: incomplete _Complex type specifier\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7074\n\n",
    "created_at": "2009-09-29T13:51:32Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cvxopt-0.9.p8 sends GNU options to Sun Fortran compiler and has bad C code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7074",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  dimpase

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha4
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used #7021 


```
cvxopt-0.9.p8/spkg-install
cvxopt-0.9.p8/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
Using gfortran
running install
running build
running build_py
creating build
creating build/lib.solaris-2.10-sun4u-2.6
creating build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/__init__.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/misc.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/cvxprog.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/modeling.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/info.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/coneprog.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/solvers.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
running build_ext
building 'base' extension
creating build/temp.solaris-2.10-sun4u-2.6
creating build/temp.solaris-2.10-sun4u-2.6/C
/opt/xxxsunstudio12.1/bin/cc -DNDEBUG -O -xcode=pic32 -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.10-sun4u-2.6/C/base.o
"C/sun_complex.h", line 30: invalid type combination
"C/sun_complex.h", line 30: incomplete _Imaginary type specifier
"C/sun_complex.h", line 30: warning: useless declaration
"C/sun_complex.h", line 30: warning: typedef declares no type name
"C/misc.h", line 29: incomplete _Complex type specifier
```


Issue created by migration from https://trac.sagemath.org/ticket/7074





---

archive/issue_comments_058507.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7074#issuecomment-58507",
    "user": "mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_058508.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7074#issuecomment-58508",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058509.json:
```json
{
    "body": "The goal of these tickets is laudable, but:\n\n* We need at least one user who is able to test.\n* The package/OS information on this ticket is outdated beyond usefulness.\n* Upstream is a better place to report portability issues these days.",
    "created_at": "2020-07-12T20:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7074#issuecomment-58509",
    "user": "mjo"
}
```

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.



---

archive/issue_comments_058510.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-12T20:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7074#issuecomment-58510",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058511.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7074#issuecomment-58511",
    "user": "chapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.



---

archive/issue_comments_058512.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7074#issuecomment-58512",
    "user": "chapoton"
}
```

Resolution: invalid
