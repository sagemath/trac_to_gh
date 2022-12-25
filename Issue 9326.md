# Issue 9326: Add cohomology of toric varieties

archive/issues_009326.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @novoselt\n\nThis patch adds a cohomology ring to toric varieties. This is then used for characteristic classes.\n\nI'm using the usual description of the rational cohomology ring via the Stanley-Reisner ideal of the fan. This does not work for singular varities with worse than orbifold singularities. I don't have any good candidate for the \"space where the Chern classes live\" in that case. \n\nApplies on top of \n* #9245: trac_9245_named_toric_varieties.py\n* #8988: trac_8988_Kahlercone_lattice.patch\n* #9296: trac_9296_lattice_computations_for_cones.patch\nand their prerequisites...\n\nIssue created by migration from https://trac.sagemath.org/ticket/9326\n\n",
    "created_at": "2010-06-24T10:46:02Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Add cohomology of toric varieties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9326",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  @novoselt

This patch adds a cohomology ring to toric varieties. This is then used for characteristic classes.

I'm using the usual description of the rational cohomology ring via the Stanley-Reisner ideal of the fan. This does not work for singular varities with worse than orbifold singularities. I don't have any good candidate for the "space where the Chern classes live" in that case. 

Applies on top of 
* #9245: trac_9245_named_toric_varieties.py
* #8988: trac_8988_Kahlercone_lattice.patch
* #9296: trac_9296_lattice_computations_for_cones.patch
and their prerequisites...

Issue created by migration from https://trac.sagemath.org/ticket/9326





---

archive/issue_comments_087806.json:
```json
{
    "body": "It would be nice if there were a `Cone_of_toric_variety` or so that knows about the toric variety it belongs to, then `cone.HH()` could return its cohomology class. But right now the fan could be shared between different toric varieties, so there is no way to attach this information. We might want to use the `EnhancedFan`/`EnhancedCone` framework already for toric varieties....\n\nNote: The `HH` abbreviation (Macaulay2 notation) for cohomology might be cryptic, but then expanding it just replaces that question with \"which cohomology theory are you talking about?\". So I don't know whats worse...",
    "created_at": "2010-06-24T11:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87806",
    "user": "https://github.com/vbraun"
}
```

It would be nice if there were a `Cone_of_toric_variety` or so that knows about the toric variety it belongs to, then `cone.HH()` could return its cohomology class. But right now the fan could be shared between different toric varieties, so there is no way to attach this information. We might want to use the `EnhancedFan`/`EnhancedCone` framework already for toric varieties....

Note: The `HH` abbreviation (Macaulay2 notation) for cohomology might be cryptic, but then expanding it just replaces that question with "which cohomology theory are you talking about?". So I don't know whats worse...



---

archive/issue_comments_087807.json:
```json
{
    "body": "I didn't get the cc before, I guess trac engine cannot translate names into accounts. Will look over once prerequisites are settled.",
    "created_at": "2010-06-26T00:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87807",
    "user": "https://github.com/novoselt"
}
```

I didn't get the cc before, I guess trac engine cannot translate names into accounts. Will look over once prerequisites are settled.



---

archive/issue_comments_087808.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-03T13:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87808",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087809.json:
```json
{
    "body": "Updated to work with changed method names in `toric_variety_library.py`.",
    "created_at": "2010-07-03T13:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87809",
    "user": "https://github.com/vbraun"
}
```

Updated to work with changed method names in `toric_variety_library.py`.



---

archive/issue_events_022979.json:
```json
{
    "actor": "https://github.com/novoselt",
    "created_at": "2010-07-03T20:25:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9326#event-22979"
}
```



---

archive/issue_comments_087810.json:
```json
{
    "body": "This patch applied cleanly on top of #9245, so it seems that there is no need for Kaehler/Mori cones and cone-lattices computations. Let's keep it this way then, since #9245 and all its prerequisites already got positive review.",
    "created_at": "2010-07-03T20:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87810",
    "user": "https://github.com/novoselt"
}
```

This patch applied cleanly on top of #9245, so it seems that there is no need for Kaehler/Mori cones and cone-lattices computations. Let's keep it this way then, since #9245 and all its prerequisites already got positive review.



---

