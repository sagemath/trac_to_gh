# Issue 7028: matplotlib 0.99.0 tries to use C compiler for C++ code.

archive/issues_007028.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used, I found that matplotlib-0.99.0 will not build. \n\nCC was set to the Sun C compler, and CXX to the Sun C++ compiler, What appears to be happening is that matplotlib-0.99.0 is taking the CC variable but using that to try to build C++ code. Note the extension on the file the C compiler is trying to compile is '.cc', suggesting to me that it is really C++ code. \n\n```\n/opt/xxxsunstudio12.1/bin/cc -DNDEBUG -O -xcode=pic32 -DPY_ARRAYAUNIQUE_SYMBOL=MPL_ARRAY_API -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/numpy/core/include -I/usr/sfw/include -I/usr/sfw/include/freetype2 -I/usr/local/include -I. -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/ -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -c src/ft2font.cpp -o build/temp.solaris-2.10-sun4u-2.6/src/ft2font.o\ncc: No valid input files specified, no output generated\nerror: command '/opt/xxxsunstudio12.1/bin/cc' failed with exit status 1\nError building matplotlib package.\n\nreal    0m3.752s\nuser    0m1.227s\nsys     0m1.034s\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7028\n\n",
    "created_at": "2009-09-27T12:05:58Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "matplotlib 0.99.0 tries to use C compiler for C++ code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7028",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used, I found that matplotlib-0.99.0 will not build. 

CC was set to the Sun C compler, and CXX to the Sun C++ compiler, What appears to be happening is that matplotlib-0.99.0 is taking the CC variable but using that to try to build C++ code. Note the extension on the file the C compiler is trying to compile is '.cc', suggesting to me that it is really C++ code. 

```
/opt/xxxsunstudio12.1/bin/cc -DNDEBUG -O -xcode=pic32 -DPY_ARRAYAUNIQUE_SYMBOL=MPL_ARRAY_API -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/numpy/core/include -I/usr/sfw/include -I/usr/sfw/include/freetype2 -I/usr/local/include -I. -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/ -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -c src/ft2font.cpp -o build/temp.solaris-2.10-sun4u-2.6/src/ft2font.o
cc: No valid input files specified, no output generated
error: command '/opt/xxxsunstudio12.1/bin/cc' failed with exit status 1
Error building matplotlib package.

real    0m3.752s
user    0m1.227s
sys     0m1.034s

```

Issue created by migration from https://trac.sagemath.org/ticket/7028





---

archive/issue_comments_058110.json:
```json
{
    "body": "This has been reported upstream to matplotlib-users`@`lists.sourceforge.net. The developers acknowledge this is a bug, but to quote from Michael Droettboom. \n\n*This is a years-old known bug in distutils (which it looks like you've already commented on...).  I've looked at it many times over those years, and it's really very difficult to fix from outside without terrible monkey-patching hacks that are certain to break on as many systems as they fix.*\n\nOne suggested workaround is to defined CC to be a C++ compiler, then all code gets built with a C++ compiler. I have poined out that there will be a performance impact with this.",
    "created_at": "2009-11-24T16:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7028#issuecomment-58110",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This has been reported upstream to matplotlib-users`@`lists.sourceforge.net. The developers acknowledge this is a bug, but to quote from Michael Droettboom. 

*This is a years-old known bug in distutils (which it looks like you've already commented on...).  I've looked at it many times over those years, and it's really very difficult to fix from outside without terrible monkey-patching hacks that are certain to break on as many systems as they fix.*

One suggested workaround is to defined CC to be a C++ compiler, then all code gets built with a C++ compiler. I have poined out that there will be a performance impact with this.



---

archive/issue_events_016495.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16495"
}
```



---

archive/issue_events_016496.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16496"
}
```



---

archive/issue_events_016497.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16497"
}
```



---

archive/issue_events_016498.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16498"
}
```



---

archive/issue_events_016499.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16499"
}
```



---

archive/issue_events_016500.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16500"
}
```



---

archive/issue_events_016501.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16501"
}
```



---

archive/issue_comments_058111.json:
```json
{
    "body": "Changing component from build to packages: standard.",
    "created_at": "2015-09-08T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7028#issuecomment-58111",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to packages: standard.



---

archive/issue_events_016502.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-09-22T13:33:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16502"
}
```



---

archive/issue_events_016503.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-09-22T13:33:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7028#event-16503"
}
```



---

archive/issue_comments_058112.json:
```json
{
    "body": "So Jeroen, you want to resurrect this issue to fix distutils in sage?",
    "created_at": "2017-09-24T09:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7028#issuecomment-58112",
    "user": "https://github.com/kiwifb"
}
```

So Jeroen, you want to resurrect this issue to fix distutils in sage?
