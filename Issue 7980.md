# Issue 7980: Move 'Category with concrete representation' code into Sage

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2010-01-18 18:04:02

Assignee: nthiery

CC:  sage-combinat

This code currently exists on the sage-combinat queue, in the ncsf patch.  It should be put in a more natural place in the category code.


---

Comment by mhansen created at 2010-05-07 15:26:31

Didn't we want Realization rather than Representation?


---

Comment by nthiery created at 2011-01-13 09:20:55

Changing type from defect to enhancement.


---

Comment by nthiery created at 2011-01-13 09:20:55

Changing status from new to needs_work.


---

Comment by SimonKing created at 2011-11-16 10:27:52

Since the ticket description is rather sparse, I'm collecting here some statements that emerged from reading the patch and discussing with Nicolas, who is sitting beside me.

 * It disposes of abstract categories. Hooray!
 * On the one hand, one has (abstract) vectorspaces. A realization of such abstract vector space is given by specific data, for example by a basis, but it should be emphasized that not all realizations of a vector space are necessarily in terms of a basis. So, not any realization of a vectorspace is a "vectorspace with basis".
 * The realizations of a vector space are related by canonical morphisms (for example, change of basis).
 * Is any "vectorspace with basis" a realisation of a vector space? No! There is no gurantee that this specific vectorspace with basis is equiped with the above-mentioned canonical morphisms. 

*__TODO__*

 * The docstring of the class `Category_realization` has no examples. Its `__init__` method should define its arguments and provide a test. `_get_name` is not documented either.
 * Similarly, `Realizations` is undocumented.
 * `Realizations.super_categories()` returns `[Sets()]`. Idea of Nicolas: Add an optional argument `Realizations(parent, category=Bla)`, so that the default for Bla is `Sets()`. The given category will be returned as super category.

 * I tried some example, with comments/questions inserted:
 {{{
sage: C = Algebras(QQ)
sage: C.WithRealizations()
Join of Category of algebras over Rational Field and Category of sets with realizations
 }}}
 Does it really have to be a join category?
 {{{
sage: from sage.categories.category_types import Category_realization
sage: Category_realization(QQ)
The category of category_realization of Rational Field
 }}}
 So, do I understand correctly that the set of all realisations of `QQ` forms a category, each object being a realisation of `QQ`, the morphisms being canonical maps between the different realisations?
 {{{
sage: Category_realization(QQ).is_subcategory(Rings().WithRealizations())
BOOM
sage: hasattr(Category_realization(QQ), 'super_categories')
False
 }}}
 So, that's a bug. `Category_realization(QQ)` is a category and thus MUST have a `super_categories` method.


*__Is the category of "Bla with realisations" a 2-category?__*

Since Nicolas is now teaching, I can not ask him directly:

 * If I understand correctly, for any parent P there is a _category_ `Category_realizations(P)`.
 * For any category C, there is a category `C.WithRealizations()`.
 * Shouldn't it be the case that for any `P in C`, the realisations of P (thus, the _category_ `Category_realizations(P)`) is an object in `C.WithRealizations()`?
 * But if the objects of `C.WithRealizations()` are categories themselves, shouldn't we first implement the notion of higher categories in Sage, before we treat the category of realizations of objects of C?


---

Comment by SimonKing created at 2011-11-16 14:32:02

Replying to [comment:5 SimonKing]:
> *__Is the category of "Bla with realisations" a 2-category?__*

No, it isn't. I had a totally wrong notion of a higher category. Sorry.

Anyway, the missing super_categories method must be provided (as for any category).


---

Comment by nthiery created at 2012-02-09 18:07:40

Changing keywords from "" to "Cernay2012".


---

Comment by nthiery created at 2012-02-18 01:02:45

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-02-18 01:02:45

100% doctest coverage; all test pass

Category_realization (now Category_realization_of_parent) does not need a super_category method: it is an abstract class.


---

Comment by hivert created at 2012-02-20 21:34:46

Hi Nicolas,

