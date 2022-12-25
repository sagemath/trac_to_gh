# Issue 7620: Inconsistent ordering when composing functors

archive/issues_007620.json:
```json
{
    "body": "Assignee: @nthiery\n\nKeywords: Functor composition order\n\nApparently the composition of construction functors is inconsistent.\n\n**__Examples__**\n\n\n```\nsage: from sage.categories.pushout import construction_tower\nsage: P = QQ['x','y']\nsage: construction_tower(P)\n[(None, Multivariate Polynomial Ring in x, y over Rational Field),\n (MPoly[x,y], Rational Field),\n (FractionField, Integer Ring)]\n```\n\n\nLet us see what the product of the two functors above does:\n\n```\nsage: F = prod([X[0] for X in construction_tower(P) if X[0] is not None])\nsage: F\nMPoly[x,y](FractionField(...))\n```\n\n\nOK, that's reasonable, we have `F1*F2(X) = F1(F2(X))`.\n\nBut in a slightly more complicated example, the product gets messed up:\n\n\n```\nsage: P = QQ['x'].fraction_field()['y']\nsage: construction_tower(P)\n[(None,\n  Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field),\n (Poly[y],\n  Fraction Field of Univariate Polynomial Ring in x over Rational Field),\n (FractionField, Univariate Polynomial Ring in x over Rational Field),\n (Poly[x], Rational Field),\n (FractionField, Integer Ring)]\n```\n\n\nNow we do the same product as above:\n\n```\nsage: F = prod([X[0] for X in construction_tower(P) if X[0] is not None])\nsage: F\nFractionField(Poly[x](Poly[y](FractionField(...))))\n```\n\n\nSo, apparently the order is perturbed.\n\nRelated with it, it seems counter-intuitive that the product over the expansion of a functor does not return the functor:\n\n\n```\nsage: F\nFractionField(Poly[x](Poly[y](FractionField(...))))\nsage: prod(F.expand())\nFractionField(Poly[x](FractionField(Poly[y](...))))\n```\n\n\n**__Conventions__**\n\nPossible conventions on the order of composition are: `F1*F2(X)=F1(F2(X))` and `F1*F2(X)=F2(F1(X))`\n\nMy personal preference is `F1*F2(X)=F1(F2(X))`, and it happens to be used in the generic multiplication method of ConstructionFunctor:\n\n\n```\nclass ConstructionFunctor(Functor):\n    def __mul__(self, other):\n        if not isinstance(self, ConstructionFunctor) and not isinstance(other, ConstructionFunctor):\n            raise CoercionException, \"Non-constructive product\"\n        return CompositConstructionFunctor(other, self)\n```\n\n\nSo, I think the convention `F1*F2(X)=F1(F2(X))` should be (or is already) the official Sage convention.\n\n**__About expand()__**\n\n\n```\nclass CompositConstructionFunctor(ConstructionFunctor):\n    def expand(self):\n        return self.all\n```\n\nSince the convention `F1*F2(X)=F1(F2(X))` is used, this method should return `list(reversed(self.all))`.\n\n**__Wrong multiplication order__**\n\n\n```\nclass CompositConstructionFunctor(ConstructionFunctor):\n    def __init__(self, *args):\n        self.all = []\n        for c in args:\n            if isinstance(c, list):\n                self.all += c\n            elif isinstance(c, CompositConstructionFunctor):\n                self.all += c.all\n            else:\n                self.all.append(c)\n        Functor.__init__(self, self.all[0].domain(), self.all[-1].codomain())\n    def __mul__(self, other):\n        if isinstance(self, CompositConstructionFunctor):\n            all = self.all + [other]\n        else:\n            all = [self] + other.all\n        return CompositConstructionFunctor(*all)\n```\n\n\nThat means `self` is applied *before* `other`!\n\n**__Suggested fix__**\n\n1. I suggest that `CompositConstructionFunctor.expand()` returns `list(reversed(self.all))`. Then, we would have `prod(F.expand())==F`. \n\n2. Change the order of `self` and `other` in the multiplication method of `CompositFunctor`\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7620\n\n",
    "created_at": "2009-12-08T13:02:23Z",
    "labels": [
        "component: categories",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Inconsistent ordering when composing functors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7620",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @nthiery

Keywords: Functor composition order

Apparently the composition of construction functors is inconsistent.

**__Examples__**


```
sage: from sage.categories.pushout import construction_tower
sage: P = QQ['x','y']
sage: construction_tower(P)
[(None, Multivariate Polynomial Ring in x, y over Rational Field),
 (MPoly[x,y], Rational Field),
 (FractionField, Integer Ring)]
```


Let us see what the product of the two functors above does:

```
sage: F = prod([X[0] for X in construction_tower(P) if X[0] is not None])
sage: F
MPoly[x,y](FractionField(...))
```


OK, that's reasonable, we have `F1*F2(X) = F1(F2(X))`.

But in a slightly more complicated example, the product gets messed up:


```
sage: P = QQ['x'].fraction_field()['y']
sage: construction_tower(P)
[(None,
  Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field),
 (Poly[y],
  Fraction Field of Univariate Polynomial Ring in x over Rational Field),
 (FractionField, Univariate Polynomial Ring in x over Rational Field),
 (Poly[x], Rational Field),
 (FractionField, Integer Ring)]
```


Now we do the same product as above:

```
sage: F = prod([X[0] for X in construction_tower(P) if X[0] is not None])
sage: F
FractionField(Poly[x](Poly[y](FractionField(...))))
```


So, apparently the order is perturbed.

Related with it, it seems counter-intuitive that the product over the expansion of a functor does not return the functor:


```
sage: F
FractionField(Poly[x](Poly[y](FractionField(...))))
sage: prod(F.expand())
FractionField(Poly[x](FractionField(Poly[y](...))))
```


**__Conventions__**

Possible conventions on the order of composition are: `F1*F2(X)=F1(F2(X))` and `F1*F2(X)=F2(F1(X))`

My personal preference is `F1*F2(X)=F1(F2(X))`, and it happens to be used in the generic multiplication method of ConstructionFunctor:


```
class ConstructionFunctor(Functor):
    def __mul__(self, other):
        if not isinstance(self, ConstructionFunctor) and not isinstance(other, ConstructionFunctor):
            raise CoercionException, "Non-constructive product"
        return CompositConstructionFunctor(other, self)
```


So, I think the convention `F1*F2(X)=F1(F2(X))` should be (or is already) the official Sage convention.

**__About expand()__**


```
class CompositConstructionFunctor(ConstructionFunctor):
    def expand(self):
        return self.all
```

Since the convention `F1*F2(X)=F1(F2(X))` is used, this method should return `list(reversed(self.all))`.

**__Wrong multiplication order__**


```
class CompositConstructionFunctor(ConstructionFunctor):
    def __init__(self, *args):
        self.all = []
        for c in args:
            if isinstance(c, list):
                self.all += c
            elif isinstance(c, CompositConstructionFunctor):
                self.all += c.all
            else:
                self.all.append(c)
        Functor.__init__(self, self.all[0].domain(), self.all[-1].codomain())
    def __mul__(self, other):
        if isinstance(self, CompositConstructionFunctor):
            all = self.all + [other]
        else:
            all = [self] + other.all
        return CompositConstructionFunctor(*all)
```


That means `self` is applied *before* `other`!

**__Suggested fix__**

1. I suggest that `CompositConstructionFunctor.expand()` returns `list(reversed(self.all))`. Then, we would have `prod(F.expand())==F`. 

2. Change the order of `self` and `other` in the multiplication method of `CompositFunctor`


Issue created by migration from https://trac.sagemath.org/ticket/7620





---

archive/issue_comments_065004.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-08T13:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7620#issuecomment-65004",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065005.json:
```json
{
    "body": "With the patch, that should apply to sage-4.3.alpha1, one has\n\n\n```\nsage: from sage.categories.pushout import CompositConstructionFunctor\nsage: F1 = CompositConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0])\nsage: F2 = CompositConstructionFunctor(QQ.construction()[0],ZZ['y'].construction()[0])\nsage: F1*F2\nPoly[x](FractionField(Poly[y](FractionField(...))))\n```\n\n\nand \n\n\n```\nsage: from sage.categories.pushout import CompositConstructionFunctor\nsage: F = CompositConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0],QQ.construction()[0],ZZ['y'].construction()[0])\nsage: F\nPoly[y](FractionField(Poly[x](FractionField(...))))\nsage: prod(F.expand()) == F\nTrue\n```\n\n\nand I think that is how it should be.",
    "created_at": "2009-12-08T13:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7620#issuecomment-65005",
    "user": "https://github.com/simon-king-jena"
}
```

