# Issue 6599: hidden markov models are completely broken on OS X 64-bit

archive/issues_006599.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nwas@bsd:~/build/64bit/sage-4.1.rc1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: A  = [[0.5,0.5],[0.5,0.5]]\nsage: B  = [[(0.5,(0.0,1.0)), (0.1,(1,10000))],[(1,(1,1)), (0,(0,0.1))]]\nsage: pi = [1,0]\nsage: hmm.GaussianMixtureHiddenMarkovModel(A, B, pi)\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n```\n\n\nNote that a long time ago we stupidly turned off doctesting of HMM's so that tests would pass on itanium.  We were lazy and never turned them back on, which is why this never got caught before. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6599\n\n",
    "created_at": "2009-07-23T10:12:26Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "hidden markov models are completely broken on OS X 64-bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6599",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
was@bsd:~/build/64bit/sage-4.1.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A  = [[0.5,0.5],[0.5,0.5]]
sage: B  = [[(0.5,(0.0,1.0)), (0.1,(1,10000))],[(1,(1,1)), (0,(0,0.1))]]
sage: pi = [1,0]
sage: hmm.GaussianMixtureHiddenMarkovModel(A, B, pi)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```


Note that a long time ago we stupidly turned off doctesting of HMM's so that tests would pass on itanium.  We were lazy and never turned them back on, which is why this never got caught before. 

Issue created by migration from https://trac.sagemath.org/ticket/6599





---

archive/issue_comments_053919.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-04-30T12:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6599#issuecomment-53919",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053920.json:
```json
{
    "body": "There are plenty of tests in sage/stats/hmm/hmm.pyx.\n\nLet us close that old one.",
    "created_at": "2018-04-30T12:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6599#issuecomment-53920",
    "user": "https://github.com/fchapoton"
}
```

There are plenty of tests in sage/stats/hmm/hmm.pyx.

Let us close that old one.



---

archive/issue_comments_053921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-06-01T12:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6599#issuecomment-53921",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053922.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6599#issuecomment-53922",
    "user": "https://github.com/embray"
}
```

Resolution: invalid



---

archive/issue_events_006838.json:
```json
{
    "actor": "@embray",
    "created_at": "2019-02-26T13:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6599",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6599#event-6838"
}
```



---

archive/issue_comments_053923.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6599#issuecomment-53923",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
