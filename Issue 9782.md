# Issue 9782: Add additive groups to the documentation

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-08-22 23:25:14

Assignee: joyner

CC:  cremona

Add the relatively new additive group documentation from #6449 into the reference manual and verify that it builds properly.


---

Attachment


---

Comment by rbeezer created at 2010-08-23 06:39:41

Patch:

1) Adds the modules for additive abelian groups to the documentation, which builds just fine.

2) Some minor touchups and additions to the documentation.

3) I removed the note about the output format, as this seems to have been fixed.

4) I added some doctests about creating elements, since this had me very confused when I created #9695.


---

Comment by rbeezer created at 2010-08-23 06:39:41

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-23 08:51:37

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-23 08:51:37

Good job (especially the extra notes).  Applies fine to 4.5.3.alpha1, builds with no problems, and the output looks good.


---

Comment by mpatel created at 2010-08-31 03:20:18

Resolution: fixed
