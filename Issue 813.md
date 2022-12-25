# Issue 813: forced coercion vs. automatic coercion

archive/issues_000813.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis should give similar results, but it is inconsistent:\n\n```\nP1.<x>=QQ[]\nL=P1.fraction_field()\nx=L(x)\nP2.<y>=P1[]\n\nf=x+y\n\nP3.<x,y>=QQ[]\n\nP3(f)\n\n0*P3.0+f\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/813\n\n",
    "created_at": "2007-10-03T18:52:27Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "forced coercion vs. automatic coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/813",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

This should give similar results, but it is inconsistent:

```
P1.<x>=QQ[]
L=P1.fraction_field()
x=L(x)
P2.<y>=P1[]

f=x+y

P3.<x,y>=QQ[]

P3(f)

0*P3.0+f
```

Issue created by migration from https://trac.sagemath.org/ticket/813





---

archive/issue_comments_005013.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-10-03T20:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5013",
    "user": "https://github.com/nbruin"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_005014.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2007-10-03T20:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5014",
    "user": "https://github.com/nbruin"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_events_002284.json:
```json
{
    "actor": "https://github.com/nbruin",
    "created_at": "2007-10-03T20:58:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/813#event-2284"
}
```



---

archive/issue_events_002285.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T18:10:29Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/813#event-2285"
}
```



---

archive/issue_events_002286.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T18:10:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/813#event-2286"
}
```



---

archive/issue_comments_005015.json:
```json
{
    "body": "I will work on this once Robert has added rdef'd functions to Sage (that way I don't have to redo the changes once this occurs)",
    "created_at": "2007-10-13T00:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5015",
    "user": "https://github.com/roed314"
}
```

I will work on this once Robert has added rdef'd functions to Sage (that way I don't have to redo the changes once this occurs)



---

archive/issue_events_002287.json:
```json
{
    "actor": "https://github.com/roed314",
    "created_at": "2007-10-13T00:42:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/813#event-2287"
}
```



---

archive/issue_events_002288.json:
```json
{
    "actor": "https://github.com/roed314",
    "created_at": "2007-10-13T00:42:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/813#event-2288"
}
```



---

archive/issue_comments_005016.json:
```json
{
    "body": "This now gives a TypeError when doing the last arithmetic:\n\n```\nTypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'\n```",
    "created_at": "2008-11-14T09:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5016",
    "user": "https://github.com/mwhansen"
}
```

This now gives a TypeError when doing the last arithmetic:

```
TypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'
```



---

archive/issue_comments_005017.json:
```json
{
    "body": "I accidentally came accross this stone age ticket.\n\nFor the record: Current behaviour as of sage-4.7.rc2 is\n\n```\nsage: P1.<x>=QQ[]\nsage: L=P1.fraction_field()\nsage: x=L(x)\nsage: P2.<y>=P1[]\nsage:\nsage: f=x+y\nsage:\nsage: P3.<x,y>=QQ[]\nsage:\nsage: P3(f)\nx + y\nsage:\nsage: 0*P3.0+f\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/<ipython console> in <module>()\n\n/mnt/local/king/SAGE/sage-4.7.rc2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11959)()\n\n/mnt/local/king/SAGE/sage-4.7.rc2/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7382)()\n\nTypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'\nsage: f.parent()\nUnivariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field\nsage: P3\nMultivariate Polynomial Ring in x, y over Rational Field\n```\n\nThe question thus is: Should there be a coercion from P3 to the parent of f? Then one should implement it. Otherwise, the ticket should be closed as invalid.\n\nLet fP be the parent of f, hence, the polynomial ring in y over the fraction field of the polynomial ring in x over the rationals.\n\nThere *is* a coercion to fP from the polyomial ring in y over the polynomial ring in x over the rationals:\n\n```\nsage: from sage.structure.element import get_coercion_model\nsage: cm = get_coercion_model()\nsage: fP = f.parent()\nsage: cm.explain(fP, QQ[x][y])\nCoercion on right operand via\n    Conversion map:\n      From: Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field\n      To:   Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field\nArithmetic performed after coercions.\nResult lives in Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field\nUnivariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field\n```\n\nHowever, there is no such coercion from the bivariate polynomial ring in x and y over the rationals:\n\n```\nsage: cm.explain(fP, QQ[x,y])\nWill try _r_action and _l_action\nUnknown result parent.\n```\n\nI think there should be such coercion! What do you think? I guess I'll also ask sage-devel.",
    "created_at": "2011-07-31T14:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5017",
    "user": "https://github.com/simon-king-jena"
}
```

I accidentally came accross this stone age ticket.

For the record: Current behaviour as of sage-4.7.rc2 is

```
sage: P1.<x>=QQ[]
sage: L=P1.fraction_field()
sage: x=L(x)
sage: P2.<y>=P1[]
sage:
sage: f=x+y
sage:
sage: P3.<x,y>=QQ[]
sage:
sage: P3(f)
x + y
sage:
sage: 0*P3.0+f
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.rc2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11959)()

