# Issue 5597: [with patch, needs review] rename coercion action methods

archive/issues_005597.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @nthiery georgsweber @craigcitro\n\n```\nCurrently, if A has an action on B (where B is not an A-module) one  \nimplements either a._l_action_ or b._r_action_. This is because  \nsometimes it makes sense to put the method on the actor (e.g. Galois  \ngroups acting on field elements) and sometimes on the acted on (e.g.  \nmatrices acting on quadratic forms). However, the _x_action_ is hard  \nto remember and doesn't always correspond to right/left actions. This  \nmay be why they're hardly used up to this point.\n\nThe proposal is to make the methods a._act_on_(b, self_on_left) and  \nb._acted_upon_(a, self_on_left). In other words, a*b would try  \n\"a._act_on_(b, True)\" and \"b._acted_upon_(a, False)\". \n```\n\nSee discussion at \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/4c6ce1731ace1016\n\nIssue created by migration from https://trac.sagemath.org/ticket/5597\n\n",
    "created_at": "2009-03-24T05:09:01Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] rename coercion action methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5597",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

CC:  @nthiery georgsweber @craigcitro

```
Currently, if A has an action on B (where B is not an A-module) one  
implements either a._l_action_ or b._r_action_. This is because  
sometimes it makes sense to put the method on the actor (e.g. Galois  
groups acting on field elements) and sometimes on the acted on (e.g.  
matrices acting on quadratic forms). However, the _x_action_ is hard  
to remember and doesn't always correspond to right/left actions. This  
may be why they're hardly used up to this point.

The proposal is to make the methods a._act_on_(b, self_on_left) and  
b._acted_upon_(a, self_on_left). In other words, a*b would try  
"a._act_on_(b, True)" and "b._acted_upon_(a, False)". 
```

See discussion at 

http://groups.google.com/group/sage-devel/browse_thread/thread/4c6ce1731ace1016

Issue created by migration from https://trac.sagemath.org/ticket/5597





---

archive/issue_comments_043518.json:
```json
{
    "body": "Attachment [5597-coerce-actions.patch](tarball://root/attachments/some-uuid/ticket5597/5597-coerce-actions.patch) by @robertwb created at 2009-03-24 05:17:58",
    "created_at": "2009-03-24T05:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43518",
    "user": "https://github.com/robertwb"
}
```

