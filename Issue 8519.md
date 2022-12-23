# Issue 8519: Add a set of Positive Integer with categories (and factor the code with NonNegativeInteger)

archive/issues_008519.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat\n\nKeywords: positive integer\n\nWe have already a proper set with category of NonNegativeIntegers, let's use it to also define PositiveInteger\n\n\n```\nsage: NonNegativeIntegers()\nNon negative integers\nsage: PositiveInteger()\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/home/nicolas/<ipython console> in <module>()\n\nNameError: name 'PositiveInteger' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8519\n\n",
    "created_at": "2010-03-13T11:33:46Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Add a set of Positive Integer with categories (and factor the code with NonNegativeInteger)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8519",
    "user": "nborie"
}
```
Assignee: nborie

CC:  sage-combinat

Keywords: positive integer

We have already a proper set with category of NonNegativeIntegers, let's use it to also define PositiveInteger


```
sage: NonNegativeIntegers()
Non negative integers
sage: PositiveInteger()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/nicolas/<ipython console> in <module>()

NameError: name 'PositiveInteger' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/8519





---

archive/issue_comments_076940.json:
```json
{
    "body": "+1!\n\nThat will be useful for NCSF too (see the beginning of sage/combinat/ncsf/categories.py).\n\nJust mind the 's': PositiveIntegers\n\nLet me guess: TransitiveGroup(0,1) does not work, right? Maybe it should actually?",
    "created_at": "2010-03-13T11:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76940",
    "user": "nthiery"
}
```

+1!

That will be useful for NCSF too (see the beginning of sage/combinat/ncsf/categories.py).

Just mind the 's': PositiveIntegers

Let me guess: TransitiveGroup(0,1) does not work, right? Maybe it should actually?



---

archive/issue_comments_076941.json:
```json
{
    "body": "Changing keywords from \"positive integer\" to \"range, categories, set, integer\".",
    "created_at": "2010-03-13T11:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76941",
    "user": "nborie"
}
```

Changing keywords from "positive integer" to "range, categories, set, integer".



---

archive/issue_comments_076942.json:
```json
{
    "body": "Hello Nicolas, will you set a +2 with the new description ?",
    "created_at": "2010-03-13T11:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76942",
    "user": "nborie"
}
```

Hello Nicolas, will you set a +2 with the new description ?



---

archive/issue_comments_076943.json:
```json
{
    "body": "Replying to [comment:5 nborie]:\n> Hello Nicolas, will you set a +2 with the new description ?\n\nYes. I just spent 5 minutes discussing about this with Florent over the phone. In the end, we vote for IntegerRange(a,b, step=c), and NonNegativeIntegers / PositiveIntegers being subclasses (to add further properties; like the fact that they are semigroups/monoids/semirings/....).",
    "created_at": "2010-03-13T12:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76943",
    "user": "nthiery"
}
```

Replying to [comment:5 nborie]:
> Hello Nicolas, will you set a +2 with the new description ?

Yes. I just spent 5 minutes discussing about this with Florent over the phone. In the end, we vote for IntegerRange(a,b, step=c), and NonNegativeIntegers / PositiveIntegers being subclasses (to add further properties; like the fact that they are semigroups/monoids/semirings/....).



---

archive/issue_comments_076944.json:
```json
{
    "body": "+1 for `IntegerRange` instead of `Range`.",
    "created_at": "2010-03-13T14:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76944",
    "user": "saliola"
}
```

+1 for `IntegerRange` instead of `Range`.



---

archive/issue_comments_076945.json:
```json
{
    "body": "So guys,\n\nI add a patch with a first implementation...\n\nQuestions:\n- First, if you find a language mistake, please tell me.\n- What should I keep, what should I drop in NonNegativeIntegers ?\n- Does IntegerRange need an _element_constructor_ method ?\n- What should I had in PositiveIntegers (easy thing please) ?\n- Do you want to tell me about your day ?\n- Any comment ....\n\nThanks for further advises.",
    "created_at": "2010-03-13T16:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76945",
    "user": "nborie"
}
```

