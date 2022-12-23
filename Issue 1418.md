# Issue 1418: magma element __floordiv__

Issue created by migration from https://trac.sagemath.org/ticket/1418

Original creator: jbmohler

Original creation time: 2007-12-07 11:52:22

Assignee: was

I added a !__floordiv!__ to the magma element for the 'div' operator.


---

Comment by jbmohler created at 2007-12-07 12:37:44

Oops, this should go on hold.  I screwed it up in various ways with the doc-tests.


---

Attachment

a fixed patch which should work


---

Comment by jbmohler created at 2007-12-19 01:46:19

I just added a patch which adds "# optional" at the right points.


---

Comment by ncalexan created at 2008-01-20 06:44:44

Looks fine, apply.


---

Comment by mabshoff created at 2008-01-21 05:42:00

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:42:00

Resolution: fixed