I just posted a
[review patch](http://combinat.sagemath.org/patches/file/a9bb0e6af448/trac_7980-multiple-realizations-review-fh.patch)
on sage-combinat queue. Here are the main changes

1. This is mostly documentation, except that I changed trivially the code in
the example, by renaming some parameter names:

   - in `SubsetAlgebra(S)` the parameter S is a set;

   - in `Fundamental(S)`, `In(S)` and `Out(S)` it is a
     `SubsetAlgebra`;

I was really confused about that reading the code so that I renamed `S`
to `SAlg` in the second case and added an `INPUT:` field in the doc

2. The correct markup for see also is the following:

```
.. seealso::
   bla bla bla
   bla bla 
```

as variants, you can use uppercase as Sphinx markup is not case sensitive. You
can also put everything on one line if it fits:

```
.. SEEALSO:: bla bla bla
```

If you put a space as in `..see also::` then this become a comment and is
ignored by Sphinx ! This remind me that I should finish #12078 Add an example
of SEE ALSO

3. There is a missing doctest in my review patch

```
    sage: A.F() in A.Realizations()
Expected:
    True
Got:
    False
```

I left it on purpose. I realize that the correct doctest is

```
    sage: A.F() in A.Bases()
Expected:
    True
Got:
    False
```

But it took me quite a lot of thinking understanding that. I think we should
explain this somewhere, probably where the broken test is.

Please review my numerous doc change, fold the patch if you are Ok with it.

Florent


---

Comment by nthiery created at 2012-02-20 22:59:16

Replying to [comment:9 hivert]:
> I just posted a review patch on sage-combinat queue.

Thanks!

I went through it, folded it in, and added a
[http://combinat.sagemath.org/patches/file/tip/trac_7980-multiple-realizations-review-nt.patch
review review patch]

> 1. This is mostly documentation, except that I changed trivially the code in
> the example, by renaming some parameter names:
> 
>    - in `SubsetAlgebra(S)` the parameter S is a set;
> 
>    - in `Fundamental(S)`, `In(S)` and `Out(S)` it is a
>      `SubsetAlgebra`;
> 
> I was really confused about that reading the code so that I renamed `S`
> to `SAlg` in the second case and added an `INPUT:` field in the doc

Good point. I ended up renaming SAlg to A since this is what we use in
all the examples.

> 3. There is a missing doctest in my review patch
> {{{
>     sage: A.F() in A.Realizations()
> Expected:
>     True
> Got:
>     False
> }}}

Ouch! That's not good. I am not sure this is the best approach, but I
added A.Realizations() to the super categories Bases(A). Maybe
A.Realizations() should be Bases(A) instead. In any cases, that will
work for now. I added A._test_realizations() which checks:


```
    R in A.Realizations() for R in A.realizations()
```


Feel free to fold in my review patch and repost after checking it out.

Cheers,
                          Nicolas


---

Comment by nthiery created at 2012-02-21 07:45:50

Please update the queue first, since I took off the fix to the CategoryObject link to put it in #9469


---

Comment by nthiery created at 2012-02-25 01:14:19

Replying to [comment:11 nthiery]:
> Please update the queue first, since I took off the fix to the CategoryObject link to put it in #9469

Again: I fixed a couple trivially failing doctests.


---

Comment by SimonKing created at 2012-03-10 06:24:11

Replying to [ticket:7980 jbandlow]:
> This patch implement generic support for parents with (multiple) realizations

What patch? This ticket does not provide any patch.


---

Comment by SimonKing created at 2012-03-10 06:24:11

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2012-03-10 08:19:33

Replying to [comment:13 SimonKing]:
> Replying to [ticket:7980 jbandlow]:
> > This patch implement generic support for parents with (multiple) realizations
> 
> What patch? This ticket does not provide any patch.

I should have mentioned that it is in on the Sage-Combinat queue, and the review by Florent is occuring here. In such situations it's a waste of time to update the patch on trac all the time; and leaving an outdated patch on trac is not so good either (someone might waste time reviewing old stuff).


---

Comment by hivert created at 2012-03-15 10:55:32

For the record: as of version [a7993225ce8e/trac_7980-multiple-realizations-nt.patch](http://combinat.sagemath.org/patches/file/a7993225ce8e/trac_7980-multiple-realizations-nt.patch) I'm Ok with the patch upto a few documentation glitches. I pushed the following patch [a7993225ce8e/trac_7980-multiple-realizations-review-fh.patch](http://combinat.sagemath.org/patches/file/a7993225ce8e/trac_7980-multiple-realizations-review-fh.patch). If you are Ok with my review patch and the tests pass you can set positive review on my behalf. If so don't forget to fold and update.

Florent


---

Attachment


---

Comment by nthiery created at 2012-03-16 16:46:34

I folded Florent's patch, and we fixed together a couple remaining glitches on the Sage-Combinat queue.

Florent: the sphinx errors were clearly due to a broken sphinx state on my test machine. After nuking the doctrees, this compiled smoothly. So I set a positive review on your behalf.


---

Comment by nthiery created at 2012-03-16 16:46:34

Changing status from needs_work to positive_review.


---

Comment by hivert created at 2012-03-16 19:22:52

One more ! Good !

Florent


---

Comment by jdemeyer created at 2012-03-28 10:02:39

Resolution: fixed
