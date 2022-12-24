# Issue 4061: coercion from torsion subgroup of elliptic curve to elliptic curve is broken

archive/issues_004061.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nThe traceback at the bottom shouldn't happen, IMHO.\n\n\n```\nsage: E = EllipticCurve([0,1,0,72,-368]); E\nElliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field\nsage: T = E.torsion_subgroup(); T\nTorsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 associated to the Elliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field\nsage: [n*T.0 for n in range(6)]\n[(0 : 1 : 0), (36 : 224 : 1), (8 : 28 : 1), (4 : 0 : 1), (8 : -28 : 1), (36 : -224 : 1)]\nsage: [E(z) for z in T]\nTraceback (most recent call last):\n...\nTypeError: v (=(1,)) must have 3 components\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4061\n\n",
    "created_at": "2008-09-04T14:03:52Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "coercion from torsion subgroup of elliptic curve to elliptic curve is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4061",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @JohnCremona

The traceback at the bottom shouldn't happen, IMHO.


```
sage: E = EllipticCurve([0,1,0,72,-368]); E
Elliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field
sage: T = E.torsion_subgroup(); T
Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 associated to the Elliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field
sage: [n*T.0 for n in range(6)]
[(0 : 1 : 0), (36 : 224 : 1), (8 : 28 : 1), (4 : 0 : 1), (8 : -28 : 1), (36 : -224 : 1)]
sage: [E(z) for z in T]
Traceback (most recent call last):
...
TypeError: v (=(1,)) must have 3 components
```


Issue created by migration from https://trac.sagemath.org/ticket/4061





---

archive/issue_comments_029290.json:
```json
{
    "body": "This is still a problem in Sage 3.2.1.alpha2:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: E = EllipticCurve([0,1,0,72,-368]); E\nElliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field\nsage: T = E.torsion_subgroup(); T\nTorsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 associated to the Elliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field\nsage: [n*T.0 for n in range(6)]\n| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\n[(0 : 1 : 0),\n (36 : 224 : 1),\n (8 : 28 : 1),\n (4 : 0 : 1),\n (8 : -28 : 1),\n (36 : -224 : 1)]\nsage: [E(z) for z in T]\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.pyc in __call__(self, *args, **kwds)\n    505                ell_point.EllipticCurvePoint)):\n    506             args = tuple(args[0])\n--> 507         return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)\n    508     \n    509     def is_x_coord(self, x):\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in __call__(self, *args)\n    180                 else:\n    181                     return self.point(S)\n--> 182         return self.point(args)\n    183 \n    184     def point_homset(self, S = None):\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in point(self, v, check)\n    213 \n    214     def point(self, v, check=True):\n--> 215         return self._point_class(self, v, check=check)\n    216     \n    217     def _point_class(self):\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.pyc in __init__(self, curve, v, check)\n    190                       \"Argument v (= %s) must be a scheme point, list, or tuple.\"%str(v)\n    191             if len(v) != d and len(v) != d-1:\n--> 192                 raise TypeError, \"v (=%s) must have %s components\"%(v, d)\n    193             v = Sequence(v, point_homset.value_ring())\n    194             if len(v) == d-1:     # very common special case\n\nTypeError: v (=(1,)) must have 3 components\n```\n\n\nI am adding John to the CC field - maybe he has some insight here.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T09:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29290",
    "user": "mabshoff"
}
```

This is still a problem in Sage 3.2.1.alpha2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E = EllipticCurve([0,1,0,72,-368]); E
Elliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field
sage: T = E.torsion_subgroup(); T
Torsion Subgroup isomorphic to Multiplicative Abelian Group isomorphic to C6 associated to the Elliptic Curve defined by y^2  = x^3 + x^2 + 72*x - 368 over Rational Field
sage: [n*T.0 for n in range(6)]
| Sage Version 3.2.1.alpha2, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
[(0 : 1 : 0),
 (36 : 224 : 1),
 (8 : 28 : 1),
 (4 : 0 : 1),
 (8 : -28 : 1),
 (36 : -224 : 1)]
sage: [E(z) for z in T]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.pyc in __call__(self, *args, **kwds)
    505                ell_point.EllipticCurvePoint)):
    506             args = tuple(args[0])
--> 507         return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)
    508     
    509     def is_x_coord(self, x):

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in __call__(self, *args)
    180                 else:
    181                     return self.point(S)
--> 182         return self.point(args)
    183 
    184     def point_homset(self, S = None):

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in point(self, v, check)
    213 
    214     def point(self, v, check=True):
--> 215         return self._point_class(self, v, check=check)
    216     
    217     def _point_class(self):

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.pyc in __init__(self, curve, v, check)
    190                       "Argument v (= %s) must be a scheme point, list, or tuple."%str(v)
    191             if len(v) != d and len(v) != d-1:
--> 192                 raise TypeError, "v (=%s) must have %s components"%(v, d)
    193             v = Sequence(v, point_homset.value_ring())
    194             if len(v) == d-1:     # very common special case

TypeError: v (=(1,)) must have 3 components
```


