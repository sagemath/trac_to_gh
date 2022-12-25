# Issue 6201: CC() raises exception instead of returning 0

archive/issues_006201.json:
```json
{
    "body": "Assignee: somebody\n\nThis is inconsistent:\n\n\n```\nZZ(); QQ(); RR(); CC()\n\n0\n0\n0.000000000000000\nTraceback (click to the left for traceback)\n...\nTypeError: __call__() takes at least 2 arguments (1 given)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6201\n\n",
    "created_at": "2009-06-03T21:14:11Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "CC() raises exception instead of returning 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6201",
    "user": "https://github.com/fredrik-johansson"
}
```
Assignee: somebody

This is inconsistent:


```
ZZ(); QQ(); RR(); CC()

0
0
0.000000000000000
Traceback (click to the left for traceback)
...
TypeError: __call__() takes at least 2 arguments (1 given)
```


Issue created by migration from https://trac.sagemath.org/ticket/6201





---

archive/issue_comments_049445.json:
```json
{
    "body": "Changing assignee from somebody to @aghitza.",
    "created_at": "2009-06-03T23:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6201#issuecomment-49445",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from somebody to @aghitza.



---

archive/issue_events_014548.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-06-03T23:09:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "milestone": "sage-4.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6201#event-14548"
}
```



---

archive/issue_comments_049446.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-03T23:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6201#issuecomment-49446",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049447.json:
```json
{
    "body": "Simple fix up for review.",
    "created_at": "2009-06-03T23:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6201#issuecomment-49447",
    "user": "https://github.com/aghitza"
}
```

Simple fix up for review.



---

archive/issue_comments_049448.json:
```json
{
    "body": "Attachment [trac_6201.patch](tarball://root/attachments/some-uuid/ticket6201/trac_6201.patch) by @jhpalmieri created at 2009-06-09 03:41:34\n\nSimple change to the code, includes a doctest, passes all tests, reference manual builds.  Positive review.\n\nNow should we do the same thing with GF(2)(), CDF(), etc.?",
    "created_at": "2009-06-09T03:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6201#issuecomment-49448",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6201.patch](tarball://root/attachments/some-uuid/ticket6201/trac_6201.patch) by @jhpalmieri created at 2009-06-09 03:41:34

Simple change to the code, includes a doctest, passes all tests, reference manual builds.  Positive review.

Now should we do the same thing with GF(2)(), CDF(), etc.?



---

archive/issue_events_014549.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T21:19:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6201#event-14549"
}
```



---

archive/issue_comments_049449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6201#issuecomment-49449",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
