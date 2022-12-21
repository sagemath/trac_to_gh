# Issue 9851: Error in edge_cut

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-09-03 18:24:28

Assignee: jason, ncohen, rlm

This method contains an error, as reported in 
http://groups.google.com/group/sage-support/browse_thread/thread/f747663b0b315105/5c1314c9855e0cfb?show_docid=5c1314c9855e0cfb&pli=1

This (very) short patch fixes it. I do not even understand why it was not like that fromt he beginning. I'm guessing a copy/paste is responsible `:-D`

To be applied on top of #9350 which is an important update and may be broken if this patch was to be applied first.


---

Comment by ncohen created at 2010-09-03 18:26:49

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-09-03 18:26:49

Changing priority from major to critical.


---

Comment by dimpase created at 2010-09-04 03:57:46

Changing status from needs_review to positive_review.


---

Attachment

looks reasonable.


---

Comment by mpatel created at 2010-09-15 22:52:22

Resolution: fixed
