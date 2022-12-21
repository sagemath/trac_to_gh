# Issue 7620: Inconsistent ordering when composing functors

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-12-08 13:02:23

Assignee: nthiery

Keywords: Functor composition order

Apparently the composition of construction functors is inconsistent.

*__Examples__*


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


*__Conventions__*

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

*__About expand()__*


```
class CompositConstructionFunctor(ConstructionFunctor):
    def expand(self):
        return self.all
```

Since the convention `F1*F2(X)=F1(F2(X))` is used, this method should return `list(reversed(self.all))`.

*__Wrong multiplication order__*


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


That means `self` is applied _before_ `other`!

*__Suggested fix__*

1. I suggest that `CompositConstructionFunctor.expand()` returns `list(reversed(self.all))`. Then, we would have `prod(F.expand())==F`. 

2. Change the order of `self` and `other` in the multiplication method of `CompositFunctor`



---

Comment by SimonKing created at 2009-12-08 13:12:14

Changing status from new to needs_review.


---

Comment by SimonKing created at 2009-12-08 13:12:14

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

Attachment

Fixing bugs in the composition order of CompositConstructionFunctor, and adding some doc


---

Comment by mhansen created at 2009-12-27 15:54:08

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:46:42

Resolution: fixed
