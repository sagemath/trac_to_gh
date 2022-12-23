# Issue 254: p-adic precision drop in evaluating a polynomial

Issue created by migration from https://trac.sagemath.org/ticket/254

Original creator: dmharvey

Original creation time: 2007-02-09 21:16:13

Assignee: somebody


```
sage: R = pAdicField(5)

sage: T.<u> = PolynomialRing(R)

sage: h = u + (1 + O(5^8))*u^2 + (1 + O(5^4))*u^3

sage: h(u)
 (1 + O(5^4))*u^3 + (1 + O(5^4))*u^2 + (1 + O(5^4))*u
```


It looks like the precision of all the coefficient is dropping to that of the lowest precision of the other coefficients. It's not clear to me why the precision is dropping. [What I really want to do is evaluate h(2*u), which should just multiply each coefficient by the appropriate power of 2.]



---

Comment by was created at 2007-08-18 18:10:15

Resolution: fixed


---

Comment by was created at 2007-08-18 18:10:15

David Roe fixed this with his new p-adic polynomials class.
