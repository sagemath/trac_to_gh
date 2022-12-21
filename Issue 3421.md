# Issue 3421: [with patch, needs review] MPolynomialRing_libsingular should accept longs in __call__

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-06-13 22:08:37

Assignee: malb

CC:  burcin

This now works:

```
sage: P.<x,y> = PolynomialRing(QQ)
sage: P("111111111111111111111111111111111111111111111111111111111")
111111111111111111111111111111111111111111111111111111111
```



---

Comment by burcin created at 2008-06-14 00:20:34

This still fails on sage.math:


```
sage: P("31367566080")
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/burcin/sage-3.0.2/<ipython console> in <module>()

/home/burcin/sage-3.0.2/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:4707)()

/home/burcin/sage-3.0.2/parent.pyx in sage.structure.parent.Parent._coerce_c (sage/structure/parent.c:3400)()

/home/burcin/sage-3.0.2/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._coerce_c_impl (sage/rings/polynomial/multi_polynomial_libsingular.cpp:4283)()

OverflowError: value too large to convert to int
```



---

Comment by malb created at 2008-06-14 00:47:21

updated patch to address review


---

Attachment

The updated patch addresses that bug.


---

Comment by burcin created at 2008-06-14 00:57:51

Looks good to me.


---

Comment by mabshoff created at 2008-06-15 15:09:41

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 15:09:41

Resolution: fixed
