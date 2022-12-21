# Issue 1120: [with patch] speed up point counting for elliptic curves over GF(p^n) if coefficients are in GF(p)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-07 15:51:26

Assignee: was

If possible #E is computed over the prime subfield now.


```
sage: EllipticCurve(GF(4,'a'),[1,2,3,4,5]).cardinality()
8
sage: k.<a> = GF(3^3)
sage: l = [a^2 + 1, 2*a^2 + 2*a + 1, a^2 + a + 1, 2, 2*a]
sage: EllipticCurve(k,l).cardinality()
WARNING: Using very very stupid algorithm for counting
points over non-prime finite field. Please rewrite.
See the file ell_finite_field.py.
29

sage: l = [1, 1, 0, 2, 0]
sage: EllipticCurve(k,l).cardinality()
38
```



---

Attachment


---

Comment by robertwb created at 2007-11-18 09:06:00

Works great for me.


---

Comment by mabshoff created at 2007-11-19 21:27:21

Resolution: fixed


---

Comment by mabshoff created at 2007-11-19 21:27:21

Merged in 2.8.13.alpha1

Applied with slight fuzz:

```
mabshoff`@`sage:$hg import ell_finite_field_order.patch
applying ell_finite_field_order.patch
patching file sage/schemes/elliptic_curves/ell_finite_field.py
Hunk #4 succeeded at 330 with fuzz 1 (offset 0 lines).
```


Cheers,

Michael
