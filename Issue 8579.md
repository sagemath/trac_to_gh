# Issue 8579: Add the categories of magmas and additive magmas

archive/issues_008579.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @roed314\n\nThis patch adds the categories Magmas() and AdditiveMagmas()\n(sets with a plain binary operation * or +).\n\nIt factors out some of the code previously in Semigroups / CommutativeAdditiveSemigroups.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8579\n\n",
    "created_at": "2010-03-22T16:33:34Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Add the categories of magmas and additive magmas",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8579",
    "user": "@nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @roed314

This patch adds the categories Magmas() and AdditiveMagmas()
(sets with a plain binary operation * or +).

It factors out some of the code previously in Semigroups / CommutativeAdditiveSemigroups.

Issue created by migration from https://trac.sagemath.org/ticket/8579





---

archive/issue_comments_077698.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-22T20:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77698",
    "user": "@nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077699.json:
```json
{
    "body": "Changing keywords from \"\" to \"categories, magma\".",
    "created_at": "2010-03-22T20:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77699",
    "user": "@nthiery"
}
```

Changing keywords from "" to "categories, magma".



---

archive/issue_comments_077700.json:
```json
{
    "body": "Hi Nicolas,\n\nI get about 10 \"hunk failures\" trying to apply this to a stock 4.3.4.\n\nI noticed a \"-git\" in the diff commands in the patch, which I don't see in the patches I usually make.  Is it it me, or does this patch need some attention?\n\nRob",
    "created_at": "2010-03-23T04:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77700",
    "user": "@rbeezer"
}
```

Hi Nicolas,

I get about 10 "hunk failures" trying to apply this to a stock 4.3.4.

I noticed a "-git" in the diff commands in the patch, which I don't see in the patches I usually make.  Is it it me, or does this patch need some attention?

Rob



---

archive/issue_comments_077701.json:
```json
{
    "body": "Thanks, Nicolas, I'll test tonight with #7880.",
    "created_at": "2010-03-23T14:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77701",
    "user": "@rbeezer"
}
```

Thanks, Nicolas, I'll test tonight with #7880.



---

archive/issue_comments_077702.json:
```json
{
    "body": "Attachment [trac_8579-category-magmas-nt.patch](tarball://root/attachments/some-uuid/ticket8579/trac_8579-category-magmas-nt.patch) by @nthiery created at 2010-03-24 08:52:43\n\nThis updated patch fixes the copyright headers",
    "created_at": "2010-03-24T08:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77702",
    "user": "@nthiery"
}
```

Attachment [trac_8579-category-magmas-nt.patch](tarball://root/attachments/some-uuid/ticket8579/trac_8579-category-magmas-nt.patch) by @nthiery created at 2010-03-24 08:52:43

This updated patch fixes the copyright headers



---

archive/issue_comments_077703.json:
```json
{
    "body": "This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.\n\nI can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.\n\nRob",
    "created_at": "2010-03-24T14:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77703",
    "user": "@rbeezer"
}
```

This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.

I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.

Rob



---

archive/issue_comments_077704.json:
```json
{
    "body": "Finally, Magma gets included in Sage!!",
    "created_at": "2010-03-29T07:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77704",
    "user": "@williamstein"
}
```

Finally, Magma gets included in Sage!!



---

archive/issue_comments_077705.json:
```json
{
    "body": "Hi Rob,\n\nReplying to [comment:5 rbeezer]:\n> This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.\n\nThanks for checking this.\n\n> I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.\n\nFrom the category implementation point of view, everything looks fine upto the\nfollowing small problem which can be left for a future patch: the\n`SubQuotient` code in `Semigroups()` is sufficiently general to work\nin magmas (computing product by lifting/retracting). It should be moved in\n`Magmas()`.\n\nOtherwise, I'm okay to give a positive review. I'll ask Nicolas directly.\n\nFlorent",
    "created_at": "2010-03-31T10:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77705",
    "user": "@hivert"
}
```

Hi Rob,

Replying to [comment:5 rbeezer]:
> This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.

Thanks for checking this.

> I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.

From the category implementation point of view, everything looks fine upto the
following small problem which can be left for a future patch: the
`SubQuotient` code in `Semigroups()` is sufficiently general to work
in magmas (computing product by lifting/retracting). It should be moved in
`Magmas()`.

Otherwise, I'm okay to give a positive review. I'll ask Nicolas directly.

Florent



---

archive/issue_comments_077706.json:
```json
{
    "body": "Replying to [comment:7 hivert]:\n> From the category implementation point of view, everything looks fine upto the\n> following small problem which can be left for a future patch: the\n> `SubQuotient` code in `Semigroups()` is sufficiently general to work\n> in magmas (computing product by lifting/retracting). It should be moved in\n> `Magmas()`.\n\nAh, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.",
    "created_at": "2010-04-01T12:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77706",
    "user": "@nthiery"
}
```

Replying to [comment:7 hivert]:
> From the category implementation point of view, everything looks fine upto the
> following small problem which can be left for a future patch: the
> `SubQuotient` code in `Semigroups()` is sufficiently general to work
> in magmas (computing product by lifting/retracting). It should be moved in
> `Magmas()`.

Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.



---

archive/issue_comments_077707.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-01T15:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77707",
    "user": "@hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077708.json:
```json
{
    "body": "Replying to [comment:8 nthiery]:\n> Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.\n\nThen It's ok ! positive review.",
    "created_at": "2010-04-01T15:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77708",
    "user": "@hivert"
}
```

Replying to [comment:8 nthiery]:
> Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.

Then It's ok ! positive review.



---

archive/issue_comments_077709.json:
```json
{
    "body": "Replying to [comment:10 hivert]:\n> Then It's ok ! positive review.\n\nFlorent,\n\nThanks for finishing this one off!\n\nRob",
    "created_at": "2010-04-01T17:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77709",
    "user": "@rbeezer"
}
```

Replying to [comment:10 hivert]:
> Then It's ok ! positive review.

Florent,

Thanks for finishing this one off!

Rob



---

archive/issue_comments_077710.json:
```json
{
    "body": "Merged \"trac_8579-category-magmas-nt.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77710",
    "user": "@jhpalmieri"
}
```

Merged "trac_8579-category-magmas-nt.patch" in 4.4.alpha0



---

archive/issue_comments_077711.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77711",
    "user": "@jhpalmieri"
}
```

Resolution: fixed
