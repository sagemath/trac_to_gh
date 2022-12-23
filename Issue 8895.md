# Issue 8895: symbolic unit conversion function should ignore non-unit symbolic variables

Issue created by migration from https://trac.sagemath.org/ticket/8895

Original creator: was

Original creation time: 2010-05-05 19:59:18

Assignee: burcin

CC:  jdemeyer

This seems wrong to me:


```
sage: (x * units.length.meter).convert(units.length.mile)
Traceback (most recent call last):
...
ValueError: Incompatible units
sage: (10 * units.length.meter).convert(units.length.mile)
625/100584*mile
```



---

Comment by eviatarbach created at 2011-07-13 01:56:47

Ticket #11592 fixes this.


---

Comment by burcin created at 2011-07-20 17:42:42

Changing component from calculus to symbolics.


---

Comment by burcin created at 2011-07-20 17:42:42

This should be closed as a duplicate of #11592. The patch attached to that ticket fixes this and contains doctests covering William's example from the description.


---

Comment by tscrim created at 2013-03-20 22:59:08

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-03-20 23:06:17

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-03-20 23:06:17

Still fixed in 5.7:

```
sage: (x*units.length.meter).convert(units.length.mile)
(125/201168*x)*mile
sage: (10*units.length.meter).convert(units.length.mile)
625/100584*mile
```



---

Comment by jdemeyer created at 2013-03-29 18:55:41

Resolution: worksforme
