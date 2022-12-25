# Issue 7980: Move 'Category with concrete representation' code into Sage

archive/issues_007980.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nThis code currently exists on the sage-combinat queue, in the ncsf patch.  It should be put in a more natural place in the category code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7980\n\n",
    "created_at": "2010-01-18T18:04:02Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Move 'Category with concrete representation' code into Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7980",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @nthiery

CC:  sage-combinat

This code currently exists on the sage-combinat queue, in the ncsf patch.  It should be put in a more natural place in the category code.

Issue created by migration from https://trac.sagemath.org/ticket/7980





---

archive/issue_comments_069498.json:
```json
{
    "body": "Didn't we want Realization rather than Representation?",
    "created_at": "2010-05-07T15:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69498",
    "user": "https://github.com/mwhansen"
}
```

Didn't we want Realization rather than Representation?



---

archive/issue_comments_069499.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2011-01-13T09:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69499",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_069500.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-13T09:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69500",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069501.json:
```json
{
    "body": "Since the ticket description is rather sparse, I'm collecting here some statements that emerged from reading the patch and discussing with Nicolas, who is sitting beside me.\n\n* It disposes of abstract categories. Hooray!\n* On the one hand, one has (abstract) vectorspaces. A realization of such abstract vector space is given by specific data, for example by a basis, but it should be emphasized that not all realizations of a vector space are necessarily in terms of a basis. So, not any realization of a vectorspace is a \"vectorspace with basis\".\n* The realizations of a vector space are related by canonical morphisms (for example, change of basis).\n* Is any \"vectorspace with basis\" a realisation of a vector space? No! There is no gurantee that this specific vectorspace with basis is equiped with the above-mentioned canonical morphisms. \n\n**__TODO__**\n\n* The docstring of the class `Category_realization` has no examples. Its `__init__` method should define its arguments and provide a test. `_get_name` is not documented either.\n* Similarly, `Realizations` is undocumented.\n* `Realizations.super_categories()` returns `[Sets()]`. Idea of Nicolas: Add an optional argument `Realizations(parent, category=Bla)`, so that the default for Bla is `Sets()`. The given category will be returned as super category.\n\n* I tried some example, with comments/questions inserted:\n {{{\nsage: C = Algebras(QQ)\nsage: C.WithRealizations()\nJoin of Category of algebras over Rational Field and Category of sets with realizations\n }}}\n Does it really have to be a join category?\n {{{\nsage: from sage.categories.category_types import Category_realization\nsage: Category_realization(QQ)\nThe category of category_realization of Rational Field\n }}}\n So, do I understand correctly that the set of all realisations of `QQ` forms a category, each object being a realisation of `QQ`, the morphisms being canonical maps between the different realisations?\n {{{\nsage: Category_realization(QQ).is_subcategory(Rings().WithRealizations())\nBOOM\nsage: hasattr(Category_realization(QQ), 'super_categories')\nFalse\n }}}\n So, that's a bug. `Category_realization(QQ)` is a category and thus MUST have a `super_categories` method.\n\n\n**__Is the category of \"Bla with realisations\" a 2-category?__**\n\nSince Nicolas is now teaching, I can not ask him directly:\n\n* If I understand correctly, for any parent P there is a *category* `Category_realizations(P)`.\n* For any category C, there is a category `C.WithRealizations()`.\n* Shouldn't it be the case that for any `P in C`, the realisations of P (thus, the *category* `Category_realizations(P)`) is an object in `C.WithRealizations()`?\n* But if the objects of `C.WithRealizations()` are categories themselves, shouldn't we first implement the notion of higher categories in Sage, before we treat the category of realizations of objects of C?",
    "created_at": "2011-11-16T10:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69501",
    "user": "https://github.com/simon-king-jena"
}
```

Since the ticket description is rather sparse, I'm collecting here some statements that emerged from reading the patch and discussing with Nicolas, who is sitting beside me.

* It disposes of abstract categories. Hooray!
* On the one hand, one has (abstract) vectorspaces. A realization of such abstract vector space is given by specific data, for example by a basis, but it should be emphasized that not all realizations of a vector space are necessarily in terms of a basis. So, not any realization of a vectorspace is a "vectorspace with basis".
* The realizations of a vector space are related by canonical morphisms (for example, change of basis).
* Is any "vectorspace with basis" a realisation of a vector space? No! There is no gurantee that this specific vectorspace with basis is equiped with the above-mentioned canonical morphisms. 

**__TODO__**

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


**__Is the category of "Bla with realisations" a 2-category?__**

Since Nicolas is now teaching, I can not ask him directly:

* If I understand correctly, for any parent P there is a *category* `Category_realizations(P)`.
* For any category C, there is a category `C.WithRealizations()`.
* Shouldn't it be the case that for any `P in C`, the realisations of P (thus, the *category* `Category_realizations(P)`) is an object in `C.WithRealizations()`?
* But if the objects of `C.WithRealizations()` are categories themselves, shouldn't we first implement the notion of higher categories in Sage, before we treat the category of realizations of objects of C?



