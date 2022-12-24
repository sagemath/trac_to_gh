# Issue 8920: Factor code between words's alphabets and sets/enumerated sets/ordered sets

archive/issues_008920.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat vdelecroix sstarosta\n\nKeywords: Words, Sets\n\nThere is a lot of common code....\n\nIssue created by migration from https://trac.sagemath.org/ticket/8920\n\n",
    "created_at": "2010-05-07T17:04:04Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Factor code between words's alphabets and sets/enumerated sets/ordered sets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8920",
    "user": "hivert"
}
```
Assignee: sage-combinat

CC:  sage-combinat vdelecroix sstarosta

Keywords: Words, Sets

There is a lot of common code....

Issue created by migration from https://trac.sagemath.org/ticket/8920





---

archive/issue_comments_082148.json:
```json
{
    "body": "Hi Vincent,\n\nYou are currently taking car of this. You may want either to reuse this ticket or to close it as duplicate.\n\nFlorent",
    "created_at": "2012-02-09T01:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82148",
    "user": "hivert"
}
```

Hi Vincent,

You are currently taking car of this. You may want either to reuse this ticket or to close it as duplicate.

Florent



---

archive/issue_comments_082149.json:
```json
{
    "body": "Changing keywords from \"Words, Sets\" to \"Words, Sets, Cernay2012\".",
    "created_at": "2012-02-09T01:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82149",
    "user": "hivert"
}
```

Changing keywords from "Words, Sets" to "Words, Sets, Cernay2012".



---

archive/issue_comments_082150.json:
```json
{
    "body": "Many tests currently break because of the following behavior\n\n```\nsage: int(2) in Integers()\nTrue\nsage: int(2) in PositiveIntegers()\nFalse\n```\n",
    "created_at": "2012-08-16T11:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82150",
    "user": "vdelecroix"
}
```

Many tests currently break because of the following behavior

```
sage: int(2) in Integers()
True
sage: int(2) in PositiveIntegers()
False
```




---

archive/issue_comments_082151.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-08-17T12:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82151",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082152.json:
```json
{
    "body": "Hey Vincent,\n   The patch needs rebasing to 5.5.rc0. Once you upload the rebase, I'll review the patch.\n\nI think the only merged patch which might have caused the conflict is #13677.\n\nThanks,\n\nTravis",
    "created_at": "2012-11-28T00:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82152",
    "user": "tscrim"
}
```

Hey Vincent,
   The patch needs rebasing to 5.5.rc0. Once you upload the rebase, I'll review the patch.

I think the only merged patch which might have caused the conflict is #13677.

Thanks,

Travis



---

archive/issue_comments_082153.json:
```json
{
    "body": "Replying to [comment:7 tscrim]:\n> Hey Vincent,\n>    The patch needs rebasing to 5.5.rc0. Once you upload the rebase, I'll review the patch.\n> \n> I think the only merged patch which might have caused the conflict is #13677.\n> \n> Thanks,\n\n> Travis\n\nHi Travis,\n\nI rebased the patch (together with Stepan Starosta) and actually we decided to simplify the FiniteEnumeratedSet (the new version was slower). Everything should apply and work on 5.5.rc0.\n\nBest,\nVincent",
    "created_at": "2012-11-30T16:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82153",
    "user": "vdelecroix"
}
```

Replying to [comment:7 tscrim]:
> Hey Vincent,
>    The patch needs rebasing to 5.5.rc0. Once you upload the rebase, I'll review the patch.
> 
> I think the only merged patch which might have caused the conflict is #13677.
> 
> Thanks,

> Travis

Hi Travis,

I rebased the patch (together with Stepan Starosta) and actually we decided to simplify the FiniteEnumeratedSet (the new version was slower). Everything should apply and work on 5.5.rc0.

Best,
Vincent



---

archive/issue_comments_082154.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-12-02T08:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82154",
    "user": "tscrim"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_082155.json:
```json
{
    "body": "Hey Vincent and Stepan,\n\nIn `build_alphabet`, the docstring states that this is an ordered alphabet. I get the following:\n\n```\nsage: A = Alphabet([1,3,7,2])\nsage: A(3) < A(7)     \nTrue\nsage: A(3) < A(2)\nFalse\n```\n\nI expected the last one to return `True` since I expected these to be letters in `A` and the comparison to take place in there (not default back to their natural ordering). I also get this:\n\n```\nsage: B = Alphabet(['a', 'b'])\nsage: B('a')\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: Cannot convert str to sage.structure.element.Element\n```\n\nand both problems are because the alphabet does not have any element class. These problems were worse before this patch, but I was wondering if you wanted to take care of these here?\n\n`Words` still does proper comparison:\n\n```\nsage: W = Words(A); W\nWords over {1, 3, 7, 2}\nsage: W([2,1]) < W([2,2])\nTrue\nsage: W([2,3]) < W([2,2])\nTrue\nsage: W([2,2]) < W([2,7])\nFalse\n```\n\n\nAdditionally on `is_endomorphism()` (line 1111 in `morphism.py`), it was changed to test equality of the domain and codomain. What was the reasoning for this?\n\nThis applied cleanly for me on `5.5.rc0`, I'm curious as to why the patchbot defaulted back to `5.4.rc3`...\n\nThanks for you work on this,\n\nTravis",
    "created_at": "2012-12-02T08:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82155",
    "user": "tscrim"
}
```

Hey Vincent and Stepan,

In `build_alphabet`, the docstring states that this is an ordered alphabet. I get the following:

```
sage: A = Alphabet([1,3,7,2])
sage: A(3) < A(7)     
True
sage: A(3) < A(2)
False
```

I expected the last one to return `True` since I expected these to be letters in `A` and the comparison to take place in there (not default back to their natural ordering). I also get this:

```
sage: B = Alphabet(['a', 'b'])
sage: B('a')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: Cannot convert str to sage.structure.element.Element
```

and both problems are because the alphabet does not have any element class. These problems were worse before this patch, but I was wondering if you wanted to take care of these here?

`Words` still does proper comparison:

```
sage: W = Words(A); W
Words over {1, 3, 7, 2}
sage: W([2,1]) < W([2,2])
True
sage: W([2,3]) < W([2,2])
True
sage: W([2,2]) < W([2,7])
False
```


Additionally on `is_endomorphism()` (line 1111 in `morphism.py`), it was changed to test equality of the domain and codomain. What was the reasoning for this?

This applied cleanly for me on `5.5.rc0`, I'm curious as to why the patchbot defaulted back to `5.4.rc3`...

Thanks for you work on this,

Travis



---

archive/issue_comments_082156.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-12-05T17:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82156",
    "user": "vdelecroix"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_082157.json:
```json
{
    "body": "Hi Travis,\n\nthanks for reviewing the patch and your comments! I uploaded a new version with two major changes\n* a new class TotallyOrderedFiniteSet\n* a dependency on #13801\n\nAll problems are similar to the ones there are currently with Nathann and posets (#13747) : to be or not to be a facade, that is the question. One major difference with the previous patch is that we provide a class TotallyOrderedFiniteSet which has a facade option behavior and may choose the behavior you prefer.\n\n**How do facades behave**\n\nFacade are the default behavior for alphabets. The disadvantage of having a facade is that the elements need to have their order implemented, i.e., we get\n\n```\nsage: A = TotallyOrderedFiniteSet([0,2,1], facade=True)\nsage: A(2) < A(1) \nFalse\n```\n\nAnother disadvantage of having a facade is that if some elements do not inherit from Element, the constructor raises an error\n\n```\nsage: B = TotallyOrderedFiniteSet(['a','b',3],facade=True)\nsage: B('a')\nTraceback (most recent call last):\n...\nTypeError: Cannot convert str to sage.structure.element.Element\n```\n\n\n**Not using facade ?**\n\nThe possible workaround for the two above problems is to have a dedicated element class for TotallyOrderedFiniteSet. If the option facade is set to False, it is what you get\n\n```\nsage: C = TotallyOrderedFiniteSet([1, 'a', -4], facade = False)\nsage: C(1) < C(-4)\nTrue\nsage: C('a')\n'a'\n```\n\n... but\n\n```\nsage: 1 in C\nFalse\nsage: 1 == C(1)\nFalse\nsage: C(1) == 1\nTrue\n```\n\n\n**Partial conclusion**\n\n we do prefer having facade = True as a default behavior (as Nathann does).\n\n**About endomorphisms**\n\nTwo reason to change is_endomorphism() are: \n  1) the operator <= is not defined on sets\n  2) the test was mathematically inaccurate : an endomorphism is a morphism for which domain = codomain (and not just a subset of codomain)\n\nThanks,\nStepan and Vincent",
    "created_at": "2012-12-05T17:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82157",
    "user": "vdelecroix"
}
```

Hi Travis,

thanks for reviewing the patch and your comments! I uploaded a new version with two major changes
* a new class TotallyOrderedFiniteSet
* a dependency on #13801

All problems are similar to the ones there are currently with Nathann and posets (#13747) : to be or not to be a facade, that is the question. One major difference with the previous patch is that we provide a class TotallyOrderedFiniteSet which has a facade option behavior and may choose the behavior you prefer.

**How do facades behave**

Facade are the default behavior for alphabets. The disadvantage of having a facade is that the elements need to have their order implemented, i.e., we get

```
sage: A = TotallyOrderedFiniteSet([0,2,1], facade=True)
sage: A(2) < A(1) 
False
```

Another disadvantage of having a facade is that if some elements do not inherit from Element, the constructor raises an error

```
sage: B = TotallyOrderedFiniteSet(['a','b',3],facade=True)
sage: B('a')
Traceback (most recent call last):
...
TypeError: Cannot convert str to sage.structure.element.Element
```


**Not using facade ?**

The possible workaround for the two above problems is to have a dedicated element class for TotallyOrderedFiniteSet. If the option facade is set to False, it is what you get

```
sage: C = TotallyOrderedFiniteSet([1, 'a', -4], facade = False)
sage: C(1) < C(-4)
True
sage: C('a')
'a'
```

... but

```
sage: 1 in C
False
sage: 1 == C(1)
False
sage: C(1) == 1
True
```


**Partial conclusion**

 we do prefer having facade = True as a default behavior (as Nathann does).

**About endomorphisms**

Two reason to change is_endomorphism() are: 
  1) the operator <= is not defined on sets
  2) the test was mathematically inaccurate : an endomorphism is a morphism for which domain = codomain (and not just a subset of codomain)

Thanks,
Stepan and Vincent



---

archive/issue_comments_082158.json:
```json
{
    "body": "Replying to [comment:11 vdelecroix]:\n> Another disadvantage of having a facade is that if some elements do not inherit from Element, the constructor raises an error\n> {{{\n> sage: B = TotallyOrderedFiniteSet(['a','b',3],facade=True)\n> sage: B('a')\n> Traceback (most recent call last):\n> ...\n> TypeError: Cannot convert str to sage.structure.element.Element\n> }}}\n\nYeah, we hit the same problem in Poset, and we worked around it by\nhaving a custom __call__ function. At some point, we should really fix\nit once for all in Parent.__call__.\n\nCheers,\n                              Nicolas",
    "created_at": "2012-12-06T09:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82158",
    "user": "nthiery"
}
```

Replying to [comment:11 vdelecroix]:
> Another disadvantage of having a facade is that if some elements do not inherit from Element, the constructor raises an error
> {{{
> sage: B = TotallyOrderedFiniteSet(['a','b',3],facade=True)
> sage: B('a')
> Traceback (most recent call last):
> ...
> TypeError: Cannot convert str to sage.structure.element.Element
> }}}

Yeah, we hit the same problem in Poset, and we worked around it by
having a custom __call__ function. At some point, we should really fix
it once for all in Parent.__call__.

Cheers,
                              Nicolas



---

archive/issue_comments_082159.json:
```json
{
    "body": "Hey Stepan and Vincent,\n\nFew more things:\n\n- I get the same doctest failures as the patchbot; you just need to change the tests' output in `finite_word.py`.\n\n- Would it be possible to just have `Alphabet()` (thus removing/renaming the `build_alphabet()`)?\n\n- Could you issue a deprecation warning for `OrderedAlphabet`?\n\n- The `__new__()` function for `OrderedAlphabet` needs a doctest.\n\n- I would recommend for the documentation of `OrderedAlphabet_backward_compatibility`:\n\n```\nVersions prior to :trac:`8920` uses the ``Alphabet`` classes with an\nargument ``._alphabet()`` instead of ``._elements()`` used in\n:class:`TotallyOrderedFiniteSet`. This class is dedicated to handling this\nproblem which occurs when unpickling :class:`OrderedAlphabet`.\n```\n\n\n- The operator `<=` for `Alphabet` and `Words` did not behave as I expected:\n\n```\n# Before\nsage: Alphabet('abc') <= Alphabet('12')\nFalse\nsage: Alphabet('abc') >= Alphabet('12')\nFalse\nsage: Alphabet('abcdef') <= Alphabet('12')\nFalse\nsage: Words('a') <= Words('123')           \nFalse\nsage: Words('abcdef') <= Words('123')\nFalse\nsage: Words('abcdef') >= Words('123')\nFalse\n\n# With the patch\nsage: Alphabet('abc') <= Alphabet('12')\nTrue\nsage: Alphabet('abc') >= Alphabet('12')\nFalse\nsage: Alphabet('abcdef') <= Alphabet('12')\nTrue\nsage: Words('a') <= Words('123')     \nTrue\nsage: Words('abcdef') <= Words('123')\nFalse\nsage: Words('abcdef') >= Words('123')\nTrue\n```\n\n\n- I'm still uncomfortable with the change to `is_endomorphism()` since I would (naively) expect the map `a->a, b->aa, c->aaa` be an endomorphism. The problem is word morphism automatically sets the codomain based on the image. As for the mathematics, yes, if it is a proper subset, it is not an endomorphism, but it naturally extends to one. I believe that having anything that is naturally extendable to an endomorphism should be considered an endomorphism by sage via the coercion model. Also in case you're worried, the above morphism worked with composition.\n\n  If a third party agrees with the changes in the patch, then I would add a warning to `is_endomorphism()` and/or to `WordMorphism` about defining endomorphisms and add the tests\n\n```\nsage: w = WordMorphism('a->a,b->aa,c->aaa', codomain=Words('abc'))\nsage: w.is_endomorphism()\nTrue\nsage: w2 = WordMorphism('a->a,b->aa,c->aaa')                      \nsage: w == w2\nFalse\n```\n\n  However there is one problem with this, and that is `w == w2` returns `True`. Thus the equality operator will need to be changed to reflect the dependency on the codomain.\n\nThank you,\n\nTravis",
    "created_at": "2012-12-12T20:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82159",
    "user": "tscrim"
}
```

Hey Stepan and Vincent,

Few more things:

- I get the same doctest failures as the patchbot; you just need to change the tests' output in `finite_word.py`.

- Would it be possible to just have `Alphabet()` (thus removing/renaming the `build_alphabet()`)?

- Could you issue a deprecation warning for `OrderedAlphabet`?

- The `__new__()` function for `OrderedAlphabet` needs a doctest.

- I would recommend for the documentation of `OrderedAlphabet_backward_compatibility`:

```
Versions prior to :trac:`8920` uses the ``Alphabet`` classes with an
argument ``._alphabet()`` instead of ``._elements()`` used in
:class:`TotallyOrderedFiniteSet`. This class is dedicated to handling this
problem which occurs when unpickling :class:`OrderedAlphabet`.
```


- The operator `<=` for `Alphabet` and `Words` did not behave as I expected:

```
# Before
sage: Alphabet('abc') <= Alphabet('12')
False
sage: Alphabet('abc') >= Alphabet('12')
False
sage: Alphabet('abcdef') <= Alphabet('12')
False
sage: Words('a') <= Words('123')           
False
sage: Words('abcdef') <= Words('123')
False
sage: Words('abcdef') >= Words('123')
False

