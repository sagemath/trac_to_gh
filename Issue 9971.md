# Issue 9971: Add toric lattice morphisms

archive/issues_009971.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @vbraun\n\nThis patch adds classes for toric lattices homspaces and homomorphisms and allows checking fan compatibility and automatic subdivision to achieve this compatibility.\n\nSee #9604 for prerequisites.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9972\n\n",
    "created_at": "2010-09-23T02:05:09Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Add toric lattice morphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9971",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

CC:  @vbraun

This patch adds classes for toric lattices homspaces and homomorphisms and allows checking fan compatibility and automatic subdivision to achieve this compatibility.

See #9604 for prerequisites.

Issue created by migration from https://trac.sagemath.org/ticket/9972





---

archive/issue_comments_099815.json:
```json
{
    "body": "Attachment [trac_9972_add_toric_lattice_morphisms.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_add_toric_lattice_morphisms.patch) by @novoselt created at 2010-09-23 02:19:05\n\nThe patch is in principle ready, but while we are at it - do we want to make custom `_repr_` for such morphisms? If yes, how should they be different from the standard?\n\nAlso, the speed is far from spectacular, but it is not easy to make it better until simple polyhedra work faster - currently most time is spend on constructing them for intersection purposes and I tried hard not to intersect more cones than necessary.",
    "created_at": "2010-09-23T02:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99815",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9972_add_toric_lattice_morphisms.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_add_toric_lattice_morphisms.patch) by @novoselt created at 2010-09-23 02:19:05

The patch is in principle ready, but while we are at it - do we want to make custom `_repr_` for such morphisms? If yes, how should they be different from the standard?

Also, the speed is far from spectacular, but it is not easy to make it better until simple polyhedra work faster - currently most time is spend on constructing them for intersection purposes and I tried hard not to intersect more cones than necessary.



---

archive/issue_comments_099816.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-09-23T02:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99816",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_099817.json:
```json
{
    "body": "I don't have any good suggestion for how to improve `_repr_`, we can always leave that for later. \n\nI'll rewrite the Polyhedron constructor in cython one of these days, that should fix the speed issues. Though its a good idea to minimize the number of intersections computed :)\n\nThe current version looks good for an initial shot at toric morphisms. Are you still changing things around or should I officially review it?",
    "created_at": "2010-09-27T20:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99817",
    "user": "https://github.com/vbraun"
}
```

I don't have any good suggestion for how to improve `_repr_`, we can always leave that for later. 

I'll rewrite the Polyhedron constructor in cython one of these days, that should fix the speed issues. Though its a good idea to minimize the number of intersections computed :)

The current version looks good for an initial shot at toric morphisms. Are you still changing things around or should I officially review it?



---

archive/issue_comments_099818.json:
```json
{
    "body": "I don't plan on changing these functions further, so this ticket is ready for review!",
    "created_at": "2010-09-27T23:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99818",
    "user": "https://github.com/novoselt"
}
```

I don't plan on changing these functions further, so this ticket is ready for review!



---

archive/issue_comments_099819.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-27T23:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99819",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_099820.json:
```json
{
    "body": "I like the functionality, but I'm confused about the name. Is this supposed to be a `ToricLatticeMorphism` or a `FanMorphism`? I am thinking that it would be good to split those apart, and perhaps make the latter inherit from the former. \n\n`ToricLatticeMorphism.make_compatible_with(fan)` doesn't make the morphism compatible with the fan, it is the other way round. So it should be either `fan.make_compatible_with(toric_morphism)` or, say,  `ToricLatticeMorphism.subdivide_domain(domain_fan,codomain_fan)`. Or see below.\n\nAnother functionality that I would like to have is to figure out the image fan from the lattice morphism and the domain. How about the following proposal:\n\n1. separate `ToricLatticeMorphism` and `FanMorphism`.\n\n2. `FanMorphism(lattice_hom, domain=Fan, codomain=Fan)` constructs the fan morphism. If `lattice_hom` is a matrix the corresponding `ToricLatticeMorphism` is constructed automatically. Raises `ValueError` if the fans are not compatible.\n\n3. `FanMorphism(lattice_hom, domain=Fan)` constructs the image fan and uses it as codomain. Raise `ValueError` if not possible.\n\n4. `FanMorphism(lattice_hom, domain=Fan, codomain=Fan, subdivide=True)` will subdivide the domain fan as necessary. \n\nLet me know what you think & I'd be happy to help, of course!",
    "created_at": "2010-10-04T10:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99820",
    "user": "https://github.com/vbraun"
}
```

I like the functionality, but I'm confused about the name. Is this supposed to be a `ToricLatticeMorphism` or a `FanMorphism`? I am thinking that it would be good to split those apart, and perhaps make the latter inherit from the former. 

`ToricLatticeMorphism.make_compatible_with(fan)` doesn't make the morphism compatible with the fan, it is the other way round. So it should be either `fan.make_compatible_with(toric_morphism)` or, say,  `ToricLatticeMorphism.subdivide_domain(domain_fan,codomain_fan)`. Or see below.

Another functionality that I would like to have is to figure out the image fan from the lattice morphism and the domain. How about the following proposal:

1. separate `ToricLatticeMorphism` and `FanMorphism`.

2. `FanMorphism(lattice_hom, domain=Fan, codomain=Fan)` constructs the fan morphism. If `lattice_hom` is a matrix the corresponding `ToricLatticeMorphism` is constructed automatically. Raises `ValueError` if the fans are not compatible.

3. `FanMorphism(lattice_hom, domain=Fan)` constructs the image fan and uses it as codomain. Raise `ValueError` if not possible.

4. `FanMorphism(lattice_hom, domain=Fan, codomain=Fan, subdivide=True)` will subdivide the domain fan as necessary. 

Let me know what you think & I'd be happy to help, of course!



---

archive/issue_comments_099821.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-10-04T16:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99821",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_099822.json:
```json
{
    "body": "I am now putting finishing touches on plotting, but then return back to morphisms.\n\nAfter actually working on morphisms a bit, I had second thoughts about class organization. In particular, I didn't see how `FanMorphism` can fit nicely into Sage and I didn't even understand what it is mathematically. A fan is a collection of cones with certain restrictions, right? Then a fan morphism should be a map between sets of cones, in our case finite. But that's not what we want, we rather want a morphism between supports of fans, which is given on points of the space by a linear map. Put it another way, we want a `ToricLatticeMorphism` restricted to the support of the domain. During construction of such a morphism we have to check that everything is compatible, which can be quite expensive. During any application of this morphism to a point, we should check that this point is in the domain and this is also non-trivial (the only thing that will work for general fans is checking this point against every generating cone). So if we do have a special class for `FanMorphism`, how about this definition: \"it is a morphism between toric lattices with distinguished fans in the domain and codomain which are compatible with this morphism.\" I.e. the domain is still a whole toric lattice and there is no need for complicated checks. One can write then\n\n```\nsage: phi = FanMorphism(lattice_morphism, F1, F2)\nsage: phi.image_cone(cone_of_F1)\n<some cone of F2>\nsage: phi.preimage_cones(cone_of_F2)\n<a tuple of cones of F1>\n```\n\nGoing further, I don't think anymore that we should derive special fans for domain/codomain of morphisms between toric varieties themselves, let's call this class `ToricMorphism`. The problem I have is that a single variety can be a (co)domain of different morphisms. (I definitely need such functionality.) This can make it very inconvenient to work with divisors and classes because they will get confused which parent do they belong to, we will have to work with coercion, and the code may need to look something like this:\n\n```\nsage: fan = ...\nsage: X = ToricVariety(fan)\nsage: fan = X.fan() # This is already a bit strange...\nsage: phi = ToricMorphism(matrix(...), X, Y)\nsage: psi = ToricMorphism(matrix(...), Z, X)\nsage: X_fan_codomain = psi.codomain().fan() # These two lines are plain confusing\nsage: X_fan_domain = phi.domain().fan()\nsage: phi.domain().rational_divisor_group() == psi.codomain().rational_divisor_group()\n???\n```\nAll four fans above are mathematically the same, the only difference is what kind of extra functionality do they get. But they will be different Python objects and associated toric varieties will be also different objects for no apparent reason, i.e. how these reasons can be explained to a user rather than a developer?\n\nSo I think that either morphisms derive their own fans for domain/codomain and use them internally without actually changing the varieties they were created for (i.e. `phi.domain().fan()` is the same as `X.fan()`, but `phi.domain_fan()` can be something specialized), or they store this information in some other way and return (pre)images taking cones of usual fans as arguments.\n\nI recall that we already had a similar argument in the beginning, whether or not we need any kind of specialized cones, which provide clean access to new features. I just checked how many new features got added:\n* TWO methods for `Cone_of_fan`: `star_generators` and `star_generator_indices`. (There were actually many new methods here originally, but others migrated to plain cones.) Still, I think that this class is justified, because these are very natural operations to perform on cones that belong to a fan. Also, a cone cannot quite belong to several fans in the sense that its internal data structures are severely tied to a fan and it is very important performance-wise. (E.g. intersection of cones of the same fan is incomparably easier/faster than for arbitrary ones, and this will remain true even when polyhedra are made fast.)\n* ONE method for `Cone_of_toric_variety`: `cohomology_class`. Here I feel less convinced that it is necessary, `cone.cohomology_class()` does not feel more natural to me than `X.cohomology_class(cone)`. However, I think there are more methods added here by patches which are not applied in my queue and something else may come up during later development. If not, we should probably reconsider this class, because it would be nice to have \n {{{\nsage: ToricVariety(fan).fan() is fan\nTrue\n}}}\n* Hypothetical cones of (co)domain would each add one more method, but make it difficult/inconvenient to deal with multiple morphisms, while the whole point of making new classes should be making life easier...\n\nFor this ticket I propose the following:\n\n1. Rename `make_compatible_with` to `subdivide_domain`.\n2. Add to `ToricLatticeMorphism` a method like `image_fan(domain_fan)` to construct the \"natural\" fan in the codomain, as you have suggested.\n3. Add `FanMorphism(ToricLatticeMorphism)` which mathematically is what I have said above, will live in the same Hom-space as lattice morphisms, and will behave in the same way (including `domain` and `codomain` returning toric lattices), except that it also has `domain_fan` and `codomain_fan` methods returning fans which are guaranteed to be compatible with the morphism. It also has `image_cone` and `preimage_cones`, results are cached (perhaps it is more efficient to compute them at once for all cones or even do it during compatibility check).\n4. Cones of fans also get `image_cone` and `preimage_cones` methods that take as an argument a `FanMorphism` with appropriate fans.\n\nA follow-up ticket will add `ToricMorphism` for arbitrary scheme morphisms between toric varieties and `ToricEquivariantMorphism` for those coming from `FanMorphisms`.\n\nLet me know what you think!",
    "created_at": "2010-10-04T16:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99822",
    "user": "https://github.com/novoselt"
}
```

I am now putting finishing touches on plotting, but then return back to morphisms.

After actually working on morphisms a bit, I had second thoughts about class organization. In particular, I didn't see how `FanMorphism` can fit nicely into Sage and I didn't even understand what it is mathematically. A fan is a collection of cones with certain restrictions, right? Then a fan morphism should be a map between sets of cones, in our case finite. But that's not what we want, we rather want a morphism between supports of fans, which is given on points of the space by a linear map. Put it another way, we want a `ToricLatticeMorphism` restricted to the support of the domain. During construction of such a morphism we have to check that everything is compatible, which can be quite expensive. During any application of this morphism to a point, we should check that this point is in the domain and this is also non-trivial (the only thing that will work for general fans is checking this point against every generating cone). So if we do have a special class for `FanMorphism`, how about this definition: "it is a morphism between toric lattices with distinguished fans in the domain and codomain which are compatible with this morphism." I.e. the domain is still a whole toric lattice and there is no need for complicated checks. One can write then

```
sage: phi = FanMorphism(lattice_morphism, F1, F2)
sage: phi.image_cone(cone_of_F1)
<some cone of F2>
sage: phi.preimage_cones(cone_of_F2)
<a tuple of cones of F1>
```

Going further, I don't think anymore that we should derive special fans for domain/codomain of morphisms between toric varieties themselves, let's call this class `ToricMorphism`. The problem I have is that a single variety can be a (co)domain of different morphisms. (I definitely need such functionality.) This can make it very inconvenient to work with divisors and classes because they will get confused which parent do they belong to, we will have to work with coercion, and the code may need to look something like this:

```
sage: fan = ...
sage: X = ToricVariety(fan)
sage: fan = X.fan() # This is already a bit strange...
sage: phi = ToricMorphism(matrix(...), X, Y)
sage: psi = ToricMorphism(matrix(...), Z, X)
sage: X_fan_codomain = psi.codomain().fan() # These two lines are plain confusing
sage: X_fan_domain = phi.domain().fan()
sage: phi.domain().rational_divisor_group() == psi.codomain().rational_divisor_group()
???
```
All four fans above are mathematically the same, the only difference is what kind of extra functionality do they get. But they will be different Python objects and associated toric varieties will be also different objects for no apparent reason, i.e. how these reasons can be explained to a user rather than a developer?

So I think that either morphisms derive their own fans for domain/codomain and use them internally without actually changing the varieties they were created for (i.e. `phi.domain().fan()` is the same as `X.fan()`, but `phi.domain_fan()` can be something specialized), or they store this information in some other way and return (pre)images taking cones of usual fans as arguments.

I recall that we already had a similar argument in the beginning, whether or not we need any kind of specialized cones, which provide clean access to new features. I just checked how many new features got added:
* TWO methods for `Cone_of_fan`: `star_generators` and `star_generator_indices`. (There were actually many new methods here originally, but others migrated to plain cones.) Still, I think that this class is justified, because these are very natural operations to perform on cones that belong to a fan. Also, a cone cannot quite belong to several fans in the sense that its internal data structures are severely tied to a fan and it is very important performance-wise. (E.g. intersection of cones of the same fan is incomparably easier/faster than for arbitrary ones, and this will remain true even when polyhedra are made fast.)
* ONE method for `Cone_of_toric_variety`: `cohomology_class`. Here I feel less convinced that it is necessary, `cone.cohomology_class()` does not feel more natural to me than `X.cohomology_class(cone)`. However, I think there are more methods added here by patches which are not applied in my queue and something else may come up during later development. If not, we should probably reconsider this class, because it would be nice to have 
 {{{
sage: ToricVariety(fan).fan() is fan
True
}}}
* Hypothetical cones of (co)domain would each add one more method, but make it difficult/inconvenient to deal with multiple morphisms, while the whole point of making new classes should be making life easier...

For this ticket I propose the following:

1. Rename `make_compatible_with` to `subdivide_domain`.
2. Add to `ToricLatticeMorphism` a method like `image_fan(domain_fan)` to construct the "natural" fan in the codomain, as you have suggested.
3. Add `FanMorphism(ToricLatticeMorphism)` which mathematically is what I have said above, will live in the same Hom-space as lattice morphisms, and will behave in the same way (including `domain` and `codomain` returning toric lattices), except that it also has `domain_fan` and `codomain_fan` methods returning fans which are guaranteed to be compatible with the morphism. It also has `image_cone` and `preimage_cones`, results are cached (perhaps it is more efficient to compute them at once for all cones or even do it during compatibility check).
4. Cones of fans also get `image_cone` and `preimage_cones` methods that take as an argument a `FanMorphism` with appropriate fans.

A follow-up ticket will add `ToricMorphism` for arbitrary scheme morphisms between toric varieties and `ToricEquivariantMorphism` for those coming from `FanMorphisms`.

Let me know what you think!



---

archive/issue_comments_099823.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> \"it is a morphism between toric lattices with distinguished fans in the domain and codomain which are compatible with this morphism.\"\n\n\nYes, that is the usual definition. No restriction on the support of the underlying lattice map. \n\nOn an unrelated note, I would call \"point\" = \"0-dimensional torus orbit\" = full-dimensional cone. A toric morphism maps points to potentially higher-dimensional torus orbits. Though I do understand that you meant lattice points.\n\nI understand your issue about having multiple morphisms. But if the fans don't know about the toric morphism then they shouldn't know about the toric variety either, otherwise its confusing. So in principle I don't mind getting rid of the `Cone_of_toric_variety` class. At least this solves the dilemma `cone_of_variety.cohomology_class()` vs. `variety.cohomology_class(cone)`; since the cone doesn't know about the variety only the latter can work. But instead of adding a `cohomology_class` method, I'd rather have the `CohomologyRing` element constructor accept cones:\n\n```\n  sage: HH = X.cohomology_ring()\n  sage: HH( X.fan(2)[23] )\n```\nThis pattern works already for the divisor group and Chow group:\n\n```\nsage: Div = X.divisor_group()\nsage: Div( X.fan(1)[0] )   #  output should have been V(z0)?!?\nV(1-d cone of Rational polyhedral fan in 2-d lattice N)\nsage: A = X.Chow_group()\nsage: A( X.fan(1)[0] )\nThe Chow cycle (1, 0, 0)\n```\n\n> For this ticket I propose the following:\n> 1. Rename `make_compatible_with` to `subdivide_domain`.\n> 2. Add to `ToricLatticeMorphism` a method like `image_fan(domain_fan)` to construct the \"natural\" fan in the codomain, as you have suggested.\n\n\nIf we can agree on a hierarchy `ToricLatticeMorphism` -> `FanMorphism` -> `ToricMorphism` then  `ToricLatticeMorphism` shouldn't know about fans at all, if only to avoid circular imports. Similar to how `ToricLattice` doesn't know about `Fan`. So `make_compatible_with` and `image_fan` become special cases of the `FanMorphism` constructor. \n\nAnd instead of an `is_compatible_with` method, why not have `FanMorphism(matrix,fan1,fan2)` raise `ValueError, \"Cone <3,4,5> is not contained in any image cone\"`.\n\n>  3. Add `FanMorphism(ToricLatticeMorphism)` which mathematically is what I have said above, will live in the same Hom-space as lattice morphisms, and will behave in the same way (including `domain` and `codomain` returning toric lattices), except that it also has `domain_fan` and `codomain_fan` methods returning fans which are guaranteed to be compatible with the morphism. It also has `image_cone` and `preimage_cones`, results are cached (perhaps it is more efficient to compute them at once for all cones or even do it during compatibility check).\n\n\nYes, sounds good!\n\n>  4. Cones of fans also get `image_cone` and `preimage_cones` methods that take as an argument a `FanMorphism` with appropriate fans.\n\n\nI'd rather have only `morphism(cone)` (or `morphism.image(cone)`) and `morphism.preimages(cone)`.\n\n> A follow-up ticket will add `ToricMorphism` for arbitrary scheme morphisms between toric varieties and `ToricEquivariantMorphism` for those coming from `FanMorphisms`.\n\n\nI agree, but can we use, say, `AlgebraicMorphism` and `ToricMorphism`? Toric should really always be replaceable with \"torus-equivariant\".",
    "created_at": "2010-10-04T17:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99823",
    "user": "https://github.com/vbraun"
}
```

Replying to [comment:5 novoselt]:
> "it is a morphism between toric lattices with distinguished fans in the domain and codomain which are compatible with this morphism."


Yes, that is the usual definition. No restriction on the support of the underlying lattice map. 

On an unrelated note, I would call "point" = "0-dimensional torus orbit" = full-dimensional cone. A toric morphism maps points to potentially higher-dimensional torus orbits. Though I do understand that you meant lattice points.

I understand your issue about having multiple morphisms. But if the fans don't know about the toric morphism then they shouldn't know about the toric variety either, otherwise its confusing. So in principle I don't mind getting rid of the `Cone_of_toric_variety` class. At least this solves the dilemma `cone_of_variety.cohomology_class()` vs. `variety.cohomology_class(cone)`; since the cone doesn't know about the variety only the latter can work. But instead of adding a `cohomology_class` method, I'd rather have the `CohomologyRing` element constructor accept cones:

```
  sage: HH = X.cohomology_ring()
  sage: HH( X.fan(2)[23] )
