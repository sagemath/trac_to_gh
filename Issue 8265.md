# Issue 8265: LaTeX-friendly Unicode characters in underscored methods' docstrings

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-14 18:54:03

Assignee: was

CC:  jhpalmieri

It seems the only problem is in

   `sagenb.notebook.worksheet.Worksheet.__init__`

See #7549.  This is a follow-up to #8167.


---

Comment by mpatel created at 2010-02-14 18:57:41

Applies #8167's treatment to `Worksheet.__init__`.  sagenb repo.


---

Attachment


---

Comment by mpatel created at 2010-02-14 19:05:38

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-02-17 20:33:07

As far as I understand it, this patch is supposed to make the documentation build in pdf format with underscore methods included.  It does this successfully.


---

Comment by jhpalmieri created at 2010-02-17 20:33:07

Changing priority from minor to trivial.


---

Comment by jhpalmieri created at 2010-02-17 20:33:07

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-03-04 22:51:16

Resolution: fixed
