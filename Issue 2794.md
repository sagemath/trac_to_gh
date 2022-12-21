# Issue 2794: [with patch, needs review] PolyBoRi to Magma conversion

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-04 09:50:44

Assignee: malb

CC:  burcin

Keywords: polybori, magma

This now works:

```
sage: B.<a,b,z> = BooleanPolynomialRing(3)
sage: B._magma_()

Affine Algebra of rank 3 over GF(2)
Lexicographical Order
Variables: a, b, z
Quotient relations:
[
a^2 + a,
b^2 + b,
z^2 + z
]
sage: magma(a+b)
a + b
```



---

Attachment


---

Comment by mhansen created at 2008-04-04 21:29:56

Looks good to me.


---

Comment by mabshoff created at 2008-04-04 22:14:53

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 22:14:53

Merged in Sage 3.0.alpha1