archive/issue_comments_087811.json:
```json
{
    "body": "If there is only one function for which it would be nice to have a corresponding cone method, I'd wait before redoing toric varieties to make copies of fans.\n\nI don't like `HH` notation, which I associate with Hochschild (co)homology... While it is used in Macaulay2, it does not quite seem to be in the spirit of Sage. Macaulay2 is much more flexible in terms of operators and it may be a good choice there, but here I would prefer `cohomology_ring` etc. I don't see any problems with \"What cohomology?\" question since it can be clearly indicated in the documentation of all functions. (Do we plan to support multiple cohomology theories?)\n\nI think `HH_class_of(cone)` ===> `cohomology_class(cone)` would be better.\n\nAlso `HH_exp(p)` ===> `cohomology_exp(p)` or better yet just `exp(p)`. Even better would be `p.exp()` which will not require toric variety at all, but that requires completely different handling so should be left till after divisor patch is merged.\n\nI propose to do the following with `c` and others:\n\n```\ndef Chern_class(self, deg=None): \n    r\"\"\"\n    Return Chern class of the tangent bundle of the toric variety. \n\n    A synonym for this function is ``c``.\n    ...\n    \"\"\"\n    ... # actual code\n\nc = Chern_class\n```\n\nThis way we keep convenient access to all this functions, but at the same time provide descriptive names, so that glancing on TAB-completion clearly shows what is available. The same thing is done with `.numerical_approx()` and `.n()` methods in Sage.",
    "created_at": "2010-07-03T21:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87811",
    "user": "https://github.com/novoselt"
}
```

If there is only one function for which it would be nice to have a corresponding cone method, I'd wait before redoing toric varieties to make copies of fans.

I don't like `HH` notation, which I associate with Hochschild (co)homology... While it is used in Macaulay2, it does not quite seem to be in the spirit of Sage. Macaulay2 is much more flexible in terms of operators and it may be a good choice there, but here I would prefer `cohomology_ring` etc. I don't see any problems with "What cohomology?" question since it can be clearly indicated in the documentation of all functions. (Do we plan to support multiple cohomology theories?)

I think `HH_class_of(cone)` ===> `cohomology_class(cone)` would be better.

Also `HH_exp(p)` ===> `cohomology_exp(p)` or better yet just `exp(p)`. Even better would be `p.exp()` which will not require toric variety at all, but that requires completely different handling so should be left till after divisor patch is merged.

I propose to do the following with `c` and others:

```
def Chern_class(self, deg=None): 
    r"""
    Return Chern class of the tangent bundle of the toric variety. 

    A synonym for this function is ``c``.
    ...
    """
    ... # actual code

c = Chern_class
```

This way we keep convenient access to all this functions, but at the same time provide descriptive names, so that glancing on TAB-completion clearly shows what is available. The same thing is done with `.numerical_approx()` and `.n()` methods in Sage.



---

archive/issue_comments_087812.json:
```json
{
    "body": "As for the cones, once I get to the Chow group it would also be nice if `cone.A()` would return the Chow cycle associated to the cone. And a cone should be able to return the orbit closure as a toric variety. Really, in toric geometry there is lots of stuff associated to a cone and it would be nice if we could write `cone.stuff()`.\n\nAs for the cohomology ring, I did the name changes. The new patch also defines classes `CohomologyRing(QuotientRing)` and `CohomologyClass(QuotientRingElement)`, so we have something to attach `exp()` and `truncate_to_degree()` to.",
    "created_at": "2010-07-05T12:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87812",
    "user": "https://github.com/vbraun"
}
```

As for the cones, once I get to the Chow group it would also be nice if `cone.A()` would return the Chow cycle associated to the cone. And a cone should be able to return the orbit closure as a toric variety. Really, in toric geometry there is lots of stuff associated to a cone and it would be nice if we could write `cone.stuff()`.

As for the cohomology ring, I did the name changes. The new patch also defines classes `CohomologyRing(QuotientRing)` and `CohomologyClass(QuotientRingElement)`, so we have something to attach `exp()` and `truncate_to_degree()` to.



---

archive/issue_comments_087813.json:
```json
{
    "body": "Replying to [comment:6 vbraun]:\n> As for the cones, once I get to the Chow group it would also be nice if `cone.A()` would return the Chow cycle associated to the cone. And a cone should be able to return the orbit closure as a toric variety. Really, in toric geometry there is lots of stuff associated to a cone and it would be nice if we could write `cone.stuff()`.\n\nOK, will work on it this week.\n\n> As for the cohomology ring, I did the name changes. The new patch also defines classes `CohomologyRing(QuotientRing)` and `CohomologyClass(QuotientRingElement)`, so we have something to attach `exp()` and `truncate_to_degree()` to.\n\nGreat and neat! However, http://wiki.sagemath.org/coercion advises against overriding `__call__` method in classes derived from `Parent`, and in this case I think it should be doable to do it the recommended way.",
    "created_at": "2010-07-05T13:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87813",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:6 vbraun]:
> As for the cones, once I get to the Chow group it would also be nice if `cone.A()` would return the Chow cycle associated to the cone. And a cone should be able to return the orbit closure as a toric variety. Really, in toric geometry there is lots of stuff associated to a cone and it would be nice if we could write `cone.stuff()`.

OK, will work on it this week.

