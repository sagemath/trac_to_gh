# Issue 4262: Elliptic curve a_invariants command returns a list reference (BAD!!)

Issue created by migration from https://trac.sagemath.org/ticket/4262

Original creator: was

Original creation time: 2008-10-11 08:25:23

Assignee: was

This sucks:

```
sage: E = EllipticCurve([1,0,0,0,1])
sage: E.a_invariants()[0] = 100000000
sage: E
Elliptic Curve defined by y^2 + 100000000*x*y  = x^3 +1 over Rational Field
```



---

Attachment


---

Comment by was created at 2008-10-11 08:32:20





---

Comment by malb created at 2008-10-11 08:33:32

Shouldn't we just return a tuple to emphasise that this is invariant?


---

Comment by was created at 2008-10-11 09:14:42

Changing to tuples should be another ticket.


---

Comment by was created at 2008-10-11 09:46:42

See #4264 for changing to return a tuple.


---

Comment by mabshoff created at 2008-10-11 12:11:02

Merged in Sage 3.1.3.rc0


---

Comment by mabshoff created at 2008-10-11 12:11:02

Resolution: fixed
