# Issue 7774: notebook: after performing "evaluate all" behauviour of  creating new cells changes.

Issue created by migration from https://trac.sagemath.org/ticket/7774

Original creator: ggrafendorfer

Original creation time: 2009-12-27 16:10:19

Assignee: was

sage 4.3, 32-bit Athlon XP, OS: Debian "lenny", this issue appears in a local notebook as well as on www.sagenb.org using firefox 3.0.6 and epiphany

When working in the notebook, usually after evaluating the last cell, the result is printed out and the cursor is placed in a newly created empty cell.

This behaviour changes if "evaluate all" is performed on the worksheet:

Create a new worksheet, type "1+1" into the first cell and evaluate it, then go to the menu "action" and perform "evaluate all", then go to the last empty cell again, type something like "1+2" and evaluate the cell (by pressing Shift-Return), the result is printed out, but instead of creating a new empty cell and placing the cursor there, no new cell will be created, the cursor is placed in the beginning of the last evaluated cell.



---

Comment by robert.marik created at 2009-12-27 17:37:32

I confirm this bug (K-meleon and WVista, server is 32-bit Debian lenny).
However, when I "save and quit" the notebook a return back, the missing new cell is at the and.


---

Comment by mpatel created at 2010-01-02 00:59:59

This should be fixed by #7666 + #6855.


---

Comment by kcrisman created at 2014-12-10 20:28:51

If someone sees this again, let's open a new ticket with more updated info; I cannot replicate this.


---

Comment by kcrisman created at 2014-12-10 20:28:51

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-12-10 20:29:03

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-11 18:35:00

Resolution: worksforme