```
This pattern works already for the divisor group and Chow group:

```
sage: Div = X.divisor_group()
sage: Div( X.fan(1)[0] )   #  output should have been V(z0)?!?
V(1-d cone of Rational polyhedral fan in 2-d lattice N)
sage: A = X.Chow_group()
sage: A( X.fan(1)[0] )
The Chow cycle (1, 0, 0)
```

> For this ticket I propose the following:
> 1. Rename `make_compatible_with` to `subdivide_domain`.
> 2. Add to `ToricLatticeMorphism` a method like `image_fan(domain_fan)` to construct the "natural" fan in the codomain, as you have suggested.


If we can agree on a hierarchy `ToricLatticeMorphism` -> `FanMorphism` -> `ToricMorphism` then  `ToricLatticeMorphism` shouldn't know about fans at all, if only to avoid circular imports. Similar to how `ToricLattice` doesn't know about `Fan`. So `make_compatible_with` and `image_fan` become special cases of the `FanMorphism` constructor. 

And instead of an `is_compatible_with` method, why not have `FanMorphism(matrix,fan1,fan2)` raise `ValueError, "Cone <3,4,5> is not contained in any image cone"`.

>  3. Add `FanMorphism(ToricLatticeMorphism)` which mathematically is what I have said above, will live in the same Hom-space as lattice morphisms, and will behave in the same way (including `domain` and `codomain` returning toric lattices), except that it also has `domain_fan` and `codomain_fan` methods returning fans which are guaranteed to be compatible with the morphism. It also has `image_cone` and `preimage_cones`, results are cached (perhaps it is more efficient to compute them at once for all cones or even do it during compatibility check).


Yes, sounds good!

>  4. Cones of fans also get `image_cone` and `preimage_cones` methods that take as an argument a `FanMorphism` with appropriate fans.


I'd rather have only `morphism(cone)` (or `morphism.image(cone)`) and `morphism.preimages(cone)`.

> A follow-up ticket will add `ToricMorphism` for arbitrary scheme morphisms between toric varieties and `ToricEquivariantMorphism` for those coming from `FanMorphisms`.


I agree, but can we use, say, `AlgebraicMorphism` and `ToricMorphism`? Toric should really always be replaceable with "torus-equivariant".



---

archive/issue_comments_099824.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-10-04T18:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99824",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_099825.json:
```json
{
    "body": "OK, I wanted to avoid \"compatibility check by exception\" but I can live with it ;-) How about this:\n\n1. Move `cone.cohomology_class` functionality to the element constructor of cohomology ring (I actually think this is the best and the most clear way there can be.) Can you perhaps make a patch for this change since it involves mostly your code?\n2. Get rid of `Cone_of_toric_variety` (that's my part so I can do this). This raises a question whether `EnhancedCone/Fan` should survive at all. One option is to put `_` in front so that they disappear from the documentation. \n3. Make `FanMorphism` work as you have described, including informative error message.\n4. See if there is then any point in having `ToricLatticeMorphism` at all.\n5. No changes to cones, all (pre)images are computed/stored by morphisms. Which is probably also the cleanest way to do it.\n\nI am also OK with `ToricMorphism` for equivariant ones. I'll see what name should fit nicely with existing classes for affine/projective morphisms for a \"non-toric morphism between toric varieties.\"",
    "created_at": "2010-10-04T18:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99825",
    "user": "https://github.com/novoselt"
}
```

OK, I wanted to avoid "compatibility check by exception" but I can live with it ;-) How about this:

1. Move `cone.cohomology_class` functionality to the element constructor of cohomology ring (I actually think this is the best and the most clear way there can be.) Can you perhaps make a patch for this change since it involves mostly your code?
2. Get rid of `Cone_of_toric_variety` (that's my part so I can do this). This raises a question whether `EnhancedCone/Fan` should survive at all. One option is to put `_` in front so that they disappear from the documentation. 
3. Make `FanMorphism` work as you have described, including informative error message.
4. See if there is then any point in having `ToricLatticeMorphism` at all.
5. No changes to cones, all (pre)images are computed/stored by morphisms. Which is probably also the cleanest way to do it.

I am also OK with `ToricMorphism` for equivariant ones. I'll see what name should fit nicely with existing classes for affine/projective morphisms for a "non-toric morphism between toric varieties."



---

archive/issue_comments_099826.json:
```json
{
    "body": "1. I'll write a patch and post it here for the `cohomology ring` and `divisor_group`. \n\n2. I don't see why we need the `Enhanced*` versions, then.",
    "created_at": "2010-10-04T18:37:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99826",
    "user": "https://github.com/vbraun"
}
```

1. I'll write a patch and post it here for the `cohomology ring` and `divisor_group`. 

2. I don't see why we need the `Enhanced*` versions, then.



---

archive/issue_comments_099827.json:
```json
{
    "body": "I'll also tighten `x in fan` to only return `True` if `x` is actually a `cone`. I'll add another method `fan.support_contains(point)` for the other usage. That'll make it easier to ensure that \"something\" is a cone of the correct fan. Otherwise we have stuff like `0 in fan` return True...",
    "created_at": "2010-10-04T21:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99827",
    "user": "https://github.com/vbraun"
}
```

I'll also tighten `x in fan` to only return `True` if `x` is actually a `cone`. I'll add another method `fan.support_contains(point)` for the other usage. That'll make it easier to ensure that "something" is a cone of the correct fan. Otherwise we have stuff like `0 in fan` return True...



---

archive/issue_comments_099828.json:
```json
{
    "body": "Sounds good!",
    "created_at": "2010-10-05T02:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99828",
    "user": "https://github.com/novoselt"
}
```

Sounds good!



---

archive/issue_comments_099829.json:
```json
{
    "body": "Patch is attached. I removed 'cohomology_class' from `Cone_of_toric_variety` to make sure that I got all occurrences, but tried to make as few other changes in that area as possible. Can you try to put my patch at the bottom of this ticket's queue?\n\nI added an overriding method `Cone_of_fan.is_equivalent` (see the \"TODO\" comment) that you should uncomment after removing the enhanced cones.\n\nThe `CohomologyRing._element_constructor_` now accepts cones as well. For the other issue, you should have complained that `divisor_group` returns the non-toric divisor group and only `toric_divisor_group` should accept cones ;-) The latter already works as it should.",
    "created_at": "2010-10-05T17:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99829",
    "user": "https://github.com/vbraun"
}
```

Patch is attached. I removed 'cohomology_class' from `Cone_of_toric_variety` to make sure that I got all occurrences, but tried to make as few other changes in that area as possible. Can you try to put my patch at the bottom of this ticket's queue?

I added an overriding method `Cone_of_fan.is_equivalent` (see the "TODO" comment) that you should uncomment after removing the enhanced cones.

The `CohomologyRing._element_constructor_` now accepts cones as well. For the other issue, you should have complained that `divisor_group` returns the non-toric divisor group and only `toric_divisor_group` should accept cones ;-) The latter already works as it should.



---

archive/issue_comments_099830.json:
```json
{
    "body": "Regarding `Cone_of_fan.is_equivalent` - cones of fan are also constructed by intersection method and during computing the cone lattice. They can certainly be non-unique now and I don't think that we should try to make them unique. So I propose removal of the overriding method.",
    "created_at": "2010-10-08T01:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99830",
    "user": "https://github.com/novoselt"
}
```

Regarding `Cone_of_fan.is_equivalent` - cones of fan are also constructed by intersection method and during computing the cone lattice. They can certainly be non-unique now and I don't think that we should try to make them unique. So I propose removal of the overriding method.



---

archive/issue_comments_099831.json:
```json
{
    "body": "My thought was that it can be expensive to ensure that two cones of a fan are not the same, and comparing ambient ray indices would be faster. And you always have to go through all cones of the fan to test membership, so it will be called often. I thought about whether that is a problem during the construction, but then I found it easiest to leave that question up to you ;-)\n\nHow about constructing `Cone_of_fan` always though a factory function that tests (via `Cone.is_equivalent`) if the cone is already in the fan. That would be simple to implement and we can then rely on uniqueness of the `Cone_of_fan`.",
    "created_at": "2010-10-08T11:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99831",
    "user": "https://github.com/vbraun"
}
```

My thought was that it can be expensive to ensure that two cones of a fan are not the same, and comparing ambient ray indices would be faster. And you always have to go through all cones of the fan to test membership, so it will be called often. I thought about whether that is a problem during the construction, but then I found it easiest to leave that question up to you ;-)

How about constructing `Cone_of_fan` always though a factory function that tests (via `Cone.is_equivalent`) if the cone is already in the fan. That would be simple to implement and we can then rely on uniqueness of the `Cone_of_fan`.



---

archive/issue_comments_099832.json:
```json
{
    "body": "What membership exactly do you want to test?\n\nThe assumption is that there are no invalid cones of the fan, so if you want \nto check if a cone is in the fan, it is enough to check if the ambient fan of the cone is the fan in question. For checking equivalence of two cones of the same fan it is enough indeed to check that their ambient ray indices are the same, as tuples, since they are always assumed to be sorted and when they are not - it is a bug.\n\nI don't mind adding uniqueness of cones of fan or even cones themselves for that matter (on a separate ticket, perhaps?), I just don't quite understand why do you want it. The advantages that I see are\n* memory saving;\n* cached data sharing;\nand disadvantages\n* more complicated code for construction;\n* longer time for construction.\nDo you have something else in mind?",
    "created_at": "2010-10-08T14:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99832",
    "user": "https://github.com/novoselt"
}
```

What membership exactly do you want to test?

The assumption is that there are no invalid cones of the fan, so if you want 
to check if a cone is in the fan, it is enough to check if the ambient fan of the cone is the fan in question. For checking equivalence of two cones of the same fan it is enough indeed to check that their ambient ray indices are the same, as tuples, since they are always assumed to be sorted and when they are not - it is a bug.

I don't mind adding uniqueness of cones of fan or even cones themselves for that matter (on a separate ticket, perhaps?), I just don't quite understand why do you want it. The advantages that I see are
* memory saving;
* cached data sharing;
and disadvantages
* more complicated code for construction;
* longer time for construction.
Do you have something else in mind?



---

archive/issue_comments_099833.json:
```json
{
    "body": "Some more thoughts:\n1. When there is an attempt to check if a point is in the fan, should we try to interpret this point as a ray, i.e. 1-d cone?\n2. The last line of `_contains` should be replaced with the original version:\n {{{\ntry: \n    return data.is_equivalent(self.cone_containing(data.rays())) \nexcept ValueError:  # No cone containing all these rays \n    return False \n}}}\n For example, if you take a fan which is a subdivision of a cone, then this cone will trickle  down to this block, but `cone_containing` will raise an exception. There probably should be a test for such a situation (although I certainly don't claim that all other places test all possible exceptions...)\n3. `Fan.contains` should no longer accept many arguments after your change - let's replace `*arg` with `cone`.\n4. Typo: \"or a something\" should be without \"a\".\n5. Typo: \"class associated to cones\" should be \"classes\".\n\nOtherwise looks great: the new approach allows users to create their own shortcuts and write `HH(cone)` instead of `cone.cohomology_class()`. While I like names exposed in Sage to be descriptive, I certainly don't want to force users do it in their code ;-)\n\nI will base other patches of the ticket on top of this one.",
    "created_at": "2010-10-08T15:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99833",
    "user": "https://github.com/novoselt"
}
```

Some more thoughts:
1. When there is an attempt to check if a point is in the fan, should we try to interpret this point as a ray, i.e. 1-d cone?
2. The last line of `_contains` should be replaced with the original version:
 {{{
try: 
    return data.is_equivalent(self.cone_containing(data.rays())) 
except ValueError:  # No cone containing all these rays 
    return False 
}}}
 For example, if you take a fan which is a subdivision of a cone, then this cone will trickle  down to this block, but `cone_containing` will raise an exception. There probably should be a test for such a situation (although I certainly don't claim that all other places test all possible exceptions...)
3. `Fan.contains` should no longer accept many arguments after your change - let's replace `*arg` with `cone`.
4. Typo: "or a something" should be without "a".
5. Typo: "class associated to cones" should be "classes".

Otherwise looks great: the new approach allows users to create their own shortcuts and write `HH(cone)` instead of `cone.cohomology_class()`. While I like names exposed in Sage to be descriptive, I certainly don't want to force users do it in their code ;-)

I will base other patches of the ticket on top of this one.



---

archive/issue_comments_099834.json:
```json
{
    "body": "A fan is a collection of cones. A point is never in a fan, as it is not a cone. I don't think we should make cones unique in general, only cones of a fan. You can have arbitrarily many cones (memory permitting), but the cones of a fan are a finite set; To me it then feels right to have the `Cone_of_fan` be unique. In the current implementation they actually are unique after the fan is constructed. So it ends up being a minor change to guarantee that they are always unique, I think.",
    "created_at": "2010-10-08T17:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99834",
    "user": "https://github.com/vbraun"
}
```

A fan is a collection of cones. A point is never in a fan, as it is not a cone. I don't think we should make cones unique in general, only cones of a fan. You can have arbitrarily many cones (memory permitting), but the cones of a fan are a finite set; To me it then feels right to have the `Cone_of_fan` be unique. In the current implementation they actually are unique after the fan is constructed. So it ends up being a minor change to guarantee that they are always unique, I think.



---

archive/issue_comments_099835.json:
```json
{
    "body": "One potential danger is that `cone.ambient_ray_indices()` is meaningless if `cone` is only mathematically equivalent to a fan, but not a `Cone_of_fan`. I've added a new method `RationalPolyhedralFan.get_cone(cone)` that finds the `Cone_of_fan` corresponding to the cone, and I tried to make sure it gets called wherever we accept arbitrary cones from the user. \n\nBut its a potential pitfall to watch out for. We could always insist on the user passing only `Cone_of_fan`, but that seems to be too unwieldy for the user. I would suggest that we move the `ambient_ray_indices()` accessor method to `Cone_of_fan` and convert the code in `cone.py`, `fan.py` to use the data member `_ambient_ray_indices` instead. All higher level functions then shall only use `cone.ambient_ray_indices()`, converting a generic cone to a `Cone_of_fan` via `fan.get_cone(cone)` if necessary.",
    "created_at": "2010-10-08T18:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99835",
    "user": "https://github.com/vbraun"
}
```

One potential danger is that `cone.ambient_ray_indices()` is meaningless if `cone` is only mathematically equivalent to a fan, but not a `Cone_of_fan`. I've added a new method `RationalPolyhedralFan.get_cone(cone)` that finds the `Cone_of_fan` corresponding to the cone, and I tried to make sure it gets called wherever we accept arbitrary cones from the user. 

But its a potential pitfall to watch out for. We could always insist on the user passing only `Cone_of_fan`, but that seems to be too unwieldy for the user. I would suggest that we move the `ambient_ray_indices()` accessor method to `Cone_of_fan` and convert the code in `cone.py`, `fan.py` to use the data member `_ambient_ray_indices` instead. All higher level functions then shall only use `cone.ambient_ray_indices()`, converting a generic cone to a `Cone_of_fan` via `fan.get_cone(cone)` if necessary.



---

archive/issue_comments_099836.json:
```json
{
    "body": "Attachment [trac_9972_improve_element_constructors.2.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_improve_element_constructors.2.patch) by @vbraun created at 2010-10-08 18:57:58\n\nUpdated patch",
    "created_at": "2010-10-08T18:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99836",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9972_improve_element_constructors.2.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_improve_element_constructors.2.patch) by @vbraun created at 2010-10-08 18:57:58

