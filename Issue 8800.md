# Issue 8800: Doctest coverage of categories

archive/issues_008800.json:
```json
{
    "body": "Assignee: Simon King\n\nKeywords: categories doctests\n\nAccording to William at the doctest coverage of categories is too low:\n\n\n```\naction.pyx: 0% (0 of 31)\nfunctor.pyx: 17% (3 of 17)\nmap.pyx: 27% (10 of 37)\nmorphism.pyx: 20% (5 of 24)\npushout.py: 24% (19 of 77) \n```\n\nTrying to add doc tests, I actually found a bug:\n\n\n```\nsage: abgrps = CommutativeAdditiveGroups()\nsage: ForgetfulFunctor(abgrps, abgrps)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/SAGE/patches/doku/english/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/categories/functor.so in sage.categories.functor.ForgetfulFunctor (sage/categories/functor.c:2083)()\n\nTypeError: IdentityFunctor() takes exactly one argument (2 given)\n```\n\nThe forgetful functor should coincide with the identity functor, but inside ``ForgetfulFunctor``, the latter is called in the wrong way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8800\n\n",
    "created_at": "2010-04-28T08:47:56Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Doctest coverage of categories",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8800",
    "user": "@simon-king-jena"
}
```
Assignee: Simon King

Keywords: categories doctests

According to William at the doctest coverage of categories is too low:


```
action.pyx: 0% (0 of 31)
functor.pyx: 17% (3 of 17)
map.pyx: 27% (10 of 37)
morphism.pyx: 20% (5 of 24)
pushout.py: 24% (19 of 77) 
```

Trying to add doc tests, I actually found a bug:


```
sage: abgrps = CommutativeAdditiveGroups()
sage: ForgetfulFunctor(abgrps, abgrps)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/patches/doku/english/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/categories/functor.so in sage.categories.functor.ForgetfulFunctor (sage/categories/functor.c:2083)()

TypeError: IdentityFunctor() takes exactly one argument (2 given)
```

The forgetful functor should coincide with the identity functor, but inside ``ForgetfulFunctor``, the latter is called in the wrong way.

Issue created by migration from https://trac.sagemath.org/ticket/8800





---

archive/issue_comments_080629.json:
```json
{
    "body": "Shouldn't the following raise an error, since the argument is not contained in the domain? Instead, it returns ``None``.\n\n```\nsage: fields = Fields()\nsage: rings = Rings()\nsage: F = ForgetfulFunctor(fields,rings)\nsage: F(ZZ['x','y'])\n```\n",
    "created_at": "2010-04-28T09:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80629",
    "user": "@simon-king-jena"
}
```

Shouldn't the following raise an error, since the argument is not contained in the domain? Instead, it returns ``None``.

```
sage: fields = Fields()
sage: rings = Rings()
sage: F = ForgetfulFunctor(fields,rings)
sage: F(ZZ['x','y'])
```




---

archive/issue_comments_080630.json:
```json
{
    "body": "Replying to [comment:2 SimonKing]:\n> Shouldn't the following raise an error, since the argument is not contained in the domain? Instead, it returns ``None``.\n\nAnd this is because the generic ``__call__`` method of ``Functor`` has *no* return value! That's clearly a bug.",
    "created_at": "2010-04-28T09:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80630",
    "user": "@simon-king-jena"
}
```

Replying to [comment:2 SimonKing]:
> Shouldn't the following raise an error, since the argument is not contained in the domain? Instead, it returns ``None``.

And this is because the generic ``__call__`` method of ``Functor`` has *no* return value! That's clearly a bug.



---

archive/issue_comments_080631.json:
```json
{
    "body": "Next bug:\n\n```\nsage: F = QQ['x'].construction()[0]\nsage: F\nPoly[x]\nsage: F == IdentityFunctor(Rings())\nFalse\nsage: IdentityFunctor(Rings()) == F\nTrue\n\n```\n\nThis is since the cmp method of ``IdentityFunctor_generic`` only checks whether domain and codomain coincide, but doesn't check the type of the functor.\n\nEven worse, comparison it may raise an error - how unpythonic!\n\n```\nsage: IdentityFunctor(Rings()) == QQ\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/king/SAGE/patches/doku/english/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/categories/functor.so in sage.categories.functor.ForgetfulFunctor_generic.__cmp__ (sage/categories/functor.c:1429)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:5064)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2738)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2610)()\n\nAttributeError: 'RationalField_with_category' object has no attribute 'domain'\n```\n",
    "created_at": "2010-04-28T09:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80631",
    "user": "@simon-king-jena"
}
```

Next bug:

```
sage: F = QQ['x'].construction()[0]
sage: F
Poly[x]
sage: F == IdentityFunctor(Rings())
False
sage: IdentityFunctor(Rings()) == F
True

```

This is since the cmp method of ``IdentityFunctor_generic`` only checks whether domain and codomain coincide, but doesn't check the type of the functor.

Even worse, comparison it may raise an error - how unpythonic!

```
sage: IdentityFunctor(Rings()) == QQ
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/king/SAGE/patches/doku/english/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/categories/functor.so in sage.categories.functor.ForgetfulFunctor_generic.__cmp__ (sage/categories/functor.c:1429)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:5064)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2738)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2610)()

AttributeError: 'RationalField_with_category' object has no attribute 'domain'
```




---

archive/issue_comments_080632.json:
```json
{
    "body": "I think the call method of the class Functor is not cleanly implemented.\n\nIt seems intended that the user does not implement the call method. Instead s/he should implement _apply_functor, which is supposed to return an object in the functor's codomain.\n\nBefore using _apply_functor, the default call method tests whether the argument belongs to the domain. If this is not the case, it **coerces** the argument into the domain. I don't think that this is always wanted. E.g., the forgetful functor from fields to rings, when applied to the integer ring, currently returns the rational field (so, the forgetful functor *adds* structure), since the default call method first coerces the integer ring into the category of fields (which is done by the fraction field construction functor).\n\nI suggest to introduce a method _coerce_into_domain. By default, it returns its argument without change. If the user wants coercion into the domain (e.g. Integer Ring --> Rational Field), then s/he must implement it here.\n\nThe default call method should first apply _coerce_into_domain, check whether the result is in the domain (raise an error if this is not the case), then use _apply_functor, and check whether the result is in the codomain (and raise an error otherwise). And of course it should return the result (which was forgotten!).\n\nThoughts?",
    "created_at": "2010-04-28T11:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80632",
    "user": "@simon-king-jena"
}
```

I think the call method of the class Functor is not cleanly implemented.

It seems intended that the user does not implement the call method. Instead s/he should implement _apply_functor, which is supposed to return an object in the functor's codomain.

Before using _apply_functor, the default call method tests whether the argument belongs to the domain. If this is not the case, it **coerces** the argument into the domain. I don't think that this is always wanted. E.g., the forgetful functor from fields to rings, when applied to the integer ring, currently returns the rational field (so, the forgetful functor *adds* structure), since the default call method first coerces the integer ring into the category of fields (which is done by the fraction field construction functor).

I suggest to introduce a method _coerce_into_domain. By default, it returns its argument without change. If the user wants coercion into the domain (e.g. Integer Ring --> Rational Field), then s/he must implement it here.

The default call method should first apply _coerce_into_domain, check whether the result is in the domain (raise an error if this is not the case), then use _apply_functor, and check whether the result is in the codomain (and raise an error otherwise). And of course it should return the result (which was forgotten!).

Thoughts?



---

archive/issue_comments_080633.json:
```json
{
    "body": "It meanwhile seems to me that an overhaul of the category framework is needed, in order to properly support working with morphisms and functors. I therefore opened #8807. \n\nIt could be that this ticket will eventually be 'absorbed' by #8807. We will see...",
    "created_at": "2010-04-28T18:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80633",
    "user": "@simon-king-jena"
}
```

It meanwhile seems to me that an overhaul of the category framework is needed, in order to properly support working with morphisms and functors. I therefore opened #8807. 

It could be that this ticket will eventually be 'absorbed' by #8807. We will see...



---

archive/issue_comments_080634.json:
```json
{
    "body": "I think it would be better to base this ticket on #8807, since I believe that #8807 should be merged soon anyway. \n\nContinuing with the doc tests, I think I found another bug, namely in the ``merge`` method of the Quotient construction functor:\n\n```\nsage: Q15,R = (ZZ.quo(15*ZZ)).construction()\nsage: Q15\nQuotientFunctor\nsage: Q35,R = (ZZ.quo(35*ZZ)).construction()\nsage: Q35\nQuotientFunctor\nsage: Q15.merge(Q35) is None\nTrue\nsage: from sage.categories.pushout import pushout\nsage: pushout(ZZ.quo(15*ZZ),ZZ.quo(35*ZZ))\n---------------------------------------------------------------------------\nCoercionException                         Traceback (most recent call last)\n\n/home/SimonKing/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)\n   1099                         else:\n   1100                             # Otherwise, we cannot proceed.\n-> 1101                             raise CoercionException, (\"Ambiguous Base Extension\", R, S)\n   1102\n   1103         return all(Z)\n\nCoercionException: ('Ambiguous Base Extension', Ring of integers modulo 15, Ring of integers modulo 35)\n```\n\n\nThe reason is that internally ``Q35.I + Q15.I`` is tried, but this raises an error. It works with ``Q35.I.gcd(Q15.I)``, though. If I do this (in a patch that I will hopefully post in a few days, one gets (as one *should*, if I am not mistaken)\n\n```\nsage: pushout(ZZ.quo(15*ZZ),ZZ.quo(35*ZZ))\nRing of integers modulo 5\n```\n",
    "created_at": "2010-05-02T19:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80634",
    "user": "@simon-king-jena"
}
```

I think it would be better to base this ticket on #8807, since I believe that #8807 should be merged soon anyway. 

Continuing with the doc tests, I think I found another bug, namely in the ``merge`` method of the Quotient construction functor:

```
sage: Q15,R = (ZZ.quo(15*ZZ)).construction()
sage: Q15
QuotientFunctor
sage: Q35,R = (ZZ.quo(35*ZZ)).construction()
sage: Q35
QuotientFunctor
sage: Q15.merge(Q35) is None
True
sage: from sage.categories.pushout import pushout
sage: pushout(ZZ.quo(15*ZZ),ZZ.quo(35*ZZ))
---------------------------------------------------------------------------
CoercionException                         Traceback (most recent call last)

/home/SimonKing/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)
   1099                         else:
   1100                             # Otherwise, we cannot proceed.
-> 1101                             raise CoercionException, ("Ambiguous Base Extension", R, S)
   1102
   1103         return all(Z)

