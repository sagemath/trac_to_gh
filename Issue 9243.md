# Issue 9243: sage-doctest should use powers of 2 for return codes

archive/issues_009243.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @wjp\n\nRight now, sage-doctest uses these return codes:\n\n```\n# Return value in process exit code:\n# 0: all tests passed\n# 1: file not found\n# 2: KeyboardInterrupt\n# 3: doctest process was terminated by a signal\n# 4: the doctesting framework raised an exception\n# 100: failed doctests\n```\n\nIn #8641 and #9224, we make sure that the return code gets passed on to the user, and for multiple files, we `or' the return codes together. It would be much nicer for the user if we used powers of 2 for return codes, so that it's easy to see exactly what happened. \n\nI recommend we change 3->4, 4->8, and 100->128 in sage-doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9243\n\n",
    "created_at": "2010-06-15T09:33:59Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "sage-doctest should use powers of 2 for return codes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9243",
    "user": "@dandrake"
}
```
Assignee: mvngu

CC:  @wjp

Right now, sage-doctest uses these return codes:

```
# Return value in process exit code:
# 0: all tests passed
# 1: file not found
# 2: KeyboardInterrupt
# 3: doctest process was terminated by a signal
# 4: the doctesting framework raised an exception
# 100: failed doctests
```

In #8641 and #9224, we make sure that the return code gets passed on to the user, and for multiple files, we `or' the return codes together. It would be much nicer for the user if we used powers of 2 for return codes, so that it's easy to see exactly what happened. 

I recommend we change 3->4, 4->8, and 100->128 in sage-doctest.

Issue created by migration from https://trac.sagemath.org/ticket/9243





---

archive/issue_comments_086925.json:
```json
{
    "body": "Patch up, please review. This depends on #8641. I added an exit code of 16 for \"bad options\"; previously, sage-doctest exited with code 1 for both \"file not found\" and \"bad options\".",
    "created_at": "2010-06-16T04:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86925",
    "user": "@dandrake"
}
```

Patch up, please review. This depends on #8641. I added an exit code of 16 for "bad options"; previously, sage-doctest exited with code 1 for both "file not found" and "bad options".



---

archive/issue_comments_086926.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-16T04:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86926",
    "user": "@dandrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086927.json:
```json
{
    "body": "Attachment [trac_9243.patch](tarball://root/attachments/some-uuid/ticket9243/trac_9243.patch) by @dandrake created at 2010-06-18 01:59:30\n\napply to scripts repo",
    "created_at": "2010-06-18T01:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86927",
    "user": "@dandrake"
}
```

Attachment [trac_9243.patch](tarball://root/attachments/some-uuid/ticket9243/trac_9243.patch) by @dandrake created at 2010-06-18 01:59:30

apply to scripts repo



---

archive/issue_comments_086928.json:
```json
{
    "body": "The new patch changes the absurdly accurate reporting of how long the tests took when you hit Ctrl-C; before we had \"KeyboardInterrupt -- interrupted after 2.2340259552 seconds!\" and now it just uses one decimal place, instead of 10.",
    "created_at": "2010-06-18T02:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86928",
    "user": "@dandrake"
}
```

The new patch changes the absurdly accurate reporting of how long the tests took when you hit Ctrl-C; before we had "KeyboardInterrupt -- interrupted after 2.2340259552 seconds!" and now it just uses one decimal place, instead of 10.



---

archive/issue_comments_086929.json:
```json
{
    "body": "When #9316 merges, will we need to use 256, too, or use a different collection scheme?",
    "created_at": "2010-07-06T07:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86929",
    "user": "@qed777"
}
```

When #9316 merges, will we need to use 256, too, or use a different collection scheme?



---

archive/issue_comments_086930.json:
```json
{
    "body": "Thanks for adding me to CC.\n\nI like this patch. There's one more instance, though: test_file in sage-ptest uses 5 as its own internal error code for unhandled exception. We should probably change that to 32. (And keep that one reserved.)\n\nIf #9316 is rebased on top of this one (which I can do), it will use error code 64 for timeouts.\n\nAll 8 available bits are then in use, so if we want to add more error conditions after that, we'll have to re-think this, or merge some error flags together.\n\n\nMeta-comment: there are now three doctest related patches that I'm aware of, and that should probably all be merged. I would suggest this order: #9243, #9316, #8641.",
    "created_at": "2010-07-06T08:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86930",
    "user": "@wjp"
}
```

Thanks for adding me to CC.

I like this patch. There's one more instance, though: test_file in sage-ptest uses 5 as its own internal error code for unhandled exception. We should probably change that to 32. (And keep that one reserved.)

If #9316 is rebased on top of this one (which I can do), it will use error code 64 for timeouts.

All 8 available bits are then in use, so if we want to add more error conditions after that, we'll have to re-think this, or merge some error flags together.


Meta-comment: there are now three doctest related patches that I'm aware of, and that should probably all be merged. I would suggest this order: #9243, #9316, #8641.



---

archive/issue_comments_086931.json:
```json
{
    "body": "Meta-meta-comment: sorry, I'm blind. This patch already depends on #8641 of course. I'll rebase #9316 to apply after #8641 and #9243.",
    "created_at": "2010-07-06T16:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86931",
    "user": "@wjp"
}
```

Meta-meta-comment: sorry, I'm blind. This patch already depends on #8641 of course. I'll rebase #9316 to apply after #8641 and #9243.



---

archive/issue_comments_086932.json:
```json
{
    "body": "apply after trac_9243.patch",
    "created_at": "2010-07-06T20:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86932",
    "user": "@wjp"
}
```

apply after trac_9243.patch



---

archive/issue_comments_086933.json:
```json
{
    "body": "Attachment [trac_9243_2.patch](tarball://root/attachments/some-uuid/ticket9243/trac_9243_2.patch) by @wjp created at 2010-07-06 20:53:48\n\nI added a patch to address the internally used error code 5.\n\nPositive review for the rest of the patch. Could someone review my small reviewer patch?",
    "created_at": "2010-07-06T20:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86933",
    "user": "@wjp"
}
```

Attachment [trac_9243_2.patch](tarball://root/attachments/some-uuid/ticket9243/trac_9243_2.patch) by @wjp created at 2010-07-06 20:53:48

I added a patch to address the internally used error code 5.

Positive review for the rest of the patch. Could someone review my small reviewer patch?



---

archive/issue_comments_086934.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-07T03:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86934",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086935.json:
```json
{
    "body": "To release manager: Apply *both* patches to 4.5.alpha4 + #8641.",
    "created_at": "2010-07-07T03:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86935",
    "user": "@qed777"
}
```

To release manager: Apply *both* patches to 4.5.alpha4 + #8641.



---

archive/issue_comments_086936.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86936",
    "user": "@dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_086937.json:
```json
{
    "body": "Merged both patches in 4.5.2.alpha1.",
    "created_at": "2010-07-22T07:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9243#issuecomment-86937",
    "user": "@dandrake"
}
```

Merged both patches in 4.5.2.alpha1.