> As for the cohomology ring, I did the name changes. The new patch also defines classes `CohomologyRing(QuotientRing)` and `CohomologyClass(QuotientRingElement)`, so we have something to attach `exp()` and `truncate_to_degree()` to.

Great and neat! However, http://wiki.sagemath.org/coercion advises against overriding `__call__` method in classes derived from `Parent`, and in this case I think it should be doable to do it the recommended way.



---

archive/issue_comments_087814.json:
```json
{
    "body": "Note that `QuotientRing`  does override `__call__` and, moreover, explicitly refers to `QuotientRingElement`. I'll see if I can fix `QuotientRing` to play nice with `_element_constructor_`.",
    "created_at": "2010-07-05T14:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87814",
    "user": "https://github.com/vbraun"
}
```

Note that `QuotientRing`  does override `__call__` and, moreover, explicitly refers to `QuotientRingElement`. I'll see if I can fix `QuotientRing` to play nice with `_element_constructor_`.



---

archive/issue_comments_087815.json:
```json
{
    "body": "I fixed `QuotientRing` to use the coercion as described in the wiki, but now everything else breaks. Something is going on with the coercion system that I don't understand. With the `first_attempt.patch`, the quotient rings work fine. But, for example, this now fails:\n\n```\nsage: FF = FiniteField(7)\nsage: P.<x> = PolynomialRing(FF)\nsage: x+1\nTypeError                                 Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.5.alpha1/devel/sage-main/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10876)()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()\n\nTypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in x over Finite Field of size 7' and 'Integer Ring'\n```\n\nBut I neither touched univariate polynomial rings nor finite field code! Does anyone understand what is going on?",
    "created_at": "2010-07-06T06:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87815",
    "user": "https://github.com/vbraun"
}
```

I fixed `QuotientRing` to use the coercion as described in the wiki, but now everything else breaks. Something is going on with the coercion system that I don't understand. With the `first_attempt.patch`, the quotient rings work fine. But, for example, this now fails:

```
sage: FF = FiniteField(7)
sage: P.<x> = PolynomialRing(FF)
sage: x+1
TypeError                                 Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.alpha1/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10876)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in x over Finite Field of size 7' and 'Integer Ring'
```

But I neither touched univariate polynomial rings nor finite field code! Does anyone understand what is going on?



---

archive/issue_comments_087816.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-07-06T06:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87816",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_087817.json:
```json
{
    "body": "Test patch, breaks coercion for many rings for some reason.",
    "created_at": "2010-07-06T06:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87817",
    "user": "https://github.com/vbraun"
}
```

Test patch, breaks coercion for many rings for some reason.



---

archive/issue_comments_087818.json:
```json
{
    "body": "Attachment [first_attempt.patch](tarball://root/attachments/some-uuid/ticket9326/first_attempt.patch) by @novoselt created at 2010-07-06 15:56:34\n\nThis patch is actually related to #9429, so I am moving there.",
    "created_at": "2010-07-06T15:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87818",
    "user": "https://github.com/novoselt"
}
```

Attachment [first_attempt.patch](tarball://root/attachments/some-uuid/ticket9326/first_attempt.patch) by @novoselt created at 2010-07-06 15:56:34

This patch is actually related to #9429, so I am moving there.



---

archive/issue_comments_087819.json:
```json
{
    "body": "Updated patch that implements classes `CohomologyRing` and `CohomologyClass`. These do not follow the coercion model since their superclasses `QuotientRing_generic` and `QuotientRingElement` have not been converted to the new coercion model. The new classes will easily convert to the new coercion model once `QuotientRing` and its subclasses are updated.\n\nFirst apply `trac_9326_QuotientRing_fix_derived_classes.patch` (which is just a renamed version of Andrey's `trac_9429_fix_derived_classes.2.patch`), then `trac_9326_toric_variety_cohomology.patch` on top.",
    "created_at": "2010-07-15T18:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87819",
    "user": "https://github.com/vbraun"
}
```

Updated patch that implements classes `CohomologyRing` and `CohomologyClass`. These do not follow the coercion model since their superclasses `QuotientRing_generic` and `QuotientRingElement` have not been converted to the new coercion model. The new classes will easily convert to the new coercion model once `QuotientRing` and its subclasses are updated.

First apply `trac_9326_QuotientRing_fix_derived_classes.patch` (which is just a renamed version of Andrey's `trac_9429_fix_derived_classes.2.patch`), then `trac_9326_toric_variety_cohomology.patch` on top.



---

archive/issue_comments_087820.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-15T18:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87820",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_087821.json:
```json
{
    "body": "1. General documentation comment: I would appreciate precise definitions and/or links (Wikipedia?) to detailed description of Chern/Todd classes etc. I think that others would appreciate it too.\n   1. `primitive_collections` - I don't like the statement that it returns generators of Stanley-Reisner ideal. I'd prefer to have the combinatorial description (which is already present there) and a note that they *correspond* to generators of this ideal.\n   2. `Stanley_Reisner_ideal` and `linear_equivalence_ideal` - do they really belong to the fan class? The fact that it is necessary to pass a ring to them suggests that maybe not. (Also, it is not clear what is the point to cache the result for a potentially new ring next time.) How about moving them to toric variety class, removing the ring argument, and making them return an ideal in `QQ[coordinate names of the variety]`? Note that such a ring is unique in Sage, so if you \"construct\" it twice in two different functions, it actually will be the same one. So your code\n   {{{\nR = PolynomialRing(QQ, variety.variable_names()) \nself._polynomial_ring = R \nI = variety._fan.linear_equivalence_ideal(R) + variety._fan.Stanley_Reisner_ideal(R) \nsuper(CohomologyRing, self).__init__(R, I, names=variety.variable_names()) \n}}}\n will be replaced with\n {{{\nR = PolynomialRing(QQ, variety.variable_names()) \nself._polynomial_ring = R \nI = variety.linear_equivalence_ideal() + variety.Stanley_Reisner_ideal() \nsuper(CohomologyRing, self).__init__(R, I, names=variety.variable_names()) \n}}}\n It may be good actually to give some name to this ring `R` and make it accessible from the toric variety as well. (Does it have some standard name? It suppose it should, since it is the ambient ring of the Stanley-Reisner ideal.)\n1. Regarding names of divisors and divisor classes. I personally think that it is just fine to have them the same, but maybe they should be different from coordinate names. The reason is that I would like to inject both coordinates and divisors into the global name space and work with them. I think that I would prefer coordinates `x, y, z2, z3, z4` to be translated into `D_x, D_y, D2, D3, D4`. This may be a bit hard to implement, since it requires tracking which variables were given explicit names and which were created automatically, maybe `D_x, D_y, D_z2, D_z3, D_z4` or just `D0, D1, D2, D3, D4` would be better. In any way there should be a way for the user to provide custom names. I think there should be one more optional argument to the toric variety constructor and if it was not given, then the first call to `cohomology_ring` can specify these names. (I don't mind having a separate follow-up ticket for this and can provide a patch on top of this one.)\n2. `cohomology_ring` - can we remove \"... as a quotient of a polynomial ring.\" from the first line of documentation? It is no longer quite true since there are special classes for cohomology now.\n3. `CohomologyRing` constructor - input is not described in the documentation and from the code it is clear that not any toric variety will work. The second exception is a bit misleading since it says that `CC` is required as the base field, but actually it checks only characteristics (we already had some discussion about it). How about the following: the constructor should check if the base field is exactly complex (by which I mean any complex field in Sage independent of precision, maybe function fields over complex one are also OK?) if not, it should raise an exception. However there should be a function like `X.treat_base_field_as_CC()` and if it was called, then all cohomology computations proceed without checks of the base field. That way we preserve mathematical correctness yet allow users to use any representation they want at their own risk. (To avoid potential complications with cached and created objects, this function should not be reversible, i.e. it is not OK to turn off `CC`-check and later turn it back on for the same variety.)\n4. `truncate_to_degree` - the name does not match what the function actually does. I would expect it to drop all terms higher than the given degree, but it also \"truncates\" lower terms. Can we change it to something like `part_of_degree`?\n5. `exp` - would be nice to mention in the documentation that there should be no constant part and explain why. Its output description is also not quite clear, I think it would be better to write that it returns a cohomology class.\n6. `cohomology_basis` - in the first output case you meant `H^d`, not `H^\\bullet`.\n7. `cohomology_class` - can we add some message to `NotImplementedError`? Note also that #9470 should allow implementing `cone.cohomology_class()` as you wanted.\n8. `volume_form` - I think documentation should explain the normalization of this form. What assumptions on the variety does this function make? Simplicial? Complete? Generated by maximal-dimensional cones? It would be nice to check for those that are not checked by cohomology ring construction.\n9. `integrate` - would be nice if the documentation explained that integration is done with respect to `volume_form`, i.e. that normalization is the same.\n10. `Todd_class` - can we add a message to `NotImplementedError`?\n11. `Euler` - in the spirit of `Chern_class` etc., I think it would be more consistent to call it `Euler_number` and add a standard notation alias `X.chi()`. Out of curiosity - why is there a special case for complete varieties? Should it be faster?",
    "created_at": "2010-07-18T04:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87821",
    "user": "https://github.com/novoselt"
}
```

1. General documentation comment: I would appreciate precise definitions and/or links (Wikipedia?) to detailed description of Chern/Todd classes etc. I think that others would appreciate it too.
   1. `primitive_collections` - I don't like the statement that it returns generators of Stanley-Reisner ideal. I'd prefer to have the combinatorial description (which is already present there) and a note that they *correspond* to generators of this ideal.
   2. `Stanley_Reisner_ideal` and `linear_equivalence_ideal` - do they really belong to the fan class? The fact that it is necessary to pass a ring to them suggests that maybe not. (Also, it is not clear what is the point to cache the result for a potentially new ring next time.) How about moving them to toric variety class, removing the ring argument, and making them return an ideal in `QQ[coordinate names of the variety]`? Note that such a ring is unique in Sage, so if you "construct" it twice in two different functions, it actually will be the same one. So your code
   {{{
R = PolynomialRing(QQ, variety.variable_names()) 
self._polynomial_ring = R 
I = variety._fan.linear_equivalence_ideal(R) + variety._fan.Stanley_Reisner_ideal(R) 
super(CohomologyRing, self).__init__(R, I, names=variety.variable_names()) 
}}}
 will be replaced with
 {{{
R = PolynomialRing(QQ, variety.variable_names()) 
self._polynomial_ring = R 
I = variety.linear_equivalence_ideal() + variety.Stanley_Reisner_ideal() 
super(CohomologyRing, self).__init__(R, I, names=variety.variable_names()) 
}}}
 It may be good actually to give some name to this ring `R` and make it accessible from the toric variety as well. (Does it have some standard name? It suppose it should, since it is the ambient ring of the Stanley-Reisner ideal.)
1. Regarding names of divisors and divisor classes. I personally think that it is just fine to have them the same, but maybe they should be different from coordinate names. The reason is that I would like to inject both coordinates and divisors into the global name space and work with them. I think that I would prefer coordinates `x, y, z2, z3, z4` to be translated into `D_x, D_y, D2, D3, D4`. This may be a bit hard to implement, since it requires tracking which variables were given explicit names and which were created automatically, maybe `D_x, D_y, D_z2, D_z3, D_z4` or just `D0, D1, D2, D3, D4` would be better. In any way there should be a way for the user to provide custom names. I think there should be one more optional argument to the toric variety constructor and if it was not given, then the first call to `cohomology_ring` can specify these names. (I don't mind having a separate follow-up ticket for this and can provide a patch on top of this one.)
2. `cohomology_ring` - can we remove "... as a quotient of a polynomial ring." from the first line of documentation? It is no longer quite true since there are special classes for cohomology now.
3. `CohomologyRing` constructor - input is not described in the documentation and from the code it is clear that not any toric variety will work. The second exception is a bit misleading since it says that `CC` is required as the base field, but actually it checks only characteristics (we already had some discussion about it). How about the following: the constructor should check if the base field is exactly complex (by which I mean any complex field in Sage independent of precision, maybe function fields over complex one are also OK?) if not, it should raise an exception. However there should be a function like `X.treat_base_field_as_CC()` and if it was called, then all cohomology computations proceed without checks of the base field. That way we preserve mathematical correctness yet allow users to use any representation they want at their own risk. (To avoid potential complications with cached and created objects, this function should not be reversible, i.e. it is not OK to turn off `CC`-check and later turn it back on for the same variety.)
4. `truncate_to_degree` - the name does not match what the function actually does. I would expect it to drop all terms higher than the given degree, but it also "truncates" lower terms. Can we change it to something like `part_of_degree`?
5. `exp` - would be nice to mention in the documentation that there should be no constant part and explain why. Its output description is also not quite clear, I think it would be better to write that it returns a cohomology class.
6. `cohomology_basis` - in the first output case you meant `H^d`, not `H^\bullet`.
7. `cohomology_class` - can we add some message to `NotImplementedError`? Note also that #9470 should allow implementing `cone.cohomology_class()` as you wanted.
8. `volume_form` - I think documentation should explain the normalization of this form. What assumptions on the variety does this function make? Simplicial? Complete? Generated by maximal-dimensional cones? It would be nice to check for those that are not checked by cohomology ring construction.
9. `integrate` - would be nice if the documentation explained that integration is done with respect to `volume_form`, i.e. that normalization is the same.
10. `Todd_class` - can we add a message to `NotImplementedError`?
11. `Euler` - in the spirit of `Chern_class` etc., I think it would be more consistent to call it `Euler_number` and add a standard notation alias `X.chi()`. Out of curiosity - why is there a special case for complete varieties? Should it be faster?



---

archive/issue_comments_087822.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-18T04:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87822",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087823.json:
```json
{
    "body": "P.S. Looks like patch at #9470 is in conflict with this one, so we should decide which one will be first, i.e. if you want to use it here or not.",
    "created_at": "2010-07-18T04:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87823",
    "user": "https://github.com/novoselt"
}
```

P.S. Looks like patch at #9470 is in conflict with this one, so we should decide which one will be first, i.e. if you want to use it here or not.



---

archive/issue_comments_087824.json:
```json
{
    "body": "3. I was trying to not have yet another ring attached to fans, since there are already too many rings floating around ;-)  On the other hand, the SR ideal makes sense just for fans so I wanted to move the SR ideal function there, maybe someone is interested in it without the toric variety. I'll move the caching of rings up to the toric variety.\n\n4. I agree with the divisor names, but until we have the divisors finished I think its easiest to just go with default names = names of homogeneous coordinates. \n\n12. Integration is with compact supports (it is really intersection in homology)\n\n```\nsage: C2 = toric_varieties.A2()\nsage: C2.volume_form()\n0\n```\n\nand the index theorem doesn't work. In particular, Euler number of `C^2` = Euler number of point = 1. And yes, evaluation of the index theorem is faster than computing a basis for the (co)homology groups.",
    "created_at": "2010-07-18T19:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87824",
    "user": "https://github.com/vbraun"
}
```

3. I was trying to not have yet another ring attached to fans, since there are already too many rings floating around ;-)  On the other hand, the SR ideal makes sense just for fans so I wanted to move the SR ideal function there, maybe someone is interested in it without the toric variety. I'll move the caching of rings up to the toric variety.

4. I agree with the divisor names, but until we have the divisors finished I think its easiest to just go with default names = names of homogeneous coordinates. 

12. Integration is with compact supports (it is really intersection in homology)

```
sage: C2 = toric_varieties.A2()
sage: C2.volume_form()
0
```

and the index theorem doesn't work. In particular, Euler number of `C^2` = Euler number of point = 1. And yes, evaluation of the index theorem is faster than computing a basis for the (co)homology groups.



---

archive/issue_comments_087825.json:
```json
{
    "body": "3. Well, if SR ideal does make sense for fans, then, since it is an ideal, it lives in some ring. What is this ring? (And in what situations does it come up?) It just seems to me that if this ring is not canonically associated to the fan, then it means that both the ring and the ideal actually correspond to some object derived from the fan, rather than fan itself. If this is the case and you still really want to have it as a method of a fan, then I think that the ring argument must be mandatory.\n\n4. OK, let's leave this for later (I'd actually prefer to play with it a bit before choosing a default name scheme).\n\n11-12. I find this example quite confusing for a new user. The plane has zero volume form? What about `dx\\wedge dy`??? We go to http://en.wikipedia.org/wiki/Volume_form and see that any orientable Riemannian manifold has infinitely many volume forms, and they are never 0. Can we maybe rename it to `volume_class` or something? That's how other functions returning cohomology classes are named. By the way, calling it for a non-simplicial variety (e.g. `Cube_face_fan`) crashes with a non-informative message in the context of toric varieties: \"self must be a square matrix.\"",
    "created_at": "2010-07-18T21:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87825",
    "user": "https://github.com/novoselt"
}
```

3. Well, if SR ideal does make sense for fans, then, since it is an ideal, it lives in some ring. What is this ring? (And in what situations does it come up?) It just seems to me that if this ring is not canonically associated to the fan, then it means that both the ring and the ideal actually correspond to some object derived from the fan, rather than fan itself. If this is the case and you still really want to have it as a method of a fan, then I think that the ring argument must be mandatory.

4. OK, let's leave this for later (I'd actually prefer to play with it a bit before choosing a default name scheme).

11-12. I find this example quite confusing for a new user. The plane has zero volume form? What about `dx\wedge dy`??? We go to http://en.wikipedia.org/wiki/Volume_form and see that any orientable Riemannian manifold has infinitely many volume forms, and they are never 0. Can we maybe rename it to `volume_class` or something? That's how other functions returning cohomology classes are named. By the way, calling it for a non-simplicial variety (e.g. `Cube_face_fan`) crashes with a non-informative message in the context of toric varieties: "self must be a square matrix."



---

archive/issue_comments_087826.json:
```json
{
    "body": "1., 2. Done.\n\n3. `Fan.Stanley_Reisner_ideal` and `Fan.linear_equivalence_ideal` now require a ring. There is no special name for this ring in the literature as far as I know.\n\n4. Cohomology classes are now printed as `[1+z+z^2]` instead of `1+z+z^2`.\n\n5. Done.\n\n6. I've changed `CohomologyRing` to always take the variety to be over complex numbers, and made that clear in the docstring. The `ToricVariety_fan.cohomology_ring()` method checks that the field has characteristic zero, which is then treated as complex numbers. Without having any other cohomology rings in mind, I think this is ought to be fine for now.\n\n7., 8., 9. Done\n\n10. Renamed to `volume_class()` now raises a `ValueError` if it does not exist.\n\n21. Done.\n\n12., 13., 14. Done.",
    "created_at": "2010-07-24T22:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87826",
    "user": "https://github.com/vbraun"
}
```

1., 2. Done.

3. `Fan.Stanley_Reisner_ideal` and `Fan.linear_equivalence_ideal` now require a ring. There is no special name for this ring in the literature as far as I know.

4. Cohomology classes are now printed as `[1+z+z^2]` instead of `1+z+z^2`.

5. Done.

6. I've changed `CohomologyRing` to always take the variety to be over complex numbers, and made that clear in the docstring. The `ToricVariety_fan.cohomology_ring()` method checks that the field has characteristic zero, which is then treated as complex numbers. Without having any other cohomology rings in mind, I think this is ought to be fine for now.

7., 8., 9. Done

10. Renamed to `volume_class()` now raises a `ValueError` if it does not exist.

21. Done.

12., 13., 14. Done.



---

archive/issue_comments_087827.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-25T01:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87827",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087828.json:
```json
{
    "body": "Move cohomology_class() method from ToricVariety_field to Cone_of_toric_variety.",
    "created_at": "2010-07-25T04:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87828",
    "user": "https://github.com/vbraun"
}
```

Move cohomology_class() method from ToricVariety_field to Cone_of_toric_variety.



---

archive/issue_comments_087829.json:
```json
{
    "body": "Attachment [trac_9326_QuotientRing_fix_derived_classes.2.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_QuotientRing_fix_derived_classes.2.patch) by @novoselt created at 2010-07-27 06:36:20\n\nRebase against 4.5.alpha0",
    "created_at": "2010-07-27T06:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87829",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9326_QuotientRing_fix_derived_classes.2.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_QuotientRing_fix_derived_classes.2.patch) by @novoselt created at 2010-07-27 06:36:20

