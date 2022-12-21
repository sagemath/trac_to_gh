# Issue 6536: Constructor in sage.rings.number_field.order.Order calls a method of the wrong class

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-15 07:37:59

Assignee: was

At the moment the `__init__` method of class `sage.rings.number_field.order.Order` calls `DedekindDomain.__init__`, despite the fact that `Order` doesn't inherit from `DedekindDomain`. This hasn't caused any problems yet, since `DedekindDomain` inherits its `__init__` function from `IntegralDomain` (which *is* the correct base class for `Order`). But nonetheless it is sloppy coding, and if the Dedekind domain class is either deleted or added to it will cause weird behaviour.


inherits from `sage.rings.ring.IntegralDomain`, but its `__init__` method , despite the fact that


---

Attachment

Here's a two-line fix.


---

Comment by was created at 2009-07-21 04:56:06

Nicely spotted.


---

Comment by davidloeffler created at 2009-07-21 08:15:46

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:15:46

Changing assignee from was to davidloeffler.


---

Comment by mvngu created at 2009-07-23 08:30:00

Resolution: fixed