/mnt/local/king/SAGE/sage-4.7.rc2/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7382)()

TypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'
sage: f.parent()
Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: P3
Multivariate Polynomial Ring in x, y over Rational Field
```

The question thus is: Should there be a coercion from P3 to the parent of f? Then one should implement it. Otherwise, the ticket should be closed as invalid.

Let fP be the parent of f, hence, the polynomial ring in y over the fraction field of the polynomial ring in x over the rationals.

There *is* a coercion to fP from the polyomial ring in y over the polynomial ring in x over the rationals:

```
sage: from sage.structure.element import get_coercion_model
sage: cm = get_coercion_model()
sage: fP = f.parent()
sage: cm.explain(fP, QQ[x][y])
Coercion on right operand via
    Conversion map:
      From: Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
      To:   Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
Arithmetic performed after coercions.
Result lives in Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
```

However, there is no such coercion from the bivariate polynomial ring in x and y over the rationals:

```
sage: cm.explain(fP, QQ[x,y])
Will try _r_action and _l_action
Unknown result parent.
```

I think there should be such coercion! What do you think? I guess I'll also ask sage-devel.



---

archive/issue_comments_005018.json:
```json
{
    "body": "For the record: I did post on [sage-algebra](http://groups.google.com/group/sage-algebra/browse_thread/thread/7f884449de17bb31), not sage-devel.\n\nThere, I argued that there should be no coercion/pushout between `QQ[x][y]` and `QQ[y][x]`, even though there is a coercion between `QQ[x,y]` and `QQ[y,x]`. I wonder whether my argument is convincing, though.\n\nHowever, even in that case, I could imagine that with a little more effort one could modify the algorithm behind `sage.categories.pushout.pushout` so that the pushout of `Frac(QQ['x'])['y']` and `QQ['x','y']` is `Frac(QQ['x'])['y']`. Do we want that behaviour of the pushout?",
    "created_at": "2011-07-31T20:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5018",
    "user": "https://github.com/simon-king-jena"
}
```

For the record: I did post on [sage-algebra](http://groups.google.com/group/sage-algebra/browse_thread/thread/7f884449de17bb31), not sage-devel.

There, I argued that there should be no coercion/pushout between `QQ[x][y]` and `QQ[y][x]`, even though there is a coercion between `QQ[x,y]` and `QQ[y,x]`. I wonder whether my argument is convincing, though.

However, even in that case, I could imagine that with a little more effort one could modify the algorithm behind `sage.categories.pushout.pushout` so that the pushout of `Frac(QQ['x'])['y']` and `QQ['x','y']` is `Frac(QQ['x'])['y']`. Do we want that behaviour of the pushout?



---

archive/issue_comments_005019.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2011-08-02T13:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5019",
    "user": "https://github.com/simon-king-jena"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_comments_005020.json:
```json
{
    "body": "Meanwhile I believe that this is *not* invalid. Namely, we have the following:\n\n```\nsage: from sage.categories.pushout import pushout\nsage: pushout(QQ['x','y'],Frac(QQ['x'])['y'])\nUnivariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field\n```\n\nHence, arithmetic between `QQ['x','y']` and `Frac(QQ['x'])['y']` should work! But it doesn't:\n\n```\nsage: QQ['x','y'](1) + Frac(QQ['x'])['y'](1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/Projekte/MeatAxe/meataxe-2.2.4/<ipython console> in <module>()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11997)()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7382)()\n\nTypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'\n```\n\nWhat is the problem? The conversion is fine:\n\n```\nsage: Frac(QQ['x'])['y'](QQ['x','y'](1))\n1\n```\n\nBut in fact there is no coercion into the pushout:\n\n```\nsage: pushout(QQ['x','y'],Frac(QQ['x'])['y']).has_coerce_map_from(QQ['x','y'])\nFalse\n```\n\nThat's a bug, I think.",
    "created_at": "2011-08-02T13:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5020",
    "user": "https://github.com/simon-king-jena"
}
```

Meanwhile I believe that this is *not* invalid. Namely, we have the following:

```
sage: from sage.categories.pushout import pushout
sage: pushout(QQ['x','y'],Frac(QQ['x'])['y'])
Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
```

Hence, arithmetic between `QQ['x','y']` and `Frac(QQ['x'])['y']` should work! But it doesn't:

```
sage: QQ['x','y'](1) + Frac(QQ['x'])['y'](1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/Projekte/MeatAxe/meataxe-2.2.4/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11997)()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7382)()

TypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'
```

What is the problem? The conversion is fine:

```
sage: Frac(QQ['x'])['y'](QQ['x','y'](1))
1
```

But in fact there is no coercion into the pushout:

```
sage: pushout(QQ['x','y'],Frac(QQ['x'])['y']).has_coerce_map_from(QQ['x','y'])
False
```

That's a bug, I think.



---

archive/issue_comments_005021.json:
```json
{
    "body": "PS: In addition, since there is a coercion from `QQ['y','x']` to `QQ['x','y']`, it is conceivable that the pushout of `QQ['y','x']` with `Frac(QQ['x'])['y']` should be `Frac(QQ['x'])['y']` as well. But it isn't:\n\n```\nsage: pushout(QQ['y','x'],Frac(QQ['x'])['y'])\n---------------------------------------------------------------------------\nCoercionException                         Traceback (most recent call last)\n\n/home/king/Projekte/MeatAxe/meataxe-2.2.4/<ipython console> in <module>()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)\n   3072                     if Rc[-1] in Sc:\n   3073                         if Sc[-1] in Rc:\n-> 3074                             raise CoercionException, (\"Ambiguous Base Extension\", R, S)\n   3075                         else:\n   3076                             all = Sc.pop() * all\n\nCoercionException: ('Ambiguous Base Extension', Multivariate Polynomial Ring in y, x over Rational Field, Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field)\n```",
    "created_at": "2011-08-02T13:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5021",
    "user": "https://github.com/simon-king-jena"
}
```

PS: In addition, since there is a coercion from `QQ['y','x']` to `QQ['x','y']`, it is conceivable that the pushout of `QQ['y','x']` with `Frac(QQ['x'])['y']` should be `Frac(QQ['x'])['y']` as well. But it isn't:

```
sage: pushout(QQ['y','x'],Frac(QQ['x'])['y'])
---------------------------------------------------------------------------
CoercionException                         Traceback (most recent call last)

/home/king/Projekte/MeatAxe/meataxe-2.2.4/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)
   3072                     if Rc[-1] in Sc:
   3073                         if Sc[-1] in Rc:
-> 3074                             raise CoercionException, ("Ambiguous Base Extension", R, S)
   3075                         else:
   3076                             all = Sc.pop() * all

