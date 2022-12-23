# Issue 7256: reset() needs to be improved

Issue created by migration from https://trac.sagemath.org/ticket/7256

Original creator: mhampton

Original creation time: 2009-10-20 19:52:35

Assignee: wstein

Keywords: reset, notebook,sage-4.1.2

In sage-4.1.2, reset() causes problems by deleting 'sagenb' from the namespace; there may be other important things deleted as well.

A simple fix might be to add 'sagenb' to the sage.misc.reset.EXCLUDE list.  But perhaps a more extensive rewrite of this function would be better.


---

Comment by mhampton created at 2009-10-20 19:53:49

Resolution: duplicate


---

Comment by mhampton created at 2009-10-20 19:54:11

This is a duplicate of #7255, sorry about that.