CoercionException: ('Ambiguous Base Extension', Ring of integers modulo 15, Ring of integers modulo 35)
```


The reason is that internally ``Q35.I + Q15.I`` is tried, but this raises an error. It works with ``Q35.I.gcd(Q15.I)``, though. If I do this (in a patch that I will hopefully post in a few days, one gets (as one *should*, if I am not mistaken)

```
sage: pushout(ZZ.quo(15*ZZ),ZZ.quo(35*ZZ))
Ring of integers modulo 5
```




---

archive/issue_comments_080635.json:
```json
{
    "body": "Another bug that I plan to remove:\n\n```\nsage: F = MatrixSpace(ZZ,2,3).construction()[0]\nsage: F(RR) in F.codomain()\nFalse\n```\n\n\nThe problem is that the codomain of ``F`` is supposed to be the category of rings, even for non-square matrices. I'll change it to the following:\n\n```\nsage: MatrixSpace(ZZ,2,3).construction()[0].codomain()\nCategory of commutative additive groups\nsage: MatrixSpace(ZZ,2,2).construction()[0].codomain()\nCategory of rings\n```\n\n\nI'd actually like to have the category of modules (rather than of additive groups), but this would require a ring over which the module is defined (and which the functor obviously can't know).",
    "created_at": "2010-05-07T14:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80635",
    "user": "@simon-king-jena"
}
```

Another bug that I plan to remove:

```
sage: F = MatrixSpace(ZZ,2,3).construction()[0]
sage: F(RR) in F.codomain()
False
```


The problem is that the codomain of ``F`` is supposed to be the category of rings, even for non-square matrices. I'll change it to the following:

```
sage: MatrixSpace(ZZ,2,3).construction()[0].codomain()
Category of commutative additive groups
sage: MatrixSpace(ZZ,2,2).construction()[0].codomain()
Category of rings
```


I'd actually like to have the category of modules (rather than of additive groups), but this would require a ring over which the module is defined (and which the functor obviously can't know).



---

archive/issue_comments_080636.json:
```json
{
    "body": "The next one:\n\n```\nsage: F = FreeModule(ZZ,3).construction()[0]\nsage: F\nVectorFunctor\nsage: F.domain()\nCategory of objects\nsage: F.codomain()\nCategory of objects\nsage: Set([1,2,3]) in F.domain()\nTrue\nsage: F(Set([1,2,3]))\nTraceback (most recent call last):\n...\nAttributeError: 'Set_object_enumerated' object has no attribute 'is_commutative'\n```\n\n\nSince the functor calls the ``FreeModule`` constructor, and since this constructor expects a commutative ring, the Vector functor should go from the category of commutative rings to the category of commutative additive groups (since the category of modules requires naming a base ring).",
    "created_at": "2010-05-07T14:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80636",
    "user": "@simon-king-jena"
}
```

The next one:

```
sage: F = FreeModule(ZZ,3).construction()[0]
sage: F
VectorFunctor
sage: F.domain()
Category of objects
sage: F.codomain()
Category of objects
sage: Set([1,2,3]) in F.domain()
True
sage: F(Set([1,2,3]))
Traceback (most recent call last):
...
AttributeError: 'Set_object_enumerated' object has no attribute 'is_commutative'
```


Since the functor calls the ``FreeModule`` constructor, and since this constructor expects a commutative ring, the Vector functor should go from the category of commutative rings to the category of commutative additive groups (since the category of modules requires naming a base ring).



---

archive/issue_comments_080637.json:
```json
{
    "body": "Next bug:\n\n``BlackBoxConstructionFunctor`` should be a class, but is defined as a function. Moreover, the given init method is not using the init method of ``ConstructionFunctor``. And the cmp method would raise an error if the second argument has no attribute ``.box``.",
    "created_at": "2010-05-07T19:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80637",
    "user": "@simon-king-jena"
}
```

Next bug:

``BlackBoxConstructionFunctor`` should be a class, but is defined as a function. Moreover, the given init method is not using the init method of ``ConstructionFunctor``. And the cmp method would raise an error if the second argument has no attribute ``.box``.



---

archive/issue_comments_080638.json:
```json
{
    "body": "Merging ``AlgebraicClosureFunctor`` with *anything* else always yields the ``AlgebraicClosureFunctor``. I doubt that this was intended. There should be a merging with an ``AlgebraicExtensionFunctor``, though.",
    "created_at": "2010-05-07T20:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80638",
    "user": "@simon-king-jena"
}
```

Merging ``AlgebraicClosureFunctor`` with *anything* else always yields the ``AlgebraicClosureFunctor``. I doubt that this was intended. There should be a merging with an ``AlgebraicExtensionFunctor``, though.



---

archive/issue_comments_080639.json:
```json
{
    "body": "Replying to [comment:11 SimonKing]:\n> ... There should be a merging with an ``AlgebraicExtensionFunctor``, though.\n\n... which is nowhere used, though. I think the method ``construction`` for number fields should be defined.",
    "created_at": "2010-05-07T20:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80639",
    "user": "@simon-king-jena"
}
```

Replying to [comment:11 SimonKing]:
> ... There should be a merging with an ``AlgebraicExtensionFunctor``, though.

... which is nowhere used, though. I think the method ``construction`` for number fields should be defined.



---

archive/issue_comments_080640.json:
```json
{
    "body": "\n```\nsage: P.<x> = QQ[]\nsage: CC.extension(x^3+x^2+1,'a')\nUnivariate Quotient Polynomial Ring in a over Complex Field with 53 bits of precision with modulus a^3 + a^2 + 1.00000000000000\nsage: CDF.extension(x^3+x^2+1,'a')\nUnivariate Quotient Polynomial Ring in a over Complex Double Field with modulus a^3 + a^2 + 1.0\nsage: QQbar.extension(x^3+x^2+1,'a')\nUnivariate Quotient Polynomial Ring in a over Algebraic Field with modulus a^3 + a^2 + 1\n```\n\n\nAren't the three above fields algebraically complete? So, I guess the ``extension`` method should be modified to take this into account.",
    "created_at": "2010-05-08T09:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80640",
    "user": "@simon-king-jena"
}
```


```
sage: P.<x> = QQ[]
sage: CC.extension(x^3+x^2+1,'a')
Univariate Quotient Polynomial Ring in a over Complex Field with 53 bits of precision with modulus a^3 + a^2 + 1.00000000000000
sage: CDF.extension(x^3+x^2+1,'a')
Univariate Quotient Polynomial Ring in a over Complex Double Field with modulus a^3 + a^2 + 1.0
sage: QQbar.extension(x^3+x^2+1,'a')
Univariate Quotient Polynomial Ring in a over Algebraic Field with modulus a^3 + a^2 + 1
```


Aren't the three above fields algebraically complete? So, I guess the ``extension`` method should be modified to take this into account.



---

archive/issue_comments_080641.json:
```json
{
    "body": "Concerning algebraic extension of algebraically complete fields: sage-devel expressed the opinion that it is better to do the construction (namely quotient of a univariate polynomial ring) in any case. So, I leave it as it is.\n\nHere is another problem:\n\n```\nsage: R1.<x> = Zp(5)[]\nsage: R2 = Qp(5)\nsage: R2(1)+x\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/SimonKing/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10830)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()\n\nTypeError: unsupported operand parent(s) for '+': '5-adic Field with capped relative precision 20' and 'Univariate Polynomial Ring in x over 5-adic Ring with capped relative precision 20'\n```\n\n\nThe reason is \n\n```\nsage: from sage.categories.pushout import pushout\nsage: pushout(R1,R2)\n---------------------------------------------------------------------------\nCoercionException                         Traceback (most recent call last)\n\n/home/SimonKing/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)\n   1109         # make sense, and in this case simply want to return that a pushout\n   1110         # couldn't be found.\n-> 1111         raise CoercionException(ex)\n   1112\n   1113\n\nCoercionException: 'pAdicFieldCappedRelative' object has no attribute 'completion'\n```\n\n\nRather than implementing a completion of p-adic fields, I suggest to give the construction functors of fraction fields and of completions the same rank. This would already suffice (together with the existing merge method of the completion functor) so that one has\n\n```\nsage: R1.<x> = Zp(5)[]\nsage: R2 = Qp(5)\nsage: R2(1) + x\n(1 + O(5^20))*x + (1 + O(5^20))\n```\n\n\nNote that there is an additional problem, namely that there is no coercion from a p-adic field of high precision to a p-adic field of lower precision. I hope sage-devel will answer whether this issue is worth a separate ticket.",
    "created_at": "2010-05-14T13:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80641",
    "user": "@simon-king-jena"
}
```

Concerning algebraic extension of algebraically complete fields: sage-devel expressed the opinion that it is better to do the construction (namely quotient of a univariate polynomial ring) in any case. So, I leave it as it is.

Here is another problem:

```
sage: R1.<x> = Zp(5)[]
sage: R2 = Qp(5)
sage: R2(1)+x
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/SimonKing/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:10830)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '+': '5-adic Field with capped relative precision 20' and 'Univariate Polynomial Ring in x over 5-adic Ring with capped relative precision 20'
```


The reason is 

```
sage: from sage.categories.pushout import pushout
sage: pushout(R1,R2)
---------------------------------------------------------------------------
CoercionException                         Traceback (most recent call last)

/home/SimonKing/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)
   1109         # make sense, and in this case simply want to return that a pushout
   1110         # couldn't be found.
-> 1111         raise CoercionException(ex)
   1112
   1113

CoercionException: 'pAdicFieldCappedRelative' object has no attribute 'completion'
```


Rather than implementing a completion of p-adic fields, I suggest to give the construction functors of fraction fields and of completions the same rank. This would already suffice (together with the existing merge method of the completion functor) so that one has

```
sage: R1.<x> = Zp(5)[]
sage: R2 = Qp(5)
sage: R2(1) + x
(1 + O(5^20))*x + (1 + O(5^20))
```


Note that there is an additional problem, namely that there is no coercion from a p-adic field of high precision to a p-adic field of lower precision. I hope sage-devel will answer whether this issue is worth a separate ticket.



---

archive/issue_comments_080642.json:
```json
{
    "body": "PS:\n\nReplying to [comment:14 SimonKing]:\n> Rather than implementing a completion of p-adic fields, I suggest to give the construction functors of fraction fields and of completions the same rank...\n\n... since they commute anyway. I guess it wouldn't harm to implement the ``commutes`` method as well.\n\nI now consider the Localization functor. It uses the method \"localize\", but:\n\n```\nsage: search_def('localize')\n\nsage: search_src('localize')\ncategories/pushout.py:1294:        return R.localize(t)\nlibs/singular/option.pyx:367:    This object localizes changes to options.\n```\n\n\nIn other words, there is no class that has a localize method. So, I guess it is safe to comment the Localization functor out.",
    "created_at": "2010-05-14T14:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80642",
    "user": "@simon-king-jena"
}
```

PS:

Replying to [comment:14 SimonKing]:
> Rather than implementing a completion of p-adic fields, I suggest to give the construction functors of fraction fields and of completions the same rank...

... since they commute anyway. I guess it wouldn't harm to implement the ``commutes`` method as well.

I now consider the Localization functor. It uses the method "localize", but:

```
sage: search_def('localize')