So guys,

I add a patch with a first implementation...

Questions:
- First, if you find a language mistake, please tell me.
- What should I keep, what should I drop in NonNegativeIntegers ?
- Does IntegerRange need an _element_constructor_ method ?
- What should I had in PositiveIntegers (easy thing please) ?
- Do you want to tell me about your day ?
- Any comment ....

Thanks for further advises.



---

archive/issue_comments_076946.json:
```json
{
    "body": "The __contains__ function is false. It works only for IntegerRange(-Infinity,Infinity,a,b)...",
    "created_at": "2010-03-13T17:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76946",
    "user": "nborie"
}
```

The __contains__ function is false. It works only for IntegerRange(-Infinity,Infinity,a,b)...



---

archive/issue_comments_076947.json:
```json
{
    "body": "Ok, after think a while...\n\nI will update this code and give IntegerRange the behavior of range() if and only if someone (else than me) can give me an empty set with categories which can pass the tests....\n\n```\nsage: TestSuite(Set([])).run()\nThe following tests failed: _test_an_element, _test_category, _test_elements, _test_some_elements\n```\n\nI need this feature for coherence!! Python range easily give out an empty list like:\n\n```\nsage: range(1,20,-1)\n[]\nsage: range(20,1,1)\n[]\n```\n\nAdding - and + Infinity, we will have a lot of arguments which will build an emptyset. Currently, I did not find a good empty set with categories.\n\nMy code does not allow negative ``step`` and check that ``begin`` < ``end`` to avoid the empty case.\n\nOn other hand, my current status is:\nBenchmarks for my PhD Thesis --> add number_of_transitive_group --> Add enumerated set of TransitiveGroups() --> Add PositiveInteger --> Add IntegerRange feature --> MAX DEPTH OF RECURSION...\n\nAs this EmptySet (with categories) is an empty thing, I have an idea of who can implemented that ?",
    "created_at": "2010-03-13T21:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76947",
    "user": "nborie"
}
```

Ok, after think a while...

I will update this code and give IntegerRange the behavior of range() if and only if someone (else than me) can give me an empty set with categories which can pass the tests....

```
sage: TestSuite(Set([])).run()
The following tests failed: _test_an_element, _test_category, _test_elements, _test_some_elements
```

I need this feature for coherence!! Python range easily give out an empty list like:

```
sage: range(1,20,-1)
[]
sage: range(20,1,1)
[]
```

Adding - and + Infinity, we will have a lot of arguments which will build an emptyset. Currently, I did not find a good empty set with categories.

My code does not allow negative ``step`` and check that ``begin`` < ``end`` to avoid the empty case.

On other hand, my current status is:
Benchmarks for my PhD Thesis --> add number_of_transitive_group --> Add enumerated set of TransitiveGroups() --> Add PositiveInteger --> Add IntegerRange feature --> MAX DEPTH OF RECURSION...

As this EmptySet (with categories) is an empty thing, I have an idea of who can implemented that ?



---

archive/issue_comments_076948.json:
```json
{
    "body": "Replying to [comment:10 nborie]:\n> I will update this code and give IntegerRange the behavior of range() if and only if someone (else than me) can give me an empty set with categories which can pass the tests....\n> {{{\n> sage: TestSuite(Set([])).run()\n> The following tests failed: _test_an_element, _test_category, _test_elements, _test_some_elements\n> }}}\n\nFor consintency of the category you should use an `EnumeratedSet` rather than a `Set`:\n\n```\nsage: f = FiniteEnumeratedSet([])\nsage: TestSuite(f).run()\n[...]\nThe following tests failed: _test_an_element, _test_elements, _test_some_elements\n```\n\nYou can't expect to get anything better than that with the current specification of sets: All those three tests are buggy in the sense that they suppose that there is at least one element in the set. So forget about it and don't run TestSuite on an empty set until we fix this.",
    "created_at": "2010-03-13T22:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76948",
    "user": "hivert"
}
```

