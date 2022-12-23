# Issue 9365: sage-4.5.alpha0: R fails to build on OS X 10.6

archive/issues_009365.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nSee\n\n  http://sage.math.washington.edu/home/wstein/tmp/install-4.5.alpha0.log\n\nand \n\n  http://sage.math.washington.edu/home/justin/logs/install-4.5.a0.log\n\nfor potentially two different issues with building R on OS X 10.6\n\nIssue created by migration from https://trac.sagemath.org/ticket/9365\n\n",
    "created_at": "2010-06-28T21:08:45Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "sage-4.5.alpha0: R fails to build on OS X 10.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9365",
    "user": "was"
}
```
Assignee: GeorgSWeber

See

  http://sage.math.washington.edu/home/wstein/tmp/install-4.5.alpha0.log

and 

  http://sage.math.washington.edu/home/justin/logs/install-4.5.a0.log

for potentially two different issues with building R on OS X 10.6

Issue created by migration from https://trac.sagemath.org/ticket/9365





---

archive/issue_comments_088962.json:
```json
{
    "body": "I suspect it is related to this - #9346 \n\nDave",
    "created_at": "2010-06-28T21:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9365#issuecomment-88962",
    "user": "drkirkby"
}
```

I suspect it is related to this - #9346 

Dave



---

archive/issue_comments_088963.json:
```json
{
    "body": "The fix for Justin's problem is up at #9388.\n\nI suspect the fixes to fortran in 4.5.alpha1 will fix William's, so once we see a successful R build on bsd.math, we can close this ticket.",
    "created_at": "2010-06-30T01:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9365#issuecomment-88963",
    "user": "rlm"
}
```

The fix for Justin's problem is up at #9388.

I suspect the fixes to fortran in 4.5.alpha1 will fix William's, so once we see a successful R build on bsd.math, we can close this ticket.



---

archive/issue_comments_088964.json:
```json
{
    "body": "This has been fixed by the fortran spkg updates in sage-4.5.alpha1.",
    "created_at": "2010-06-30T22:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9365#issuecomment-88964",
    "user": "rlm"
}
```

This has been fixed by the fortran spkg updates in sage-4.5.alpha1.



---

archive/issue_comments_088965.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-06-30T22:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9365#issuecomment-88965",
    "user": "rlm"
}
```

Resolution: worksforme
