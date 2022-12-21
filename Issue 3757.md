# Issue 3757: [with preliminary patch, needs review] change printing for intervals (and AA/QQbar)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-08-02 14:33:47

Assignee: somebody

This patch introduces "question-mark style printing" for intervals, where instead of [1.123 .. 1.125] we get 1.124? (the question mark means that the previous digit may be off by +/- 1).  (The slightly unfortunate thing is that [1.1238 .. 1.1242] will also print as 1.124?, so the new default printing loses a lot of information about exactly how tight the interval is.)

I'm going to post a preliminary patch first, that actually changes the printing and adds extensive docstrings and doctests for the new/changed methods.  This leaves many, many doctests broken throughout the rest of Sage.

If/when this preliminary patch is positively reviewed, I will go ahead and post a follow-on patch that fixes all the doctests.


---

Attachment

Looks good to me!  Positive review for part1.patch


---

Attachment


---

Comment by cwitty created at 2008-08-02 20:37:04

OK, I've added the rest of the patch; after applying both patches, testall passes (on 32-bit and 64-bit x86 Debian testing).


---

Comment by was created at 2008-08-03 18:24:53

REVIEW:

I just read through both patches.  Wow, these are models of how to write good quality code that is very very well documented!!

Also, I very much appreciate the added discussion of the "error digits" in the second patch.

This passes all tests for me on OS X.  Thus positive review for the whole thing.


---

Comment by mabshoff created at 2008-08-05 23:53:00

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-05 23:53:00

Resolution: fixed
