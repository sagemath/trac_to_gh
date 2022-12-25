# Issue 7024: Flint ignores CC and CXX.

archive/issues_007024.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori\n\nFlitn 1.3.0.p2 is one of several programs which ignores the settings of CC and CXX and users a gcc and g++ that it finds. \n\n\n```\n\nflint-1.3.0.p2/src/profiler.h\nflint-1.3.0.p2/src/mpn_extras-test.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nFound gcc 4 or later\nTurning off loop unrolling on Solaris/Sparc\nmake[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/flint-1.3.0.p2/src'\ngcc -std=c99 -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/ -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include  -fPIC  -O2  -DNDEBUG -o zn_mod.o -c zn_poly/src/zn_mod.c\n```\n\nThis needs fixing to add support for the Sun Studio compilers.\n\n**spkg**:\n[http://wstein.org/home/ohanar/clang-port/sage-5.0.beta1-src/spkg/standard/flint-1.5.0.p11.spkg](http://wstein.org/home/ohanar/clang-port/sage-5.0.beta1-src/spkg/standard/flint-1.5.0.p11.spkg)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7024\n\n",
    "closed_at": "2013-11-23T10:36:33Z",
    "created_at": "2009-09-27T10:57:28Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Flint ignores CC and CXX.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7024",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  jpflori

Flitn 1.3.0.p2 is one of several programs which ignores the settings of CC and CXX and users a gcc and g++ that it finds. 


```

flint-1.3.0.p2/src/profiler.h
flint-1.3.0.p2/src/mpn_extras-test.c
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
Found gcc 4 or later
Turning off loop unrolling on Solaris/Sparc
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/flint-1.3.0.p2/src'
gcc -std=c99 -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/ -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include  -fPIC  -O2  -DNDEBUG -o zn_mod.o -c zn_poly/src/zn_mod.c
```

This needs fixing to add support for the Sun Studio compilers.

**spkg**:
[http://wstein.org/home/ohanar/clang-port/sage-5.0.beta1-src/spkg/standard/flint-1.5.0.p11.spkg](http://wstein.org/home/ohanar/clang-port/sage-5.0.beta1-src/spkg/standard/flint-1.5.0.p11.spkg)


Issue created by migration from https://trac.sagemath.org/ticket/7024





---

archive/issue_comments_058057.json:
```json
{
    "body": "See ticket #6919 for an updated FLINT spkg.",
    "created_at": "2009-09-27T11:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58057",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See ticket #6919 for an updated FLINT spkg.



---

archive/issue_comments_058058.json:
```json
{
    "body": "Bill Hart reported on 27th September that:\n\n''I've added this to a FLINT todo list and will attend to it in the next release.\n\nThanks for mentioning it.\n\nBill.''\n\nI will chase this up, to find out if it is fixed or not.",
    "created_at": "2009-11-25T03:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58058",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Bill Hart reported on 27th September that:

''I've added this to a FLINT todo list and will attend to it in the next release.

Thanks for mentioning it.

Bill.''

I will chase this up, to find out if it is fixed or not.



---

archive/issue_comments_058059.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-09T14:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58059",
    "user": "https://github.com/ohanar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058060.json:
```json
{
    "body": "Attachment [flint-1.5.0.p11.patch](tarball://root/attachments/some-uuid/ticket7024/flint-1.5.0.p11.patch) by @ohanar created at 2012-02-09 14:38:31\n\nfor review purposes",
    "created_at": "2012-02-09T14:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58060",
    "user": "https://github.com/ohanar"
}
```

Attachment [flint-1.5.0.p11.patch](tarball://root/attachments/some-uuid/ticket7024/flint-1.5.0.p11.patch) by @ohanar created at 2012-02-09 14:38:31

for review purposes



---

archive/issue_comments_058061.json:
```json
{
    "body": "`$CC` and `$CXX` have to be quoted.\n\nNote that the issue is (at least partially) fixed upstream in FLINT 1.5.2 IIRC; I already made an spkg with various other changes (including the `Makefile`) a while ago btw. ... (cf. discussion at #9858)",
    "created_at": "2012-03-17T01:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58061",
    "user": "https://github.com/nexttime"
}
```

`$CC` and `$CXX` have to be quoted.

Note that the issue is (at least partially) fixed upstream in FLINT 1.5.2 IIRC; I already made an spkg with various other changes (including the `Makefile`) a while ago btw. ... (cf. discussion at #9858)



---

archive/issue_comments_058062.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-17T01:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58062",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_016478.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7024#event-16478"
}
```



---

archive/issue_comments_058063.json:
```json
{
    "body": "Works with the newer FLINT 2.x",
    "created_at": "2013-11-23T10:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58063",
    "user": "https://github.com/jdemeyer"
}
```

Works with the newer FLINT 2.x



---

archive/issue_events_016479.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-11-23T10:36:33Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7024#event-16479"
}
```



---

archive/issue_events_016480.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-11-23T10:36:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7024#event-16480"
}
```



---

archive/issue_comments_058064.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-11-23T10:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7024#issuecomment-58064",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_016481.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-11-23T10:36:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7024",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7024#event-16481"
}
```