Rebase against 4.5.alpha0



---

archive/issue_comments_087830.json:
```json
{
    "body": "Updated patch `trac_9326_toric_variety_cohomology.patch` to fix coverage warnings.",
    "created_at": "2010-07-27T13:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87830",
    "user": "https://github.com/vbraun"
}
```

Updated patch `trac_9326_toric_variety_cohomology.patch` to fix coverage warnings.



---

archive/issue_comments_087831.json:
```json
{
    "body": "fix coverage warnings",
    "created_at": "2010-07-27T13:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87831",
    "user": "https://github.com/vbraun"
}
```

fix coverage warnings



---

archive/issue_comments_087832.json:
```json
{
    "body": "Attachment [trac_9326_toric_variety_cohomology.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_toric_variety_cohomology.patch) by @novoselt created at 2010-07-27 17:19:49\n\nAwesome! I have a few little changes and typo fixes which I will post later today and if you agree with them it goes to positive review!",
    "created_at": "2010-07-27T17:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87832",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9326_toric_variety_cohomology.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_toric_variety_cohomology.patch) by @novoselt created at 2010-07-27 17:19:49

Awesome! I have a few little changes and typo fixes which I will post later today and if you agree with them it goes to positive review!



---

archive/issue_comments_087833.json:
```json
{
    "body": "Attachment [trac_9326_toric_cohomology_reviewer.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_toric_cohomology_reviewer.patch) by @novoselt created at 2010-07-28 04:54:46\n\nOK, here is the patch, let me know if you approve it. I have\n* changed `_latex_` to give LaTeX representation of the lift-polynomial, I think it is better than using text representation;\n* made `cohomology_basis` return tuple of tuples so that it does not get changed accidentally, I also rewrote its computation using list comprehension instead of functional style since I got a little confused. Of course, this is just me, so I am ready to change it back if you want. I actually though that calling `map` and filter should be faster, but\n {{{\nsage: L = [1..1000]\nsage: timeit(\"[e for e in L]\", number=10000)\n10000 loops, best of 3: 114 \u00b5s per loop\nsage: timeit(\"map(lambda x: x, L)\", number=10000)\n10000 loops, best of 3: 263 \u00b5s per loop\nsage: timeit(\"[e for e in L if e > 50]\", number=10000)\n10000 loops, best of 3: 637 \u00b5s per loop\nsage: timeit(\"filter(lambda x: x > 50, L)\", number=10000)\n10000 loops, best of 3: 775 \u00b5s per loop\n}}}\n so it seems that actually list comprehension is a little more efficient. My variant also does the degree splitting in a single pass through the full basis;\n* made changes in a couple of places to check for existence of cached value before checking for errors (my sneaky plan is to allow myself to circumvent you characteristic zero defense system by setting `_cohomology_ring` directly if I wish so, but for sane users everything will work exactly as you have written it originally ;-));\n* some little changes to the documentation, see the patch.\n\nI'll now run complete tests including this patch, to make sure there are no surprises in unrelated places, but if you are happy with modifications I am ready to switch it to positive review.",
    "created_at": "2010-07-28T04:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87833",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9326_toric_cohomology_reviewer.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_toric_cohomology_reviewer.patch) by @novoselt created at 2010-07-28 04:54:46