CoercionException: ('Ambiguous Base Extension', Multivariate Polynomial Ring in y, x over Rational Field, Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field)
```



---

archive/issue_comments_005022.json:
```json
{
    "body": "Here is my plan for implementing a coercion of `P = QQ['x','y']` into `Q = Frac(QQ['x'])['y']`.\n\nSince conversion of P into Q works, we only need to make `Q._coerce_map_from_(P)` return True.\n\nLet p be an element of P. When converting p into Q, the multivariate polynomial p is transformed into a univeriate polynomial via p. This is done using `p._polynomial_(Q)`, which ultimately boils down to `Q(p.polynomial(P('y')))`:\n\n```\nsage: P = QQ['x','y']\nsage: p = P.gen(0)\nsage: Q = Frac(QQ['x'])['y']\nsage: Q(p.polynomial(P('y')))\nx\n```\n\n`p.polynomial(P('y')).parent()` lives in a stacked polynomial ring:\n\n```\nsage: p.polynomial(P('y')).parent()\nUnivariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field\n```\nThat stacked ring coerces into Q:\n\n```\nsage: Q.has_coerce_map_from(p.polynomial(P('y')).parent())\nTrue\n```\n\nConclusion: If we want to test whether a multivariate polynomial ring P coerces into a univariate polynomial ring Q in variable y, then we need to try and transform P into a *univariate* polynomial ring P' in variable y; here, we have `P'=QQ['x']['y']`. There is a coercion from P into Q if and only if there is a coercion from P' into Q.\n\nI already have a patch, but \"surprisingly\" the additional coercion yields some doctest errors in other places.",
    "created_at": "2011-08-02T14:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5022",
    "user": "https://github.com/simon-king-jena"
}
```

Here is my plan for implementing a coercion of `P = QQ['x','y']` into `Q = Frac(QQ['x'])['y']`.

Since conversion of P into Q works, we only need to make `Q._coerce_map_from_(P)` return True.

Let p be an element of P. When converting p into Q, the multivariate polynomial p is transformed into a univeriate polynomial via p. This is done using `p._polynomial_(Q)`, which ultimately boils down to `Q(p.polynomial(P('y')))`:

```
sage: P = QQ['x','y']
sage: p = P.gen(0)
sage: Q = Frac(QQ['x'])['y']
sage: Q(p.polynomial(P('y')))
x
```

`p.polynomial(P('y')).parent()` lives in a stacked polynomial ring:

```
sage: p.polynomial(P('y')).parent()
Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
```
That stacked ring coerces into Q:

```
sage: Q.has_coerce_map_from(p.polynomial(P('y')).parent())
True
```

Conclusion: If we want to test whether a multivariate polynomial ring P coerces into a univariate polynomial ring Q in variable y, then we need to try and transform P into a *univariate* polynomial ring P' in variable y; here, we have `P'=QQ['x']['y']`. There is a coercion from P into Q if and only if there is a coercion from P' into Q.

I already have a patch, but "surprisingly" the additional coercion yields some doctest errors in other places.



---

archive/issue_comments_005023.json:
```json
{
    "body": "The problem with my approach is that it would create a bidirectional coercion, namely a coercion from `QQ['x','y']` to `QQ['x']['y']` in addition to the coercion from `QQ['x']['y']` to `QQ['x','y']` that already exists.\n\nBut I think I have an idea that would solve the problem.\n\nMy original idea was to have a coercion from P to Q if there is a coercion from `P.remove_var(Q.variable_name())` to `Q.base_ring()`. That created the bidirectional coercion.\n\nMy modified idea is to have the coercion from P to Q *only* if `P.remove_var(Q.variable_name())` is different from `Q.base_ring()`, but coerces into it. Hence, a coercion only takes place if the rings become more complicated, thus avoiding circles.\n\nThe tests in sage/rings/polynomial pass. I am now running all doc tests, and then I can hopefully submit my patch...",
    "created_at": "2011-08-02T15:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5023",
    "user": "https://github.com/simon-king-jena"
}
```

The problem with my approach is that it would create a bidirectional coercion, namely a coercion from `QQ['x','y']` to `QQ['x']['y']` in addition to the coercion from `QQ['x']['y']` to `QQ['x','y']` that already exists.

But I think I have an idea that would solve the problem.

My original idea was to have a coercion from P to Q if there is a coercion from `P.remove_var(Q.variable_name())` to `Q.base_ring()`. That created the bidirectional coercion.

My modified idea is to have the coercion from P to Q *only* if `P.remove_var(Q.variable_name())` is different from `Q.base_ring()`, but coerces into it. Hence, a coercion only takes place if the rings become more complicated, thus avoiding circles.

The tests in sage/rings/polynomial pass. I am now running all doc tests, and then I can hopefully submit my patch...



