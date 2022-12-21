# Issue 6361: elliptic curves -- easy to fix mistake in docs

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-19 18:02:44

Assignee: was


```
eval_modular_form(points, prec) 
Evaluate the L-series of this elliptic curve at points in CC 
INPUT: 
•points - a list of points in the half-plane of convergence 
•prec - precision 
OUTPUT: A list of values L(E,s) for s in points 
Note: Better examples are welcome. 
EXAMPLES: 
sage: E=EllipticCurve(’37a1’) 
sage: E.eval_modular_form([1.5+I,2.0+I,2.5+I],0.000001) 
[0, 0, 0] 
```


It should *NOT* say L-series above.  It should say modular form.


---

Attachment

based on Sage 4.0.2


---

Comment by mhansen created at 2009-06-20 00:54:40

Looks good to me.


---

Comment by rlm created at 2009-06-24 10:04:05

Resolution: fixed