OK, here is the patch, let me know if you approve it. I have
* changed `_latex_` to give LaTeX representation of the lift-polynomial, I think it is better than using text representation;
* made `cohomology_basis` return tuple of tuples so that it does not get changed accidentally, I also rewrote its computation using list comprehension instead of functional style since I got a little confused. Of course, this is just me, so I am ready to change it back if you want. I actually though that calling `map` and filter should be faster, but
 {{{
sage: L = [1..1000]
sage: timeit("[e for e in L]", number=10000)
10000 loops, best of 3: 114 µs per loop
sage: timeit("map(lambda x: x, L)", number=10000)
10000 loops, best of 3: 263 µs per loop
sage: timeit("[e for e in L if e > 50]", number=10000)
10000 loops, best of 3: 637 µs per loop
sage: timeit("filter(lambda x: x > 50, L)", number=10000)
10000 loops, best of 3: 775 µs per loop
}}}
 so it seems that actually list comprehension is a little more efficient. My variant also does the degree splitting in a single pass through the full basis;
* made changes in a couple of places to check for existence of cached value before checking for errors (my sneaky plan is to allow myself to circumvent you characteristic zero defense system by setting `_cohomology_ring` directly if I wish so, but for sane users everything will work exactly as you have written it originally ;-));
* some little changes to the documentation, see the patch.

