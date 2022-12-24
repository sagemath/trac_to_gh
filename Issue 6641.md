# Issue 6641: switch the poset antichains method to use GenericBacktracker and add antichains_iterator.

archive/issues_006641.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  @fchapoton\n\nThe current implementation of antichains must construct the complete set of antichains, but it can be done via an iterator (using the `GenericBacktracker` class).\n\nI have a patch that I will post shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6641\n\n",
    "created_at": "2009-07-27T15:01:27Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "switch the poset antichains method to use GenericBacktracker and add antichains_iterator.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6641",
    "user": "@saliola"
}
```
Assignee: @saliola

CC:  @fchapoton

The current implementation of antichains must construct the complete set of antichains, but it can be done via an iterator (using the `GenericBacktracker` class).

I have a patch that I will post shortly.

Issue created by migration from https://trac.sagemath.org/ticket/6641





---

archive/issue_comments_054444.json:
```json
{
    "body": "Attachment [trac_6641-poset_antichains_backtracker.patch](tarball://root/attachments/some-uuid/ticket6641/trac_6641-poset_antichains_backtracker.patch) by @saliola created at 2009-07-27 15:29:57",
    "created_at": "2009-07-27T15:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54444",
    "user": "@saliola"
}
```

Attachment [trac_6641-poset_antichains_backtracker.patch](tarball://root/attachments/some-uuid/ticket6641/trac_6641-poset_antichains_backtracker.patch) by @saliola created at 2009-07-27 15:29:57



---

archive/issue_comments_054445.json:
```json
{
    "body": "Thanks to Dan Drake for teaching me how to use the backtracker.",
    "created_at": "2009-07-27T15:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54445",
    "user": "@saliola"
}
```

Thanks to Dan Drake for teaching me how to use the backtracker.



---

archive/issue_comments_054446.json:
```json
{
    "body": "Attachment [trac_6641-poset_antichains_backtracker-part2.patch](tarball://root/attachments/some-uuid/ticket6641/trac_6641-poset_antichains_backtracker-part2.patch) by @saliola created at 2009-07-27 19:56:06",
    "created_at": "2009-07-27T19:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54446",
    "user": "@saliola"
}
```

Attachment [trac_6641-poset_antichains_backtracker-part2.patch](tarball://root/attachments/some-uuid/ticket6641/trac_6641-poset_antichains_backtracker-part2.patch) by @saliola created at 2009-07-27 19:56:06



---

archive/issue_comments_054447.json:
```json
{
    "body": "Changing type from task to enhancement.",
    "created_at": "2009-09-16T02:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54447",
    "user": "@dandrake"
}
```

Changing type from task to enhancement.



---

archive/issue_comments_054448.json:
```json
{
    "body": "I like using the backtracker code, and I'm the one who showed it to Franco and said it was all great and stuff...but I think this is \"needs work\". I've done a bunch of testing, and this patch is consistently 30-50% slower than the current code. For some things, it was only about 15-20% slower, but mostly it's 30-50%. Here's what I tested:\n\n* antichain posets 5 and 10 elements\n* symmetric group Bruhat order 3, 4\n* chains with 10-14 elements\n* random posets: 100 elements and 500 elements, with probabilities .05, .2, and .5. The .sobj files for these are in my home directory on sage.math.\n\nA slowdown might be acceptable if there's a big win in code clarity, memory use, ease of doctesting, etc, but I'm not sure we get any of that, except maybe the memory usage. Thoughts?",
    "created_at": "2009-09-16T02:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54448",
    "user": "@dandrake"
}
```

I like using the backtracker code, and I'm the one who showed it to Franco and said it was all great and stuff...but I think this is "needs work". I've done a bunch of testing, and this patch is consistently 30-50% slower than the current code. For some things, it was only about 15-20% slower, but mostly it's 30-50%. Here's what I tested:

* antichain posets 5 and 10 elements
* symmetric group Bruhat order 3, 4
* chains with 10-14 elements
* random posets: 100 elements and 500 elements, with probabilities .05, .2, and .5. The .sobj files for these are in my home directory on sage.math.

A slowdown might be acceptable if there's a big win in code clarity, memory use, ease of doctesting, etc, but I'm not sure we get any of that, except maybe the memory usage. Thoughts?



---

archive/issue_comments_054449.json:
```json
{
    "body": "Thanks for running the timings. That is a significant difference. I agree that this should be marked as needs work.\n\nFor the record, I took the recursive algorithm that is currently used and did very minor adaptations to be able to use it with the backtracker code. So the backtracker code seems to be adding a lot of overhead in this case. The best way to proceed would be to better adapt the recursive construction.\n\nThe main advantage to using the backtracker code is that you get an iterator instead of a list.",
    "created_at": "2009-09-16T13:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54449",
    "user": "@saliola"
}
```

Thanks for running the timings. That is a significant difference. I agree that this should be marked as needs work.

For the record, I took the recursive algorithm that is currently used and did very minor adaptations to be able to use it with the backtracker code. So the backtracker code seems to be adding a lot of overhead in this case. The best way to proceed would be to better adapt the recursive construction.

The main advantage to using the backtracker code is that you get an iterator instead of a list.



---

archive/issue_comments_054450.json:
```json
{
    "body": "I had to rebase the patch which now depends on #8735. I reuploaded it from sage-combinat queue.\n\nFlorent",
    "created_at": "2010-04-21T21:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54450",
    "user": "@hivert"
}
```

I had to rebase the patch which now depends on #8735. I reuploaded it from sage-combinat queue.

Florent



---

archive/issue_comments_054451.json:
```json
{
    "body": "Rebased version against #8735",
    "created_at": "2010-04-21T21:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54451",
    "user": "@hivert"
}
```

Rebased version against #8735



---

archive/issue_comments_054452.json:
```json
{
    "body": "Attachment [trac_6641-poset_antichains_backtracker.2.patch](tarball://root/attachments/some-uuid/ticket6641/trac_6641-poset_antichains_backtracker.2.patch) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54452",
    "user": "@jdemeyer"
}
```

Attachment [trac_6641-poset_antichains_backtracker.2.patch](tarball://root/attachments/some-uuid/ticket6641/trac_6641-poset_antichains_backtracker.2.patch) by @jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_comments_054453.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-02-23T10:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54453",
    "user": "@jm58660"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054454.json:
```json
{
    "body": "`antichains_iterator` has been done in some other ticket.",
    "created_at": "2018-02-23T10:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54454",
    "user": "@jm58660"
}
```

`antichains_iterator` has been done in some other ticket.



---

archive/issue_comments_054455.json:
```json
{
    "body": "ok",
    "created_at": "2018-02-23T19:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54455",
    "user": "@fchapoton"
}
```

ok



---

archive/issue_comments_054456.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-02-23T19:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54456",
    "user": "@fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054457.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54457",
    "user": "@videlec"
}
```

closing positively reviewed duplicates



---

archive/issue_comments_054458.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6641#issuecomment-54458",
    "user": "@videlec"
}
```

Resolution: wontfix
