# Issue 8875: Problem with Set created from iterator.

Issue created by migration from https://trac.sagemath.org/ticket/8875

Original creator: mrobado

Original creation time: 2010-05-04 20:43:08

Assignee: sage-combinat

A Set_object gets created instead of an Set_object_enumerated.


---

Attachment


---

Comment by mrobado created at 2010-05-04 20:52:52

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2010-05-04 21:53:07

I posted a new patch to add a test to make sure that this has been (and stays) fixed.  Marco, can you take a look, make sure it's okay, and then mark this ticket as having a positive review?


---

Comment by mrobado created at 2010-05-06 13:32:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:43:31

Merged [trac_8875_Set_from_iterator_mr.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8875/trac_8875_Set_from_iterator_mr.2.patch).


---

Comment by mvngu created at 2010-05-08 21:43:31

Resolution: fixed
