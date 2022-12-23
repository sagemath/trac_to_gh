# Issue 7421: Weaker precondition for registering a new coercion.

archive/issues_007421.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  sage-combinat robertwb\n\nKeywords: coercion\n\nWith the attached patch, the precondition for registering a new\ncoercion from P to Q with register_coercion becomes: \n\n \"no over coercion from P to Q has been registered or discovered earlier\"\n\nWhich is a bit weaker than the previous:\n\n \"no coercion into P has been queried\"\n\nThis should still be quite safe, while covering all the formerly\nproblematic practical use cases coming up in the category code #5981.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7421\n\n",
    "created_at": "2009-11-10T01:02:16Z",
    "labels": [
        "coercion",
        "blocker",
        "enhancement"
    ],
    "title": "Weaker precondition for registering a new coercion.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7421",
    "user": "nthiery"
}
```
Assignee: robertwb

CC:  sage-combinat robertwb

Keywords: coercion

With the attached patch, the precondition for registering a new
coercion from P to Q with register_coercion becomes: 

 "no over coercion from P to Q has been registered or discovered earlier"

Which is a bit weaker than the previous:

 "no coercion into P has been queried"

This should still be quite safe, while covering all the formerly
problematic practical use cases coming up in the category code #5981.

Issue created by migration from https://trac.sagemath.org/ticket/7421





---

archive/issue_comments_062452.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T01:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62452",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062453.json:
```json
{
    "body": "I think is probably okay.  After thinking about it for a bit, I could come up with a situation where this change would make the coercion graph non-commutatitve.\n\nI'll run all the tests with it here in a bit.",
    "created_at": "2009-11-10T05:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62453",
    "user": "mhansen"
}
```

I think is probably okay.  After thinking about it for a bit, I could come up with a situation where this change would make the coercion graph non-commutatitve.

I'll run all the tests with it here in a bit.



---

archive/issue_comments_062454.json:
```json
{
    "body": "There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. \n\nNow I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it.",
    "created_at": "2009-11-11T18:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62454",
    "user": "robertwb"
}
```

There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. 

Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it.



---

archive/issue_comments_062455.json:
```json
{
    "body": "With the updated patch register_coercion also does not bark if _coercions_used is false.\n\nOtherwise, this triggered to failing doctests in sage/modules/fg_pid/fgp_module.py\nand sage/modules/fg_pid/fgp_morphism.py. An expert should investigate why a coercion gets registered twice in those modules, and whether this is not a bug. But I vote for postponing that for later.",
    "created_at": "2009-11-11T21:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62455",
    "user": "nthiery"
}
```

With the updated patch register_coercion also does not bark if _coercions_used is false.

Otherwise, this triggered to failing doctests in sage/modules/fg_pid/fgp_module.py
and sage/modules/fg_pid/fgp_morphism.py. An expert should investigate why a coercion gets registered twice in those modules, and whether this is not a bug. But I vote for postponing that for later.



---

archive/issue_comments_062456.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. \n> \n> Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it. \n\nI agree.\n\nSo, is this positive review?",
    "created_at": "2009-11-11T21:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62456",
    "user": "nthiery"
}
```

Replying to [comment:4 robertwb]:
> There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. 
> 
> Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it. 

I agree.

So, is this positive review?



---

archive/issue_comments_062457.json:
```json
{
    "body": "The previous version was missing a patch header.",
    "created_at": "2009-11-11T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62457",
    "user": "nthiery"
}
```

The previous version was missing a patch header.



---

archive/issue_comments_062458.json:
```json
{
    "body": "Attachment\n\nI'm going to move this to 4.3 where it's more relevant.",
    "created_at": "2009-11-13T04:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62458",
    "user": "mhansen"
}
```

Attachment

I'm going to move this to 4.3 where it's more relevant.



---

archive/issue_comments_062459.json:
```json
{
    "body": "Yes, positive review.",
    "created_at": "2009-11-14T07:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62459",
    "user": "robertwb"
}
```

Yes, positive review.



---

archive/issue_comments_062460.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-14T07:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62460",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062461.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T05:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62461",
    "user": "mhansen"
}
```

Resolution: fixed