---

archive/issue_comments_005024.json:
```json
{
    "body": "Coercion from multivariate to univariate polynomial rings",
    "created_at": "2011-08-02T17:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5024",
    "user": "https://github.com/simon-king-jena"
}
```

Coercion from multivariate to univariate polynomial rings



---

archive/issue_comments_005025.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-02T17:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5025",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_005026.json:
```json
{
    "body": "Attachment [trac813_univariate_coerce_from_multivariate.patch](tarball://root/attachments/some-uuid/ticket813/trac813_univariate_coerce_from_multivariate.patch) by @simon-king-jena created at 2011-08-02 17:11:41\n\nI think I was able to solve the problem. With my patch applied on top of sage-4.7.1.rc1, all tests seem to pass, and one can do\n\n```\n            sage: P = QQ['x','y']\n            sage: Q = Frac(QQ['x'])['y']\n            sage: Q.has_coerce_map_from(P)\n            True\n            sage: P.0+Q.0\n            y + x\n```\n\nIn order to avoid bidirectional coercions (that would break a lot of tests), I have\n\n```\n            sage: Q = QQ['x']['y']\n            sage: Q.has_coerce_map_from(P)\n            False\n            sage: Q.base_ring() is P.remove_var(Q.variable_name())\n            True\n```\n\nThe rule is: If `Q.base_ring() is P.remove_var(Q.variable_name())` then there can not be a coercion from the multivariate ring P to the univariate ring Q; in fact, there is a coercion in the opposite direction. But otherwise, there is a coercion if `Q.base_ring()` has a coercion from `P.remove_var(Q.variable_name())`.",
    "created_at": "2011-08-02T17:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5026",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac813_univariate_coerce_from_multivariate.patch](tarball://root/attachments/some-uuid/ticket813/trac813_univariate_coerce_from_multivariate.patch) by @simon-king-jena created at 2011-08-02 17:11:41

I think I was able to solve the problem. With my patch applied on top of sage-4.7.1.rc1, all tests seem to pass, and one can do

```
            sage: P = QQ['x','y']
            sage: Q = Frac(QQ['x'])['y']
            sage: Q.has_coerce_map_from(P)
            True
            sage: P.0+Q.0
            y + x
```

In order to avoid bidirectional coercions (that would break a lot of tests), I have

```
            sage: Q = QQ['x']['y']
            sage: Q.has_coerce_map_from(P)
            False
            sage: Q.base_ring() is P.remove_var(Q.variable_name())
            True
```

The rule is: If `Q.base_ring() is P.remove_var(Q.variable_name())` then there can not be a coercion from the multivariate ring P to the univariate ring Q; in fact, there is a coercion in the opposite direction. But otherwise, there is a coercion if `Q.base_ring()` has a coercion from `P.remove_var(Q.variable_name())`.



---

archive/issue_comments_005027.json:
```json
{
    "body": "Any reviewer for a time-honoured ticket?",
    "created_at": "2011-08-30T10:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5027",
    "user": "https://github.com/simon-king-jena"
}
```

Any reviewer for a time-honoured ticket?



---

archive/issue_comments_005028.json:
```json
{
    "body": "Looking at your patch, was `def univariate_ring(self, x):` added by purpose? Apart from that it seems to be a perfectly good solution as long as we can not have cyclic coercions.",
    "created_at": "2011-09-21T10:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5028",
    "user": "https://github.com/saraedum"
}
```

Looking at your patch, was `def univariate_ring(self, x):` added by purpose? Apart from that it seems to be a perfectly good solution as long as we can not have cyclic coercions.



---

archive/issue_comments_005029.json:
```json
{
    "body": "btw., doctests pass when applied to 4.7.2.alpha2.",
    "created_at": "2011-09-21T12:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5029",
    "user": "https://github.com/saraedum"
}
```

btw., doctests pass when applied to 4.7.2.alpha2.



---

archive/issue_comments_005030.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-09-21T12:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5030",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_005031.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-21T13:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5031",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_005032.json:
```json
{
    "body": "Replying to [comment:14 saraedum]:\n> Looking at your patch, was `def univariate_ring(self, x):` added by purpose? \n\n\nGood question. I think it was meant as analogy to the method `univariate_polynomial` of multivariate polynomials. But really, it seems unneeded to have that method. Could probably be dropped, if you prefer (needs to be tested, though).",
    "created_at": "2011-09-21T13:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5032",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:14 saraedum]:
