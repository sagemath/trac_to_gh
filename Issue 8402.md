# Issue 8402: Sanity check for Parent and Elemet

archive/issues_008402.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: Parent, Element, equality, zero, one\n\nHere is the summary of what was decided on [sage=devel](http://groups.google.com/group/sage-devel/t/5d9c32390ffe3c96):\n\n1 - Any Parent or Element must have an equality methods such that\n`self == self` and `self != None`. This is not required for general `SageObject`.\n\n2 - Element construction should be idempotent. More precisely, for any element e within parent P, the equality `P(e) == e` must hold.\n\nCase by case exception such as `RealIntervalField` are possible.\n\n3 - element of a parent in the category `Monoid()` (respectively `CommutativeAdditiveMonoid()`) must have a `__hash__` method,\nwhich may raise an error for mutable element but never on `.one()` (respectively `.zero()`)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8402\n\n",
    "created_at": "2010-02-28T16:45:15Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Sanity check for Parent and Elemet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8402",
    "user": "https://github.com/hivert"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: Parent, Element, equality, zero, one

Here is the summary of what was decided on [sage=devel](http://groups.google.com/group/sage-devel/t/5d9c32390ffe3c96):

1 - Any Parent or Element must have an equality methods such that
`self == self` and `self != None`. This is not required for general `SageObject`.

2 - Element construction should be idempotent. More precisely, for any element e within parent P, the equality `P(e) == e` must hold.

Case by case exception such as `RealIntervalField` are possible.

3 - element of a parent in the category `Monoid()` (respectively `CommutativeAdditiveMonoid()`) must have a `__hash__` method,
which may raise an error for mutable element but never on `.one()` (respectively `.zero()`)

Issue created by migration from https://trac.sagemath.org/ticket/8402





---

archive/issue_comments_075124.json:
```json
{
    "body": "Changing assignee from @nthiery to @hivert.",
    "created_at": "2010-03-02T22:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75124",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @nthiery to @hivert.



---

archive/issue_comments_075125.json:
```json
{
    "body": "I'm preparing some patches on sage-combinat queue. I already caught some bug with it: see #8695.",
    "created_at": "2010-04-17T00:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75125",
    "user": "https://github.com/hivert"
}
```

I'm preparing some patches on sage-combinat queue. I already caught some bug with it: see #8695.



---

archive/issue_comments_075126.json:
```json
{
    "body": "Review in process on the Sage-Combinat queue.\nAll tests pass with sage-4.4-alpha0 (with the other patches under review applied as well)",
    "created_at": "2010-04-18T23:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75126",
    "user": "https://github.com/nthiery"
}
```

Review in process on the Sage-Combinat queue.
All tests pass with sage-4.4-alpha0 (with the other patches under review applied as well)



---

archive/issue_comments_075127.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-19T22:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75127",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075128.json:
```json
{
    "body": "All test still pass, even after my reviewer's patch on the patch queue :-)\n\nFlorent: please double check it. If that's fine, fold everything together, post here and set a positive review!\n\nNote: I ended up throwing away a bit of code in crystals/spins.py, which was the easiest way to fix equality :-)",
    "created_at": "2010-04-19T22:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75128",
    "user": "https://github.com/nthiery"
}
```

All test still pass, even after my reviewer's patch on the patch queue :-)

Florent: please double check it. If that's fine, fold everything together, post here and set a positive review!

Note: I ended up throwing away a bit of code in crystals/spins.py, which was the easiest way to fix equality :-)



---

archive/issue_comments_075129.json:
```json
{
    "body": "> Florent: please double check it. If that's fine, fold everything together, post here and set a positive review!\n\nAll tests passed on sage, I folded and set positive review.",
    "created_at": "2010-04-21T21:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75129",
    "user": "https://github.com/hivert"
}
```

> Florent: please double check it. If that's fine, fold everything together, post here and set a positive review!

All tests passed on sage, I folded and set positive review.



---

archive/issue_comments_075130.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T21:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75130",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075131.json:
```json
{
    "body": "Attachment [trac_8402-categories_missing_test-fh.patch](tarball://root/attachments/some-uuid/ticket8402/trac_8402-categories_missing_test-fh.patch) by @williamstein created at 2010-04-29 05:24:19",
    "created_at": "2010-04-29T05:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75131",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8402-categories_missing_test-fh.patch](tarball://root/attachments/some-uuid/ticket8402/trac_8402-categories_missing_test-fh.patch) by @williamstein created at 2010-04-29 05:24:19



---

archive/issue_events_008587.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T05:24:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8402#event-8587"
}
```



---

archive/issue_comments_075132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8402#issuecomment-75132",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
