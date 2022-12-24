# Issue 9172: cygwin: numerical noise in sage/rings/integer.pyx

archive/issues_009172.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori\n\n\n```\n\nsage -t  \"devel/sage/sage/rings/integer.pyx\"                \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/rings/integer.pyx\", line 1681:\n    sage: 2^float(1.5)       # python float\nExpected:\n    2.8284271247461903\nGot:\n    2.8284271247461898\n**********************************************************************\n1 items had failures:\n   1 of  26 in __main__.example_42\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_integer.py\n\t [15.2 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9172\n\n",
    "created_at": "2010-06-07T04:52:04Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: numerical noise in sage/rings/integer.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9172",
    "user": "was"
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

archive/issue_comments_085783.json:
```json
{
    "body": "The correct answer is 2*sqrt(2), which is `2.8284271247461900976033774484193961...`  \n\nSo the expected value is `2.0239x10`<sup>-16</sup> high, and result on Cygwin is 2.9760x10<sup>-16</sup> low. So the errors on Linux/OSX/Solaris is not much lower than on Cygwin. We can't really expect any more from a floating point number. \n\nWe could change the Expected value to `2.8284271247461...` What I don't like about that, is then much larger errors can exist and them not be detected. But this is far from the only such case, so I suggest just changing the test to `2.8284271247461...`, which will solve this. \n\nDave",
    "created_at": "2011-02-09T17:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85783",
    "user": "drkirkby"
}
```

The correct answer is 2*sqrt(2), which is `2.8284271247461900976033774484193961...`  

So the expected value is `2.0239x10`<sup>-16</sup> high, and result on Cygwin is 2.9760x10<sup>-16</sup> low. So the errors on Linux/OSX/Solaris is not much lower than on Cygwin. We can't really expect any more from a floating point number. 

We could change the Expected value to `2.8284271247461...` What I don't like about that, is then much larger errors can exist and them not be detected. But this is far from the only such case, so I suggest just changing the test to `2.8284271247461...`, which will solve this. 

Dave



---

archive/issue_comments_085784.json:
```json
{
    "body": "This file passed doctests on a build of mine on XP.",
    "created_at": "2011-08-02T02:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85784",
    "user": "kcrisman"
}
```

This file passed doctests on a build of mine on XP.



---

archive/issue_comments_085785.json:
```json
{
    "body": "But when doing the test by hand, the same thing happens.",
    "created_at": "2011-08-19T14:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85785",
    "user": "kcrisman"
}
```

But when doing the test by hand, the same thing happens.



---

archive/issue_comments_085786.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2013-01-15T15:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85786",
    "user": "kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_085787.json:
```json
{
    "body": "This now fails with\n\n```\n2.82842712474619\n```\n\nwhich I suppose is an improvement.  Maybe we can use `abs tol`?",
    "created_at": "2013-01-15T15:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85787",
    "user": "kcrisman"
}
```

This now fails with

```
2.82842712474619
```

which I suppose is an improvement.  Maybe we can use `abs tol`?



---

archive/issue_comments_085788.json:
```json
{
    "body": "And the test passes for me (64bits W7 + 5.6.rc0).",
    "created_at": "2013-01-15T18:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85788",
    "user": "jpflori"
}
```

And the test passes for me (64bits W7 + 5.6.rc0).



---

archive/issue_comments_085789.json:
```json
{
    "body": "> And the test passes for me (64bits W7 + 5.6.rc0).\nIn which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?",
    "created_at": "2013-01-15T18:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85789",
    "user": "kcrisman"
}
```

> And the test passes for me (64bits W7 + 5.6.rc0).
In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?



---

archive/issue_comments_085790.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-27T10:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85790",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085791.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> > And the test passes for me (64bits W7 + 5.6.rc0).\n> In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?\n\nworks for me, both ways. I think we can close this one.",
    "created_at": "2013-01-27T10:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85791",
    "user": "dimpase"
}
```

Replying to [comment:6 kcrisman]:
> > And the test passes for me (64bits W7 + 5.6.rc0).
> In which case it might just be a 32-bit versus 64-bit issue.  Did you try it by hand as well?

works for me, both ways. I think we can close this one.



---

archive/issue_comments_085792.json:
```json
{
    "body": "Hmm, I'm reluctant to not just change this a bit for 32-bit...",
    "created_at": "2013-01-28T02:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85792",
    "user": "kcrisman"
}
```

Hmm, I'm reluctant to not just change this a bit for 32-bit...



---

archive/issue_comments_085793.json:
```json
{
    "body": "Yeah, I think we should make sure this passes on 32 bits.\nI'll double check when I have the time to build on such a computer.",
    "created_at": "2013-01-30T10:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85793",
    "user": "jpflori"
}
```

Yeah, I think we should make sure this passes on 32 bits.
I'll double check when I have the time to build on such a computer.



---

archive/issue_comments_085794.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-30T10:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85794",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085795.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-08T12:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85795",
    "user": "jpflori"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_085796.json:
```json
{
    "body": "I have no problems on my 32 bits Windows 7 install, so Cygwin must have gotten better.\nI really doubt Cygwin on XP would have a different behavior for this one, so let's close it.",
    "created_at": "2013-02-08T12:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85796",
    "user": "jpflori"
}
```

I have no problems on my 32 bits Windows 7 install, so Cygwin must have gotten better.
I really doubt Cygwin on XP would have a different behavior for this one, so let's close it.



---

archive/issue_comments_085797.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-08T13:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9172#issuecomment-85797",
    "user": "jdemeyer"
}
```

Resolution: worksforme
