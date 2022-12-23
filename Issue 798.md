# Issue 798: [with patch] MPolynomial_libsingular.subs

Issue created by migration from https://trac.sagemath.org/ticket/798

Original creator: malb

Original creation time: 2007-10-03 03:04:29

Assignee: somebody

This used to be broken:

```
sage: P.<x,y,z> = PolynomialRing(GF(2),3)
sage: f = x + y + 1
sage: f.subs(x=y+1)
0 # used to return 1
```

the attached two patches fixes this.


---

Attachment


---

Comment by was created at 2007-10-04 18:11:40

Resolution: fixed
