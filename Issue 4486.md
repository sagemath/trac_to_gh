# Issue 4486: Clean up partitions_c.cc and partitions_c.h

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-09 23:22:58

Assignee: tornaria

These files need audited. In particular, `partitions_c.cc` should depend on `partitions_c.h`, and shouldn't duplicate the code there. Someone familiar with C should go ahead and clean these files up.


---

Comment by AlexGhitza created at 2009-01-23 02:47:34

Changing type from defect to enhancement.


---

Comment by mmezzarobba created at 2015-04-14 07:24:22

Perhaps they could just be replaced by the implementation in arb once arb becomes a standard part of Sage.