Replying to [comment:10 nborie]:
> I will update this code and give IntegerRange the behavior of range() if and only if someone (else than me) can give me an empty set with categories which can pass the tests....
> {{{
> sage: TestSuite(Set([])).run()
> The following tests failed: _test_an_element, _test_category, _test_elements, _test_some_elements
> }}}

For consintency of the category you should use an `EnumeratedSet` rather than a `Set`:

```
sage: f = FiniteEnumeratedSet([])
sage: TestSuite(f).run()
[...]
The following tests failed: _test_an_element, _test_elements, _test_some_elements
```

You can't expect to get anything better than that with the current specification of sets: All those three tests are buggy in the sense that they suppose that there is at least one element in the set. So forget about it and don't run TestSuite on an empty set until we fix this.



---

archive/issue_comments_076949.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-14T18:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76949",
    "user": "nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076950.json:
```json
{
    "body": "This last version begin to be final...\n\nI didn't manage to attach PositiveInteger to the reference manual. The docbuild was always saying :\nUNABLE TO FIND THE MODULE. Even after 3421 checks, I didn't succeed...",
    "created_at": "2010-03-14T18:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76950",
    "user": "nborie"
}
```

This last version begin to be final...

I didn't manage to attach PositiveInteger to the reference manual. The docbuild was always saying :
UNABLE TO FIND THE MODULE. Even after 3421 checks, I didn't succeed...



---

archive/issue_comments_076951.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-15T19:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76951",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_076952.json:
```json
{
    "body": "Attachment\n\nHi Nicolas,\n\nI added a review patch which\n- Adds a class factory\n- Adds a cardinality method\n- Improves the doc\n- temporarily solve the handling of empty sets\n\nPlease review it,\n\nExcept for those issues your patch is good,\n\nFlorent",
    "created_at": "2010-03-15T19:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76952",
    "user": "hivert"
}
```

Attachment

Hi Nicolas,

I added a review patch which
- Adds a class factory
- Adds a cardinality method
- Improves the doc
- temporarily solve the handling of empty sets

Please review it,

Except for those issues your patch is good,

Florent



---

archive/issue_comments_076953.json:
```json
{
    "body": "I had a second though and decided that `_from_integer_` was a little overkill. I removed it.\n\nCheers,\n\nFlorent",
    "created_at": "2010-03-15T20:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76953",
    "user": "hivert"
}
```

I had a second though and decided that `_from_integer_` was a little overkill. I removed it.

Cheers,

Florent



---

