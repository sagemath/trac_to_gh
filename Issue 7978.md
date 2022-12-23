# Issue 7978: The file sage/combinat/affine.py contains lots of 'tab' characters

Issue created by migration from https://trac.sagemath.org/ticket/7978

Original creator: jbandlow

Original creation time: 2010-01-18 14:43:28

Assignee: sage-combinat

CC:  sage-combinat

They should be replaced with spaces.


---

Comment by jbandlow created at 2010-01-18 15:17:51

Changing status from new to needs_work.


---

Attachment

Oops.  This patch depends on some patches in the combinat stack.  (I suspect the 'crystal-cleanup' patches.)  The change is trivial, but I'll coordinate with the sage-combinat list before marking this ready for review.


---

Attachment


---

Comment by aschilling created at 2010-01-25 06:31:06

The patch trac_7978_crystal_cleanup-as.patch supersedes Jason's patch. It fixes the whitespace issues in combinat/crystals/affine.py and does a lot more improvements in crystals (see description).


---

Comment by aschilling created at 2010-01-25 06:31:06

Changing keywords from "" to "crystals".


---

Comment by aschilling created at 2010-01-25 06:31:06

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-01-25 21:11:29

Changing type from defect to enhancement.


---

Comment by nthiery created at 2010-01-27 01:53:07

Updated patch updates one doctest.


---

Attachment

I checked that the patch passes sage --testall, either with or without #8028.

I checked that it does not break latex method for classical crystals or metapost method for fastcrystals. I think the latex changes are specific to
affine crystals.

The patch does not seem to break anything, and fixes some problems. I recommend merging it.


---

Comment by bump created at 2010-02-02 14:45:40

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 14:35:49

I've added the ticket number in the refreshed patch I'm applying to 4.3.3.alpha0.


---

Comment by bump created at 2010-02-11 13:36:53

I'm having trouble parsing mpatel's message. Does this mean the patch is to be merged in 4.3.3.alpha0?

What "refreshed patch" does this message refer to?  The patch trac_7978_crystal_cleanup-as.2.patch
applies cleanly to sage-4.3.2 and does not break anything in sage/combinat/crystals.


---

Comment by mpatel created at 2010-02-11 13:52:07

I'll merge this ticket into 4.3.3.alpha0.  I mean only that I've prepended the ticket number to the first line of the commit string of the patch I've added to my working tree for 4.3.3.alpha0.  I apologize for being so cryptic.


---

Comment by mpatel created at 2010-02-11 14:48:23

Resolution: fixed
