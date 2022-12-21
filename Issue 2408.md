# Issue 2408: MPolynomial_libsingular.factor does not set units

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-03-06 17:36:30

Assignee: malb

MPolynomial_libsingular.factor does not set units.

We now have


```
sage: R.<x,y,z> = QQ[]
sage: p = -1*(x*y+z)  
sage: F = p.factor(); F
(-1) * (x*y + z)
sage: F.unit()
1
sage: len(F)
2
```


It should be

```
sage: F = p.factor(); F
x*y + z
sage: F.unit()
-1
sage: len(F)
1


---

Comment by burcin created at 2008-03-06 18:07:03

This works on 2.10.2, I was using 2.10 at the time. Sorry for the noise.


---

Comment by burcin created at 2008-03-06 18:07:03

Resolution: invalid
