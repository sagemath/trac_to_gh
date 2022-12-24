# Issue 8573: prod(primes(190)).divisors() crashes

archive/issues_008573.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: product primes 190\n\nExactly what the title says...The divisors of the product of all primes under 190 crashes sage.\n\nThe number has about 74 digits I believe, and finding the divisors of a similar 74 digit prime works.\n\nI believe the crash is due to the fact that the number that comes out of prod(primes(190)) has over 4 million divisors.\n\nThe I probably selected the wrong component, by the way, I chose factorization, but really I'm talking about divisors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8573\n\n",
    "created_at": "2010-03-21T21:31:02Z",
    "labels": [
        "factorization",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "prod(primes(190)).divisors() crashes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8573",
    "user": "asdjughewou9474388"
}
```
Assignee: tbd

Keywords: product primes 190

Exactly what the title says...The divisors of the product of all primes under 190 crashes sage.

The number has about 74 digits I believe, and finding the divisors of a similar 74 digit prime works.

I believe the crash is due to the fact that the number that comes out of prod(primes(190)) has over 4 million divisors.

The I probably selected the wrong component, by the way, I chose factorization, but really I'm talking about divisors.

Issue created by migration from https://trac.sagemath.org/ticket/8573





---

archive/issue_comments_077641.json:
```json
{
    "body": "Changing keywords from \"product primes 190\" to \"product primes 190 divisors\".",
    "created_at": "2010-03-21T21:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77641",
    "user": "asdjughewou9474388"
}
```

Changing keywords from "product primes 190" to "product primes 190 divisors".



---

archive/issue_comments_077642.json:
```json
{
    "body": "It now (6.1) fails with a `MemoryError`, which looks reasonable to me.",
    "created_at": "2014-02-02T11:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77642",
    "user": "mmezzarobba"
}
```

It now (6.1) fails with a `MemoryError`, which looks reasonable to me.



---

archive/issue_comments_077643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-02T11:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77643",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077644.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-03T10:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77644",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077645.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-02-03T10:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77645",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077646.json:
```json
{
    "body": "Changing keywords from \"product primes 190 divisors\" to \"integer divisors\".",
    "created_at": "2014-02-03T10:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77646",
    "user": "jdemeyer"
}
```

Changing keywords from "product primes 190 divisors" to "integer divisors".



---

archive/issue_comments_077647.json:
```json
{
    "body": "Changing component from factorization to basic arithmetic.",
    "created_at": "2014-02-03T10:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77647",
    "user": "jdemeyer"
}
```

Changing component from factorization to basic arithmetic.



---

archive/issue_comments_077648.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-02-03T14:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77648",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077649.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-02-05T09:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77649",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_077650.json:
```json
{
    "body": "Rebased on 6.2.beta3. Tests OK --long in rings/. Seems to be an uncomplicated change.\n----\nNew commits:",
    "created_at": "2014-03-10T10:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77650",
    "user": "rws"
}
```

Rebased on 6.2.beta3. Tests OK --long in rings/. Seems to be an uncomplicated change.
----
New commits:



---

archive/issue_comments_077651.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-10T10:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77651",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077652.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-03-12T08:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77652",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_077653.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-03-12T08:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77653",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_077654.json:
```json
{
    "body": "Why change the branch all the time?\n----\nNew commits:",
    "created_at": "2014-03-12T10:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77654",
    "user": "jdemeyer"
}
```

Why change the branch all the time?
----
New commits:



---

archive/issue_comments_077655.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-12T10:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77655",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077656.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> Why change the branch all the time?\n\nhttps://groups.google.com/forum/#!topic/sage-devel/sTLT83d1g14",
    "created_at": "2014-03-12T10:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77656",
    "user": "rws"
}
```

Replying to [comment:13 jdemeyer]:
> Why change the branch all the time?

https://groups.google.com/forum/#!topic/sage-devel/sTLT83d1g14



---

archive/issue_comments_077657.json:
```json
{
    "body": "In this ticket, you made no changes, so there is no reason at all to commit/push anything. I'm not complaining about changing the branch, I am complaining about changing the branch *without making any changes*.",
    "created_at": "2014-03-12T12:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77657",
    "user": "jdemeyer"
}
```

In this ticket, you made no changes, so there is no reason at all to commit/push anything. I'm not complaining about changing the branch, I am complaining about changing the branch *without making any changes*.



---

archive/issue_comments_077658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-13T02:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8573#issuecomment-77658",
    "user": "vbraun"
}
```

Resolution: fixed
