# Issue 8579: Add the categories of magmas and additive magmas

archive/issues_008579.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @roed314\n\nKeywords: categories, magma\n\nThis patch adds the categories Magmas() and AdditiveMagmas()\n(sets with a plain binary operation * or +).\n\nIt factors out some of the code previously in Semigroups / CommutativeAdditiveSemigroups.\n\nThis is used by the updated #7555 to make it more general.\n\nDepends trivially on #7880.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8579\n\n",
    "closed_at": "2010-04-15T20:14:02Z",
    "created_at": "2010-03-22T16:33:34Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Add the categories of magmas and additive magmas",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8579",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @roed314

Keywords: categories, magma

This patch adds the categories Magmas() and AdditiveMagmas()
(sets with a plain binary operation * or +).

It factors out some of the code previously in Semigroups / CommutativeAdditiveSemigroups.

This is used by the updated #7555 to make it more general.

Depends trivially on #7880.

Issue created by migration from https://trac.sagemath.org/ticket/8579





---

archive/issue_comments_077570.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-22T20:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77570",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077571.json:
```json
{
    "body": "Changing keywords from \"\" to \"categories, magma\".",
    "created_at": "2010-03-22T20:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77571",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "categories, magma".



---

archive/issue_comments_077572.json:
```json
{
    "body": "Hi Nicolas,\n\nI get about 10 \"hunk failures\" trying to apply this to a stock 4.3.4.\n\nI noticed a \"-git\" in the diff commands in the patch, which I don't see in the patches I usually make.  Is it it me, or does this patch need some attention?\n\nRob",
    "created_at": "2010-03-23T04:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77572",
    "user": "https://github.com/rbeezer"
}
```

Hi Nicolas,

I get about 10 "hunk failures" trying to apply this to a stock 4.3.4.

I noticed a "-git" in the diff commands in the patch, which I don't see in the patches I usually make.  Is it it me, or does this patch need some attention?

Rob



---

archive/issue_comments_077573.json:
```json
{
    "body": "Thanks, Nicolas, I'll test tonight with #7880.",
    "created_at": "2010-03-23T14:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77573",
    "user": "https://github.com/rbeezer"
}
```

Thanks, Nicolas, I'll test tonight with #7880.



---

archive/issue_comments_077574.json:
```json
{
    "body": "Attachment [trac_8579-category-magmas-nt.patch](tarball://root/attachments/some-uuid/ticket8579/trac_8579-category-magmas-nt.patch) by @nthiery created at 2010-03-24 08:52:43\n\nThis updated patch fixes the copyright headers",
    "created_at": "2010-03-24T08:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77574",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8579-category-magmas-nt.patch](tarball://root/attachments/some-uuid/ticket8579/trac_8579-category-magmas-nt.patch) by @nthiery created at 2010-03-24 08:52:43

This updated patch fixes the copyright headers



---

archive/issue_comments_077575.json:
```json
{
    "body": "This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.\n\nI can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.\n\nRob",
    "created_at": "2010-03-24T14:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77575",
    "user": "https://github.com/rbeezer"
}
```

This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.

I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.

Rob



---

archive/issue_comments_077576.json:
```json
{
    "body": "Finally, Magma gets included in Sage!!",
    "created_at": "2010-03-29T07:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77576",
    "user": "https://github.com/williamstein"
}
```

Finally, Magma gets included in Sage!!



---

archive/issue_comments_077577.json:
```json
{
    "body": "Hi Rob,\n\nReplying to [comment:5 rbeezer]:\n> This passes all tests on 4.3.4.final and docs build without any problems.  It also works well when the fairly extensive #7555 is applied on top of it.  So there should be no surprises for the interested reviewer.\n\n\nThanks for checking this.\n\n> I can't say at the moment that I know enough about implementing categories to verify its completeness, so right now it either (a) needs a quick review from a knowledgeable category specialist, or (b) I need to get more education on categories so #7555 can go in.\n\n\nFrom the category implementation point of view, everything looks fine upto the\nfollowing small problem which can be left for a future patch: the\n`SubQuotient` code in `Semigroups()` is sufficiently general to work\nin magmas (computing product by lifting/retracting). It should be moved in\n`Magmas()`.\n\nOtherwise, I'm okay to give a positive review. I'll ask Nicolas directly.\n\nFlorent",
    "created_at": "2010-03-31T10:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77577",
    "user": "https://github.com/hivert"
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

archive/issue_comments_077578.json:
```json
{
    "body": "Replying to [comment:7 hivert]:\n> From the category implementation point of view, everything looks fine upto the\n> following small problem which can be left for a future patch: the\n> `SubQuotient` code in `Semigroups()` is sufficiently general to work\n> in magmas (computing product by lifting/retracting). It should be moved in\n> `Magmas()`.\n\n\nAh, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.",
    "created_at": "2010-04-01T12:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77578",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_077579.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-01T15:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77579",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077580.json:
```json
{
    "body": "Replying to [comment:8 nthiery]:\n> Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.\n\n\nThen It's ok ! positive review.",
    "created_at": "2010-04-01T15:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77580",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:8 nthiery]:
> Ah, right, I forgot to mention that. I decided to implement this moving in the upcoming functorial construction patch instead, in order to avoid potential conflicts between the two patches.


Then It's ok ! positive review.



---

archive/issue_comments_077581.json:
```json
{
    "body": "Replying to [comment:10 hivert]:\n> Then It's ok ! positive review.\n\n\nFlorent,\n\nThanks for finishing this one off!\n\nRob",
    "created_at": "2010-04-01T17:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77581",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:10 hivert]:
> Then It's ok ! positive review.


Florent,

Thanks for finishing this one off!

Rob



---

archive/issue_comments_077582.json:
```json
{
    "body": "Merged \"trac_8579-category-magmas-nt.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77582",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8579-category-magmas-nt.patch" in 4.4.alpha0



---

archive/issue_events_020714.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T20:14:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8579#event-20714"
}
```



---

archive/issue_comments_077583.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8579#issuecomment-77583",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
