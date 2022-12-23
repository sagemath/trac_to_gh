# Issue 350: bug in rational_points on hyperelliptic curve

Issue created by migration from https://trac.sagemath.org/ticket/350

Original creator: was

Original creation time: 2007-04-11 01:53:05

Assignee: was


Hi.
I am quite happy that rational_points() of a hyperelliptic curve over
a finite field lists the poitn at infinity twice, but I don't
understand why it also lists other points twice.

Chris.



```
f = x^8+x+1
ft = f.change_ring(GF(7))
C = HyperellipticCurve(ft)
C.rational_points()
///
[(2 : 0 : 1), (4 : 0 : 1), (2 : 0 : 1), (4 : 0 : 1), (0 : 1 : 1), (6 :
1 : 1), (0 : 6 : 1), (6 : 6 : 1), (0 : 1 : 0), (0 : 1 : 0)]
```




---

Comment by dmharvey created at 2007-08-18 17:29:12

The expression `x^8+x+1` is now a symbolic expression, not a polynomial, so the `change_ring` method is no longer valid.

In any case, the bug appears to be fixed now, so I'm closing this ticket.


---

Comment by dmharvey created at 2007-08-18 17:29:12

Resolution: fixed
