# Issue 6715: spell-check all modules under sage/logic

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-09 16:09:50

Assignee: tba

As the subject says.


---

Attachment

based on Sage 4.1.1.rc2


---

Comment by mvngu created at 2009-08-09 16:42:49

Patches should be applied in this order:
 1. `trac_6715-unix-endlines.patch` --- Most files under the directory `sage/logic` are in the DOS text file format. This patch converts all such files to the Unix text file format.
 1. `trac_6715-spell-check-logic.patch` --- This patch spell-checks all modules under `sage/logic`.


---

Comment by mvngu created at 2009-08-11 12:23:20

based on Sage 4.1.1.rc2


---

Attachment

looks good, only comments and doc-lines touched, no code or doctests.

there is just a "newline missing" note from mercurial at the bottom of the first part of the first patch. i think it is still ok, though (line 123 in sage/logic/booleval.py, first patch).


---

Comment by mvngu created at 2009-08-14 10:42:16

Resolution: fixed


---

Comment by mvngu created at 2009-08-14 10:42:16

Merged both patches.
