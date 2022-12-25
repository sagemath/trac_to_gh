# Issue 9713: Add toric Chow group

archive/issues_009713.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @novoselt\n\nThe toric Chow group is a useful version of a homology theory for toric varieties, especially for singular varieties. The attached patch provides support for computing the toric Chow group as well as elementary intersection theory.\n\nSee tracker bug at #9604 to for the patch queue/dependencies.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9713\n\n",
    "created_at": "2010-08-09T22:54:14Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Add toric Chow group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9713",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  @novoselt

The toric Chow group is a useful version of a homology theory for toric varieties, especially for singular varieties. The attached patch provides support for computing the toric Chow group as well as elementary intersection theory.

See tracker bug at #9604 to for the patch queue/dependencies.

Issue created by migration from https://trac.sagemath.org/ticket/9713





---

archive/issue_comments_094508.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-09-10T02:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94508",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_094509.json:
```json
{
    "body": "Volker, is this one ready for review? (It needs a little rebasement on top of new #9337.)",
    "created_at": "2010-09-10T02:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94509",
    "user": "https://github.com/novoselt"
}
```

Volker, is this one ready for review? (It needs a little rebasement on top of new #9337.)



---

archive/issue_comments_094510.json:
```json
{
    "body": "I think its ready, but you will probably soon find something to disagree on ;-)\n\nRebased patch is attached.",
    "created_at": "2010-09-10T08:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94510",
    "user": "https://github.com/vbraun"
}
```

I think its ready, but you will probably soon find something to disagree on ;-)

Rebased patch is attached.



---

archive/issue_comments_094511.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-10T08:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94511",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_094512.json:
```json
{
    "body": "Some preliminary comments:\n\n1. The new module is not completely documented yet, `sage -coverage` shows some issues.\n2. It seems to me that it is more common to use A<sup>k</sup> rather than A<sub>d-k</sub>, so I think it would be better to stick with it in the documentation.\n3. I'd prefer to drop \"The \" from \"The Chow cycle ...\" in `_repr_` as was done for divisor classes.\n4. It is not clear how to construct Chow cycles (except for those that correspond to cones).\n5. It is not clear what do numbers mean in the representation - i.e. how the basis is chosen?\n6. Regardless of the chosen basis, I think it would be more useful to see cycles as linear combination of cones (perhaps with cones represented by their `ambient_ray_indices`), without seeing those that got zero coefficients, of course. This issue is also relevant for divisor/cohomology classes and for divisor classes we do use coordinates in some basis, but I think that it makes more sense there, while here basis elements can be given by cycles of different dimension and having no separation between them makes it difficult to interpret the output.",
    "created_at": "2010-09-17T02:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94512",
    "user": "https://github.com/novoselt"
}
```

Some preliminary comments:

1. The new module is not completely documented yet, `sage -coverage` shows some issues.
2. It seems to me that it is more common to use A<sup>k</sup> rather than A<sub>d-k</sub>, so I think it would be better to stick with it in the documentation.
3. I'd prefer to drop "The " from "The Chow cycle ..." in `_repr_` as was done for divisor classes.
4. It is not clear how to construct Chow cycles (except for those that correspond to cones).
5. It is not clear what do numbers mean in the representation - i.e. how the basis is chosen?
6. Regardless of the chosen basis, I think it would be more useful to see cycles as linear combination of cones (perhaps with cones represented by their `ambient_ray_indices`), without seeing those that got zero coefficients, of course. This issue is also relevant for divisor/cohomology classes and for divisor classes we do use coordinates in some basis, but I think that it makes more sense there, while here basis elements can be given by cycles of different dimension and having no separation between them makes it difficult to interpret the output.



---

archive/issue_comments_094513.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-17T02:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94513",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094514.json:
```json
{
    "body": "I'll try to add the missing docstrings.\n\nI was intentionally using `A_k` and not `A^{d-k}` because this patch implements the Chow homology and not the cohomology. I'm not sure to which extend they are the same over singular/noncompact varieties over ZZ.\n\nI'm not entirely happy with the output either. But printing all the cones (even if we abbreviate them) will very quickly produce multi-line output. Right now, the output is essentially in a random basis corresponding to `cycle.parent().degree()`. \n\n```\nsage: cycle = X.Chow_group().gen(1)\nsage: cycle\nThe Chow cycle (0, 1, 0, 0, 0, 0)\nsage: cycle.parent().degree()\n(Z, Z x Z, Z x Z, Z)\nsage: cycle.lift()\n(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)\n```\n\nFor all practical purposes, the user should use `lift()` to get the coefficients of the cones in the given order `flatten(toric_variety.fan().cones())`. Would printing\n\n```\nChow cycle ((0,), (1, 0), (0, 0), (0,))\n```\n\nmake you more happy? Note that some methods (in particular, intersection with a divisor) need to change the cycle within its Chow class, so even \"simple\" cycles will  produce output where all coefficients are turned on. This is part of why I don't want to print the cone information explicitly.",
    "created_at": "2010-09-17T14:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94514",
    "user": "https://github.com/vbraun"
}
```

I'll try to add the missing docstrings.

I was intentionally using `A_k` and not `A^{d-k}` because this patch implements the Chow homology and not the cohomology. I'm not sure to which extend they are the same over singular/noncompact varieties over ZZ.

I'm not entirely happy with the output either. But printing all the cones (even if we abbreviate them) will very quickly produce multi-line output. Right now, the output is essentially in a random basis corresponding to `cycle.parent().degree()`. 

```
sage: cycle = X.Chow_group().gen(1)
sage: cycle
The Chow cycle (0, 1, 0, 0, 0, 0)
sage: cycle.parent().degree()
(Z, Z x Z, Z x Z, Z)
sage: cycle.lift()
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
```

For all practical purposes, the user should use `lift()` to get the coefficients of the cones in the given order `flatten(toric_variety.fan().cones())`. Would printing

```
Chow cycle ((0,), (1, 0), (0, 0), (0,))
```

make you more happy? Note that some methods (in particular, intersection with a divisor) need to change the cycle within its Chow class, so even "simple" cycles will  produce output where all coefficients are turned on. This is part of why I don't want to print the cone information explicitly.



---

archive/issue_comments_094515.json:
```json
{
    "body": "OK, let's stick to A_k.\n\n\n```\nChow cycle ((0,), (1, 0), (0, 0), (0,))\n```\n\nis a bit ugly ;-) Maybe to have it as a vector but separate degrees something like this may work:\n\n```\nChow cycle (0 | 1, 0 | 0, 0 | 0)\n```\n\n\nMy concern is that if I create the Chow cycle corresponding to a cone generated by rays 2 and 5, it would be nice to see it clearly in the output, say\n\n```\nChow cycle {2, 5}\n```\n\nwith combinations printed as\n\n```\nChow cycle 2*{2, 5} - 7*{1, 2, 3}\n```\n\nBut to have it nicely will require storing the original cone combination, since lift algorithm from a quotient element will involve a lot of cones, as you pointed out. I don't know if it worths the benefits. But it would be nice at least to have some markers between degrees.",
    "created_at": "2010-09-17T15:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94515",
    "user": "https://github.com/novoselt"
}
```

OK, let's stick to A_k.


```
Chow cycle ((0,), (1, 0), (0, 0), (0,))
```

is a bit ugly ;-) Maybe to have it as a vector but separate degrees something like this may work:

```
Chow cycle (0 | 1, 0 | 0, 0 | 0)
```


My concern is that if I create the Chow cycle corresponding to a cone generated by rays 2 and 5, it would be nice to see it clearly in the output, say

```
Chow cycle {2, 5}
```

with combinations printed as

```
Chow cycle 2*{2, 5} - 7*{1, 2, 3}
```

But to have it nicely will require storing the original cone combination, since lift algorithm from a quotient element will involve a lot of cones, as you pointed out. I don't know if it worths the benefits. But it would be nice at least to have some markers between degrees.



---

