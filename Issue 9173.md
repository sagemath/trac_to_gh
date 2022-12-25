# Issue 9173: cygwin: BSD.py tests behave differently on cygwin, so need to be written to reflect that

archive/issues_009173.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori @dimpase @kcrisman\n\n\n```\n\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/BSD.py\"   \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py\", line 174:\n    sage: native_two_isogeny_descent_work(E, E.two_torsion_rank())\nExpected:\n    (1, 1, 0, 0, None)\nGot:\n    (0, 1, 0, 1, None)\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py\", line 391:\n    sage: E.prove_BSD(verbosity=1, secs_hi=1)\nExpected:\n    p = 2: True by 2-descent\n    Timeout stopped Heegner index computation...\n    Proceeding to use heegner_index_bound instead.\n    True for p not in {2, 3} by Kolyvagin.\n    [3]\nGot:\n    p = 2: True by 2-descent\n    Timeout stopped Heegner index computation...\n    Proceeding to use heegner_index_bound instead.\n    True for p not in {2, 3, 5} by Kolyvagin.\n    True for p=5 by Stein-Wuthrich.\n    [3]\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py\", line 426:\n    sage: E.prove_BSD(verbosity=1)\nExpected:\n    p = 2: True by 2-descent\n    Timeout stopped Heegner index computation...\n    Proceeding to use heegner_index_bound instead.\n    True for p not in {2} by Kolyvagin.\n    []\nGot:\n    p = 2: True by 2-descent\n    Timeout stopped Heegner index computation...\n    Proceeding to use heegner_index_bound instead.\n    True for p not in {2, 3, 5} by Kolyvagin.\n    True for p=5 by Stein-Wuthrich.\n    p = 3 may divide the Heegner index, for which only a bound was computed.\n    ALERT: p = 3 left in Kolyvagin bound\n        0 <= ord_p(#Sha) <= 2\n        ord_p(#Sha_an) = 0\n    [3]\n**********************************************************************\n2 items had failures:\n   1 of   7 in __main__.example_4\n   2 of  34 in __main__.example_6\n***Test Failed*** 3 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9173\n\n",
    "created_at": "2010-06-07T04:55:50Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: BSD.py tests behave differently on cygwin, so need to be written to reflect that",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9173",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  jpflori @dimpase @kcrisman


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/BSD.py"   
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 174:
    sage: native_two_isogeny_descent_work(E, E.two_torsion_rank())
Expected:
    (1, 1, 0, 0, None)
Got:
    (0, 1, 0, 1, None)
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 391:
    sage: E.prove_BSD(verbosity=1, secs_hi=1)
Expected:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3} by Kolyvagin.
    [3]
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3, 5} by Kolyvagin.
    True for p=5 by Stein-Wuthrich.
    [3]
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 426:
    sage: E.prove_BSD(verbosity=1)
Expected:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2} by Kolyvagin.
    []
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3, 5} by Kolyvagin.
    True for p=5 by Stein-Wuthrich.
    p = 3 may divide the Heegner index, for which only a bound was computed.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 0
    [3]
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_4
   2 of  34 in __main__.example_6
***Test Failed*** 3 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/9173





---

archive/issue_comments_085660.json:
```json
{
    "body": "The same is happening on Solaris 10 on all the SPARC boxes I have access to - see #9127  It appears to be a function of the speed of the computer, with timeouts occuring on slower hardware. I assume the overhead of Cygwin is causing this problem. \n\nAs such, I think this can probably be closed as a duplicate of #9127, which has positive review. You can try the patch there\n\nhttp://trac.sagemath.org/sage_trac/raw-attachment/ticket/9127/trac_9127.patch\n\nDave",
    "created_at": "2010-06-08T00:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85660",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The same is happening on Solaris 10 on all the SPARC boxes I have access to - see #9127  It appears to be a function of the speed of the computer, with timeouts occuring on slower hardware. I assume the overhead of Cygwin is causing this problem. 

As such, I think this can probably be closed as a duplicate of #9127, which has positive review. You can try the patch there

http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9127/trac_9127.patch

Dave



---

archive/issue_comments_085661.json:
```json
{
    "body": "On closer inspection, it looks like the issues you are getting on Cygwin are larger than those on Solaris, as I have not seen the \n\n\n```\nExpected:\n    (1, 1, 0, 0, None)\nGot:\n    (0, 1, 0, 1, None)\n```\n\n\nerror - only the ones due to timeouts. \n\nDave",
    "created_at": "2010-06-08T00:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85661",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

On closer inspection, it looks like the issues you are getting on Cygwin are larger than those on Solaris, as I have not seen the 


```
Expected:
    (1, 1, 0, 0, None)
Got:
    (0, 1, 0, 1, None)
```


error - only the ones due to timeouts. 

Dave



---

archive/issue_comments_085662.json:
```json
{
    "body": "This doctest passed on a build of mine on XP.  In fact, the only files in schemes/ that failed were two in the plane conics section, probably because of \"I\" not working.",
    "created_at": "2011-08-02T02:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85662",
    "user": "https://github.com/kcrisman"
}
```

This doctest passed on a build of mine on XP.  In fact, the only files in schemes/ that failed were two in the plane conics section, probably because of "I" not working.



---

archive/issue_comments_085663.json:
```json
{
    "body": "I get lots of forking errors now, because it \"can't start pari\".",
    "created_at": "2013-01-15T15:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85663",
    "user": "https://github.com/kcrisman"
}
```

I get lots of forking errors now, because it "can't start pari".



---

archive/issue_comments_085664.json:
```json
{
    "body": "And the test passes for me (64bits W7 + 5.6.rc0).",
    "created_at": "2013-01-15T18:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85664",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

And the test passes for me (64bits W7 + 5.6.rc0).



---

archive/issue_comments_085665.json:
```json
{
    "body": "> And the test passes for me (64bits W7 + 5.6.rc0).\nDon't forget to try these by hand as well.  In the past I've had failures only in the terminal.",
    "created_at": "2013-01-15T18:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85665",
    "user": "https://github.com/kcrisman"
}
```

> And the test passes for me (64bits W7 + 5.6.rc0).
Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.



---

archive/issue_comments_085666.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> > And the test passes for me (64bits W7 + 5.6.rc0).\n> Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.\nYou mean copy/paste the doctests in an interactive Sage session?\nThat's kind of boring isn't it? :)",
    "created_at": "2013-01-15T21:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85666",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:6 kcrisman]:
