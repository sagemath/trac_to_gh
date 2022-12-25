# Issue 8742: Lazy format strings

archive/issues_008742.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  @nthiery\n\nKeywords: lazy format strings\n\nThe class `LazyFormat` allows to create format strings which calls their argument's `__repr__` only if needed. Otherwise it behaves as usual format string.\n\nThis is useful tor speeding up tests suites. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8742\n\n",
    "created_at": "2010-04-21T19:50:06Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Lazy format strings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8742",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  @nthiery

Keywords: lazy format strings

The class `LazyFormat` allows to create format strings which calls their argument's `__repr__` only if needed. Otherwise it behaves as usual format string.

This is useful tor speeding up tests suites. 

Issue created by migration from https://trac.sagemath.org/ticket/8742





---

archive/issue_comments_079855.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-21T19:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8742#issuecomment-79855",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079856.json:
```json
{
    "body": "I forgot to add the doc in the reference manual, I just reuploaded a version with it.",
    "created_at": "2010-04-21T22:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8742#issuecomment-79856",
    "user": "https://github.com/hivert"
}
```

I forgot to add the doc in the reference manual, I just reuploaded a version with it.



---

archive/issue_comments_079857.json:
```json
{
    "body": "Attachment [trac_8742-lazy_format-fh.patch](tarball://root/attachments/some-uuid/ticket8742/trac_8742-lazy_format-fh.patch) by @hivert created at 2010-04-22 19:41:22\n\nThe former patch made sphinx to raise a warning. This is now fixed.",
    "created_at": "2010-04-22T19:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8742#issuecomment-79857",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8742-lazy_format-fh.patch](tarball://root/attachments/some-uuid/ticket8742/trac_8742-lazy_format-fh.patch) by @hivert created at 2010-04-22 19:41:22

The former patch made sphinx to raise a warning. This is now fixed.



---

archive/issue_comments_079858.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T17:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8742#issuecomment-79858",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079859.json:
```json
{
    "body": "Attachment [trac_8742-lazy_format-review-nt.patch](tarball://root/attachments/some-uuid/ticket8742/trac_8742-lazy_format-review-nt.patch) by @hivert created at 2010-05-12 17:37:58\n\nThis is an extract from a private mail from Nicolas Thi\u00e9ry:\n\n```\n - trac_8742-lazy_format-fh.patch\n   trac_8742-lazy_format-review-nt.patch\n\n   Si mon patch de review est ok et les tests passent, c'est tout bon!\n```\nTranslation: If my review patch is ok and if the tests pass, this is all good.\n\nI'm ok with Nicolas review patch. I Put a positive review.",
    "created_at": "2010-05-12T17:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8742#issuecomment-79859",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8742-lazy_format-review-nt.patch](tarball://root/attachments/some-uuid/ticket8742/trac_8742-lazy_format-review-nt.patch) by @hivert created at 2010-05-12 17:37:58

This is an extract from a private mail from Nicolas Thiéry:

```
 - trac_8742-lazy_format-fh.patch
   trac_8742-lazy_format-review-nt.patch

   Si mon patch de review est ok et les tests passent, c'est tout bon!
```
Translation: If my review patch is ok and if the tests pass, this is all good.

I'm ok with Nicolas review patch. I Put a positive review.



---

archive/issue_comments_079860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T21:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8742#issuecomment-79860",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021246.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T21:50:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8742",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8742#event-21246"
}
```
