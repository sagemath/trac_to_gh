# Issue 7974: hg_sage.diff() silently appends

Issue created by migration from https://trac.sagemath.org/ticket/7974

Original creator: gaer

Original creation time: 2010-01-18 09:07:55

Assignee: was

`hg_sage.diff()` silently appends to a preceding patch file of the same name rather than overwriting or warning of appending/overwriting.  This is due to the -o option used in implementing the command.


---

Comment by mmezzarobba created at 2014-02-02 11:06:23

No more relevant?


---

Comment by mmezzarobba created at 2014-02-02 11:06:23

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-02-06 21:37:29

Changing status from needs_review to positive_review.


---

Comment by aapitzsch created at 2014-02-06 21:37:29

Yes, no longer relevant.


---

Comment by vbraun created at 2014-02-07 21:31:30

Resolution: wontfix