Updated patch



---

archive/issue_comments_099837.json:
```json
{
    "body": "In what sense `ambient_ray_indices` is dangerous? If ambient structures of two cones are different, there is no point to look at these attributes at all. Otherwise they are the same if and only if cones are the same.\n\nI am definitely against moving `ambient_ray_indices` to `Cone_of_fan` because the point in having it is uniform treatment of faces of cones and cones of fans, which are pretty much the same things. In fact, even `star_generators` make sense for faces of a cone in the sense of containing facets, it just should not be called that name. So currently the main reason for a `Cone_of_fan` to exist is that terminology for faces of cones and cones of fans is a bit different. I think that it should stay this way as much as possible, so that all cones behave the same.\n\nI am also against new containment check - cones are equal if they have the same rays in the same order and equivalent if they define the same set of points. If the same cone happened to belong to different fans and so has two objects representing it, it does not change anything. We can check if cones belong to the same ambient structure for code optimization, but the output should be the same. Note that in this case this check actually can be done in generic cones and there is no need to override the method for `Cone_of_fan`.\n\nI still don't understand exactly what are you trying to achieve in general and in particular why do we need `get_cone` method. I agree that `fan.contains` should return `True` only for (some) cones and not for anything else, because a fan is a collection of cones. I agree that it may be good to have uniqueness of `Cone_of_fan` but I don't see any reasons for doing this except for some performance gain and it is not clear how significant it can be. It also seems to me that it makes more sense to make all cones unique based on the ordered rays and the ambient structure, because essentially this is how cones of fans can be made unique.",
    "created_at": "2010-10-08T20:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99837",
    "user": "https://github.com/novoselt"
}
```

In what sense `ambient_ray_indices` is dangerous? If ambient structures of two cones are different, there is no point to look at these attributes at all. Otherwise they are the same if and only if cones are the same.

I am definitely against moving `ambient_ray_indices` to `Cone_of_fan` because the point in having it is uniform treatment of faces of cones and cones of fans, which are pretty much the same things. In fact, even `star_generators` make sense for faces of a cone in the sense of containing facets, it just should not be called that name. So currently the main reason for a `Cone_of_fan` to exist is that terminology for faces of cones and cones of fans is a bit different. I think that it should stay this way as much as possible, so that all cones behave the same.

I am also against new containment check - cones are equal if they have the same rays in the same order and equivalent if they define the same set of points. If the same cone happened to belong to different fans and so has two objects representing it, it does not change anything. We can check if cones belong to the same ambient structure for code optimization, but the output should be the same. Note that in this case this check actually can be done in generic cones and there is no need to override the method for `Cone_of_fan`.

I still don't understand exactly what are you trying to achieve in general and in particular why do we need `get_cone` method. I agree that `fan.contains` should return `True` only for (some) cones and not for anything else, because a fan is a collection of cones. I agree that it may be good to have uniqueness of `Cone_of_fan` but I don't see any reasons for doing this except for some performance gain and it is not clear how significant it can be. It also seems to me that it makes more sense to make all cones unique based on the ordered rays and the ambient structure, because essentially this is how cones of fans can be made unique.



---

archive/issue_comments_099838.json:
```json
{
    "body": "So for `is_equivalent` optimization I propose inserting\n\n```\n        if self == other:\n            return True\n        if self.ambient() == other.ambient():\n            return self.ambient_ray_indices() == other.ambient_ray_indices()\n```\nin the beginning of `Cone.is_equivalent`. Maybe with `==` replaced with `is` in the `if` statements - both variants will work correctly, the question is how many simple but potentially non-informative checks we want to perform before using a generic algorithm.",
    "created_at": "2010-10-08T20:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99838",
    "user": "https://github.com/novoselt"
}
```

So for `is_equivalent` optimization I propose inserting

```
        if self == other:
            return True
        if self.ambient() == other.ambient():
            return self.ambient_ray_indices() == other.ambient_ray_indices()
```
in the beginning of `Cone.is_equivalent`. Maybe with `==` replaced with `is` in the `if` statements - both variants will work correctly, the question is how many simple but potentially non-informative checks we want to perform before using a generic algorithm.



---

archive/issue_comments_099839.json:
```json
{
    "body": "Replying to [comment:19 novoselt]:\n> In what sense ambient_ray_indices is dangerous? If ambient structures of two cones are different, there is no point to look at these attributes at all.\n\n\nThats of course true, but we got that wrong in the `ToricDivisor` constructor (no check that the ambient was the same) and you didn't catch it ;-)\n\nI'm just trying to explore options that make it impossible to make this mistake in the future. One more idea would be to force the user to pass the ambient to `ambient_ray_indices()`,\n\n```\nsage: fan1 = ...\nsage: fan2 = ...\nsage: fan1.generating_cone(2).ambient_ray_indices(fan1)   # fast\nsage: fan1.generating_cone(2).ambient_ray_indices(fan2)   # slower\n```\nThis would also get rid of the need for `get_cone()`\n\nThe point of the `get_cone` method is to avoid this extra branch whenever the user passes a cone that is not necessarilly within the same ambient:\n\n```\n    if is_Cone(c):\n        if c.ambient()==fan\n            indices = c.ambient_ray_indices()\n        else:\n            try:\n                indices = tuple(sorted([ fan.rays().index(r) for r in c.rays() ]))\n            except ValueError:\n                ...\n```\nand instead just write \n\n```\n    if is_Cone(c):\n        indices = fan.get_cone(c).ambient_ray_indices()\n```",
    "created_at": "2010-10-09T14:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99839",
    "user": "https://github.com/vbraun"
}
```

Replying to [comment:19 novoselt]:
> In what sense ambient_ray_indices is dangerous? If ambient structures of two cones are different, there is no point to look at these attributes at all.


Thats of course true, but we got that wrong in the `ToricDivisor` constructor (no check that the ambient was the same) and you didn't catch it ;-)

I'm just trying to explore options that make it impossible to make this mistake in the future. One more idea would be to force the user to pass the ambient to `ambient_ray_indices()`,

```
sage: fan1 = ...
sage: fan2 = ...
sage: fan1.generating_cone(2).ambient_ray_indices(fan1)   # fast
sage: fan1.generating_cone(2).ambient_ray_indices(fan2)   # slower
```
This would also get rid of the need for `get_cone()`

The point of the `get_cone` method is to avoid this extra branch whenever the user passes a cone that is not necessarilly within the same ambient:

```
    if is_Cone(c):
        if c.ambient()==fan
            indices = c.ambient_ray_indices()
        else:
            try:
                indices = tuple(sorted([ fan.rays().index(r) for r in c.rays() ]))
            except ValueError:
                ...
```
and instead just write 

```
    if is_Cone(c):
        indices = fan.get_cone(c).ambient_ray_indices()
