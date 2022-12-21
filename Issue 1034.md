# Issue 1034: clean up 'revlex' term ordering mess

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-30 15:03:33

Assignee: malb

What we call 'revlex' and which translates to 'rp' in Singular is not what is called 'revlex' in literature. Also our generic implementation doesn't match the one of Singular. This needs to be cleaned up.


---

Attachment


---

Comment by malb created at 2007-10-30 16:07:06

the attached patch removes revlex which Singular does not support and introduces invlex which Singular supports and which is only relevant for non-commutative rings.


---

Comment by malb created at 2007-10-30 16:07:06

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-01 10:20:02

applied to 2.8.11.alpha0


---

Comment by mabshoff created at 2007-11-01 10:20:02

Resolution: fixed