# With the patch
sage: Alphabet('abc') <= Alphabet('12')
True
sage: Alphabet('abc') >= Alphabet('12')
False
sage: Alphabet('abcdef') <= Alphabet('12')
True
sage: Words('a') <= Words('123')     
True
sage: Words('abcdef') <= Words('123')
False
sage: Words('abcdef') >= Words('123')
True
```


- I'm still uncomfortable with the change to `is_endomorphism()` since I would (naively) expect the map `a->a, b->aa, c->aaa` be an endomorphism. The problem is word morphism automatically sets the codomain based on the image. As for the mathematics, yes, if it is a proper subset, it is not an endomorphism, but it naturally extends to one. I believe that having anything that is naturally extendable to an endomorphism should be considered an endomorphism by sage via the coercion model. Also in case you're worried, the above morphism worked with composition.

  If a third party agrees with the changes in the patch, then I would add a warning to `is_endomorphism()` and/or to `WordMorphism` about defining endomorphisms and add the tests

```
sage: w = WordMorphism('a->a,b->aa,c->aaa', codomain=Words('abc'))
sage: w.is_endomorphism()
True
sage: w2 = WordMorphism('a->a,b->aa,c->aaa')                      
sage: w == w2
False
```

  However there is one problem with this, and that is `w == w2` returns `True`. Thus the equality operator will need to be changed to reflect the dependency on the codomain.

Thank you,

Travis



---

archive/issue_comments_082160.json:
```json
{
    "body": "Hey Stepan and Vincent,\n\nReplying to [comment:13 tscrim]:\n> - I'm still uncomfortable with the change to `is_endomorphism()` since I would (naively) expect the map `a->a, b->aa, c->aaa` be an endomorphism. The problem is word morphism automatically sets the codomain based on the image. As for the mathematics, yes, if it is a proper subset, it is not an endomorphism, but it naturally extends to one. I believe that having anything that is naturally extendable to an endomorphism should be considered an endomorphism by sage via the coercion model. Also in case you're worried, the above morphism worked with composition.\n> \n>   If a third party agrees with the changes in the patch, then I would add a warning to `is_endomorphism()` and/or to `WordMorphism` about defining endomorphisms and add the tests\n> {{{\n> sage: w = WordMorphism('a->a,b->aa,c->aaa', codomain=Words('abc'))\n> sage: w.is_endomorphism()\n> True\n> sage: w2 = WordMorphism('a->a,b->aa,c->aaa')                      \n> sage: w == w2\n> False\n> }}}\n>   However there is one problem with this, and that is `w == w2` returns `True`. Thus the equality operator will need to be changed to reflect the dependency on the codomain.\n\nI talked with Nicolas about this, and he agreed with the changes in your patch, but also said we needed to change the `==` operator to check the codomain (in particular, we don't want a map `f` to be surjective and `g` to not be and compare equal because `g` has a larger codomain). This might be a more general problem, and I'll take a look at it today and let you know what I find.\n\nBest,\n\nTravis",
    "created_at": "2013-02-01T12:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82160",
    "user": "tscrim"
}
```

Hey Stepan and Vincent,

Replying to [comment:13 tscrim]:
> - I'm still uncomfortable with the change to `is_endomorphism()` since I would (naively) expect the map `a->a, b->aa, c->aaa` be an endomorphism. The problem is word morphism automatically sets the codomain based on the image. As for the mathematics, yes, if it is a proper subset, it is not an endomorphism, but it naturally extends to one. I believe that having anything that is naturally extendable to an endomorphism should be considered an endomorphism by sage via the coercion model. Also in case you're worried, the above morphism worked with composition.
> 
>   If a third party agrees with the changes in the patch, then I would add a warning to `is_endomorphism()` and/or to `WordMorphism` about defining endomorphisms and add the tests
> {{{
> sage: w = WordMorphism('a->a,b->aa,c->aaa', codomain=Words('abc'))
> sage: w.is_endomorphism()
> True
> sage: w2 = WordMorphism('a->a,b->aa,c->aaa')                      
> sage: w == w2
> False
> }}}
>   However there is one problem with this, and that is `w == w2` returns `True`. Thus the equality operator will need to be changed to reflect the dependency on the codomain.

I talked with Nicolas about this, and he agreed with the changes in your patch, but also said we needed to change the `==` operator to check the codomain (in particular, we don't want a map `f` to be surjective and `g` to not be and compare equal because `g` has a larger codomain). This might be a more general problem, and I'll take a look at it today and let you know what I find.

Best,

Travis



---

archive/issue_comments_082161.json:
```json
{
    "body": "I've attached my review patch which address my comments and the doctests. The set comparisons in [comment:14] are a more general issue for another ticket. If you agree with my changes, you can set this to positive review.\n\nBest,\n\nTravis",
    "created_at": "2013-02-13T16:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82161",
    "user": "tscrim"
}
```

I've attached my review patch which address my comments and the doctests. The set comparisons in [comment:14] are a more general issue for another ticket. If you agree with my changes, you can set this to positive review.

Best,

Travis



---

archive/issue_comments_082162.json:
```json
{
    "body": "I modified the comparison of elements of `TotallyOrderedFiniteSet` to make it more coherent.",
    "created_at": "2013-02-14T00:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82162",
    "user": "vdelecroix"
}
```

I modified the comparison of elements of `TotallyOrderedFiniteSet` to make it more coherent.



---

archive/issue_comments_082163.json:
```json
{
    "body": "I added link in the documentation and double quotes where it is needed.",
    "created_at": "2013-02-15T21:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82163",
    "user": "vdelecroix"
}
```

I added link in the documentation and double quotes where it is needed.



---

archive/issue_comments_082164.json:
```json
{
    "body": "Changing keywords from \"Words, Sets, Cernay2012\" to \"Words, Sets, Cernay2012, days45\".",
    "created_at": "2013-02-15T21:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82164",
    "user": "tscrim"
}
```

Changing keywords from "Words, Sets, Cernay2012" to "Words, Sets, Cernay2012, days45".



---

archive/issue_comments_082165.json:
```json
{
    "body": "Looks good to me now. Thank you.\n\nTravis",
    "created_at": "2013-02-15T21:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82165",
    "user": "tscrim"
}
```

Looks good to me now. Thank you.

Travis



---

archive/issue_comments_082166.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-15T21:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82166",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082167.json:
```json
{
    "body": "This needs to be rebased to #6495 and also this fuzz needs to be fixed:\n\n```\napplying /release/merger/patches/trac_8920-alphabet.patch\nunable to find 'doc/en/reference/structure.rst' for patching\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/structure.rst.rej\npatching file sage/combinat/words/morphism.py\nHunk #1 succeeded at 12 with fuzz 2 (offset 0 lines).\n```\n",
    "created_at": "2013-02-19T11:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82167",
    "user": "jdemeyer"
}
```

This needs to be rebased to #6495 and also this fuzz needs to be fixed:

```
applying /release/merger/patches/trac_8920-alphabet.patch
unable to find 'doc/en/reference/structure.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/structure.rst.rej
patching file sage/combinat/words/morphism.py
Hunk #1 succeeded at 12 with fuzz 2 (offset 0 lines).
```




---

archive/issue_comments_082168.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-02-19T11:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82168",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082169.json:
```json
{
    "body": "I rebased the patch for #6495.\n\nVincnet",
    "created_at": "2013-02-19T12:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82169",
    "user": "vdelecroix"
}
```

I rebased the patch for #6495.

Vincnet



---

archive/issue_comments_082170.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-19T15:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82170",
    "user": "tscrim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_082171.json:
```json
{
    "body": "On OS X:\n\n```\nsage -t  --long -force_lib devel/sage/sage/sets/totally_ordered_finite_set.py\n**********************************************************************\nFile \"/Users/dehayebuildbot/build/sage/dehaye/dehaye_full/build/sage-5.8.beta1/devel/sage-main/sage/sets/totally_ordered_finite_set.py\", line 207:\n    sage: A(1) < 1\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n",
    "created_at": "2013-02-21T13:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82171",
    "user": "jdemeyer"
}
```

On OS X:

```
sage -t  --long -force_lib devel/sage/sage/sets/totally_ordered_finite_set.py
**********************************************************************
File "/Users/dehayebuildbot/build/sage/dehaye/dehaye_full/build/sage-5.8.beta1/devel/sage-main/sage/sets/totally_ordered_finite_set.py", line 207:
    sage: A(1) < 1
