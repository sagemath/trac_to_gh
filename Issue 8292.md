# Issue 8292: improvements to eisenstein_series_qexp

archive/issues_008292.json:
```json
{
    "body": "Assignee: craigcitro\n\nThe attached patch makes the following changes to `eisenstein_series_qexp`:\n\n* removes the workaround at the end of the method, since it is no longer needed\n* a few small modifications that speed things up a bit:\n\nBEFORE THE PATCH:\n\n```\nsage: timeit(\"eisenstein_series_qexp(4, 100)\")\n125 loops, best of 3: 6.19 ms per loop\nsage: timeit(\"eisenstein_series_qexp(4, 1000)\")\n5 loops, best of 3: 56.4 ms per loop\nsage: timeit(\"eisenstein_series_qexp(4, 10000)\")\n5 loops, best of 3: 568 ms per loop\nsage: timeit(\"eisenstein_series_qexp(4, 100000)\")\n5 loops, best of 3: 5.84 s per loop\nsage: timeit(\"eisenstein_series_qexp(6, 100)\")\n125 loops, best of 3: 6.26 ms per loop\nsage: timeit(\"eisenstein_series_qexp(6, 1000)\")\n5 loops, best of 3: 57 ms per loop\nsage: timeit(\"eisenstein_series_qexp(6, 10000)\")\n5 loops, best of 3: 575 ms per loop\nsage: timeit(\"eisenstein_series_qexp(6, 100000)\")\n5 loops, best of 3: 5.97 s per loop\nsage: timeit(\"eisenstein_series_qexp(100, 1000)\")\n5 loops, best of 3: 100 ms per loop\nsage: timeit(\"eisenstein_series_qexp(100, 10000)\")\n5 loops, best of 3: 1.21 s per loop\nsage: timeit(\"eisenstein_series_qexp(1000, 10000)\")\n5 loops, best of 3: 12.9 s per loop\n```\n\n\nAFTER THE PATCH:\n\n```\nsage: timeit(\"eisenstein_series_qexp(4, 100)\")\n125 loops, best of 3: 2.21 ms per loop\nsage: timeit(\"eisenstein_series_qexp(4, 1000)\")\n25 loops, best of 3: 20.5 ms per loop\nsage: timeit(\"eisenstein_series_qexp(4, 10000)\")\n5 loops, best of 3: 220 ms per loop\nsage: timeit(\"eisenstein_series_qexp(4, 100000)\")\n5 loops, best of 3: 2.41 s per loop\nsage: timeit(\"eisenstein_series_qexp(6, 100)\")\n125 loops, best of 3: 2.24 ms per loop\nsage: timeit(\"eisenstein_series_qexp(6, 1000)\")\n25 loops, best of 3: 21 ms per loop\nsage: timeit(\"eisenstein_series_qexp(6, 10000)\")\n5 loops, best of 3: 223 ms per loop\nsage: timeit(\"eisenstein_series_qexp(6, 100000)\")\n5 loops, best of 3: 2.54 s per loop\nsage: timeit(\"eisenstein_series_qexp(100, 1000)\")\n5 loops, best of 3: 50.6 ms per loop\nsage: timeit(\"eisenstein_series_qexp(100, 10000)\")\n5 loops, best of 3: 641 ms per loop\nsage: timeit(\"eisenstein_series_qexp(1000, 10000)\")\n5 loops, best of 3: 8.62 s per loop\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8292\n\n",
    "created_at": "2010-02-17T11:56:01Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "title": "improvements to eisenstein_series_qexp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8292",
    "user": "AlexGhitza"
}
```
Assignee: craigcitro

The attached patch makes the following changes to `eisenstein_series_qexp`:

* removes the workaround at the end of the method, since it is no longer needed
* a few small modifications that speed things up a bit:

BEFORE THE PATCH:

```
sage: timeit("eisenstein_series_qexp(4, 100)")
125 loops, best of 3: 6.19 ms per loop
sage: timeit("eisenstein_series_qexp(4, 1000)")
5 loops, best of 3: 56.4 ms per loop
sage: timeit("eisenstein_series_qexp(4, 10000)")
5 loops, best of 3: 568 ms per loop
sage: timeit("eisenstein_series_qexp(4, 100000)")
5 loops, best of 3: 5.84 s per loop
sage: timeit("eisenstein_series_qexp(6, 100)")
125 loops, best of 3: 6.26 ms per loop
sage: timeit("eisenstein_series_qexp(6, 1000)")
5 loops, best of 3: 57 ms per loop
sage: timeit("eisenstein_series_qexp(6, 10000)")
5 loops, best of 3: 575 ms per loop
sage: timeit("eisenstein_series_qexp(6, 100000)")
5 loops, best of 3: 5.97 s per loop
sage: timeit("eisenstein_series_qexp(100, 1000)")
5 loops, best of 3: 100 ms per loop
sage: timeit("eisenstein_series_qexp(100, 10000)")
5 loops, best of 3: 1.21 s per loop
sage: timeit("eisenstein_series_qexp(1000, 10000)")
5 loops, best of 3: 12.9 s per loop
```


AFTER THE PATCH:

```
sage: timeit("eisenstein_series_qexp(4, 100)")
125 loops, best of 3: 2.21 ms per loop
sage: timeit("eisenstein_series_qexp(4, 1000)")
25 loops, best of 3: 20.5 ms per loop
sage: timeit("eisenstein_series_qexp(4, 10000)")
5 loops, best of 3: 220 ms per loop
sage: timeit("eisenstein_series_qexp(4, 100000)")
5 loops, best of 3: 2.41 s per loop
sage: timeit("eisenstein_series_qexp(6, 100)")
125 loops, best of 3: 2.24 ms per loop
sage: timeit("eisenstein_series_qexp(6, 1000)")
25 loops, best of 3: 21 ms per loop
sage: timeit("eisenstein_series_qexp(6, 10000)")
5 loops, best of 3: 223 ms per loop
sage: timeit("eisenstein_series_qexp(6, 100000)")
5 loops, best of 3: 2.54 s per loop
sage: timeit("eisenstein_series_qexp(100, 1000)")
5 loops, best of 3: 50.6 ms per loop
sage: timeit("eisenstein_series_qexp(100, 10000)")
5 loops, best of 3: 641 ms per loop
sage: timeit("eisenstein_series_qexp(1000, 10000)")
5 loops, best of 3: 8.62 s per loop
```



Issue created by migration from https://trac.sagemath.org/ticket/8292





---

archive/issue_comments_073466.json:
```json
{
    "body": "Attachment [trac_8292.patch](tarball://root/attachments/some-uuid/ticket8292/trac_8292.patch) by AlexGhitza created at 2010-02-17 12:02:15",
    "created_at": "2010-02-17T12:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73466",
    "user": "AlexGhitza"
}
```

Attachment [trac_8292.patch](tarball://root/attachments/some-uuid/ticket8292/trac_8292.patch) by AlexGhitza created at 2010-02-17 12:02:15



---

archive/issue_comments_073467.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-11-05T15:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73467",
    "user": "mraum"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_073468.json:
```json
{
    "body": "This is already covered by the cythonification of the Eisenstein series. I propose we close this ticket. Any objections, Alex?",
    "created_at": "2010-11-05T15:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73468",
    "user": "mraum"
}
```

This is already covered by the cythonification of the Eisenstein series. I propose we close this ticket. Any objections, Alex?



---

archive/issue_comments_073469.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-05T20:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73469",
    "user": "AlexGhitza"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_073470.json:
```json
{
    "body": "That sounds right.\n\nI'm marking this as \"positive review\" so it gets picked up.\n\nTo the release manager: please close this, as the issue has already been addressed by #6671.",
    "created_at": "2010-11-05T20:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73470",
    "user": "AlexGhitza"
}
```

That sounds right.

I'm marking this as "positive review" so it gets picked up.

To the release manager: please close this, as the issue has already been addressed by #6671.



---

archive/issue_comments_073471.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-05T20:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73471",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073472.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-07T10:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8292#issuecomment-73472",
    "user": "jdemeyer"
}
```

Resolution: duplicate
