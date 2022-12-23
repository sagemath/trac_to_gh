# Issue 2515: ExtendedRationalField not so extended

Issue created by migration from https://trac.sagemath.org/ticket/2515

Original creator: edrex

Original creation time: 2008-03-14 08:10:23

Assignee: joyner


```
ExtendedRationalField(1)/ExtendedRationalField(0)
```

yields

```
ZeroDivisionError: Rational division by zero
```

Same for ExtendedIntegerRing(1)/ExtendedIntegerRing(0)

Presumably these should both yield +Infinity?


---

Comment by burcin created at 2008-03-14 10:48:09

Changing assignee from joyner to cwitty.


---

Comment by burcin created at 2008-03-14 10:48:09

The way Sage handles infinity should be revised in general. I say `ExtendedRationalRing` (and `ExtendedIntegerRing`) should go away altogether, since the signed and unsigned infinity rings in `sage/rings/infinity.py` handle the situations when infinity is encountered adequately, at least after #1915 is fixed.


---

Comment by burcin created at 2008-03-14 10:48:09

Changing component from group_theory to misc.


---

Comment by mabshoff created at 2009-04-10 21:00:30

This ticket should be closed once #5735 is merged since the functionality will be removed from Sage - for details see that ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 04:10:22

Fixed in Sage 3.4.1.rc3 via #5735.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 04:10:22

Resolution: fixed
