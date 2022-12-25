# Issue 9222: improve doctest coverage of databases/conway.py

archive/issues_009222.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu\n\nKeywords: conway polynomial database\n\nAs of sage-4.4.3:\n\n\n```\n----------------------------------------------------------------------\nconway.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE conway.py: 0% (0 of 7)\n\nMissing documentation:\n\t * _init(self):\n\t * __repr__(self):\n\t * polynomial(self, p, n):\n\t * has_polynomial(self, p, n):\n\t * primes(self):\n\t * degrees(self, p):\n\n\nMissing doctests:\n\t * __init__(self, read_only=True):\n\n----------------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9222\n\n",
    "created_at": "2010-06-12T07:09:15Z",
    "labels": [
        "component: doctest coverage",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "improve doctest coverage of databases/conway.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9222",
    "user": "https://github.com/aghitza"
}
```
Assignee: tbd

CC:  mvngu

Keywords: conway polynomial database

As of sage-4.4.3:


```
----------------------------------------------------------------------
conway.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE conway.py: 0% (0 of 7)

Missing documentation:
	 * _init(self):
	 * __repr__(self):
	 * polynomial(self, p, n):
	 * has_polynomial(self, p, n):
	 * primes(self):
	 * degrees(self, p):


Missing doctests:
	 * __init__(self, read_only=True):

----------------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/9222





---

archive/issue_comments_086374.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-12T08:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86374",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086375.json:
```json
{
    "body": "After the patch:\n\n\n```\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE conway.py: 85% (6 of 7)\n\nMissing documentation:\n\t * _init(self):\n```\n\n\nI'm not convinced a `TestSuite` test makes sense here (and I have tried to put one in and got a pickling-related error).  Also, I'm not sure what `_init(self)` is meant to be doing, so I'm leaving it alone for now.",
    "created_at": "2010-06-12T08:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86375",
    "user": "https://github.com/aghitza"
}
```

After the patch:


```
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE conway.py: 85% (6 of 7)

Missing documentation:
	 * _init(self):
```


I'm not convinced a `TestSuite` test makes sense here (and I have tried to put one in and got a pickling-related error).  Also, I'm not sure what `_init(self)` is meant to be doing, so I'm leaving it alone for now.



---

archive/issue_comments_086376.json:
```json
{
    "body": "Looks fine to me. Tests pass and the documentation builds OK. I agree that the _init method isn't something one can reasonably doctest!",
    "created_at": "2010-06-14T10:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86376",
    "user": "https://github.com/loefflerd"
}
```

Looks fine to me. Tests pass and the documentation builds OK. I agree that the _init method isn't something one can reasonably doctest!



---

archive/issue_comments_086377.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-14T10:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86377",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086378.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T02:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86378",
    "user": "https://github.com/dandrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086379.json:
```json
{
    "body": "Please include ticket numbers in the commit strings of your patches!",
    "created_at": "2010-07-22T02:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86379",
    "user": "https://github.com/dandrake"
}
```

Please include ticket numbers in the commit strings of your patches!



---

archive/issue_comments_086380.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-22T03:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86380",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_086381.json:
```json
{
    "body": "Attachment [trac_9222.patch](tarball://root/attachments/some-uuid/ticket9222/trac_9222.patch) by @aghitza created at 2010-07-22 03:12:03\n\nDone.",
    "created_at": "2010-07-22T03:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86381",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_9222.patch](tarball://root/attachments/some-uuid/ticket9222/trac_9222.patch) by @aghitza created at 2010-07-22 03:12:03

Done.



---

archive/issue_comments_086382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86382",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_086383.json:
```json
{
    "body": "Replying to [comment:6 AlexGhitza]:\n> Done.\n\nThanks!",
    "created_at": "2010-07-22T07:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86383",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:6 AlexGhitza]:
> Done.

Thanks!



---

archive/issue_events_009380.json:
```json
{
    "actor": "@dandrake",
    "created_at": "2010-07-22T07:46:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9222#event-9380"
}
```