sage: search_src('localize')
categories/pushout.py:1294:        return R.localize(t)
libs/singular/option.pyx:367:    This object localizes changes to options.
```


In other words, there is no class that has a localize method. So, I guess it is safe to comment the Localization functor out.



---

archive/issue_comments_080643.json:
```json
{
    "body": "Wow, I count 7 bugs in the comments above!  What a testament for the need for writing good doctests (and to how careful you are!)",
    "created_at": "2010-05-14T15:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80643",
    "user": "@jasongrout"
}
```

Wow, I count 7 bugs in the comments above!  What a testament for the need for writing good doctests (and to how careful you are!)



---

archive/issue_comments_080644.json:
```json
{
    "body": "Replying to [comment:14 SimonKing]:\n> Note that there is an additional problem, namely that there is no coercion from a p-adic field of high precision to a p-adic field of lower precision. I hope sage-devel will answer whether this issue is worth a separate ticket.\n\nSage-devel (more precisely Robert Bradshaw) wrote that the meaning of \"precision\" is different for completion at Infinity and at finite primes, and it makes sense that sometimes the precision is non-decreasing and sometimes non-increasing under coercion.\n\nSo, I guess I have to modify the merge method of the Completion funtor, rather than the _coerce_map_from method of p-adic rings.",
    "created_at": "2010-05-14T18:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80644",
    "user": "@simon-king-jena"
}
```

Replying to [comment:14 SimonKing]:
> Note that there is an additional problem, namely that there is no coercion from a p-adic field of high precision to a p-adic field of lower precision. I hope sage-devel will answer whether this issue is worth a separate ticket.

Sage-devel (more precisely Robert Bradshaw) wrote that the meaning of "precision" is different for completion at Infinity and at finite primes, and it makes sense that sometimes the precision is non-decreasing and sometimes non-increasing under coercion.

So, I guess I have to modify the merge method of the Completion funtor, rather than the _coerce_map_from method of p-adic rings.



---

archive/issue_comments_080645.json:
```json
{
    "body": "I noticed the following:\n\n```\nsage: P.<x> = ZZ[]\nsage: C = P.completion(x).construction()[0]\nsage: R = FractionField(P)\nsage: hasattr(R,'completion')\nFalse\nsage: C(R)\nTraceback (most recent  call last):\n...\nAttributeError: 'FractionField_generic' object has no attribute 'completion'\n```\n\n\nThis is since the completion functor simply tries to call the completion method of its argument. However, one can use that the fraction field construction functor and the completion functor commute.\n\nSo, I first try to apply a completion method of the argument, R. If it fails with an AttributeError or NotImplementedError, I look at R's construction (F,R1). If F merges with completion, then I apply the result of merging to R1. Otherwise, if the completion commutes with F, I try to first apply the completion to R1 and then apply F to the result, and obtain:\n\n```\nsage: C(R)\nFraction Field of Power Series Ring in x over Integer Ring\n```\n\n\nNote that this would *not* be the first place where merging and commutation of construction functors is used outside the ``pushout`` function. The other place is the construction of infinite polynomial rings, which I wrote as well. Indeed I believe that construction functors should be used more intensely...",
    "created_at": "2010-05-15T12:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80645",
    "user": "@simon-king-jena"
}
```

I noticed the following:

```
sage: P.<x> = ZZ[]
sage: C = P.completion(x).construction()[0]
sage: R = FractionField(P)
sage: hasattr(R,'completion')
False
sage: C(R)
Traceback (most recent  call last):
...
AttributeError: 'FractionField_generic' object has no attribute 'completion'
```


This is since the completion functor simply tries to call the completion method of its argument. However, one can use that the fraction field construction functor and the completion functor commute.

So, I first try to apply a completion method of the argument, R. If it fails with an AttributeError or NotImplementedError, I look at R's construction (F,R1). If F merges with completion, then I apply the result of merging to R1. Otherwise, if the completion commutes with F, I try to first apply the completion to R1 and then apply F to the result, and obtain:

```
sage: C(R)
Fraction Field of Power Series Ring in x over Integer Ring
```


Note that this would *not* be the first place where merging and commutation of construction functors is used outside the ``pushout`` function. The other place is the construction of infinite polynomial rings, which I wrote as well. Indeed I believe that construction functors should be used more intensely...



---

archive/issue_comments_080646.json:
```json
{
    "body": "Replying to [comment:18 SimonKing]:\n> ...\n> {{{\n> sage: C(R)\n> Fraction Field of Power Series Ring in x over Integer Ring\n> }}}\n\nI believe that the fraction field of a power series ring over a base ring ``B`` should be identical with the Laurent series ring over the fraction field of ``B``. This is implemented in ticket #8972.\n\nI am tempted to say \"let's wait until #8972 is refereed\", because the doc tests I am constructing here will depend on whether #8972 gets merged or not.\n\nWhat is the policy in those cases? Should I simply continue the work on the doc tests and care about #8972 later?",
    "created_at": "2010-05-17T09:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80646",
    "user": "@simon-king-jena"
}
```

Replying to [comment:18 SimonKing]:
> ...
> {{{
> sage: C(R)
> Fraction Field of Power Series Ring in x over Integer Ring
> }}}

I believe that the fraction field of a power series ring over a base ring ``B`` should be identical with the Laurent series ring over the fraction field of ``B``. This is implemented in ticket #8972.

I am tempted to say "let's wait until #8972 is refereed", because the doc tests I am constructing here will depend on whether #8972 gets merged or not.

What is the policy in those cases? Should I simply continue the work on the doc tests and care about #8972 later?



---

archive/issue_comments_080647.json:
```json
{
    "body": "Currently, the construction functors for free modules and for matrix spaces have the same rank, but they do not commute and do not merge. Hence, the following goes boom:\n\n```\nsage: from sage.categories.pushout import pushout\nsage: pushout(QQ^3,MatrixSpace(QQ,3))\n---------------------------------------------------------------------------\nCoercionException                         Traceback (most recent call last)\n...\nCoercionException: ('Ambiguous Base Extension', Vector space of dimension 3 over Rational Field, Full MatrixSpace of 3 by 3 dense matrices over Rational Field)\n```\n\n\nI think this pushout should exist. But what should result?\n\n1. ``MatrixSpace(QQ,3)<sup>3</sup>`` resp. ``FreeModule(MatrixSpace(QQ,3),3)``. This is currently not possible, since ``MatrixSpace_generic`` has no attribute ``is_commutative``.\n\n2. ``MatrixSpace(QQ<sup>3</sup>,3)`` makes no sense, as ``QQ<sup>3</sup>`` is no ring.\n\n3. ``MatrixSpace(QQ,27)`` makes not much sense, as I don't see coercion maps.\n\nSo, probably it is solution number 1, which at least requires to implement an ``is_commutative`` method, resp. to first test for the presence of such method in ``FreeModule``. I think I'll go for it.",
    "created_at": "2010-05-17T12:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80647",
    "user": "@simon-king-jena"
}
```

Currently, the construction functors for free modules and for matrix spaces have the same rank, but they do not commute and do not merge. Hence, the following goes boom:

```
sage: from sage.categories.pushout import pushout
sage: pushout(QQ^3,MatrixSpace(QQ,3))
---------------------------------------------------------------------------
CoercionException                         Traceback (most recent call last)
...
CoercionException: ('Ambiguous Base Extension', Vector space of dimension 3 over Rational Field, Full MatrixSpace of 3 by 3 dense matrices over Rational Field)
```


I think this pushout should exist. But what should result?

1. ``MatrixSpace(QQ,3)<sup>3</sup>`` resp. ``FreeModule(MatrixSpace(QQ,3),3)``. This is currently not possible, since ``MatrixSpace_generic`` has no attribute ``is_commutative``.

2. ``MatrixSpace(QQ<sup>3</sup>,3)`` makes no sense, as ``QQ<sup>3</sup>`` is no ring.

3. ``MatrixSpace(QQ,27)`` makes not much sense, as I don't see coercion maps.

So, probably it is solution number 1, which at least requires to implement an ``is_commutative`` method, resp. to first test for the presence of such method in ``FreeModule``. I think I'll go for it.



---

archive/issue_comments_080648.json:
```json
{
    "body": "Replying to [comment:20 SimonKing]:\n> So, probably it is solution number 1, which at least requires to implement an ``is_commutative`` method, resp. to first test for the presence of such method in ``FreeModule``. I think I'll go for it.\n\nOops, this is nonsense. The ``FreeModule`` constructor expects a commutative ring. So, solution 1. is no solution. I will change the constructor so that it is first tested whether the ``is_commutative`` method exists, so that the error message is clearer, but apart from that, it is OK that the pushout does not exist.",
    "created_at": "2010-05-17T12:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80648",
    "user": "@simon-king-jena"
}
```

Replying to [comment:20 SimonKing]:
> So, probably it is solution number 1, which at least requires to implement an ``is_commutative`` method, resp. to first test for the presence of such method in ``FreeModule``. I think I'll go for it.

Oops, this is nonsense. The ``FreeModule`` constructor expects a commutative ring. So, solution 1. is no solution. I will change the constructor so that it is first tested whether the ``is_commutative`` method exists, so that the error message is clearer, but apart from that, it is OK that the pushout does not exist.



---

archive/issue_comments_080649.json:
```json
{
    "body": "I believe that free modules of the same rank but with different inner product matrix should not allow coercion. Hence, I think the following is a bug:\n\n```\nsage: P.<t> = ZZ[]\nsage: M1 = FreeModule(P,3)\nsage: M2 = QQ^3\nsage: M2([1,1/2,1/3]) + M1([t,t^2+t,3])     # This is ok\n(t + 1, t^2 + t + 1/2, 10/3)\nsage: M3 = FreeModule(P,3, inner_product_matrix = Matrix(3,3,range(9)))\nsage: M2([1,1/2,1/3]) + M3([t,t^2+t,3])     # This should result in an error\n(t + 1, t^2 + t + 1/2, 10/3)\n```\n\n\nThis inappropriate coercion can be avoided by modifying the merge method of the construction functors, so that the inner product matrices are used for comparison as well.\n\nBut I acknowledge that other people might think that a coercion should exist. Perhaps I shall ask on sage-algebra...",
    "created_at": "2010-05-17T13:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80649",
    "user": "@simon-king-jena"
}
```

I believe that free modules of the same rank but with different inner product matrix should not allow coercion. Hence, I think the following is a bug:

```
sage: P.<t> = ZZ[]
sage: M1 = FreeModule(P,3)
sage: M2 = QQ^3
sage: M2([1,1/2,1/3]) + M1([t,t^2+t,3])     # This is ok
(t + 1, t^2 + t + 1/2, 10/3)
sage: M3 = FreeModule(P,3, inner_product_matrix = Matrix(3,3,range(9)))
sage: M2([1,1/2,1/3]) + M3([t,t^2+t,3])     # This should result in an error
(t + 1, t^2 + t + 1/2, 10/3)
```


This inappropriate coercion can be avoided by modifying the merge method of the construction functors, so that the inner product matrices are used for comparison as well.

But I acknowledge that other people might think that a coercion should exist. Perhaps I shall ask on sage-algebra...



---

archive/issue_comments_080650.json:
```json
{
    "body": "Replying to [comment:22 SimonKing]:\n> ...\n> But I acknowledge that other people might think that a coercion should exist. Perhaps I shall ask on sage-algebra...\n\nsage-algebra (John Cremona and William Stein) answered that the inner product is an important structure if and *only* if it is explicitly defined by the user. Hence, in the above example with ``M2`` and ``M3``, no error should be raised, since ``M2`` has no user-defined inner product. But if ``M2`` was *explicitly* be provided with the standard inner product, then an error should be raised.\n\nThat's easy to implement: The ``construction()`` method of the modules returns a ``VectorFunctor``, and this one carries the inner product matrix (if provided by the user) or None. And two ``VectorFunctor``s carrying different inner product matrices will not be merged.",
    "created_at": "2010-05-17T17:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80650",
    "user": "@simon-king-jena"
}
```

Replying to [comment:22 SimonKing]:
> ...
> But I acknowledge that other people might think that a coercion should exist. Perhaps I shall ask on sage-algebra...

sage-algebra (John Cremona and William Stein) answered that the inner product is an important structure if and *only* if it is explicitly defined by the user. Hence, in the above example with ``M2`` and ``M3``, no error should be raised, since ``M2`` has no user-defined inner product. But if ``M2`` was *explicitly* be provided with the standard inner product, then an error should be raised.

That's easy to implement: The ``construction()`` method of the modules returns a ``VectorFunctor``, and this one carries the inner product matrix (if provided by the user) or None. And two ``VectorFunctor``s carrying different inner product matrices will not be merged.



---

archive/issue_comments_080651.json:
```json
{
    "body": "Next issue: Quotient rings of univariate polynomial rings did not have a construction method. I am implementing it, so that one has:\n\n```\nsage: P.<t>=ZZ[]\nsage: Q = P.quo(5+t^2)\nsage: F,R = Q.construction()\nsage: F(R) == Q\nTrue\nsage: P.<t> = GF(3)[]\nsage: Q = P.quo([2+t^2])\nsage: F,R = Q.construction()\nsage: F(R) == Q\nTrue\n```\n",
    "created_at": "2010-05-18T15:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80651",
    "user": "@simon-king-jena"
}
```

Next issue: Quotient rings of univariate polynomial rings did not have a construction method. I am implementing it, so that one has:

```
sage: P.<t>=ZZ[]
sage: Q = P.quo(5+t^2)
sage: F,R = Q.construction()
sage: F(R) == Q
True
sage: P.<t> = GF(3)[]
sage: Q = P.quo([2+t^2])
sage: F,R = Q.construction()
sage: F(R) == Q
True
```




---

archive/issue_comments_080652.json:
```json
{
    "body": "I am now almost finished with the doc tests for pushout.py.\n\nThe soon-to-be-submitted patch is already quite big, and comprises various bug fixes. I suggest that this ticket will mainly be about pushout.py, and the other files will be done on a separate ticket.\n\nHere are three more bugs. Number one:\n\n```\nsage: sage: P.<x> = QQ[]\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])\nsage: from sage.categories.pushout import pushout\nsage: pushout(Q1,Q2)\n---------------------------------------------------------------------------\nCoercionException                         Traceback (most recent call last)\n\n/home/king/SAGE/work/invarianten/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)\n   1037\n   1038     else:\n-> 1039         raise CoercionException, \"No common base\"\n   1040\n   1041     # Rc is a list of functors from Z to R and Sc is a list of functors from Z to S\n\nCoercionException: No common base\n```\n\nThis I can fix. The problem is that the quotient rings have no proper ``construction()`` method.\n\nNumber 2, continuing the above example:\n\n```\nsage: Q = P.quo([(x^2+1)^2])\nsage: Q.has_coerce_map_from(Q1)\nFalse\nsage: Q.has_coerce_map_from(Q2)\nFalse\n```\n\n\nThis is wrong since the modulus of Q divides the modulus of Q1 and Q2. Actually Q is supposed to be the pushout of Q1 and Q2.\n\nNumber three:\n\n```\nsage: Q(Q1.gen())\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (932, 0))\n...\nTypeError: Unable to coerce xbar (<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>) to Rational\n```\n\n\nBut I guess these last two errors should be on a different ticket.",
    "created_at": "2010-05-18T16:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80652",
    "user": "@simon-king-jena"
}
```

I am now almost finished with the doc tests for pushout.py.

The soon-to-be-submitted patch is already quite big, and comprises various bug fixes. I suggest that this ticket will mainly be about pushout.py, and the other files will be done on a separate ticket.

Here are three more bugs. Number one:

```
sage: sage: P.<x> = QQ[]
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: from sage.categories.pushout import pushout
sage: pushout(Q1,Q2)
---------------------------------------------------------------------------
CoercionException                         Traceback (most recent call last)

/home/king/SAGE/work/invarianten/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)
   1037
   1038     else:
-> 1039         raise CoercionException, "No common base"
   1040
   1041     # Rc is a list of functors from Z to R and Sc is a list of functors from Z to S

