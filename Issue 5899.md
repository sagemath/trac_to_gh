# Issue 5899: [with patch, needs review] Update Debian build support for Sage spkg

Issue created by migration from https://trac.sagemath.org/ticket/5899

Original creator: tabbott

Original creation time: 2009-04-26 05:39:48

Assignee: tabbott

I've been working on getting the Debian build of Sage updated for the current version.  Because of some refactoring in setup.py for the sage spkg, the SAGE_DEBIAN definition no longer works as intended.  The three patches that are attached should fix this, without having any effect on other systems.  It'd be good to get these merged just to bring down the number of patches I have against Sage (future work for this code is to rename SAGE_DEBIAN to something more appropriate).

They need to be applied in order.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-10-16 08:46:26

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-10-16 08:46:46

Resolution: fixed
