# Issue 4951: expose Singular's numerical solver

Issue created by migration from https://trac.sagemath.org/ticket/4951

Original creator: malb

Original creation time: 2009-01-07 16:00:58

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

