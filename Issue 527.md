# Issue 527: gap -- gap_reset_workspace()

Issue created by migration from https://trac.sagemath.org/ticket/527

Original creator: was

Original creation time: 2007-08-30 06:49:55

Assignee: was

The gap workspace cache should be invalidated not only when the version of gap changes but when the
spkg version number changes.  This very important. 


---

Comment by was created at 2007-09-07 18:30:36

Actually invalidate it even when SAGE is upgraded at all!


---

Comment by was created at 2007-09-07 18:30:52

Changing priority from major to blocker.


---

Comment by was created at 2007-10-05 06:42:43

Changing priority from blocker to critical.


---

Comment by mabshoff created at 2007-10-19 18:47:31

This ticket is related to #407.

Cheers,

Michael


---

Attachment


---

Comment by was created at 2007-11-03 19:22:59

It is also a good idea to replace the gap packages by these:
(I didn't up the version, since forcing an upgrade is pointless.)

  http://sage.math.washington.edu/tmp/gap-4.4.10.spkg

This is for the next release manager.


---

Comment by was created at 2007-11-03 19:22:59

Resolution: fixed
