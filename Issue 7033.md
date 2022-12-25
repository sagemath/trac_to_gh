# Issue 7033: libfplll can't find _gmpz_init in -lgmp

archive/issues_007033.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @dimpase\n\nKeywords: solaris gmp\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021\n\nCC was set to the Sun C compiler, and CXX to the Sun C++ compiler, \n\n\n```\nchecking whether we are using the GNU C++ compiler... (cached) no\nchecking whether /opt/xxxsunstudio12.1/bin/CC accepts -g... (cached) yes\nchecking dependency style of /opt/xxxsunstudio12.1/bin/CC... (cached) none\nchecking for gcc... (cached) /opt/xxxsunstudio12.1/bin/cc\nchecking whether we are using the GNU C compiler... (cached) no\nchecking whether /opt/xxxsunstudio12.1/bin/cc accepts -g... (cached) yes\nchecking for /opt/xxxsunstudio12.1/bin/cc option to accept ISO C89... (cached) none needed\nchecking dependency style of /opt/xxxsunstudio12.1/bin/cc... (cached) none\nchecking whether make sets $(MAKE)... (cached) yes\nchecking for __gmpz_init in -lgmp... no\nconfigure: error: GNU MP not found, see http://gmplib.org\nError configuring libfplll\n\nreal    0m45.568s\nuser    0m10.239s\nsys     0m25.294s\n```\n\n\nmpir is insalled ok - all the gmp headers and libraries have been built. I suspect some programs not to accept mpir as being the same as gmp when the compiler is not gcc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7033\n\n",
    "created_at": "2009-09-27T14:51:48Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libfplll can't find _gmpz_init in -lgmp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7033",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @dimpase

Keywords: solaris gmp

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler, 


```
checking whether we are using the GNU C++ compiler... (cached) no
checking whether /opt/xxxsunstudio12.1/bin/CC accepts -g... (cached) yes
checking dependency style of /opt/xxxsunstudio12.1/bin/CC... (cached) none
checking for gcc... (cached) /opt/xxxsunstudio12.1/bin/cc
checking whether we are using the GNU C compiler... (cached) no
checking whether /opt/xxxsunstudio12.1/bin/cc accepts -g... (cached) yes
checking for /opt/xxxsunstudio12.1/bin/cc option to accept ISO C89... (cached) none needed
checking dependency style of /opt/xxxsunstudio12.1/bin/cc... (cached) none
checking whether make sets $(MAKE)... (cached) yes
checking for __gmpz_init in -lgmp... no
configure: error: GNU MP not found, see http://gmplib.org
Error configuring libfplll

real    0m45.568s
user    0m10.239s
sys     0m25.294s
```


mpir is insalled ok - all the gmp headers and libraries have been built. I suspect some programs not to accept mpir as being the same as gmp when the compiler is not gcc.

Issue created by migration from https://trac.sagemath.org/ticket/7033





---

archive/issue_comments_058132.json:
```json
{
    "body": "Changing component from build to packages: standard.",
    "created_at": "2015-09-08T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7033#issuecomment-58132",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to packages: standard.



---

archive/issue_comments_058133.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7033#issuecomment-58133",
    "user": "https://github.com/mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_comments_058134.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7033#issuecomment-58134",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_007254.json:
```json
{
    "actor": "@slel",
    "created_at": "2020-08-22T07:15:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7033",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7033#event-7254"
}
```



---

archive/issue_comments_058135.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-22T07:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7033#issuecomment-58135",
    "user": "https://github.com/slel"
}
```

Resolution: invalid
