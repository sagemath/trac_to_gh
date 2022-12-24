# Issue 9816: blas uses non-POSIX option -p to uname. This causes problems on HP-UX.

archive/issues_009816.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  pjeremy leif\n\nThe POSIX standard for Unix states the command `uname` must exist, and list the options it should take. See\n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html\n\nThe **only** options which should be given in code that can be run on any system is these:\n\n\n\n```\n    uname [-amnrsv]\n```\n\n\nbut the BLAS package ignores this, and calls `uname -p`, which screws up on systems like HP-UX where the -p option is not supported. \n\n\n```\nblas-20070724/src/ztrsm.f\nblas-20070724/src/ztrsv.f\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa2.0w-hp-hpux11.11\nConfigured with: ../gcc-4.3.4/configure --with-gnu-as --with-as=/home/dclarke/local/bin/as --without-gnu-ld --with-ld=/usr/bin/ld --enable-threads=posix --enable-nls --prefix=/home/dclarke/local --enable-shared --enable-multilib --with-included-gettext --with-libiconv-prefix=/home/dclarke/local --with-system-zlib --with-gmp=/home/dclarke/local --with-mpfr=/home/dclarke/local --enable-languages=c,c++,fortran,objc --enable-bootstrap\nThread model: posix\ngcc version 4.3.4 (GCC) \n****************************************************\nuname: illegal option -- p\nusage: uname [-amnrsvil] [-S nodename]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9817\n\n",
    "created_at": "2010-08-27T09:52:35Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "blas uses non-POSIX option -p to uname. This causes problems on HP-UX.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9816",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  pjeremy leif

The POSIX standard for Unix states the command `uname` must exist, and list the options it should take. See

http://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html

The **only** options which should be given in code that can be run on any system is these:



```
    uname [-amnrsv]
```


but the BLAS package ignores this, and calls `uname -p`, which screws up on systems like HP-UX where the -p option is not supported. 


```
blas-20070724/src/ztrsm.f
blas-20070724/src/ztrsv.f
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
Target: hppa2.0w-hp-hpux11.11
Configured with: ../gcc-4.3.4/configure --with-gnu-as --with-as=/home/dclarke/local/bin/as --without-gnu-ld --with-ld=/usr/bin/ld --enable-threads=posix --enable-nls --prefix=/home/dclarke/local --enable-shared --enable-multilib --with-included-gettext --with-libiconv-prefix=/home/dclarke/local --with-system-zlib --with-gmp=/home/dclarke/local --with-mpfr=/home/dclarke/local --enable-languages=c,c++,fortran,objc --enable-bootstrap
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
uname: illegal option -- p
usage: uname [-amnrsvil] [-S nodename]

```


Issue created by migration from https://trac.sagemath.org/ticket/9817





---

archive/issue_comments_096804.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2010-09-13T12:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96804",
    "user": "drkirkby"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_comments_096805.json:
```json
{
    "body": "On seconds thoughts, this is a portability issue in general, not one specific to HP-UX. So changing the component back. \n\nDave",
    "created_at": "2010-09-13T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96805",
    "user": "drkirkby"
}
```

On seconds thoughts, this is a portability issue in general, not one specific to HP-UX. So changing the component back. 

Dave



---

archive/issue_comments_096806.json:
```json
{
    "body": "Changing component from AIX or HP-UX ports to porting.",
    "created_at": "2010-09-13T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96806",
    "user": "drkirkby"
}
```

Changing component from AIX or HP-UX ports to porting.



---

archive/issue_comments_096807.json:
```json
{
    "body": "There is no longer a \"blas\" package.",
    "created_at": "2015-09-08T12:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96807",
    "user": "jdemeyer"
}
```

There is no longer a "blas" package.



---

archive/issue_comments_096808.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-08T12:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96808",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096809.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-08T12:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96809",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9816#issuecomment-96810",
    "user": "vbraun"
}
```

Resolution: fixed
