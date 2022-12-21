# Issue 7915: Improve TAB-completion in Macaulay2

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-01-13 04:24:27

Assignee: was

Keywords: Macaulay2, interface, TAB-completion

There are the following problems with the current TAB-completion in Macaulay2:
 * it is slow and there is a special function which creates the list of commands and stores it in file for future use;
 * this function prints a message which is not visible in the notebook and it looks like the notebook stopped responding;
 * new objects defined by user or introduced by loaded packages do not appear in this static list;
 * TAB-completion for Macaulay2 objects shows the same list of more than 1000 names as for Macaulay2 sessions, most of the stuff in this list cannot be applied to the given object.

The attached patch changes trait_names functions so that
 * functions for building command lists execute reasonably fast for interaction (0.2-0.6 second on my machine);
 * both lists for an interpreter session and for objects in it are computed dynamically on each call and take into account loaded and created names;
 * only methods which can take an object as the first argument are shown for objects;
 * execution time for "sage -t --optional macaulay2.py" dropped from 3 minutes (which was really annoying me for the last 5 days) to 30 seconds. 

New problem (doesn't need much attention, I think):
 * shortcuts like "gens" for "generators" are not displayed in both lists because of the way they are defined in Macaulay2, this is likely to be fixed in the next release (of Macaulay2).

Remaining problem (to be addressed later):
 * Macaulay2 convention is to put "the important argument" last, so a useful function "f" will not be displayed in TAB-completion for "x" if it should be called like "f(7, x)" in Macaulay2. Since the default call corresponding to Sage command "x.f(7)" is "f(x, 7)", this is actually correct and "f" should not be listed. However, it may be useful to have an option to translate all calls of the form "x.f(...)" in Sage to "f(..., x)" in Macaulay2.

Patches from #7897 are a prerequisite for this one.


---

Comment by novoselt created at 2010-01-13 04:25:09

Changing status from new to needs_review.


---

Attachment


---

Attachment


---

Comment by novoselt created at 2010-02-01 04:47:58

Changed the patch name and the commit message to contain the ticket number.


---

Comment by mhansen created at 2010-07-09 01:12:13

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-07-09 01:12:13

Looks good to me.


---

Comment by mpatel created at 2010-07-21 03:31:06

Resolution: fixed
