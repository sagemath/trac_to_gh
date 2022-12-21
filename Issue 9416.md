# Issue 9416: elliptic curve E.__call__ is not fully equivalent to E.point, specifically for check flag

Issue created by migration from Trac.

Original creator: rkirov

Original creation time: 2010-07-03 03:00:44

Assignee: AlexGhitza

For example, the flag check=False can only be used with E.point()


```
sage: emb = K2.places()[0]
sage: E_complex = EllipticCurve(CC,map(emb, E2point.a_invariants()))
sage: P = L2[-1]
sage: print 'Exact arithmetic:', P in E2
Exact arithmetic: True
sage: P_complex = map(emb,P)
sage: E_complex(P_complex, check=False)
TypeError: __call__() got an unexpected keyword argument 'check'

sage: E_complex.point(P_complex, check=False)
(-10.0000000000000 + 5.65685424949238*I : 28.0000000000000 + 25.4558441227157*I : 1.00000000000000)
```



---

Comment by rkirov created at 2010-07-03 03:01:05

Changing assignee from AlexGhitza to cremona.


---

Comment by rkirov created at 2010-07-03 03:01:05

Changing component from algebra to elliptic curves.


---

Comment by rkirov created at 2010-07-03 03:01:32

Changing priority from major to minor.