archive/issue_comments_076954.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-15T23:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76954",
    "user": "nborie"
}
```

Attachment



---

archive/issue_comments_076955.json:
```json
{
    "body": "Attachment\n\nHi Florent,\n\nI am very Ok with your changes! To complete this review, please check the 3 hyperlinks I just fixed in positive_integers.py and non_negative_integers.py. That's will be a very easy review I think.\n\nPatchs to be applied :\n\ntrac_8519_Range_factory-nb.patch\ntrac_8519_Range_factory-review-fh.2.patch\ntrac_8519_Range_factory-review2-nb.patch\n\nThanks for all.",
    "created_at": "2010-03-15T23:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76955",
    "user": "nborie"
}
```

Attachment

Hi Florent,

I am very Ok with your changes! To complete this review, please check the 3 hyperlinks I just fixed in positive_integers.py and non_negative_integers.py. That's will be a very easy review I think.

Patchs to be applied :

trac_8519_Range_factory-nb.patch
trac_8519_Range_factory-review-fh.2.patch
trac_8519_Range_factory-review2-nb.patch

Thanks for all.



---

archive/issue_comments_076956.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-21T22:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76956",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076957.json:
```json
{
    "body": "Patch looks good, ready to go.\n\nFlorent",
    "created_at": "2010-03-21T22:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76957",
    "user": "hivert"
}
```

Patch looks good, ready to go.

Florent



---

archive/issue_comments_076958.json:
```json
{
    "body": "My last comment was not well formatted, so for the release manager, please apply : \n\n*  trac_8519_Range_factory-nb.patch \n*  trac_8519_Range_factory-review-fh.2.patch \n*  trac_8519_Range_factory-review2-nb.patch\n\nThanks for all.\nNicolas.",
    "created_at": "2010-03-21T22:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76958",
    "user": "nborie"
}
```

My last comment was not well formatted, so for the release manager, please apply : 

*  trac_8519_Range_factory-nb.patch 
*  trac_8519_Range_factory-review-fh.2.patch 
*  trac_8519_Range_factory-review2-nb.patch

Thanks for all.
Nicolas.



---

archive/issue_comments_076959.json:
```json
{
    "body": "Replying to [comment:17 nborie]:\n> My last comment was not well formatted, so for the release manager, please apply : \n \n*  trac_8519_Range_factory-nb.patch \n*  trac_8519_Range_factory-review-fh.2.patch \n*  trac_8519_Range_factory-review2-nb.patch\n\nReviewing this I noticed that we forgot to mention that this depends on #8524\n\nFlorent",
    "created_at": "2010-04-16T12:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76959",
    "user": "hivert"
}
```

Replying to [comment:17 nborie]:
> My last comment was not well formatted, so for the release manager, please apply : 
 
*  trac_8519_Range_factory-nb.patch 
*  trac_8519_Range_factory-review-fh.2.patch 
*  trac_8519_Range_factory-review2-nb.patch

Reviewing this I noticed that we forgot to mention that this depends on #8524

Florent



---

archive/issue_comments_076960.json:
```json
{
    "body": "Replying to [comment:18 hivert]:\n> Reviewing this I noticed that we forgot to mention that this depends on #8524\n\nIn what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?",
    "created_at": "2010-04-16T18:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76960",
    "user": "jhpalmieri"
}
```

Replying to [comment:18 hivert]:
> Reviewing this I noticed that we forgot to mention that this depends on #8524

In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?



---

archive/issue_comments_076961.json:
```json
{
    "body": "Replying to [comment:19 jhpalmieri]:\n> Replying to [comment:18 hivert]:\n> > Reviewing this I noticed that we forgot to mention that this depends on #8524\n> \n> In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?\n\nDone (well, almost; Florent just need to check my changes). The dependency is functional, not syntactical. I would have expected the tests to fail without #8524! Maybe the problem that was encountered and triggered the writting of #8524 did not end up being doctested, which would be bad!",
    "created_at": "2010-04-16T23:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76961",
    "user": "nthiery"
}
```

Replying to [comment:19 jhpalmieri]:
> Replying to [comment:18 hivert]:
> > Reviewing this I noticed that we forgot to mention that this depends on #8524
> 
> In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?

Done (well, almost; Florent just need to check my changes). The dependency is functional, not syntactical. I would have expected the tests to fail without #8524! Maybe the problem that was encountered and triggered the writting of #8524 did not end up being doctested, which would be bad!



---

archive/issue_comments_076962.json:
```json
{
    "body": "Replying to [comment:19 jhpalmieri]:\n> Replying to [comment:18 hivert]:\n> > Reviewing this I noticed that we forgot to mention that this depends on #8524\n> \n> In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?\n\nMy mistake ! Forget about my comment.",
    "created_at": "2010-04-16T23:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76962",
    "user": "hivert"
}
```

Replying to [comment:19 jhpalmieri]:
> Replying to [comment:18 hivert]:
> > Reviewing this I noticed that we forgot to mention that this depends on #8524
> 
> In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?

My mistake ! Forget about my comment.



---

archive/issue_comments_076963.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8519_Range_factory-nb.patch \n- trac_8519_Range_factory-review-fh.2.patch\n- trac_8519_Range_factory-review2-nb.patch",
    "created_at": "2010-04-17T02:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76963",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8519_Range_factory-nb.patch 
- trac_8519_Range_factory-review-fh.2.patch
- trac_8519_Range_factory-review2-nb.patch



---

archive/issue_comments_076964.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-17T02:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8519#issuecomment-76964",
    "user": "jhpalmieri"
}
```

Resolution: fixed
