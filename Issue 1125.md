# Issue 1125: cvxopt fix completely breaks building Sage with gfortran

archive/issues_001125.json:
```json
{
    "body": "Assignee: was\n\n\n```\n> \n> Compiling from source using gcc-4.2.2, I get\n> \n> ***\n> x86-Linux, ia64-Linux\n> ***\n> While compiling cvxopt-0.8.2.p4, I get\n> \n> gcc -pthread -shared build/temp.linux-i686-2.5/C/base.o\n> build/temp.linux-i686-2.5/C/dense.o\n> build/temp.linux-i686-2.5/C/sparse.o\n> -L/home/kate/sage/sage-2.8.12-x86-Linux/local/lib\n> -L/home/kate/sage/sage-2.8.12-x86-Linux/local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3\n> -lm -llapack -lblas -lf95 -o build/lib.linux-i686-2.5/cvxopt/base.so\n> /usr/local/binutils-2.17/x86-Linux-gcc-4.1.1/bin/ld: cannot find -lf95\n\nThat's because you're using gfortran.  Evidently Josh's fix for cvxopt not fully working\nfails for people using gfortran.  I'll open a trac ticket. \n\n```\n\n\n\nThis either has to be properly fixed, or cvxopt has to be removed or something.\nWe need to make sure we fully support using gfortran.  Perhaps we should just\ncompletely switch to using gfortran and make having gfortran installed a requirement for building sage.  Tempting.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/1125\n\n",
    "created_at": "2007-11-07T19:06:15Z",
    "labels": [
        "packages: standard",
        "critical",
        "bug"
    ],
    "title": "cvxopt fix completely breaks building Sage with gfortran",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1125",
    "user": "was"
}
```
Assignee: was


```
> 
> Compiling from source using gcc-4.2.2, I get
> 
> ***
> x86-Linux, ia64-Linux
> ***
> While compiling cvxopt-0.8.2.p4, I get
> 
> gcc -pthread -shared build/temp.linux-i686-2.5/C/base.o
> build/temp.linux-i686-2.5/C/dense.o
> build/temp.linux-i686-2.5/C/sparse.o
> -L/home/kate/sage/sage-2.8.12-x86-Linux/local/lib
> -L/home/kate/sage/sage-2.8.12-x86-Linux/local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3
> -lm -llapack -lblas -lf95 -o build/lib.linux-i686-2.5/cvxopt/base.so
> /usr/local/binutils-2.17/x86-Linux-gcc-4.1.1/bin/ld: cannot find -lf95

That's because you're using gfortran.  Evidently Josh's fix for cvxopt not fully working
fails for people using gfortran.  I'll open a trac ticket. 

```



This either has to be properly fixed, or cvxopt has to be removed or something.
We need to make sure we fully support using gfortran.  Perhaps we should just
completely switch to using gfortran and make having gfortran installed a requirement for building sage.  Tempting.  

Issue created by migration from https://trac.sagemath.org/ticket/1125





---

archive/issue_comments_006796.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2007-11-07T19:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1125#issuecomment-6796",
    "user": "was"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_006797.json:
```json
{
    "body": "Waiting on feedbackk from Kate, but there is a new spkg by Josh:\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/cvxopt-0.8.2.p5.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-11-08T20:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1125#issuecomment-6797",
    "user": "mabshoff"
}
```

Waiting on feedbackk from Kate, but there is a new spkg by Josh:

http://sage.math.washington.edu/home/jkantor/spkgs/cvxopt-0.8.2.p5.spkg

Cheers,

Michael



---

archive/issue_comments_006798.json:
```json
{
    "body": "The spkg in 1161 incorporates the fix for this and also upgrades cvxopt to a newer version.",
    "created_at": "2007-11-17T01:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1125#issuecomment-6798",
    "user": "jkantor"
}
```

The spkg in 1161 incorporates the fix for this and also upgrades cvxopt to a newer version.



---

archive/issue_comments_006799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T06:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1125#issuecomment-6799",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006800.json:
```json
{
    "body": "superseded by #1161, which also contains this fix.",
    "created_at": "2007-11-18T06:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1125#issuecomment-6800",
    "user": "mabshoff"
}
```

superseded by #1161, which also contains this fix.
