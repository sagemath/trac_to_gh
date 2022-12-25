# Issue 7421: Weaker precondition for registering a new coercion.

archive/issues_007421.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  sage-combinat @robertwb\n\nKeywords: coercion\n\nWith the attached patch, the precondition for registering a new\ncoercion from P to Q with register_coercion becomes: \n\n \"no over coercion from P to Q has been registered or discovered earlier\"\n\nWhich is a bit weaker than the previous:\n\n \"no coercion into P has been queried\"\n\nThis should still be quite safe, while covering all the formerly\nproblematic practical use cases coming up in the category code #5981.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7421\n\n",
    "created_at": "2009-11-10T01:02:16Z",
    "labels": [
        "component: coercion",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Weaker precondition for registering a new coercion.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7421",
    "user": "https://github.com/nthiery"
}
```
Assignee: @robertwb

CC:  sage-combinat @robertwb

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

archive/issue_comments_062337.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T01:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62337",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062338.json:
```json
{
    "body": "I think is probably okay.  After thinking about it for a bit, I could come up with a situation where this change would make the coercion graph non-commutatitve.\n\nI'll run all the tests with it here in a bit.",
    "created_at": "2009-11-10T05:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62338",
    "user": "https://github.com/mwhansen"
}
```

I think is probably okay.  After thinking about it for a bit, I could come up with a situation where this change would make the coercion graph non-commutatitve.

I'll run all the tests with it here in a bit.



---

archive/issue_comments_062339.json:
```json
{
    "body": "There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. \n\nNow I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it.",
    "created_at": "2009-11-11T18:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62339",
    "user": "https://github.com/robertwb"
}
```

There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. 

Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it.



---

archive/issue_comments_062340.json:
```json
{
    "body": "With the updated patch register_coercion also does not bark if _coercions_used is false.\n\nOtherwise, this triggered to failing doctests in sage/modules/fg_pid/fgp_module.py\nand sage/modules/fg_pid/fgp_morphism.py. An expert should investigate why a coercion gets registered twice in those modules, and whether this is not a bug. But I vote for postponing that for later.",
    "created_at": "2009-11-11T21:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62340",
    "user": "https://github.com/nthiery"
}
```

With the updated patch register_coercion also does not bark if _coercions_used is false.

Otherwise, this triggered to failing doctests in sage/modules/fg_pid/fgp_module.py
and sage/modules/fg_pid/fgp_morphism.py. An expert should investigate why a coercion gets registered twice in those modules, and whether this is not a bug. But I vote for postponing that for later.



---

archive/issue_comments_062341.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. \n> \n> Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it. \n\nI agree.\n\nSo, is this positive review?",
    "created_at": "2009-11-11T21:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62341",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 robertwb]:
> There is one way this can go wrong. Suppose one has B -> C, and one wants to register A -> B. If A -> C was previously requested, its non-existence will be cached. 
> 
> Now I don't think this will be an issue in practice, nor does `_unset_coercions_used` solve it. 

I agree.

So, is this positive review?



---

archive/issue_comments_062342.json:
```json
{
    "body": "The previous version was missing a patch header.",
    "created_at": "2009-11-11T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62342",
    "user": "https://github.com/nthiery"
}
```

The previous version was missing a patch header.



---

archive/issue_comments_062343.json:
```json
{
    "body": "Attachment [trac_7421-register_coercion_weaker_assertion.patch](tarball://root/attachments/some-uuid/ticket7421/trac_7421-register_coercion_weaker_assertion.patch) by @mwhansen created at 2009-11-13 04:48:17\n\nI'm going to move this to 4.3 where it's more relevant.",
    "created_at": "2009-11-13T04:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62343",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7421-register_coercion_weaker_assertion.patch](tarball://root/attachments/some-uuid/ticket7421/trac_7421-register_coercion_weaker_assertion.patch) by @mwhansen created at 2009-11-13 04:48:17

I'm going to move this to 4.3 where it's more relevant.



---

archive/issue_comments_062344.json:
```json
{
    "body": "Yes, positive review.",
    "created_at": "2009-11-14T07:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62344",
    "user": "https://github.com/robertwb"
}
```

Yes, positive review.



---

archive/issue_comments_062345.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-14T07:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62345",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007645.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T05:53:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7421#event-7645"
}
```



---

archive/issue_comments_062346.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T05:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7421#issuecomment-62346",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
