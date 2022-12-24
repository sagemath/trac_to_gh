# Issue 8543: EmptySet is Back !

archive/issues_008543.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  nborie sage-combinat\n\nKeywords: empty set, Testsuite\n\nThere is currently no way to have an empty set which pass the category tests. Indeed the current specification says: for any set `S` there must be a method `S.an_element()` which returns an actual element `x` such that `x in S`:\n\n```\nan_element = self.an_element()\ntester.assert_(an_element in self, \"self.an_element() is not in self\")\n```\n\nThis tests should allows `S` to be empty.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8543\n\n",
    "created_at": "2010-03-15T17:27:20Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "title": "EmptySet is Back !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8543",
    "user": "hivert"
}
```
Assignee: hivert

CC:  nborie sage-combinat

Keywords: empty set, Testsuite

There is currently no way to have an empty set which pass the category tests. Indeed the current specification says: for any set `S` there must be a method `S.an_element()` which returns an actual element `x` such that `x in S`:

```
an_element = self.an_element()
tester.assert_(an_element in self, "self.an_element() is not in self")
```

This tests should allows `S` to be empty.

Issue created by migration from https://trac.sagemath.org/ticket/8543





---

archive/issue_comments_077242.json:
```json
{
    "body": "Attachment [trac_8543-empty_set_categories-fh.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-fh.patch) by hivert created at 2010-03-23 09:48:06",
    "created_at": "2010-03-23T09:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77242",
    "user": "hivert"
}
```

Attachment [trac_8543-empty_set_categories-fh.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-fh.patch) by hivert created at 2010-03-23 09:48:06



---

archive/issue_comments_077243.json:
```json
{
    "body": "Changing keywords from \"empty set, Testsuite\" to \"empty set, Testsuite, EmptySetError\".",
    "created_at": "2010-03-23T09:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77243",
    "user": "hivert"
}
```

Changing keywords from "empty set, Testsuite" to "empty set, Testsuite, EmptySetError".



---

archive/issue_comments_077244.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T09:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77244",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077245.json:
```json
{
    "body": "Patches from #8519 your patch apply fine on 4.3.4\nAll tests passed for each touched files, doc is OK too. This another empty problem is fixed...\n\nThanks for fixing this!\n\nI give this patch a positive review...",
    "created_at": "2010-03-23T11:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77245",
    "user": "nborie"
}
```

Patches from #8519 your patch apply fine on 4.3.4
All tests passed for each touched files, doc is OK too. This another empty problem is fixed...

Thanks for fixing this!

I give this patch a positive review...



---

archive/issue_comments_077246.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-23T11:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77246",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077247.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-16T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77247",
    "user": "nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077248.json:
```json
{
    "body": "Nicolas: thanks for your review!\n\nFlorent: I made a quick reviewer patch fixing some trivial things. Please double check, and set back the positive review!",
    "created_at": "2010-04-16T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77248",
    "user": "nthiery"
}
```

Nicolas: thanks for your review!

Florent: I made a quick reviewer patch fixing some trivial things. Please double check, and set back the positive review!



---

archive/issue_comments_077249.json:
```json
{
    "body": "Attachment [trac_8543-empty_set_categories-review-nt.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-review-nt.patch) by nthiery created at 2010-04-16 21:15:05",
    "created_at": "2010-04-16T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77249",
    "user": "nthiery"
}
```

Attachment [trac_8543-empty_set_categories-review-nt.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-review-nt.patch) by nthiery created at 2010-04-16 21:15:05



---

archive/issue_comments_077250.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-16T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77250",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077251.json:
```json
{
    "body": "The new changes are good to me => positive review.",
    "created_at": "2010-04-17T00:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77251",
    "user": "hivert"
}
```

The new changes are good to me => positive review.



---

archive/issue_comments_077252.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T00:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77252",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077253.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8543-empty_set_categories-fh.patch\n- trac_8543-empty_set_categories-review-nt.patch",
    "created_at": "2010-04-17T02:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77253",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8543-empty_set_categories-fh.patch
- trac_8543-empty_set_categories-review-nt.patch



---

archive/issue_comments_077254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-17T02:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77254",
    "user": "jhpalmieri"
}
```

Resolution: fixed
