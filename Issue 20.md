# Issue 20: coercion issues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:20:48

Assignee: somebody

{{{From David Harvey:
Further to our discussion of a few days ago, I found something quite confusing, not sure what the correct behaviour should be.
 
sage: poly_ring1.<gen1> = PolynomialRing(QQ)
sage: poly_ring2.<gen2> = PolynomialRing(QQ)
sage: huge_ring.<x> = PolynomialRing(poly_ring1)
sage: huge_ring(gen1)
 gen1
sage: huge_ring(gen2)
 x
 
In the first example gen1 is getting coerced into a constant polynomial because it belongs to the coefficient ring, and in the second example it's "renaming the variable". I suppose that makes sense, although I'm a bit uneasy about the second one.
 
BUT it's not consistent with the behaviour for power series:
 
sage: power_ring1.<gen1> = PowerSeriesRing(QQ)
sage: power_ring2.<gen2> = PowerSeriesRing(QQ)
sage: huge_power_ring.<x> = PowerSeriesRing(power_ring1)
sage: huge_power_ring(gen1)
 x
sage: huge_power_ring(gen2)
 x
 
Is this a bug?

Response: from william: "Yes"
}}}


---

Comment by was created at 2007-01-07 03:36:23

This is fixed in sage-1.5:

```
sage: power_ring1.<gen1> = PowerSeriesRing(QQ)
sage: power_ring2.<gen2> = PowerSeriesRing(QQ)
sage: huge_power_ring.<x> = PowerSeriesRing(power_ring1)
sage: huge_power_ring(gen1)
gen1
sage: huge_power_ring(gen2)
x
```



---

Comment by was created at 2007-01-07 03:36:23

Resolution: fixed
