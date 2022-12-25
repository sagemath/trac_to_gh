# Issue 9721: Problem upgrading from 4.5.2 to 4.5.3.alpha0 on OS X 10.6

archive/issues_009721.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @kcrisman @nexttime\n\nReported by Karl-Dieter Crisman on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/a487f3968757f7b4#a487f3968757f7b4):\n\n```\n4.5.3.alpha0 did NOT upgrade successfully for me on OS X 10.6 from\n4.5.2.  See below - though note that Sage does start up properly, and\nsage -i returns (among others)\n\nlibm4ri-20100221\n\nhowever the\n\npycrypto-2.1.0 pynac-0.2.0.p5 sage-4.5.3.alpha0\n\npackages did then not update either, presumably.\n\n- kcrisman\n\nThread model: posix\ngcc version 4.2.1 (Apple Inc. build 5664)\n****************************************************\nStarting build...\nRemoving old PolyBoRi install...\nDone removing old PolyBoRi install.\nRunning build_polybori...\nscons: Reading SConscript files ...\nChecking for C header file gd.h... yes\nChecking for C library gd... no\nChecking for C++ header file ext/hash_map... yes\nWarning: No LaTeX to html converter found, Tutorial will not be installed\nChecking for C library m4ri... no\nChecking for C header file gd.h... yes\nChecking for C library gd... no\nSymlinking to M4RI/m4ri ...\nOSError: [Errno 2] No such file or directory:\n  File \"/Users/.../sage-4.5.2/spkg/build/polybori-0.6.4.p2/src/polybori-0.6.4/SConstruct\", line 421:\n    os.symlink('.', m4ri_inc)\nError building PolyBoRi.\n\nreal    0m1.425s\nuser    0m0.860s\nsys     0m0.473s\nsage: An error occurred while installing polybori-0.6.4.p2\n```\n\nLeif Leonhardy [replied](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/69df2817539da964#69df2817539da964):\n\n```\nThat's apparently due to my new (stripped) PolyBoRi spkg (#9472).\n\nI'm currently looking at this, but in principle SCons should find the\n\"external m4ri\" (on MacOS X, too) and not try to use the (now obsolete)\ncopy of it that was included in previous PolyBoRi spkgs. \n```\n\nRelated: #9472.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9721\n\n",
    "created_at": "2010-08-11T01:17:29Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Problem upgrading from 4.5.2 to 4.5.3.alpha0 on OS X 10.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9721",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  @kcrisman @nexttime

Reported by Karl-Dieter Crisman on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/a487f3968757f7b4#a487f3968757f7b4):

```
4.5.3.alpha0 did NOT upgrade successfully for me on OS X 10.6 from
4.5.2.  See below - though note that Sage does start up properly, and
sage -i returns (among others)

libm4ri-20100221

however the

pycrypto-2.1.0 pynac-0.2.0.p5 sage-4.5.3.alpha0

packages did then not update either, presumably.

- kcrisman

Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5664)
****************************************************
Starting build...
Removing old PolyBoRi install...
Done removing old PolyBoRi install.
Running build_polybori...
scons: Reading SConscript files ...
Checking for C header file gd.h... yes
Checking for C library gd... no
Checking for C++ header file ext/hash_map... yes
Warning: No LaTeX to html converter found, Tutorial will not be installed
Checking for C library m4ri... no
Checking for C header file gd.h... yes
Checking for C library gd... no
Symlinking to M4RI/m4ri ...
OSError: [Errno 2] No such file or directory:
  File "/Users/.../sage-4.5.2/spkg/build/polybori-0.6.4.p2/src/polybori-0.6.4/SConstruct", line 421:
    os.symlink('.', m4ri_inc)
Error building PolyBoRi.

real    0m1.425s
user    0m0.860s
sys     0m0.473s
sage: An error occurred while installing polybori-0.6.4.p2
```

Leif Leonhardy [replied](http://groups.google.com/group/sage-release/browse_thread/thread/7abfbeedb07abb53/69df2817539da964#69df2817539da964):

```
That's apparently due to my new (stripped) PolyBoRi spkg (#9472).

I'm currently looking at this, but in principle SCons should find the
"external m4ri" (on MacOS X, too) and not try to use the (now obsolete)
copy of it that was included in previous PolyBoRi spkgs. 
```

Related: #9472.

Issue created by migration from https://trac.sagemath.org/ticket/9721





---

archive/issue_comments_094740.json:
```json
{
    "body": "Note that neither the M4RI library **nor the GD library** (in the second attempt) are found, so this is not directly (or exclusively) related to removing the M4RI source tree.\n\nIt seems some SCons parameters have gotten messed up during the upgrade process. I'm currently trying to reproduce this error on Linux (though frankly speaking I expect this to be Apple-specific once again...)\n\nCan someone try to reproduce this on other MacOS X boxes?",
    "created_at": "2010-08-11T02:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94740",
    "user": "https://github.com/nexttime"
}
```

Note that neither the M4RI library **nor the GD library** (in the second attempt) are found, so this is not directly (or exclusively) related to removing the M4RI source tree.

It seems some SCons parameters have gotten messed up during the upgrade process. I'm currently trying to reproduce this error on Linux (though frankly speaking I expect this to be Apple-specific once again...)

Can someone try to reproduce this on other MacOS X boxes?



---

archive/issue_comments_094741.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> I'm currently trying to reproduce this error on Linux (though frankly speaking I expect this to be Apple-specific once again...)\n\n\"Of course\"<sup>TM</sup> this worked for me on Ubuntu 9.04 x86_64.\n(I've built 4.5.2 from scratch, successfully run ptestlong, successfully upgraded to 4.5.3.alpha0, then again successfully run ptestlong.)\n\n```\n...\nStarting build...\nRemoving old PolyBoRi install...\nDone removing old PolyBoRi install.\nRunning build_polybori...\nscons: Reading SConscript files ...\nChecking for C header file gd.h... yes\nChecking for C library gd... no\nChecking for C++ header file unordered_map... no\nChecking for C++ header file tr1/unordered_map... yes\nWarning: No LaTeX to html converter found, Tutorial will not be installed\nChecking for C library m4ri... yes\nChecking for C header file gd.h... yes\nChecking for C library gd... yes\nno python extension\nscons: done reading SConscript files.\nscons: Building targets ...\n...\n```\n\n\nI don't think disabling/bypassing the check for a system (or Sage) M4RI library will fix Karl-Dieter's issue, since the GD library wasn't found either.\n\nSo, again,\n\n> Can someone try to reproduce this on other MacOS X boxes?\n\nPerhaps just his base installation was somehow broken...",
    "created_at": "2010-08-11T04:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94741",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:1 leif]:
