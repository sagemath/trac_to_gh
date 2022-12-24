# Issue 9596: is_totally_positive should give proven output

archive/issues_009596.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  mstreng\n\nKeywords: real_embeddings is_totally_positive algebraic real numbers proven output\n\nThe number field function `real_embeddings` gives embeddings into finite precision real numbers, hence cannot be used for functions whose values are supposed to be proven (like `is_totally_positive`).\n\nA patch for this ticket should correct the usage of `real_embeddings` and give `real_embeddings` a warning in the documentation string.\n\nFor more info, see\n\n* [http://groups.google.com/group/sage-nt/browse_thread/thread/fb34ad5be1bbe5fd](http://groups.google.com/group/sage-nt/browse_thread/thread/fb34ad5be1bbe5fd) and\n* [http://groups.google.com/group/sage-nt/browse_thread/thread/ce2a4b9555618f99/fbed7f10a944af48](http://groups.google.com/group/sage-nt/browse_thread/thread/ce2a4b9555618f99/fbed7f10a944af48)\n\n\n```\nsage: a = 30122754096401; b = 21300003689580\nsage: (a/b)^2 > 2\nTrue\nsage: K.<sqrt2> = QuadraticField(2)\nsage: (a/b+sqrt2).is_totally_positive()\nFalse\n```\n\nBoth should be `True`.\n\nI'm creating a patch right now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9596\n\n",
    "created_at": "2010-07-25T12:45:28Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "is_totally_positive should give proven output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9596",
    "user": "mstreng"
}
```
Assignee: davidloeffler

CC:  mstreng

Keywords: real_embeddings is_totally_positive algebraic real numbers proven output

The number field function `real_embeddings` gives embeddings into finite precision real numbers, hence cannot be used for functions whose values are supposed to be proven (like `is_totally_positive`).

A patch for this ticket should correct the usage of `real_embeddings` and give `real_embeddings` a warning in the documentation string.

For more info, see

* [http://groups.google.com/group/sage-nt/browse_thread/thread/fb34ad5be1bbe5fd](http://groups.google.com/group/sage-nt/browse_thread/thread/fb34ad5be1bbe5fd) and
* [http://groups.google.com/group/sage-nt/browse_thread/thread/ce2a4b9555618f99/fbed7f10a944af48](http://groups.google.com/group/sage-nt/browse_thread/thread/ce2a4b9555618f99/fbed7f10a944af48)


```
sage: a = 30122754096401; b = 21300003689580
sage: (a/b)^2 > 2
True
sage: K.<sqrt2> = QuadraticField(2)
sage: (a/b+sqrt2).is_totally_positive()
False
```

Both should be `True`.

I'm creating a patch right now.

Issue created by migration from https://trac.sagemath.org/ticket/9596





---

archive/issue_comments_092840.json:
```json
{
    "body": "Attachment [trac_9596_is_totally_positive.patch](tarball://root/attachments/some-uuid/ticket9596/trac_9596_is_totally_positive.patch) by mstreng created at 2010-07-30 12:14:55",
    "created_at": "2010-07-30T12:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9596#issuecomment-92840",
    "user": "mstreng"
}
```

Attachment [trac_9596_is_totally_positive.patch](tarball://root/attachments/some-uuid/ticket9596/trac_9596_is_totally_positive.patch) by mstreng created at 2010-07-30 12:14:55



---

archive/issue_comments_092841.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-30T12:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9596#issuecomment-92841",
    "user": "mstreng"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T09:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9596#issuecomment-92842",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092843.json:
```json
{
    "body": "Changes look sensible, and all doctests in `sage/rings/number_field` pass. Positive review.",
    "created_at": "2010-09-22T09:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9596#issuecomment-92843",
    "user": "davidloeffler"
}
```

Changes look sensible, and all doctests in `sage/rings/number_field` pass. Positive review.



---

archive/issue_comments_092844.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9596#issuecomment-92844",
    "user": "mpatel"
}
```

Resolution: fixed
