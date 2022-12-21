# Issue 6190: Fix documentation in sage/combinat/backtrack.py

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-06-02 20:04:48

Assignee: rbeezer

CC:  davidloeffler

Four doctests introduced in #6000 need proper indentations, plus some lists, and some spelling.


---

Attachment

Here's a patch.


---

Comment by rbeezer created at 2009-06-03 00:13:35

Hi David,

Thanks for the changes.  I'd intended to do them, since I understand ReST better now than I did a few weeks ago, but you've done a nice job with it.

Passes doctests on this one file, which it should since all of the changes are to documentation (not code, or tests).  HTML version builds without errors and looks very nice.

Positive review.

Rob


---

Comment by mhansen created at 2009-06-03 20:25:30

Resolution: fixed


---

Comment by mhansen created at 2009-06-03 20:25:30

Merged in 4.0.1.rc0.
