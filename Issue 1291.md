# Issue 1291: solving recurrences

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-27 14:55:10

Assignee: was

CC:  burcin kevin.stueve kcrisman robert.marik eviatarbach rws ktkohl

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



---

Comment by rws created at 2015-02-02 16:40:23

Some questions must be answered before doing this:
 * Where would this live, `misc/`?
 * Which way to represent recurrence relations, 
   1. equations of indexed values (Maxima);
   2. equations of function expressions (Sympy);
   3. a dedicated class/ring like in #15714?
 * Who commits to the review?