Expected:
    True
Got:
    False
**********************************************************************
```




---

archive/issue_comments_082172.json:
```json
{
    "body": "On `arando` (Ubuntu 12.04 Linux i686 32-bit):\n\n```\nsage -t  --long -force_lib devel/sage/sage/combinat/words/words.py\n**********************************************************************\nFile \"/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.8.beta1/devel/sage-main/sage/combinat/words/words.py\", line 851:\n    sage: Words('ab') >= Words('abc')\nExpected:\n    False\nGot:\n    True\n**********************************************************************\nFile \"/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.8.beta1/devel/sage-main/sage/combinat/words/words.py\", line 853:\n    sage: Words('abc') >= Words('ab')\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n",
    "created_at": "2013-02-21T13:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82172",
    "user": "jdemeyer"
}
```

On `arando` (Ubuntu 12.04 Linux i686 32-bit):

```
sage -t  --long -force_lib devel/sage/sage/combinat/words/words.py
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.8.beta1/devel/sage-main/sage/combinat/words/words.py", line 851:
    sage: Words('ab') >= Words('abc')
Expected:
    False
Got:
    True
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.8.beta1/devel/sage-main/sage/combinat/words/words.py", line 853:
    sage: Words('abc') >= Words('ab')
Expected:
    True
Got:
    False
