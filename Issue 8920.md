# Issue 8920: Factor code between words's alphabets and sets/enumerated sets/ordered sets

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-07 17:04:04

Assignee: sage-combinat

CC:  sage-combinat vdelecroix sstarosta

Keywords: Words, Sets

There is a lot of common code....


---

Comment by hivert created at 2012-02-09 01:42:51

Hi Vincent,

You are currently taking car of this. You may want either to reuse this ticket or to close it as duplicate.

Florent


---

Comment by hivert created at 2012-02-09 01:42:51

Changing keywords from "Words, Sets" to "Words, Sets, Cernay2012".


---

Comment by vdelecroix created at 2012-08-16 11:08:12

Many tests currently break because of the following behavior

```
sage: int(2) in Integers()
True
sage: int(2) in PositiveIntegers()
False
```



---

Comment by vdelecroix created at 2012-08-17 12:25:30

Changing status from new to needs_review.


---

Comment by tscrim created at 2012-11-28 00:14:48

Hey Vincent,
   The patch needs rebasing to 5.5.rc0. Once you upload the rebase, I'll review the patch.

I think the only merged patch which might have caused the conflict is #13677.

Thanks,

Travis


---

Comment by vdelecroix created at 2012-11-30 16:49:58

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

Comment by tscrim created at 2012-12-02 08:10:26

Changing status from needs_review to needs_info.


---

Comment by tscrim created at 2012-12-02 08:10:26

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

Comment by vdelecroix created at 2012-12-05 17:17:07

Changing status from needs_info to needs_review.


---

Comment by vdelecroix created at 2012-12-05 17:17:07

Hi Travis,

thanks for reviewing the patch and your comments! I uploaded a new version with two major changes
  * a new class TotallyOrderedFiniteSet
  * a dependency on #13801

All problems are similar to the ones there are currently with Nathann and posets (#13747) : to be or not to be a facade, that is the question. One major difference with the previous patch is that we provide a class TotallyOrderedFiniteSet which has a facade option behavior and may choose the behavior you prefer.

*How do facades behave*

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


*Not using facade ?*

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


*Partial conclusion*

 we do prefer having facade = True as a default behavior (as Nathann does).

*About endomorphisms*

Two reason to change is_endomorphism() are: 
  1) the operator <= is not defined on sets
  2) the test was mathematically inaccurate : an endomorphism is a morphism for which domain = codomain (and not just a subset of codomain)

Thanks,
Stepan and Vincent


---

Comment by nthiery created at 2012-12-06 09:56:47

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

Comment by tscrim created at 2012-12-12 20:04:13

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

Comment by tscrim created at 2013-02-01 12:42:47

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

Comment by tscrim created at 2013-02-13 16:55:05

I've attached my review patch which address my comments and the doctests. The set comparisons in [comment:14] are a more general issue for another ticket. If you agree with my changes, you can set this to positive review.

Best,

Travis


---

Comment by vdelecroix created at 2013-02-14 00:04:17

I modified the comparison of elements of `TotallyOrderedFiniteSet` to make it more coherent.


---

Comment by vdelecroix created at 2013-02-15 21:24:22

I added link in the documentation and double quotes where it is needed.


---

Comment by tscrim created at 2013-02-15 21:34:19

Changing keywords from "Words, Sets, Cernay2012" to "Words, Sets, Cernay2012, days45".


---

Comment by tscrim created at 2013-02-15 21:34:19

Looks good to me now. Thank you.

Travis


---

Comment by tscrim created at 2013-02-15 21:34:19

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-19 11:00:57

This needs to be rebased to #6495 and also this fuzz needs to be fixed:

```
applying /release/merger/patches/trac_8920-alphabet.patch
unable to find 'doc/en/reference/structure.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/structure.rst.rej
patching file sage/combinat/words/morphism.py
Hunk #1 succeeded at 12 with fuzz 2 (offset 0 lines).
```



---

Comment by jdemeyer created at 2013-02-19 11:00:57

Changing status from positive_review to needs_work.


---

Comment by vdelecroix created at 2013-02-19 12:29:53

I rebased the patch for #6495.

Vincnet


---

Comment by tscrim created at 2013-02-19 15:15:25

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-02-21 13:19:58

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

Comment by jdemeyer created at 2013-02-21 13:20:55

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

Comment by jdemeyer created at 2013-02-21 13:32:21

Changing status from positive_review to needs_work.


---

Attachment

apply only this one (takes care of changes in the review patch)


---

Comment by vdelecroix created at 2013-02-21 15:00:28

I do not understand the first failure on OS X but I made a small modification in `TotallyOrderedFiniteSet.__cmp__` and made more careful testing.

For the issue about comparisons of "Words", I just removed all related methods as they were needed nowhere and rely on comparison of alphabets which is not possible anymore.

Vincent


---

Comment by vdelecroix created at 2013-02-21 15:04:29

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-02-26 16:23:57

The long tests pass for me now. I'll try harder to remember to (re)run the long tests in the future.


---

Comment by tscrim created at 2013-02-26 16:23:57

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-28 10:30:47

Resolution: fixed


---

Comment by jdemeyer created at 2013-04-05 14:51:01

Advice for the future: don't make needless whitespace changes, like you did here in `morphism.py`. This causes a conflict with #12230 for no good reason.