> I'm currently trying to reproduce this error on Linux (though frankly speaking I expect this to be Apple-specific once again...)

"Of course"<sup>TM</sup> this worked for me on Ubuntu 9.04 x86_64.
(I've built 4.5.2 from scratch, successfully run ptestlong, successfully upgraded to 4.5.3.alpha0, then again successfully run ptestlong.)

```
...
Starting build...
Removing old PolyBoRi install...
Done removing old PolyBoRi install.
Running build_polybori...
scons: Reading SConscript files ...
Checking for C header file gd.h... yes
Checking for C library gd... no
Checking for C++ header file unordered_map... no
Checking for C++ header file tr1/unordered_map... yes
Warning: No LaTeX to html converter found, Tutorial will not be installed
Checking for C library m4ri... yes
Checking for C header file gd.h... yes
Checking for C library gd... yes
no python extension
scons: done reading SConscript files.
scons: Building targets ...
...
```


I don't think disabling/bypassing the check for a system (or Sage) M4RI library will fix Karl-Dieter's issue, since the GD library wasn't found either.

So, again,

> Can someone try to reproduce this on other MacOS X boxes?

Perhaps just his base installation was somehow broken...



---

archive/issue_comments_094742.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> Can someone try to reproduce this on other MacOS X boxes?\n\nI upgraded successfully from a scratch-built 4.5.2 to 4.5.3.alpha0 on bsd.math (OS X 10.6).",
    "created_at": "2010-08-11T09:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94742",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:1 leif]:
> Can someone try to reproduce this on other MacOS X boxes?

I upgraded successfully from a scratch-built 4.5.2 to 4.5.3.alpha0 on bsd.math (OS X 10.6).



---

archive/issue_comments_094743.json:
```json
{
    "body": "This might be relevant http://trac.sagemath.org/sage_trac/ticket/9717#comment:5",
    "created_at": "2010-08-11T12:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94743",
    "user": "https://github.com/malb"
}
```

This might be relevant http://trac.sagemath.org/sage_trac/ticket/9717#comment:5



---

archive/issue_comments_094744.json:
```json
{
    "body": "Is it possible that #9717, which we merged into 4.5.3.alpha1, has fixed this problem?",
    "created_at": "2010-08-17T07:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94744",
    "user": "https://github.com/qed777"
}
```

Is it possible that #9717, which we merged into 4.5.3.alpha1, has fixed this problem?



---

archive/issue_comments_094745.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Is it possible that #9717, which we merged into 4.5.3.alpha1, has fixed this problem?\nI will try to check this out today.  It will depend on whether my wireless connection is useful - I won't have other access today.",
    "created_at": "2010-08-17T10:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94745",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 mpatel]:
> Is it possible that #9717, which we merged into 4.5.3.alpha1, has fixed this problem?
I will try to check this out today.  It will depend on whether my wireless connection is useful - I won't have other access today.



---

archive/issue_comments_094746.json:
```json
{
    "body": "Well, I was able to upgrade from the (broken) 4.5.2 to 4.5.3.alpha1 with no problems and all tests seem to be passing.  Is that good enough?",
    "created_at": "2010-08-17T19:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94746",
    "user": "https://github.com/kcrisman"
}
```

Well, I was able to upgrade from the (broken) 4.5.2 to 4.5.3.alpha1 with no problems and all tests seem to be passing.  Is that good enough?



---

archive/issue_comments_094747.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-17T22:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94747",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_events_024328.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-17T22:02:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9721#event-24328"
}
```



---

archive/issue_events_024329.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-17T22:02:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9721#event-24329"
}
```



---

archive/issue_comments_094748.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Replying to [comment:1 leif]:\n> > Can someone try to reproduce this on other MacOS X boxes?\n> \n> I upgraded successfully from a scratch-built 4.5.2 to 4.5.3.alpha0 on bsd.math (OS X 10.6).\n\nFor what it's worth, a 4.5.2-to-4.5.3.alpha1 upgrade also works for me.  The long doctests pass.\n\nI'm resolving this ticket as a \"duplicate\" of (possibly fixed by) #9717.  Of course, we can reopen it or open another ticket, if there are new reports.",
    "created_at": "2010-08-17T22:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9721",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9721#issuecomment-94748",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 mpatel]:
> Replying to [comment:1 leif]:
> > Can someone try to reproduce this on other MacOS X boxes?
> 
> I upgraded successfully from a scratch-built 4.5.2 to 4.5.3.alpha0 on bsd.math (OS X 10.6).

For what it's worth, a 4.5.2-to-4.5.3.alpha1 upgrade also works for me.  The long doctests pass.

I'm resolving this ticket as a "duplicate" of (possibly fixed by) #9717.  Of course, we can reopen it or open another ticket, if there are new reports.
