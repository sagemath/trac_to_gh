# Issue 9148: [with patch, needs review] Fix deprecated sha module usage in wiki2html.py

Issue created by migration from https://trac.sagemath.org/ticket/9148

Original creator: cschwan

Original creation time: 2010-06-05 11:02:03

Assignee: tba

The following patch replaces the deprecated sha module in sagenb/notebook/wiki2html.py to get rid of the following warning:

DeprecationWarning: the sha module is deprecated; use the hashlib module instead



---

Comment by mhansen created at 2010-09-17 01:16:52

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-09-17 01:16:52

Looks good to me.


---

Comment by mhansen created at 2010-09-17 01:16:59

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-18 07:47:05

Could someone prepend the ticket number to the first line of the patch commit string and restore the positive review?


---

Comment by mpatel created at 2010-09-18 07:47:05

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by cschwan created at 2010-09-30 10:39:12

Updated patch - contains the ticket number now.


---

Comment by mpatel created at 2010-09-30 10:49:26

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-10-03 10:11:39

Rebase to fix failed "hunk".  Apply only this patch.


---

Attachment

I've attached a rebased patch that fixes a failed "hunk."


---

Comment by mpatel created at 2010-10-04 01:34:36

Resolution: fixed