I am adding John to the CC field - maybe he has some insight here.

Cheers,

Michael



---

archive/issue_comments_029291.json:
```json
{
    "body": "I had not noticed this on trac, or I had forgotten.\n\nThe class EllipticCurveTorsionSubgroup is derived form an abstract abelian group class, but does store the associated curve and the generators as points on the curve.  That is why T.0 is an actual point.  But E(z) does not work because the call() method for elliptic curves does not have implemented a case where the argument is tested (or rather, its parent) to be an element of type EllipticCurveTorsionSubgroup.  That would not be hard to do.  I would recommend this:  \n\n1. Implement a method for the EllipticCurveTorsionSubgroup class which converts an element of the abstract group to an actual point.  For example, this code does that for all elements of the abstract group:\n\n```\n[sum([zi*Ti for zi,Ti in zip(P.list(),T.gens())]) for P in T]\n[(0 : 1 : 0),\n (36 : 224 : 1),\n (8 : 28 : 1),\n (4 : 0 : 1),\n (8 : -28 : 1),\n (36 : -224 : 1)]\n```\n\nThis also works ok when there are 2 generators, but  not quite when there are none (for the trivial group!)  -- I just tried that and it gives an empty list, strange.\n\n2. Add a section in the function `__call__()` in ell_generic.py to catch the case where the argument's parent is an element of the torsion subgroup class like this:\n\n```\nsage: isinstance(T[3].parent(),sage.schemes.elliptic_curves.ell_torsion.EllipticCurveTorsionSubgroup)\nTrue\n```\n\n\nWe'll want something similar when we have a MordellWeilGroup class to hold the whole abelian group of a curve.\n\nThis should be an easy thing for someone to do!",
    "created_at": "2008-11-28T10:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29291",
    "user": "@JohnCremona"
}
```

I had not noticed this on trac, or I had forgotten.

The class EllipticCurveTorsionSubgroup is derived form an abstract abelian group class, but does store the associated curve and the generators as points on the curve.  That is why T.0 is an actual point.  But E(z) does not work because the call() method for elliptic curves does not have implemented a case where the argument is tested (or rather, its parent) to be an element of type EllipticCurveTorsionSubgroup.  That would not be hard to do.  I would recommend this:  

1. Implement a method for the EllipticCurveTorsionSubgroup class which converts an element of the abstract group to an actual point.  For example, this code does that for all elements of the abstract group:

```
[sum([zi*Ti for zi,Ti in zip(P.list(),T.gens())]) for P in T]
[(0 : 1 : 0),
 (36 : 224 : 1),
 (8 : 28 : 1),
 (4 : 0 : 1),
 (8 : -28 : 1),
 (36 : -224 : 1)]
```

This also works ok when there are 2 generators, but  not quite when there are none (for the trivial group!)  -- I just tried that and it gives an empty list, strange.

2. Add a section in the function `__call__()` in ell_generic.py to catch the case where the argument's parent is an element of the torsion subgroup class like this:

```
sage: isinstance(T[3].parent(),sage.schemes.elliptic_curves.ell_torsion.EllipticCurveTorsionSubgroup)
True
```


We'll want something similar when we have a MordellWeilGroup class to hold the whole abelian group of a curve.

This should be an easy thing for someone to do!



---

