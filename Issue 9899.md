# Issue 9899: better conjugation for special functions

Issue created by migration from https://trac.sagemath.org/ticket/9900

Original creator: burcin

Original creation time: 2010-09-12 09:52:40

Assignee: burcin

Keywords: pynac

Add doctests to test enhancements to conjugates of some special functions in pynac/GiNaC.


---

Attachment


---

Comment by burcin created at 2010-09-12 12:28:07

attachment:trac_9900_conjugate_doctests.patch adds doctests to reflect the changes in the new pynac version at #9901.

The pynac package includes patches for #9394, #9834, #9878, #9879, #9881 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.


---

Comment by burcin created at 2010-09-12 12:28:07

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-29 18:55:39

This patch depends on knowing the branch cuts we wish to use.  A followup ticket for giving references for these choices (and/or for making sure they're the same as used for our numerical approximations of these!) is at #10033.


---

Comment by kcrisman created at 2010-09-29 19:05:43

This comes from upstream in Ginac.  According to Burcin:

 just imported Richard Kreckel's [patch from upstream](http://www.ginac.de/ginac.git?p=ginac.git;a=commit;h=ff8b400eb500618644231ed9e6f199c3b0b25135).


---

Comment by kcrisman created at 2010-10-05 00:53:55

Other than one spot where `arccos` should be `arccosh` in the new doctests, this is fine.  However, it seems good to add some more doctests, especially for the branch cuts to make sure they stay unsimplified.   A patch for this should be done by tomorrow sometime.


---

Attachment

Rebase of original patch with respect to reviewer patches of #9879 and #9881


---

Comment by kcrisman created at 2010-10-05 13:01:08

Okay, reviewer patch is ready and coming right up.   Positive review.

To release manager: please merge first rebase patch, then reviewer patch.


---

Comment by kcrisman created at 2010-10-05 13:01:08

Changing status from needs_review to positive_review.


---

Attachment

Reviewer patch, apply after rebase patch


---

Comment by mpatel created at 2010-10-06 03:20:24

Resolution: fixed
