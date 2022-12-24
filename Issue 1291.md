# Issue 1291: solving recurrences

archive/issues_001291.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin kevin.stueve @kcrisman @robert-marik @eviatarbach @rwst ktkohl\n\nSage should be able to easily solve at least some recurrences.  Maxima is actually pretty capable here.\n\n```\nsage: maxima.load('solve_rec')\n?\\/Users\\/was\\/s\\/local\\/share\\/maxima\\/5\\.13\\.0\\/share\\/contrib\\/solve_rec\\/solve_rec\\.mac\nsage: print maxima('solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n])')\n                         n          n                       n\n            (sqrt(5) - 1)  %k  (- 1)           (sqrt(5) + 1)  %k\n                             1           n                      2    2\n       a  = ------------------------- - ---- + ------------------ - ----\n        n               n                  n            n              n\n                       2                5 2            2            5 2\n\n```\n\n\n\nSomebody should wrap this:\n\n```\n\nsage: maxima.solve_rec?\nMaxima 5.13.0 http://maxima.sourceforge.net\nUsing Lisp CLISP 2.41 (2006-10-13)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) \n -- Function: solve_rec (<eqn>, <var>, [<init>])\n     Solves for hypergeometrical solutions to linear recurrence <eqn>\n     with polynomials coefficient in variable <var>. Optional arguments\n     <init> are initial conditions.\n\n     `solve_rec' can solve linear recurrences with constant\n     coefficients, finds hypergeometrical solutions to homogeneous\n     linear recurrences with polynomial coefficients, rational\n     solutions to linear recurrences with polynomial coefficients and\n     can solve Ricatti type recurrences.\n\n     Note that the running time of the algorithm used to find\n     hypergeometrical solutions is exponential in the degree of the\n     leading and trailing coefficient.\n\n     To use this function first load the `solve_rec' package with\n     `load(solve_rec);'.\n\n     Example of linear recurrence with constant coefficients:\n\n          (%i2) solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n]);\n                                  n          n\n                     (sqrt(5) - 1)  %k  (- 1)\n                                      1           n\n          (%o2) a  = ------------------------- - ----\n                 n               n                  n\n                                2                5 2\n                                                          n\n                                             (sqrt(5) + 1)  %k\n                                                              2    2\n                                           + ------------------ - ----\n                                                      n              n\n                                                     2            5 2\n\n     Example of linear recurrence with polynomial coefficients:\n\n          (%i7) 2*x*(x+1)*y[x] - (x^2+3*x-2)*y[x+1] + (x-1)*y[x+2];\n                                   2\n          (%o7) (x - 1) y      - (x  + 3 x - 2) y      + 2 x (x + 1) y\n                         x + 2                   x + 1                x\n          (%i8) solve_rec(%, y[x], y[1]=1, y[3]=3);\n                                        x\n                                     3 2    x!\n          (%o9)                 y  = ---- - --\n                                 x    4     2\n\n     Example of Ricatti type recurrence:\n\n          (%i2) x*y[x+1]*y[x] - y[x+1]/(x+2) + y[x]/(x-1) = 0;\n                                      y         y\n                                       x + 1     x\n          (%o2)         x y  y      - ------ + ----- = 0\n                           x  x + 1   x + 2    x - 1\n          (%i3) solve_rec(%, y[x], y[3]=5)$\n          (%i4) ratsimp(minfactorial(factcomb(%)));\n                                             3\n                                         30 x  - 30 x\n          (%o4) y  = - -------------------------------------------------\n                 x        6      5       4       3       2\n                       5 x  - 3 x  - 25 x  + 15 x  + 20 x  - 12 x - 1584\n\n     See also: `solve_rec_rat', `simplify_products', and\n     `product_use_gamma'.\n\n\n  There are also some inexact matches for `solve_rec'.\n  Try `?? solve_rec' to see them.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1291\n\n",
    "created_at": "2007-11-27T14:55:10Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "solving recurrences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1291",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @burcin kevin.stueve @kcrisman @robert-marik @eviatarbach @rwst ktkohl

