# Issue 1847: add nice print method for Sha(Elliptic curve) [trivial to implement -- requires taste]

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-19 12:46:42

Assignee: was

Printing of Sha is ugly:


```
sage: E = EllipticCurve('37a')
sage: Sha = E.sha(); Sha
<class 'sage.schemes.elliptic_curves.sha.Sha'>
```



---

Comment by AlexGhitza created at 2009-01-23 20:37:28

Looks good.


---

Comment by mabshoff created at 2009-01-25 20:47:24

This patch causes the following doctest failure:

```
mabshoff`@`geom:/scratch/mabshoff/sage-3.3.alpha3$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha3/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 3639:
    sage: S
Expected:
    <class 'sage.schemes.elliptic_curves.sha_tate.Sha'>
Got:
    Shafarevich-Tate group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
**********************************************************************
```

I guess the obvious fix is to change the doctest.

Cheers,

Michael


---

Attachment

Patch updated.


---

Comment by mabshoff created at 2009-01-28 14:10:39

Merged in Sage 3.3.alpha3


---

Comment by mabshoff created at 2009-01-28 14:10:39

Resolution: fixed
