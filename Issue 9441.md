# Issue 9441: Atkin-Lehner operators for Cremona modular symbols

archive/issues_009441.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @williamstein\n\nKeywords: modular symbols\n\nThe code in sage/libs/cremona wraps some of Cremona's modular symbols code, including Hecke operators.  The wrapping function incorrectly assumes that the function heckeop(p) only works for primes p not dividing the level, when in fact it works fine for primes dividing the level, in that case returning the matrix of the Atkin-Lehner involution.\n\nThe patch remedies this, with some tests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9441\n\n",
    "created_at": "2010-07-06T20:34:58Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Atkin-Lehner operators for Cremona modular symbols",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9441",
    "user": "@JohnCremona"
}
```
Assignee: @craigcitro

CC:  @williamstein

Keywords: modular symbols

The code in sage/libs/cremona wraps some of Cremona's modular symbols code, including Hecke operators.  The wrapping function incorrectly assumes that the function heckeop(p) only works for primes p not dividing the level, when in fact it works fine for primes dividing the level, in that case returning the matrix of the Atkin-Lehner involution.

The patch remedies this, with some tests.

Issue created by migration from https://trac.sagemath.org/ticket/9441





---

archive/issue_comments_090462.json:
```json
{
    "body": "Attachment [trac_9441-atkin-lehner.patch](tarball://root/attachments/some-uuid/ticket9441/trac_9441-atkin-lehner.patch) by @JohnCremona created at 2010-07-06 20:37:04\n\nApplies to 4.5.alpha3",
    "created_at": "2010-07-06T20:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9441#issuecomment-90462",
    "user": "@JohnCremona"
}
```

Attachment [trac_9441-atkin-lehner.patch](tarball://root/attachments/some-uuid/ticket9441/trac_9441-atkin-lehner.patch) by @JohnCremona created at 2010-07-06 20:37:04

Applies to 4.5.alpha3



---

archive/issue_comments_090463.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T20:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9441#issuecomment-90463",
    "user": "@JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090464.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-17T12:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9441#issuecomment-90464",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090465.json:
```json
{
    "body": "Looks good to me! Applies, passes tests.",
    "created_at": "2010-07-17T12:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9441#issuecomment-90465",
    "user": "@rlmill"
}
```

Looks good to me! Applies, passes tests.



---

archive/issue_comments_090466.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9441#issuecomment-90466",
    "user": "@qed777"
}
```

Resolution: fixed
