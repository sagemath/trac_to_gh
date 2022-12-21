# Issue 994: ntl_GF2X class has very strange __int__ method

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-25 05:15:01

Assignee: malb

The `__int__` method on the ntl_GF2X class is quite strange.   It takes the terms of the polynomial from x<sup>0</sup> to x<sup>31</sup> (or x<sup>63</sup>), and treats them as the bits of a machine long (in a non-portable way, depending on the endianness of the processor).

Perhaps it should use all the terms, and return a Python long if necessary (in little-endian format, as documented for the conversion from Integer to GF2X)?  Or maybe the `__int__` method should not be implemented at all?


---

Comment by malb created at 2007-10-25 22:05:20

Changing status from new to assigned.


---

Comment by malb created at 2007-10-25 22:05:20

as I called it __int__ and not BytesFromGF2X I think the behaviour is 
wrong and thus I changed it locally to return the constant coefficient if the  polynomial is constant. The patch to this is stuck in the patch attached to #416. So if that is accepted this ticket should be closed.


---

Comment by cwitty created at 2007-10-27 02:48:38

Resolution: fixed
