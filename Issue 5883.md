# Issue 5883: integrate relevant functionality from modular/modsym/p1list.pyx into projective space code

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-04-24 00:23:07

Assignee: AlexGhitza

Keywords: rational points projective line finite

There is optimised code in p1list.pyx for creating the list of points on P1 over Z/NZ.  It would be nice to also have this available as, for instance:


```
sage: P1 = ProjectiveSpace(1, Integers(N))
sage: P1.rational_points()
```




---

Comment by AlexGhitza created at 2009-04-24 00:25:34

This can be done independently of, but will greatly benefit from, John's work on #5876.
