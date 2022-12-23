# Issue 6170: automate applying patches from a ticket and testing them

Issue created by migration from https://trac.sagemath.org/ticket/6170

Original creator: was

Original creation time: 2009-05-31 08:12:37

Assignee: craigcitro

CC:  ncalexan

Automate the process of 

  1. take a subset of patch from a ticket

  2. merge

  3. Run "sage -br"

  4. Run "make ptest"

and much more.  


This could look like the following, though the first patch to this ticket should be much less ambitious and just do *something* useful.

```
sage: hg_devel.test(6738)

[[applying patches on trac ticket 6738 to the correct repos...]]

[[starting new sage process in os.system and doing "sage -br"]]

[[report any failures]]

[[run make ptestlong and report results]]

[[revert state of sage to exactly what it was before stuff applied]]

sage: hg_devel.apply(6738)

[[apply everything from ticket 6738 to all relevant repos -- basically hg_devel.test without running tests, and without undoing at the end;  would also place all relevant downloaded patches in a directory -- this is what Michael always did manually with the patches/ directory]]

sage: hg_devel.needs_review()

[[would query trac and make a list of all tickets that are [with patch; needs review], and would return a list of the ticket numbers.]]

sage: hg_devel.positive_review()

[[would query trac and make a list of all tickets that are [with patch; positive review], and would return a list of the ticket numbers.]]

sage: hg_devel.test_positive_review()

[[would try hg_devel.test(...) on every ticket with positive review and make a nice html (and/or text) based report summarizing what happened]]


sage: hg_devel.test_needs_review()

[[would try hg_devel.test(...) on every ticket that needs review and make a nice html (and/or text) based report summarizing what happened.   This could probably quickly indicate that half the tickets "needs review" are broken or need a rebase -- it could easily take several hours to run.  This would be incredibly valuable, imho.]]



```




---

Attachment

apply to $SAGE_LOCAL/bin


---

Attachment


---

Comment by craigcitro created at 2009-06-18 23:55:15

I've added a second patch that does a bit of error checking with the `$EDITOR` variable.


---

Comment by ncalexan created at 2009-06-19 06:27:23

First cut looks good!


---

Comment by craigcitro created at 2009-06-19 06:44:52

Merged first patch in `rc3`, second in final release.


---

Comment by craigcitro created at 2009-06-19 06:44:52

Resolution: fixed