> Looking at your patch, was `def univariate_ring(self, x):` added by purpose? 


Good question. I think it was meant as analogy to the method `univariate_polynomial` of multivariate polynomials. But really, it seems unneeded to have that method. Could probably be dropped, if you prefer (needs to be tested, though).



---

archive/issue_comments_005033.json:
```json
{
    "body": "Ok. In this case it makes sense to have this method. I made some minor changes to the docstrings.\n\nSorry, I created an extra attachment. Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.2.patch.",
    "created_at": "2011-09-21T13:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5033",
    "user": "https://github.com/saraedum"
}
```

Ok. In this case it makes sense to have this method. I made some minor changes to the docstrings.

Sorry, I created an extra attachment. Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.2.patch.



---

archive/issue_comments_005034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-21T13:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5034",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005035.json:
```json
{
    "body": "Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.2.patch.",
    "created_at": "2011-09-21T13:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5035",
    "user": "https://github.com/saraedum"
}
```

Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.2.patch.



---

archive/issue_comments_005036.json:
```json
{
    "body": "Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.patch\n\nSorry, struggling with the patchbot.",
    "created_at": "2011-09-21T13:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5036",
    "user": "https://github.com/saraedum"
}
```

Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.patch

Sorry, struggling with the patchbot.



---

archive/issue_comments_005037.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-09-23T10:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5037",
    "user": "https://github.com/nexttime"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_005038.json:
```json
{
    "body": "Replying to [ticket:813 nbruin]:\n> Apply \n\n\n> \n\n\n>  1. [attachment:trac813_univariate_coerce_from_multivariate.patch] \n\n\n>  2. [attachment:trac_813_review.2.patch] \n\n\n> \n\n\n> to the sage repository.\n\n\n? The attachment comment of the second file says *\"ignore this file\"*, and the \"patch\" is only 17 bytes in total...\n\nSo I guess the description should be updated, to apply the [attachment:trac_813_review.patch \"old\" reviewer patch].",
    "created_at": "2011-09-23T10:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5038",
    "user": "https://github.com/nexttime"
}
```

Replying to [ticket:813 nbruin]:
> Apply 


> 


>  1. [attachment:trac813_univariate_coerce_from_multivariate.patch] 


>  2. [attachment:trac_813_review.2.patch] 


> 


> to the sage repository.


? The attachment comment of the second file says *"ignore this file"*, and the "patch" is only 17 bytes in total...

So I guess the description should be updated, to apply the [attachment:trac_813_review.patch "old" reviewer patch].



---

archive/issue_comments_005039.json:
```json
{
    "body": "sure. sorry, only updated the patchbot instructions but not the ticket description.",
    "created_at": "2011-09-23T10:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5039",
    "user": "https://github.com/saraedum"
}
```

sure. sorry, only updated the patchbot instructions but not the ticket description.



---

archive/issue_comments_005040.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-23T10:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5040",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_005041.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-23T10:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5041",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005042.json:
```json
{
    "body": "Ok, I've deleted the 17 bytes...",
    "created_at": "2011-09-23T11:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5042",
    "user": "https://github.com/nexttime"
}
```

Ok, I've deleted the 17 bytes...



---

archive/issue_events_002289.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-09-27T17:42:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/813#event-2289"
}
```



---

archive/issue_comments_005043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-27T17:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5043",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_comments_005044.json:
```json
{
    "body": "Attachment [trac_813_review.patch](tarball://root/attachments/some-uuid/ticket813/trac_813_review.patch) by @jdemeyer created at 2011-10-04 10:11:48\n\nsmall changes to docstrings",
    "created_at": "2011-10-04T10:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/813#issuecomment-5044",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_813_review.patch](tarball://root/attachments/some-uuid/ticket813/trac_813_review.patch) by @jdemeyer created at 2011-10-04 10:11:48

small changes to docstrings
