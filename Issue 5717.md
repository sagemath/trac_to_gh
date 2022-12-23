# Issue 5717: subdivide and matrices mod 2 -- printing broken

Issue created by migration from https://trac.sagemath.org/ticket/5717

Original creator: was

Original creation time: 2009-04-08 19:19:01

Assignee: was

Printing of subdivisions of matrices mod 2 is broken.  Also, lifting of matrices should preserve subdivision but doesn't, but that's a separate ticket (#5716)


```
sage: a = random_matrix(GF(2),4)
sage: a.subdivide(2,2)
sage: a
[1 0 1 0]
[1 0 1 0]
[1 1 1 1]
[1 1 0 1]
sage: b = a.lift()
sage: b.subdivide(2,2)
sage: b
[1 0|1 0]
[1 0|1 0]
[---+---]
[1 1|1 1]
[1 1|0 1]
```



---

Comment by was created at 2009-04-08 19:20:04

This is a dup of #5714.


---

Comment by was created at 2009-04-08 19:20:04

Resolution: duplicate
