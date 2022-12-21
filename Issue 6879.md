# Issue 6879: Elliptic curve constructor does not check if the base is a field properly

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-09-03 16:24:13

Assignee: davidloeffler

CC:  jcooley

Keywords: elliptic curve

Example:

```
sage: E = EllipticCurve(QQbar,[1,0])
sage: E.base_field()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/jec/sage/isog50.py in <module>()

AttributeError: 'EllipticCurve_generic' object has no attribute 'base_field'
```


This is because the curve constructed is an ell_generic and not an ell_field, despite {{{QQbar.is_field()}} returning True.

Similarly with RR and CC in place of QQbar.

All that is required is a two-line addition around line 213 of elliptic_curves/constructor.py.

Patch up soon.


---

Attachment

Applies to 4.1.1


---

Comment by cremona created at 2009-09-03 16:46:31

Patched applies to 4.1.1.  All sage/schemes/elliptic_curves tests ok.


---

Comment by mhansen created at 2009-09-26 04:37:06

Looks good to me.


---

Comment by mvngu created at 2009-09-26 07:05:00

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:51:07

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
