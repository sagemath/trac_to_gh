# Issue 9033: Singular does not try to build 64-bit on OpenSolaris.

archive/issues_009033.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @dimpase\n\nOn a Sun Ultra 27 running OpenSolaris x64, Singular is not attempting to build as a 64-bit binary, but also fails to build fully as a 32-bit binary. (It does however build partially as 32-bit).\n\n```\nsingular-3-1-0-4-20100214/src/svd/tests/\nsingular-3-1-0-4-20100214/src/svd/tests/testsvdunit.h\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\n\n<snip>\ngcc -O3 -g -fPIC -I. -I/export/home/drkirkby/sage-4.4.2/local/include  -I/export/home/drkirkby/sage-4.4.2/local/include -DHAVE_CONFIG_H -c omBinPage.c\n<snip>\ng++ -c cf_factor.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.4.2/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include  -I/export/home/drkirkby/sage-4.4.2/local/include -O3 -g -fPIC -o cf_factor.o\nIn file included from /export/home/drkirkby/sage-4.4.2/local/include/NTL/vec_ZZ.h:5,\n                 from /export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZX.h:5,\n                 from /export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZXFactoring.h:5,\n                 from NTLconvert.h:23,\n                 from cf_factor.cc:33:\n/export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZ.h: In function \u2018long int NTL::MulModPrecon(long int, long int, long int, long unsigned int)\u2019:\n/export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZ.h:1795: error: \u2018MulHiUL\u2019 was not declared in this scope\nmake[2]: *** [cf_factor.o] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/singular-3-1-0-4-20100214/src/factory'\nmake[1]: *** [install] Error 1\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/singular-3-1-0-4-20100214/src'\nmake: *** [/export/home/drkirkby/sage-4.4.2/local/bin/Singular-3-1-0] Error 2\nUnable to build Singular.\n\nreal    0m13.142s\nuser    0m8.853s\nsys     0m4.226s\nsage: An error occurred while installing singular-3-1-0-4-20100214\n```\n\nThe files \n\n```\n$SAGE_LOCAL/lib/omalloc_debug.o\n$SAGE_LOCAL/lib/omalloc.o\n```\n\nare being installed as 32-bit bit objects. \n\nIt's somewhat worrying this does not build fully. If it built fully as 32-bit, one would expect converting it to 64-bit would be relatively easy (add option -m64), but the problem could be a bit more serious than this. I've not investigated yet. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9033\n\n",
    "created_at": "2010-05-24T10:43:56Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Singular does not try to build 64-bit on OpenSolaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9033",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @dimpase

On a Sun Ultra 27 running OpenSolaris x64, Singular is not attempting to build as a 64-bit binary, but also fails to build fully as a 32-bit binary. (It does however build partially as 32-bit).

```
singular-3-1-0-4-20100214/src/svd/tests/
singular-3-1-0-4-20100214/src/svd/tests/testsvdunit.h
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************

<snip>
gcc -O3 -g -fPIC -I. -I/export/home/drkirkby/sage-4.4.2/local/include  -I/export/home/drkirkby/sage-4.4.2/local/include -DHAVE_CONFIG_H -c omBinPage.c
<snip>
g++ -c cf_factor.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.4.2/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include  -I/export/home/drkirkby/sage-4.4.2/local/include -O3 -g -fPIC -o cf_factor.o
In file included from /export/home/drkirkby/sage-4.4.2/local/include/NTL/vec_ZZ.h:5,
                 from /export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZX.h:5,
                 from /export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZXFactoring.h:5,
                 from NTLconvert.h:23,
                 from cf_factor.cc:33:
/export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZ.h: In function ‘long int NTL::MulModPrecon(long int, long int, long int, long unsigned int)’:
/export/home/drkirkby/sage-4.4.2/local/include/NTL/ZZ.h:1795: error: ‘MulHiUL’ was not declared in this scope
make[2]: *** [cf_factor.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/singular-3-1-0-4-20100214/src/factory'
make[1]: *** [install] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/singular-3-1-0-4-20100214/src'
make: *** [/export/home/drkirkby/sage-4.4.2/local/bin/Singular-3-1-0] Error 2
Unable to build Singular.

real    0m13.142s
user    0m8.853s
sys     0m4.226s
sage: An error occurred while installing singular-3-1-0-4-20100214
```

The files 

```
$SAGE_LOCAL/lib/omalloc_debug.o
$SAGE_LOCAL/lib/omalloc.o
```

are being installed as 32-bit bit objects. 

It's somewhat worrying this does not build fully. If it built fully as 32-bit, one would expect converting it to 64-bit would be relatively easy (add option -m64), but the problem could be a bit more serious than this. I've not investigated yet. 

Issue created by migration from https://trac.sagemath.org/ticket/9033





---

archive/issue_comments_083495.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9033#issuecomment-83495",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_events_022110.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22110"
}
```



---

archive/issue_events_022111.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22111"
}
```



---

archive/issue_events_022112.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22112"
}
```



---

archive/issue_events_022113.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22113"
}
```



---

archive/issue_events_022114.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22114"
}
```



---

archive/issue_events_022115.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22115"
}
```



---

archive/issue_events_022116.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22116"
}
```



---

archive/issue_comments_083496.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9033#issuecomment-83496",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022117.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-08T16:33:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22117"
}
```



---

archive/issue_events_022118.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-08T16:33:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22118"
}
```



---

archive/issue_comments_083497.json:
```json
{
    "body": "outdated, should be closed",
    "created_at": "2020-07-08T16:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9033#issuecomment-83497",
    "user": "https://github.com/mkoeppe"
}
```

outdated, should be closed



---

archive/issue_comments_083498.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-08T18:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9033#issuecomment-83498",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083499.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9033#issuecomment-83499",
    "user": "https://github.com/fchapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.



---

archive/issue_events_022119.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-15T07:18:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9033#event-22119"
}
```



---

archive/issue_comments_083500.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9033#issuecomment-83500",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
