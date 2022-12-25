# Issue 7200: Fixing longest increasing subsequence (permutation method)

archive/issues_007200.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: permutation\n\nThe method \"longest_increasing_subsequence\" was computing the longest increasing factors of the permutation!\n\nThis patch fixes the problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7200\n\n",
    "created_at": "2009-10-13T14:04:38Z",
    "labels": [
        "component: combinatorics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Fixing longest increasing subsequence (permutation method)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7200",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: permutation

The method "longest_increasing_subsequence" was computing the longest increasing factors of the permutation!

This patch fixes the problem.

Issue created by migration from https://trac.sagemath.org/ticket/7200





---

archive/issue_comments_059630.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-13T14:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59630",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059631.json:
```json
{
    "body": "Attachment [permutations_fix_longest_increasing_subsequence_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_vf.patch) by vferay created at 2009-10-13 14:16:19",
    "created_at": "2009-10-13T14:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59631",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Attachment [permutations_fix_longest_increasing_subsequence_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_vf.patch) by vferay created at 2009-10-13 14:16:19



---

archive/issue_comments_059632.json:
```json
{
    "body": "Changing assignee from @mwhansen to vferay.",
    "created_at": "2009-10-14T08:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59632",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Changing assignee from @mwhansen to vferay.



---

archive/issue_comments_059633.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-17T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59633",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_059634.json:
```json
{
    "body": "I dislike the name `length_of_lis` ! I whould never had gessed the meaning of `lis`. Is it so painful to type `length_of_longest_increasing_subsequence` or `longest_incressing_subsequence_length` ? \n\nThe latter is my favourite... \n\nI cc this to sage-combinat to have a vote. Add set the status to \"needs info\". \n\nCheers,\n\nFlorent",
    "created_at": "2009-10-17T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59634",
    "user": "https://github.com/hivert"
}
```

I dislike the name `length_of_lis` ! I whould never had gessed the meaning of `lis`. Is it so painful to type `length_of_longest_increasing_subsequence` or `longest_incressing_subsequence_length` ? 

The latter is my favourite... 

I cc this to sage-combinat to have a vote. Add set the status to "needs info". 

Cheers,

Florent



---

archive/issue_comments_059635.json:
```json
{
    "body": "Hi Florent,\n\nI agree... I think \"longest_increasing_subsequence_length\" is also better because it will be near \"longest_increasing_subsequences\" in the method list...\n\nBest,\nValentin",
    "created_at": "2009-10-18T09:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59635",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Hi Florent,

I agree... I think "longest_increasing_subsequence_length" is also better because it will be near "longest_increasing_subsequences" in the method list...

Best,
Valentin



---

archive/issue_comments_059636.json:
```json
{
    "body": "Hi !\n\n> I agree... I think \"longest_increasing_subsequence_length\" is also better because it will be near \"longest_increasing_subsequences\" in the method list...\n\nIn case you are just waiting for more vote, I think you can go for it ...\n\nFlorent",
    "created_at": "2009-10-23T16:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59636",
    "user": "https://github.com/hivert"
}
```

Hi !

> I agree... I think "longest_increasing_subsequence_length" is also better because it will be near "longest_increasing_subsequences" in the method list...

In case you are just waiting for more vote, I think you can go for it ...

Florent



---

archive/issue_comments_059637.json:
```json
{
    "body": "Attachment [permutations_fix_longest_increasing_subsequence_7200_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_7200_vf.patch) by vferay created at 2009-11-04 17:27:21",
    "created_at": "2009-11-04T17:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59637",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

Attachment [permutations_fix_longest_increasing_subsequence_7200_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_7200_vf.patch) by vferay created at 2009-11-04 17:27:21



---

archive/issue_comments_059638.json:
```json
{
    "body": "ok I changed the name. What shall I do now?",
    "created_at": "2009-11-04T17:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59638",
    "user": "https://trac.sagemath.org/admin/accounts/users/vferay"
}
```

ok I changed the name. What shall I do now?



---

archive/issue_comments_059639.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-11-04T21:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59639",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_059640.json:
```json
{
    "body": "Replying to [comment:6 vferay]:\n> ok I changed the name. What shall I do now?\n\nFirst you should say something like:\n\"I just submitted a new version of the patch which is ready for review.\"\n\nThen after that you should change the status which is currently \"needs info\" to \"needs review\" (see the frame at the bottom of the page) and then wait if someone react by putting a positive review or another request...\n\nAnd finally for the release manager you should tell that only `permutations_fix_longest_increasing_subsequence_7200_vf.patch`\nshould be applied.\n\nAs you can see, I've done this for you :-). So everything is ok... \n\nI'm reviewing the patch...\n\nFlorent",
    "created_at": "2009-11-04T21:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59640",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:6 vferay]:
> ok I changed the name. What shall I do now?

First you should say something like:
"I just submitted a new version of the patch which is ready for review."

Then after that you should change the status which is currently "needs info" to "needs review" (see the frame at the bottom of the page) and then wait if someone react by putting a positive review or another request...

And finally for the release manager you should tell that only `permutations_fix_longest_increasing_subsequence_7200_vf.patch`
should be applied.

As you can see, I've done this for you :-). So everything is ok... 

I'm reviewing the patch...

Florent



---

archive/issue_comments_059641.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-04T21:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59641",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059642.json:
```json
{
    "body": "Patch looks good, all tests ok. Positive review.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-04T21:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59642",
    "user": "https://github.com/hivert"
}
```

Patch looks good, all tests ok. Positive review.

Cheers,

Florent



---

archive/issue_comments_059643.json:
```json
{
    "body": "Attachment [trac_7200.patch](tarball://root/attachments/some-uuid/ticket7200/trac_7200.patch) by @mwhansen created at 2009-11-05 01:43:03",
    "created_at": "2009-11-05T01:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59643",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7200.patch](tarball://root/attachments/some-uuid/ticket7200/trac_7200.patch) by @mwhansen created at 2009-11-05 01:43:03



---

archive/issue_comments_059644.json:
```json
{
    "body": "I uploaded a patch which makes a small change to the documentation markup.  I've also updated the patch on the patch server.",
    "created_at": "2009-11-05T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59644",
    "user": "https://github.com/mwhansen"
}
```

I uploaded a patch which makes a small change to the documentation markup.  I've also updated the patch on the patch server.



---

archive/issue_comments_059645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-05T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59645",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
