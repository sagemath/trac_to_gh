# Issue 9172: cygwin: numerical noise in sage/rings/integer.pyx

archive/issues_009172.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori\n\n\n```\n\nsage -t  \"devel/sage/sage/rings/integer.pyx\"                \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/rings/integer.pyx\", line 1681:\n    sage: 2^float(1.5)       # python float\nExpected:\n    2.8284271247461903\nGot:\n    2.8284271247461898\n**********************************************************************\n1 items had failures:\n   1 of  26 in __main__.example_42\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_integer.py\n\t [15.2 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9172\n\n",
    "created_at": "2010-06-07T04:52:04Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: numerical noise in sage/rings/integer.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9172",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  jpflori


```

sage -t  "devel/sage/sage/rings/integer.pyx"                
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/rings/integer.pyx", line 1681:
    sage: 2^float(1.5)       # python float
Expected:
    2.8284271247461903
Got:
    2.8284271247461898
**********************************************************************
1 items had failures:
   1 of  26 in __main__.example_42
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_integer.py
	 [15.2 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/9172





---

archive/issue_comments_085645.json:
```json
{
    "body": "The correct answer is 2*sqrt(2), which is `2.8284271247461900976033774484193961...`  \n\nSo the expected value is `2.0239x10`<sup>-16</sup> high, and result on Cygwin is 2.9760x10<sup>-16</sup> low. So the errors on Linux/OSX/Solaris is not much lower than on Cygwin. We can't really expect any more from a floating point number. \n\nWe could change the Expected value to `2.8284271247461...` What I don't like about that, is then much larger errors can exist and them not be detected. But this is far from the only such case, so I suggest just changing the test to `2.8284271247461...`, which will solve this. \n\nDave",
    "created_at": "2011-02-09T17:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85645",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The correct answer is 2*sqrt(2), which is `2.8284271247461900976033774484193961...`  

So the expected value is `2.0239x10`<sup>-16</sup> high, and result on Cygwin is 2.9760x10<sup>-16</sup> low. So the errors on Linux/OSX/Solaris is not much lower than on Cygwin. We can't really expect any more from a floating point number. 

We could change the Expected value to `2.8284271247461...` What I don't like about that, is then much larger errors can exist and them not be detected. But this is far from the only such case, so I suggest just changing the test to `2.8284271247461...`, which will solve this. 

Dave



---

archive/issue_comments_085646.json:
```json
{
    "body": "This file passed doctests on a build of mine on XP.",
    "created_at": "2011-08-02T02:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85646",
    "user": "https://github.com/kcrisman"
}
```

This file passed doctests on a build of mine on XP.



---

archive/issue_comments_085647.json:
```json
{
    "body": "But when doing the test by hand, the same thing happens.",
    "created_at": "2011-08-19T14:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85647",
    "user": "https://github.com/kcrisman"
}
```

But when doing the test by hand, the same thing happens.



---

archive/issue_comments_085648.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2013-01-15T15:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85648",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_085649.json:
```json
{
    "body": "This now fails with\n\n```\n2.82842712474619\n```\n\nwhich I suppose is an improvement.  Maybe we can use `abs tol`?",
    "created_at": "2013-01-15T15:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85649",
    "user": "https://github.com/kcrisman"
}
```

This now fails with

```
2.82842712474619
```

which I suppose is an improvement.  Maybe we can use `abs tol`?



---

archive/issue_comments_085650.json:
```json
{
    "body": "And the test passes for me (64bits W7 + 5.6.rc0).",
    "created_at": "2013-01-15T18:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85650",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

And the test passes for me (64bits W7 + 5.6.rc0).



---

archive/issue_comments_085651.json:
```json
{
    "body": "> And the test passes for me (64bits W7 + 5.6.rc0).\nIn which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?",
    "created_at": "2013-01-15T18:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85651",
    "user": "https://github.com/kcrisman"
}
```

> And the test passes for me (64bits W7 + 5.6.rc0).
In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?



---

archive/issue_comments_085652.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-27T10:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85652",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085653.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> > And the test passes for me (64bits W7 + 5.6.rc0).\n> In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?\n\nworks for me, both ways. I think we can close this one.",
    "created_at": "2013-01-27T10:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85653",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:6 kcrisman]:
> > And the test passes for me (64bits W7 + 5.6.rc0).
> In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?

works for me, both ways. I think we can close this one.



---

archive/issue_comments_085654.json:
```json
{
    "body": "Hmm, I'm reluctant to not just change this a bit for 32-bit...",
    "created_at": "2013-01-28T02:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85654",
    "user": "https://github.com/kcrisman"
}
```

Hmm, I'm reluctant to not just change this a bit for 32-bit...



---

archive/issue_comments_085655.json:
```json
{
    "body": "Yeah, I think we should make sure this passes on 32 bits.\nI'll double check when I have the time to build on such a computer.",
    "created_at": "2013-01-30T10:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85655",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Yeah, I think we should make sure this passes on 32 bits.
I'll double check when I have the time to build on such a computer.



---

archive/issue_comments_085656.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-30T10:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85656",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085657.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-08T12:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85657",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_085658.json:
```json
{
    "body": "I have no problems on my 32 bits Windows 7 install, so Cygwin must have gotten better.\nI really doubt Cygwin on XP would have a different behavior for this one, so let's close it.",
    "created_at": "2013-02-08T12:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85658",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I have no problems on my 32 bits Windows 7 install, so Cygwin must have gotten better.
I really doubt Cygwin on XP would have a different behavior for this one, so let's close it.



---

archive/issue_events_009329.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-08T13:20:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9172#event-9329"
}
```



---

archive/issue_comments_085659.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-08T13:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85659",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
