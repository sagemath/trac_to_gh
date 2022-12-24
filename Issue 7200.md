# Issue 7200: Fixing longest increasing subsequence (permutation method)

archive/issues_007200.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nKeywords: permutation\n\nThe method \"longest_increasing_subsequence\" was computing the longest increasing factors of the permutation!\n\nThis patch fixes the problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7200\n\n",
    "created_at": "2009-10-13T14:04:38Z",
    "labels": [
        "combinatorics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Fixing longest increasing subsequence (permutation method)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7200",
    "user": "vferay"
}
```
Assignee: mhansen

CC:  sage-combinat

Keywords: permutation

The method "longest_increasing_subsequence" was computing the longest increasing factors of the permutation!

This patch fixes the problem.

Issue created by migration from https://trac.sagemath.org/ticket/7200





---

archive/issue_comments_059742.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-13T14:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59742",
    "user": "vferay"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059743.json:
```json
{
    "body": "Attachment [permutations_fix_longest_increasing_subsequence_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_vf.patch) by vferay created at 2009-10-13 14:16:19",
    "created_at": "2009-10-13T14:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59743",
    "user": "vferay"
}
```

Attachment [permutations_fix_longest_increasing_subsequence_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_vf.patch) by vferay created at 2009-10-13 14:16:19



---

archive/issue_comments_059744.json:
```json
{
    "body": "Changing assignee from mhansen to vferay.",
    "created_at": "2009-10-14T08:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59744",
    "user": "vferay"
}
```

Changing assignee from mhansen to vferay.



---

archive/issue_comments_059745.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-17T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59745",
    "user": "hivert"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_059746.json:
```json
{
    "body": "I dislike the name `length_of_lis` ! I whould never had gessed the meaning of `lis`. Is it so painful to type `length_of_longest_increasing_subsequence` or `longest_incressing_subsequence_length` ? \n\nThe latter is my favourite... \n\nI cc this to sage-combinat to have a vote. Add set the status to \"needs info\". \n\nCheers,\n\nFlorent",
    "created_at": "2009-10-17T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59746",
    "user": "hivert"
}
```

I dislike the name `length_of_lis` ! I whould never had gessed the meaning of `lis`. Is it so painful to type `length_of_longest_increasing_subsequence` or `longest_incressing_subsequence_length` ? 

The latter is my favourite... 

I cc this to sage-combinat to have a vote. Add set the status to "needs info". 

Cheers,

Florent



---

archive/issue_comments_059747.json:
```json
{
    "body": "Hi Florent,\n\nI agree... I think \"longest_increasing_subsequence_length\" is also better because it will be near \"longest_increasing_subsequences\" in the method list...\n\nBest,\nValentin",
    "created_at": "2009-10-18T09:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59747",
    "user": "vferay"
}
```

Hi Florent,

I agree... I think "longest_increasing_subsequence_length" is also better because it will be near "longest_increasing_subsequences" in the method list...

Best,
Valentin



---

archive/issue_comments_059748.json:
```json
{
    "body": "Hi !\n\n> I agree... I think \"longest_increasing_subsequence_length\" is also better because it will be near \"longest_increasing_subsequences\" in the method list...\n\nIn case you are just waiting for more vote, I think you can go for it ...\n\nFlorent",
    "created_at": "2009-10-23T16:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59748",
    "user": "hivert"
}
```

Hi !

> I agree... I think "longest_increasing_subsequence_length" is also better because it will be near "longest_increasing_subsequences" in the method list...

In case you are just waiting for more vote, I think you can go for it ...

Florent



---

archive/issue_comments_059749.json:
```json
{
    "body": "Attachment [permutations_fix_longest_increasing_subsequence_7200_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_7200_vf.patch) by vferay created at 2009-11-04 17:27:21",
    "created_at": "2009-11-04T17:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59749",
    "user": "vferay"
}
```

Attachment [permutations_fix_longest_increasing_subsequence_7200_vf.patch](tarball://root/attachments/some-uuid/ticket7200/permutations_fix_longest_increasing_subsequence_7200_vf.patch) by vferay created at 2009-11-04 17:27:21



---

archive/issue_comments_059750.json:
```json
{
    "body": "ok I changed the name. What shall I do now?",
    "created_at": "2009-11-04T17:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59750",
    "user": "vferay"
}
```

ok I changed the name. What shall I do now?



---

archive/issue_comments_059751.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-11-04T21:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59751",
    "user": "hivert"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_059752.json:
```json
{
    "body": "Replying to [comment:6 vferay]:\n> ok I changed the name. What shall I do now?\n\nFirst you should say something like:\n\"I just submitted a new version of the patch which is ready for review.\"\n\nThen after that you should change the status which is currently \"needs info\" to \"needs review\" (see the frame at the bottom of the page) and then wait if someone react by putting a positive review or another request...\n\nAnd finally for the release manager you should tell that only `permutations_fix_longest_increasing_subsequence_7200_vf.patch`\nshould be applied.\n\nAs you can see, I've done this for you :-). So everything is ok... \n\nI'm reviewing the patch...\n\nFlorent",
    "created_at": "2009-11-04T21:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59752",
    "user": "hivert"
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

archive/issue_comments_059753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-04T21:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59753",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059754.json:
```json
{
    "body": "Patch looks good, all tests ok. Positive review.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-04T21:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59754",
    "user": "hivert"
}
```

Patch looks good, all tests ok. Positive review.

Cheers,

Florent



---

archive/issue_comments_059755.json:
```json
{
    "body": "Attachment [trac_7200.patch](tarball://root/attachments/some-uuid/ticket7200/trac_7200.patch) by mhansen created at 2009-11-05 01:43:03",
    "created_at": "2009-11-05T01:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59755",
    "user": "mhansen"
}
```

Attachment [trac_7200.patch](tarball://root/attachments/some-uuid/ticket7200/trac_7200.patch) by mhansen created at 2009-11-05 01:43:03



---

archive/issue_comments_059756.json:
```json
{
    "body": "I uploaded a patch which makes a small change to the documentation markup.  I've also updated the patch on the patch server.",
    "created_at": "2009-11-05T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59756",
    "user": "mhansen"
}
```

I uploaded a patch which makes a small change to the documentation markup.  I've also updated the patch on the patch server.



---

archive/issue_comments_059757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-05T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7200#issuecomment-59757",
    "user": "mhansen"
}
```

Resolution: fixed