Sage should be able to easily solve at least some recurrences.  Maxima is actually pretty capable here.

```
sage: maxima.load('solve_rec')
?\/Users\/was\/s\/local\/share\/maxima\/5\.13\.0\/share\/contrib\/solve_rec\/solve_rec\.mac
sage: print maxima('solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n])')
                         n          n                       n
            (sqrt(5) - 1)  %k  (- 1)           (sqrt(5) + 1)  %k
                             1           n                      2    2
       a  = ------------------------- - ---- + ------------------ - ----
        n               n                  n            n              n
                       2                5 2            2            5 2

```



Somebody should wrap this:

```

sage: maxima.solve_rec?
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) 
 -- Function: solve_rec (<eqn>, <var>, [<init>])
     Solves for hypergeometrical solutions to linear recurrence <eqn>
     with polynomials coefficient in variable <var>. Optional arguments
     <init> are initial conditions.

     `solve_rec' can solve linear recurrences with constant
     coefficients, finds hypergeometrical solutions to homogeneous
     linear recurrences with polynomial coefficients, rational
     solutions to linear recurrences with polynomial coefficients and
     can solve Ricatti type recurrences.

     Note that the running time of the algorithm used to find
     hypergeometrical solutions is exponential in the degree of the
     leading and trailing coefficient.

     To use this function first load the `solve_rec' package with
     `load(solve_rec);'.

     Example of linear recurrence with constant coefficients:

          (%i2) solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n]);
                                  n          n
                     (sqrt(5) - 1)  %k  (- 1)
                                      1           n
          (%o2) a  = ------------------------- - ----
                 n               n                  n
                                2                5 2
                                                          n
                                             (sqrt(5) + 1)  %k
                                                              2    2
                                           + ------------------ - ----
                                                      n              n
                                                     2            5 2

     Example of linear recurrence with polynomial coefficients:

          (%i7) 2*x*(x+1)*y[x] - (x^2+3*x-2)*y[x+1] + (x-1)*y[x+2];
                                   2
          (%o7) (x - 1) y      - (x  + 3 x - 2) y      + 2 x (x + 1) y
                         x + 2                   x + 1                x
          (%i8) solve_rec(%, y[x], y[1]=1, y[3]=3);
                                        x
                                     3 2    x!
          (%o9)                 y  = ---- - --
                                 x    4     2

     Example of Ricatti type recurrence:

          (%i2) x*y[x+1]*y[x] - y[x+1]/(x+2) + y[x]/(x-1) = 0;
                                      y         y
                                       x + 1     x
          (%o2)         x y  y      - ------ + ----- = 0
                           x  x + 1   x + 2    x - 1
          (%i3) solve_rec(%, y[x], y[3]=5)$
          (%i4) ratsimp(minfactorial(factcomb(%)));
                                             3
                                         30 x  - 30 x
          (%o4) y  = - -------------------------------------------------
                 x        6      5       4       3       2
                       5 x  - 3 x  - 25 x  + 15 x  + 20 x  - 12 x - 1584

     See also: `solve_rec_rat', `simplify_products', and
     `product_use_gamma'.


  There are also some inexact matches for `solve_rec'.
  Try `?? solve_rec' to see them.
```


Issue created by migration from https://trac.sagemath.org/ticket/1291





---

archive/issue_comments_008106.json:
```json
{
    "body": "Some questions must be answered before doing this:\n* Where would this live, `misc/`?\n* Which way to represent recurrence relations, \n  1. equations of indexed values (Maxima);\n  2. equations of function expressions (Sympy);\n  3. a dedicated class/ring like in #15714?\n* Who commits to the review?",
    "created_at": "2015-02-02T16:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1291#issuecomment-8106",
    "user": "@rwst"
}
```

Some questions must be answered before doing this:
* Where would this live, `misc/`?
* Which way to represent recurrence relations, 
  1. equations of indexed values (Maxima);
  2. equations of function expressions (Sympy);
  3. a dedicated class/ring like in #15714?
* Who commits to the review?