> > And the test passes for me (64bits W7 + 5.6.rc0).
> Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.
You mean copy/paste the doctests in an interactive Sage session?
That's kind of boring isn't it? :)



---

archive/issue_comments_085667.json:
```json
{
    "body": "I tested some random examples and some from te failing ones quoting in the ticket description and had no problems.",
    "created_at": "2013-01-15T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85667",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I tested some random examples and some from te failing ones quoting in the ticket description and had no problems.



---

archive/issue_comments_085668.json:
```json
{
    "body": "> > > And the test passes for me (64bits W7 + 5.6.rc0).\n> > Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.\n> You mean copy/paste the doctests in an interactive Sage session?\n> That's kind of boring isn't it? :)\nYes, you are right.  But unfortunately I had some bad experiences with these Cygwin tests in the past so I figure I should ask - sorry :(",
    "created_at": "2013-01-16T01:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85668",
    "user": "https://github.com/kcrisman"
}
```

> > > And the test passes for me (64bits W7 + 5.6.rc0).
> > Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.
> You mean copy/paste the doctests in an interactive Sage session?
> That's kind of boring isn't it? :)
Yes, you are right.  But unfortunately I had some bad experiences with these Cygwin tests in the past so I figure I should ask - sorry :(



---

archive/issue_comments_085669.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-30T10:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85669",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-08T12:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85670",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022563.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/jpflori",
    "created_at": "2013-02-08T12:45:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9173#event-22563"
}
```



---

archive/issue_comments_085671.json:
```json
{
    "body": "No problems on another install, so let's close this one.",
    "created_at": "2013-02-08T12:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85671",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

No problems on another install, so let's close this one.



---

archive/issue_comments_085672.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-08T13:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9173#issuecomment-85672",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_022564.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-08T13:19:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9173",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9173#event-22564"
}
```
