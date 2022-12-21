# Issue 762: Elliptic curve L-series bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-30 04:34:43

Assignee: was

There is a bug in computing the values along a line of the L-series:


```
sage: E = EllipticCurve('389a')
sage: L = E.Lseries_dokchitser()
sage: E.Lseries_values_along_line(0.5, 3, 5)
Traceback (most recent call last):
...
ValueError: too many values to unpack
```


This is just a light wrapper around Rubinstein's lcalc, so should be very easy to fix.


---

Comment by mabshoff created at 2007-10-28 23:27:22

With 2.8.10.alpha1 we are getting a different error:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10.alpha1, Release Date: 2007-10-27               |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: E = EllipticCurve('389a')
sage: sage: L = E.Lseries_dokchitser()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/tmp/Work-mabshoff/sage-2.8.10.alpha1/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'Lseries_dokchitser'
sage: sage: E.Lseries_values_along_line(0.5, 3, 5)
```


Cheers,

Michael


---

Comment by was created at 2007-10-28 23:58:26

this fixes the bug.


---

Attachment


---

Comment by mabshoff created at 2007-11-01 09:43:21

applied to 2.8.11.alpha0


---

Comment by mabshoff created at 2007-11-01 09:43:21

Resolution: fixed
