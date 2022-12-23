# Issue 9174: cygwin: robert miller's 2-descent is completely broken on cygwin

archive/issues_009174.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori dimpase kcrisman\n\n\n```\n\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\"\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1093:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    1\nGot:\n    0\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1098:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    2\nGot:\n    0\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1102:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    3\nGot:\n    2*log(3)/log(2) - 2\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1195:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    1\nGot:\n    0\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1198:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    2\nGot:\n    0\n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1201:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    3\nGot:\n    log(3)/log(2) - 1\n**********************************************************************\n2 items had failures:\n   3 of  30 in __main__.example_18\n   3 of  11 in __main__.example_19\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_descent_two_isogeny.py\n\t [29.1 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9174\n\n",
    "created_at": "2010-06-07T04:57:52Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "cygwin: robert miller's 2-descent is completely broken on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9174",
    "user": "was"
}
```
Assignee: tbd

CC:  jpflori dimpase kcrisman


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx"
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1093:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    1
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1098:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    2
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1102:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    3
Got:
    2*log(3)/log(2) - 2
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1195:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    1
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1198:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    2
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1201:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    3
Got:
    log(3)/log(2) - 1
**********************************************************************
2 items had failures:
   3 of  30 in __main__.example_18
   3 of  11 in __main__.example_19
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_descent_two_isogeny.py
	 [29.1 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/9174





---

archive/issue_comments_085811.json:
```json
{
    "body": "This file passed doctests in a build of mine on XP.",
    "created_at": "2011-08-02T02:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85811",
    "user": "kcrisman"
}
```

This file passed doctests in a build of mine on XP.



---

archive/issue_comments_085812.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-19T14:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85812",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085813.json:
```json
{
    "body": "And checking by hand works. \n\nSince this was undoubtedly an XP machine on which the original failure was reported, I will move this to sage-invalid.",
    "created_at": "2011-08-19T14:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85813",
    "user": "kcrisman"
}
```

And checking by hand works. 

Since this was undoubtedly an XP machine on which the original failure was reported, I will move this to sage-invalid.



---

archive/issue_comments_085814.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-19T14:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85814",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085815.json:
```json
{
    "body": "But doing anything other than the **first** one by hand doesn't work.  In fact, nasty things happen.",
    "created_at": "2011-08-19T14:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85815",
    "user": "kcrisman"
}
```

But doing anything other than the **first** one by hand doesn't work.  In fact, nasty things happen.



---

archive/issue_comments_085816.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-08-19T14:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85816",
    "user": "kcrisman"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085817.json:
```json
{
    "body": "I attempted this, but got forking errors; that doesn't mean it doesn't actually work.  JP, want to give it a whirl?",
    "created_at": "2013-01-15T16:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85817",
    "user": "kcrisman"
}
```

I attempted this, but got forking errors; that doesn't mean it doesn't actually work.  JP, want to give it a whirl?



---

archive/issue_comments_085818.json:
```json
{
    "body": "And the test passes for me (64bits W7 + 5.6.rc0).",
    "created_at": "2013-01-15T18:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85818",
    "user": "jpflori"
}
```

And the test passes for me (64bits W7 + 5.6.rc0).



---

archive/issue_comments_085819.json:
```json
{
    "body": "> And the test passes for me (64bits W7 + 5.6.rc0).\nDon't forget to try these by hand as well.  In the past I've had failures only in the terminal.",
    "created_at": "2013-01-15T18:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85819",
    "user": "kcrisman"
}
```

> And the test passes for me (64bits W7 + 5.6.rc0).
Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.



---

archive/issue_comments_085820.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-30T10:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85820",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085821.json:
```json
{
    "body": "No problems on another 32 bits W7, let's close this one.",
    "created_at": "2013-02-08T12:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85821",
    "user": "jpflori"
}
```

No problems on another 32 bits W7, let's close this one.



---

archive/issue_comments_085822.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-08T12:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85822",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085823.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-08T13:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9174#issuecomment-85823",
    "user": "jdemeyer"
}
```

Resolution: worksforme
