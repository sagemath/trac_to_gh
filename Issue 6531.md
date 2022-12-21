# Issue 6531: Add generic ring classes to reference manual

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-14 09:59:29

Assignee: tba

Keywords: rings documentation doctest

Module `sage.rings.ring` contains 11 base classes for various types of ring. This should be added to the reference manual. The file also needs a few more doctests to get to 100% coverage.


---

Comment by davidloeffler created at 2009-07-14 10:11:46

patch against 4.1


---

Attachment

This patch does the ReSTifying, adds all missing doctests (although I cheated by flagging some old unpickling functions with "not tested"), and comments out a few methods that achieve nothing at all.


---

Attachment

Replaces previous; rebased to 4.1.1


---

Comment by cremona created at 2009-08-30 14:43:38

On applying this to 4.1.1 there were some merge problems, which I fixed.  The second patch replaces the first and applies to 4.1.1.   I kept the author's name to David!


---

Comment by mvngu created at 2009-08-31 06:03:39

Resolution: fixed


---

Comment by mvngu created at 2009-08-31 06:03:39

Merged `trac_6531-restify_generic_ring-rebase.patch`. See #6850 for a follow-up to this ticket.
