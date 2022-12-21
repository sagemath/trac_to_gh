# Issue 1414: wrap MPolynomialRing so inject_on() works.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-07 02:15:00

Assignee: malb

This should work but doesn't

```
sage: p = 17; q = (p-1)//2
sage: inject_on()
Redefining: Frac FreeMonoid GF FractionField FiniteField PolynomialRing quotient NumberField LaurentSeriesRing quo 
sage: R = MPolynomialRing(GF(p),q,"x")
Defining x
Defining x0, x1, x2, x3, x4, x5, x6, x7
```




---

Comment by burcin created at 2008-05-22 16:38:03

MPolynomialRing is going to be deprecated, see #2353.


---

Comment by malb created at 2008-08-23 23:04:22

Resolution: wontfix


---

Comment by malb created at 2008-08-23 23:04:22

Since it is deprecated now, I'm closing the ticket as `wontfix`. Mabshoff, do we need to change the milestone?
