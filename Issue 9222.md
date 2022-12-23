# Issue 9222: improve doctest coverage of databases/conway.py

archive/issues_009222.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu\n\nKeywords: conway polynomial database\n\nAs of sage-4.4.3:\n\n\n```\n----------------------------------------------------------------------\nconway.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE conway.py: 0% (0 of 7)\n\nMissing documentation:\n\t * _init(self):\n\t * __repr__(self):\n\t * polynomial(self, p, n):\n\t * has_polynomial(self, p, n):\n\t * primes(self):\n\t * degrees(self, p):\n\n\nMissing doctests:\n\t * __init__(self, read_only=True):\n\n----------------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9222\n\n",
    "created_at": "2010-06-12T07:09:15Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "title": "improve doctest coverage of databases/conway.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9222",
    "user": "AlexGhitza"
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

archive/issue_comments_086512.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-12T08:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86512",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086513.json:
```json
{
    "body": "After the patch:\n\n\n```\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE conway.py: 85% (6 of 7)\n\nMissing documentation:\n\t * _init(self):\n```\n\n\nI'm not convinced a `TestSuite` test makes sense here (and I have tried to put one in and got a pickling-related error).  Also, I'm not sure what `_init(self)` is meant to be doing, so I'm leaving it alone for now.",
    "created_at": "2010-06-12T08:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86513",
    "user": "AlexGhitza"
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

archive/issue_comments_086514.json:
```json
{
    "body": "Looks fine to me. Tests pass and the documentation builds OK. I agree that the _init method isn't something one can reasonably doctest!",
    "created_at": "2010-06-14T10:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86514",
    "user": "davidloeffler"
}
```

Looks fine to me. Tests pass and the documentation builds OK. I agree that the _init method isn't something one can reasonably doctest!



---

archive/issue_comments_086515.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-14T10:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86515",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086516.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T02:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86516",
    "user": "ddrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086517.json:
```json
{
    "body": "Please include ticket numbers in the commit strings of your patches!",
    "created_at": "2010-07-22T02:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86517",
    "user": "ddrake"
}
```

Please include ticket numbers in the commit strings of your patches!



---

archive/issue_comments_086518.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-22T03:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86518",
    "user": "AlexGhitza"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_086519.json:
```json
{
    "body": "Attachment\n\nDone.",
    "created_at": "2010-07-22T03:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86519",
    "user": "AlexGhitza"
}
```

Attachment

Done.



---

archive/issue_comments_086520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86520",
    "user": "ddrake"
}
```

Resolution: fixed



---

archive/issue_comments_086521.json:
```json
{
    "body": "Replying to [comment:6 AlexGhitza]:\n> Done.\n\nThanks!",
    "created_at": "2010-07-22T07:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9222#issuecomment-86521",
    "user": "ddrake"
}
```

Replying to [comment:6 AlexGhitza]:
> Done.

Thanks!
