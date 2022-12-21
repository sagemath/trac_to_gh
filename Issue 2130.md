# Issue 2130: Question about list( FACTORS) command

Issue created by migration from Trac.

Original creator: gmoose05

Original creation time: 2008-02-09 20:04:40

Assignee: malb

Given a factorization of a polynomial formed by ans.factor(); list(ans.factor()) does not change * symbols to commas, but ignores constants.


```
sage: t = PolynomialRing(QQ,'t',20).gens();
ans =  -t[1]^4*t[10]^3*t[13]*t[12] + t[1]^4*t[10]^2*t[12] + t[1]^2*t[11]*t[10]^2*t[13]*t[12] + t[1]^2*t[10]^2*t[13] - t[1]^2*t[11]*t[10]*t[12] - t[1]^2*t[10] - t[11]*t[10]*t[13] + t[11]; ans;
factt = ans.factor(); factt

(-1) * (x0*x3 - 1) * (t1^2*x0 - x1) * (t1^2*x0*x2 - 1)
```


{{{ 
sage: list(factt)
[(x0*x3 - 1, 1), (t1^2*x0 - x1, 1), (t1^2*x0*x2 - 1, 1)]
}}}

Can this be corrected, or is there a different command I can use?



---

Comment by was created at 2008-02-09 22:38:34

Resolution: fixed


---

Comment by was created at 2008-02-09 22:38:34

Use `f.unit()`

```
sage:  t = PolynomialRing(QQ,'t',20).gens();
sage: ans= -t[1]^4*t[10]^3*t[13]*t[12] + t[1]^4*t[10]^2*t[12] + t[1]^2*t[11]*t[10]^2*t[13]*t[12] + t[1]^2*t[10]^2*t[13] - t[1]^2*t[11]*t[10]*t[12] - t[1]^2*t[10] - t[11]*t[10]*t[13] + t[11]; ans;
sage: f = ans.factor()
sage: list(f)
[(t10*t13 - 1, 1), (t1^2*t10 - t11, 1), (t1^2*t10*t12 - 1, 1)]
sage: f.unit()
-1
```


For future reference this should have been a question asked in sage-support, not a trac ticket.
