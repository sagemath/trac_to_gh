# Issue 5947: Coleman integrals of exact forms

Issue created by migration from https://trac.sagemath.org/ticket/5947

Original creator: jen

Original creation time: 2009-04-30 14:50:30

Assignee: was

Say I define a hyperelliptic curve and calculate the action of Frobenius \phi on basis differentials w_i. Sage outputs the matrix and f_i such that \phi* w_i = df_i + \sum A_ij w_j.
Then for f_i, int(df_i,P,Q) = f_i(Q)-f_i(P). However, it seems Sage is computing f.diff() to be -df instead of df.


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x*(x-1)*(x+9))
sage: K = Qp(7,10)
sage: HK = H.change_ring(K)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)
sage: f = forms[0]
sage: P = HK(9,36)
sage: Q = HK.teichmuller(P)
sage: HK.coleman_integral(f.diff(),P,Q)
6*7^2 + 5*7^3 + 7^4 + 7^5 + 7^6 + 3*7^7 + 5*7^9 + 4*7^10 + O(7^11)
```

However, it seems that f.diff() is actually -f.diff(), as the answer should be

```
sage: f(Q[0],Q[1])-f(P[0],P[1])
7^2 + 7^3 + 5*7^4 + 5*7^5 + 5*7^6 + 3*7^7 + 6*7^8 + 7^9 + 2*7^10 + O(7^11)
```

which is in fact the negation of what it's computing:

```
sage: f(P[0],P[1])-f(Q[0],Q[1])
6*7^2 + 5*7^3 + 7^4 + 7^5 + 7^6 + 3*7^7 + 5*7^9 + 4*7^10 + O(7^11)
```



---

Comment by robertwb created at 2009-05-19 08:34:16


```
sage: sage: R.<x> = QQ['x']
sage: sage: H = HyperellipticCurve(x*(x-1)*(x+9))
sage: from sage.schemes.elliptic_curves.monsky_washnitzer import SpecialHyperellipticQuotientRing
sage: x, y = SpecialHyperellipticQuotientRing(H).gens()
sage: (x+y).diff()
((-9+2*y)*1 + 16*x + 3*x^2) dx/2y
sage: x.diff()
2*y*1 dx/2y
```


So it appears that the sign problem is in the coleman_integral, not diff.


---

Comment by robertwb created at 2009-05-20 07:43:46

See fix at #5948.


---

Comment by mhansen created at 2009-12-07 08:35:53

Resolution: fixed


---

Comment by mhansen created at 2009-12-07 08:35:53

This was fixed by #5948.
