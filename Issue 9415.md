# Issue 9415: sorting points on elliptic curves over number fields silently fails

Issue created by migration from Trac.

Original creator: rkirov

Original creation time: 2010-07-03 02:56:21

Assignee: cremona

Over QQ everything works fine:

```
sage: E = EllipticCurve([-1,0])
sage: L = [E(0,0),E(1,0)]
sage: L2 = [L[1],L[0]]
sage: print sorted(L)
[(0 : 0 : 1), (1 : 0 : 1)]
sage: print sorted(L2)
[(0 : 0 : 1), (1 : 0 : 1)]
```


But over number fields, sorting quietly returns the same list as input, with no warnings.

```
sage: K2.<b> = NumberField(x^2+2)
sage: E2 = EllipticCurve(K2,[-16,16])
sage: L = [E2(4*b - 10 ,18*b + 28) , E2(4*b - 4 , 20 )]
sage: L2 = [L[1],L[0]]
sage: print sorted(L)
[(4*b - 10 : 18*b + 28 : 1), (4*b - 4 : 20 : 1)]
sage: print sorted(L2)
[(4*b - 4 : 20 : 1), (4*b - 10 : 18*b + 28 : 1)]
```



---

Comment by rkirov created at 2011-01-10 22:45:43

Resolution: duplicate


---

Comment by rkirov created at 2011-01-10 22:45:43

culprit is in #10583
