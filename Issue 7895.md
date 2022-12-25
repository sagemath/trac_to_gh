# Issue 7895: Flint says SIZE_MAX is undeclared on Solaris 8

archive/issues_007895.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  goodwillhart@googlemail.com @dimpase\n\n\n```\nning.o -c zn_poly/src/tuning.c\nzn_poly/src/tuning.c:42: error: 'SIZE_MAX' undeclared here (not in a function)\nmake[2]: *** [tuning.o] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/flint-1.5.0.p2/src'\nError building flint shared library.\n\nreal    0m7.207s\nuser    0m6.680s\nsys     0m0.350s\nsage: An error occurred while installing flint-1.5.0.p2\n```\n\n\nIt is actually defined in the file\n\n\n```\n/usr/include/limits.h\n```\n\n\nat least on this Solaris 8 installation. \n\n\n```\nbash-2.03$ uname -a\nSunOS solaris8 5.8 Generic_108528-11 sun4u sparc SUNW,Sun-Blade-1000\nbash-2.03$ cat /etc/release\n                       Solaris 8 10/01 s28s_u6wos_08a SPARC\n           Copyright 2001 Sun Microsystems, Inc.  All Rights Reserved.\n                           Assembled 12 September 2001\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7895\n\n",
    "created_at": "2010-01-11T06:21:37Z",
    "labels": [
        "component: porting: solaris",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Flint says SIZE_MAX is undeclared on Solaris 8",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7895",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  goodwillhart@googlemail.com @dimpase


```
ning.o -c zn_poly/src/tuning.c
zn_poly/src/tuning.c:42: error: 'SIZE_MAX' undeclared here (not in a function)
make[2]: *** [tuning.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/flint-1.5.0.p2/src'
Error building flint shared library.

real    0m7.207s
user    0m6.680s
sys     0m0.350s
sage: An error occurred while installing flint-1.5.0.p2
```


It is actually defined in the file


```
/usr/include/limits.h
```


at least on this Solaris 8 installation. 


```
bash-2.03$ uname -a
SunOS solaris8 5.8 Generic_108528-11 sun4u sparc SUNW,Sun-Blade-1000
bash-2.03$ cat /etc/release
                       Solaris 8 10/01 s28s_u6wos_08a SPARC
           Copyright 2001 Sun Microsystems, Inc.  All Rights Reserved.
                           Assembled 12 September 2001
```



Issue created by migration from https://trac.sagemath.org/ticket/7895





---

archive/issue_comments_068558.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7895#issuecomment-68558",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_068559.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7895#issuecomment-68559",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068560.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-08T19:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7895#issuecomment-68560",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068561.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-14T16:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7895#issuecomment-68561",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