```



---

archive/issue_comments_099840.json:
```json
{
    "body": "Aha, now I see! I really don't like the idea of forced arguments to `ambiet_ray_indices` and `get_cone` seems to be a confusing name. How about this:\n1. Implement `get_cone` functionality using `__call__` for fans and cones, i.e. you will have to write `fan(c).ambient_ray_indices()` to make sure that indices are correct. The same goes for other relative things like face walking methonds - in all cases it is assumed that your cone knows where does it sit. This goes very well with the concept of fans being collections of cones - you \"convert\" a certain cone to an element of this collection. For cones it is not as transparent but still makes perfect sense, IMHO.\n2. In principle, I don't terribly mind adding *optional* argument so that one can write `c.ambient_ray_indices(fan)` and internally it will be translated to `fan(self).ambient_ray_indices()`. However, I then want to have it for all functions where it does make sense, it will add the same piece of code and documentation to all of them, and in the user code it does not lead to any significant clarification or space saving. So I'd rather not add such functionality and you don't usually like having two different ways to do the same thing ;-)\n3. Leave equivalence and containment checks mathematical, i.e. it is possible to get `True` for a check that a cone of one fan is \"in\" another fan. Those who want to check if it is an actual element of the collection should use `cone.ambient() is fan`.\n\nIf you agree with these proposals, then I can start implementing them and uniqueness of cones (and then fans too for uniformity, I guess) working on top of your patch.",
    "created_at": "2010-10-09T14:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99840",
    "user": "https://github.com/novoselt"
}
```

Aha, now I see! I really don't like the idea of forced arguments to `ambiet_ray_indices` and `get_cone` seems to be a confusing name. How about this:
1. Implement `get_cone` functionality using `__call__` for fans and cones, i.e. you will have to write `fan(c).ambient_ray_indices()` to make sure that indices are correct. The same goes for other relative things like face walking methonds - in all cases it is assumed that your cone knows where does it sit. This goes very well with the concept of fans being collections of cones - you "convert" a certain cone to an element of this collection. For cones it is not as transparent but still makes perfect sense, IMHO.
2. In principle, I don't terribly mind adding *optional* argument so that one can write `c.ambient_ray_indices(fan)` and internally it will be translated to `fan(self).ambient_ray_indices()`. However, I then want to have it for all functions where it does make sense, it will add the same piece of code and documentation to all of them, and in the user code it does not lead to any significant clarification or space saving. So I'd rather not add such functionality and you don't usually like having two different ways to do the same thing ;-)
3. Leave equivalence and containment checks mathematical, i.e. it is possible to get `True` for a check that a cone of one fan is "in" another fan. Those who want to check if it is an actual element of the collection should use `cone.ambient() is fan`.

If you agree with these proposals, then I can start implementing them and uniqueness of cones (and then fans too for uniformity, I guess) working on top of your patch.



---

archive/issue_comments_099841.json:
```json
{
    "body": "Adding the functionality to `__call__` still does not enforce that `ambient_ray_indices` is used correctly. In particular, it would not have caught the bug in `ToricDivisor`.\n\nHow about we remove the `ambient_ray_indices()` method from cones altogether and replace it with `fan.ray_indices(cone)`. \n\nI agree with 3.\n\nI don't think that the `Cone_of_fan` uniqueness is particularly urgent, we can come back to that later.",
    "created_at": "2010-10-09T15:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99841",
    "user": "https://github.com/vbraun"
}
```

Adding the functionality to `__call__` still does not enforce that `ambient_ray_indices` is used correctly. In particular, it would not have caught the bug in `ToricDivisor`.

How about we remove the `ambient_ray_indices()` method from cones altogether and replace it with `fan.ray_indices(cone)`. 

I agree with 3.

I don't think that the `Cone_of_fan` uniqueness is particularly urgent, we can come back to that later.



---

archive/issue_comments_099842.json:
```json
{
    "body": "It is not quite Python style to try to eliminate any possibility of user mistakes by making sure that everything is called properly in proper places. The assumption is that users know what they are doing ;-) These methods assume that your cone is in some fixed fan:\n* `adjacent`\n* `ambient_ray_indices`\n* `face_lattice` (indirectly - since elements will be cones of the same fan)\n* `faces` (indirectly)\n* `facet_of`\n* `facets` (indirectly)\n* `star_generator_indices`\n* `star_generators`\nAll of these methods are pretty important and convenient, in particular, in many cases `ambient_ray_indices` is more useful than `rays` or `ray_matrix` since it allows you to see clearly how different cones are related to each other. It would be quite annoying if for using all these methods it was necessary to mention fan explicitly.\n\nYes, there are bugs that appear because users make wrong assumptions, but I don't think that it is a valid reason to require users to always explicitly state all of their assumptions so that each function can check that they are correct and when possible fix them.\n\nIn addition, as you pointed out in a sample code above, passing ambient explicitly will mean that it always works correctly, but sometimes fast and sometimes slow. This sometimes slow can be sometimes significantly slow and the reason for keeping track of these ray indices and ambients is precisely code optimization, otherwise all cones could store only their rays and all fans - only their cones.\n\nSo I still think that if you have a cone and it is important that things about this cone are computed relevant to a certain fan, you are responsible for making sure that this cone \"sits\" in this fan and if not - trying to convert it there. I see a point in making this conversion easy, but not in making it mandatory every time you need it. Compare this\n\n```\nsage: indices = fan.ray_indices(cone)\nsage: supercones = fan.cones_with_facet(cone)\n```\nand this\n\n```\nsage: indices = fan(cone).ambient_ray_incides()\nsage: supercones = fan(cone).facet_of()\n```\nI think in the second case it is quite clear that\n\n```\nsage: cone = fan(cone)\nsage: indices = cone.ambient_ray_incides()\nsage: supercones = cone.facet_of()\n```\nis likely to be faster, plus it is a bit easier to read and there is only one place where an exception can occur due to `cone` being incompatible with `fan` at all.\n\nI also think that using cones from a wrong fan is likely to be exposed very quickly in actual work due to index-out-of range exceptions, so given several month of working with current interface, I really don't want it to change...",
    "created_at": "2010-10-09T16:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99842",
    "user": "https://github.com/novoselt"
}
```

It is not quite Python style to try to eliminate any possibility of user mistakes by making sure that everything is called properly in proper places. The assumption is that users know what they are doing ;-) These methods assume that your cone is in some fixed fan:
* `adjacent`
* `ambient_ray_indices`
* `face_lattice` (indirectly - since elements will be cones of the same fan)
* `faces` (indirectly)
* `facet_of`
* `facets` (indirectly)
* `star_generator_indices`
* `star_generators`
All of these methods are pretty important and convenient, in particular, in many cases `ambient_ray_indices` is more useful than `rays` or `ray_matrix` since it allows you to see clearly how different cones are related to each other. It would be quite annoying if for using all these methods it was necessary to mention fan explicitly.

Yes, there are bugs that appear because users make wrong assumptions, but I don't think that it is a valid reason to require users to always explicitly state all of their assumptions so that each function can check that they are correct and when possible fix them.

In addition, as you pointed out in a sample code above, passing ambient explicitly will mean that it always works correctly, but sometimes fast and sometimes slow. This sometimes slow can be sometimes significantly slow and the reason for keeping track of these ray indices and ambients is precisely code optimization, otherwise all cones could store only their rays and all fans - only their cones.

So I still think that if you have a cone and it is important that things about this cone are computed relevant to a certain fan, you are responsible for making sure that this cone "sits" in this fan and if not - trying to convert it there. I see a point in making this conversion easy, but not in making it mandatory every time you need it. Compare this

```
sage: indices = fan.ray_indices(cone)
sage: supercones = fan.cones_with_facet(cone)
```
and this

```
sage: indices = fan(cone).ambient_ray_incides()
sage: supercones = fan(cone).facet_of()
```
I think in the second case it is quite clear that

```
sage: cone = fan(cone)
sage: indices = cone.ambient_ray_incides()
sage: supercones = cone.facet_of()
```
is likely to be faster, plus it is a bit easier to read and there is only one place where an exception can occur due to `cone` being incompatible with `fan` at all.

I also think that using cones from a wrong fan is likely to be exposed very quickly in actual work due to index-out-of range exceptions, so given several month of working with current interface, I really don't want it to change...



---

archive/issue_comments_099843.json:
```json
{
    "body": "Well `face_lattice`, `faces`, `facet_of`, and `facets` should return mathematically equivalent results if the cone is in the wrong ambient, so they don't count.  For `adjacent` and `star_generators` I would tend to let your argument pass that the output would be so wildly wrong that it is immediately obvious. But `ambient_ray_indices` of a `Cone` always returns valid index ranges (namely, `range(0,cone.nrays())`). \n\nSo I do maintain that this method is particularly dangerous. Note that I don't want to get rid of the `_ambient_ray_indices` data member, just \n\n```\ndef ray_indices(self, cone):\n    if self is cone.ambient():\n        return cone._ambient_ray_indices\n    # slow fallback\n```",
    "created_at": "2010-10-09T18:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99843",
    "user": "https://github.com/vbraun"
}
```

Well `face_lattice`, `faces`, `facet_of`, and `facets` should return mathematically equivalent results if the cone is in the wrong ambient, so they don't count.  For `adjacent` and `star_generators` I would tend to let your argument pass that the output would be so wildly wrong that it is immediately obvious. But `ambient_ray_indices` of a `Cone` always returns valid index ranges (namely, `range(0,cone.nrays())`). 

So I do maintain that this method is particularly dangerous. Note that I don't want to get rid of the `_ambient_ray_indices` data member, just 

```
def ray_indices(self, cone):
    if self is cone.ambient():
        return cone._ambient_ray_indices
    # slow fallback