I'll now run complete tests including this patch, to make sure there are no surprises in unrelated places, but if you are happy with modifications I am ready to switch it to positive review.



---

archive/issue_comments_087834.json:
```json
{
    "body": "All tests pass, documentation compiles to HTML and PDF.",
    "created_at": "2010-07-28T06:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87834",
    "user": "https://github.com/novoselt"
}
```

All tests pass, documentation compiles to HTML and PDF.



---

archive/issue_events_022980.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2010-07-29T19:38:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9326#event-22980"
}
```



---

archive/issue_events_022981.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2010-07-29T19:38:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9326#event-22981"
}
```



---

archive/issue_comments_087835.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-29T19:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87835",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087836.json:
```json
{
    "body": "Looks good! I'll set \"positive review\" on your behalf ;-)",
    "created_at": "2010-07-29T19:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87836",
    "user": "https://github.com/vbraun"
}
```

Looks good! I'll set "positive review" on your behalf ;-)



---

archive/issue_comments_087837.json:
```json
{
    "body": "Thank you ;-) For the release manager: please merge patches in the following order:\n* trac_9326_QuotientRing_fix_derived_classes.2.patch\n* trac_9326_toric_variety_cohomology.patch\n* trac_9326_Cone_of_toric_variety_cohomology.patch\n* trac_9326_toric_cohomology_reviewer.patch",
    "created_at": "2010-07-29T19:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87837",
    "user": "https://github.com/novoselt"
}
```

