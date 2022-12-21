# Issue 7455: SageNB - Searching on Log page does not work.

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-11-13 20:28:26

Assignee: AlexGhitza

Searching for anything on the Log page does not work due to missing javascript libraries.


---

Comment by AlexGhitza created at 2009-11-13 22:20:30

Changing component from algebra to notebook.


---

Comment by AlexGhitza created at 2009-11-13 22:20:30

Changing assignee from AlexGhitza to boothby.


---

Attachment

This remvoes the search bar from the history page and updates the tests to reflect that.


---

Comment by timdumol created at 2009-11-13 23:34:47

The problem is apparently a bit harder to fix. It requires a few changes to the js libraries. For now, this patch is a temporary fix.


---

Comment by timdumol created at 2009-11-15 02:58:53

I have thought over this, and it seems to me that it makes more sense to keep the search box only in the worksheet list pages (Home and Published). If there are no objections, then the previous patch removing the search box should be the one included.


---

Comment by timdumol created at 2009-11-15 02:58:53

Changing status from new to needs_review.


---

Comment by was created at 2009-12-08 21:04:49

I agree with this patch.  It would of course be better to just get rid of the whole top bar, and make all the cells be properly styled, etc.   But this current patch is very simple at and at least fixes this bug.  Positive review.


---

Comment by was created at 2009-12-08 21:04:49

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 06:32:16

merged in sagenb-0.4.6


---

Comment by was created at 2009-12-09 06:32:16

Resolution: fixed