With the patch, that should apply to sage-4.3.alpha1, one has


```
sage: from sage.categories.pushout import CompositConstructionFunctor
sage: F1 = CompositConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0])
sage: F2 = CompositConstructionFunctor(QQ.construction()[0],ZZ['y'].construction()[0])
sage: F1*F2
Poly[x](FractionField(Poly[y](FractionField(...))))
```


and 


```
sage: from sage.categories.pushout import CompositConstructionFunctor
sage: F = CompositConstructionFunctor(QQ.construction()[0],ZZ['x'].construction()[0],QQ.construction()[0],ZZ['y'].construction()[0])
sage: F
Poly[y](FractionField(Poly[x](FractionField(...))))
sage: prod(F.expand()) == F
True
```


and I think that is how it should be.



---

archive/issue_comments_065006.json:
```json
{
    "body": "Attachment [7620FunctorCompositionOrder.patch](tarball://root/attachments/some-uuid/ticket7620/7620FunctorCompositionOrder.patch) by @simon-king-jena created at 2009-12-08 13:13:03\n\nFixing bugs in the composition order of CompositConstructionFunctor, and adding some doc",
    "created_at": "2009-12-08T13:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7620#issuecomment-65006",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [7620FunctorCompositionOrder.patch](tarball://root/attachments/some-uuid/ticket7620/7620FunctorCompositionOrder.patch) by @simon-king-jena created at 2009-12-08 13:13:03

Fixing bugs in the composition order of CompositConstructionFunctor, and adding some doc



---

archive/issue_comments_065007.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-27T15:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7620#issuecomment-65007",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065008.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7620#issuecomment-65008",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007845.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-03T21:46:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7620",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7620#event-7845"
}
```
