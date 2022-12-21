# Issue 2908: Polynomial gcd doesn't take coefficients into account

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-04-13 17:47:25

Assignee: somebody

With 3.0.alpha2 I get the following:


```
sage: R.<x> = QQ[]
sage: p = 2*x; q = 2*x
sage: p.gcd(q)
x
sage: R.<x> = ZZ[]
sage: p = 2*x; q = 2*x
sage: p.gcd(q)
2*x

sage: R.<x> = GF(5)[]
sage: p = 2*x; q = 2*x
sage: p.gcd(q)
x

sage: R.<x,y> = QQ[]
sage: p = 2*x; q = 2*x
sage: p.gcd(q)
x

sage: R.<x,y> = ZZ[]
sage: p = 2*x; q = 2*x
sage: p.gcd(q)
2*x

sage: R.<x,y> = GF(5)[]
sage: p = 2*x; q = 2*x
sage: p.gcd(q)
x
```





---

Comment by cwitty created at 2008-04-13 18:16:50

I think that GCDs for polynomials over a field should return monic polynomials (which seems to be the current behavior); that is, I think this bug is invalid.

(According to _Algorithms for Computer Algebra_, for instance, GCD is defined only up to units; so for your first problem, x, 2*x, and 22/7*x would all be GCDs of p and q.  We need to pick one, and picking the monic polynomial seems like the best choice.)

What do you think this should return?

```
sage: R.<x> = QQ[]
sage: p = (5*x + 7) * (3*x + 1)
sage: q = (x/7 + 1/5) * (2*x + 2)
sage: p.gcd(q)
x + 7/5
```



---

Comment by burcin created at 2008-04-13 18:51:35

Resolution: invalid


---

Comment by burcin created at 2008-04-13 18:51:35

You're right, GCD is defined up to units and this is invalid.
