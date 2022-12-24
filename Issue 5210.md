# Issue 5210: gmp-mpir-0.9.rc3: make check failure on various OSX boxen

archive/issues_005210.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nPASS: t-assign \nPASS: t-binary \nPASS: t-cast \nPASS: t-constr \nPASS: t-headers \nPASS: t-istream \nistream mpf_t operator>> wrong \n  point , \n  str   \"1,\" \n  got   123 \n  want  1 \n  localeconv point \",\" \n/bin/sh: line 1: 13352 Abort trap              ${dir}$tst \nFAIL: t-locale \nPASS: t-misc \nPASS: t-ops \nPASS: t-ostream \nPASS: t-prec \nPASS: t-rand \nPASS: t-ternary \nPASS: t-unary \n============================================================= \n1 of 14 tests failed \nPlease report to http://groups.google.co.uk/group/mpir-devel/ \n============================================================= \nmake[6]: *** [check-TESTS] Error 1 \nmake[5]: *** [check-am] Error 2 \nmake[4]: *** [check-recursive] Error 1 \nmake[3]: *** [check-recursive] Error 1 \nmake[2]: *** [check] Error 2 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5210\n\n",
    "created_at": "2009-02-08T20:17:37Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "gmp-mpir-0.9.rc3: make check failure on various OSX boxen",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5210",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
PASS: t-assign 
PASS: t-binary 
PASS: t-cast 
PASS: t-constr 
PASS: t-headers 
PASS: t-istream 
istream mpf_t operator>> wrong 
  point , 
  str   "1," 
  got   123 
  want  1 
  localeconv point "," 
/bin/sh: line 1: 13352 Abort trap              ${dir}$tst 
FAIL: t-locale 
PASS: t-misc 
PASS: t-ops 
PASS: t-ostream 
PASS: t-prec 
PASS: t-rand 
PASS: t-ternary 
PASS: t-unary 
============================================================= 
1 of 14 tests failed 
Please report to http://groups.google.co.uk/group/mpir-devel/ 
============================================================= 
make[6]: *** [check-TESTS] Error 1 
make[5]: *** [check-am] Error 2 
make[4]: *** [check-recursive] Error 1 
make[3]: *** [check-recursive] Error 1 
make[2]: *** [check] Error 2 
```


Issue created by migration from https://trac.sagemath.org/ticket/5210





---

archive/issue_comments_039916.json:
```json
{
    "body": "The cause of the bug has been isolated in the discussion at\n\n   http://groups.google.com/group/mpir-devel/t/aff995c6c3beb58d\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T11:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5210#issuecomment-39916",
    "user": "mabshoff"
}
```

The cause of the bug has been isolated in the discussion at

   http://groups.google.com/group/mpir-devel/t/aff995c6c3beb58d

Cheers,

Michael



---

archive/issue_comments_039917.json:
```json
{
    "body": "The spkg at\n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc0/gmp-mpir-0.9.rc4.spkg\n\nfixes the problem. Tested on all of SkyNet, various OSX boxen where it blew up before and sage.math. Unlike the previous spkg the test suite was run in all cases unlike the previous one where by sheer coincidence I tested an spkg where the test suite wasn't run on all affected OSX boxen. Talk about a freak accident :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T02:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5210#issuecomment-39917",
    "user": "mabshoff"
}
```

The spkg at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc0/gmp-mpir-0.9.rc4.spkg

fixes the problem. Tested on all of SkyNet, various OSX boxen where it blew up before and sage.math. Unlike the previous spkg the test suite was run in all cases unlike the previous one where by sheer coincidence I tested an spkg where the test suite wasn't run on all affected OSX boxen. Talk about a freak accident :)

Cheers,

Michael



---

archive/issue_comments_039918.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-11T02:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5210#issuecomment-39918",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039919.json:
```json
{
    "body": "Success for me.\n\n\n```\n~/Devel/sage-3.2.3 $ uname -a\nDarwin pv139196.reshsg.uci.edu 9.5.0 Darwin Kernel Version 9.5.0: Wed Sep  3 11:29:43 PDT 2008; root:xnu-1228.7.58~1/RELEASE_I386 i386 i386\n```\n\n\nLog at [http://sage.math.washington.edu/home/ncalexan/gmp-mpir-0.9.rc4.log](http://sage.math.washington.edu/home/ncalexan/gmp-mpir-0.9.rc4.log).",
    "created_at": "2009-02-11T05:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5210#issuecomment-39919",
    "user": "@ncalexan"
}
```

Success for me.


```
~/Devel/sage-3.2.3 $ uname -a
Darwin pv139196.reshsg.uci.edu 9.5.0 Darwin Kernel Version 9.5.0: Wed Sep  3 11:29:43 PDT 2008; root:xnu-1228.7.58~1/RELEASE_I386 i386 i386
```


Log at [http://sage.math.washington.edu/home/ncalexan/gmp-mpir-0.9.rc4.log](http://sage.math.washington.edu/home/ncalexan/gmp-mpir-0.9.rc4.log).



---

archive/issue_comments_039920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T05:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5210#issuecomment-39920",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039921.json:
```json
{
    "body": "Merged in Sage 3.3.rc0. Thanks Nick.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T05:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5210#issuecomment-39921",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc0. Thanks Nick.

Cheers,

Michael
