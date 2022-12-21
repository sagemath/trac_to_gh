# Issue 1783: fix latex errors with fraction field elements

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-01-15 19:06:52

Assignee: malb


```
sage:             sage: R = PolynomialRing(QQ, 'x').fraction_field()
sage:             sage: x = R.gen()
sage:             sage: a = 1/x
sage:             sage: a._FractionFieldElement__numerator = R(0)
sage:             sage: latex(a)
\frac{0}{x}
```


It should instead give 0.


---

Attachment


---

Attachment


---

Comment by ncalexan created at 2008-01-15 19:29:23

This should go in.


---

Comment by mabshoff created at 2008-01-15 19:47:56

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 19:47:56

Both patches merged in Sage 2.10.alpha4
