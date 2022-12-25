# Issue 7522: Implement orthogonal complement in vector spaces

archive/issues_007522.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @rbeezer\n\nIt should be easy to get the orthogonal complement of a subspace W of a vector space V.   From Jason Grout: \n\n```\nsage: def orthogonal_complement(space):\n....:     if space.dimension()==0:\n....:         return space.ambient_vector_space()\n....:     else:\n....:         return space.basis_matrix().right_kernel()\n```\n\nOne would also want to add an option to specify the larger space in which you were dealing, with it defaulting to the ambient vector space.  Probably 'perp()' should be an alias.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7522\n\n",
    "created_at": "2009-11-24T01:27:57Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "Implement orthogonal complement in vector spaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7522",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

CC:  @jasongrout @rbeezer

It should be easy to get the orthogonal complement of a subspace W of a vector space V.   From Jason Grout: 

```
sage: def orthogonal_complement(space):
....:     if space.dimension()==0:
....:         return space.ambient_vector_space()
....:     else:
....:         return space.basis_matrix().right_kernel()
```

One would also want to add an option to specify the larger space in which you were dealing, with it defaulting to the ambient vector space.  Probably 'perp()' should be an alias.

Issue created by migration from https://trac.sagemath.org/ticket/7522





---

archive/issue_comments_063619.json:
```json
{
    "body": "Attachment [7522-perp.patch](tarball://root/attachments/some-uuid/ticket7522/7522-perp.patch) by @jasongrout created at 2010-09-22 03:02:04",
    "created_at": "2010-09-22T03:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63619",
    "user": "https://github.com/jasongrout"
}
```

Attachment [7522-perp.patch](tarball://root/attachments/some-uuid/ticket7522/7522-perp.patch) by @jasongrout created at 2010-09-22 03:02:04



---

archive/issue_comments_063620.json:
```json
{
    "body": "This adds the basic orthogonal complement command.  Specifying a larger space can go on another ticket, if someone wants it.",
    "created_at": "2010-09-22T03:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63620",
    "user": "https://github.com/jasongrout"
}
```

This adds the basic orthogonal complement command.  Specifying a larger space can go on another ticket, if someone wants it.



---

archive/issue_comments_063621.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T03:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63621",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063622.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> This adds the basic orthogonal complement command.  Specifying a larger space can go on another ticket, if someone wants it.\nThanks for doing this - I never got to it, since I haven't used this lately.   Agreed on the enhancement.\n\nThe documentation should make it clear what the ambient space is by default, perhaps by adding an example where things fail?  Or at least commenting that the first example just shows itself as the ambient space.  What would happen if one took a double subspace - what would it consider to be the ambient subspace?",
    "created_at": "2010-09-23T00:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63622",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:1 jason]:
> This adds the basic orthogonal complement command.  Specifying a larger space can go on another ticket, if someone wants it.
Thanks for doing this - I never got to it, since I haven't used this lately.   Agreed on the enhancement.

The documentation should make it clear what the ambient space is by default, perhaps by adding an example where things fail?  Or at least commenting that the first example just shows itself as the ambient space.  What would happen if one took a double subspace - what would it consider to be the ambient subspace?



---

archive/issue_comments_063623.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-09-23T23:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63623",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_063624.json:
```json
{
    "body": "Attachment [7522-review.patch](tarball://root/attachments/some-uuid/ticket7522/7522-review.patch) by @jasongrout created at 2010-09-23 23:28:31\n\nReplying to [comment:2 kcrisman]:\n\n\n> The documentation should make it clear what the ambient space is by default, perhaps by adding an example where things fail?  Or at least commenting that the first example just shows itself as the ambient space.  What would happen if one took a double subspace - what would it consider to be the ambient subspace?  \n\nReview patch attached.  Better now?",
    "created_at": "2010-09-23T23:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63624",
    "user": "https://github.com/jasongrout"
}
```

