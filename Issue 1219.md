# Issue 1219: bug in eigenspaces over CC

Issue created by migration from https://trac.sagemath.org/ticket/1219

Original creator: wdj

Original creation time: 2007-11-20 19:56:40

Assignee: was

Something funny is going on:


```
sage: MS = MatrixSpace(CC, 2, 2)
sage: A = MS([[1,5],[3,-1]])
sage: A.eigenspaces()

[
(4.00000000000000, [
(1.00000000000000, 1.00000000000000)
]),
(-4.00000000000000, [

])
]
sage: A.eigenspaces()[0]

(4.00000000000000, [
(1.00000000000000, 1.00000000000000)
])
sage: A.eigenspaces()[1]

(-4.00000000000000, [

])
sage: MS = MatrixSpace(QQ, 2, 2)
sage: A = MS([[1,5],[3,-1]])
sage: A.eigenspaces()

[
(4, [
(1, 1)
]),
(-4, [
(1, -5/3)
])
]
```

I find it strange that eigenspaces works for QQ
but not for the larger field CC.

Willam: The issue above is undoubtedly that
there is no specialized implementation of matrices over CC.
It's just completely generic code.  So some generic echelon
is going wrong.  



---

Comment by ncalexan created at 2008-02-17 06:52:41

#1706 and #2050 are essentially the same.


---

Comment by ncalexan created at 2008-02-17 06:52:41

Resolution: duplicate
