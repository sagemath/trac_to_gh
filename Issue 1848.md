# Issue 1848: Elliptic curve Sha an documentation misleading about proof

Issue created by migration from https://trac.sagemath.org/ticket/1848

Original creator: was

Original creation time: 2008-01-19 12:51:26

Assignee: was

CC:  cremona

The sha an function:

```
sage: E = EllipticCurve('37a')
sage: Sha = E.sha(); Sha
<class 'sage.schemes.elliptic_curves.sha.Sha'>
sage: Sha.an()
1    
```

has help that at the beginning misleadingly suggests that it is provably correct when the analytic rank is 1.  Looking at the code, it is clear that currently it is not provably correct except when the rank is 0 and a Manin constant hypothesis holds (which does hold for Cremona's curves). 

Fix: 
   1. Have a proof=False flag that keeps the current implementation
   2. Have a proof=True flag that fails if the Manin constant isn't known by a theorem to be <=2, and which runs new provably correct code in the case of analytic rank 1. 


---

Comment by was created at 2008-01-19 12:51:33

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-07-20 19:46:45

Changing component from number theory to elliptic curves.
