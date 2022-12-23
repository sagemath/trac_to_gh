# Issue 8408: Update sqlite to 3.6.22 (the latest version)

Issue created by migration from https://trac.sagemath.org/ticket/8408

Original creator: drkirkby

Original creation time: 2010-03-01 13:33:20

Assignee: GeorgSWeber

One doctest that fails on Solaris #8400 is solved by updating the version of sqlite to the latest upstream release, which is http://www.sqlite.org/sqlite-amalgamation-3.6.22.tar.gz







---

Comment by drkirkby created at 2010-03-01 14:24:38

Actually, this solves *ALL* the doctest failures on Solaris, so assuming nobody manages to break anything, Sage 4.3.4 should work on Solaris with all doctests passing! 

The new package can be found at http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/sqlite-3.6.22/sqlite-3.6.22.spkg

Dave


---

Comment by drkirkby created at 2010-03-01 14:24:38

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-03-03 08:05:05

Do we know what changed from 3.6.19 to 3.6.22 that might have fixed the segmentation faults?


---

Comment by mpatel created at 2010-03-03 08:05:05

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 08:23:07

Resolution: fixed


---

Comment by drkirkby created at 2010-03-06 21:58:48

*Notes to the release manager*

Sorry, I should have written on the ticket, but #8397, #8398, #8399 #8400 and #8401 can all be closed now this is fixed. 

Dave
