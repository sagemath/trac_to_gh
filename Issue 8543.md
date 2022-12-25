# Issue 8543: EmptySet is Back !

archive/issues_008543.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  nborie sage-combinat\n\nKeywords: empty set, Testsuite\n\nThere is currently no way to have an empty set which pass the category tests. Indeed the current specification says: for any set `S` there must be a method `S.an_element()` which returns an actual element `x` such that `x in S`:\n\n```\nan_element = self.an_element()\ntester.assert_(an_element in self, \"self.an_element() is not in self\")\n```\n\nThis tests should allows `S` to be empty.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8543\n\n",
    "created_at": "2010-03-15T17:27:20Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "EmptySet is Back !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8543",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

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

archive/issue_comments_077115.json:
```json
{
    "body": "Attachment [trac_8543-empty_set_categories-fh.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-fh.patch) by @hivert created at 2010-03-23 09:48:06",
    "created_at": "2010-03-23T09:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77115",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8543-empty_set_categories-fh.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-fh.patch) by @hivert created at 2010-03-23 09:48:06



---

archive/issue_comments_077116.json:
```json
{
    "body": "Changing keywords from \"empty set, Testsuite\" to \"empty set, Testsuite, EmptySetError\".",
    "created_at": "2010-03-23T09:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77116",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "empty set, Testsuite" to "empty set, Testsuite, EmptySetError".



---

archive/issue_comments_077117.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T09:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77117",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077118.json:
```json
{
    "body": "Patches from #8519 your patch apply fine on 4.3.4\nAll tests passed for each touched files, doc is OK too. This another empty problem is fixed...\n\nThanks for fixing this!\n\nI give this patch a positive review...",
    "created_at": "2010-03-23T11:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77118",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Patches from #8519 your patch apply fine on 4.3.4
All tests passed for each touched files, doc is OK too. This another empty problem is fixed...

Thanks for fixing this!

I give this patch a positive review...



---

archive/issue_comments_077119.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-23T11:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77119",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077120.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-16T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77120",
    "user": "https://github.com/nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_077121.json:
```json
{
    "body": "Nicolas: thanks for your review!\n\nFlorent: I made a quick reviewer patch fixing some trivial things. Please double check, and set back the positive review!",
    "created_at": "2010-04-16T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77121",
    "user": "https://github.com/nthiery"
}
```

Nicolas: thanks for your review!

Florent: I made a quick reviewer patch fixing some trivial things. Please double check, and set back the positive review!



---

archive/issue_comments_077122.json:
```json
{
    "body": "Attachment [trac_8543-empty_set_categories-review-nt.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-review-nt.patch) by @nthiery created at 2010-04-16 21:15:05",
    "created_at": "2010-04-16T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77122",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8543-empty_set_categories-review-nt.patch](tarball://root/attachments/some-uuid/ticket8543/trac_8543-empty_set_categories-review-nt.patch) by @nthiery created at 2010-04-16 21:15:05



---

archive/issue_comments_077123.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-16T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77123",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077124.json:
```json
{
    "body": "The new changes are good to me => positive review.",
    "created_at": "2010-04-17T00:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77124",
    "user": "https://github.com/hivert"
}
```

The new changes are good to me => positive review.



---

archive/issue_comments_077125.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T00:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77125",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008724.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-17T02:50:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8543#event-8724"
}
```



---

archive/issue_comments_077126.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8543-empty_set_categories-fh.patch\n- trac_8543-empty_set_categories-review-nt.patch",
    "created_at": "2010-04-17T02:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77126",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8543-empty_set_categories-fh.patch
- trac_8543-empty_set_categories-review-nt.patch



---

archive/issue_comments_077127.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-17T02:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8543#issuecomment-77127",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