---

archive/issue_comments_069502.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n> **__Is the category of \"Bla with realisations\" a 2-category?__**\n\nNo, it isn't. I had a totally wrong notion of a higher category. Sorry.\n\nAnyway, the missing super_categories method must be provided (as for any category).",
    "created_at": "2011-11-16T14:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69502",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:5 SimonKing]:
> **__Is the category of "Bla with realisations" a 2-category?__**

No, it isn't. I had a totally wrong notion of a higher category. Sorry.

Anyway, the missing super_categories method must be provided (as for any category).



---

archive/issue_comments_069503.json:
```json
{
    "body": "Changing keywords from \"\" to \"Cernay2012\".",
    "created_at": "2012-02-09T18:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69503",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "Cernay2012".



---

archive/issue_comments_069504.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-18T01:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69504",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069505.json:
```json
{
    "body": "100% doctest coverage; all test pass\n\nCategory_realization (now Category_realization_of_parent) does not need a super_category method: it is an abstract class.",
    "created_at": "2012-02-18T01:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69505",
    "user": "https://github.com/nthiery"
}
```

100% doctest coverage; all test pass

Category_realization (now Category_realization_of_parent) does not need a super_category method: it is an abstract class.



---

archive/issue_comments_069506.json:
```json
{
    "body": "Hi Nicolas,\n\nI just posted a\n[review patch](http://combinat.sagemath.org/patches/file/a9bb0e6af448/trac_7980-multiple-realizations-review-fh.patch)\non sage-combinat queue. Here are the main changes\n\n1. This is mostly documentation, except that I changed trivially the code in\nthe example, by renaming some parameter names:\n\n- in `SubsetAlgebra(S)` the parameter S is a set;\n\n- in `Fundamental(S)`, `In(S)` and `Out(S)` it is a\n  `SubsetAlgebra`;\n\nI was really confused about that reading the code so that I renamed `S`\nto `SAlg` in the second case and added an `INPUT:` field in the doc\n\n2. The correct markup for see also is the following:\n\n```\n.. seealso::\n   bla bla bla\n   bla bla \n```\n\nas variants, you can use uppercase as Sphinx markup is not case sensitive. You\ncan also put everything on one line if it fits:\n\n```\n.. SEEALSO:: bla bla bla\n```\n\nIf you put a space as in `..see also::` then this become a comment and is\nignored by Sphinx ! This remind me that I should finish #12078 Add an example\nof SEE ALSO\n\n3. There is a missing doctest in my review patch\n\n```\n    sage: A.F() in A.Realizations()\nExpected:\n    True\nGot:\n    False\n```\n\nI left it on purpose. I realize that the correct doctest is\n\n```\n    sage: A.F() in A.Bases()\nExpected:\n    True\nGot:\n    False\n```\n\nBut it took me quite a lot of thinking understanding that. I think we should\nexplain this somewhere, probably where the broken test is.\n\nPlease review my numerous doc change, fold the patch if you are Ok with it.\n\nFlorent",
    "created_at": "2012-02-20T21:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69506",
    "user": "https://github.com/hivert"
}
```

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

archive/issue_comments_069507.json:
```json
{
    "body": "Replying to [comment:9 hivert]:\n> I just posted a review patch on sage-combinat queue.\n\nThanks!\n\nI went through it, folded it in, and added a\n[http://combinat.sagemath.org/patches/file/tip/trac_7980-multiple-realizations-review-nt.patch\nreview review patch]\n\n> 1. This is mostly documentation, except that I changed trivially the code in\n> the example, by renaming some parameter names:\n> \n>    - in `SubsetAlgebra(S)` the parameter S is a set;\n> \n>    - in `Fundamental(S)`, `In(S)` and `Out(S)` it is a\n>      `SubsetAlgebra`;\n> \n> I was really confused about that reading the code so that I renamed `S`\n> to `SAlg` in the second case and added an `INPUT:` field in the doc\n\nGood point. I ended up renaming SAlg to A since this is what we use in\nall the examples.\n\n> 3. There is a missing doctest in my review patch\n> {{{\n>     sage: A.F() in A.Realizations()\n> Expected:\n>     True\n> Got:\n>     False\n> }}}\n\nOuch! That's not good. I am not sure this is the best approach, but I\nadded A.Realizations() to the super categories Bases(A). Maybe\nA.Realizations() should be Bases(A) instead. In any cases, that will\nwork for now. I added A._test_realizations() which checks:\n\n\n```\n    R in A.Realizations() for R in A.realizations()\n```\n\n\nFeel free to fold in my review patch and repost after checking it out.\n\nCheers,\n                          Nicolas",
    "created_at": "2012-02-20T22:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69507",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_069508.json:
```json
{
    "body": "Please update the queue first, since I took off the fix to the CategoryObject link to put it in #9469",
    "created_at": "2012-02-21T07:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69508",
    "user": "https://github.com/nthiery"
}
```

Please update the queue first, since I took off the fix to the CategoryObject link to put it in #9469



---

archive/issue_comments_069509.json:
```json
{
    "body": "Replying to [comment:11 nthiery]:\n> Please update the queue first, since I took off the fix to the CategoryObject link to put it in #9469\n\nAgain: I fixed a couple trivially failing doctests.",
    "created_at": "2012-02-25T01:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69509",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:11 nthiery]:
> Please update the queue first, since I took off the fix to the CategoryObject link to put it in #9469

Again: I fixed a couple trivially failing doctests.



---

archive/issue_comments_069510.json:
```json
{
    "body": "Replying to [ticket:7980 jbandlow]:\n> This patch implement generic support for parents with (multiple) realizations\n\nWhat patch? This ticket does not provide any patch.",
    "created_at": "2012-03-10T06:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69510",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [ticket:7980 jbandlow]:
> This patch implement generic support for parents with (multiple) realizations

What patch? This ticket does not provide any patch.



---

archive/issue_comments_069511.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-10T06:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69511",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069512.json:
```json
{
    "body": "Replying to [comment:13 SimonKing]:\n> Replying to [ticket:7980 jbandlow]:\n> > This patch implement generic support for parents with (multiple) realizations\n> \n> What patch? This ticket does not provide any patch.\n\nI should have mentioned that it is in on the Sage-Combinat queue, and the review by Florent is occuring here. In such situations it's a waste of time to update the patch on trac all the time; and leaving an outdated patch on trac is not so good either (someone might waste time reviewing old stuff).",
    "created_at": "2012-03-10T08:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69512",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:13 SimonKing]:
> Replying to [ticket:7980 jbandlow]:
> > This patch implement generic support for parents with (multiple) realizations
> 
> What patch? This ticket does not provide any patch.

I should have mentioned that it is in on the Sage-Combinat queue, and the review by Florent is occuring here. In such situations it's a waste of time to update the patch on trac all the time; and leaving an outdated patch on trac is not so good either (someone might waste time reviewing old stuff).



---

archive/issue_comments_069513.json:
```json
{
    "body": "For the record: as of version [a7993225ce8e/trac_7980-multiple-realizations-nt.patch](http://combinat.sagemath.org/patches/file/a7993225ce8e/trac_7980-multiple-realizations-nt.patch) I'm Ok with the patch upto a few documentation glitches. I pushed the following patch [a7993225ce8e/trac_7980-multiple-realizations-review-fh.patch](http://combinat.sagemath.org/patches/file/a7993225ce8e/trac_7980-multiple-realizations-review-fh.patch). If you are Ok with my review patch and the tests pass you can set positive review on my behalf. If so don't forget to fold and update.\n\nFlorent",
    "created_at": "2012-03-15T10:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69513",
    "user": "https://github.com/hivert"
}
```

For the record: as of version [a7993225ce8e/trac_7980-multiple-realizations-nt.patch](http://combinat.sagemath.org/patches/file/a7993225ce8e/trac_7980-multiple-realizations-nt.patch) I'm Ok with the patch upto a few documentation glitches. I pushed the following patch [a7993225ce8e/trac_7980-multiple-realizations-review-fh.patch](http://combinat.sagemath.org/patches/file/a7993225ce8e/trac_7980-multiple-realizations-review-fh.patch). If you are Ok with my review patch and the tests pass you can set positive review on my behalf. If so don't forget to fold and update.

Florent



---

archive/issue_comments_069514.json:
```json
{
    "body": "Attachment [trac_7980-multiple-realizations-nt.patch](tarball://root/attachments/some-uuid/ticket7980/trac_7980-multiple-realizations-nt.patch) by @nthiery created at 2012-03-16 16:44:10",
    "created_at": "2012-03-16T16:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69514",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7980-multiple-realizations-nt.patch](tarball://root/attachments/some-uuid/ticket7980/trac_7980-multiple-realizations-nt.patch) by @nthiery created at 2012-03-16 16:44:10



---

archive/issue_comments_069515.json:
```json
{
    "body": "I folded Florent's patch, and we fixed together a couple remaining glitches on the Sage-Combinat queue.\n\nFlorent: the sphinx errors were clearly due to a broken sphinx state on my test machine. After nuking the doctrees, this compiled smoothly. So I set a positive review on your behalf.",
    "created_at": "2012-03-16T16:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69515",
    "user": "https://github.com/nthiery"
}
```

I folded Florent's patch, and we fixed together a couple remaining glitches on the Sage-Combinat queue.

Florent: the sphinx errors were clearly due to a broken sphinx state on my test machine. After nuking the doctrees, this compiled smoothly. So I set a positive review on your behalf.



---

archive/issue_comments_069516.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-16T16:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69516",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_069517.json:
```json
{
    "body": "One more ! Good !\n\nFlorent",
    "created_at": "2012-03-16T19:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69517",
    "user": "https://github.com/hivert"
}
```

One more ! Good !

Florent



---

archive/issue_comments_069518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-28T10:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7980#issuecomment-69518",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