**********************************************************************
```




---

archive/issue_comments_082173.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-02-21T13:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82173",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082174.json:
```json
{
    "body": "Attachment [trac_8920-alphabet.patch](tarball://root/attachments/some-uuid/ticket8920/trac_8920-alphabet.patch) by vdelecroix created at 2013-02-21 14:57:57\n\napply only this one (takes care of changes in the review patch)",
    "created_at": "2013-02-21T14:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82174",
    "user": "vdelecroix"
}
```

Attachment [trac_8920-alphabet.patch](tarball://root/attachments/some-uuid/ticket8920/trac_8920-alphabet.patch) by vdelecroix created at 2013-02-21 14:57:57

apply only this one (takes care of changes in the review patch)



---

archive/issue_comments_082175.json:
```json
{
    "body": "I do not understand the first failure on OS X but I made a small modification in `TotallyOrderedFiniteSet.__cmp__` and made more careful testing.\n\nFor the issue about comparisons of \"Words\", I just removed all related methods as they were needed nowhere and rely on comparison of alphabets which is not possible anymore.\n\nVincent",
    "created_at": "2013-02-21T15:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82175",
    "user": "vdelecroix"
}
```

I do not understand the first failure on OS X but I made a small modification in `TotallyOrderedFiniteSet.__cmp__` and made more careful testing.

For the issue about comparisons of "Words", I just removed all related methods as they were needed nowhere and rely on comparison of alphabets which is not possible anymore.

Vincent



---

archive/issue_comments_082176.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-21T15:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82176",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082177.json:
```json
{
    "body": "The long tests pass for me now. I'll try harder to remember to (re)run the long tests in the future.",
    "created_at": "2013-02-26T16:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82177",
    "user": "tscrim"
}
```

The long tests pass for me now. I'll try harder to remember to (re)run the long tests in the future.



---

archive/issue_comments_082178.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-26T16:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82178",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-28T10:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82179",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_082180.json:
```json
{
    "body": "Advice for the future: don't make needless whitespace changes, like you did here in `morphism.py`. This causes a conflict with #12230 for no good reason.",
    "created_at": "2013-04-05T14:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8920#issuecomment-82180",
    "user": "jdemeyer"
}
```

Advice for the future: don't make needless whitespace changes, like you did here in `morphism.py`. This causes a conflict with #12230 for no good reason.