Thank you ;-) For the release manager: please merge patches in the following order:
* trac_9326_QuotientRing_fix_derived_classes.2.patch
* trac_9326_toric_variety_cohomology.patch
* trac_9326_Cone_of_toric_variety_cohomology.patch
* trac_9326_toric_cohomology_reviewer.patch



---

archive/issue_comments_087838.json:
```json
{
    "body": "Attachment [trac_9326_QuotientRing_fix_derived_classes.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_QuotientRing_fix_derived_classes.patch) by @vbraun created at 2010-08-08 16:05:02\n\nRefreshed patch for sage-4.5.2",
    "created_at": "2010-08-08T16:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87838",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9326_QuotientRing_fix_derived_classes.patch](tarball://root/attachments/some-uuid/ticket9326/trac_9326_QuotientRing_fix_derived_classes.patch) by @vbraun created at 2010-08-08 16:05:02

Refreshed patch for sage-4.5.2



---

archive/issue_comments_087839.json:
```json
{
    "body": "The first patch collided with some unrelated change in sage-4.5.2. I rediffed it, nothing else changed. Patch order is\n\n* trac_9326_QuotientRing_fix_derived_classes.patch\n* trac_9326_toric_variety_cohomology.patch\n* trac_9326_Cone_of_toric_variety_cohomology.patch\n* trac_9326_toric_cohomology_reviewer.patch",
    "created_at": "2010-08-08T16:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87839",
    "user": "https://github.com/vbraun"
}
```

The first patch collided with some unrelated change in sage-4.5.2. I rediffed it, nothing else changed. Patch order is

* trac_9326_QuotientRing_fix_derived_classes.patch
* trac_9326_toric_variety_cohomology.patch
* trac_9326_Cone_of_toric_variety_cohomology.patch
* trac_9326_toric_cohomology_reviewer.patch



---

archive/issue_comments_087840.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9326#issuecomment-87840",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022982.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:48:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9326#event-22982"
}
```
