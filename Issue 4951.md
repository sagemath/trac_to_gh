# Issue 4951: expose Singular's numerical solver

archive/issues_004951.json:
```json
{
    "body": "Assignee: jkantor\n\nThis should be more Sage-ish:\n\n\n```\nsage: P.<x,y,z> = PolynomialRing(QQ)\nsage: sage.rings.ideal.Katsura(P).dimension()\n0\nsage: I = sage.rings.ideal.Katsura(P)\nsage: singular.lib(\"solve\")\nsage: singular.solve(I)\n\n//   characteristic : 0 (complex:8 digits, additional 8 digits)\n//   1 parameter    : i\n//   minpoly        : (i^2+1)\n//   number of vars : 3\n//        block   1 : ordering lp\n//                  : names    x y z\n//        block   2 : ordering C\nsage: singular.set_ring(_)\n\nsage: singular(\"SOL\")\n[1]:\n   [1]:\n      0.63060194\n   [2]:\n      0.31530097\n   [3]:\n      -0.13060194\n[2]:\n   [1]:\n      1\n   [2]:\n      0\n   [3]:\n      0\n[3]:\n   [1]:\n      0.22654092\n   [2]:\n      0.11327046\n   [3]:\n      0.27345908\n[4]:\n   [1]:\n      0.33333333\n   [2]:\n      0\n   [3]:\n      0.33333333\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4951\n\n",
    "created_at": "2009-01-07T16:00:58Z",
    "labels": [
        "numerical",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "expose Singular's numerical solver",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4951",
    "user": "@malb"
}
```
Assignee: jkantor

This should be more Sage-ish:


```
sage: P.<x,y,z> = PolynomialRing(QQ)
sage: sage.rings.ideal.Katsura(P).dimension()
0
sage: I = sage.rings.ideal.Katsura(P)
sage: singular.lib("solve")
sage: singular.solve(I)

//   characteristic : 0 (complex:8 digits, additional 8 digits)
//   1 parameter    : i
//   minpoly        : (i^2+1)
//   number of vars : 3
//        block   1 : ordering lp
//                  : names    x y z
//        block   2 : ordering C
sage: singular.set_ring(_)

sage: singular("SOL")
[1]:
   [1]:
      0.63060194
   [2]:
      0.31530097
   [3]:
      -0.13060194
[2]:
   [1]:
      1
   [2]:
      0
   [3]:
      0
[3]:
   [1]:
      0.22654092
   [2]:
      0.11327046
   [3]:
      0.27345908
[4]:
   [1]:
      0.33333333
   [2]:
      0
   [3]:
      0.33333333
```


Issue created by migration from https://trac.sagemath.org/ticket/4951


