# Issue 8197: Documenting check=True/False parameters

archive/issues_008197.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nMany functions have a check=True (or check=False) parameter where the caller can avoid come costly checking of the input if they know exactly what they are doing.  That is a Good Thing, but unfortunately it is not always documented well.\n\nFor example,\n\n```\nage: P2 = ProjectiveSpace(GF(2),2)\nsage: P = P2.point((0,0,1))\nsage: Q = P2.point([0,0,1])\nsage: P\n(0 : 0 : 1)\nsage: Q\n(0 : 0 : 1)\nsage: P==Q\nTrue\nsage: P._coords\n[0, 0, 1]\nsage: Q._coords\n[0, 0, 1]\n```\n\n\nNow the same but with \"check=False\":\n\n\n```\nsage: P = P2.point((0,0,1),check=False)\nsage: Q = P2.point([0,0,1],check=False)\nsage: P\n(0 : 0 : 1)\nsage: Q\n(0 : 0 : 1)\nsage: P==Q\nFalse\nsage: P._coords\n(0, 0, 1)\nsage: Q._coords\n[0, 0, 1]\n```\n\nThe point is that on creation of the point, valid tuple input is\nconverted to a list, unless check=False in which case tuples are left as tuples.  This can result in wrong results.\n\nIn this example, the point-creation function should document the check= parameter by stating that the coordinates should be given as a list, not a tuple, with entries in the right parent, of the roght length, and (for curves or other schemes where there are polynomial equations to be satisfied) satisfying the defining equations.\n\nThere are surely many places in the source code where these remarks apply, but I have tagged this ticket \"algebraic geometry\" since that's where I ran into it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8197\n\n",
    "created_at": "2010-02-05T20:20:21Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Documenting check=True/False parameters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8197",
    "user": "cremona"
}
```
Assignee: AlexGhitza

Many functions have a check=True (or check=False) parameter where the caller can avoid come costly checking of the input if they know exactly what they are doing.  That is a Good Thing, but unfortunately it is not always documented well.

For example,

```
age: P2 = ProjectiveSpace(GF(2),2)
sage: P = P2.point((0,0,1))
sage: Q = P2.point([0,0,1])
sage: P
(0 : 0 : 1)
sage: Q
(0 : 0 : 1)
sage: P==Q
True
sage: P._coords
[0, 0, 1]
sage: Q._coords
[0, 0, 1]
```


Now the same but with "check=False":


```
sage: P = P2.point((0,0,1),check=False)
sage: Q = P2.point([0,0,1],check=False)
sage: P
(0 : 0 : 1)
sage: Q
(0 : 0 : 1)
sage: P==Q
False
sage: P._coords
(0, 0, 1)
sage: Q._coords
[0, 0, 1]
```

The point is that on creation of the point, valid tuple input is
converted to a list, unless check=False in which case tuples are left as tuples.  This can result in wrong results.

In this example, the point-creation function should document the check= parameter by stating that the coordinates should be given as a list, not a tuple, with entries in the right parent, of the roght length, and (for curves or other schemes where there are polynomial equations to be satisfied) satisfying the defining equations.

There are surely many places in the source code where these remarks apply, but I have tagged this ticket "algebraic geometry" since that's where I ran into it.

Issue created by migration from https://trac.sagemath.org/ticket/8197





---

archive/issue_comments_072291.json:
```json
{
    "body": "In fact, naively, I would have expected that if\n`F(arg)`\nreturns successfully then\n`F(arg, check=False)`\nwill as well. To me this looks like `check=False` does more than turn off checks on whether input is valid -- it changes what valid input is!",
    "created_at": "2010-02-05T21:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8197#issuecomment-72291",
    "user": "nbruin"
}
```

In fact, naively, I would have expected that if
`F(arg)`
returns successfully then
`F(arg, check=False)`
will as well. To me this looks like `check=False` does more than turn off checks on whether input is valid -- it changes what valid input is!



---

archive/issue_comments_072292.json:
```json
{
    "body": "Replying to [ticket:8197 cremona]:\n\n> The point is that on creation of the point, valid tuple input is converted to a list, unless check=False in which case tuples are left as tuples.\n\nJohn, it's not quite accurate what you say:\n\n\n```\nsage: P2 = ProjectiveSpace(GF(2),2)\nsage: type(P2.point([0,0,1])._coords)\n<class 'sage.structure.sequence.Sequence'>\nsage: type(P2.point([0,0,1], check=False)._coords)\n<type 'list'>\n```\n\neven though\n\n\n```\nsage: P2.point([0,0,1], check=False) == P2.point([0,0,1])\nTrue\n```\n\nThe relevant code is for the class  `SchemeMorphism_projective_coordinates_field` in  `schemes/generic/morphism.py :`\u00a0with `check=False,` absolutely nothing is  done except for setting the attribute `_coords`.  Thus\n\n\n```\nsage: P = P2.point(\"Anything\", check=False)\nsage: P._coords\n'Anything'\nsage: P\n('A' : 'n' : 'y' : 't' : 'h' : 'i' : 'n' : 'g')\n```\n\nSo, strictly speaking, the coordinates have to be given as a `Sequence` of the right length.\n\nI think you're right that the key thing is documentation.  In each case there's a design balance to be drawn (when `check=False`) between on the one hand checking nothing at all and on the other making some basic conversions, while not doing time-consuming things such as, for example, verifying that an input satisfies a polynomial.  How this balance is drawn will vary, but the INPUT block ought make it clear how the requirements depend on the value of `check`.\n\nThe relevant part of the documentation for `SchemeMorphism_projective_coordinates_field` says\n\n\n```\n\u00a0\u00a0\u00a0 \u00a0- \u00a0``v`` - a list or tuple of coordinates in K\n```\n\nThe code shows that this is actually too restrictive when `check` is True, and it is inaccurate when\u00a0check\u00a0is False.",
    "created_at": "2010-02-06T10:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8197#issuecomment-72292",
    "user": "fwclarke"
}
```

Replying to [ticket:8197 cremona]:

> The point is that on creation of the point, valid tuple input is converted to a list, unless check=False in which case tuples are left as tuples.

John, it's not quite accurate what you say:


```
sage: P2 = ProjectiveSpace(GF(2),2)
sage: type(P2.point([0,0,1])._coords)
<class 'sage.structure.sequence.Sequence'>
sage: type(P2.point([0,0,1], check=False)._coords)
<type 'list'>
```

even though


```
sage: P2.point([0,0,1], check=False) == P2.point([0,0,1])
True
```

The relevant code is for the class  `SchemeMorphism_projective_coordinates_field` in  `schemes/generic/morphism.py :` with `check=False,` absolutely nothing is  done except for setting the attribute `_coords`.  Thus


```
sage: P = P2.point("Anything", check=False)
sage: P._coords
'Anything'
sage: P
('A' : 'n' : 'y' : 't' : 'h' : 'i' : 'n' : 'g')
```

So, strictly speaking, the coordinates have to be given as a `Sequence` of the right length.

I think you're right that the key thing is documentation.  In each case there's a design balance to be drawn (when `check=False`) between on the one hand checking nothing at all and on the other making some basic conversions, while not doing time-consuming things such as, for example, verifying that an input satisfies a polynomial.  How this balance is drawn will vary, but the INPUT block ought make it clear how the requirements depend on the value of `check`.

The relevant part of the documentation for `SchemeMorphism_projective_coordinates_field` says


```
     -  ``v`` - a list or tuple of coordinates in K
```

The code shows that this is actually too restrictive when `check` is True, and it is inaccurate when check is False.



---

archive/issue_comments_072293.json:
```json
{
    "body": "You are quite right -- the code run when check=True converts the input into a sequence.\n\nThis does not effect this ticket;  but it means that the patch I put up at #8193 needs adjusting slightly.  (There, I construct a whole lot of points on a curve knowing that they coordinates I pass to the point constructor satisfy the equations, and wanted to save time by not asking for the equations to be checked.  But I now see that setting check=False has so many other negative side-effects that I think I'll put back check=True.  The main point of the patch at that ticket is far more significant than this tiny saving anyway!)",
    "created_at": "2010-02-06T11:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8197#issuecomment-72293",
    "user": "cremona"
}
```

You are quite right -- the code run when check=True converts the input into a sequence.

This does not effect this ticket;  but it means that the patch I put up at #8193 needs adjusting slightly.  (There, I construct a whole lot of points on a curve knowing that they coordinates I pass to the point constructor satisfy the equations, and wanted to save time by not asking for the equations to be checked.  But I now see that setting check=False has so many other negative side-effects that I think I'll put back check=True.  The main point of the patch at that ticket is far more significant than this tiny saving anyway!)
