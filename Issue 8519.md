# Issue 8519: Add a set of Positive Integer with categories (and factor the code with NonNegativeInteger)

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-03-13 11:33:46

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



---

Comment by nthiery created at 2010-03-13 11:42:16

+1!

That will be useful for NCSF too (see the beginning of sage/combinat/ncsf/categories.py).

Just mind the 's': PositiveIntegers

Let me guess: TransitiveGroup(0,1) does not work, right? Maybe it should actually?


---

Comment by nborie created at 2010-03-13 11:51:29

Changing keywords from "positive integer" to "range, categories, set, integer".


---

Comment by nborie created at 2010-03-13 11:53:59

Hello Nicolas, will you set a +2 with the new description ?


---

Comment by nthiery created at 2010-03-13 12:15:29

Replying to [comment:5 nborie]:
> Hello Nicolas, will you set a +2 with the new description ?

Yes. I just spent 5 minutes discussing about this with Florent over the phone. In the end, we vote for IntegerRange(a,b, step=c), and NonNegativeIntegers / PositiveIntegers being subclasses (to add further properties; like the fact that they are semigroups/monoids/semirings/....).


---

Comment by saliola created at 2010-03-13 14:21:15

+1 for `IntegerRange` instead of `Range`.


---

Comment by nborie created at 2010-03-13 16:13:31

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

Comment by nborie created at 2010-03-13 17:14:16

The __contains__ function is false. It works only for IntegerRange(-Infinity,Infinity,a,b)...


---

Comment by nborie created at 2010-03-13 21:09:22

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

Comment by hivert created at 2010-03-13 22:00:07

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

Comment by nborie created at 2010-03-14 18:56:39

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-14 18:56:39

This last version begin to be final...

I didn't manage to attach PositiveInteger to the reference manual. The docbuild was always saying :
UNABLE TO FIND THE MODULE. Even after 3421 checks, I didn't succeed...


---

Attachment


---

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

Comment by hivert created at 2010-03-15 20:18:35

I had a second though and decided that `_from_integer_` was a little overkill. I removed it.

Cheers,

Florent


---

Attachment


---

Attachment

Hi Florent,

I am very Ok with your changes! To complete this review, please check the 3 hyperlinks I just fixed in positive_integers.py and non_negative_integers.py. That's will be a very easy review I think.

Patchs to be applied :

trac_8519_Range_factory-nb.patch
trac_8519_Range_factory-review-fh.2.patch
trac_8519_Range_factory-review2-nb.patch

Thanks for all.


---

Comment by hivert created at 2010-03-21 22:01:43

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-03-21 22:01:43

Patch looks good, ready to go.

Florent


---

Comment by nborie created at 2010-03-21 22:33:26

My last comment was not well formatted, so for the release manager, please apply : 

 *  trac_8519_Range_factory-nb.patch 
 *  trac_8519_Range_factory-review-fh.2.patch 
 *  trac_8519_Range_factory-review2-nb.patch

Thanks for all.
Nicolas.


---

Comment by hivert created at 2010-04-16 12:33:57

Replying to [comment:17 nborie]:
> My last comment was not well formatted, so for the release manager, please apply : 
 
 *  trac_8519_Range_factory-nb.patch 
 *  trac_8519_Range_factory-review-fh.2.patch 
 *  trac_8519_Range_factory-review2-nb.patch

Reviewing this I noticed that we forgot to mention that this depends on #8524

Florent


---

Comment by jhpalmieri created at 2010-04-16 18:28:19

Replying to [comment:18 hivert]:
> Reviewing this I noticed that we forgot to mention that this depends on #8524

In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?


---

Comment by nthiery created at 2010-04-16 23:21:50

Replying to [comment:19 jhpalmieri]:
> Replying to [comment:18 hivert]:
> > Reviewing this I noticed that we forgot to mention that this depends on #8524
> 
> In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?

Done (well, almost; Florent just need to check my changes). The dependency is functional, not syntactical. I would have expected the tests to fail without #8524! Maybe the problem that was encountered and triggered the writting of #8524 did not end up being doctested, which would be bad!


---

Comment by hivert created at 2010-04-16 23:52:57

Replying to [comment:19 jhpalmieri]:
> Replying to [comment:18 hivert]:
> > Reviewing this I noticed that we forgot to mention that this depends on #8524
> 
> In what way does it depend on it?  I've merged the three patches into a prototype for Sage 4.4.alpha0, and all tests pass.  Do I need to back that change out now?  Or can someone review #8524 quickly (and thoroughly)?

My mistake ! Forget about my comment.


---

Comment by jhpalmieri created at 2010-04-17 02:50:09

Merged in 4.4.alpha0:
 - trac_8519_Range_factory-nb.patch 
 - trac_8519_Range_factory-review-fh.2.patch
 - trac_8519_Range_factory-review2-nb.patch


---

Comment by jhpalmieri created at 2010-04-17 02:50:09

Resolution: fixed
