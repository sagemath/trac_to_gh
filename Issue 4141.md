# Issue 4141: OS X: R pulls in libraries from fink

archive/issues_004141.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  georgsweber @williamstein\n\nWhen building sage 3.1.2 without hiding fink,\n\n```\nsage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtcl8.4.dylib\nsage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtk8.4.dylib\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4141\n\n",
    "created_at": "2008-09-18T00:39:25Z",
    "labels": [
        "component: distribution",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "OS X: R pulls in libraries from fink",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4141",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```
Assignee: mabshoff

CC:  georgsweber @williamstein

When building sage 3.1.2 without hiding fink,

```
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtcl8.4.dylib
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtk8.4.dylib
```

Issue created by migration from https://trac.sagemath.org/ticket/4141





---

archive/issue_comments_030007.json:
```json
{
    "body": "Since we now automatically make Sage barf when /sw is in PATH, is this ticket invalid?  I no longer have that in my PATH, so I can't test this - someone else?",
    "created_at": "2010-05-26T20:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4141#issuecomment-30007",
    "user": "https://github.com/kcrisman"
}
```

Since we now automatically make Sage barf when /sw is in PATH, is this ticket invalid?  I no longer have that in my PATH, so I can't test this - someone else?



---

archive/issue_events_009427.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2010-05-26T20:28:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4141#event-9427"
}
```



---

archive/issue_comments_030008.json:
```json
{
    "body": "Yeah, we can close this.  I put it back in my PATH (in fact, the very files listed here are available in my /sw folder!) and got\n\n```\n***************************************************\n***************************************************\nFound Fink in  /sw/bin//fink\n\n*********************************************************\n\nFound either MacPorts or Fink in your PATH, which potentially wrecks the Sage build process.\nYou should make sure MacPorts and Fink cannot be found.  Either:\n(1) rename /opt/local and /sw, or\n(2) change PATH and DYLD_LIBRARY_PATH\n(Once Sage is built, you can restore them.)\n\n*********************************************************\n\nmake[1]: *** [installed/prereq-0.8] Error 1\n\nreal\t0m5.581s\nuser\t0m1.715s\nsys\t0m1.913s\nError building Sage.\nmake: *** [build] Error 1\nnew-host-2:sage-4.7.alpha5-Finktest \n```\nSo I highly doubt this is possible any more.    We haven't gotten a single report of this other than this one in 3 years.  \n\nAlso, the sage-check-libraries.py script that found this on #4140 seems to not work any more!  \n\nAnyway, this should be closed.",
    "created_at": "2011-04-26T02:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4141#issuecomment-30008",
    "user": "https://github.com/kcrisman"
}
```

Yeah, we can close this.  I put it back in my PATH (in fact, the very files listed here are available in my /sw folder!) and got

```
***************************************************
***************************************************
Found Fink in  /sw/bin//fink

*********************************************************

Found either MacPorts or Fink in your PATH, which potentially wrecks the Sage build process.
You should make sure MacPorts and Fink cannot be found.  Either:
(1) rename /opt/local and /sw, or
(2) change PATH and DYLD_LIBRARY_PATH
(Once Sage is built, you can restore them.)

*********************************************************

make[1]: *** [installed/prereq-0.8] Error 1

real	0m5.581s
user	0m1.715s
sys	0m1.913s
Error building Sage.
make: *** [build] Error 1
new-host-2:sage-4.7.alpha5-Finktest 
```
So I highly doubt this is possible any more.    We haven't gotten a single report of this other than this one in 3 years.  

Also, the sage-check-libraries.py script that found this on #4140 seems to not work any more!  

Anyway, this should be closed.



---

archive/issue_comments_030009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-04-26T02:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4141#issuecomment-30009",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030010.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-26T02:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4141#issuecomment-30010",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030011.json:
```json
{
    "body": "> Also, the sage-check-libraries.py script that found this on #4140 seems to not work any more!  \n\n\nIn the meantime I found #4127, which talks about how to correctly use it.  Sadly, the file itself doesn't tell this (e.g., source sage-env first!).",
    "created_at": "2011-04-26T03:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4141#issuecomment-30011",
    "user": "https://github.com/kcrisman"
}
```

> Also, the sage-check-libraries.py script that found this on #4140 seems to not work any more!  


In the meantime I found #4127, which talks about how to correctly use it.  Sadly, the file itself doesn't tell this (e.g., source sage-env first!).



---

archive/issue_events_009428.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-26T09:08:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4141#event-9428"
}
```



---

archive/issue_events_009429.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-26T09:08:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4141#event-9429"
}
```



---

archive/issue_events_009430.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-26T09:08:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4141#event-9430"
}
```



---

archive/issue_comments_030012.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-04-26T09:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4141#issuecomment-30012",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