CoercionException: No common base
```

This I can fix. The problem is that the quotient rings have no proper ``construction()`` method.

Number 2, continuing the above example:

```
sage: Q = P.quo([(x^2+1)^2])
sage: Q.has_coerce_map_from(Q1)
False
sage: Q.has_coerce_map_from(Q2)
False
```


This is wrong since the modulus of Q divides the modulus of Q1 and Q2. Actually Q is supposed to be the pushout of Q1 and Q2.

Number three:

```
sage: Q(Q1.gen())
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))
...
TypeError: Unable to coerce xbar (<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>) to Rational
```


But I guess these last two errors should be on a different ticket.



---

archive/issue_comments_080653.json:
```json
{
    "body": "* The patch is to be applied *after the patches from* #8807.\n\n* It raises the **doctest coverage of sage.categories.functor and sage.categories.pushout to 100%** and occasionally adds doc tests in other places.\n\n* It fixes numerous bugs related with coercion, as indicated in the posts above.\n\nConstructing doc tests for pushout.py and functor.pyx revealed many bugs, so that I needed to change\n\n```\nsage/structure/parent.pyx\nsage/rings/ring.pyx\nsage/rings/rational_field.py\nsage/rings/quotient_ring.py\nsage/rings/qqbar.py\nsage/rings/polynomial/polynomial_quotient_ring.py\nsage/rings/number_field/number_field.py\nsage/modules/free_module.py\nsage/categories/pushout.py\nsage/categories/functor.pyx\n```\n\n\nThe doc tests for all these files still pass.\n\nI think it would make no sense to put more on this ticket. The work on doc tests in map.pyx, morphism.pyx and action.pyx will be moved to a different ticket.",
    "created_at": "2010-05-18T23:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80653",
    "user": "@simon-king-jena"
}
```

* The patch is to be applied *after the patches from* #8807.

* It raises the **doctest coverage of sage.categories.functor and sage.categories.pushout to 100%** and occasionally adds doc tests in other places.

* It fixes numerous bugs related with coercion, as indicated in the posts above.

Constructing doc tests for pushout.py and functor.pyx revealed many bugs, so that I needed to change

```
sage/structure/parent.pyx
sage/rings/ring.pyx
sage/rings/rational_field.py
sage/rings/quotient_ring.py
sage/rings/qqbar.py
sage/rings/polynomial/polynomial_quotient_ring.py
sage/rings/number_field/number_field.py
sage/modules/free_module.py
sage/categories/pushout.py
sage/categories/functor.pyx
```


The doc tests for all these files still pass.

I think it would make no sense to put more on this ticket. The work on doc tests in map.pyx, morphism.pyx and action.pyx will be moved to a different ticket.



---

archive/issue_comments_080654.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T23:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80654",
    "user": "@simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080655.json:
```json
{
    "body": "Wow, this is looking very good! \n\nMatrixFunctor.__init__, is there not a module category that could be used in place of `CommutativeAdditiveGroups`? I guess if tbe basering is unknown then that's more difficult. \n\nMissing periods on `VectorFunctor.__cmp__` and `VectorFunctor.merge`. I agree with the logic for that merge function. \n\nThat's all I've seen so far (and I've read most of the patch.) You've fixed a lot of bugs too. Pending doctests passing, I'd say this is ready for a positive review.",
    "created_at": "2010-05-19T03:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80655",
    "user": "@robertwb"
}
```

Wow, this is looking very good! 

MatrixFunctor.__init__, is there not a module category that could be used in place of `CommutativeAdditiveGroups`? I guess if tbe basering is unknown then that's more difficult. 

Missing periods on `VectorFunctor.__cmp__` and `VectorFunctor.merge`. I agree with the logic for that merge function. 

That's all I've seen so far (and I've read most of the patch.) You've fixed a lot of bugs too. Pending doctests passing, I'd say this is ready for a positive review.



---

archive/issue_comments_080656.json:
```json
{
    "body": "Hi Robert!\n\nReplying to [comment:27 robertwb]:\n> MatrixFunctor.__init__, is there not a module category that could be used in place of `CommutativeAdditiveGroups`? I guess if tbe basering is unknown then that's more difficult. \n\nYes, `Modules()` requires a base ring. There is currently no category of modules, but only a category of R-modules for any ring R. This is why I used `CommutativeAdditiveGroups()` in several cases. \n\n\n> Missing periods on `VectorFunctor.__cmp__` and `VectorFunctor.merge`.\n\nMissing where? In the doc string?\n\nConcerning positive review, note that technically this ticket depends on #8807, which has no review yet.\n\nBest regards,\nSimon",
    "created_at": "2010-05-19T08:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80656",
    "user": "@simon-king-jena"
}
```

Hi Robert!

Replying to [comment:27 robertwb]:
> MatrixFunctor.__init__, is there not a module category that could be used in place of `CommutativeAdditiveGroups`? I guess if tbe basering is unknown then that's more difficult. 

Yes, `Modules()` requires a base ring. There is currently no category of modules, but only a category of R-modules for any ring R. This is why I used `CommutativeAdditiveGroups()` in several cases. 


> Missing periods on `VectorFunctor.__cmp__` and `VectorFunctor.merge`.

Missing where? In the doc string?

Concerning positive review, note that technically this ticket depends on #8807, which has no review yet.

Best regards,
Simon



---

archive/issue_comments_080657.json:
```json
{
    "body": "Replying to [comment:28 SimonKing]:\n> Hi Robert!\n> \n> Replying to [comment:27 robertwb]:\n> > MatrixFunctor.__init__, is there not a module category that could be used in place of `CommutativeAdditiveGroups`? I guess if tbe basering is unknown then that's more difficult. \n> \n> Yes, `Modules()` requires a base ring. There is currently no category of modules, but only a category of R-modules for any ring R. This is why I used `CommutativeAdditiveGroups()` in several cases. \n\nHmm... does it make sense to have a category of Modules (over any basering)? \n\n> > Missing periods on `VectorFunctor.__cmp__` and `VectorFunctor.merge`.\n> \n> Missing where? In the doc string?\n\nYes, there were a couple of sentences without ending periods. Nothing major. \n\n> Concerning positive review, note that technically this ticket depends on #8807, which has no review yet.\n> \n\nYep. I started to look at that one too, and will review it if no one beats me too it when I have another spare moment (maybe the upcoming Sage days, depending on how good of shape my thesis is in by then).",
    "created_at": "2010-05-19T10:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80657",
    "user": "@robertwb"
}
```

Replying to [comment:28 SimonKing]:
> Hi Robert!
> 
> Replying to [comment:27 robertwb]:
> > MatrixFunctor.__init__, is there not a module category that could be used in place of `CommutativeAdditiveGroups`? I guess if tbe basering is unknown then that's more difficult. 
> 
> Yes, `Modules()` requires a base ring. There is currently no category of modules, but only a category of R-modules for any ring R. This is why I used `CommutativeAdditiveGroups()` in several cases. 

Hmm... does it make sense to have a category of Modules (over any basering)? 

> > Missing periods on `VectorFunctor.__cmp__` and `VectorFunctor.merge`.
> 
> Missing where? In the doc string?

Yes, there were a couple of sentences without ending periods. Nothing major. 

> Concerning positive review, note that technically this ticket depends on #8807, which has no review yet.
> 

Yep. I started to look at that one too, and will review it if no one beats me too it when I have another spare moment (maybe the upcoming Sage days, depending on how good of shape my thesis is in by then).



---

archive/issue_comments_080658.json:
```json
{
    "body": "Replying to [comment:29 robertwb]:\n> ...\n> Hmm... does it make sense to have a category of Modules (over any basering)? \n\nThe axioms of categories say that there must be the identity morphism for any object, and that composition of functors must be associative. It is not required that there is a morphism (e.g., the null-homomorphism) between any two objects. So, I guess a category of modules is just fine.\n\nCheers,\nSimon",
    "created_at": "2010-05-19T10:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80658",
    "user": "@simon-king-jena"
}
```

Replying to [comment:29 robertwb]:
> ...
> Hmm... does it make sense to have a category of Modules (over any basering)? 

The axioms of categories say that there must be the identity morphism for any object, and that composition of functors must be associative. It is not required that there is a morphism (e.g., the null-homomorphism) between any two objects. So, I guess a category of modules is just fine.

Cheers,
Simon



---

archive/issue_comments_080659.json:
```json
{
    "body": "There was a change needed in the patch from #8807. So, I had to rebase the ticket here. I just did! \n\nI did not yet have the time to run `make ptestall`, but will start it right now.",
    "created_at": "2010-07-21T13:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80659",
    "user": "@simon-king-jena"
}
```

There was a change needed in the patch from #8807. So, I had to rebase the ticket here. I just did! 

I did not yet have the time to run `make ptestall`, but will start it right now.



---

archive/issue_comments_080660.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-26T20:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80660",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080661.json:
```json
{
    "body": "The patch here does not apply cleanly after the one at #8807 (on 4.6.rc0).",
    "created_at": "2010-10-26T20:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80661",
    "user": "@JohnCremona"
}
```

The patch here does not apply cleanly after the one at #8807 (on 4.6.rc0).



---

archive/issue_comments_080662.json:
```json
{
    "body": "Replying to [comment:32 cremona]:\n> The patch here does not apply cleanly after the one at #8807 (on 4.6.rc0).\n\nThank you for trying. Do you say that #8807 did apply, but the patch here did not?\n\nAnyway, it will take a until next week befor I will be able to resume work.\n\nBest regards, Simon",
    "created_at": "2010-10-26T20:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80662",
    "user": "@simon-king-jena"
}
```

Replying to [comment:32 cremona]:
> The patch here does not apply cleanly after the one at #8807 (on 4.6.rc0).

Thank you for trying. Do you say that #8807 did apply, but the patch here did not?

Anyway, it will take a until next week befor I will be able to resume work.

Best regards, Simon



---

archive/issue_comments_080663.json:
```json
{
    "body": "I just uploaded a new version of my patch. It does apply after the patch from #8807 (with some fuzz), but now various doctests fail.\n\nAt least in one case, the reason is that some matrices still have a custom `__mul__` method were they should have a `_mul_` (single underscore) and `_act_on_` method. I expect that it will be addressed on a different ticket.\n\nSo, it needs work, but feel free to experiment with the new patch...",
    "created_at": "2010-11-24T12:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80663",
    "user": "@simon-king-jena"
}
```

I just uploaded a new version of my patch. It does apply after the patch from #8807 (with some fuzz), but now various doctests fail.

At least in one case, the reason is that some matrices still have a custom `__mul__` method were they should have a `_mul_` (single underscore) and `_act_on_` method. I expect that it will be addressed on a different ticket.

So, it needs work, but feel free to experiment with the new patch...



---

archive/issue_comments_080664.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-06T10:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80664",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080665.json:
```json
{
    "body": "Now, as the patch is updated, it is again ready for review. See the new ticket description for an account of what the patch does.",
    "created_at": "2010-12-06T10:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80665",
    "user": "@simon-king-jena"
}
```

Now, as the patch is updated, it is again ready for review. See the new ticket description for an account of what the patch does.



---

archive/issue_comments_080666.json:
```json
{
    "body": "There is quite a lot of work here. Thanks!\n\nCould you please coordinate this patch with #10318? That ticket already has a positive review, is related to #8807 and is incompatible with #8800.\n\nI have not read the code yet, but about problem 17. In which I participated partially I am not sure to like the solution.\n\n\n```\nsage: K.<r4> = NumberField(x^4-2)\nsage: L1.<r2_1> = NumberField(x^2-2, embedding = r4**2)\nsage: L2.<r2_2> = NumberField(x^2-2, embedding = -r4**2)\nsage: r2_1+r2_2    # indirect doctest\n0\nsage: (r2_1+r2_2).parent() is L1\nTrue\nsage: (r2_2+r2_1).parent() is L2\nTrue\n```\n\n\nNow I realise that there was some dicussion in sage-nt. Are there more examples in which the parent depends on the order of operands? I understand that this happen only where the parents are canonically isomorphic.",
    "created_at": "2010-12-06T11:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80666",
    "user": "@lftabera"
}
```

There is quite a lot of work here. Thanks!

Could you please coordinate this patch with #10318? That ticket already has a positive review, is related to #8807 and is incompatible with #8800.

I have not read the code yet, but about problem 17. In which I participated partially I am not sure to like the solution.


```
sage: K.<r4> = NumberField(x^4-2)
sage: L1.<r2_1> = NumberField(x^2-2, embedding = r4**2)
sage: L2.<r2_2> = NumberField(x^2-2, embedding = -r4**2)
sage: r2_1+r2_2    # indirect doctest
0
sage: (r2_1+r2_2).parent() is L1
True
sage: (r2_2+r2_1).parent() is L2
True
```


Now I realise that there was some dicussion in sage-nt. Are there more examples in which the parent depends on the order of operands? I understand that this happen only where the parents are canonically isomorphic.



---

archive/issue_comments_080667.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-06T11:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80667",
    "user": "@lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080668.json:
```json
{
    "body": "I should have read the threads before posting. I see that the bahaviour with different parents was already present in Sage for fields with embedding to CDF. So I have nothing to say about this.",
    "created_at": "2010-12-06T12:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80668",
    "user": "@lftabera"
}
```

I should have read the threads before posting. I see that the bahaviour with different parents was already present in Sage for fields with embedding to CDF. So I have nothing to say about this.



---

archive/issue_comments_080669.json:
```json
{
    "body": "Replying to [comment:37 lftabera]:\n> Could you please coordinate this patch with #10318? That ticket already has a positive review, is related to #8807 and is incompatible with #8800.\n\nOK, I'll try. I'm putting it into the \"work issues\" field.",
    "created_at": "2010-12-06T12:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80669",
    "user": "@simon-king-jena"
}
```

Replying to [comment:37 lftabera]:
> Could you please coordinate this patch with #10318? That ticket already has a positive review, is related to #8807 and is incompatible with #8800.

OK, I'll try. I'm putting it into the "work issues" field.



---

archive/issue_comments_080670.json:
```json
{
    "body": "Replying to [comment:39 SimonKing]:\n> Replying to [comment:37 lftabera]:\n> > Could you please coordinate this patch with #10318? That ticket already has a positive review, is related to #8807 and is incompatible with #8800.\n> \n> OK, I'll try. I'm putting it into the \"work issues\" field.\n\nI'm sorry that it was my trivial patch (spelling correction) which cased this.  A simple search-and-replace will be all that is required to make this patch apply after #10318.",
    "created_at": "2010-12-06T12:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80670",
    "user": "@JohnCremona"
}
```

Replying to [comment:39 SimonKing]:
> Replying to [comment:37 lftabera]:
> > Could you please coordinate this patch with #10318? That ticket already has a positive review, is related to #8807 and is incompatible with #8800.
> 
> OK, I'll try. I'm putting it into the "work issues" field.

I'm sorry that it was my trivial patch (spelling correction) which cased this.  A simple search-and-replace will be all that is required to make this patch apply after #10318.



---

archive/issue_comments_080671.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-06T13:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80671",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080672.json:
```json
{
    "body": "Replying to [comment:40 cremona]:\n> I'm sorry that it was my trivial patch (spelling correction) which cased this.  A simple search-and-replace will be all that is required to make this patch apply after #10318.\n\nYes, it seems that it was really to solve by a simple search-and-replace. The patch should now apply after #8807 and #10318. So, back to \"needs review\".\n\nBest regards,\n\nSimon",
    "created_at": "2010-12-06T13:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80672",
    "user": "@simon-king-jena"
}
```

Replying to [comment:40 cremona]:
> I'm sorry that it was my trivial patch (spelling correction) which cased this.  A simple search-and-replace will be all that is required to make this patch apply after #10318.

Yes, it seems that it was really to solve by a simple search-and-replace. The patch should now apply after #8807 and #10318. So, back to "needs review".

Best regards,

Simon



---

archive/issue_comments_080673.json:
```json
{
    "body": "Could one of you please test on 32 bit? I had to change the doc test of selmer_group: With my patch, I get on 64-bit the same output that was previously only expected on 32-bit. So, I could imagine that the expected output on 32-bit needs to be changed as well.\n\nCheers,\n\nSimon",
    "created_at": "2010-12-06T20:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80673",
    "user": "@simon-king-jena"
}
```

Could one of you please test on 32 bit? I had to change the doc test of selmer_group: With my patch, I get on 64-bit the same output that was previously only expected on 32-bit. So, I could imagine that the expected output on 32-bit needs to be changed as well.

Cheers,

Simon



---

archive/issue_comments_080674.json:
```json
{
    "body": "Replying to [comment:42 SimonKing]:\n> Could one of you please test on 32 bit? I had to change the doc test of selmer_group: With my patch, I get on 64-bit the same output that was previously only expected on 32-bit. So, I could imagine that the expected output on 32-bit needs to be changed as well.\n\nOK, will do -- it will on top of 4.6.1.alpha2 since I don't yet have a 32-bit build of alpha3.\n\n> \n> Cheers,\n> \n> Simon",
    "created_at": "2010-12-06T21:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80674",
    "user": "@JohnCremona"
}
```

Replying to [comment:42 SimonKing]:
> Could one of you please test on 32 bit? I had to change the doc test of selmer_group: With my patch, I get on 64-bit the same output that was previously only expected on 32-bit. So, I could imagine that the expected output on 32-bit needs to be changed as well.

OK, will do -- it will on top of 4.6.1.alpha2 since I don't yet have a 32-bit build of alpha3.

> 
> Cheers,
> 
> Simon



---

archive/issue_comments_080675.json:
```json
{
    "body": "Applies fine after #8807 and #10318.  Testing now: will take some time.\n\nI'm not sure that the buildbot will know how to apply just the last patch from #8807 and then the one from #10318.",
    "created_at": "2010-12-06T21:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80675",
    "user": "@JohnCremona"
}
```

Applies fine after #8807 and #10318.  Testing now: will take some time.

I'm not sure that the buildbot will know how to apply just the last patch from #8807 and then the one from #10318.



---

archive/issue_comments_080676.json:
```json
{
    "body": "Test failures:\n\n```\nsage -t  \"sage/groups/perm_gps/permgroup.py\"                \n**********************************************************************\nFile \"/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/groups/perm_gps/permgroup.py\", line 1114:\n    sage: G.random_element()\nExpected:\n    (2,3)(4,5)\nGot:\n    (1,2)(4,5)\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_34\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/john/.sage//tmp/.doctest_permgroup.py\n\t [7.8 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"sage/groups/perm_gps/permgroup.py\"\nTotal time for all tests: 7.9 seconds\njohn@John-laptop%sage -t  \"sage/rings/number_field/number_field.py\"\nsage -t  \"sage/rings/number_field/number_field.py\"          \nException RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored\nException GeneratorExit in <generator object <genexpr> at 0xc094e64> ignored\nException RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored\nException GeneratorExit in <generator object <genexpr> at 0xc094d74> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored\n**********************************************************************\nFile \"/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/rings/number_field/number_field.py\", line 2960:\n    sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)\nExpected:\n    [2, a + 1, a]    \nGot:\n    [2, a + 1, -a]\n**********************************************************************\n1 items had failures:\n   1 of  12 in __main__.example_62\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/john/.sage//tmp/.doctest_number_field.py\n\t [82.3 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"sage/rings/number_field/number_field.py\"\n```\n",
    "created_at": "2010-12-07T08:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80676",
    "user": "@JohnCremona"
}
```

Test failures:

```
sage -t  "sage/groups/perm_gps/permgroup.py"                
**********************************************************************
File "/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/groups/perm_gps/permgroup.py", line 1114:
    sage: G.random_element()
