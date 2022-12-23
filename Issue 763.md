# Issue 763: serious bug latexing p-adic L-series

Issue created by migration from https://trac.sagemath.org/ticket/763

Original creator: was

Original creation time: 2007-09-30 05:26:46

Assignee: was

The following are the same L-series twice, but the latex print version is missing the alphas!!


```
sage: E = EllipticCurve('37a')
sage: L = E.padic_lseries(3)
sage: L.series(4)
(O(3^1))*alpha + (O(3^2)) + ((O(3^-1))*alpha + (2*3^-1 + O(3^0)))*T + ((O(3^-1))*alpha + (2*3^-1 + O(3^0)))*T^2 + ((O(3^-2))*alpha + (O(3^-1)))*T^3 + ((O(3^-1))*alpha + (3^-1 + O(3^0)))*T^4 + O(T^5)
sage: latex(L.series(4))
\left(2 \cdot 3^{-1} + O(3^{0})\right)T + \left(2 \cdot 3^{-1} + O(3^{0})\right)T^{2} + \left(3^{-1} + O(3^{0})\right)T^{4} + O(\left(1 + O(3^{5})\right)T^{5})
```



---

Comment by was created at 2007-10-04 00:46:21

Changing status from new to assigned.


---

Comment by was created at 2007-10-04 03:25:33

Resolution: fixed
