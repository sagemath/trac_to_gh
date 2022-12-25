# Issue 9658: mpz_clear->mpq_clear (typo)

archive/issues_009658.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @robertwb\n\nWe can't include vector_rational_sparse_c.pxi in a cython file because of a typo.  This patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9658\n\n",
    "created_at": "2010-08-01T05:00:21Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "mpz_clear->mpq_clear (typo)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9658",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @robertwb

We can't include vector_rational_sparse_c.pxi in a cython file because of a typo.  This patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/9658





---

archive/issue_comments_093589.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-01T05:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93589",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093590.json:
```json
{
    "body": "Attachment [trac-9658-mpz-typo.patch](tarball://root/attachments/some-uuid/ticket9658/trac-9658-mpz-typo.patch) by @jasongrout created at 2010-08-01 05:02:40",
    "created_at": "2010-08-01T05:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93590",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9658-mpz-typo.patch](tarball://root/attachments/some-uuid/ticket9658/trac-9658-mpz-typo.patch) by @jasongrout created at 2010-08-01 05:02:40



---

archive/issue_comments_093591.json:
```json
{
    "body": "I thought the typo prevented someone from loading the file, but it seems like I can include it with the typo.  Regardless, it is still pretty clear it is a typo (look at the declaration of z).",
    "created_at": "2010-08-01T05:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93591",
    "user": "https://github.com/jasongrout"
}
```

I thought the typo prevented someone from loading the file, but it seems like I can include it with the typo.  Regardless, it is still pretty clear it is a typo (look at the declaration of z).



---

archive/issue_comments_093592.json:
```json
{
    "body": "robert, or someone: ping about a review.  This is really a trivial typo fix.",
    "created_at": "2010-09-28T20:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93592",
    "user": "https://github.com/jasongrout"
}
```

robert, or someone: ping about a review.  This is really a trivial typo fix.



---

archive/issue_comments_093593.json:
```json
{
    "body": "Obviously.",
    "created_at": "2010-09-28T21:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93593",
    "user": "https://github.com/nexttime"
}
```

Obviously.



---

archive/issue_comments_093594.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T21:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93594",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093595.json:
```json
{
    "body": "P.S.: Applied to Sage 4.6.alpha1 without problems.",
    "created_at": "2010-09-28T22:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93595",
    "user": "https://github.com/nexttime"
}
```

P.S.: Applied to Sage 4.6.alpha1 without problems.



---

archive/issue_comments_093596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93596",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024095.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T04:23:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9658#event-24095"
}
```



---

archive/issue_comments_093597.json:
```json
{
    "body": "Why did this even compile before? Yes, the fix is good.",
    "created_at": "2010-09-29T07:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9658#issuecomment-93597",
    "user": "https://github.com/robertwb"
}
```

Why did this even compile before? Yes, the fix is good.
