# Issue 1640: missing documentation Elliptic Curve - heegner_discriminants

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2007-12-30 14:27:11

Assignee: tba

Documentation missing:

```
E = EllipticCurve('5077a')
E.heegner_discriminants?
```



says



```
File:        /opt/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py
Type:        <type 'instancemethod'>
Definition:  E.heegner_discriminants(bound)
Docstring: 
x.__init__(...) initializes x; see x.__class__.__doc__ for signature
```



but



```
E.heegner_index?
```



is ok.


---

Attachment


---

Comment by AlexGhitza created at 2008-01-08 11:28:10

Changing component from documentation to algebraic geometry.


---

Comment by AlexGhitza created at 2008-01-08 11:28:10

Changing assignee from tba to was.


---

Comment by was created at 2008-01-16 17:02:01

Looks very good!


---

Comment by mabshoff created at 2008-01-16 17:05:16

Resolution: fixed


---

Comment by mabshoff created at 2008-01-16 17:05:16

Merged in Sage 2.10.alpha4
