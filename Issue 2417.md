# Issue 2417: discriminant method sometimes returns values in the fraction field

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-07 04:43:09

Assignee: was

For non-monic polynomials, the discriminant method introduced in #2392 returns values in the fraction field of the base ring, instead of in the base ring.

```
sage: R.<y> = QQ[]
sage: S.<x> = R[]
sage: (x*y+x+y+1).discriminant()
1
sage: (x*y+x+y+1).discriminant().parent()
Fraction Field of Univariate Polynomial Ring in y over Rational Field
```




---

Attachment

This is due to the fact that discriminants are computed via resultants, using a formula that sometimes divides the resultant by the leading coefficient.  When the coefficients are themselves polynomials, this makes the result appear in the fraction field.

The fix is very simple: just coerce the result back into the base ring before returning.  This is in the attached patch, together with a couple of typo fixes.  I've also replaced one of the doctests that was supposed to illustrate precisely this behavior (but didn't) with Carl's example.


---

Comment by robertwb created at 2008-03-26 06:03:00

Works well for me.


---

Comment by mabshoff created at 2008-03-26 22:09:33

Resolution: fixed


---

Comment by mabshoff created at 2008-03-26 22:09:33

Merged in Sage 2.11.alpha2
