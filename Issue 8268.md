# Issue 8268: Improve speed of Christoffel word construction

archive/issues_008268.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  abmasse\n\nThis patch adds a new implementation for construction of Christoffel words using continued fraction :\n\n\n```\nsage: %timeit words.ChristoffelWord(5, 9, algorithm='linear')\n625 loops, best of 3: 67.7 \u00b5s per loop\nsage: %timeit words.ChristoffelWord(5, 9, algorithm='cf')\n625 loops, best of 3: 309 \u00b5s per loop\n```\n\n\nFor large words, it is much faster than the actual implementation.\n\n\n```\nsage: %timeit words.ChristoffelWord(500, 90001, algorithm='linear')\n5 loops, best of 3: 111 ms per loop\nsage: %timeit words.ChristoffelWord(500, 90001, algorithm='cf')\n125 loops, best of 3: 4 ms per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8268\n\n",
    "created_at": "2010-02-15T00:15:17Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Improve speed of Christoffel word construction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8268",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  abmasse

This patch adds a new implementation for construction of Christoffel words using continued fraction :


```
sage: %timeit words.ChristoffelWord(5, 9, algorithm='linear')
625 loops, best of 3: 67.7 µs per loop
sage: %timeit words.ChristoffelWord(5, 9, algorithm='cf')
625 loops, best of 3: 309 µs per loop
```


For large words, it is much faster than the actual implementation.


```
sage: %timeit words.ChristoffelWord(500, 90001, algorithm='linear')
5 loops, best of 3: 111 ms per loop
sage: %timeit words.ChristoffelWord(500, 90001, algorithm='cf')
125 loops, best of 3: 4 ms per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/8268





---

archive/issue_comments_073185.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-15T00:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73185",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_073186.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-15T00:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73186",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073187.json:
```json
{
    "body": "I tested the improved function. It is indeed much faster, especially when the two prime numbers are big. The code makes sense, all tests passed, and I tried also other values with very big prime numbers: no problem. The doc builds fine too.\n\nI made very minor changes (typos, punctuation, etc.). Positive review.",
    "created_at": "2010-02-24T01:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73187",
    "user": "abmasse"
}
```

I tested the improved function. It is indeed much faster, especially when the two prime numbers are big. The code makes sense, all tests passed, and I tried also other values with very big prime numbers: no problem. The doc builds fine too.

I made very minor changes (typos, punctuation, etc.). Positive review.



---

archive/issue_comments_073188.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-24T01:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73188",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073189.json:
```json
{
    "body": "Changing keywords from \"\" to \"christoffel words\".",
    "created_at": "2010-02-24T01:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73189",
    "user": "abmasse"
}
```

Changing keywords from "" to "christoffel words".



---

archive/issue_comments_073190.json:
```json
{
    "body": "Sorry, forgot two small things, uploading a new patch in a few minutes.",
    "created_at": "2010-02-24T01:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73190",
    "user": "abmasse"
}
```

Sorry, forgot two small things, uploading a new patch in a few minutes.



---

archive/issue_comments_073191.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-24T01:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73191",
    "user": "abmasse"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_073192.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-24T02:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73192",
    "user": "abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073193.json:
```json
{
    "body": "Minor change -- apply on top",
    "created_at": "2010-02-24T02:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73193",
    "user": "abmasse"
}
```

Minor change -- apply on top



---

archive/issue_comments_073194.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-24T02:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73194",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073195.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-24T02:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73195",
    "user": "abmasse"
}
```

Attachment



---

archive/issue_comments_073196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73196",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073197.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8268_speed_up_Christoffel-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8268/trac_8268_speed_up_Christoffel-sl.patch)\n2. [trac_8268_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8268/trac_8268_review-abm.patch)",
    "created_at": "2010-03-02T21:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8268#issuecomment-73197",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8268_speed_up_Christoffel-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8268/trac_8268_speed_up_Christoffel-sl.patch)
2. [trac_8268_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8268/trac_8268_review-abm.patch)
