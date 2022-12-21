# Issue 2789: multivariate polynomials over residue fields of number fields are broken

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-04-03 03:50:11

Assignee: somebody

This example from Genya Zaytman:


```
sage: F1.<u> = NumberField(x^6 + 6*x^5 + 124*x^4 + 452*x^3 + 4336*x^2 + 8200*x + 42316)
sage: reduct_id = F1.factor_integer(47)[0][0]
sage: Rf = F1.residue_field(reduct_id)   # = GF(47^3)
sage: R1.<X,Y> = PolynomialRing(Rf)
sage: ubar = Rf(u)
sage: I = ideal([ubar*X+Y])
sage: I.groebner_basis()
[boom]
```


Basically all we're doing is working with polynomials over a finite field. Perhaps the singular interface can't handle the way the field is presented, or something like that.



---

Comment by ncalexan created at 2009-01-22 09:02:38

This now works without major changes... but I found a show stopper bug.  It had to do with hashing "large" residue fields, meaning large characteristic residue fields.  The hash method tried to hash an ideal of the residue field itself, which tried to hash its parent, leading to an infinite loop.

This means that at no time has a residue field with cardinality a very large prime been created in Sage!

I've added the obvious .ideal() method, tested the hashing and construction for larger examples, and added doctests showing Groebner basis computations.


---

Comment by ncalexan created at 2009-01-22 09:02:38

Changing component from basic arithmetic to commutative algebra.


---

Comment by ncalexan created at 2009-01-22 09:02:38

Changing assignee from somebody to malb.


---

Comment by ncalexan created at 2009-01-22 09:02:38

Changing priority from major to critical.


---

Comment by ncalexan created at 2009-01-22 09:02:38

Changing keywords from "" to "residue field multivariate prime groebner basis".


---

Attachment

replaces some line numbers in verbose output by ...


---

Comment by mabshoff created at 2009-01-23 02:33:12

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 02:33:12

Merged in Sage 3.3.alpha1
