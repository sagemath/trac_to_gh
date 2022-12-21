# Issue 9104: _name is set too late when creating a combinatorial free module

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-31 13:07:27

Assignee: sage-combinat

Keywords: CombinatorialFreeModule name

This is a followup to #8882

In the `__init__` of `CombinatorialFreeModule`, an attribute `_name` is set if it wasn't before. However it can be used during the initialization of Parent by the coercion mechanism leading to some failure. The patch fixes the problem.

Note: right now the problem does appear but it will in the upcomming #8881


---

Attachment


---

Comment by hivert created at 2010-05-31 13:12:05

Note: This patch was forgotten during the uploading of #8882 but the problem only appeared later on.


---

Comment by hivert created at 2010-05-31 13:12:05

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-31 13:12:27

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-05-31 13:12:27

Patch is ok !


---

Comment by mhansen created at 2010-06-05 21:39:43

Resolution: fixed
