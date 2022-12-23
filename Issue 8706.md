# Issue 8706: sage-4.4.alpha0: numerical noise in chmm.pyx

Issue created by migration from https://trac.sagemath.org/ticket/8706

Original creator: was

Original creation time: 2010-04-17 19:23:13

Assignee: amhou




---

Comment by was created at 2010-04-17 19:24:52

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-04-18 13:52:46

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-18 13:52:46

Sorry this took 18 hours.  Patch looks fine, applied fine and deals with the problem on the machine which had it (32-bit ubuntu), and also works fine on a 64-bit ubuntu.


---

Comment by jhpalmieri created at 2010-04-19 05:17:40

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-19 05:17:40

Merged into 4.4.alpha1.
