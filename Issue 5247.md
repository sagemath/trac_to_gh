# Issue 5247: cuspform_lseries() computing sign of functional equation incorrectly

Issue created by migration from https://trac.sagemath.org/ticket/5247

Original creator: mabshoff

Original creation time: 2009-02-12 16:43:56

Assignee: craigcitro

Sal reports: The following computation should produce identical values in the last line:

```
E=EllipticCurve('37b2')
h=E.modular_form()
Lh = h.cuspform_lseries()
LE=E.lseries()
h.elliptic_curve()==E, Lh(1), LE(1)
```

The output is:

```
(True, 0, 0.725681061936153)
```

I'm running Sage 3.3.alpha3 of sage.math.

The problem seems to be the sign of the functional equation -- it looks like the cuspform_lseries() incorrectly computes it to be -1, forcing the value at s=1 to be 0. In sage/modular/modform/element.py the sign of the functional equation fed into the Dokchister is computed by

```
e = (-1)**(l/2)*n.atkin_lehner_operator().matrix()[0,0]
```

which Gonzalo and Mark tell me is not correct.


---

Comment by mabshoff created at 2009-02-14 02:52:41

This is a dupe of #5262. William did open the other ticket later, but since #5262 has the better description I am closing this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 02:52:41

Resolution: duplicate
