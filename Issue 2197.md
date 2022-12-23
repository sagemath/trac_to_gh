# Issue 2197: Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0

Issue created by migration from https://trac.sagemath.org/ticket/2197

Original creator: cremona

Original creation time: 2008-02-17 19:10:18

Assignee: was

The code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.

Note that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.

The patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).


---

Comment by mabshoff created at 2008-02-17 21:16:23

Resolution: duplicate


---

Comment by mabshoff created at 2008-02-17 21:16:23

This is a duplicate of #2196.
