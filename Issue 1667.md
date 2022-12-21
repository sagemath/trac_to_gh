# Issue 1667: [with patch, needs review] coercion fixes for PolyBoRi

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-01-03 14:54:15

Assignee: was

Keywords: polybori

`BooleanPolynomialRing` supports coercion from rings where the number of variables is greater than self. This code should be in `__call__` and coercion should first check for the number of variables of the parent ring.

Attached patch fixes this problem, and adds similar coercion and `__call__` semantics to `BooleanMonomialMonoid`. It also fixes minor problems where using iterators of polynomials over a ring other than the current one messes `PolyBoRi` up.


---

Comment by burcin created at 2008-01-03 14:54:52

coercion & minor fixes to polybori


---

Attachment

Looks good to me. This is isolated to polybori, so I merged it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-03 16:01:46

Resolution: fixed
