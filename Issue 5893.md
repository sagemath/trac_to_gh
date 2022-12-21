# Issue 5893: Norm Form for Number Fields and Orders

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2009-04-25 09:43:11

Assignee: roed

Often if one is doing computations with number fields and orders by hand, it's useful to have the norm form with respect to a given basis.  For example:


```
sage: K.<sqrt2> = NumberField(x^2 - 2); T.<a, b> = QQ[]
sage: K.power_basis()
[1, sqrt2]
sage: K.norm_form([a, b])
a^2 - 2*b^2
sage: K.norm_form([1, b])
1 - 2*b^2
sage: OK = NumberField(x^2-5, names='sqrt5').maximal_order(); T.<a, b> = ZZ[]
sage: OK.basis()
[1/2*sqrt5 + 1/2, sqrt5]
sage: OK.norm_form([a, b])
-a^2 - 5*a*b - 5*b^2
```




---

Comment by davidloeffler created at 2009-07-21 08:19:10

Changing component from number theory to number fields.