Attachment [7522-review.patch](tarball://root/attachments/some-uuid/ticket7522/7522-review.patch) by @jasongrout created at 2010-09-23 23:28:31

Replying to [comment:2 kcrisman]:


> The documentation should make it clear what the ambient space is by default, perhaps by adding an example where things fail?  Or at least commenting that the first example just shows itself as the ambient space.  What would happen if one took a double subspace - what would it consider to be the ambient subspace?  

Review patch attached.  Better now?



---

archive/issue_comments_063625.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-27T12:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63625",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063626.json:
```json
{
    "body": "I got a chance to look at this over the weekend.  Unsurprisingly, in general it's great.  But...\n\nSince this is in the free module module (!), there should be a better error for \n\n```\nsage: c = FreeModule(Integers(8), 2)\nsage: c.perp()\n---------------------------------------------------------------------------\n<snip>\nNotImplementedError: Don't know how to compute kernels over Ring of integers modulo 8\n```\n\nI also noticed the following behavior, which is probably desirable, but which should then definitely be explicitly mentioned in the documentation for this function, since it does return a different type of object for the perp object:\n\n```\nsage: c = FreeModule(ZZ, 2)\nsage: c\nAmbient free module of rank 2 over the principal ideal domain Integer Ring\nsage: c.perp()\nVector space of degree 2 and dimension 0 over Rational Field\nBasis matrix:\n[]\n```\n",
    "created_at": "2010-09-27T12:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63626",
    "user": "https://github.com/kcrisman"
}
```

I got a chance to look at this over the weekend.  Unsurprisingly, in general it's great.  But...

Since this is in the free module module (!), there should be a better error for 

```
sage: c = FreeModule(Integers(8), 2)
sage: c.perp()
---------------------------------------------------------------------------
<snip>
NotImplementedError: Don't know how to compute kernels over Ring of integers modulo 8
```

I also noticed the following behavior, which is probably desirable, but which should then definitely be explicitly mentioned in the documentation for this function, since it does return a different type of object for the perp object:

```
sage: c = FreeModule(ZZ, 2)
sage: c
Ambient free module of rank 2 over the principal ideal domain Integer Ring
sage: c.perp()
Vector space of degree 2 and dimension 0 over Rational Field
Basis matrix:
[]
```




---

archive/issue_comments_063627.json:
```json
{
    "body": "By the way, why didn't `TestSuite` catch this?\n\n```\n    sage: M = ZZ^3\n    sage: TestSuite(M).run()\n    sage: W = M.span_of_basis([[1,2,3],[4,5,19]])\n    sage: TestSuite(W).run()\n```\n",
    "created_at": "2010-09-27T20:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63627",
    "user": "https://github.com/kcrisman"
}
```

By the way, why didn't `TestSuite` catch this?

```
    sage: M = ZZ^3
    sage: TestSuite(M).run()
    sage: W = M.span_of_basis([[1,2,3],[4,5,19]])
    sage: TestSuite(W).run()