archive/issue_comments_029292.json:
```json
{
    "body": "Attachment [trac-4061.patch](tarball://root/attachments/some-uuid/ticket4061/trac-4061.patch) by @JohnCremona created at 2008-11-30 11:56:07",
    "created_at": "2008-11-30T11:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29292",
    "user": "@JohnCremona"
}
```

Attachment [trac-4061.patch](tarball://root/attachments/some-uuid/ticket4061/trac-4061.patch) by @JohnCremona created at 2008-11-30 11:56:07



---

archive/issue_comments_029293.json:
```json
{
    "body": "The patch fixes this, based on 3.2.1.rc0.  All doctests in elliptic_curves pass, and both files touched still have 100% coverage :).\n\nThe behaviour for trivial torsion groups is not ideal, but is due to a bug in the Abelian Group class which causes the list of elements of a trivial abelian group to be empty.  That should be in a separate ticket, but it would of course be best solved by the total rewrite of Abelian Groups which we have all wanted (and some of us have partially implemented) for many months...",
    "created_at": "2008-11-30T12:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29293",
    "user": "@JohnCremona"
}
```

The patch fixes this, based on 3.2.1.rc0.  All doctests in elliptic_curves pass, and both files touched still have 100% coverage :).

The behaviour for trivial torsion groups is not ideal, but is due to a bug in the Abelian Group class which causes the list of elements of a trivial abelian group to be empty.  That should be in a separate ticket, but it would of course be best solved by the total rewrite of Abelian Groups which we have all wanted (and some of us have partially implemented) for many months...



---

archive/issue_comments_029294.json:
```json
{
    "body": "Attachment [trac-4061-2.patch](tarball://root/attachments/some-uuid/ticket4061/trac-4061-2.patch) by @JohnCremona created at 2008-11-30 14:44:08",
    "created_at": "2008-11-30T14:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29294",
    "user": "@JohnCremona"
}
```

Attachment [trac-4061-2.patch](tarball://root/attachments/some-uuid/ticket4061/trac-4061-2.patch) by @JohnCremona created at 2008-11-30 14:44:08



---

archive/issue_comments_029295.json:
```json
{
    "body": "Attachment [trac-4061-3.patch](tarball://root/attachments/some-uuid/ticket4061/trac-4061-3.patch) by @JohnCremona created at 2008-11-30 14:44:48\n\nThe second patch (apply after the first) fixes the behaviour for trivial torsion, by fixing the method list() for abelian groups which are trivial.  The 3rd patch adds a doctest in the Abelian Groups code which I forgot the first time.",
    "created_at": "2008-11-30T14:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29295",
    "user": "@JohnCremona"
}
```

Attachment [trac-4061-3.patch](tarball://root/attachments/some-uuid/ticket4061/trac-4061-3.patch) by @JohnCremona created at 2008-11-30 14:44:48

The second patch (apply after the first) fixes the behaviour for trivial torsion, by fixing the method list() for abelian groups which are trivial.  The 3rd patch adds a doctest in the Abelian Groups code which I forgot the first time.



---

archive/issue_comments_029296.json:
```json
{
    "body": "Looks good. Thanks for fixing this (including that very annoying bug in trivial abelian groups). I still find it annoying that it returns a multiplicative abelian group (rather than an additive one) but as is mentioned, that's a later ticket/project. \n\nThis is a bit odd \n\n\n```\nsage: E = EllipticCurve('11a')\nsage: T = E.torsion_subgroup()\nsage: T.gen(0) in T\nFalse\n```\n\n\nbut I suppose that's how it used to be, not part of this ticket.",
    "created_at": "2008-12-07T03:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29296",
    "user": "@robertwb"
}
```

Looks good. Thanks for fixing this (including that very annoying bug in trivial abelian groups). I still find it annoying that it returns a multiplicative abelian group (rather than an additive one) but as is mentioned, that's a later ticket/project. 

This is a bit odd 


```
sage: E = EllipticCurve('11a')
sage: T = E.torsion_subgroup()
sage: T.gen(0) in T
False
```


but I suppose that's how it used to be, not part of this ticket.



---

archive/issue_comments_029297.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.2.alpha1",
    "created_at": "2008-12-07T09:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29297",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.2.2.alpha1



---

archive/issue_comments_029298.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T09:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4061#issuecomment-29298",
    "user": "mabshoff"
}
```

Resolution: fixed
