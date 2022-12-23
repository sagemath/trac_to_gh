# Issue 9658: mpz_clear->mpq_clear (typo)

archive/issues_009658.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  robertwb\n\nWe can't include vector_rational_sparse_c.pxi in a cython file because of a typo.  This patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9658\n\n",
    "created_at": "2010-08-01T05:00:21Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "mpz_clear->mpq_clear (typo)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9658",
    "user": "jason"
}
```
Assignee: jason, was

CC:  robertwb

We can't include vector_rational_sparse_c.pxi in a cython file because of a typo.  This patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/9658





---

archive/issue_comments_093746.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-01T05:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93746",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093747.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-01T05:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93747",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_093748.json:
```json
{
    "body": "I thought the typo prevented someone from loading the file, but it seems like I can include it with the typo.  Regardless, it is still pretty clear it is a typo (look at the declaration of z).",
    "created_at": "2010-08-01T05:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93748",
    "user": "jason"
}
```

I thought the typo prevented someone from loading the file, but it seems like I can include it with the typo.  Regardless, it is still pretty clear it is a typo (look at the declaration of z).



---

archive/issue_comments_093749.json:
```json
{
    "body": "robert, or someone: ping about a review.  This is really a trivial typo fix.",
    "created_at": "2010-09-28T20:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93749",
    "user": "jason"
}
```

robert, or someone: ping about a review.  This is really a trivial typo fix.



---

archive/issue_comments_093750.json:
```json
{
    "body": "Obviously.",
    "created_at": "2010-09-28T21:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93750",
    "user": "leif"
}
```

Obviously.



---

archive/issue_comments_093751.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T21:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93751",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093752.json:
```json
{
    "body": "P.S.: Applied to Sage 4.6.alpha1 without problems.",
    "created_at": "2010-09-28T22:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93752",
    "user": "leif"
}
```

P.S.: Applied to Sage 4.6.alpha1 without problems.



---

archive/issue_comments_093753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93753",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_093754.json:
```json
{
    "body": "Why did this even compile before? Yes, the fix is good.",
    "created_at": "2010-09-29T07:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93754",
    "user": "robertwb"
}
```

Why did this even compile before? Yes, the fix is good.