archive/issue_comments_094516.json:
```json
{
    "body": "I've changed the printing of Chow cycles to the following:\n\n```\nsage: X = toric_varieties.Cube_deformation(7)\nsage: A = X.Chow_group()\nsage: A.degree()\n(Z, C7, Z^5 x C2 x C2, Z)\nsage: a = sum( A.gen(i) * (i+1) for i in range(0,A.ngens()) )   # an element of A\nsage: a\n( 3 | 1 mod 7 | 0 mod 2, 1 mod 2, 4, 5, 6, 7, 8 | 9 )\n```\n\nI'll upload a new patch when #9972 is finished, as this patch will require some rediffing.",
    "created_at": "2010-10-06T18:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94516",
    "user": "https://github.com/vbraun"
}
```

I've changed the printing of Chow cycles to the following:

```
sage: X = toric_varieties.Cube_deformation(7)
sage: A = X.Chow_group()
sage: A.degree()
(Z, C7, Z^5 x C2 x C2, Z)
sage: a = sum( A.gen(i) * (i+1) for i in range(0,A.ngens()) )   # an element of A
sage: a
( 3 | 1 mod 7 | 0 mod 2, 1 mod 2, 4, 5, 6, 7, 8 | 9 )
```

I'll upload a new patch when #9972 is finished, as this patch will require some rediffing.



---

archive/issue_comments_094517.json:
```json
{
    "body": "Updated patch now applies cleanly. Ready for review...",
    "created_at": "2010-11-25T09:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94517",
    "user": "https://github.com/vbraun"
}
```

Updated patch now applies cleanly. Ready for review...



---

archive/issue_comments_094518.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-25T09:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94518",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094519.json:
```json
{
    "body": "I am a bit confused by the first example:\n\n```\nsage: A.degree()\n(Z, C7, Z^5 x C2 x C2, Z)\nsage: a = sum( A.gen(i) * (i+1) for i in range(0,A.ngens()) )   # an element of A\nsage: a\n( 3 | 1 mod 7 | 0 mod 2, 1 mod 2, 4, 5, 6, 7, 8 | 9 )\n```\n\nwith explanation \"The Chow group elements are printed as ( a0 | a1 mod 7 | a2 mod 2, a3 mod 2, a4, a5, a6, a7, a8 | a9 ), which denotes the element of the Chow group in the same basis as A.degree().\"\n\n`A.degree()` shows the third component as `Z^5 x C2 x C2`, yet it seems that elements put cyclic groups first, or maybe it is the reverse order (which would matter for several cyclic groups of different degrees).",
    "created_at": "2010-12-01T06:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94519",
    "user": "https://github.com/novoselt"
}
```

I am a bit confused by the first example:

```
sage: A.degree()
(Z, C7, Z^5 x C2 x C2, Z)
sage: a = sum( A.gen(i) * (i+1) for i in range(0,A.ngens()) )   # an element of A
sage: a
( 3 | 1 mod 7 | 0 mod 2, 1 mod 2, 4, 5, 6, 7, 8 | 9 )
```

with explanation "The Chow group elements are printed as ( a0 | a1 mod 7 | a2 mod 2, a3 mod 2, a4, a5, a6, a7, a8 | a9 ), which denotes the element of the Chow group in the same basis as A.degree()."

`A.degree()` shows the third component as `Z^5 x C2 x C2`, yet it seems that elements put cyclic groups first, or maybe it is the reverse order (which would matter for several cyclic groups of different degrees).



---

archive/issue_comments_094520.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-01T06:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94520",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094521.json:
```json
{
    "body": "A little optional note: it may be better to use `\\QQ` etc. rather than `\\mathbb{Q}`. I personally prefer the look of the last variant, but using standard macros brings more uniformity to the whole Sage documentation.",
    "created_at": "2010-12-01T16:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94521",
    "user": "https://github.com/novoselt"
}
```

A little optional note: it may be better to use `\QQ` etc. rather than `\mathbb{Q}`. I personally prefer the look of the last variant, but using standard macros brings more uniformity to the whole Sage documentation.



---

archive/issue_comments_094522.json:
```json
{
    "body": "Done. Now prints as\n\n```\nsage: A.degree()\n(Z, C7, C2 x C2 x Z^5, Z)\n```\n\nbecause thats how `FGP_Module` organizes its generators (first torsion, then free generators).",
    "created_at": "2010-12-01T19:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94522",
    "user": "https://github.com/vbraun"
}
```

Done. Now prints as

```
sage: A.degree()
(Z, C7, C2 x C2 x Z^5, Z)
```

because thats how `FGP_Module` organizes its generators (first torsion, then free generators).



---

archive/issue_comments_094523.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-01T19:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94523",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094524.json:
```json
{
    "body": "Just a minor point - there is a lot of reference to the Chow group of this and that, but it's apparently only the 'toric' Chow group, as noted at the beginning of the file.  Is it typical in the literature to conflate these notions - or is there a theorem that they are equivalent for toric varieties?  This should be clarified somehow, maybe even with an example of where they are not the same.  It would be unfortunate if they were *not* the same and someone later wanted to implement regular Chow groups!\n\nForgive me if the question is naive; I am fairly familiar with 'regular' Chow groups but hadn't encountered this (natural) version before.  If there is a foundational paper, it would be helpful to refer to that in the documentation as well; the Wikipedia page referenced doesn't actually refer to the 'toric' variety at all.",
    "created_at": "2010-12-02T16:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94524",
    "user": "https://github.com/kcrisman"
}
```

Just a minor point - there is a lot of reference to the Chow group of this and that, but it's apparently only the 'toric' Chow group, as noted at the beginning of the file.  Is it typical in the literature to conflate these notions - or is there a theorem that they are equivalent for toric varieties?  This should be clarified somehow, maybe even with an example of where they are not the same.  It would be unfortunate if they were *not* the same and someone later wanted to implement regular Chow groups!

Forgive me if the question is naive; I am fairly familiar with 'regular' Chow groups but hadn't encountered this (natural) version before.  If there is a foundational paper, it would be helpful to refer to that in the documentation as well; the Wikipedia page referenced doesn't actually refer to the 'toric' variety at all.



---

archive/issue_comments_094525.json:
```json
{
    "body": "The **toric** Chow cycles are the torus-invariant subvarieties only. Its a standard construction, see e.g. Fultons book. I don't think that there is any hope of it being the same as the full Chow group. But then the Chow group is in general huge and there is little hope of a complete description, and even less of a toric algorithm. I guess we could sprinkle some more \"toric_\" prefixes around in anticipation of someone inventing the requisite mathematics. But I think its clear enough...",
    "created_at": "2010-12-02T19:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94525",
    "user": "https://github.com/vbraun"
}
```

The **toric** Chow cycles are the torus-invariant subvarieties only. Its a standard construction, see e.g. Fultons book. I don't think that there is any hope of it being the same as the full Chow group. But then the Chow group is in general huge and there is little hope of a complete description, and even less of a toric algorithm. I guess we could sprinkle some more "toric_" prefixes around in anticipation of someone inventing the requisite mathematics. But I think its clear enough...



---

archive/issue_comments_094526.json:
```json
{
    "body": "Replying to [comment:12 vbraun]:\n> The **toric** Chow cycles are the torus-invariant subvarieties only.\nYes, I got that. \n> Its a standard construction, see e.g. Fultons book. I don't think that there is any hope of it being the same as the full Chow group. \nAh, when you say \"Fulton's book\" I first got out Intersection Theory :) but here it is.  Sections 3.3 and 3.4 seem quite relevant.  Page 63 says that Pic and the divisor piece of the Chow group can be computed only with what Fulton consistently calls \"T-Weil\" and \"T-Cartier\" divisors.  Further, the first proposition in Chapter 5 certainly seems to imply that this is in fact true in general for toric varieties.  The 'orbit closures' seem to be toric subvarieties by definition, and they generate the Chow group.  Am I reading this wrong?",
    "created_at": "2010-12-02T20:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94526",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:12 vbraun]:
> The **toric** Chow cycles are the torus-invariant subvarieties only.
Yes, I got that. 
> Its a standard construction, see e.g. Fultons book. I don't think that there is any hope of it being the same as the full Chow group. 
Ah, when you say "Fulton's book" I first got out Intersection Theory :) but here it is.  Sections 3.3 and 3.4 seem quite relevant.  Page 63 says that Pic and the divisor piece of the Chow group can be computed only with what Fulton consistently calls "T-Weil" and "T-Cartier" divisors.  Further, the first proposition in Chapter 5 certainly seems to imply that this is in fact true in general for toric varieties.  The 'orbit closures' seem to be toric subvarieties by definition, and they generate the Chow group.  Am I reading this wrong?



---

archive/issue_comments_094527.json:
```json
{
    "body": "The T-Weil divisor class group is the divisor part of the toric Chow group, and the T-Cartier divisor class group is the Pic (not the other way round).  And the orbit closures are the toric subvarieties. As usual, the divisor part of the Chow group is easy; the higher Chow groups become more complicated. Once you understand these, the Hodge conjecture follows easily ;-)",
    "created_at": "2010-12-02T22:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94527",
    "user": "https://github.com/vbraun"
}
```

The T-Weil divisor class group is the divisor part of the toric Chow group, and the T-Cartier divisor class group is the Pic (not the other way round).  And the orbit closures are the toric subvarieties. As usual, the divisor part of the Chow group is easy; the higher Chow groups become more complicated. Once you understand these, the Hodge conjecture follows easily ;-)



---

archive/issue_comments_094528.json:
```json
{
    "body": "Yes, I didn't intend to switch those but did by accident.   Sorry.\n\nMaybe I wasn't clear.  I'm saying that the propositions I reference seem to imply that the regular Chow groups ARE the toric Chow groups, because the free Abelian group on p-cycles turns out to be generated by the toric p-cycles in a toric subvariety.  But again, maybe I'm misreading them somehow - are there fewer relations?  But the definitions there seem to have the same notion of rational equivalence (?).  Unfortunately, I don't have it on me, it was at work I checked this out.\n\nOh, and don't call them higher Chow groups; that is something else again :) unless you want to start talking about the so-called Beilinson-Hodge conjecture",
    "created_at": "2010-12-03T03:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94528",
    "user": "https://github.com/kcrisman"
}
```

Yes, I didn't intend to switch those but did by accident.   Sorry.

Maybe I wasn't clear.  I'm saying that the propositions I reference seem to imply that the regular Chow groups ARE the toric Chow groups, because the free Abelian group on p-cycles turns out to be generated by the toric p-cycles in a toric subvariety.  But again, maybe I'm misreading them somehow - are there fewer relations?  But the definitions there seem to have the same notion of rational equivalence (?).  Unfortunately, I don't have it on me, it was at work I checked this out.

Oh, and don't call them higher Chow groups; that is something else again :) unless you want to start talking about the so-called Beilinson-Hodge conjecture



---

archive/issue_comments_094529.json:
```json
{
    "body": "Here it is, I called the fan Sigma rather than Delta:\n\n**Proposition** The Chow group A_k_(X) of an arbitrary toric variety X = X(Sigma) is generated by the classes of the orbit closures V(sigma) of the cones of dimension n-k of Sigma.\n\nSo yes, the patch does implement the \"honest Chow group\" with the exception that arbitrary subvarieties cannot be translated into their Chow cycles (I think).\n\nKarl, do you plan to review the patch completely? It is fine if no, I am going to do it in the near future. But if yes, it certainly will be great to have more people looking at our toric stuff ;-)",
    "created_at": "2010-12-03T04:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94529",
    "user": "https://github.com/novoselt"
}
```

Here it is, I called the fan Sigma rather than Delta:

**Proposition** The Chow group A_k_(X) of an arbitrary toric variety X = X(Sigma) is generated by the classes of the orbit closures V(sigma) of the cones of dimension n-k of Sigma.

So yes, the patch does implement the "honest Chow group" with the exception that arbitrary subvarieties cannot be translated into their Chow cycles (I think).

Karl, do you plan to review the patch completely? It is fine if no, I am going to do it in the near future. But if yes, it certainly will be great to have more people looking at our toric stuff ;-)



---

archive/issue_comments_094530.json:
```json
{
    "body": "Yes, I think that is the case - nicely summed up.\n\nNo, I am not at all an expert on toric varieties (though I wish I had learned more about them in graduate school now, they are so  concrete), so I can't help review.  The title of the ticket was just too good not to click on, and then I had this minor point which ballooned into a conversation.  Since of course lots of stuff IS toric that one might care about, I am glad you are doing it, but I'm sorry that it's above my pay grade for now.   If I had a sabbatical right now we might be talking ;)",
    "created_at": "2010-12-03T13:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94530",
    "user": "https://github.com/kcrisman"
}
```

Yes, I think that is the case - nicely summed up.

No, I am not at all an expert on toric varieties (though I wish I had learned more about them in graduate school now, they are so  concrete), so I can't help review.  The title of the ticket was just too good not to click on, and then I had this minor point which ballooned into a conversation.  Since of course lots of stuff IS toric that one might care about, I am glad you are doing it, but I'm sorry that it's above my pay grade for now.   If I had a sabbatical right now we might be talking ;)



---

