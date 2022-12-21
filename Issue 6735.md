# Issue 6735: spell-check all modules under sage/structure

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-11 10:08:04

Assignee: tba

As the subject says.


---

Comment by mvngu created at 2009-08-11 17:33:36

based on Sage 4.1.1.rc2


---

Attachment

All these changes look good; as discussed on sage-devel, "Pyrex" should be changed to "Cython" but that is done on another ticket.  I tested the patch just to be safe, but as expected these changes don't cause any doctesting problems.


---

Comment by mvngu created at 2009-08-12 06:26:22

Resolution: fixed
