# Issue 7412: from_lehmer_code modifies its argument

archive/issues_007412.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @hivert\n\nHere is the problem:\n\n\n```\nsage: L = [0,0,0]\nsage: sage.combinat.permutation.from_lehmer_code( L )\n[1, 2, 3]\nsage: L\n[1, 1, 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7412\n\n",
    "created_at": "2009-11-08T16:32:34Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "from_lehmer_code modifies its argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7412",
    "user": "ylchapuy"
}
```
Assignee: @mwhansen

CC:  @hivert

Here is the problem:


```
sage: L = [0,0,0]
sage: sage.combinat.permutation.from_lehmer_code( L )
[1, 2, 3]
sage: L
[1, 1, 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/7412





---

archive/issue_comments_062369.json:
```json
{
    "body": "Hi Yann ! \n\nThanks for the report ! Are you working on it ? The fix is rather trivial and I'm not in the mood for racing with you to get the first patch :-)\n \nBy the way, thanks for putting me in CC, but it is better to put all the sage-combinat group for all these problem.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-08T16:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62369",
    "user": "@hivert"
}
```

Hi Yann ! 

Thanks for the report ! Are you working on it ? The fix is rather trivial and I'm not in the mood for racing with you to get the first patch :-)
 
By the way, thanks for putting me in CC, but it is better to put all the sage-combinat group for all these problem.

Cheers,

Florent



---

archive/issue_comments_062370.json:
```json
{
    "body": "need #7011",
    "created_at": "2009-11-08T17:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62370",
    "user": "ylchapuy"
}
```

need #7011



---

archive/issue_comments_062371.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-08T17:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62371",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062372.json:
```json
{
    "body": "Attachment [trac_7412-lehmer.patch](tarball://root/attachments/some-uuid/ticket7412/trac_7412-lehmer.patch) by ylchapuy created at 2009-11-08 17:47:26\n\nHi Florent,\n\nHere is the patch. Sorry for the CC, next time I'll follow your advice.\n\nRegards,\n Yann",
    "created_at": "2009-11-08T17:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62372",
    "user": "ylchapuy"
}
```

Attachment [trac_7412-lehmer.patch](tarball://root/attachments/some-uuid/ticket7412/trac_7412-lehmer.patch) by ylchapuy created at 2009-11-08 17:47:26

Hi Florent,

Here is the patch. Sorry for the CC, next time I'll follow your advice.

Regards,
 Yann



---

archive/issue_comments_062373.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-08T18:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62373",
    "user": "@hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062374.json:
```json
{
    "body": "The patch is ok and ready to go but I don't see any dependence with #7011...\nMaybe you meant #7411, but there is no problem with it. The two patches do commute. \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-08T18:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62374",
    "user": "@hivert"
}
```

The patch is ok and ready to go but I don't see any dependence with #7011...
Maybe you meant #7411, but there is no problem with it. The two patches do commute. 

Cheers,

Florent



---

archive/issue_comments_062375.json:
```json
{
    "body": "Oups, yes I meant #7411. Thanks for the review.",
    "created_at": "2009-11-08T19:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62375",
    "user": "ylchapuy"
}
```

Oups, yes I meant #7411. Thanks for the review.



---

archive/issue_comments_062376.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-11-10T00:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62376",
    "user": "ylchapuy"
}
```

Resolution: duplicate



---

archive/issue_comments_062377.json:
```json
{
    "body": "I don't know if duplicate is the right word, but the patch in #7414 solves this problem as well, but improve also the performance. Sometimes it's useful to think a little bit more...\n\nYann",
    "created_at": "2009-11-10T00:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7412#issuecomment-62377",
    "user": "ylchapuy"
}
```

I don't know if duplicate is the right word, but the patch in #7414 solves this problem as well, but improve also the performance. Sometimes it's useful to think a little bit more...

Yann