archive/issue_comments_094531.json:
```json
{
    "body": "By \"higher\", I mean of course \"lower degree\" Chow groups. I'm pretty sure its correct in the module documentation :-)\n\nBut the free Abelian group of p-cycles is not generated by the toric p-cycles; The former is never finitely generated while the latter always is. In the case of divisors, the relations save you (the `Pic^0` is a point). But already for the curves part of the Chow group of a three-dimensional variety its not clear to me that the full Chow group is finitely generated.",
    "created_at": "2010-12-03T15:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94531",
    "user": "https://github.com/vbraun"
}
```

By "higher", I mean of course "lower degree" Chow groups. I'm pretty sure its correct in the module documentation :-)

But the free Abelian group of p-cycles is not generated by the toric p-cycles; The former is never finitely generated while the latter always is. In the case of divisors, the relations save you (the `Pic^0` is a point). But already for the curves part of the Chow group of a three-dimensional variety its not clear to me that the full Chow group is finitely generated.



---

archive/issue_comments_094532.json:
```json
{
    "body": "Well, Fulton claims that quotients are the same even though the starting free groups are very different ;-)\n\nSo I think we should include this proposition in the top of the module level documentation and comment that this allows us to worry only about orbit closures.",
    "created_at": "2010-12-03T16:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94532",
    "user": "https://github.com/novoselt"
}
```

Well, Fulton claims that quotients are the same even though the starting free groups are very different ;-)

So I think we should include this proposition in the top of the module level documentation and comment that this allows us to worry only about orbit closures.



---

archive/issue_comments_094533.json:
```json
{
    "body": "The relevant paper is Fulton/MacPherson/Sottile/Sturmfels: Intersection theory on spherical varieties. The bottom line is that, for any connected solvable linear algebraic group G acting on a scheme, the G-Chow group (made out of G-invariant cycles) is canonically the same as the ordinary Chow group. I think I knew this paper at one point, but then obviously forgot ;-)",
    "created_at": "2010-12-03T16:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94533",
    "user": "https://github.com/vbraun"
}
```

The relevant paper is Fulton/MacPherson/Sottile/Sturmfels: Intersection theory on spherical varieties. The bottom line is that, for any connected solvable linear algebraic group G acting on a scheme, the G-Chow group (made out of G-invariant cycles) is canonically the same as the ordinary Chow group. I think I knew this paper at one point, but then obviously forgot ;-)



---

archive/issue_comments_094534.json:
```json
{
    "body": "1. The discussed above fact that this patch implement the full Chow group should be reflected in module level documentation.\n   1. Documentation from `ChowCycle.__init__` should be moved to the class docstring, otherwise it is invisible.\n   2. Behaviour of `check=False` is strange for it: usually such an option omits validity checks assuming that user will take care of it. Here it seems to allow a different form of input. Is it inherited from the base class? If so, maybe it should be fixed there...\n   3. Line 170 misses the second \":\" in the end.\n   4. The first words of some docstrings have extra s'es, like \"Returns\" and \"Intersects\".\n   5. It would be nice if the documentation and example for `count_points` were expanded/clarified a little bit more. The phrase \"integral over the dual cohomology class\" does not make it clear what is the integrand and to what the cohomology class is dual. Is it the Chow cycle in both cases? The example starts with a divisor and then integrates the square of this divisor and counts points on the intersection of the Chow cycle of this divisor with the original divisor. How about starting with some Chow cycle with non-zero point count and then showing how to get a corresponding cohomology class and integrate it?\n   6. For `intersect_with_divisor` it would be nice to give a reference to the used algorithm (Fulton p.97?). I think also that `intersection_with_divisor` would be a better name, since the function returns the intersection rather than updates the original cycle. (I do realize now that the same consideration should have been applied to some methods that I have added...) By the way, this function has no input/output description. And perhaps `i = I_gamma.pop()` does the same thing as `i = iter(I_gamma).next()` in a little cleaner fashion. (It does alter the set, but it is not used anyway.) What exactly is tested by the long test with many zeros in this function? This function says that divisor must be Cartier, but it is not checked, is it intended? Am I right that it actually makes sense to use it with Q-Cartier divisors if the Chow group is also rational?\n   7. `Chow_cycle` method of toric divisors does not have a doctest and input/output description.\n   8. Line 394 misses closing quotes after True.\n\nI didn't go over actual Chow group code yet, but will do it. Soon ;-)",
    "created_at": "2010-12-05T04:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94534",
    "user": "https://github.com/novoselt"
}
```

1. The discussed above fact that this patch implement the full Chow group should be reflected in module level documentation.
   1. Documentation from `ChowCycle.__init__` should be moved to the class docstring, otherwise it is invisible.
   2. Behaviour of `check=False` is strange for it: usually such an option omits validity checks assuming that user will take care of it. Here it seems to allow a different form of input. Is it inherited from the base class? If so, maybe it should be fixed there...
   3. Line 170 misses the second ":" in the end.
   4. The first words of some docstrings have extra s'es, like "Returns" and "Intersects".
   5. It would be nice if the documentation and example for `count_points` were expanded/clarified a little bit more. The phrase "integral over the dual cohomology class" does not make it clear what is the integrand and to what the cohomology class is dual. Is it the Chow cycle in both cases? The example starts with a divisor and then integrates the square of this divisor and counts points on the intersection of the Chow cycle of this divisor with the original divisor. How about starting with some Chow cycle with non-zero point count and then showing how to get a corresponding cohomology class and integrate it?
   6. For `intersect_with_divisor` it would be nice to give a reference to the used algorithm (Fulton p.97?). I think also that `intersection_with_divisor` would be a better name, since the function returns the intersection rather than updates the original cycle. (I do realize now that the same consideration should have been applied to some methods that I have added...) By the way, this function has no input/output description. And perhaps `i = I_gamma.pop()` does the same thing as `i = iter(I_gamma).next()` in a little cleaner fashion. (It does alter the set, but it is not used anyway.) What exactly is tested by the long test with many zeros in this function? This function says that divisor must be Cartier, but it is not checked, is it intended? Am I right that it actually makes sense to use it with Q-Cartier divisors if the Chow group is also rational?
   7. `Chow_cycle` method of toric divisors does not have a doctest and input/output description.
   8. Line 394 misses closing quotes after True.

I didn't go over actual Chow group code yet, but will do it. Soon ;-)



---

archive/issue_comments_094535.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-05T04:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94535",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094536.json:
```json
{
    "body": "10. It is probably worth mentioning what is the point of `A(Cone(cone))` after `A(cone)`. I actually didn't even know that `Cone(cone)` works! Fortunately, it works as expected ;-)\n   11. In `_rational_equivalence_relations` I find it very difficult to understand the LaTeX expression, which does not get typeset in the documentation (since it is a private method), especially since it does not explain what is \"! over =\", what is `n_{\\rho, \\sigma}`, and how d, k, n, and p are related (I guess pairs of them are equal). I think that this description should be moved to some visible place (module documentation or `relation_gens`?) and there should be a reference to where it was taken from.\n   22. What is the purpose of the super call in `__eq__` for Chow groups? Do we want anything but a Chow group equal to a Chow group?\n   33. I think that `_cone_to_V` would be more efficient if it was implemented via a dictionary. I don't know how significant such a speed up will be in real computations, but I think it is worthwhile to do this change.\n   44. There is a note in `degree` method about smooth varieties: \"Using the cohomology ring instead of the Chow group will be much faster.\" I think that this is a very important point and it should be also mentioned in the module level documentation and in the Chow group method of toric varieties. (Perhaps with explanations of why this is the case.) Examples of this method are very nice! I'd remove the sentence \"The resulting fan is not the fan over a convex cube.\"\n   55. I think it would be more natural if `gens` without parameters returned the union of all `gens` of specified degree. Is it possible to implement? (I.e. is it possible to force the quotient module to use these generators? I definitely don't suggest \"just\" returning union of degree generators.)\n   66. For `relation_gens` wouldn't it be more natural to return elements of the covering module, i.e. lifts of the current output?\n   77. Line 979: you meant `== QQ`.\n   88. Would it make sense to derive `ChowGroup_degree_class` from some kind of a group rather than `SageObject`?\n\nThat's it for the current patch!",
    "created_at": "2010-12-07T06:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94536",
    "user": "https://github.com/novoselt"
}
```