```




---

archive/issue_comments_063628.json:
```json
{
    "body": "I've uploaded a new version of the patch which moves the `perp()` method to the free module with the PID as a base ring (so you shouldn't get the `NotImplementedError`) and made sure the submodules have the correct base rings.",
    "created_at": "2013-04-04T22:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63628",
    "user": "https://github.com/tscrim"
}
```

I've uploaded a new version of the patch which moves the `perp()` method to the free module with the PID as a base ring (so you shouldn't get the `NotImplementedError`) and made sure the submodules have the correct base rings.



---

archive/issue_comments_063629.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-04-04T22:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63629",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063630.json:
```json
{
    "body": "For patchbot:\n\nApply: trac_7522-perp-ts.patch",
    "created_at": "2013-04-04T22:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63630",
    "user": "https://github.com/tscrim"
}
```

For patchbot:

Apply: trac_7522-perp-ts.patch



---

archive/issue_comments_063631.json:
```json
{
    "body": "`perp()` isn't documented in this patch.  Also,\n\n```\nsage: c = FreeModule(Integers(8), 2)\nsage: c.perp()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\nAttributeError: 'FreeModule_ambient_with_category' object has no attribute 'perp'\n<and later>\nAttributeError: 'IntegerModRing_generic_with_category' object has no attribute 'parent'\n```\n\nApparently `Integers(8)` isn't a PID, according to Sage?  This isn't bad, but perhaps we should have a different error message... or maybe this is okay.",
    "created_at": "2013-04-05T00:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63631",
    "user": "https://github.com/kcrisman"
}
```

`perp()` isn't documented in this patch.  Also,

```
sage: c = FreeModule(Integers(8), 2)
sage: c.perp()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
AttributeError: 'FreeModule_ambient_with_category' object has no attribute 'perp'
<and later>
AttributeError: 'IntegerModRing_generic_with_category' object has no attribute 'parent'
```

Apparently `Integers(8)` isn't a PID, according to Sage?  This isn't bad, but perhaps we should have a different error message... or maybe this is okay.



---

archive/issue_comments_063632.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-04-05T00:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63632",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063633.json:
```json
{
    "body": "Also, would it be better to do the kernel first and then change the ring?  Just wondering if there might be any difference.",
    "created_at": "2013-04-05T00:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63633",
    "user": "https://github.com/kcrisman"
}
```

Also, would it be better to do the kernel first and then change the ring?  Just wondering if there might be any difference.



---

archive/issue_comments_063634.json:
```json
{
    "body": "- You only have an orthogonal complement on an inner product space.\n  - Whenever you have a canonical isomorphism between a vector space and its dual, you can do the \"kernel trick\" that you're doing (note you have to take a transpose somewhere). A basis choice induces such a canonical isomorphism, as does an inner product. For every subspace `W subset V` it gives you a complementary subspace `W'` such that V is a direct product of `W` and `W'`.\n  - For (free) modules over rings this doesn't really work, because not every submodule is a direct summand.\n  - Of course, if your ring is a domain, you can tensor with the field of fractions, take the complement, and intersect with the module inside to get another submodule. Doing that twice should get you the \"saturation\" of your original module.\n\nI suggest you don't call it orthogonal complement. For instance, on vector spaces over finite fields, it's not (but a basis choice still induces an isomorphism to the dual).",
    "created_at": "2013-04-05T01:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63634",
    "user": "https://github.com/nbruin"
}
```

- You only have an orthogonal complement on an inner product space.
  - Whenever you have a canonical isomorphism between a vector space and its dual, you can do the "kernel trick" that you're doing (note you have to take a transpose somewhere). A basis choice induces such a canonical isomorphism, as does an inner product. For every subspace `W subset V` it gives you a complementary subspace `W'` such that V is a direct product of `W` and `W'`.
  - For (free) modules over rings this doesn't really work, because not every submodule is a direct summand.
  - Of course, if your ring is a domain, you can tensor with the field of fractions, take the complement, and intersect with the module inside to get another submodule. Doing that twice should get you the "saturation" of your original module.

I suggest you don't call it orthogonal complement. For instance, on vector spaces over finite fields, it's not (but a basis choice still induces an isomorphism to the dual).



---

archive/issue_comments_063635.json:
```json
{
    "body": ">  - You only have an orthogonal complement on an inner product space.\n>  - Whenever you have a canonical isomorphism between a vector space and its dual, you can do the \"kernel trick\" that you're doing (note you have to take a transpose somewhere). A basis choice induces such a canonical isomorphism, as does an inner product. For every subspace `W subset V` it gives you a complementary subspace `W'` such that V is a direct product of `W` and `W'`.\n>  - For (free) modules over rings this doesn't really work, because not every submodule is a direct summand.\nAargh!  You had to go remind us of the whole mathematical correctness thing.  You're right, of course.  Not every submodule is projective.\n>  - Of course, if your ring is a domain, you can tensor with the field of fractions, take the complement, and intersect with the module inside to get another submodule. Doing that twice should get you the \"saturation\" of your original module.\n> I suggest you don't call it orthogonal complement. For instance, on vector spaces over finite fields, it's not (but a basis choice still induces an isomorphism to the dual).\nThen what do you suggest?  Since this is primarily useful for pedagogical purposes, perhaps we can just raise an error outside of QQ, RR, and friends.  In particular, I think it's definitely appropriate to not allow this for anything but vector spaces.\n\nOne interesting thing is that Sage is already doing something analogous to your suggestion about tensoring in getting the \"basis matrix\", which led to the workaround Travis made.  Then again,\n\n```\nVector space of degree 3 and dimension 2 over Integer Ring\n```\n\nshouldn't even be legal to appear in Sage, in some sense...",
    "created_at": "2013-04-05T01:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63635",
    "user": "https://github.com/kcrisman"
}
```

>  - You only have an orthogonal complement on an inner product space.
>  - Whenever you have a canonical isomorphism between a vector space and its dual, you can do the "kernel trick" that you're doing (note you have to take a transpose somewhere). A basis choice induces such a canonical isomorphism, as does an inner product. For every subspace `W subset V` it gives you a complementary subspace `W'` such that V is a direct product of `W` and `W'`.
>  - For (free) modules over rings this doesn't really work, because not every submodule is a direct summand.
Aargh!  You had to go remind us of the whole mathematical correctness thing.  You're right, of course.  Not every submodule is projective.
>  - Of course, if your ring is a domain, you can tensor with the field of fractions, take the complement, and intersect with the module inside to get another submodule. Doing that twice should get you the "saturation" of your original module.
> I suggest you don't call it orthogonal complement. For instance, on vector spaces over finite fields, it's not (but a basis choice still induces an isomorphism to the dual).
Then what do you suggest?  Since this is primarily useful for pedagogical purposes, perhaps we can just raise an error outside of QQ, RR, and friends.  In particular, I think it's definitely appropriate to not allow this for anything but vector spaces.

One interesting thing is that Sage is already doing something analogous to your suggestion about tensoring in getting the "basis matrix", which led to the workaround Travis made.  Then again,

```
Vector space of degree 3 and dimension 2 over Integer Ring
```

shouldn't even be legal to appear in Sage, in some sense...



---

archive/issue_comments_063636.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> Then what do you suggest?  Since this is primarily useful for pedagogical purposes, perhaps we can just raise an error outside of QQ, RR, and friends.\n\nEven there it's only wrt the standard inner product (i.e., if your basis is orthogonal) that this complement is *orthogonal*.\n\nWouldn't just `complement` work? I think that's a reasonably established term for direct cofactor.\n\nAnd indeed, you should probably only offer this for vector spaces, i.e., when the base ring is a field.",
    "created_at": "2013-04-05T03:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63636",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:12 kcrisman]:
> Then what do you suggest?  Since this is primarily useful for pedagogical purposes, perhaps we can just raise an error outside of QQ, RR, and friends.

Even there it's only wrt the standard inner product (i.e., if your basis is orthogonal) that this complement is *orthogonal*.

Wouldn't just `complement` work? I think that's a reasonably established term for direct cofactor.

And indeed, you should probably only offer this for vector spaces, i.e., when the base ring is a field.



---

archive/issue_comments_063637.json:
```json
{
    "body": "First, if the ring is not a PID, there are many attributes that are not there anymore (ex. `span()`), so getting the attribute error is consistent with the rest of free modules.\n\nAs for them being inner product spaces, we have this in sage:\n\n```\nsage: F = FreeModule(Integers(8), 3)\nsage: v = F([1, 2, 3])\nsage: v*v\n6\nsage: F.inner_product_matrix()\n[1 0 0]\n[0 1 0]\n[0 0 1]\n```\n\nso I think sage always assumes it has an inner product (although not necessarily a nice inner product).\n\nFor the\n\n```\nVector space of degree 3 and dimension 2 over Integer Ring\n```\n\nthat was a doctest error coming from me thinking I know what the output should be >_<.\n\nAnyways, new version of the patch with the method now called `complement()`, removed `perp()`, and only works for vector spaces.\n\nFor patchbot:\n\nApply: trac_7522-perp-ts.patch",
    "created_at": "2013-04-05T16:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63637",
    "user": "https://github.com/tscrim"
}
```

First, if the ring is not a PID, there are many attributes that are not there anymore (ex. `span()`), so getting the attribute error is consistent with the rest of free modules.

As for them being inner product spaces, we have this in sage:

```
sage: F = FreeModule(Integers(8), 3)
sage: v = F([1, 2, 3])
sage: v*v
6
sage: F.inner_product_matrix()
[1 0 0]
[0 1 0]
[0 0 1]
```

so I think sage always assumes it has an inner product (although not necessarily a nice inner product).

For the

```
Vector space of degree 3 and dimension 2 over Integer Ring
```

that was a doctest error coming from me thinking I know what the output should be >_<.

Anyways, new version of the patch with the method now called `complement()`, removed `perp()`, and only works for vector spaces.

For patchbot:

Apply: trac_7522-perp-ts.patch



---

archive/issue_comments_063638.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-04-05T16:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63638",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063639.json:
```json
{
    "body": "Question for Jason and Rob: for teaching linear algebra, would it be useful to have `complement` but not `perp` or `orthogonal_complement`?  I think that the standard basis is always kind of implicit in such situations; we aren't asking for complements with respect to other (orthogonal or not) bases with this function, or at least originally weren't.",
    "created_at": "2013-04-05T17:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63639",
    "user": "https://github.com/kcrisman"
}
```

Question for Jason and Rob: for teaching linear algebra, would it be useful to have `complement` but not `perp` or `orthogonal_complement`?  I think that the standard basis is always kind of implicit in such situations; we aren't asking for complements with respect to other (orthogonal or not) bases with this function, or at least originally weren't.



---

archive/issue_comments_063640.json:
```json
{
    "body": "Rather than testing if the base ring is a field, shouldn't you place the method on `sage.modules.free_module.FreeModule_generic_field` or something like that? The usual idea is to let inheritance take care of which methods are available rather than explicit argument checking wherever possible.",
    "created_at": "2013-04-05T17:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63640",
    "user": "https://github.com/nbruin"
}
```

Rather than testing if the base ring is a field, shouldn't you place the method on `sage.modules.free_module.FreeModule_generic_field` or something like that? The usual idea is to let inheritance take care of which methods are available rather than explicit argument checking wherever possible.



---

archive/issue_comments_063641.json:
```json
{
    "body": "Attachment [trac_7522-perp-ts.patch](tarball://root/attachments/some-uuid/ticket7522/trac_7522-perp-ts.patch) by @tscrim created at 2013-04-05 18:46:26\n\nHere I was looking for something called `VectorSpace`... Done. Now just waiting on a response from Rob or Jason.",
    "created_at": "2013-04-05T18:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63641",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_7522-perp-ts.patch](tarball://root/attachments/some-uuid/ticket7522/trac_7522-perp-ts.patch) by @tscrim created at 2013-04-05 18:46:26

Here I was looking for something called `VectorSpace`... Done. Now just waiting on a response from Rob or Jason.



---

archive/issue_comments_063642.json:
```json
{
    "body": "I've just discussed this with Rob and Jason at Sage Days 48.  The consensus is that the solution here is acceptable.\n\nPatchbot, apply: trac_7522-perp-ts.patch",
    "created_at": "2013-06-18T23:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63642",
    "user": "https://github.com/kcrisman"
}
```

I've just discussed this with Rob and Jason at Sage Days 48.  The consensus is that the solution here is acceptable.

Patchbot, apply: trac_7522-perp-ts.patch



---

archive/issue_comments_063643.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd48\".",
    "created_at": "2013-06-18T23:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63643",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "sd48".



---

archive/issue_comments_063644.json:
```json
{
    "body": "I'm going to add an example pointing out that over a finite field this gives a complement which intersects the original subspace, which 3 people here say is fine (in the sense that it's not wrong, but we should just point out it's not what one might expect from the \"usual\" case).  Nils, is it okay as long as we don't call it orthogonal?",
    "created_at": "2013-06-18T23:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63644",
    "user": "https://github.com/kcrisman"
}
```

I'm going to add an example pointing out that over a finite field this gives a complement which intersects the original subspace, which 3 people here say is fine (in the sense that it's not wrong, but we should just point out it's not what one might expect from the "usual" case).  Nils, is it okay as long as we don't call it orthogonal?



---

archive/issue_comments_063645.json:
```json
{
    "body": "Okay, Travis and/or Nils and/or anyone else, is this okay?  The terminology is really the issue here, but hopefully this will satisfy everyone.\n\nPatchbot, apply trac_7522-perp-ts.patch and trac_7522-finite.patch",
    "created_at": "2013-06-18T23:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63645",
    "user": "https://github.com/kcrisman"
}
```

Okay, Travis and/or Nils and/or anyone else, is this okay?  The terminology is really the issue here, but hopefully this will satisfy everyone.

Patchbot, apply trac_7522-perp-ts.patch and trac_7522-finite.patch



---

archive/issue_comments_063646.json:
```json
{
    "body": "There's a small typo:\n\n```\na a vector\n```\n\nonce that is fixed, I'm fine with this being set to positive reivew (but I'm probably one of the less opinionated people on this). Feel free to do this on my behalf because I'm going to sleep now to be ready for more Sage Days 49. Hope the 48 is going well.\n\nTravis",
    "created_at": "2013-06-18T23:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63646",
    "user": "https://github.com/tscrim"
}
```

There's a small typo:

```
a a vector
```

once that is fixed, I'm fine with this being set to positive reivew (but I'm probably one of the less opinionated people on this). Feel free to do this on my behalf because I'm going to sleep now to be ready for more Sage Days 49. Hope the 48 is going well.

Travis



---

archive/issue_comments_063647.json:
```json
{
    "body": "Attachment [trac_7522-finite.patch](tarball://root/attachments/some-uuid/ticket7522/trac_7522-finite.patch) by @kcrisman created at 2013-06-18 23:59:32\n\nThanks, fixed.\n\nPatchbot, apply trac_7522-perp-ts.patch and trac_7522-finite.patch",
    "created_at": "2013-06-18T23:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63647",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_7522-finite.patch](tarball://root/attachments/some-uuid/ticket7522/trac_7522-finite.patch) by @kcrisman created at 2013-06-18 23:59:32

Thanks, fixed.

Patchbot, apply trac_7522-perp-ts.patch and trac_7522-finite.patch



---

archive/issue_comments_063648.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-20T00:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63648",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007751.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-06-20T21:33:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7522#event-7751"
}
```



---

archive/issue_comments_063649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-20T21:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7522#issuecomment-63649",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
