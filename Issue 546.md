# Issue 546: hg_extcode should merge repository on upgrade/install instead of overwriting

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-31 23:10:47

Assignee: was




---

Comment by was created at 2007-10-05 03:15:19

Changing priority from major to critical.


---

Comment by was created at 2007-11-03 20:51:06

Resolution: fixed


---

Comment by was created at 2007-11-03 20:51:06

This is now fixed and pushed out (get it with hg_extcode.pull()).

NOTE: This will probably open up a whole new can of worms with people trying
up upgrade and having a messed up extcode repo, but that's another story.