```



---

archive/issue_comments_099844.json:
```json
{
    "body": "Well, if you just want to add `fan.ray_indices(cone)` method (which can be potentially slow), I am OK with it, although I'd rather not ;-) But I really want to keep `cone.ambient_ray_indices()` as is without any arguments, especially forced ones.\n\nAnd I still think that the best way is to explicitly convert input cones to cones of a particular fan and then freely use any fan-dependent methods. Given the current size of toric code it does not seem to me that we have any particularly dangerous methods (the most dangerous are `check=False` and `normalize=False` options, which are described as dangerous). So maybe instead of changing code we can put a warning in the documentation that this method may be dangerous and one should ensure that `cone.ambient()` is what it should be before calling this method. It seems to me that it is quite difficult to start using `ambient_ray_indices` without reading its documentation at least once.",
    "created_at": "2010-10-09T19:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99844",
    "user": "https://github.com/novoselt"
}
```

Well, if you just want to add `fan.ray_indices(cone)` method (which can be potentially slow), I am OK with it, although I'd rather not ;-) But I really want to keep `cone.ambient_ray_indices()` as is without any arguments, especially forced ones.

And I still think that the best way is to explicitly convert input cones to cones of a particular fan and then freely use any fan-dependent methods. Given the current size of toric code it does not seem to me that we have any particularly dangerous methods (the most dangerous are `check=False` and `normalize=False` options, which are described as dangerous). So maybe instead of changing code we can put a warning in the documentation that this method may be dangerous and one should ensure that `cone.ambient()` is what it should be before calling this method. It seems to me that it is quite difficult to start using `ambient_ray_indices` without reading its documentation at least once.



---

archive/issue_comments_099845.json:
```json
{
    "body": "I agree that the best way is to first convert the input cone to the fan and then work with that. \n\nBut 1) its easy to accidentally omit that step and 2) it is very hard to detect that you got it wrong. In my book, thats a very dangerous API design. I don't think a warning in the documentation is sufficient here, after all, we should have known better yet we fell into that trap with `ToricDivisor`. \n\nAt the very least `ambient_ray_indices()` should spit out a warning if `self==self.ambient()` [what ARE you trying to do?]. But the best option seems to me to be the `fan.ray_indices(cone)` method. If you wrote your code correctly there won't be any slowdown, and if you forgot to convert the cone to a cone of the fan then you'll still get the right answer. Ideally we'd then make `ambient_ray_indices` private not use it outside of `cone.py`/`fan.py` (and fan morphisms).",
    "created_at": "2010-10-09T20:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99845",
    "user": "https://github.com/vbraun"
}
```

I agree that the best way is to first convert the input cone to the fan and then work with that. 

But 1) its easy to accidentally omit that step and 2) it is very hard to detect that you got it wrong. In my book, thats a very dangerous API design. I don't think a warning in the documentation is sufficient here, after all, we should have known better yet we fell into that trap with `ToricDivisor`. 

At the very least `ambient_ray_indices()` should spit out a warning if `self==self.ambient()` [what ARE you trying to do?]. But the best option seems to me to be the `fan.ray_indices(cone)` method. If you wrote your code correctly there won't be any slowdown, and if you forgot to convert the cone to a cone of the fan then you'll still get the right answer. Ideally we'd then make `ambient_ray_indices` private not use it outside of `cone.py`/`fan.py` (and fan morphisms).



---

archive/issue_comments_099846.json:
```json
{
    "body": "After some more contemplating and checking\n\n```\n$ grep \"ambient_ray_indices()\" sage/geometry/* |wc\n     30     179    2579\n$ grep \"ambient_ray_indices()\" sage/schemes/generic/* |wc\n     13      85    1383\n```\non Sage-4.6.alpha3, I think that you may be a bit overestimating the danger. We have used this function in 43 places and so far everything is working quite well. The \"mistake\" you ran into got quickly caught even before the ticket got ready for a review. Also, *why* did you get this mistake? Because you took a code from a place where the ambient definitely was set correctly and moved it to the place where potentially other cones maybe passed in. Finally, *you* actually have not done any mistake, you just left a possibility for a user to make one by passing a wrong cone. (In this case, I think, the mistake would be realized quite fast even if the code did not throw up an exception.)\n\nAdding a warning for calling `ambient_ray_indices` on the ambient itself may not work because it may be called internally in some cycles. (I didn't check but it is quite likely.) Besides, nothing is wrong with such a call. I also strongly believe that this method must be open/documented/public, because if we have used it in 43 places, it is quite important for development and therefore users who build their own structures on top of stuff shipped in Sage are likely to find it convenient in their code. I personally use it all the time when working with varieties and sometimes even regret that these indices are not the default output for cones, so when I have a list of them I need to write a cycle calling this method.\n\nA few months ago I already suggested switching to notation like `fan.ray_indices(cone)` etc. but you opposed and pointed out that it is not in the spirit of OOP. Now I actually completely agree and think that it is very fortunate that we have not done so then. I even still see some benefits of having special classes for cones of toric varieties and morphisms (in particular, this problem would not occur ;-)) but for these cases the disadvantages overweight.\n\nHave I convinced you yet or should I abandon any hope?-)",
    "created_at": "2010-10-10T03:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99846",
    "user": "https://github.com/novoselt"
}
```

After some more contemplating and checking

```
$ grep "ambient_ray_indices()" sage/geometry/* |wc
     30     179    2579
$ grep "ambient_ray_indices()" sage/schemes/generic/* |wc
     13      85    1383
```
on Sage-4.6.alpha3, I think that you may be a bit overestimating the danger. We have used this function in 43 places and so far everything is working quite well. The "mistake" you ran into got quickly caught even before the ticket got ready for a review. Also, *why* did you get this mistake? Because you took a code from a place where the ambient definitely was set correctly and moved it to the place where potentially other cones maybe passed in. Finally, *you* actually have not done any mistake, you just left a possibility for a user to make one by passing a wrong cone. (In this case, I think, the mistake would be realized quite fast even if the code did not throw up an exception.)

Adding a warning for calling `ambient_ray_indices` on the ambient itself may not work because it may be called internally in some cycles. (I didn't check but it is quite likely.) Besides, nothing is wrong with such a call. I also strongly believe that this method must be open/documented/public, because if we have used it in 43 places, it is quite important for development and therefore users who build their own structures on top of stuff shipped in Sage are likely to find it convenient in their code. I personally use it all the time when working with varieties and sometimes even regret that these indices are not the default output for cones, so when I have a list of them I need to write a cycle calling this method.

A few months ago I already suggested switching to notation like `fan.ray_indices(cone)` etc. but you opposed and pointed out that it is not in the spirit of OOP. Now I actually completely agree and think that it is very fortunate that we have not done so then. I even still see some benefits of having special classes for cones of toric varieties and morphisms (in particular, this problem would not occur ;-)) but for these cases the disadvantages overweight.

Have I convinced you yet or should I abandon any hope?-)



---

archive/issue_comments_099847.json:
```json
{
    "body": "I had counted the occurrences of `ambient_ray_lattice` as well, but my conclusion was that it is seldomly used outside of `/sage/geometry/cone,fan.py`. Replacing the 13 occurrences wouldn't be hard. The fact that copy/pasting \"correct\" code turns it so easily into \"incorrect\" code is precisely what I find disturbing. Also, the mistake in `ToricDivisor` was not caught easily. It is in the current release. And saying that its the user's fault (\"You are holding it wrong\" :-) is not helpful.",
    "created_at": "2010-10-10T10:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99847",
    "user": "https://github.com/vbraun"
}
```

I had counted the occurrences of `ambient_ray_lattice` as well, but my conclusion was that it is seldomly used outside of `/sage/geometry/cone,fan.py`. Replacing the 13 occurrences wouldn't be hard. The fact that copy/pasting "correct" code turns it so easily into "incorrect" code is precisely what I find disturbing. Also, the mistake in `ToricDivisor` was not caught easily. It is in the current release. And saying that its the user's fault ("You are holding it wrong" :-) is not helpful.



---

archive/issue_comments_099848.json:
```json
{
    "body": "I meant that mistake would be realized quite fast once the code was actually used. I didn't actually use code for toric divisors yet, especially with cones from another fan. But anyway - this is all hypothetical and I may be very wrong.\n\nMy main point is not that it is difficult to replace 13 uses of `ambient_ray_indices`, but that it is a very convenient and natural function which I personally use both when developing new code and when actually using Sage interactively. I would rather not pass any arguments to it, because it is annoying for interaction and in functions it may lead to code like\n\n```\ncone.ambient_ray_indices(cone.ambient())\n```\nor\n\n```\ncone.ambient().ray_indices(cone)\n```\nwhich is plain confusing.\n\nThe name of the function clearly indicates that there is something ambient and cone must be aware of it, since no arguments were passed. Therefore, when using this function, the user should be sure that this something ambient is what it is supposed to be. In fact, it may be more clear for new outside users than for us, since we are used to writing code inside the class where in many cases this requirement is definitely satisfied. (How can `self` have a wrong `self.ambient()`???) And after all this discussion I will probably remember very well for a long time to make an extra check that this function is used after making sure that ambient is what it is assumed to be.\n\nIf you want to add extra functionality like `fan.ray_indices(cone)` which will be safer to use and then use this one when you want - I am fine with it. But if you insist on getting rid of `cone.ambient_ray_indices()` in its present form/namespace, we need to invite more people from sage-devel for opinions...",
    "created_at": "2010-10-10T14:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99848",
    "user": "https://github.com/novoselt"
}
```

I meant that mistake would be realized quite fast once the code was actually used. I didn't actually use code for toric divisors yet, especially with cones from another fan. But anyway - this is all hypothetical and I may be very wrong.

My main point is not that it is difficult to replace 13 uses of `ambient_ray_indices`, but that it is a very convenient and natural function which I personally use both when developing new code and when actually using Sage interactively. I would rather not pass any arguments to it, because it is annoying for interaction and in functions it may lead to code like

```
cone.ambient_ray_indices(cone.ambient())
```
or

```
cone.ambient().ray_indices(cone)
```
which is plain confusing.

The name of the function clearly indicates that there is something ambient and cone must be aware of it, since no arguments were passed. Therefore, when using this function, the user should be sure that this something ambient is what it is supposed to be. In fact, it may be more clear for new outside users than for us, since we are used to writing code inside the class where in many cases this requirement is definitely satisfied. (How can `self` have a wrong `self.ambient()`???) And after all this discussion I will probably remember very well for a long time to make an extra check that this function is used after making sure that ambient is what it is assumed to be.

If you want to add extra functionality like `fan.ray_indices(cone)` which will be safer to use and then use this one when you want - I am fine with it. But if you insist on getting rid of `cone.ambient_ray_indices()` in its present form/namespace, we need to invite more people from sage-devel for opinions...



---

archive/issue_comments_099849.json:
```json
{
    "body": "By the way, in schemes `ambient_ray_indices` is used several times in the examples and it was also used in Hal's examples for their book. It is very-very natural and should be as easy to access as possible...",
    "created_at": "2010-10-10T14:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99849",
    "user": "https://github.com/novoselt"
}
```

By the way, in schemes `ambient_ray_indices` is used several times in the examples and it was also used in Hal's examples for their book. It is very-very natural and should be as easy to access as possible...



---

archive/issue_comments_099850.json:
```json
{
    "body": "`ambient_ray_indices` is not natural! Natural operations on cones should work without referring to a particular enumeration of the rays. Think `cone1.intesection(cone2)` vs. `set(cone1.ambient_ray_indices()).intersection(set(cone2.ambient_ray_indices()))`. Of course sometimes you can't avoid it, definitely not in the internal implementations, but higher-level code (like the toric varieties) could easily move away from it. Case in point is that it is used only 9 times (the other 4 are in doctests). \n\nAnd this looks horrible\n\n```\ncone.ambient().ray_indices(cone)\n```\nprecisely because it is bad! It will break things! Its like a big, flashing sign: Do not write this code! You really want to use `self.fan().ray_indices(cone)`!\n\nI don't mind the availability of `cone.ambient_ray_indices()` so much if you use it on the command line; In that case you know what your ambient() is. But I think we should ban its use from the toric varieties code. Then we algorithmically audit it for correctness by grepping `sage/schemes/generic` for `ambient_ray_indices`. How does that sound?",
    "created_at": "2010-10-10T15:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99850",
    "user": "https://github.com/vbraun"
}
```

`ambient_ray_indices` is not natural! Natural operations on cones should work without referring to a particular enumeration of the rays. Think `cone1.intesection(cone2)` vs. `set(cone1.ambient_ray_indices()).intersection(set(cone2.ambient_ray_indices()))`. Of course sometimes you can't avoid it, definitely not in the internal implementations, but higher-level code (like the toric varieties) could easily move away from it. Case in point is that it is used only 9 times (the other 4 are in doctests). 

And this looks horrible

```
cone.ambient().ray_indices(cone)
```
precisely because it is bad! It will break things! Its like a big, flashing sign: Do not write this code! You really want to use `self.fan().ray_indices(cone)`!

I don't mind the availability of `cone.ambient_ray_indices()` so much if you use it on the command line; In that case you know what your ambient() is. But I think we should ban its use from the toric varieties code. Then we algorithmically audit it for correctness by grepping `sage/schemes/generic` for `ambient_ray_indices`. How does that sound?



---

archive/issue_comments_099851.json:
```json
{
    "body": "Well, instead of \"very-very\" let me say that `ambient_ray_incices` are as natural as coordinates. Coordinates may be not very convenient for definitions, since you need to make sure that the choice of the coordinate system does not matter. They are in many cases not mathematically natural in the sense that there are many different choices without any preference. At the same time they are quite useful both for proofs and for working with concrete examples.\n\nNow, choosing between `cone.ambient_ray_indices()` and `fan.ray_indices(cone)` is like choosing between always mentioning which coordinate system you are using whenever you use coordinates and having some coordinate system \"understood from context.\" Of course, in the second case you are risking to encounter a situation when it was not quite clear and it leads to mistakes since coordinates in one system may have very little to do with coordinates in another one. People do such mistakes from time to time, that's just life. But it is very convenient to have this default and I still vote for it despite the mistake that you have discovered. (By the way - how did you find it?)\n\nLeaving a function but banning it for internal use is a bit silly - the way to enforce it is to scan for occurrences of this function and then replace it with a \"safe version\". If you do it, then the second step can be making sure that it is used safely and correctly.",
    "created_at": "2010-10-11T00:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99851",
    "user": "https://github.com/novoselt"
}
```

Well, instead of "very-very" let me say that `ambient_ray_incices` are as natural as coordinates. Coordinates may be not very convenient for definitions, since you need to make sure that the choice of the coordinate system does not matter. They are in many cases not mathematically natural in the sense that there are many different choices without any preference. At the same time they are quite useful both for proofs and for working with concrete examples.

Now, choosing between `cone.ambient_ray_indices()` and `fan.ray_indices(cone)` is like choosing between always mentioning which coordinate system you are using whenever you use coordinates and having some coordinate system "understood from context." Of course, in the second case you are risking to encounter a situation when it was not quite clear and it leads to mistakes since coordinates in one system may have very little to do with coordinates in another one. People do such mistakes from time to time, that's just life. But it is very convenient to have this default and I still vote for it despite the mistake that you have discovered. (By the way - how did you find it?)

Leaving a function but banning it for internal use is a bit silly - the way to enforce it is to scan for occurrences of this function and then replace it with a "safe version". If you do it, then the second step can be making sure that it is used safely and correctly.



---

archive/issue_comments_099852.json:
```json
{
    "body": "In an effort to be less stubborn, here is what I think I should do if we cannot live with the existing interface:\n\n1. Keep internal fields `_ambient` and `_ambient_ray_indices` which can be related either to a cone or a fan (from the coding point of view these situations are similar and it is very convenient to treat them together - I know for sure since my initial version didn't do it).\n2. Remove `ambient()` and `ambient_ray_indices()` methods. In the code we still can use attributes since they always must be set in the constructor. Also remove `adjacent` and `facet_of` methods from cones and `star_generator_indices` and `star_generators` from cones of fan. The class `Cone_of_fan` becomes completely unnecessary and should be discarded.\n3. Add methods corresponding to the above ones with respect to an explicit ambient (of course, there is no analog for `ambient` itself anymore):\n {{{\nsage: ambient_cone.ray_indices(cone)\nsage: ambient_cone.adjacent_faces(cone)\nsage: ambient_cone.faces_with_facet(cone)\nsage: fan.ray_indices(cone)\nsage: fan.adjacent_cones(cone)\nsage: fan.cones_with_facet(cone)\nsage: fan.star_generators(cone)\nsage: fan.star_generator_indices(cone)\n}}}\n Cones still will cache all this stuff for their own `_ambient` in a hope that it will be useful later and that's how usually they will be called.\n\nBut I still need some voting before performing such a change.\n\nI still think that it is convenient to have a default for \"the thing before dot\" above. This opinion is based on actually working with such structures, so maybe I have bad habits, but that's what I prefer. I also still think that it is natural in mathematics. E.g. Fulton on p.52 defines Star(tau), where it is assumed that tau is a cone in some fan. In a lot of papers using reflexive polytopes people introduce some notation for dual faces. I have never seen such a notation mentioning the ambient polytope, yet the notion of a dual face does not make sense without one. One can argue that a face is supposed to know its ambient, because it is a face and not just a standalone polytope. But with this line of thoughts I think toric divisors may require a cone of an appropriate fan as an input. Or we can agree that we will use any input cone and try to interpret it as a cone in this appropriate fan, in which case it is our responsibility to ensure that we do such an interpretation correctly. It is also common to fix some index set and then use it to index rays of the fan, their generators, corresponding homogeneous variables, and divisors. So I still think that these indices are relevant beyond the implementation guts of cones...",
    "created_at": "2010-10-11T17:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99852",
    "user": "https://github.com/novoselt"
}
```

In an effort to be less stubborn, here is what I think I should do if we cannot live with the existing interface:

1. Keep internal fields `_ambient` and `_ambient_ray_indices` which can be related either to a cone or a fan (from the coding point of view these situations are similar and it is very convenient to treat them together - I know for sure since my initial version didn't do it).
2. Remove `ambient()` and `ambient_ray_indices()` methods. In the code we still can use attributes since they always must be set in the constructor. Also remove `adjacent` and `facet_of` methods from cones and `star_generator_indices` and `star_generators` from cones of fan. The class `Cone_of_fan` becomes completely unnecessary and should be discarded.
3. Add methods corresponding to the above ones with respect to an explicit ambient (of course, there is no analog for `ambient` itself anymore):
 {{{
sage: ambient_cone.ray_indices(cone)
sage: ambient_cone.adjacent_faces(cone)
sage: ambient_cone.faces_with_facet(cone)
sage: fan.ray_indices(cone)
sage: fan.adjacent_cones(cone)
sage: fan.cones_with_facet(cone)
sage: fan.star_generators(cone)
sage: fan.star_generator_indices(cone)
}}}
 Cones still will cache all this stuff for their own `_ambient` in a hope that it will be useful later and that's how usually they will be called.

But I still need some voting before performing such a change.

I still think that it is convenient to have a default for "the thing before dot" above. This opinion is based on actually working with such structures, so maybe I have bad habits, but that's what I prefer. I also still think that it is natural in mathematics. E.g. Fulton on p.52 defines Star(tau), where it is assumed that tau is a cone in some fan. In a lot of papers using reflexive polytopes people introduce some notation for dual faces. I have never seen such a notation mentioning the ambient polytope, yet the notion of a dual face does not make sense without one. One can argue that a face is supposed to know its ambient, because it is a face and not just a standalone polytope. But with this line of thoughts I think toric divisors may require a cone of an appropriate fan as an input. Or we can agree that we will use any input cone and try to interpret it as a cone in this appropriate fan, in which case it is our responsibility to ensure that we do such an interpretation correctly. It is also common to fix some index set and then use it to index rays of the fan, their generators, corresponding homogeneous variables, and divisors. So I still think that these indices are relevant beyond the implementation guts of cones...



---

archive/issue_comments_099853.json:
```json
{
    "body": "I don't want to rewrite the entire interface, and I think that having some implicit assumption about what the `ambient()` is is usually fine. Also, 3.) is spectacularly ugly :-P  As I said before, if the method call e.g. returns again a collection of cones then you'll immediately notice that you had the wrong `ambient()`. The difference with `ambient_ray_indices` is that its output will fail in much more subtle ways if the hidden assumption is wrong.\n\nIf you desperately want to keep `ambient_ray_indices()`, how about we prefix any use in the toric varieties code with an assertion that makes it explicit. This would be yet another way to make the implicit assumption explicit and have it easily machine-verifiable. \n\nOn an unrelated note, I don't like `cone_of_fan = fan(cone)`, its too similar to `Fan([cone])`. How about `Fan.cone_equivalent_to(cone)`, see also the already-existing similar method `Fan.cone_containing(cone)`.",
    "created_at": "2010-10-12T12:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99853",
    "user": "https://github.com/vbraun"
}
```

I don't want to rewrite the entire interface, and I think that having some implicit assumption about what the `ambient()` is is usually fine. Also, 3.) is spectacularly ugly :-P  As I said before, if the method call e.g. returns again a collection of cones then you'll immediately notice that you had the wrong `ambient()`. The difference with `ambient_ray_indices` is that its output will fail in much more subtle ways if the hidden assumption is wrong.

If you desperately want to keep `ambient_ray_indices()`, how about we prefix any use in the toric varieties code with an assertion that makes it explicit. This would be yet another way to make the implicit assumption explicit and have it easily machine-verifiable. 

On an unrelated note, I don't like `cone_of_fan = fan(cone)`, its too similar to `Fan([cone])`. How about `Fan.cone_equivalent_to(cone)`, see also the already-existing similar method `Fan.cone_containing(cone)`.



---

archive/issue_comments_099854.json:
```json
{
    "body": "Replying to [comment:34 vbraun]:\n> 3.) is spectacularly ugly :-P\n\n\nI wholeheartedly agree ;-)\n \n> If you desperately want to keep `ambient_ray_indices()`, how about we prefix any use in the toric varieties code with an assertion that makes it explicit. This would be yet another way to make the implicit assumption explicit and have it easily machine-verifiable. \n\n\nI desperately want to keep it! I think that assertions are great - I don't use them much mostly because I didn't know about them until reviewing some of your code, but I am totally for them. However using them always before `ambient_ray_indices()` is too harsh - I went through `cone.py, fan.py, toric_variety.py, fano_toric_variety.py` and in all cases it was actually already clear that `cone._ambient` is correct, e.g. because `cone` was constructed in the same code. So I think that more generally we should use assertions for input parameters, which was the problem in this case.\n\n> On an unrelated note, I don't like `cone_of_fan = fan(cone)`, its too similar to `Fan([cone])`. How about `Fan.cone_equivalent_to(cone)`, see also the already-existing similar method `Fan.cone_containing(cone)`.\n\n\n`fan(cone)` is similar to `Fan([cone])` only if your fan is called `fan` ;-) I was thinking of such format to mimic Element-Parent behaviour in Sage, but:\n* currently we don't use this model for cones and fans;\n* if we did, then cones must be both elements (of fans) and parents (of points), and this is not yet supported in Sage;\n* I don't clearly see advantages of such a switch;\n* I would like to have the same interface for \"putting\" cones into fans and faces into cones.\nSo the attached patch implements for cones and fans methods `embed(cone)`. `cone_equivalent_to` seems unclear to me despite of being long, but I am not sure if `embed` is much better - what do you think of it? Maybe `embed_cone/embed_face` would be more clear?\n\nI propose a bit different implementation of this method than in your patch. For fans it computes potential ray indices and then uses `cone_containing` method. This should be faster than using `cone_containing` directly on the rays and does not trigger cone lattice computation. For cones it will go through all faces of the relevant dimension, but instead of checking cone equivalence it still computes potential ray indices and then looks for a face with them. It will not work for non-strictly convex cones, where I also check for equivalence. (Although it will not work yet anyway - we cannot compute face lattice in such a case.) Documentation is mostly the same for fans and cones, but I tried to explain and illustrate clearly what the function does and why one should care.\n\nI have also tweaked `Fan` constructor a little bit - now rays of the fan generated by a singe cone will have the same order as this cone. Shuffling bugged me some time before and again now that I was writing doctests for embeddings. My general attitude to such situations is that users enter data in the way they like, so it is good to preserve it as much as possible.",
    "created_at": "2010-10-13T04:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99854",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:34 vbraun]:
> 3.) is spectacularly ugly :-P


I wholeheartedly agree ;-)
 
> If you desperately want to keep `ambient_ray_indices()`, how about we prefix any use in the toric varieties code with an assertion that makes it explicit. This would be yet another way to make the implicit assumption explicit and have it easily machine-verifiable. 


I desperately want to keep it! I think that assertions are great - I don't use them much mostly because I didn't know about them until reviewing some of your code, but I am totally for them. However using them always before `ambient_ray_indices()` is too harsh - I went through `cone.py, fan.py, toric_variety.py, fano_toric_variety.py` and in all cases it was actually already clear that `cone._ambient` is correct, e.g. because `cone` was constructed in the same code. So I think that more generally we should use assertions for input parameters, which was the problem in this case.

> On an unrelated note, I don't like `cone_of_fan = fan(cone)`, its too similar to `Fan([cone])`. How about `Fan.cone_equivalent_to(cone)`, see also the already-existing similar method `Fan.cone_containing(cone)`.


`fan(cone)` is similar to `Fan([cone])` only if your fan is called `fan` ;-) I was thinking of such format to mimic Element-Parent behaviour in Sage, but:
* currently we don't use this model for cones and fans;
* if we did, then cones must be both elements (of fans) and parents (of points), and this is not yet supported in Sage;
* I don't clearly see advantages of such a switch;
* I would like to have the same interface for "putting" cones into fans and faces into cones.
So the attached patch implements for cones and fans methods `embed(cone)`. `cone_equivalent_to` seems unclear to me despite of being long, but I am not sure if `embed` is much better - what do you think of it? Maybe `embed_cone/embed_face` would be more clear?

I propose a bit different implementation of this method than in your patch. For fans it computes potential ray indices and then uses `cone_containing` method. This should be faster than using `cone_containing` directly on the rays and does not trigger cone lattice computation. For cones it will go through all faces of the relevant dimension, but instead of checking cone equivalence it still computes potential ray indices and then looks for a face with them. It will not work for non-strictly convex cones, where I also check for equivalence. (Although it will not work yet anyway - we cannot compute face lattice in such a case.) Documentation is mostly the same for fans and cones, but I tried to explain and illustrate clearly what the function does and why one should care.

I have also tweaked `Fan` constructor a little bit - now rays of the fan generated by a singe cone will have the same order as this cone. Shuffling bugged me some time before and again now that I was writing doctests for embeddings. My general attitude to such situations is that users enter data in the way they like, so it is good to preserve it as much as possible.



---

archive/issue_comments_099855.json:
```json
{
    "body": "P.S. I also optimized `is_equivalent` for cones of the same ambient, as was suggested in http://trac.sagemath.org/sage_trac/ticket/9972#comment:20.",
    "created_at": "2010-10-13T04:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99855",
    "user": "https://github.com/novoselt"
}
```

P.S. I also optimized `is_equivalent` for cones of the same ambient, as was suggested in http://trac.sagemath.org/sage_trac/ticket/9972#comment:20.



---

archive/issue_comments_099856.json:
```json
{
    "body": "Fixes for non-strictly convex cones: `cone` --> `self` for convexity check in `Cone.embed` and extra convexity check in `Cone.is_equivalent` for the case of common ambient (does not require extra computations for cones of fans, they are always directly set to be strictly convex).",
    "created_at": "2010-10-13T16:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99856",
    "user": "https://github.com/novoselt"
}
```

Fixes for non-strictly convex cones: `cone` --> `self` for convexity check in `Cone.embed` and extra convexity check in `Cone.is_equivalent` for the case of common ambient (does not require extra computations for cones of fans, they are always directly set to be strictly convex).



---

archive/issue_comments_099857.json:
```json
{
    "body": "I couldn't figure out whether your patch goes before or after mine, so I folded it into one and fixed everything.\n\nI changed \n\n```\n        # Optimization for fans generated by a single cone\n        if len(cones) == 1:\n            cone = cones[0]\n            return RationalPolyhedralFan((tuple(range(cone.nrays())), ),\n                                         cone.rays(), lattice,\n                                         is_complete=lattice.dimension() > 0)\n```\nto `is_complete=(lattice.dimension()==0)`.\n\nNow that we agree on this ;-) can you go ahead and remove the `Enhanced*` versions of fans and cones? Then we can go on with fan morphisms...",
    "created_at": "2010-10-14T19:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99857",
    "user": "https://github.com/vbraun"
}
```

I couldn't figure out whether your patch goes before or after mine, so I folded it into one and fixed everything.

I changed 

```
        # Optimization for fans generated by a single cone
        if len(cones) == 1:
            cone = cones[0]
            return RationalPolyhedralFan((tuple(range(cone.nrays())), ),
                                         cone.rays(), lattice,
                                         is_complete=lattice.dimension() > 0)
```
to `is_complete=(lattice.dimension()==0)`.

Now that we agree on this ;-) can you go ahead and remove the `Enhanced*` versions of fans and cones? Then we can go on with fan morphisms...



---

archive/issue_comments_099858.json:
```json
{
    "body": "Attachment [trac_9972_add_cone_embedding.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_add_cone_embedding.patch) by @novoselt created at 2010-10-14 23:44:15",
    "created_at": "2010-10-14T23:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99858",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9972_add_cone_embedding.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_add_cone_embedding.patch) by @novoselt created at 2010-10-14 23:44:15



---

archive/issue_comments_099859.json:
```json
{
    "body": "Attachment [trac_9972_improve_element_constructors.3.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_improve_element_constructors.3.patch) by @novoselt created at 2010-10-15 00:15:07\n\nOops, sorry - I should have written that it was supposed to be the first. I unfolded the patches back so that it is clear who is writing/reviewing what and we don't need to seek the third person for the final review. I have updated my patch to fix the mistake that you caught. In your part I have removed `is_equivalent` from `Cone_of_fan` since this optimization is now performed by general cones. I have also removed extra parenthesis from `cone = fan().embed(x)`.\n\nI also have one more issue with your patch which got lost above, regarding new containment check: cones are equal if they have the same rays in the same order and equivalent if they define the same set of points. If the same cone happened to sit in different fans (or cones, for that matter) and so has several different objects representing it, it does not change anything. We can check if cones belong to the same ambient structure for code optimization, but the output should be the same. Also, to me it feels perfectly natural to ask e.g. whether a cone of some fan belongs to a subdivision of this fan. So I think that `cone in fan` should return `True` if `cone` is equivalent to any of the cones of `fan`. What is the ambient structure of `cone` and what is its ray order does not matter. If you really disagree with this, then I think that `cone in fan` should return `True` ONLY if `cone.ambient() is fan` is `True`. But I definitely prefer the first variant. Then one can write\n\n```\nsage: if cone in fan:\nsage:     cone = fan.embed(cone)\nsage:     Do something, say with cone.adjacent()\nsage: else:\nsage:     Deal with it somehow.\n```",
    "created_at": "2010-10-15T00:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99859",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9972_improve_element_constructors.3.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_improve_element_constructors.3.patch) by @novoselt created at 2010-10-15 00:15:07

Oops, sorry - I should have written that it was supposed to be the first. I unfolded the patches back so that it is clear who is writing/reviewing what and we don't need to seek the third person for the final review. I have updated my patch to fix the mistake that you caught. In your part I have removed `is_equivalent` from `Cone_of_fan` since this optimization is now performed by general cones. I have also removed extra parenthesis from `cone = fan().embed(x)`.

I also have one more issue with your patch which got lost above, regarding new containment check: cones are equal if they have the same rays in the same order and equivalent if they define the same set of points. If the same cone happened to sit in different fans (or cones, for that matter) and so has several different objects representing it, it does not change anything. We can check if cones belong to the same ambient structure for code optimization, but the output should be the same. Also, to me it feels perfectly natural to ask e.g. whether a cone of some fan belongs to a subdivision of this fan. So I think that `cone in fan` should return `True` if `cone` is equivalent to any of the cones of `fan`. What is the ambient structure of `cone` and what is its ray order does not matter. If you really disagree with this, then I think that `cone in fan` should return `True` ONLY if `cone.ambient() is fan` is `True`. But I definitely prefer the first variant. Then one can write

```
sage: if cone in fan:
sage:     cone = fan.embed(cone)
sage:     Do something, say with cone.adjacent()
sage: else:
sage:     Deal with it somehow.
```



---

archive/issue_comments_099860.json:
```json
{
    "body": "Attachment [trac_9972_remove_enhanced_cones_and_fans.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_remove_enhanced_cones_and_fans.patch) by @novoselt created at 2010-10-15 00:58:09",
    "created_at": "2010-10-15T00:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99860",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9972_remove_enhanced_cones_and_fans.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_remove_enhanced_cones_and_fans.patch) by @novoselt created at 2010-10-15 00:58:09



---

archive/issue_comments_099861.json:
```json
{
    "body": "Enhanced cones are removed, all tests pass. Current ticket queue: last three patches then the first one (which is going to be changed).",
    "created_at": "2010-10-15T01:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99861",
    "user": "https://github.com/novoselt"
}
```

Enhanced cones are removed, all tests pass. Current ticket queue: last three patches then the first one (which is going to be changed).



---

archive/issue_comments_099862.json:
```json
{
    "body": "I agree with `cone in fan` meaning that cone is equivalent to any cone of the fan. I updated my patch to reflect this.",
    "created_at": "2010-10-15T08:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99862",
    "user": "https://github.com/vbraun"
}
```

I agree with `cone in fan` meaning that cone is equivalent to any cone of the fan. I updated my patch to reflect this.



---

archive/issue_comments_099863.json:
```json
{
    "body": "Oops I had forgotten to refresh the patch. Correct version follows.",
    "created_at": "2010-10-15T13:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99863",
    "user": "https://github.com/vbraun"
}
```

Oops I had forgotten to refresh the patch. Correct version follows.



---

archive/issue_comments_099864.json:
```json
{
    "body": "Attachment [trac_9972_improve_element_constructors.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_improve_element_constructors.patch) by @vbraun created at 2010-10-15 13:17:30\n\nUpdated patch",
    "created_at": "2010-10-15T13:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99864",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9972_improve_element_constructors.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_improve_element_constructors.patch) by @vbraun created at 2010-10-15 13:17:30

Updated patch



---

archive/issue_comments_099865.json:
```json
{
    "body": "I'll post an updated patch with `FanMorphism` shortly.\n\nRegarding `image_cone` and `preimage_cones` - I guess we want them to work for arbitrary cones of domain/codomain fans. In this case it is still clear what to return for `image_cone(cone)` - the smallest cone of the codomain fan which contains the image. But what about `preimage_cones`? Should we return all cones that are mapped to it, or only maximal ones? (We can also consider packing them into a fan, but in this case we loose connection with the domain fan, so I don't think that it is a good idea.)\n\nI am also not sure what would be an efficient way to determine preimage cones. I am thinking about determining rays that are mapped into the given codomain cone and then scanning trough all domain cones to see which are generated by such rays only. An alternative approach, which is likely to be better for intensive work with such cones, is to compute full dictionary for image cones and then revert it to get preimage ones. Any suggestions?",
    "created_at": "2010-10-18T02:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99865",
    "user": "https://github.com/novoselt"
}
```

I'll post an updated patch with `FanMorphism` shortly.

Regarding `image_cone` and `preimage_cones` - I guess we want them to work for arbitrary cones of domain/codomain fans. In this case it is still clear what to return for `image_cone(cone)` - the smallest cone of the codomain fan which contains the image. But what about `preimage_cones`? Should we return all cones that are mapped to it, or only maximal ones? (We can also consider packing them into a fan, but in this case we loose connection with the domain fan, so I don't think that it is a good idea.)

I am also not sure what would be an efficient way to determine preimage cones. I am thinking about determining rays that are mapped into the given codomain cone and then scanning trough all domain cones to see which are generated by such rays only. An alternative approach, which is likely to be better for intensive work with such cones, is to compute full dictionary for image cones and then revert it to get preimage ones. Any suggestions?



---

archive/issue_comments_099866.json:
```json
{
    "body": "I am attaching a patch that does not compute `preimage_cones` yet, but the rest is claimed to be ready for review/comments. I have removed classes for lattice morphisms themselves since they were not adding anything anymore. All of the old functionality is moved to `FanMorphism` constructor as you have suggested above. Codomain fan can now be omitted and will be computed, if possible.\n\nThis feature has exposed a problem I mentioned (I think) when we were adding warnings to the `Fan` constructor. The image fan is generated by images of cones of the original fan and these images may coincide or become non-maximal. As a result, one of the doctests fails due to the warning that some cones were discarded and users may see such a message as well, which will be quite confusing, I think. What should we do? Add a parameter to `Fan(..., warn=True)` and set it to `False` explicitly in the internal code?\n\nCurrent queue:\n* trac_9972_add_cone_embedding.patch\n* trac_9972_improve_element_constructors.patch\n* trac_9972_remove_enhanced_cones_and_fans.patch\n* trac_9972_add_fan_morphisms.patch",
    "created_at": "2010-10-18T04:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99866",
    "user": "https://github.com/novoselt"
}
```

I am attaching a patch that does not compute `preimage_cones` yet, but the rest is claimed to be ready for review/comments. I have removed classes for lattice morphisms themselves since they were not adding anything anymore. All of the old functionality is moved to `FanMorphism` constructor as you have suggested above. Codomain fan can now be omitted and will be computed, if possible.

This feature has exposed a problem I mentioned (I think) when we were adding warnings to the `Fan` constructor. The image fan is generated by images of cones of the original fan and these images may coincide or become non-maximal. As a result, one of the doctests fails due to the warning that some cones were discarded and users may see such a message as well, which will be quite confusing, I think. What should we do? Add a parameter to `Fan(..., warn=True)` and set it to `False` explicitly in the internal code?

Current queue:
* trac_9972_add_cone_embedding.patch
* trac_9972_improve_element_constructors.patch
* trac_9972_remove_enhanced_cones_and_fans.patch
* trac_9972_add_fan_morphisms.patch



---

archive/issue_comments_099867.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-10-20T03:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99867",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_099868.json:
```json
{
    "body": "OK, `preimage_cones` can now be computed, everything is doctested, the last issue is with warnings.",
    "created_at": "2010-10-20T03:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99868",
    "user": "https://github.com/novoselt"
}
```

OK, `preimage_cones` can now be computed, everything is doctested, the last issue is with warnings.



---

archive/issue_comments_099869.json:
```json
{
    "body": "Attachment [trac_9972_fix_fan_warning.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_fix_fan_warning.patch) by @novoselt created at 2010-10-23 18:02:22",
    "created_at": "2010-10-23T18:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99869",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9972_fix_fan_warning.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_fix_fan_warning.patch) by @novoselt created at 2010-10-23 18:02:22



---

archive/issue_comments_099870.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-23T18:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99870",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_099871.json:
```json
{
    "body": "After some more contemplating, I don't really see any other solution to the problem except for adding a parameter to suppress warnings. (Well, the other option is to remove the warning completely, but I have a feeling that it will not be accepted ;-)) So the last patch does exactly that, now all doctests pass smoothly and I propose merging this ticket.\n\nFor the record: I am giving positive review to the current \"trac_9972_improve_element_constructors.patch\" written by Volker Braun.",
    "created_at": "2010-10-23T18:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99871",
    "user": "https://github.com/novoselt"
}
```

After some more contemplating, I don't really see any other solution to the problem except for adding a parameter to suppress warnings. (Well, the other option is to remove the warning completely, but I have a feeling that it will not be accepted ;-)) So the last patch does exactly that, now all doctests pass smoothly and I propose merging this ticket.

For the record: I am giving positive review to the current "trac_9972_improve_element_constructors.patch" written by Volker Braun.



---

archive/issue_comments_099872.json:
```json
{
    "body": "Looks good overall, but I think there is a bug in `image_cone()`:\n\n```\nsage: N1 = ToricLattice(1)\nsage: N2 = ToricLattice(2)\nsage: Hom21 = Hom(N2,N1)\nsage: pr = Hom21([N1.0,0])\nsage: P1xP1=toric_varieties.P1xP1().fan()\nsage: f = FanMorphism(pr, P1xP1)\nsage: f.codomain_fan().generating_cones()\n(1-d cone of Rational polyhedral fan in 1-d lattice N, 1-d cone of Rational polyhedral fan in 1-d lattice N)\nsage: [ f.image_cone(c) for c in P1xP1.generating_cones() ]\n[0-d cone of Rational polyhedral fan in 1-d lattice N, 0-d cone of Rational polyhedral fan in 1-d lattice N, 0-d cone of Rational polyhedral fan in 1-d lattice N, 0-d cone of Rational polyhedral fan in 1-d lattice N]\n```",
    "created_at": "2010-11-08T04:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99872",
    "user": "https://github.com/vbraun"
}
```

Looks good overall, but I think there is a bug in `image_cone()`:

```
sage: N1 = ToricLattice(1)
sage: N2 = ToricLattice(2)
sage: Hom21 = Hom(N2,N1)
sage: pr = Hom21([N1.0,0])
sage: P1xP1=toric_varieties.P1xP1().fan()
sage: f = FanMorphism(pr, P1xP1)
sage: f.codomain_fan().generating_cones()
(1-d cone of Rational polyhedral fan in 1-d lattice N, 1-d cone of Rational polyhedral fan in 1-d lattice N)
sage: [ f.image_cone(c) for c in P1xP1.generating_cones() ]
[0-d cone of Rational polyhedral fan in 1-d lattice N, 0-d cone of Rational polyhedral fan in 1-d lattice N, 0-d cone of Rational polyhedral fan in 1-d lattice N, 0-d cone of Rational polyhedral fan in 1-d lattice N]
```



---

archive/issue_comments_099873.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-08T04:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99873",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099874.json:
```json
{
    "body": "Thanks for catching it!\n\nFortunately, I still believe that `image_cone` is correct, but I have tracked down two \"degenerate case\" bugs: #10237 (I have fixed it and it is sufficient for this ticket to work correctly) and #10238 (which I have left for you ;-)).",
    "created_at": "2010-11-08T15:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99874",
    "user": "https://github.com/novoselt"
}
```

Thanks for catching it!

Fortunately, I still believe that `image_cone` is correct, but I have tracked down two "degenerate case" bugs: #10237 (I have fixed it and it is sufficient for this ticket to work correctly) and #10238 (which I have left for you ;-)).



---

archive/issue_comments_099875.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-08T15:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99875",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099876.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-08T19:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99876",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099877.json:
```json
{
    "body": "Ok now `image_cone` works but I can't compute the preimage:\n\n```\nsage: c = f.image_cone( Cone([(1,0),(0,1)]) )\nsage: c\n1-d cone of Rational polyhedral fan in 1-d lattice N\nsage: f.preimage_cones(c)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/vbraun/opt/sage-4.6/devel/sage-main/<ipython console> in <module>()\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan_morphism.pyc in preimage_cones(self, cone)\n    858                 for dcone in dcones:\n    859                     if (possible_rays.issuperset(dcone.ambient_ray_indices())\n--> 860                         and self.image_cone(dcone).is_face_of(cone)):\n    861                         preimage_cones.append(dcone)\n    862             self._preimage_cones[cone] = preimage_cones\n\n/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan_morphism.pyc in image_cone(self, cone)\n    809                 RISGIS = self._RISGIS()\n    810                 CSGIS = set(reduce(operator.and_,\n--> 811                             (RISGIS[i] for i in cone.ambient_ray_indices())))\n    812                 image_cone = codomain_fan.generating_cone(CSGIS.pop())\n    813                 for i in CSGIS:\n\nTypeError: reduce() of empty sequence with no initial value\n```",
    "created_at": "2010-11-08T19:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99877",
    "user": "https://github.com/vbraun"
}
```

Ok now `image_cone` works but I can't compute the preimage:

```
sage: c = f.image_cone( Cone([(1,0),(0,1)]) )
sage: c
1-d cone of Rational polyhedral fan in 1-d lattice N
sage: f.preimage_cones(c)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/vbraun/opt/sage-4.6/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan_morphism.pyc in preimage_cones(self, cone)
    858                 for dcone in dcones:
    859                     if (possible_rays.issuperset(dcone.ambient_ray_indices())
--> 860                         and self.image_cone(dcone).is_face_of(cone)):
    861                         preimage_cones.append(dcone)
    862             self._preimage_cones[cone] = preimage_cones

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan_morphism.pyc in image_cone(self, cone)
    809                 RISGIS = self._RISGIS()
    810                 CSGIS = set(reduce(operator.and_,
--> 811                             (RISGIS[i] for i in cone.ambient_ray_indices())))
    812                 image_cone = codomain_fan.generating_cone(CSGIS.pop())
    813                 for i in CSGIS:

TypeError: reduce() of empty sequence with no initial value
```



---

archive/issue_comments_099878.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-08T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99878",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099879.json:
```json
{
    "body": "Indeed, it does not work and moreover - the error was in `image_cone`.\n\nI have updated the main patch by adding a special branch for the image of the trivial cone and inserted your example into `preimage_cones` docstring.",
    "created_at": "2010-11-08T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99879",
    "user": "https://github.com/novoselt"
}
```

Indeed, it does not work and moreover - the error was in `image_cone`.

I have updated the main patch by adding a special branch for the image of the trivial cone and inserted your example into `preimage_cones` docstring.



---

archive/issue_comments_099880.json:
```json
{
    "body": "Why is `preimage_cones` not the preimage of `image_cones`? This confuses me:\n\n```\nsage: cone =  f.image_cone( Cone([(1,0),(0,1)]) )\nsage: [ cone is f.image_cone(c) for c in f.preimage_cones(cone) ]\n[True, True, True, False, False, False]\n```\nI understand that it is working as documented, but it seems like it would be more useful to actually return the preimage cones. In other words, take preimage cones in the sense of fan morphisms and not in the sense of convex sets.\n\nIf one is interested in all cones mapping geometrically into a given cone one could always construct the `Fan` of the (fan morphism) preimage cones.",
    "created_at": "2010-11-09T16:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99880",
    "user": "https://github.com/vbraun"
}
```

Why is `preimage_cones` not the preimage of `image_cones`? This confuses me:

```
sage: cone =  f.image_cone( Cone([(1,0),(0,1)]) )
sage: [ cone is f.image_cone(c) for c in f.preimage_cones(cone) ]
[True, True, True, False, False, False]
```
I understand that it is working as documented, but it seems like it would be more useful to actually return the preimage cones. In other words, take preimage cones in the sense of fan morphisms and not in the sense of convex sets.

If one is interested in all cones mapping geometrically into a given cone one could always construct the `Fan` of the (fan morphism) preimage cones.



---

archive/issue_comments_099881.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-11-09T16:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99881",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_099882.json:
```json
{
    "body": "I am actually not quite sure I completely understand your comments, which makes me think that method names and definitions require some adjustments. How about the following:\n* `cones_mapped_into(cone)` returning all cones of the domain fan mapped into the given `cone` of the codomain fan (this is what `preimage_cones` does now). They do form a fan, but I am not sure that it is a good idea to construct it, since we will loose connection to the domain fan then.\n* `cones_mapped_onto(cone)` returning all cones of the domain fan whose `image_cone` is equal to the given `cone` of the codomain fan. Is this what you are talking about?\nIn both cases we may add extra parameter to allow returning only maximal cones with these properties. Or we can add a function to `fan` module like `maximal_cones(cones)` that will select the maximal ones. In the case of cones of the same fan the selection process is not terribly expensive.\n\nAs for `preimage_cones`, I would say that `preimage_cone` would make perfect sense if it was just the set-theoretic preimage of a given cone, which in general is not strictly-convex and is likely to be not a part of the domain fan. I actually compute these cones internally for generating cones of the codomain fan, but I am not sure they have much value to the end user.\n\nThoughts?",
    "created_at": "2010-11-09T22:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99882",
    "user": "https://github.com/novoselt"
}
```

I am actually not quite sure I completely understand your comments, which makes me think that method names and definitions require some adjustments. How about the following:
* `cones_mapped_into(cone)` returning all cones of the domain fan mapped into the given `cone` of the codomain fan (this is what `preimage_cones` does now). They do form a fan, but I am not sure that it is a good idea to construct it, since we will loose connection to the domain fan then.
* `cones_mapped_onto(cone)` returning all cones of the domain fan whose `image_cone` is equal to the given `cone` of the codomain fan. Is this what you are talking about?
In both cases we may add extra parameter to allow returning only maximal cones with these properties. Or we can add a function to `fan` module like `maximal_cones(cones)` that will select the maximal ones. In the case of cones of the same fan the selection process is not terribly expensive.

As for `preimage_cones`, I would say that `preimage_cone` would make perfect sense if it was just the set-theoretic preimage of a given cone, which in general is not strictly-convex and is likely to be not a part of the domain fan. I actually compute these cones internally for generating cones of the codomain fan, but I am not sure they have much value to the end user.

Thoughts?



---

archive/issue_comments_099883.json:
```json
{
    "body": "I think the geometric image/preimage of a cone is not particularly useful for toric morphisms. A fan morphism maps cones to cones, but does *not* define linear maps of the individual cones. One should think of it as a map from the poset of domain cones to the poset of codomain cones. Or, in geometric terms, maps of the poset of torus orbits to the poset of torus orbits. \n\nThe usual blow-up example \n\n```\nsage: c1 = Cone([(1,0),(1,1)])\nsage: c2 = Cone([(1,1),(0,1)])\nsage: domain_fan = Fan([c1, c2])\nsage: codomain_fan = Fan([Cone([(1,0),(0,1)])])\nsage: f = FanMorphism(identity_matrix(ZZ,2),domain_fan,codomain_fan)\nsage: ray = Cone([(1,1)])\nsage: f.image_cone(ray)\n2-d cone of Rational polyhedral fan in 2-d lattice N\n```\nmeans, geometrically, that the orbit closure `P^1` corresponding to the cone `ray` (given by the relative star of `ray`) is mapped to the point corresponding to the `f.image_cone(ray)`. Conversely, the preimage cones of `f.image_cone(ray)` are `c1`, `c2`, and `ray`. Geometrically, this means that the preimage of the point `f.image_cone(ray)` consists of the torus orbits (north pole), (south pole), `C^*` making up the fiber `P^1`.",
    "created_at": "2010-11-09T22:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99883",
    "user": "https://github.com/vbraun"
}
```

I think the geometric image/preimage of a cone is not particularly useful for toric morphisms. A fan morphism maps cones to cones, but does *not* define linear maps of the individual cones. One should think of it as a map from the poset of domain cones to the poset of codomain cones. Or, in geometric terms, maps of the poset of torus orbits to the poset of torus orbits. 

The usual blow-up example 

```
sage: c1 = Cone([(1,0),(1,1)])
sage: c2 = Cone([(1,1),(0,1)])
sage: domain_fan = Fan([c1, c2])
sage: codomain_fan = Fan([Cone([(1,0),(0,1)])])
sage: f = FanMorphism(identity_matrix(ZZ,2),domain_fan,codomain_fan)
sage: ray = Cone([(1,1)])
sage: f.image_cone(ray)
2-d cone of Rational polyhedral fan in 2-d lattice N
```
means, geometrically, that the orbit closure `P^1` corresponding to the cone `ray` (given by the relative star of `ray`) is mapped to the point corresponding to the `f.image_cone(ray)`. Conversely, the preimage cones of `f.image_cone(ray)` are `c1`, `c2`, and `ray`. Geometrically, this means that the preimage of the point `f.image_cone(ray)` consists of the torus orbits (north pole), (south pole), `C^*` making up the fiber `P^1`.



---

archive/issue_comments_099884.json:
```json
{
    "body": "Why a fan morphism does not define linear maps on individual cones? A fan morphism is a linear map between lattices, so it can be restricted to any (compatible) pair of domain/codomain cones and still induce a morphism between corresponding affine varieties. Just specifying mapping of fans as finite sets of cones is not sufficient, e.g. identity morphism and multiplication by 2 are different but obviously would induce the same cone correspondence. So since the actual linear map does matter, it makes sense to use preimages under this linear map. I agree that full (potentially non-strictly convex) preimages are probably of little use, we need to restrict to the domain fan, but I don't see why something called \"preimage\" should ever exclude the origin. In the sense of orbit closures it does correspond to the whole variety, but in the sense of affine patches it corresponds to the torus itself which is a part of any toric variety of the given dimension and always gets mapped to itself.\n\nSo I still propose the switch to `cones_mapping_into` for the current version and adding `cones_mapping_onto` for the version that you want to have. No `preimage_cones` at all since it is a confusing name in this context. On the level of toric varieties the corresponding methods may refer to orbits to make things clear, but here they are not present yet.",
    "created_at": "2010-11-09T23:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99884",
    "user": "https://github.com/novoselt"
}
```

Why a fan morphism does not define linear maps on individual cones? A fan morphism is a linear map between lattices, so it can be restricted to any (compatible) pair of domain/codomain cones and still induce a morphism between corresponding affine varieties. Just specifying mapping of fans as finite sets of cones is not sufficient, e.g. identity morphism and multiplication by 2 are different but obviously would induce the same cone correspondence. So since the actual linear map does matter, it makes sense to use preimages under this linear map. I agree that full (potentially non-strictly convex) preimages are probably of little use, we need to restrict to the domain fan, but I don't see why something called "preimage" should ever exclude the origin. In the sense of orbit closures it does correspond to the whole variety, but in the sense of affine patches it corresponds to the torus itself which is a part of any toric variety of the given dimension and always gets mapped to itself.

So I still propose the switch to `cones_mapping_into` for the current version and adding `cones_mapping_onto` for the version that you want to have. No `preimage_cones` at all since it is a confusing name in this context. On the level of toric varieties the corresponding methods may refer to orbits to make things clear, but here they are not present yet.



---

archive/issue_comments_099885.json:
```json
{
    "body": "There is clearly important information in how the lattice spanned by a cone is mapped to a sublattice of the lattice spanned by the image cone. But that is just the restriction of the underlying lattice morphism, and not associated to just any cone of the domain. You never need the geometric image/preimage of a cone for toric geometry.\n\nI would find it confusing if the `FanMorphism` contained any other \"map of cones\" than fan morphisms. Since there is no ambiguity in \"image cone\", there is no question about \"preimage cones\" in that category. If you want `cones_mapping_into` and `cones_mapping_onto` for implementation purposes that is fine, but `image_cone` and `preimage_cones` are what they are and should be called like that.",
    "created_at": "2010-11-10T04:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99885",
    "user": "https://github.com/vbraun"
}
```

There is clearly important information in how the lattice spanned by a cone is mapped to a sublattice of the lattice spanned by the image cone. But that is just the restriction of the underlying lattice morphism, and not associated to just any cone of the domain. You never need the geometric image/preimage of a cone for toric geometry.

I would find it confusing if the `FanMorphism` contained any other "map of cones" than fan morphisms. Since there is no ambiguity in "image cone", there is no question about "preimage cones" in that category. If you want `cones_mapping_into` and `cones_mapping_onto` for implementation purposes that is fine, but `image_cone` and `preimage_cones` are what they are and should be called like that.



---

archive/issue_comments_099886.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-10T05:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99886",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_099887.json:
```json
{
    "body": "I kind of complained before that I don't quite understand the term \"fan morphism\" ;-)\n\nFrom the beginning of the ticket:\n\nReplying to [comment:6 vbraun]:\n> Replying to [comment:5 novoselt]:\n> > \"it is a morphism between toric lattices with distinguished fans in the domain and codomain which are compatible with this morphism.\"\n\n> \n> Yes, that is the usual definition. No restriction on the support of the underlying lattice map. \n\n\nSo, as I understand we have a category with fans being objects. A fan is a collection of cones, each cone is a set of points. All cones of the fan sit in the same lattice, so there is also \"the lattice of the fan.\"\n\nMorphisms in this category are morphisms between lattices associated to fans, which map cones into cones as sets of points. So in particular they do define linear maps between individual cones as well, and I got lost when you said that they don't.\n\nBut I guess I agree that when we talk about images/preimages of cones, we should refer to the induced map between cones as a map between two finite sets, since we do not have a nice correspondence between cones as sets of points. Let me think a little more about it and post an updated patch.",
    "created_at": "2010-11-10T05:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99887",
    "user": "https://github.com/novoselt"
}
```

I kind of complained before that I don't quite understand the term "fan morphism" ;-)

From the beginning of the ticket:

Replying to [comment:6 vbraun]:
> Replying to [comment:5 novoselt]:
> > "it is a morphism between toric lattices with distinguished fans in the domain and codomain which are compatible with this morphism."

> 
> Yes, that is the usual definition. No restriction on the support of the underlying lattice map. 


So, as I understand we have a category with fans being objects. A fan is a collection of cones, each cone is a set of points. All cones of the fan sit in the same lattice, so there is also "the lattice of the fan."

Morphisms in this category are morphisms between lattices associated to fans, which map cones into cones as sets of points. So in particular they do define linear maps between individual cones as well, and I got lost when you said that they don't.

But I guess I agree that when we talk about images/preimages of cones, we should refer to the induced map between cones as a map between two finite sets, since we do not have a nice correspondence between cones as sets of points. Let me think a little more about it and post an updated patch.



---

archive/issue_comments_099888.json:
```json
{
    "body": "I am convinced, the updated patch does what you have suggested and now `preimage_tuple` returns a tuple, as it was intended and documented. Thanks for the input!",
    "created_at": "2010-11-10T15:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99888",
    "user": "https://github.com/novoselt"
}
```

I am convinced, the updated patch does what you have suggested and now `preimage_tuple` returns a tuple, as it was intended and documented. Thanks for the input!



---

archive/issue_comments_099889.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-10T15:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99889",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099890.json:
```json
{
    "body": "Of course, I meant that `preimage_cones` returns a tuple...",
    "created_at": "2010-11-10T15:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99890",
    "user": "https://github.com/novoselt"
}
```

Of course, I meant that `preimage_cones` returns a tuple...



---

archive/issue_comments_099891.json:
```json
{
    "body": "In the aforementioned blow-up example, I get now\n\n```\nsage: f.preimage_cones(f.image_cone(ray))\n(2-d cone of Rational polyhedral fan in 2-d lattice N, 2-d cone of Rational polyhedral fan in 2-d lattice N)\nsage: filter(lambda c:f.image_cone(c).is_equivalent(f.image_cone(ray)), flatten(domain_fan.cones()))\n[1-d cone of Rational polyhedral fan in 2-d lattice N, 2-d cone of Rational polyhedral fan in 2-d lattice N, 2-d cone of Rational polyhedral fan in 2-d lattice N]\nsage: ray in f.preimage_cones(f.image_cone(ray))  # should be True\nFalse\n```\nThe `preimage_cones` misses the 1-d cone that maps to (in the fan morphism sense) the single 2-d cone of the codomain fan.",
    "created_at": "2010-11-10T22:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99891",
    "user": "https://github.com/vbraun"
}
```

In the aforementioned blow-up example, I get now

```
sage: f.preimage_cones(f.image_cone(ray))
(2-d cone of Rational polyhedral fan in 2-d lattice N, 2-d cone of Rational polyhedral fan in 2-d lattice N)
sage: filter(lambda c:f.image_cone(c).is_equivalent(f.image_cone(ray)), flatten(domain_fan.cones()))
[1-d cone of Rational polyhedral fan in 2-d lattice N, 2-d cone of Rational polyhedral fan in 2-d lattice N, 2-d cone of Rational polyhedral fan in 2-d lattice N]
sage: ray in f.preimage_cones(f.image_cone(ray))  # should be True
False
```
The `preimage_cones` misses the 1-d cone that maps to (in the fan morphism sense) the single 2-d cone of the codomain fan.



---

archive/issue_comments_099892.json:
```json
{
    "body": "preimage_cones implemented",
    "created_at": "2010-11-10T22:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99892",
    "user": "https://github.com/novoselt"
}
```

preimage_cones implemented



---

archive/issue_comments_099893.json:
```json
{
    "body": "Attachment [trac_9972_add_fan_morphisms.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_add_fan_morphisms.patch) by @novoselt created at 2010-11-10 22:56:37\n\nGrrr... That was due to my optimization attempt without proper thinking. The new version uses the same cycle as the very first one (which was finding everything and even more), but requires equality of image cones. Should work now, the blow up example in the documentation is extended to include the preimage cones of the quadrant...",
    "created_at": "2010-11-10T22:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99893",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9972_add_fan_morphisms.patch](tarball://root/attachments/some-uuid/ticket9972/trac_9972_add_fan_morphisms.patch) by @novoselt created at 2010-11-10 22:56:37

Grrr... That was due to my optimization attempt without proper thinking. The new version uses the same cycle as the very first one (which was finding everything and even more), but requires equality of image cones. Should work now, the blow up example in the documentation is extended to include the preimage cones of the quadrant...



---

archive/issue_comments_099894.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-14T19:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99894",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099895.json:
```json
{
    "body": "Works great now!",
    "created_at": "2010-11-14T19:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99895",
    "user": "https://github.com/vbraun"
}
```

Works great now!



---

archive/issue_events_025189.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-20T10:05:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9971#event-25189"
}
```



---

archive/issue_comments_099896.json:
```json
{
    "body": "For the tracbot:\n\nApply trac_9972_add_cone_embedding.patch, trac_9972_improve_element_constructors.patch, trac_9972_remove_enhanced_cones_and_fans.patch, trac_9972_add_fan_morphisms.patch, trac_9972_fix_fan_warning.patch",
    "created_at": "2010-12-11T12:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99896",
    "user": "https://github.com/vbraun"
}
```

For the tracbot:

Apply trac_9972_add_cone_embedding.patch, trac_9972_improve_element_constructors.patch, trac_9972_remove_enhanced_cones_and_fans.patch, trac_9972_add_fan_morphisms.patch, trac_9972_fix_fan_warning.patch



---

archive/issue_events_025190.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-12T06:33:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9971#event-25190"
}
```



---

archive/issue_comments_099897.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9971#issuecomment-99897",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
