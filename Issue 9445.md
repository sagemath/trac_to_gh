# Issue 9445: GalRep.non_surjective_primes() returns unexpected errors

archive/issues_009445.json:
```json
{
    "body": "Assignee: cremona\n\nIt's possible these are related.  In tests of 4.5.a4, the following doctests fail:\n\n1)       File \"wrapper.pyx\", line 171, in sage.libs.galrep.wrapper.GalRep.non_surjective_primes (sage/libs/galrep/wrapper.c:2602)\n    ValueError: min and max must be <= 59\n\n2) File \"/Users/Sage/sage-4.5.alpha4/devel/sage/sage/libs/galrep/wrapper.pyx\", line 163:\n    sage: galrep.GalRep().non_surjective_primes(-432,8208,7,59)\nExpected:\n    []\nGot:\n    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]\n\nSeems to be a failure on Mac OS X, 10.5.8, and has not been reported elsewhere.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9445\n\n",
    "created_at": "2010-07-07T05:43:03Z",
    "labels": [
        "elliptic curves",
        "blocker",
        "bug"
    ],
    "title": "GalRep.non_surjective_primes() returns unexpected errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9445",
    "user": "justin"
}
```
Assignee: cremona

It's possible these are related.  In tests of 4.5.a4, the following doctests fail:

1)       File "wrapper.pyx", line 171, in sage.libs.galrep.wrapper.GalRep.non_surjective_primes (sage/libs/galrep/wrapper.c:2602)
    ValueError: min and max must be <= 59

2) File "/Users/Sage/sage-4.5.alpha4/devel/sage/sage/libs/galrep/wrapper.pyx", line 163:
    sage: galrep.GalRep().non_surjective_primes(-432,8208,7,59)
Expected:
    []
Got:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

Seems to be a failure on Mac OS X, 10.5.8, and has not been reported elsewhere.



Issue created by migration from https://trac.sagemath.org/ticket/9445





---

archive/issue_comments_090506.json:
```json
{
    "body": "I did not notice this ticket, but this is giving a different error on a Solaris 10 system (t2.math). See #9490. It's basically crashing:\n\n\n```\nsage -t -long \"devel/sage/sage/libs/galrep/wrapper.pyx\"     \n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\n\n\t [18.0 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/libs/galrep/wrapper.pyx\"\nTotal time for all tests: 18.0 seconds\n```\n\n\nI guess this was tested on Linux!\n\nDave",
    "created_at": "2010-07-13T14:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9445#issuecomment-90506",
    "user": "drkirkby"
}
```

I did not notice this ticket, but this is giving a different error on a Solaris 10 system (t2.math). See #9490. It's basically crashing:


```
sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"     


------------------------------------------------------------
Unhandled SIGBUS: A bus error occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------


	 [18.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"
Total time for all tests: 18.0 seconds
```


I guess this was tested on Linux!

Dave



---

archive/issue_comments_090507.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2010-07-14T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9445#issuecomment-90507",
    "user": "rlm"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_090508.json:
```json
{
    "body": "Remove blocker status since galrep was reverted.",
    "created_at": "2010-07-14T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9445#issuecomment-90508",
    "user": "rlm"
}
```

Remove blocker status since galrep was reverted.



---

archive/issue_comments_090509.json:
```json
{
    "body": "In fact, I'm closing the ticket since galrep was never added to Sage. This ticket will still be here to demonstrate the current problems...",
    "created_at": "2010-11-10T14:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9445#issuecomment-90509",
    "user": "rlm"
}
```

In fact, I'm closing the ticket since galrep was never added to Sage. This ticket will still be here to demonstrate the current problems...



---

archive/issue_comments_090510.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T14:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9445#issuecomment-90510",
    "user": "rlm"
}
```

Resolution: fixed
