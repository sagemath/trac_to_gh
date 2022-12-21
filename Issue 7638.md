# Issue 7638: [with patch, needs review] Cannot create big matrix on 64-bit system

Issue created by migration from Trac.

Original creator: dagss

Original creation time: 2009-12-09 14:02:41

Assignee: was

_64-bit only_

Due to unfortunate parenthesis, it is possible to create 2^31 by 10-matrices, but not 10 by 2^31. See patch


---

Attachment


---

Comment by dagss created at 2009-12-09 14:06:34

Changing status from new to needs_review.


---

Comment by was created at 2009-12-09 14:38:37

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 14:38:37

Thanks for finding this.  Positive review. 

I had to rebase the patch for sage-4.3.alpha1; rebased patch attached.


---

Attachment


---

Comment by mhansen created at 2009-12-10 14:24:23

Resolution: fixed