Attachment [5597-coerce-actions.patch](tarball://root/attachments/some-uuid/ticket5597/5597-coerce-actions.patch) by @robertwb created at 2009-03-24 05:17:58



---

archive/issue_comments_043519.json:
```json
{
    "body": "Rename and cleanup actions. Depends on #5596.",
    "created_at": "2009-03-24T05:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43519",
    "user": "https://github.com/robertwb"
}
```

Rename and cleanup actions. Depends on #5596.



---

archive/issue_comments_043520.json:
```json
{
    "body": "Minor issue: in element.pyx, both new actions are commented with \"Use this method to implement self acting on x.\" --- probably a copy'n'paste error for \"_acted_upon_\"?!\n\nCheers,\ngsw",
    "created_at": "2009-03-24T21:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43520",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Minor issue: in element.pyx, both new actions are commented with "Use this method to implement self acting on x." --- probably a copy'n'paste error for "_acted_upon_"?!

Cheers,
gsw



---

archive/issue_comments_043521.json:
```json
{
    "body": "REFEREE REPORT:\n\nThis patch contains substantial new code that has no doctests.  Please post another patch with full coverage.",
    "created_at": "2009-04-12T05:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43521",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

This patch contains substantial new code that has no doctests.  Please post another patch with full coverage.



---

archive/issue_comments_043522.json:
```json
{
    "body": "rebased against 4.1.1",
    "created_at": "2009-09-25T08:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43522",
    "user": "https://github.com/robertwb"
}
```

rebased against 4.1.1



---

archive/issue_comments_043523.json:
```json
{
    "body": "Attachment [5597-coerce-actions-new.patch](tarball://root/attachments/some-uuid/ticket5597/5597-coerce-actions-new.patch) by @robertwb created at 2009-09-25 08:40:50",
    "created_at": "2009-09-25T08:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43523",
    "user": "https://github.com/robertwb"
}
```

Attachment [5597-coerce-actions-new.patch](tarball://root/attachments/some-uuid/ticket5597/5597-coerce-actions-new.patch) by @robertwb created at 2009-09-25 08:40:50



---

archive/issue_comments_043524.json:
```json
{
    "body": "Attachment [5597-coerce-actions-examples.patch](tarball://root/attachments/some-uuid/ticket5597/5597-coerce-actions-examples.patch) by @robertwb created at 2009-09-25 08:41:36",
    "created_at": "2009-09-25T08:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43524",
    "user": "https://github.com/robertwb"
}
```

Attachment [5597-coerce-actions-examples.patch](tarball://root/attachments/some-uuid/ticket5597/5597-coerce-actions-examples.patch) by @robertwb created at 2009-09-25 08:41:36



---

archive/issue_comments_043525.json:
```json
{
    "body": "Attachment [5597-referee-comments.patch](tarball://root/attachments/some-uuid/ticket5597/5597-referee-comments.patch) by @robertwb created at 2009-09-29 18:27:10",
    "created_at": "2009-09-29T18:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43525",
    "user": "https://github.com/robertwb"
}
```

Attachment [5597-referee-comments.patch](tarball://root/attachments/some-uuid/ticket5597/5597-referee-comments.patch) by @robertwb created at 2009-09-29 18:27:10



---

archive/issue_comments_043526.json:
```json
{
    "body": "Hi Robert,\n\nSorry for hopping so late in the discussion. I am not sure how I understand how left vs right actions are handled.\n\nIn a*b, are you always making the assumption that a is acting on b?\n\nIf I have an algebra B (whose code I don't want to touch), and implement a right B-module A,\nam I supposed to implement:\n\n   a.act_on(b)?\n\nOr will a*b try all of:\n\n   b.act_on(a, False)\n   b.acted_upon(a, False)\n   a.act_on(b, True)\n   a.acted_upon(b, True)",
    "created_at": "2009-10-12T10:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43526",
    "user": "https://github.com/nthiery"
}
```

Hi Robert,

Sorry for hopping so late in the discussion. I am not sure how I understand how left vs right actions are handled.

In a*b, are you always making the assumption that a is acting on b?

If I have an algebra B (whose code I don't want to touch), and implement a right B-module A,
am I supposed to implement:

   a.act_on(b)?

Or will a*b try all of:

   b.act_on(a, False)
   b.acted_upon(a, False)
   a.act_on(b, True)
   a.acted_upon(b, True)



---

archive/issue_comments_043527.json:
```json
{
    "body": "Yes, it should be trying all 4 of these options.",
    "created_at": "2009-10-13T00:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43527",
    "user": "https://github.com/robertwb"
}
```

Yes, it should be trying all 4 of these options.



---

archive/issue_comments_043528.json:
```json
{
    "body": "Replying to [comment:7 robertwb]:\n> Yes, it should be trying all 4 of these options. \n\n\nOk. Then I would prefer:\n\na.act_on_left(b)\nb.act_on_right(a)\na.acted_upon_right(b)\nb.acted_upon_left(a)\n\nwhich makes it easier to implement independently the left and right actions on a module, and possibly override just one or the other in a subclass.\n\nThat being said, we can leave things as is. Those modules for which left and right action do not coincide can later implement a.acted_upon(...) by delegating the work to\nacted_upon_left and acted_upon_right.",
    "created_at": "2009-10-14T10:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43528",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:7 robertwb]:
> Yes, it should be trying all 4 of these options. 


Ok. Then I would prefer:

a.act_on_left(b)
b.act_on_right(a)
a.acted_upon_right(b)
b.acted_upon_left(a)

which makes it easier to implement independently the left and right actions on a module, and possibly override just one or the other in a subclass.

That being said, we can leave things as is. Those modules for which left and right action do not coincide can later implement a.acted_upon(...) by delegating the work to
acted_upon_left and acted_upon_right.



---

archive/issue_comments_043529.json:
```json
{
    "body": "But then we're back to the same problem of `s.acted_upon_right(p)` not being obvious whether s or p was the one on the right (though it's a bit better). In any case, this behavior is easy to implement in a superclass. \n\nSo, is this a positive review (pending all doctests passing, which they did last I checked)?",
    "created_at": "2009-10-15T05:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43529",
    "user": "https://github.com/robertwb"
}
```

But then we're back to the same problem of `s.acted_upon_right(p)` not being obvious whether s or p was the one on the right (though it's a bit better). In any case, this behavior is easy to implement in a superclass. 

So, is this a positive review (pending all doctests passing, which they did last I checked)?



---

archive/issue_comments_043530.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-15T12:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43530",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_043531.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-15T12:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43531",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_043532.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n> But then we're back to the same problem of `s.acted_upon_right(p)` not being obvious whether s or p was the one on the right (though it's a bit better). \n\n\nIt sounds rather clear to me.\n\n> In any case, this behavior is easy to implement in a superclass. \n\n\nYes.\n\n> So, is this a positive review (pending all doctests passing, which they did last I checked)?\n\n\nYes, I just wanted to discuss the matter first. Also, part of this may become obsolete once I will have a prototype implementation of overloaded operators/functions as in MuPAD, with a declarative interface (the Sage-combinat people need them anyway for other purposes). I'll post here a link to the appropriate ticket when times come.",
    "created_at": "2009-10-15T12:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43532",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:9 robertwb]:
> But then we're back to the same problem of `s.acted_upon_right(p)` not being obvious whether s or p was the one on the right (though it's a bit better). 


It sounds rather clear to me.

> In any case, this behavior is easy to implement in a superclass. 


Yes.

> So, is this a positive review (pending all doctests passing, which they did last I checked)?


Yes, I just wanted to discuss the matter first. Also, part of this may become obsolete once I will have a prototype implementation of overloaded operators/functions as in MuPAD, with a declarative interface (the Sage-combinat people need them anyway for other purposes). I'll post here a link to the appropriate ticket when times come.



---

archive/issue_comments_043533.json:
```json
{
    "body": "Changing keywords from \"\" to \"actions, left actions, right actions\".",
    "created_at": "2009-10-15T12:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43533",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "actions, left actions, right actions".



---

archive/issue_comments_043534.json:
```json
{
    "body": "Attachment [trac_5597-infinite_polynomial_ring.patch](tarball://root/attachments/some-uuid/ticket5597/trac_5597-infinite_polynomial_ring.patch) by @mwhansen created at 2009-10-21 06:03:57",
    "created_at": "2009-10-21T06:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43534",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5597-infinite_polynomial_ring.patch](tarball://root/attachments/some-uuid/ticket5597/trac_5597-infinite_polynomial_ring.patch) by @mwhansen created at 2009-10-21 06:03:57



---

archive/issue_comments_043535.json:
```json
{
    "body": "I've attached trac_5597.patch which is all the the relevant patches folded together and then rebased.\n\nI also attached trac_5597-infinite_polynomial_ring.patch which fixes some failures since an_element was returning a \"generator\" and not an actual element.",
    "created_at": "2009-10-21T06:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43535",
    "user": "https://github.com/mwhansen"
}
```

I've attached trac_5597.patch which is all the the relevant patches folded together and then rebased.

I also attached trac_5597-infinite_polynomial_ring.patch which fixes some failures since an_element was returning a "generator" and not an actual element.



---

archive/issue_comments_043536.json:
```json
{
    "body": "I applied just [attachment:trac_5597-infinite_polynomial_ring.patch] to 4.2.alpha0 and doctested `sage/rings/polynomial/infinite_polynomial_ring.py`.  Positive review for this patch.",
    "created_at": "2009-10-21T06:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43536",
    "user": "https://github.com/qed777"
}
```

I applied just [attachment:trac_5597-infinite_polynomial_ring.patch] to 4.2.alpha0 and doctested `sage/rings/polynomial/infinite_polynomial_ring.py`.  Positive review for this patch.



---

archive/issue_events_013186.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-21T06:18:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5597#event-13186"
}
```



---

archive/issue_comments_043537.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T06:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43537",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_043538.json:
```json
{
    "body": "Merged trac_5597.patch and trac_5597-infinite_polynomial_ring.patch in sage-4.2.alpha1.",
    "created_at": "2009-10-21T06:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43538",
    "user": "https://github.com/mwhansen"
}
```

Merged trac_5597.patch and trac_5597-infinite_polynomial_ring.patch in sage-4.2.alpha1.



---

archive/issue_comments_043539.json:
```json
{
    "body": "Thanks! It's so good to finally see all these coercion and category patches go in.",
    "created_at": "2009-10-21T06:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43539",
    "user": "https://github.com/robertwb"
}
```

Thanks! It's so good to finally see all these coercion and category patches go in.



---

archive/issue_comments_043540.json:
```json
{
    "body": "Me too! Thanks for doing them!",
    "created_at": "2009-10-21T06:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5597#issuecomment-43540",
    "user": "https://github.com/mwhansen"
}
```

Me too! Thanks for doing them!