10. It is probably worth mentioning what is the point of `A(Cone(cone))` after `A(cone)`. I actually didn't even know that `Cone(cone)` works! Fortunately, it works as expected ;-)
   11. In `_rational_equivalence_relations` I find it very difficult to understand the LaTeX expression, which does not get typeset in the documentation (since it is a private method), especially since it does not explain what is "! over =", what is `n_{\rho, \sigma}`, and how d, k, n, and p are related (I guess pairs of them are equal). I think that this description should be moved to some visible place (module documentation or `relation_gens`?) and there should be a reference to where it was taken from.
   22. What is the purpose of the super call in `__eq__` for Chow groups? Do we want anything but a Chow group equal to a Chow group?
   33. I think that `_cone_to_V` would be more efficient if it was implemented via a dictionary. I don't know how significant such a speed up will be in real computations, but I think it is worthwhile to do this change.
   44. There is a note in `degree` method about smooth varieties: "Using the cohomology ring instead of the Chow group will be much faster." I think that this is a very important point and it should be also mentioned in the module level documentation and in the Chow group method of toric varieties. (Perhaps with explanations of why this is the case.) Examples of this method are very nice! I'd remove the sentence "The resulting fan is not the fan over a convex cube."
   55. I think it would be more natural if `gens` without parameters returned the union of all `gens` of specified degree. Is it possible to implement? (I.e. is it possible to force the quotient module to use these generators? I definitely don't suggest "just" returning union of degree generators.)
   66. For `relation_gens` wouldn't it be more natural to return elements of the covering module, i.e. lifts of the current output?
   77. Line 979: you meant `== QQ`.
   88. Would it make sense to derive `ChowGroup_degree_class` from some kind of a group rather than `SageObject`?

That's it for the current patch!



---

archive/issue_comments_094537.json:
```json
{
    "body": "One more global question: did you think about having most of the functionality in `ChowGroup_degree_class` with Chow cycles being tuples of elements from all of them, i.e. without having the total quotient module? That would take care of some of the issues above (like gens vs. gens(degree=k)) and would avoid `flatten(fan.cones())` which I don't really like. It would also make sense to let fans determine indices of the cones in the lists in this case, i.e. `fan._index_of(cone)` would return the index of cone in `fan.cones(dim=cone.dim())`.",
    "created_at": "2010-12-07T16:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94537",
    "user": "https://github.com/novoselt"
}
```

One more global question: did you think about having most of the functionality in `ChowGroup_degree_class` with Chow cycles being tuples of elements from all of them, i.e. without having the total quotient module? That would take care of some of the issues above (like gens vs. gens(degree=k)) and would avoid `flatten(fan.cones())` which I don't really like. It would also make sense to let fans determine indices of the cones in the lists in this case, i.e. `fan._index_of(cone)` would return the index of cone in `fan.cones(dim=cone.dim())`.



---

archive/issue_comments_094538.json:
```json
{
    "body": "When I wrote the code I tried to make `gens()` return the union of the the fixed-degree generators but that did not work. I don't remember what exactly went wrong, but bad things happen if `gens()` is different from the generators that `FGP_Module` choses.\n\nI mostly added `ChowGroup_degree_class` so that the individual degree pieces can `_repr_()` themselves nicely. One could make them parents again with some coercion in the full Chow group, but that seems to be a big effort. I definitely want to allow mixed-degree Chow group elements, so we can't get rid of the whole Chow group.",
    "created_at": "2010-12-07T17:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94538",
    "user": "https://github.com/vbraun"
}
```

When I wrote the code I tried to make `gens()` return the union of the the fixed-degree generators but that did not work. I don't remember what exactly went wrong, but bad things happen if `gens()` is different from the generators that `FGP_Module` choses.

I mostly added `ChowGroup_degree_class` so that the individual degree pieces can `_repr_()` themselves nicely. One could make them parents again with some coercion in the full Chow group, but that seems to be a big effort. I definitely want to allow mixed-degree Chow group elements, so we can't get rid of the whole Chow group.



---

archive/issue_comments_094539.json:
```json
{
    "body": "A1. The discussed above fact that this patch implement the full Chow group should be reflected in module level documentation.\n\n    OK\n\n\nA2. Documentation from `ChowCycle.__init__` should be moved to the class docstring, otherwise it is invisible.\n\n    I've added a note to the `ChowCycle` class documentation that you are not supposed to manually construct them. The `__init__` docstring is hidden on purpose.\n\n\nA3. Behaviour of check=False is strange for it: usually such an option omits validity checks assuming that user will take care of it. Here it seems to allow a different form of input. Is it inherited from the base class? If so, maybe it should be fixed there...\n\n    Yes, it is inherited from `FGP_Element`. I tried to fix it there, but then I ended up trying to rewrite it for the new coercion model. And that attempt was quite unsuccessful, all of sage.modules is interrelated and you can't just change one class...\n\n\nA4. Line 170 misses the second `\":\"` in the end.\n\n    OK\n\n\nA5. The first words of some docstrings have extra `s`'es, like \"Returns\" and \"Intersects\".\n\n    OK\n\n\nA6. It would be nice if the documentation and example for `count_points` were expanded/clarified a little bit more. The  phrase `\"integral over the dual cohomology class\"` does not make it clear what is the integrand and to what the cohomology class is dual. Is it the Chow cycle in both cases? The example starts with a divisor and then integrates the square of this divisor and counts points on the intersection of the Chow cycle of this divisor with the original divisor. How about starting with some Chow cycle with non-zero point count and then showing how to get a corresponding cohomology class and integrate it?\n\n    There is no easy way to get the Poincare dual (In fact, it exists only if the variety is smooth). I've clarified the example a bit.\n\n\nA7. For `intersect_with_divisor` it would be nice to give a reference to the used algorithm (Fulton p.97?). I think also that `intersection_with_divisor` would be a better name, since the function returns the intersection rather than updates the original cycle. (I do realize now that the same consideration should have been applied to some methods that I have added...) By the way, this function has no input/output description. And perhaps `i = _gamma.pop()` does the same thing as `i = iter(I_gamma).next()` in a little cleaner fashion. (It does alter the set, but it is not used anyway.) What exactly is tested by the long test with many zeros in this function? This function says that divisor must be Cartier, but it is not checked, is it intended?  Am I right that it actually makes sense to use it with Q-Cartier divisors if the Chow group is also rational?\n\n    I renamed it to `intersection_with_divisor()` and expanded on the documentation which should now answer your questions...\n\n\n    In principle you are right with the Q-Cartier divisors, but in practice this will not work because multiplication QQ * QQ-Chow cycle is broken. The problem is that the parent does not adhere to the new coercion model. I could hack around it, but then this should really be fixed elsewhere.\n\n\nA8. `Chow_cycle` method of toric divisors does not have a doctest and input/output description.\n\n    OK\n\n\nA9. Line 394 misses closing quotes after True.\n\n    OK\n\n\nB1. It is probably worth mentioning what is the point of A(Cone(cone)) after A(cone). I actually didn't even know that Cone(cone) works! Fortunately, it works as expected ;-)\n\n    OK\n\n\nB2. In `_rational_equivalence_relations` I find it very difficult to understand the LaTeX expression, which does not get typeset in the documentation (since it is a private method), especially since it does not explain what is `\"! over =\"`, what is `n_{\\rho, \\sigma}`, and how d, k, n, and p are related (I guess pairs of them are  equal). I think that this description should be moved to some  visible place (module documentation or relation_gens?) and there should be a reference to where it was taken from.\n\n    I moved it to `relation_gens` and added more explanations.\n\n\nB3. What is the purpose of the super call in `__eq__` for Chow groups? Do we want anything but a Chow group equal to a Chow group?\n\n    Now it only returns `self is other`.\n\n\nB4. I think that `_cone_to_V` would be more efficient if it was implemented via a dictionary. I don't know how significant such a speed up will be in real computations, but I think it is worthwhile to do this change.\n\n    Its only constructing a unit vector. Surely the run time for intersection computations is dominated by the matrix normal form computations and not the construction of unit vectors?\n\n\nB5. There is a note in degree method about smooth varieties: \"Using the cohomology ring instead of the Chow group will be much faster.\" I think that this is a very important point and it should be also mentioned in the module level documentation and in the Chow group method of toric varieties. (Perhaps with explanations of why this is the case.) Examples of this method are very nice! I'd remove the sentence \"The resulting fan is not the fan over a convex cube.\"\n\n    OK\n\nB6. I think it would be more natural if gens without parameters returned the union of all gens of specified degree. Is it possible to implement? (I.e. is it possible to force the quotient module to use these generators? I definitely don't suggest \"just\" returning union of degree generators.)\n\n    I tried it but couldn't get it to work. The base `FGP_Module` has no provision to explicitly set the generators, and bad things happen if they are different from the internal normal form of the basis matrix.\n\n\nB7. For `relation_gens` wouldn't it be more natural to return elements of the covering module, i.e. lifts of the current output?\n\n    You can do that with `A.relations().gens()`. I added a note to `relation_gens`.\n\n\nB8. Line 979: you meant `== QQ`.\n \n    Yes, fixed.\n\n\nB9. Would it make sense to derive `ChowGroup_degree_class` from some kind of a group rather than `SageObject`?\n\n    Ideally they would be some other parents with coercions into the full (mixed-degree) Chow group. But then thats a lot of work for very little benefit. Not to mention that the base `FGP_Module` does not adhere to the new coercion model, so it'll be hackisch...",
    "created_at": "2010-12-15T21:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94539",
    "user": "https://github.com/vbraun"
}
```

A1. The discussed above fact that this patch implement the full Chow group should be reflected in module level documentation.

    OK


A2. Documentation from `ChowCycle.__init__` should be moved to the class docstring, otherwise it is invisible.

    I've added a note to the `ChowCycle` class documentation that you are not supposed to manually construct them. The `__init__` docstring is hidden on purpose.


A3. Behaviour of check=False is strange for it: usually such an option omits validity checks assuming that user will take care of it. Here it seems to allow a different form of input. Is it inherited from the base class? If so, maybe it should be fixed there...

    Yes, it is inherited from `FGP_Element`. I tried to fix it there, but then I ended up trying to rewrite it for the new coercion model. And that attempt was quite unsuccessful, all of sage.modules is interrelated and you can't just change one class...


A4. Line 170 misses the second `":"` in the end.

    OK


A5. The first words of some docstrings have extra `s`'es, like "Returns" and "Intersects".

    OK


A6. It would be nice if the documentation and example for `count_points` were expanded/clarified a little bit more. The  phrase `"integral over the dual cohomology class"` does not make it clear what is the integrand and to what the cohomology class is dual. Is it the Chow cycle in both cases? The example starts with a divisor and then integrates the square of this divisor and counts points on the intersection of the Chow cycle of this divisor with the original divisor. How about starting with some Chow cycle with non-zero point count and then showing how to get a corresponding cohomology class and integrate it?

    There is no easy way to get the Poincare dual (In fact, it exists only if the variety is smooth). I've clarified the example a bit.


A7. For `intersect_with_divisor` it would be nice to give a reference to the used algorithm (Fulton p.97?). I think also that `intersection_with_divisor` would be a better name, since the function returns the intersection rather than updates the original cycle. (I do realize now that the same consideration should have been applied to some methods that I have added...) By the way, this function has no input/output description. And perhaps `i = _gamma.pop()` does the same thing as `i = iter(I_gamma).next()` in a little cleaner fashion. (It does alter the set, but it is not used anyway.) What exactly is tested by the long test with many zeros in this function? This function says that divisor must be Cartier, but it is not checked, is it intended?  Am I right that it actually makes sense to use it with Q-Cartier divisors if the Chow group is also rational?

    I renamed it to `intersection_with_divisor()` and expanded on the documentation which should now answer your questions...


    In principle you are right with the Q-Cartier divisors, but in practice this will not work because multiplication QQ * QQ-Chow cycle is broken. The problem is that the parent does not adhere to the new coercion model. I could hack around it, but then this should really be fixed elsewhere.


A8. `Chow_cycle` method of toric divisors does not have a doctest and input/output description.

    OK


A9. Line 394 misses closing quotes after True.

    OK


B1. It is probably worth mentioning what is the point of A(Cone(cone)) after A(cone). I actually didn't even know that Cone(cone) works! Fortunately, it works as expected ;-)

    OK


B2. In `_rational_equivalence_relations` I find it very difficult to understand the LaTeX expression, which does not get typeset in the documentation (since it is a private method), especially since it does not explain what is `"! over ="`, what is `n_{\rho, \sigma}`, and how d, k, n, and p are related (I guess pairs of them are  equal). I think that this description should be moved to some  visible place (module documentation or relation_gens?) and there should be a reference to where it was taken from.

    I moved it to `relation_gens` and added more explanations.


B3. What is the purpose of the super call in `__eq__` for Chow groups? Do we want anything but a Chow group equal to a Chow group?

    Now it only returns `self is other`.


B4. I think that `_cone_to_V` would be more efficient if it was implemented via a dictionary. I don't know how significant such a speed up will be in real computations, but I think it is worthwhile to do this change.

    Its only constructing a unit vector. Surely the run time for intersection computations is dominated by the matrix normal form computations and not the construction of unit vectors?


B5. There is a note in degree method about smooth varieties: "Using the cohomology ring instead of the Chow group will be much faster." I think that this is a very important point and it should be also mentioned in the module level documentation and in the Chow group method of toric varieties. (Perhaps with explanations of why this is the case.) Examples of this method are very nice! I'd remove the sentence "The resulting fan is not the fan over a convex cube."

    OK

B6. I think it would be more natural if gens without parameters returned the union of all gens of specified degree. Is it possible to implement? (I.e. is it possible to force the quotient module to use these generators? I definitely don't suggest "just" returning union of degree generators.)

    I tried it but couldn't get it to work. The base `FGP_Module` has no provision to explicitly set the generators, and bad things happen if they are different from the internal normal form of the basis matrix.


B7. For `relation_gens` wouldn't it be more natural to return elements of the covering module, i.e. lifts of the current output?

    You can do that with `A.relations().gens()`. I added a note to `relation_gens`.


B8. Line 979: you meant `== QQ`.
 
    Yes, fixed.


B9. Would it make sense to derive `ChowGroup_degree_class` from some kind of a group rather than `SageObject`?

    Ideally they would be some other parents with coercions into the full (mixed-degree) Chow group. But then thats a lot of work for very little benefit. Not to mention that the base `FGP_Module` does not adhere to the new coercion model, so it'll be hackisch...



---

archive/issue_comments_094540.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-16T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94540",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094541.json:
```json
{
    "body": "For the buildbot: Depends on #9972 and #10325",
    "created_at": "2010-12-16T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94541",
    "user": "https://github.com/novoselt"
}
```

For the buildbot: Depends on #9972 and #10325



---

archive/issue_comments_094542.json:
```json
{
    "body": "Wait, I'm still meddling with the coercions...",
    "created_at": "2010-12-16T20:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94542",
    "user": "https://github.com/vbraun"
}
```

Wait, I'm still meddling with the coercions...



---

archive/issue_comments_094543.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-16T20:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94543",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094544.json:
```json
{
    "body": "Replying to [comment:25 vbraun]:\n\nA3. OK, let's hope it will get fixed eventually...\n\nA6. Am I right that it is integral OF the dual cohomology class, not OVER? That's how I interpret `integrate` method of toric varieties. Also it seems that we need completeness in addition to smoothness.\n\nA7. Let it be fixed elsewhere!\n\nB9. Ok, let it be as is.\n\nFresh comments:\n\n1. Why `get_degree` and not just `degree` for Chow cycles?\n2. What will `cohomology_class` of a Chow cycle produce in the case when there is no Poincare duality? I think this should be either explained in the documentation, or an exception should be raised varieties which are not smooth and complete.\n\nI have done some documentation prettification, feel free to fold it into your patch, if is still applies to your current version.",
    "created_at": "2010-12-16T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94544",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:25 vbraun]:

A3. OK, let's hope it will get fixed eventually...

A6. Am I right that it is integral OF the dual cohomology class, not OVER? That's how I interpret `integrate` method of toric varieties. Also it seems that we need completeness in addition to smoothness.

A7. Let it be fixed elsewhere!

B9. Ok, let it be as is.

Fresh comments:

1. Why `get_degree` and not just `degree` for Chow cycles?
2. What will `cohomology_class` of a Chow cycle produce in the case when there is no Poincare duality? I think this should be either explained in the documentation, or an exception should be raised varieties which are not smooth and complete.

I have done some documentation prettification, feel free to fold it into your patch, if is still applies to your current version.



---

archive/issue_comments_094545.json:
```json
{
    "body": "Attachment [trac_9713_reviewer.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_reviewer.patch) by @novoselt created at 2010-12-16 21:07:38",
    "created_at": "2010-12-16T21:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94545",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9713_reviewer.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_reviewer.patch) by @novoselt created at 2010-12-16 21:07:38



---

archive/issue_comments_094546.json:
```json
{
    "body": "A6. Yes, integral \"of\". Will fix it ;-)\n\n1. `ChowGroup.degree()` is probably a stupid name... ideas for better names? But I wanted to distinguish it from `ChowCycle.degree()`.\n\n2. There is no `ChowCycle.cohomology_class()` method nor any coercion to the `CohomologyRing`.",
    "created_at": "2010-12-16T22:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94546",
    "user": "https://github.com/vbraun"
}
```

A6. Yes, integral "of". Will fix it ;-)

1. `ChowGroup.degree()` is probably a stupid name... ideas for better names? But I wanted to distinguish it from `ChowCycle.degree()`.

2. There is no `ChowCycle.cohomology_class()` method nor any coercion to the `CohomologyRing`.



---

archive/issue_comments_094547.json:
```json
{
    "body": "Replying to [comment:29 vbraun]:\n> 1. `ChowGroup.degree()` is probably a stupid name... ideas for better names? But I wanted to distinguish it from `ChowCycle.degree()`.\n\nI meant that `ChowCycle.degree()` is better than `ChowCycle.get_degree()` defined on line 243. It seems fine to me, why don't you like it?\n \n> 2. There is no `ChowCycle.cohomology_class()` method nor any coercion to the `CohomologyRing`.\n\nWhat about line 444?..",
    "created_at": "2010-12-16T22:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94547",
    "user": "https://github.com/novoselt"
}
```

Replying to [comment:29 vbraun]:
> 1. `ChowGroup.degree()` is probably a stupid name... ideas for better names? But I wanted to distinguish it from `ChowCycle.degree()`.

I meant that `ChowCycle.degree()` is better than `ChowCycle.get_degree()` defined on line 243. It seems fine to me, why don't you like it?
 
> 2. There is no `ChowCycle.cohomology_class()` method nor any coercion to the `CohomologyRing`.

What about line 444?..



---

archive/issue_comments_094548.json:
```json
{
    "body": "Oops I totally forgot that I implemented the `cohomology_class()` method :-)\n\nI ported the bases Module and FGP_Module over to the new coercion model. The patch touches a lot of files but mostly small fixes, only `sage/modules/module.py` and `sage/modules/fg_pid/*py` are modified big time.\n\nFor the tracbot: Apply trac_9713_fix_cardinality.patch, trac_9713_fix_fg_pid.patch, trac_9713_toric_chow_group.patch",
    "created_at": "2010-12-17T19:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94548",
    "user": "https://github.com/vbraun"
}
```

Oops I totally forgot that I implemented the `cohomology_class()` method :-)

I ported the bases Module and FGP_Module over to the new coercion model. The patch touches a lot of files but mostly small fixes, only `sage/modules/module.py` and `sage/modules/fg_pid/*py` are modified big time.

For the tracbot: Apply trac_9713_fix_cardinality.patch, trac_9713_fix_fg_pid.patch, trac_9713_toric_chow_group.patch



---

archive/issue_comments_094549.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-20T11:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94549",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094550.json:
```json
{
    "body": "I am about to create a new ticket whose purpose is to implement the new parent and coercion framework not only for the base class `sage.modules.module.Module`, but also for the most derived classes. In that regard, it goes beyond what is done in the patches here.\n\nMy to-be-created ticket will leave the `FGP_*` stuff almost unchanged. I suggest to include that to-be-created ticket as a new dependency (mentioning it in #9604 as well), so that the ticket here can concentrate on its \"real\" purpose, which is not coercion but toric Chow group.\n\nThen I would also provide a replacement of trac_9713_toric_chow_group.patch relative to the to-be-created ticket.\n\nA few words on trac_9713_toric_chow_group.patch: The `element_class` attribute of Parent is in fact a *lazy* attribute, that takes another attribute `Element` and mixes it with some category stuff before it turns `element_class` into an actual attribute. Hence, one should *not* directly set `element_class` (which is done in the patch), but should provide an attribute `Element` instead.\n\nMy to-be-created patch would actually preserve the `_element_class` (leading underscore) method, since it chooses the right element class and is already implemented for all sub-classes. But I would call it in the `__init__` method of the base class `sage.modules.module.Module` and assign its output to the `Element` attribute. In that way, it is most easy to implement the lazy `element_class` (no leading underscore) attribute as one is supposed to.\n\nAlso, the `__call__` method of fgp morphisms should probably be replaces by `_call_`, `_call_with_args` and perhaps `pushforward` (likely depending on #10496).\n\n\nBest regards, Simon",
    "created_at": "2010-12-22T08:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94550",
    "user": "https://github.com/simon-king-jena"
}
```

I am about to create a new ticket whose purpose is to implement the new parent and coercion framework not only for the base class `sage.modules.module.Module`, but also for the most derived classes. In that regard, it goes beyond what is done in the patches here.

My to-be-created ticket will leave the `FGP_*` stuff almost unchanged. I suggest to include that to-be-created ticket as a new dependency (mentioning it in #9604 as well), so that the ticket here can concentrate on its "real" purpose, which is not coercion but toric Chow group.

Then I would also provide a replacement of trac_9713_toric_chow_group.patch relative to the to-be-created ticket.

A few words on trac_9713_toric_chow_group.patch: The `element_class` attribute of Parent is in fact a *lazy* attribute, that takes another attribute `Element` and mixes it with some category stuff before it turns `element_class` into an actual attribute. Hence, one should *not* directly set `element_class` (which is done in the patch), but should provide an attribute `Element` instead.

My to-be-created patch would actually preserve the `_element_class` (leading underscore) method, since it chooses the right element class and is already implemented for all sub-classes. But I would call it in the `__init__` method of the base class `sage.modules.module.Module` and assign its output to the `Element` attribute. In that way, it is most easy to implement the lazy `element_class` (no leading underscore) attribute as one is supposed to.

Also, the `__call__` method of fgp morphisms should probably be replaces by `_call_`, `_call_with_args` and perhaps `pushforward` (likely depending on #10496).


Best regards, Simon



---

archive/issue_comments_094551.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-22T08:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94551",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094552.json:
```json
{
    "body": "Attachment [trac_9713_fix_fg_pid_relative_10513.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid_relative_10513.patch) by @simon-king-jena created at 2010-12-22 09:27:59\n\nRebases trac_9713_fix_fg_pid.patch relative to #10513",
    "created_at": "2010-12-22T09:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94552",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_9713_fix_fg_pid_relative_10513.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid_relative_10513.patch) by @simon-king-jena created at 2010-12-22 09:27:59

Rebases trac_9713_fix_fg_pid.patch relative to #10513



---

archive/issue_comments_094553.json:
```json
{
    "body": "I just attached a version of trac_9713_fix_fg_pid.patch that is based on #10513. I'll add #10513 to the dependencies that are listed in #9604.\n\nI can not vouch for any passing doc tests, as I merely rebased the patch.",
    "created_at": "2010-12-22T09:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94553",
    "user": "https://github.com/simon-king-jena"
}
```

I just attached a version of trac_9713_fix_fg_pid.patch that is based on #10513. I'll add #10513 to the dependencies that are listed in #9604.

I can not vouch for any passing doc tests, as I merely rebased the patch.



---

archive/issue_comments_094554.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-22T09:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94554",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094555.json:
```json
{
    "body": "Sorry! Since #10513 needs much work, I should not make it a dependency for the ticket here. So, please disregard the patch trac_9713_fix_fg_pid_relative_10513.patch!\n\nI understood that you just want to implement the parent and category framework to an extent that allows you to implement the toric Chow group. Right? Then I think my remark on `_call_` and `pushforward` and `_call_with_args` of morphisms should be moved to a different ticket.\n\nSo, it remains \"needs review\".\n\nCheers,\nSimon",
    "created_at": "2010-12-22T13:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94555",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry! Since #10513 needs much work, I should not make it a dependency for the ticket here. So, please disregard the patch trac_9713_fix_fg_pid_relative_10513.patch!

I understood that you just want to implement the parent and category framework to an extent that allows you to implement the toric Chow group. Right? Then I think my remark on `_call_` and `pushforward` and `_call_with_args` of morphisms should be moved to a different ticket.

So, it remains "needs review".

Cheers,
Simon



---

archive/issue_comments_094556.json:
```json
{
    "body": "Just to make it clear: so far this ticket depends on #9972 and #10325 (both positively reviewed) on top of sage-4.6.1.alpha3, nothing else.",
    "created_at": "2010-12-22T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94556",
    "user": "https://github.com/novoselt"
}
```

Just to make it clear: so far this ticket depends on #9972 and #10325 (both positively reviewed) on top of sage-4.6.1.alpha3, nothing else.



---

archive/issue_comments_094557.json:
```json
{
    "body": "Replying to [comment:36 novoselt]:\n> Just to make it clear: so far this ticket depends on #9972 and #10325 (both positively reviewed) on top of sage-4.6.1.alpha3, nothing else.\n\nThank you for the clarification! I thought I had to apply *all* patches mentioned at #9604.",
    "created_at": "2010-12-22T17:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94557",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:36 novoselt]:
> Just to make it clear: so far this ticket depends on #9972 and #10325 (both positively reviewed) on top of sage-4.6.1.alpha3, nothing else.

Thank you for the clarification! I thought I had to apply *all* patches mentioned at #9604.



---

archive/issue_comments_094558.json:
```json
{
    "body": "Attachment [trac_9713_fix_fg_pid.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid.patch) by @vbraun created at 2010-12-22 18:16:24\n\nRenamed element_class -> Element",
    "created_at": "2010-12-22T18:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94558",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9713_fix_fg_pid.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid.patch) by @vbraun created at 2010-12-22 18:16:24

Renamed element_class -> Element



---

archive/issue_comments_094559.json:
```json
{
    "body": "I've renamed `element_class` -> `Element` as per Simon's comment, thanks!\n\nMaybe Simon would be interested in reviewing the first two patches (`trac_9713_fix_cardinality.patch`, `trac_9713_fix_fg_pid.patch`) and Andrey the ` trac_9713_toric_chow_group.patch`? :-) Then we should make it into Sage-4.6.2...",
    "created_at": "2010-12-22T18:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94559",
    "user": "https://github.com/vbraun"
}
```

I've renamed `element_class` -> `Element` as per Simon's comment, thanks!

Maybe Simon would be interested in reviewing the first two patches (`trac_9713_fix_cardinality.patch`, `trac_9713_fix_fg_pid.patch`) and Andrey the ` trac_9713_toric_chow_group.patch`? :-) Then we should make it into Sage-4.6.2...



---

archive/issue_comments_094560.json:
```json
{
    "body": "Replying to [comment:38 vbraun]:\n> I've renamed `element_class` -> `Element` as per Simon's comment, thanks!\n> \n> Maybe Simon would be interested in reviewing the first two patches (`trac_9713_fix_cardinality.patch`, `trac_9713_fix_fg_pid.patch`) and Andrey the ` trac_9713_toric_chow_group.patch`? :-) Then we should make it into Sage-4.6.2...\n\nIn what order should the patches be applied? I first applied the patches from #9972 and #10325, then proceeded with `trac_9713_toric_chow_group.patch`, but one hunk of `trac_9713_fix_fg_pid.patch` failed.",
    "created_at": "2010-12-24T11:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94560",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:38 vbraun]:
> I've renamed `element_class` -> `Element` as per Simon's comment, thanks!
> 
> Maybe Simon would be interested in reviewing the first two patches (`trac_9713_fix_cardinality.patch`, `trac_9713_fix_fg_pid.patch`) and Andrey the ` trac_9713_toric_chow_group.patch`? :-) Then we should make it into Sage-4.6.2...

In what order should the patches be applied? I first applied the patches from #9972 and #10325, then proceeded with `trac_9713_toric_chow_group.patch`, but one hunk of `trac_9713_fix_fg_pid.patch` failed.



---

archive/issue_comments_094561.json:
```json
{
    "body": "See also comment 31:\n\n* `trac_9713_fix_cardinality.patch`\n* `trac_9713_fix_fg_pid.patch`\n* `trac_9713_toric_chow_group.patch`",
    "created_at": "2010-12-24T14:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94561",
    "user": "https://github.com/vbraun"
}
```

See also comment 31:

* `trac_9713_fix_cardinality.patch`
* `trac_9713_fix_fg_pid.patch`
* `trac_9713_toric_chow_group.patch`



---

archive/issue_comments_094562.json:
```json
{
    "body": "Replying to [comment:40 vbraun]:\n> See also comment 31:\n> \n>  * `trac_9713_fix_cardinality.patch`\n>  * `trac_9713_fix_fg_pid.patch`\n\nNo, when I apply `trac_9713_fix_fg_pid.patch`, one out of 17 hunks fails, namely:\n\n```\n--- fgp_module.py\n+++ fgp_module.py\n@@ -539,7 +578,8 @@\n         \"\"\"\n         return other.is_submodule(self)\n\n-    def __call__(self, x, check=True):\n+\n+    def _element_constructor_(self, x, check=True):\n         \"\"\"\n         INPUT:\n\n```\n\n\nCheers,\nSimon",
    "created_at": "2010-12-24T20:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94562",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:40 vbraun]:
> See also comment 31:
> 
>  * `trac_9713_fix_cardinality.patch`
>  * `trac_9713_fix_fg_pid.patch`

No, when I apply `trac_9713_fix_fg_pid.patch`, one out of 17 hunks fails, namely:

```
--- fgp_module.py
+++ fgp_module.py
@@ -539,7 +578,8 @@
         """
         return other.is_submodule(self)

-    def __call__(self, x, check=True):
+
+    def _element_constructor_(self, x, check=True):
         """
         INPUT:

```


Cheers,
Simon



---

archive/issue_comments_094563.json:
```json
{
    "body": "Works for me, which sage version are you trying to apply it to?\n\n```\n/home/vbraun/opt/sage-4.6.1.rc0/devel/sage\n[vbraun@volker-desktop sage]$ hg qpush -a\napplying trac_9972_add_cone_embedding.patch\napplying trac_9972_improve_element_constructors.patch\napplying trac_9972_remove_enhanced_cones_and_fans.patch\napplying trac_9972_add_fan_morphisms.patch\napplying trac_9972_fix_fan_warning.patch\napplying trac_10325_make_toric_CohomologyRing_unique.patch\napplying trac_9713_fix_cardinality.patch\napplying trac_9713_fix_fg_pid.patch\napplying trac_9713_toric_chow_group.patch\nnow at: trac_9713_toric_chow_group.patch\n```\n",
    "created_at": "2010-12-24T20:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94563",
    "user": "https://github.com/vbraun"
}
```

Works for me, which sage version are you trying to apply it to?

```
/home/vbraun/opt/sage-4.6.1.rc0/devel/sage
[vbraun@volker-desktop sage]$ hg qpush -a
applying trac_9972_add_cone_embedding.patch
applying trac_9972_improve_element_constructors.patch
applying trac_9972_remove_enhanced_cones_and_fans.patch
applying trac_9972_add_fan_morphisms.patch
applying trac_9972_fix_fan_warning.patch
applying trac_10325_make_toric_CohomologyRing_unique.patch
applying trac_9713_fix_cardinality.patch
applying trac_9713_fix_fg_pid.patch
applying trac_9713_toric_chow_group.patch
now at: trac_9713_toric_chow_group.patch
```




---

archive/issue_comments_094564.json:
```json
{
    "body": "Replying to [comment:41 SimonKing]:\n> No, when I apply `trac_9713_fix_fg_pid.patch`, one out of 17 hunks fails\n\nIt seems to me that this hunk has a totally wrong line number. The line\n\n```\n    def __call__(self, x, check=True):\n```\n\nis line number 446 in `fgp_module.py`.",
    "created_at": "2010-12-24T20:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94564",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:41 SimonKing]:
> No, when I apply `trac_9713_fix_fg_pid.patch`, one out of 17 hunks fails

It seems to me that this hunk has a totally wrong line number. The line

```
    def __call__(self, x, check=True):
```

is line number 446 in `fgp_module.py`.



---

archive/issue_comments_094565.json:
```json
{
    "body": "No the `__call__` in `FGP_Module` is at line 542. Maybe you forgot to revert something in your sage library?\n\n```\n[vbraun@volker-desktop sage]$ hg qpop -a\nno patches applied\n[vbraun@volker-desktop sage]$ head -542 sage/modules/fg_pid/fgp_module.py | tail -1\n    def __call__(self, x, check=True):\n[vbraun@volker-desktop sage]$ \n```\n",
    "created_at": "2010-12-24T20:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94565",
    "user": "https://github.com/vbraun"
}
```

No the `__call__` in `FGP_Module` is at line 542. Maybe you forgot to revert something in your sage library?

```
[vbraun@volker-desktop sage]$ hg qpop -a
no patches applied
[vbraun@volker-desktop sage]$ head -542 sage/modules/fg_pid/fgp_module.py | tail -1
    def __call__(self, x, check=True):
[vbraun@volker-desktop sage]$ 
```




---

archive/issue_comments_094566.json:
```json
{
    "body": "Replying to [comment:42 vbraun]:\n> Works for me, which sage version are you trying to apply it to?\n\nsage-4.6\n\nSo, perhaps I should try to upgrade to sage-4.6.1.alpha3 first.\n\nIs there an easy way to use `sage -upgrade` for a development version?",
    "created_at": "2010-12-24T20:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94566",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:42 vbraun]:
> Works for me, which sage version are you trying to apply it to?

sage-4.6

So, perhaps I should try to upgrade to sage-4.6.1.alpha3 first.

Is there an easy way to use `sage -upgrade` for a development version?



---

archive/issue_comments_094567.json:
```json
{
    "body": "I usually build from scratch, but I believe the following should work:\n\n```\nsage -upgrade http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/\n```\n",
    "created_at": "2010-12-24T20:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94567",
    "user": "https://github.com/vbraun"
}
```

I usually build from scratch, but I believe the following should work:

```
sage -upgrade http://sage.math.washington.edu/home/release/sage-4.6.1.rc0/sage-4.6.1.rc0/
```




---

archive/issue_comments_094568.json:
```json
{
    "body": "Replying to [comment:46 vbraun]:\n> I usually build from scratch, but I believe the following should work:\n\nThanks, it did kind of work. At some point the process got stuck, but when I then did `make` in `SAGE_ROOT`, the upgrade did succeed (at least so it seems).\n\nThe patches apply. I don't know if I will be able to do reviewing any time soon, since currently I only have remote access to my computer via rather slow internet (237 kB/s).\n\nCheers, Simon",
    "created_at": "2010-12-25T09:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94568",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:46 vbraun]:
> I usually build from scratch, but I believe the following should work:

Thanks, it did kind of work. At some point the process got stuck, but when I then did `make` in `SAGE_ROOT`, the upgrade did succeed (at least so it seems).

The patches apply. I don't know if I will be able to do reviewing any time soon, since currently I only have remote access to my computer via rather slow internet (237 kB/s).

Cheers, Simon



---

archive/issue_comments_094569.json:
```json
{
    "body": "I applied the patches on top of `sage-4.6.1.alpha3`, and the good news is that all tests pass.\n\nHowever, I have some criticism concerning `trac_9713_fix_fg_pid.patch`.\n\nIn several cases I see things like\n\n```\n        return self.parent().Element(self.parent(), self._x - other._x)\n```\n\n\nThat's not how the attribute `Element` is supposed to be used. As far as I know, the story is like this:\n\n* One provides an attribute `Element`, which is supposed to be a class.\n\n* `Parent.element_class` is a so-called lazy attribute. That's to say, if one does `self.element_class` then the *method* `self.element_class()` is called, which computes a *new* class out of `self.Element` and `self.category()`, assigns this new class to an actual (not lazy) attribute `self.element_class`, and returns that new class.\n\n* When one requests `self.element_class` is called the next time then it is already a usual attribute, which is of course much faster than calling a method.\n\nHence, you should define `self.Element`. But then you should do\n\n```\n        P = self.parent()\n        return P.element_class(P, self._x - other._x) \n```\n\nsince `P.element_class` (in contrast to `P.Element`) also inherits stuff from the category. Note that additionally the code snipped spares a little time compared with your patch since `self.parent()` is called only once instead of twice.\n\nAs I mentioned, my bandwith is a bit restricted at the moment. So, this post might be incomplete, it is just what I found by a little reading of the patch.",
    "created_at": "2010-12-25T21:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94569",
    "user": "https://github.com/simon-king-jena"
}
```

I applied the patches on top of `sage-4.6.1.alpha3`, and the good news is that all tests pass.

However, I have some criticism concerning `trac_9713_fix_fg_pid.patch`.

In several cases I see things like

```
        return self.parent().Element(self.parent(), self._x - other._x)
```


That's not how the attribute `Element` is supposed to be used. As far as I know, the story is like this:

* One provides an attribute `Element`, which is supposed to be a class.

* `Parent.element_class` is a so-called lazy attribute. That's to say, if one does `self.element_class` then the *method* `self.element_class()` is called, which computes a *new* class out of `self.Element` and `self.category()`, assigns this new class to an actual (not lazy) attribute `self.element_class`, and returns that new class.

* When one requests `self.element_class` is called the next time then it is already a usual attribute, which is of course much faster than calling a method.

Hence, you should define `self.Element`. But then you should do

```
        P = self.parent()
        return P.element_class(P, self._x - other._x) 
```

since `P.element_class` (in contrast to `P.Element`) also inherits stuff from the category. Note that additionally the code snipped spares a little time compared with your patch since `self.parent()` is called only once instead of twice.

As I mentioned, my bandwith is a bit restricted at the moment. So, this post might be incomplete, it is just what I found by a little reading of the patch.



---

archive/issue_comments_094570.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-25T21:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94570",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094571.json:
```json
{
    "body": "Attachment [trac_9713_fix_fg_pid_reviewer.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid_reviewer.patch) by @simon-king-jena created at 2010-12-27 16:35:30\n\nApply after  trac_9713_fix_fg_pid.patch: Element vs. element_class; indirect doctests",
    "created_at": "2010-12-27T16:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94571",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_9713_fix_fg_pid_reviewer.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid_reviewer.patch) by @simon-king-jena created at 2010-12-27 16:35:30

Apply after  trac_9713_fix_fg_pid.patch: Element vs. element_class; indirect doctests



---

archive/issue_comments_094572.json:
```json
{
    "body": "Hi Volker and Andrey!\n\nReplying to [comment:38 vbraun]:\n> I've renamed `element_class` -> `Element` as per Simon's comment, thanks!\n\nAs I've pointed out in my previous post, one should *define* `self.Element`, but then the actual element class is `self.element_class`. This is taken care of in my reviewer patch, `trac_9713_fix_fg_pid_reviewer.patch`. Some doctests needed to be modified accordingly. The reviewer patch also raises the doctest coverage of `sage.modules.fg_pid` to 100% (some indirect tests had not been marked as such).\n\n> Maybe Simon would be interested in reviewing the first two patches (`trac_9713_fix_cardinality.patch`, `trac_9713_fix_fg_pid.patch`) and Andrey the ` trac_9713_toric_chow_group.patch`?\n\nI give `trac_9713_fix_cardinality.patch` and `trac_9713_fix_fg_pid.patch` (modulo my reviewer patch) a positive review. Of course, we all know that it does not provide a full implementation of the new parent and coercion model for modules; after all, that is not the purpose of this ticket. But apparently it is enough for implementing the toric chow group. So, I suggest to build a full implementation of coercion for modules on top of these patches.\n\n> Then we should make it into Sage-4.6.2...\n\nMy job is done. Andrey, your turn... :)",
    "created_at": "2010-12-27T16:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94572",
    "user": "https://github.com/simon-king-jena"
}
```

Hi Volker and Andrey!

Replying to [comment:38 vbraun]:
> I've renamed `element_class` -> `Element` as per Simon's comment, thanks!

As I've pointed out in my previous post, one should *define* `self.Element`, but then the actual element class is `self.element_class`. This is taken care of in my reviewer patch, `trac_9713_fix_fg_pid_reviewer.patch`. Some doctests needed to be modified accordingly. The reviewer patch also raises the doctest coverage of `sage.modules.fg_pid` to 100% (some indirect tests had not been marked as such).

> Maybe Simon would be interested in reviewing the first two patches (`trac_9713_fix_cardinality.patch`, `trac_9713_fix_fg_pid.patch`) and Andrey the ` trac_9713_toric_chow_group.patch`?

I give `trac_9713_fix_cardinality.patch` and `trac_9713_fix_fg_pid.patch` (modulo my reviewer patch) a positive review. Of course, we all know that it does not provide a full implementation of the new parent and coercion model for modules; after all, that is not the purpose of this ticket. But apparently it is enough for implementing the toric chow group. So, I suggest to build a full implementation of coercion for modules on top of these patches.

> Then we should make it into Sage-4.6.2...

My job is done. Andrey, your turn... :)



---

archive/issue_comments_094573.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-27T16:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94573",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094574.json:
```json
{
    "body": "Thank you for the `element_class` explanation! I'm happy with the reviewer patch. I've updated the remaining (and final) patch to also use `element_class` in the Chow group, so we should be all set. Andrey, can you set this ticket to positive review?\n\nFor the tracbot: Apply trac_9713_fix_cardinality.patch, trac_9713_fix_fg_pid.patch, trac_9713_fix_fg_pid_reviewer.patch, trac_9713_toric_chow_group.patch",
    "created_at": "2010-12-27T19:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94574",
    "user": "https://github.com/vbraun"
}
```

Thank you for the `element_class` explanation! I'm happy with the reviewer patch. I've updated the remaining (and final) patch to also use `element_class` in the Chow group, so we should be all set. Andrey, can you set this ticket to positive review?

For the tracbot: Apply trac_9713_fix_cardinality.patch, trac_9713_fix_fg_pid.patch, trac_9713_fix_fg_pid_reviewer.patch, trac_9713_toric_chow_group.patch



---

archive/issue_comments_094575.json:
```json
{
    "body": "Simon, thanks a lot for your help!\n\nVolker, shouldn't variety be complete for Poincare duality in `cohomology_class`?\n\nIn its documentation \"will be not always match intersection numbers.\" should be \"will not always match intersection numbers.\" (or \"may not match intersection numbers.\")\n\nOtherwise tests pass and all issues above seem to be resolved!",
    "created_at": "2011-01-12T00:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94575",
    "user": "https://github.com/novoselt"
}
```

Simon, thanks a lot for your help!

Volker, shouldn't variety be complete for Poincare duality in `cohomology_class`?

In its documentation "will be not always match intersection numbers." should be "will not always match intersection numbers." (or "may not match intersection numbers.")

Otherwise tests pass and all issues above seem to be resolved!



---

archive/issue_comments_094576.json:
```json
{
    "body": "So - do we need completeness and a check for it?-)",
    "created_at": "2011-01-14T01:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94576",
    "user": "https://github.com/novoselt"
}
```

So - do we need completeness and a check for it?-)



---

archive/issue_comments_094577.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-01-14T01:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94577",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_094578.json:
```json
{
    "body": "I've extended the docstring to clarify when `cohomology_class()` is Poincare dual and when not. The added example should also clarify things.",
    "created_at": "2011-01-24T19:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94578",
    "user": "https://github.com/vbraun"
}
```

I've extended the docstring to clarify when `cohomology_class()` is Poincare dual and when not. The added example should also clarify things.



---

archive/issue_comments_094579.json:
```json
{
    "body": "Can we rephrase \"We can associate a degree-`d` polynomial in the homogeneous coordinates by taking the product of the variables corresponding to the rays.\" to something else? My concern is that these variables may have different weight and, in general, there is no Z-grading on a toric variety. Maybe \"We can associate to it the product of homogeneous coordinates corresponding to its rays.\"?\n\nRight before OUTPUT \"will be not always\" should be \"will not always\"",
    "created_at": "2011-01-24T20:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94579",
    "user": "https://github.com/novoselt"
}
```

Can we rephrase "We can associate a degree-`d` polynomial in the homogeneous coordinates by taking the product of the variables corresponding to the rays." to something else? My concern is that these variables may have different weight and, in general, there is no Z-grading on a toric variety. Maybe "We can associate to it the product of homogeneous coordinates corresponding to its rays."?

Right before OUTPUT "will be not always" should be "will not always"



---

archive/issue_comments_094580.json:
```json
{
    "body": "Ok I've rewritten it to be more careful with \"degrees\".",
    "created_at": "2011-01-24T21:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94580",
    "user": "https://github.com/vbraun"
}
```

Ok I've rewritten it to be more careful with "degrees".



---

archive/issue_comments_094581.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-24T22:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94581",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_094582.json:
```json
{
    "body": "Hooray!",
    "created_at": "2011-01-24T22:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94582",
    "user": "https://github.com/novoselt"
}
```

Hooray!



---

archive/issue_comments_094583.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-24T22:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94583",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094584.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-26T10:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94584",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094585.json:
```json
{
    "body": "Needs to be rebased to sage-4.6.2.alpha2",
    "created_at": "2011-01-26T10:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94585",
    "user": "https://github.com/jdemeyer"
}
```

Needs to be rebased to sage-4.6.2.alpha2



---

archive/issue_comments_094586.json:
```json
{
    "body": "Rebased against sage-4.6.2.alpha2",
    "created_at": "2011-01-26T14:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94586",
    "user": "https://github.com/vbraun"
}
```

Rebased against sage-4.6.2.alpha2



---

archive/issue_comments_094587.json:
```json
{
    "body": "Attachment [trac_9713_fix_cardinality.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_cardinality.patch) by @vbraun created at 2011-01-26 14:08:36\n\nRebased against sage-4.6.2.alpha2",
    "created_at": "2011-01-26T14:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94587",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9713_fix_cardinality.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_cardinality.patch) by @vbraun created at 2011-01-26 14:08:36

Rebased against sage-4.6.2.alpha2



---

archive/issue_comments_094588.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-26T14:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94588",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094589.json:
```json
{
    "body": "Rebased against sage-4.6.2.alpha2",
    "created_at": "2011-01-26T14:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94589",
    "user": "https://github.com/vbraun"
}
```

Rebased against sage-4.6.2.alpha2



---

archive/issue_comments_094590.json:
```json
{
    "body": "What was necessary in rebasing??? I still have my queue applied smoothly on alpha2!",
    "created_at": "2011-01-26T14:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94590",
    "user": "https://github.com/novoselt"
}
```

What was necessary in rebasing??? I still have my queue applied smoothly on alpha2!



---

archive/issue_comments_094591.json:
```json
{
    "body": "I haven't actually checked whether anything broke. I don't remember if I had to refresh any patches for 4.6.2.alpha2, I just believed Jeroen that there was a problem. In any case, can't hurt.",
    "created_at": "2011-01-26T14:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94591",
    "user": "https://github.com/vbraun"
}
```

I haven't actually checked whether anything broke. I don't remember if I had to refresh any patches for 4.6.2.alpha2, I just believed Jeroen that there was a problem. In any case, can't hurt.



---

archive/issue_comments_094592.json:
```json
{
    "body": "Okay, there problem is slightly more involved: there is a conflict with #8948 (which is not yet merged in any alpha).  For totally arbitrary reasons I've decided to merge #8948 first, so could you please rebase your patches (at least [attachment:trac_9713_fix_fg_pid.2.patch]) to apply on top of #8948?",
    "created_at": "2011-01-26T17:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94592",
    "user": "https://github.com/jdemeyer"
}
```

Okay, there problem is slightly more involved: there is a conflict with #8948 (which is not yet merged in any alpha).  For totally arbitrary reasons I've decided to merge #8948 first, so could you please rebase your patches (at least [attachment:trac_9713_fix_fg_pid.2.patch]) to apply on top of #8948?



---

archive/issue_comments_094593.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-26T17:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94593",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094594.json:
```json
{
    "body": "Attachment [trac_9713_fix_fg_pid.2.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid.2.patch) by @vbraun created at 2011-01-26 22:37:04\n\nRebased patch.",
    "created_at": "2011-01-26T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94594",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9713_fix_fg_pid.2.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_fix_fg_pid.2.patch) by @vbraun created at 2011-01-26 22:37:04

Rebased patch.



---

archive/issue_comments_094595.json:
```json
{
    "body": "Rebased on top of Sage-4.6.2.alpha2+#8948.",
    "created_at": "2011-01-26T22:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94595",
    "user": "https://github.com/vbraun"
}
```

Rebased on top of Sage-4.6.2.alpha2+#8948.



---

archive/issue_comments_094596.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-26T22:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94596",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094597.json:
```json
{
    "body": "Replying to [comment:66 vbraun]:\n> Rebased on top of Sage-4.6.2.alpha2+#8948.\n\nThanks!  Patches apply fine now.  Sorry for the mess.",
    "created_at": "2011-01-26T22:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94597",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:66 vbraun]:
> Rebased on top of Sage-4.6.2.alpha2+#8948.

Thanks!  Patches apply fine now.  Sorry for the mess.



---

archive/issue_events_009845.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-27T09:13:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9713#event-9845"
}
```



---

archive/issue_comments_094598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-27T09:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94598",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_094599.json:
```json
{
    "body": "A doctest like this will **clearly** break on 32-bit systems:\n\n```\n    def __hash__(self):\n        \"\"\"\n        Return a hash value for the :class:`Module` instance.\n\n        OUTPUT:\n\n        An integer.\n\n        EXAMPLES::\n\n            sage: from sage.modules.module import Module\n            sage: M = Module(ZZ)\n            sage: M.__hash__()\n            6190647798068218210\n        \"\"\"\n        return hash(self.__repr__())\n```\n",
    "created_at": "2011-01-29T09:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94599",
    "user": "https://github.com/jdemeyer"
}
```

A doctest like this will **clearly** break on 32-bit systems:

```
    def __hash__(self):
        """
        Return a hash value for the :class:`Module` instance.

        OUTPUT:

        An integer.

        EXAMPLES::

            sage: from sage.modules.module import Module
            sage: M = Module(ZZ)
            sage: M.__hash__()
            6190647798068218210
        """
        return hash(self.__repr__())
```




---

archive/issue_comments_094600.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-01-29T09:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94600",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_009846.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-29T09:21:26Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9713#event-9846"
}
```



---

archive/issue_comments_094601.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-01-29T09:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94601",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_094602.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-29T09:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94602",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_094603.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-29T09:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94603",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094604.json:
```json
{
    "body": "Attachment [9713_hash.patch](tarball://root/attachments/some-uuid/ticket9713/9713_hash.patch) by @jdemeyer created at 2011-01-29 09:45:44",
    "created_at": "2011-01-29T09:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94604",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9713_hash.patch](tarball://root/attachments/some-uuid/ticket9713/9713_hash.patch) by @jdemeyer created at 2011-01-29 09:45:44



---

archive/issue_comments_094605.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-29T17:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94605",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094606.json:
```json
{
    "body": "Thanks for catching this!",
    "created_at": "2011-01-29T17:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94606",
    "user": "https://github.com/novoselt"
}
```

Thanks for catching this!



---

archive/issue_comments_094607.json:
```json
{
    "body": "I'm afraid I have to bother you again.  With this patch, the pdf reference manual fails to build:\n\n```\n! Missing $ inserted.\n<inserted text>\n                $\nl.532163 \\bibitem[wp:Chow_ring]{wp:Chow_ring}\n                                             {\\phantomsection\\label{sage/sch...\n\n?\n! Emergency stop.\n<inserted text>\n                $\nl.532163 \\bibitem[wp:Chow_ring]{wp:Chow_ring}\n                                             {\\phantomsection\\label{sage/sch...\n\n!  ==> Fatal error occurred, no output PDF file produced!\n```\n",
    "created_at": "2011-02-01T08:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94607",
    "user": "https://github.com/jdemeyer"
}
```

I'm afraid I have to bother you again.  With this patch, the pdf reference manual fails to build:

```
! Missing $ inserted.
<inserted text>
                $
l.532163 \bibitem[wp:Chow_ring]{wp:Chow_ring}
                                             {\phantomsection\label{sage/sch...

?
! Emergency stop.
<inserted text>
                $
l.532163 \bibitem[wp:Chow_ring]{wp:Chow_ring}
                                             {\phantomsection\label{sage/sch...

!  ==> Fatal error occurred, no output PDF file produced!
```




---

archive/issue_comments_094608.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-02-01T08:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94608",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094609.json:
```json
{
    "body": "Attachment [trac_9713_toric_chow_group.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_toric_chow_group.patch) by @vbraun created at 2011-02-01 12:08:20\n\nUpdated patch",
    "created_at": "2011-02-01T12:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94609",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9713_toric_chow_group.patch](tarball://root/attachments/some-uuid/ticket9713/trac_9713_toric_chow_group.patch) by @vbraun created at 2011-02-01 12:08:20

Updated patch



---

archive/issue_comments_094610.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-02-01T12:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94610",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094611.json:
```json
{
    "body": "I removed the underscore in the offending reference name. The pdf developer reference builds now if #10721 (Increase LaTeX POOL_SIZE) is applied.",
    "created_at": "2011-02-01T12:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94611",
    "user": "https://github.com/vbraun"
}
```

I removed the underscore in the offending reference name. The pdf developer reference builds now if #10721 (Increase LaTeX POOL_SIZE) is applied.



---

archive/issue_comments_094612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-07T08:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9713#issuecomment-94612",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009847.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-02-07T08:13:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9713",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9713#event-9847"
}
```
