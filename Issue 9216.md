# Issue 9216: Bring doc coverage of groups/group.pyx to 100%

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-06-11 11:47:38

Assignee: slabbe

CC:  sage-combinat




---

Attachment


---

Comment by slabbe created at 2010-06-11 11:53:47

Changing status from new to needs_review.


---

Comment by saliola created at 2010-06-11 14:13:35

Changing status from needs_review to positive_review.


---

Comment by saliola created at 2010-06-11 14:13:35

ok.

reviewed against 4.4.3.


---

Comment by rlm created at 2010-07-06 09:39:49

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-07-06 09:39:49

Perhaps you should have an example of `__contains__` working, not just failing. Should just return true or false, right?

-- RLM, and the audience at SD 23.


---

Comment by was created at 2010-07-06 09:41:28

Changing status from needs_work to positive_review.


---

Comment by was created at 2010-07-06 09:41:28

Oops -- WJP just pointed out that I was wrong.


---

Comment by mpatel created at 2010-07-21 09:55:54

Resolution: fixed