Expected:
    (2,3)(4,5)
Got:
    (1,2)(4,5)
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_34
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_permgroup.py
	 [7.8 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "sage/groups/perm_gps/permgroup.py"
Total time for all tests: 7.9 seconds
john@John-laptop%sage -t  "sage/rings/number_field/number_field.py"
sage -t  "sage/rings/number_field/number_field.py"          
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored
Exception GeneratorExit in <generator object <genexpr> at 0xc094e64> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored
Exception GeneratorExit in <generator object <genexpr> at 0xc094d74> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored
**********************************************************************
File "/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/rings/number_field/number_field.py", line 2960:
    sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
Expected:
    [2, a + 1, a]    
Got:
    [2, a + 1, -a]
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_62
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_number_field.py
	 [82.3 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "sage/rings/number_field/number_field.py"
```




---

archive/issue_comments_080677.json:
```json
{
    "body": "Hi John!\n\nIs that 32 or 64 bit? Because:\n\nReplying to [comment:45 cremona]:\n> sage -t  \"sage/groups/perm_gps/permgroup.py\"                \n> **********************************************************************\n> File \"/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/groups/perm_gps/permgroup.py\", line 1114:\n>     sage: G.random_element()\n> Expected:\n>     (2,3)(4,5)\n> Got:\n>     (1,2)(4,5)\n\nI changed the expected element. (1,2)(4,5) was originally expected, but I obtain (2,3)(4,5) on my machine (after applying the patch).\n\n> File \"/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/rings/number_field/number_field.py\", line 2960:\n>     sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)\n> Expected:\n>     [2, a + 1, a]    \n> Got:\n>     [2, a + 1, -a]\n\nThis one I also changed. [2, a + 1, -a] was originally expected with 64-bit. But after applying the patch, I got [2, a + 1, a], which was originally expected with 32-bit.\n\nStrange. What can one do to get a reproducible result?",
    "created_at": "2010-12-07T08:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80677",
    "user": "@simon-king-jena"
}
```

Hi John!

Is that 32 or 64 bit? Because:

Replying to [comment:45 cremona]:
> sage -t  "sage/groups/perm_gps/permgroup.py"                
> **********************************************************************
> File "/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/groups/perm_gps/permgroup.py", line 1114:
>     sage: G.random_element()
> Expected:
>     (2,3)(4,5)
> Got:
>     (1,2)(4,5)

I changed the expected element. (1,2)(4,5) was originally expected, but I obtain (2,3)(4,5) on my machine (after applying the patch).

> File "/home/john/sage-4.6.1.alpha2/devel/sage-main/sage/rings/number_field/number_field.py", line 2960:
>     sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
> Expected:
>     [2, a + 1, a]    
> Got:
>     [2, a + 1, -a]

This one I also changed. [2, a + 1, -a] was originally expected with 64-bit. But after applying the patch, I got [2, a + 1, a], which was originally expected with 32-bit.

Strange. What can one do to get a reproducible result?



---

archive/issue_comments_080678.json:
```json
{
    "body": "I got the same error in permgroup.py in both 32 and 64 bits. I got the permutation (1,2)(4,5) in two different machines with 4.6 + patches from this ticket.\n\nWe can investigate further what is going on, but I do not like this kind of tests against random_element. Even if we use the same seed. Is there a policy to deal with random_element methods?\n\nWhat about something like?\n\n\n```\nsage: a= G.random_element()\nsage: a in G\nTrue\nsage: a.parent() is G\nTrue\nsage: a**6\n()\n```\n\n\nAbout the errors in number_field all tests passes in 64 bits but I get the same errors as John in 32 bits. Concerning selmer group. Are both results right or only one of them?",
    "created_at": "2010-12-07T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80678",
    "user": "@lftabera"
}
```

I got the same error in permgroup.py in both 32 and 64 bits. I got the permutation (1,2)(4,5) in two different machines with 4.6 + patches from this ticket.

We can investigate further what is going on, but I do not like this kind of tests against random_element. Even if we use the same seed. Is there a policy to deal with random_element methods?

What about something like?


```
sage: a= G.random_element()
sage: a in G
True
sage: a.parent() is G
True
sage: a**6
()
```


About the errors in number_field all tests passes in 64 bits but I get the same errors as John in 32 bits. Concerning selmer group. Are both results right or only one of them?



---

archive/issue_comments_080679.json:
```json
{
    "body": "Replying to [comment:47 lftabera]:\n> I got the same error in permgroup.py in both 32 and 64 bits. I got the permutation (1,2)(4,5) in two different machines with 4.6 + patches from this ticket.\n\nReally strange.\n\n> We can investigate further what is going on, but I do not like this kind of tests against random_element. Even if we use the same seed.\n\nWell, we *do* use the same seed. So, it has to be reproducible.\n\n> What about something like?\n> \n> {{{\n> sage: a= G.random_element()\n> sage: a in G\n> True\n> sage: a.parent() is G\n> True\n> sage: a**6\n> ()\n> }}}\n\nI guess there is currently a related discussion at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c201930abdbd23d3)\n\n> About the errors in number_field all tests passes in 64 bits but I get the same errors as John in 32 bits. Concerning selmer group. Are both results right or only one of them?\n\nBoth are right. The method is supposed to return *a* generating set. And that is the case for both answers. And in the original version, the expected answer did depend on 32- versus 64-bit.\n\nBest regards,\n\nSimon",
    "created_at": "2010-12-07T09:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80679",
    "user": "@simon-king-jena"
}
```

Replying to [comment:47 lftabera]:
> I got the same error in permgroup.py in both 32 and 64 bits. I got the permutation (1,2)(4,5) in two different machines with 4.6 + patches from this ticket.

Really strange.

> We can investigate further what is going on, but I do not like this kind of tests against random_element. Even if we use the same seed.

Well, we *do* use the same seed. So, it has to be reproducible.

> What about something like?
> 
> {{{
> sage: a= G.random_element()
> sage: a in G
> True
> sage: a.parent() is G
> True
> sage: a**6
> ()
> }}}

I guess there is currently a related discussion at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c201930abdbd23d3)

> About the errors in number_field all tests passes in 64 bits but I get the same errors as John in 32 bits. Concerning selmer group. Are both results right or only one of them?

Both are right. The method is supposed to return *a* generating set. And that is the case for both answers. And in the original version, the expected answer did depend on 32- versus 64-bit.

Best regards,

Simon



---

archive/issue_comments_080680.json:
```json
{
    "body": "My tests were on 32-bit 4.6.1.alpha2.\n\nIn the Selmer group test both results are correct. It is very common for pari output to be different on 32- and 64-bit, and that the underlying this computation. The output numbers are generating a group which is abstractly (Z/3Z)3, so there is no unique generating set; and (worse) the elements themselves are representatives of cosets of K*/(K*)3.",
    "created_at": "2010-12-07T09:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80680",
    "user": "@JohnCremona"
}
```

My tests were on 32-bit 4.6.1.alpha2.

In the Selmer group test both results are correct. It is very common for pari output to be different on 32- and 64-bit, and that the underlying this computation. The output numbers are generating a group which is abstractly (Z/3Z)3, so there is no unique generating set; and (worse) the elements themselves are representatives of cosets of K*/(K*)3.



---

archive/issue_comments_080681.json:
```json
{
    "body": "Hi John!\n\nReplying to [comment:49 cremona]:\n> My tests were on 32-bit 4.6.1.alpha2.\n\nOK, that means that the results on 32-bit and on 64-bit are switched: I get on 64-bit the result that was previously expected on 32-bit, and you get on 32-bit the result that was previously expected on 64-bit. Or am I confusing things?",
    "created_at": "2010-12-07T09:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80681",
    "user": "@simon-king-jena"
}
```

Hi John!

Replying to [comment:49 cremona]:
> My tests were on 32-bit 4.6.1.alpha2.

OK, that means that the results on 32-bit and on 64-bit are switched: I get on 64-bit the result that was previously expected on 32-bit, and you get on 32-bit the result that was previously expected on 64-bit. Or am I confusing things?



---

archive/issue_comments_080682.json:
```json
{
    "body": "It is surely possible that there are other differences between alpha2 and alpha3, so perhaps I should test again when I have built alpha3.  I just started that.  (This is a different machine -- my desktop at work -- than the one I tested alpha2 on, which was my laptop at home).",
    "created_at": "2010-12-07T09:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80682",
    "user": "@JohnCremona"
}
```

It is surely possible that there are other differences between alpha2 and alpha3, so perhaps I should test again when I have built alpha3.  I just started that.  (This is a different machine -- my desktop at work -- than the one I tested alpha2 on, which was my laptop at home).



---

archive/issue_comments_080683.json:
```json
{
    "body": "Replying to [comment:51 cremona]:\n> It is surely possible that there are other differences between alpha2 and alpha3, so perhaps I should test again when I have built alpha3.  I just started that.  (This is a different machine -- my desktop at work -- than the one I tested alpha2 on, which was my laptop at home).\n> \n\nEven more confusing...\n\nBy the way, I tested based on sage-4.6, so, no alpha version.",
    "created_at": "2010-12-07T10:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80683",
    "user": "@simon-king-jena"
}
```

Replying to [comment:51 cremona]:
> It is surely possible that there are other differences between alpha2 and alpha3, so perhaps I should test again when I have built alpha3.  I just started that.  (This is a different machine -- my desktop at work -- than the one I tested alpha2 on, which was my laptop at home).
> 

Even more confusing...

By the way, I tested based on sage-4.6, so, no alpha version.



---

archive/issue_comments_080684.json:
```json
{
    "body": "I just tested on a different 32-bit machine on which I have just built 4.6.1.alpha3 (and all tests passed):  Same failure as before for sage/groups/perm_gps/permgroup.py, and for sage/groups/perm_gps/permgroup.py\n\nThe second one of these is the more worrying in that it goes into an infinite recursion.",
    "created_at": "2010-12-07T14:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80684",
    "user": "@JohnCremona"
}
```

I just tested on a different 32-bit machine on which I have just built 4.6.1.alpha3 (and all tests passed):  Same failure as before for sage/groups/perm_gps/permgroup.py, and for sage/groups/perm_gps/permgroup.py

The second one of these is the more worrying in that it goes into an infinite recursion.



---

archive/issue_comments_080685.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-07T14:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80685",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080686.json:
```json
{
    "body": "Hi John,\n\nReplying to [comment:53 cremona]:\n> I just tested on a different 32-bit machine on which I have just built 4.6.1.alpha3 (and all tests passed):  Same failure as before for sage/groups/perm_gps/permgroup.py, and for sage/groups/perm_gps/permgroup.py\n> \n> The second one of these is the more worrying in that it goes into an infinite recursion.\n\nI wonder if the recursion comes from the testing framework. Once, I observed such recursion in a test, but I could not reproduce it in  an interactive session. In addition, I got a return value different from the expected - and when I changed the expected  value in the test, the recursion disappeared as well.\n\nCould you change the expected 32-bit value in the test of selmer_group to the value that you get in an interactive session, and then try `sage -t  \"sage/rings/number_field/number_field.py\"` again?\n\nCheers,\n\nSimon",
    "created_at": "2010-12-07T16:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80686",
    "user": "@simon-king-jena"
}
```

Hi John,

Replying to [comment:53 cremona]:
> I just tested on a different 32-bit machine on which I have just built 4.6.1.alpha3 (and all tests passed):  Same failure as before for sage/groups/perm_gps/permgroup.py, and for sage/groups/perm_gps/permgroup.py
> 
> The second one of these is the more worrying in that it goes into an infinite recursion.

I wonder if the recursion comes from the testing framework. Once, I observed such recursion in a test, but I could not reproduce it in  an interactive session. In addition, I got a return value different from the expected - and when I changed the expected  value in the test, the recursion disappeared as well.

Could you change the expected 32-bit value in the test of selmer_group to the value that you get in an interactive session, and then try `sage -t  "sage/rings/number_field/number_field.py"` again?

Cheers,

Simon



---

archive/issue_comments_080687.json:
```json
{
    "body": "OK, I tried that.  Now all tests pass.  The relevant lines now look like\n\n```\n            sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)\n            [2, a + 1, -a]    # 32-bit\n            [2, a + 1, a]   # 64-bit\n```\n\nwhile before the two expected outputs were the same despite the separation into 32 and 64 bit cases.  Was this just a typo?\n\nThere is still no explanation for why, when the expected and actual output differed, there was that infinite recursion.",
    "created_at": "2010-12-07T18:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80687",
    "user": "@JohnCremona"
}
```

OK, I tried that.  Now all tests pass.  The relevant lines now look like

```
            sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
            [2, a + 1, -a]    # 32-bit
            [2, a + 1, a]   # 64-bit
```

while before the two expected outputs were the same despite the separation into 32 and 64 bit cases.  Was this just a typo?

There is still no explanation for why, when the expected and actual output differed, there was that infinite recursion.



---

archive/issue_comments_080688.json:
```json
{
    "body": "Replying to [comment:55 cremona]:\n> while before the two expected outputs were the same despite the separation into 32 and 64 bit cases.  Was this just a typo?\n\nNo. I simply have no 32-bit machine and couldn't test it. That's why I asked that some of you please test on 32-bit.\n \n> There is still no explanation for why, when the expected and actual output differed, there was that infinite recursion.\n\nYes. But it seems to me that it is located in the doctest framework.\n\nSo, unless you find more issues, I will post another patch that changes the expected value in case of 32-bit.\n\nCheers,\n\nSimon",
    "created_at": "2010-12-07T18:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80688",
    "user": "@simon-king-jena"
}
```

Replying to [comment:55 cremona]:
> while before the two expected outputs were the same despite the separation into 32 and 64 bit cases.  Was this just a typo?

No. I simply have no 32-bit machine and couldn't test it. That's why I asked that some of you please test on 32-bit.
 
> There is still no explanation for why, when the expected and actual output differed, there was that infinite recursion.

Yes. But it seems to me that it is located in the doctest framework.

So, unless you find more issues, I will post another patch that changes the expected value in case of 32-bit.

Cheers,

Simon



---

archive/issue_comments_080689.json:
```json
{
    "body": "> \n> So, unless you find more issues, I will post another patch that changes the expected value in case of 32-bit.\n\nGo for it!",
    "created_at": "2010-12-07T19:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80689",
    "user": "@JohnCremona"
}
```

> 
> So, unless you find more issues, I will post another patch that changes the expected value in case of 32-bit.

Go for it!



---

archive/issue_comments_080690.json:
```json
{
    "body": "I confirm that changing the doctest makes all doctest pass.\n\nHowever, with the coercion of embedded and non embedded number fields, now addition is not associative.\n\n\n```\nsage: K1.<r1>=NumberField(x^2-2)\nsage: K2.<r2>=NumberField(x^2-2, embedding=1)\nsage: K3.<r3>=NumberField(x^2-2, embedding=-1)\nsage: (r1+r2)+r3\n3*r1\nsage: r1+(r2+r3)\nr1\n```\n\n\nr1+r2 is ambiguous. So either this operation should raise an error or it should add an embedding to K1 compatible with K2. But as far as I understand the coercion model the latter is not possible.",
    "created_at": "2010-12-07T20:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80690",
    "user": "@lftabera"
}
```

I confirm that changing the doctest makes all doctest pass.

However, with the coercion of embedded and non embedded number fields, now addition is not associative.


```
sage: K1.<r1>=NumberField(x^2-2)
sage: K2.<r2>=NumberField(x^2-2, embedding=1)
sage: K3.<r3>=NumberField(x^2-2, embedding=-1)
sage: (r1+r2)+r3
3*r1
sage: r1+(r2+r3)
r1
```


r1+r2 is ambiguous. So either this operation should raise an error or it should add an embedding to K1 compatible with K2. But as far as I understand the coercion model the latter is not possible.



---

archive/issue_comments_080691.json:
```json
{
    "body": "Replying to [comment:58 lftabera]:\n> I confirm that changing the doctest makes all doctest pass.\n\nGood!\n\n> However, with the coercion of embedded and non embedded number fields, now addition is not associative.\n> \n> {{{\n> sage: K1.<r1>=NumberField(x^2-2)\n> sage: K2.<r2>=NumberField(x^2-2, embedding=1)\n> sage: K3.<r3>=NumberField(x^2-2, embedding=-1)\n> sage: (r1+r2)+r3\n> 3*r1\n> sage: r1+(r2+r3)\n> r1\n> }}}\n> \n> r1+r2 is ambiguous. So either this operation should raise an error or it should add an embedding to K1 compatible with K2. But as far as I understand the coercion model the latter is not possible.\n\nI disagree: It should not raise an error. This is a side-effect of Sage's coercion model. We (see discussion on sage-nt) do want a forgetful coercion from K2 to K1 and from K3 to K1; and we want a coercion between two embedded number fields induced by the embedding.\n\nHence, we have a coercion between K2 and K3 sending `r3` to `-r2`. Therefore `r2+r3` is `K2.zero()`, thus, `r1+(r2+r3)==r1`. On the other hand, `r1+r2` is `2*r1`, since the coercion from K2 to K1 sends `r2` to `r1`; and similarly `r3` is sent to `r1`, hence `(r1+r2)+r3==3*r1`.\n\nBut I suggest to discuss on sage-algebra whether people are really happy with that consequence of a forgetful coercion.",
    "created_at": "2010-12-07T20:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80691",
    "user": "@simon-king-jena"
}
```

Replying to [comment:58 lftabera]:
> I confirm that changing the doctest makes all doctest pass.

Good!

> However, with the coercion of embedded and non embedded number fields, now addition is not associative.
> 
> {{{
> sage: K1.<r1>=NumberField(x^2-2)
> sage: K2.<r2>=NumberField(x^2-2, embedding=1)
> sage: K3.<r3>=NumberField(x^2-2, embedding=-1)
> sage: (r1+r2)+r3
> 3*r1
> sage: r1+(r2+r3)
> r1
> }}}
> 
> r1+r2 is ambiguous. So either this operation should raise an error or it should add an embedding to K1 compatible with K2. But as far as I understand the coercion model the latter is not possible.

I disagree: It should not raise an error. This is a side-effect of Sage's coercion model. We (see discussion on sage-nt) do want a forgetful coercion from K2 to K1 and from K3 to K1; and we want a coercion between two embedded number fields induced by the embedding.

Hence, we have a coercion between K2 and K3 sending `r3` to `-r2`. Therefore `r2+r3` is `K2.zero()`, thus, `r1+(r2+r3)==r1`. On the other hand, `r1+r2` is `2*r1`, since the coercion from K2 to K1 sends `r2` to `r1`; and similarly `r3` is sent to `r1`, hence `(r1+r2)+r3==3*r1`.

But I suggest to discuss on sage-algebra whether people are really happy with that consequence of a forgetful coercion.



---

archive/issue_comments_080692.json:
```json
{
    "body": "Replying to [comment:58 lftabera]:\n> However, with the coercion of embedded and non embedded number fields, now addition is not associative.\n\nAs you (? I guess `luisfe == lftabera`) pointed out at [sage-algebra](http://groups.google.com/group/sage-algebra/browse_thread/thread/889464bee6a6a036), the actual problem is not the non-associativity of the addition (after all, we have different algebraic structures involved, so, there is no reason to expect that it can be globally extended to something that is associative).\n\nYou convinced me that the actual problem is the fact that the coercions in your example do not form a commuting triangle: Coercion from `K3` to `K2` followed by forgetful coercion from `K2` to `K1` is not the same as the forgetful coercion from `K3` to `K1`.\n\nHence, I have to modify the `_coerce_map_from_` of number fields and probably also the merge method of `AlgebraicExtensionFunctor`.",
    "created_at": "2010-12-08T07:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80692",
    "user": "@simon-king-jena"
}
```

Replying to [comment:58 lftabera]:
> However, with the coercion of embedded and non embedded number fields, now addition is not associative.

As you (? I guess `luisfe == lftabera`) pointed out at [sage-algebra](http://groups.google.com/group/sage-algebra/browse_thread/thread/889464bee6a6a036), the actual problem is not the non-associativity of the addition (after all, we have different algebraic structures involved, so, there is no reason to expect that it can be globally extended to something that is associative).

You convinced me that the actual problem is the fact that the coercions in your example do not form a commuting triangle: Coercion from `K3` to `K2` followed by forgetful coercion from `K2` to `K1` is not the same as the forgetful coercion from `K3` to `K1`.

Hence, I have to modify the `_coerce_map_from_` of number fields and probably also the merge method of `AlgebraicExtensionFunctor`.



---

archive/issue_comments_080693.json:
```json
{
    "body": "I removed the \"forgetful coercions\" and changed the documentation and the ticket description accordingly.\n\nI modified the 32-bit expected value of selmer_group according to your findings (but please test if it really works 32-bit; I only tested 64-bit).\n\nI modified the annoying random_element test in permgroup.py as Luis suggested.\n\nHence, I think it is ready for review again!",
    "created_at": "2010-12-08T09:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80693",
    "user": "@simon-king-jena"
}
```

I removed the "forgetful coercions" and changed the documentation and the ticket description accordingly.

I modified the 32-bit expected value of selmer_group according to your findings (but please test if it really works 32-bit; I only tested 64-bit).

I modified the annoying random_element test in permgroup.py as Luis suggested.

Hence, I think it is ready for review again!



---

archive/issue_comments_080694.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-08T09:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80694",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080695.json:
```json
{
    "body": "depends on #8807 #10318",
    "created_at": "2010-12-08T10:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80695",
    "user": "@simon-king-jena"
}
```

depends on #8807 #10318



---

archive/issue_comments_080696.json:
```json
{
    "body": "I confirm that the new patch applies to 32-bits linux and long doctest passes. I have not read the code yet.",
    "created_at": "2010-12-09T09:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80696",
    "user": "@lftabera"
}
```

I confirm that the new patch applies to 32-bits linux and long doctest passes. I have not read the code yet.



---

archive/issue_comments_080697.json:
```json
{
    "body": "Replying to [comment:65 lftabera]:\n> I confirm that the new patch applies to 32-bits linux and long doctest passes. I have not read the code yet.\n\nCould the doctests be repeated, please? I just did it on my machine, based on `sage-4.6.1.alpha3`, and again the problem is the doctest for `selmer_group`. Recall that in the original patch I had to switch the expected values for 32- and 64-bit. And now, with `sage-4.6.1.alpha3`, I get again the value that was originally expected without the patch.\n\nTherefore I'll replace the patch again, in a few minutes. Please test!",
    "created_at": "2010-12-29T20:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80697",
    "user": "@simon-king-jena"
}
```

Replying to [comment:65 lftabera]:
> I confirm that the new patch applies to 32-bits linux and long doctest passes. I have not read the code yet.

Could the doctests be repeated, please? I just did it on my machine, based on `sage-4.6.1.alpha3`, and again the problem is the doctest for `selmer_group`. Recall that in the original patch I had to switch the expected values for 32- and 64-bit. And now, with `sage-4.6.1.alpha3`, I get again the value that was originally expected without the patch.

Therefore I'll replace the patch again, in a few minutes. Please test!



---

archive/issue_comments_080698.json:
```json
{
    "body": "I really don't see what the patchbot was complaining about. The old patch did apply to `sage-4.6.2.alpha0` with just a little fuzz.\n\nAnyway, I refreshed it. The dependencies of the ticket are already merged in `sage-4.6.2.alpha0`, so, it should now apply cleanly.\n\nPlease, try to review it! I really think that fixing so many bugs and providing full doctest coverage of a large chunk of the coercion machinery is worth the effort.",
    "created_at": "2011-01-29T09:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80698",
    "user": "@simon-king-jena"
}
```

I really don't see what the patchbot was complaining about. The old patch did apply to `sage-4.6.2.alpha0` with just a little fuzz.

Anyway, I refreshed it. The dependencies of the ticket are already merged in `sage-4.6.2.alpha0`, so, it should now apply cleanly.

Please, try to review it! I really think that fixing so many bugs and providing full doctest coverage of a large chunk of the coercion machinery is worth the effort.



---

archive/issue_comments_080699.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-02-14T14:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80699",
    "user": "@lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080700.json:
```json
{
    "body": "Hi Simon,\n\nI am reading the code, it is a long patch but looks good, thanks for the work done.\n\nI have a question about functor AlgebraicExtensionFunctor and ZZ. According to the documentation:\n\nWhen applying a number field constructor to the ring of integers, the maximal order in the number field is returned::\n\nWhy is this chosen instead of ZZ[x]/polynomial?\n\nActually, the code does not follow the documentation except for CyclotomicField:\n\n\n```\nsage: N = NumberField(x^2 - 5, 'a')\nsage: F, R = N.construction()\nsage: F(ZZ).gens()\n[1, a]\nsage: F(ZZ).is_maximal()\nFalse\nsage: N.maximal_order().gens()\n[1/2*a + 1/2, a]\n```\n\n\nI add a patch that contains some small improvements (in my opinion). A couple of small tests and some style. Plase consider merging some of these changes. For example, in the code you usually write:\n\nreturn\n\ninstead of \n\nreturn None\n\nBoth are correct but, unless there are other reasons I am unaware, the second looks more readable to me (just an opinion).\n\nI have not yet finish to review the whole patch, so you may consider waiting untill I am done. I have to compile the documentation and check that the list of bugs you have solved appears in the TESTS of the patch.",
    "created_at": "2011-02-14T14:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80700",
    "user": "@lftabera"
}
```

Hi Simon,

I am reading the code, it is a long patch but looks good, thanks for the work done.

I have a question about functor AlgebraicExtensionFunctor and ZZ. According to the documentation:

When applying a number field constructor to the ring of integers, the maximal order in the number field is returned::

Why is this chosen instead of ZZ[x]/polynomial?

Actually, the code does not follow the documentation except for CyclotomicField:


```
sage: N = NumberField(x^2 - 5, 'a')
sage: F, R = N.construction()
sage: F(ZZ).gens()
[1, a]
sage: F(ZZ).is_maximal()
False
sage: N.maximal_order().gens()
[1/2*a + 1/2, a]
```


I add a patch that contains some small improvements (in my opinion). A couple of small tests and some style. Plase consider merging some of these changes. For example, in the code you usually write:

return

instead of 

return None

Both are correct but, unless there are other reasons I am unaware, the second looks more readable to me (just an opinion).

I have not yet finish to review the whole patch, so you may consider waiting untill I am done. I have to compile the documentation and check that the list of bugs you have solved appears in the TESTS of the patch.



---

archive/issue_comments_080701.json:
```json
{
    "body": "Hi Luis,\n\nFirst of all, thank you for looking at the patch and finding so many typos.\n\nReplying to [comment:68 lftabera]:\n> I have a question about functor AlgebraicExtensionFunctor and ZZ. According to the documentation:\n> \n> When applying a number field constructor to the ring of integers, the maximal order in the number field is returned::\n> \n> Why is this chosen instead of ZZ[x]/polynomial?\n\nThat is how currently extensions of `ZZ` behave:\n\n```\nsage: ZZ.extension(x^2+3*x+1,names=['y'])\nOrder in Number Field in y with defining polynomial x^2 + 3*x + 1\n```\n\nSo, it wasn't my idea; the construction functor is merely mimicking what the `extension` method of `ZZ` was doing anyway. \n\n> Actually, the code does not follow the documentation except for CyclotomicField:\n> \n> {{{\n> sage: N = NumberField(x^2 - 5, 'a')\n> sage: F, R = N.construction()\n> sage: F(ZZ).gens()\n> [1, a]\n> sage: F(ZZ).is_maximal()\n> False\n> sage: N.maximal_order().gens()\n> [1/2*a + 1/2, a]\n> }}}\n\nAgain, this is what `ZZ.extension` currently does:\n\n```\nsage: ZZ.extension(x^2 - 5, 'a').is_maximal()\nFalse\n```\n\n\nBut I don't understand why that contradicts the documentation? Is it since I wrote \"Note that the construction functor of a number field returns the order of that field\"? *The* order?\n\nPerhaps I should better write \"Note that the construction functor of a number field applied to the integers returns an order of that field, similar to the behaviour of `ZZ.extension`\"?\n\n\n> I add a patch that contains some small improvements (in my opinion). A couple of small tests and some style. Plase consider merging some of these changes.\n\nI agree with all changes that you suggest in your \"some_ideas\" patch - so, once you're done, please promote it to a referee patch!\n\nBest regards,\n\nSimon",
    "created_at": "2011-02-14T15:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80701",
    "user": "@simon-king-jena"
}
```

Hi Luis,

First of all, thank you for looking at the patch and finding so many typos.

Replying to [comment:68 lftabera]:
> I have a question about functor AlgebraicExtensionFunctor and ZZ. According to the documentation:
> 
> When applying a number field constructor to the ring of integers, the maximal order in the number field is returned::
> 
> Why is this chosen instead of ZZ[x]/polynomial?

That is how currently extensions of `ZZ` behave:

```
sage: ZZ.extension(x^2+3*x+1,names=['y'])
Order in Number Field in y with defining polynomial x^2 + 3*x + 1
```

So, it wasn't my idea; the construction functor is merely mimicking what the `extension` method of `ZZ` was doing anyway. 

> Actually, the code does not follow the documentation except for CyclotomicField:
> 
> {{{
> sage: N = NumberField(x^2 - 5, 'a')
> sage: F, R = N.construction()
> sage: F(ZZ).gens()
> [1, a]
> sage: F(ZZ).is_maximal()
> False
> sage: N.maximal_order().gens()
> [1/2*a + 1/2, a]
> }}}

Again, this is what `ZZ.extension` currently does:

```
sage: ZZ.extension(x^2 - 5, 'a').is_maximal()
False
```


But I don't understand why that contradicts the documentation? Is it since I wrote "Note that the construction functor of a number field returns the order of that field"? *The* order?

Perhaps I should better write "Note that the construction functor of a number field applied to the integers returns an order of that field, similar to the behaviour of `ZZ.extension`"?


> I add a patch that contains some small improvements (in my opinion). A couple of small tests and some style. Plase consider merging some of these changes.

I agree with all changes that you suggest in your "some_ideas" patch - so, once you're done, please promote it to a referee patch!

Best regards,

Simon



---

archive/issue_comments_080702.json:
```json
{
    "body": "Ok, current behaviur is what I would expect. But then there is a typo in \nAlgebraicExtensionFunctor.__init__ which is where the documentation claims that returs the maximal order. Lines 2223 and 2224 of your patch:\n\n\n```\n+        When applying a number field constructor to the ring of integers,\n+        the maximal order in the number field is returned::\n```\n",
    "created_at": "2011-02-14T15:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80702",
    "user": "@lftabera"
}
```

Ok, current behaviur is what I would expect. But then there is a typo in 
AlgebraicExtensionFunctor.__init__ which is where the documentation claims that returs the maximal order. Lines 2223 and 2224 of your patch:


```
+        When applying a number field constructor to the ring of integers,
+        the maximal order in the number field is returned::
```




---

archive/issue_comments_080703.json:
```json
{
    "body": "Replying to [comment:70 lftabera]:\n> Ok, current behaviur is what I would expect. But then there is a typo in \n> AlgebraicExtensionFunctor.__init__ which is where the documentation claims that returs the maximal order. Lines 2223 and 2224 of your patch:\n\nThanks! That ought to change, then. I only found the other place, where I wrote \"the order\" rather than \"an order\".",
    "created_at": "2011-02-14T15:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80703",
    "user": "@simon-king-jena"
}
```

Replying to [comment:70 lftabera]:
> Ok, current behaviur is what I would expect. But then there is a typo in 
> AlgebraicExtensionFunctor.__init__ which is where the documentation claims that returs the maximal order. Lines 2223 and 2224 of your patch:

Thanks! That ought to change, then. I only found the other place, where I wrote "the order" rather than "an order".



---

archive/issue_comments_080704.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-14T16:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80704",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080705.json:
```json
{
    "body": "Dear Luis,\n\nReplying to [comment:71 SimonKing]:\n> Replying to [comment:70 lftabera]:\n> > Ok, current behaviur is what I would expect. But then there is a typo in \n> > AlgebraicExtensionFunctor.__init__ which is where the documentation claims that returs the maximal order. Lines 2223 and 2224 of your patch:\n> \n> Thanks! That ought to change, then. I only found the other place, where I wrote \"the order\" rather than \"an order\".\n\nThis is now fixed.\n\nI change the ticket status into \"needs review\" again, since I believe the other typos can be fixed with your reviewer patch.",
    "created_at": "2011-02-14T16:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80705",
    "user": "@simon-king-jena"
}
```

Dear Luis,

Replying to [comment:71 SimonKing]:
> Replying to [comment:70 lftabera]:
> > Ok, current behaviur is what I would expect. But then there is a typo in 
> > AlgebraicExtensionFunctor.__init__ which is where the documentation claims that returs the maximal order. Lines 2223 and 2224 of your patch:
> 
> Thanks! That ought to change, then. I only found the other place, where I wrote "the order" rather than "an order".

This is now fixed.

I change the ticket status into "needs review" again, since I believe the other typos can be fixed with your reviewer patch.



---

archive/issue_comments_080706.json:
```json
{
    "body": "Simon,\n\nWhat is the reason for the following change?\n\n\n```\ndiff -r f71dd979f978 -r 7097db76160e sage/rings/rational_field.py\n--- a/sage/rings/rational_field.py\tFri Dec 10 14:50:18 2010 +0100\n+++ b/sage/rings/rational_field.py\tWed Jul 21 14:25:41 2010 +0100\n@@ -253,7 +253,7 @@\n         import integer_ring\n         return FractionField(), integer_ring.ZZ\n         \n-    def completion(self, p, prec, extras = {}):\n+    def completion(self, p, prec, extras):\n```\n\n\nIn the completion method of the RationalField. I think it is an error to eliminate the default extras = {}. It is not a mandatory argument neither for Qp not for create_RealField and the user has no idea of what to put there (QQ.completion has no documentation, which is a bug, but not for this ticket)\n\nLuis",
    "created_at": "2011-02-16T18:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80706",
    "user": "@lftabera"
}
```

Simon,

What is the reason for the following change?


```
diff -r f71dd979f978 -r 7097db76160e sage/rings/rational_field.py
--- a/sage/rings/rational_field.py	Fri Dec 10 14:50:18 2010 +0100
+++ b/sage/rings/rational_field.py	Wed Jul 21 14:25:41 2010 +0100
@@ -253,7 +253,7 @@
         import integer_ring
         return FractionField(), integer_ring.ZZ
         
-    def completion(self, p, prec, extras = {}):
+    def completion(self, p, prec, extras):
```


In the completion method of the RationalField. I think it is an error to eliminate the default extras = {}. It is not a mandatory argument neither for Qp not for create_RealField and the user has no idea of what to put there (QQ.completion has no documentation, which is a bug, but not for this ticket)

Luis



---

archive/issue_comments_080707.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-02-16T18:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80707",
    "user": "@lftabera"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_080708.json:
```json
{
    "body": "Hi Luis,\n\nReplying to [comment:73 lftabera]:\n> What is the reason for the following change?\n> \n>...\n>\n> In the completion method of the RationalField. I think it is an error to eliminate the default extras = {}.\n\nI have not the faintest idea why I did that change. Probably it was by accident. I'll try to revert that change and see if tests still pass.\n\nCheers, Simon",
    "created_at": "2011-02-16T18:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80708",
    "user": "@simon-king-jena"
}
```

Hi Luis,

Replying to [comment:73 lftabera]:
> What is the reason for the following change?
> 
>...
>
> In the completion method of the RationalField. I think it is an error to eliminate the default extras = {}.

I have not the faintest idea why I did that change. Probably it was by accident. I'll try to revert that change and see if tests still pass.

Cheers, Simon



---

archive/issue_comments_080709.json:
```json
{
    "body": "Apply 8800_functor_pushout_doc_and_fixes.patch some_ideas.patch\n\n(For the patchbot, if that's necessary)",
    "created_at": "2011-02-16T20:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80709",
    "user": "@simon-king-jena"
}
```

Apply 8800_functor_pushout_doc_and_fixes.patch some_ideas.patch

(For the patchbot, if that's necessary)



---

archive/issue_comments_080710.json:
```json
{
    "body": "I reverted the obscure \"extras\" issue. That was no problem.\n\nI had to change two doctests that used the \".transpose()\" method for vectors, which is now deprecated. With the new patch applied to sage-4.6.2.alpha4, the long doctests pass on my machine.\n\nPresumably, your \"some_ideas.patch\" will become a reviewer patch, thus I told the  patchbot to apply it.\n\nBest regards,\n\nSimon",
    "created_at": "2011-02-16T20:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80710",
    "user": "@simon-king-jena"
}
```

I reverted the obscure "extras" issue. That was no problem.

I had to change two doctests that used the ".transpose()" method for vectors, which is now deprecated. With the new patch applied to sage-4.6.2.alpha4, the long doctests pass on my machine.

Presumably, your "some_ideas.patch" will become a reviewer patch, thus I told the  patchbot to apply it.

Best regards,

Simon



---

archive/issue_comments_080711.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-02-16T20:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80711",
    "user": "@simon-king-jena"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_080712.json:
```json
{
    "body": "FWIW, the doctest failure reported by the patchbot comes from the fact that the vector method \".column()\" seems to be a feature only introduced in 4.6.2.alpha2, replacing the now deprecated \".transpose()\".",
    "created_at": "2011-02-17T07:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80712",
    "user": "@simon-king-jena"
}
```

FWIW, the doctest failure reported by the patchbot comes from the fact that the vector method ".column()" seems to be a feature only introduced in 4.6.2.alpha2, replacing the now deprecated ".transpose()".



---

archive/issue_comments_080713.json:
```json
{
    "body": "Ideas to consider merging",
    "created_at": "2011-02-18T16:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80713",
    "user": "@lftabera"
}
```

Ideas to consider merging



---

archive/issue_comments_080714.json:
```json
{
    "body": "Attachment [some_ideas.patch](tarball://root/attachments/some-uuid/ticket8800/some_ideas.patch) by @lftabera created at 2011-02-18 16:44:13\n\nThe documentation of pushout is not built in the reference manual. I have added pushout.py to categories.rst, but I get warnings and errors in the html and pdf built that I do not know how to solve.",
    "created_at": "2011-02-18T16:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80714",
    "user": "@lftabera"
}
```

Attachment [some_ideas.patch](tarball://root/attachments/some-uuid/ticket8800/some_ideas.patch) by @lftabera created at 2011-02-18 16:44:13

The documentation of pushout is not built in the reference manual. I have added pushout.py to categories.rst, but I get warnings and errors in the html and pdf built that I do not know how to solve.



---

archive/issue_comments_080715.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-02-18T16:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80715",
    "user": "@lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080716.json:
```json
{
    "body": "I just updated my patch, also merging your some_ideas.patch. The documentation seemed to build without problems (which required some editing). I am afraid I will probably be unable to see the documentation for the next ten days, as I will not be in my office.\n\nBut then I made a big mistake: I also included an autogenerated file into the repository, namely doc/en/reference/sage/categories/pushout.rst. When I noticed it and tried to `hg delete` it, apparently I managed to kill the entire documentation. I don't know whether I will recover from that stroke, because even `sage -docbuild reference html` did not help.\n\nBut perhaps you will be able to (1) see whether the documentation of sage.categories.pushout looks nice and (2) correct my patch?\n\nApply 8800_functor_pushout_doc_and_fixes.patch",
    "created_at": "2011-02-18T20:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80716",
    "user": "@simon-king-jena"
}
```

I just updated my patch, also merging your some_ideas.patch. The documentation seemed to build without problems (which required some editing). I am afraid I will probably be unable to see the documentation for the next ten days, as I will not be in my office.

But then I made a big mistake: I also included an autogenerated file into the repository, namely doc/en/reference/sage/categories/pushout.rst. When I noticed it and tried to `hg delete` it, apparently I managed to kill the entire documentation. I don't know whether I will recover from that stroke, because even `sage -docbuild reference html` did not help.

But perhaps you will be able to (1) see whether the documentation of sage.categories.pushout looks nice and (2) correct my patch?

Apply 8800_functor_pushout_doc_and_fixes.patch



---

archive/issue_comments_080717.json:
```json
{
    "body": "I think I solved the trouble with the reference manual. The new patch includes the some_ideas patch. So, only one patch needs to be applied.\n\nWith the patch, the references for sage.categories.pushout build, and no warning or error is raised. But I am currently not able to watch the result (this will take more than one week). So, I ask the reviewer to have a look on it.\n\nTo be on the safe side, I am now running doc tests (at least, `sage -tp 4 doc/en` passes). But I think I can revert it to \"needs review\".",
    "created_at": "2011-02-19T08:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80717",
    "user": "@simon-king-jena"
}
```

I think I solved the trouble with the reference manual. The new patch includes the some_ideas patch. So, only one patch needs to be applied.

With the patch, the references for sage.categories.pushout build, and no warning or error is raised. But I am currently not able to watch the result (this will take more than one week). So, I ask the reviewer to have a look on it.

To be on the safe side, I am now running doc tests (at least, `sage -tp 4 doc/en` passes). But I think I can revert it to "needs review".



---

archive/issue_comments_080718.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-19T08:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80718",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080719.json:
```json
{
    "body": "Apply 8800_functor_pushout_doc_and_fixes.patch \n\n(for the patchbot)",
    "created_at": "2011-02-19T08:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80719",
    "user": "@simon-king-jena"
}
```

Apply 8800_functor_pushout_doc_and_fixes.patch 

(for the patchbot)



---

archive/issue_comments_080720.json:
```json
{
    "body": "All long tests pass if one applies the patch to sage-4.6.2.alpha4. The patchbot uses sage-4.6.1, that's why it finds two errors.",
    "created_at": "2011-02-19T16:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80720",
    "user": "@simon-king-jena"
}
```

All long tests pass if one applies the patch to sage-4.6.2.alpha4. The patchbot uses sage-4.6.1, that's why it finds two errors.



---

archive/issue_comments_080721.json:
```json
{
    "body": "Attachment [referee.patch](tarball://root/attachments/some-uuid/ticket8800/referee.patch) by @lftabera created at 2011-02-26 11:29:16\n\nI have tested with sage-4.6.1.rc0 the documentation builds and looks good. The bugs have been corrected and the patch introduces some very nice features. Good work. Positive review to Simon's patch.\n\nHowever, I have added a referee patch with some minor changes in the documentation. I have eliminated some latex code that, in my opinion, made the documentation harder to read.\n\nSimon, could you look at my patch? If you feel it is ok, put a positive review.",
    "created_at": "2011-02-26T11:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80721",
    "user": "@lftabera"
}
```

Attachment [referee.patch](tarball://root/attachments/some-uuid/ticket8800/referee.patch) by @lftabera created at 2011-02-26 11:29:16

I have tested with sage-4.6.1.rc0 the documentation builds and looks good. The bugs have been corrected and the patch introduces some very nice features. Good work. Positive review to Simon's patch.

However, I have added a referee patch with some minor changes in the documentation. I have eliminated some latex code that, in my opinion, made the documentation harder to read.

Simon, could you look at my patch? If you feel it is ok, put a positive review.



---

archive/issue_comments_080722.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-26T12:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80722",
    "user": "@simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080723.json:
```json
{
    "body": "Replying to [comment:83 lftabera]:\n> However, I have added a referee patch with some minor changes in the documentation. I have eliminated some latex code that, in my opinion, made the documentation harder to read.\n> \n> Simon, could you look at my patch? If you feel it is ok, put a positive review.\n\nI have read the referee patch, and it seems fine. So, I guess it is a positive review then. Finally!\n\nThank you,\n\nSimon",
    "created_at": "2011-02-26T12:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80723",
    "user": "@simon-king-jena"
}
```

Replying to [comment:83 lftabera]:
> However, I have added a referee patch with some minor changes in the documentation. I have eliminated some latex code that, in my opinion, made the documentation harder to read.
> 
> Simon, could you look at my patch? If you feel it is ok, put a positive review.

I have read the referee patch, and it seems fine. So, I guess it is a positive review then. Finally!

Thank you,

Simon



---

archive/issue_comments_080724.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-02-28T14:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80724",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080725.json:
```json
{
    "body": "This should be rebased to sage-4.6.2.rc1 + #10677 + #2329 (or, you can wait until sage-4.7.alpha1 is released and then rebase to that).",
    "created_at": "2011-02-28T14:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80725",
    "user": "@jdemeyer"
}
```

This should be rebased to sage-4.6.2.rc1 + #10677 + #2329 (or, you can wait until sage-4.7.alpha1 is released and then rebase to that).



---

archive/issue_comments_080726.json:
```json
{
    "body": "Full doctest coverage for sage.categories.functor and sage.categories.pushout. Various coercion bug fixes.",
    "created_at": "2011-03-08T14:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80726",
    "user": "@simon-king-jena"
}
```

Full doctest coverage for sage.categories.functor and sage.categories.pushout. Various coercion bug fixes.



---

archive/issue_comments_080727.json:
```json
{
    "body": "Attachment [8800_functor_pushout_doc_and_fixes.patch](tarball://root/attachments/some-uuid/ticket8800/8800_functor_pushout_doc_and_fixes.patch) by @simon-king-jena created at 2011-03-08 14:20:11\n\nDepends on #10677 #2329\n\nApply 8800_functor_pushout_doc_and_fixes.patch referee.patch",
    "created_at": "2011-03-08T14:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80727",
    "user": "@simon-king-jena"
}
```

Attachment [8800_functor_pushout_doc_and_fixes.patch](tarball://root/attachments/some-uuid/ticket8800/8800_functor_pushout_doc_and_fixes.patch) by @simon-king-jena created at 2011-03-08 14:20:11

Depends on #10677 #2329

Apply 8800_functor_pushout_doc_and_fixes.patch referee.patch



---

archive/issue_comments_080728.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-08T14:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80728",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080729.json:
```json
{
    "body": "I was rebasing the main patch, so that it applies cleanly on top of sage-4.6.2 plus #10677 plus #2329. I change it into \"needs review\", since I am now running doctests.\n\nI hope I am entitled to revert to the old positive review, provided that the long tests pass.",
    "created_at": "2011-03-08T14:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80729",
    "user": "@simon-king-jena"
}
```

I was rebasing the main patch, so that it applies cleanly on top of sage-4.6.2 plus #10677 plus #2329. I change it into "needs review", since I am now running doctests.

I hope I am entitled to revert to the old positive review, provided that the long tests pass.



---

archive/issue_comments_080730.json:
```json
{
    "body": "I have absolutely no idea what the patchbot is complaining about! Its shortlog states\n\n```\n2011-03-08 06:20:58 -0800\nNone\n2011-03-08 06:21:05 -0800\n7 seconds\n```\n\nwhich means???\n\nAnyway. All long tests both in `sage/` and in `doc/` pass. So, if nobody objects, I return to the old positive review.",
    "created_at": "2011-03-08T15:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80730",
    "user": "@simon-king-jena"
}
```

I have absolutely no idea what the patchbot is complaining about! Its shortlog states

```
2011-03-08 06:20:58 -0800
None
2011-03-08 06:21:05 -0800
7 seconds
```

which means???

Anyway. All long tests both in `sage/` and in `doc/` pass. So, if nobody objects, I return to the old positive review.



---

archive/issue_comments_080731.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-08T15:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80731",
    "user": "@simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-08T21:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8800#issuecomment-80732",
    "user": "@jdemeyer"
}
```

Resolution: fixed
