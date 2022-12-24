# Issue 7198: Free Algebra Iteration, needs review

archive/issues_007198.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  burcin saliola malb\n\nKeywords: free algebra\n\nIteration over free algebra elements and monoid elements\n\nIssue created by migration from https://trac.sagemath.org/ticket/7198\n\n",
    "created_at": "2009-10-13T10:20:32Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Free Algebra Iteration, needs review",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7198",
    "user": "PolyBoRi"
}
```
Assignee: tbd

CC:  burcin saliola malb

Keywords: free algebra

Iteration over free algebra elements and monoid elements

Issue created by migration from https://trac.sagemath.org/ticket/7198





---

archive/issue_comments_059719.json:
```json
{
    "body": "Attachment [free_algebra.patch](tarball://root/attachments/some-uuid/ticket7198/free_algebra.patch) by PolyBoRi created at 2009-10-16 14:00:08",
    "created_at": "2009-10-16T14:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59719",
    "user": "PolyBoRi"
}
```

Attachment [free_algebra.patch](tarball://root/attachments/some-uuid/ticket7198/free_algebra.patch) by PolyBoRi created at 2009-10-16 14:00:08



---

archive/issue_comments_059720.json:
```json
{
    "body": "Attachment [free_algebra.2.patch](tarball://root/attachments/some-uuid/ticket7198/free_algebra.2.patch) by PolyBoRi created at 2009-10-16 14:01:17\n\nnew version free_algebra.2.patch\nredesigns the iterator based on Burcins review.",
    "created_at": "2009-10-16T14:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59720",
    "user": "PolyBoRi"
}
```

Attachment [free_algebra.2.patch](tarball://root/attachments/some-uuid/ticket7198/free_algebra.2.patch) by PolyBoRi created at 2009-10-16 14:01:17

new version free_algebra.2.patch
redesigns the iterator based on Burcins review.



---

archive/issue_comments_059721.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-16T14:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59721",
    "user": "PolyBoRi"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059722.json:
```json
{
    "body": "Attachment [trac_7198-free_algebra_iterator.patch](tarball://root/attachments/some-uuid/ticket7198/trac_7198-free_algebra_iterator.patch) by burcin created at 2009-10-16 20:06:17",
    "created_at": "2009-10-16T20:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59722",
    "user": "burcin"
}
```

Attachment [trac_7198-free_algebra_iterator.patch](tarball://root/attachments/some-uuid/ticket7198/trac_7198-free_algebra_iterator.patch) by burcin created at 2009-10-16 20:06:17



---

archive/issue_comments_059723.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T20:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59723",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059724.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-16T20:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59724",
    "user": "burcin"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_059725.json:
```json
{
    "body": "I uploaded a new patch with minor formatting changes, attachment:trac_7198-free_algebra_iterator.patch.\n\nMike, please apply only attachment:trac_7198-free_algebra_iterator.patch.",
    "created_at": "2009-10-16T20:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59725",
    "user": "burcin"
}
```

I uploaded a new patch with minor formatting changes, attachment:trac_7198-free_algebra_iterator.patch.

Mike, please apply only attachment:trac_7198-free_algebra_iterator.patch.



---

archive/issue_comments_059726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T05:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59726",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059727.json:
```json
{
    "body": "I backed this out of sage-4.2.alpha1.\n\nThis caused problems since there were other free monoid elements that expected to have an __iter__ which returned something different than what was chosen for this patch.  For example, things in the StringMonoid and free monoid elements in sage/crypto.",
    "created_at": "2009-10-19T13:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59727",
    "user": "mhansen"
}
```

I backed this out of sage-4.2.alpha1.

This caused problems since there were other free monoid elements that expected to have an __iter__ which returned something different than what was chosen for this patch.  For example, things in the StringMonoid and free monoid elements in sage/crypto.



---

archive/issue_comments_059728.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2009-10-19T13:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59728",
    "user": "mhansen"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_059729.json:
```json
{
    "body": "fix doctests, add `__iterator__` method to StringMonoidElement",
    "created_at": "2009-12-29T21:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59729",
    "user": "burcin"
}
```

fix doctests, add `__iterator__` method to StringMonoidElement



---

archive/issue_comments_059730.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-29T21:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59730",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059731.json:
```json
{
    "body": "Attachment [trac_7198-string_monoid_element_iterator.patch](tarball://root/attachments/some-uuid/ticket7198/trac_7198-string_monoid_element_iterator.patch) by burcin created at 2009-12-29 21:44:43\n\nI added a new patch which restores the expected iterator interface of `StringMonoidElement`s.\n\nMartin, can you review my changes?\n\nBoth\n* attachment:trac_7198-free_algebra_iterator.patch and\n* attachment:trac_7198-string_monoid_element_iterator.patch\nshould be applied.",
    "created_at": "2009-12-29T21:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59731",
    "user": "burcin"
}
```

Attachment [trac_7198-string_monoid_element_iterator.patch](tarball://root/attachments/some-uuid/ticket7198/trac_7198-string_monoid_element_iterator.patch) by burcin created at 2009-12-29 21:44:43

I added a new patch which restores the expected iterator interface of `StringMonoidElement`s.

Martin, can you review my changes?

Both
* attachment:trac_7198-free_algebra_iterator.patch and
* attachment:trac_7198-string_monoid_element_iterator.patch
should be applied.



---

archive/issue_comments_059732.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T01:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7198#issuecomment-59732",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.
