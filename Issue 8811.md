# Issue 8811: Translation for elements of a root lattice

Issue created by migration from https://trac.sagemath.org/ticket/8811

Original creator: aschilling

Original creation time: 2010-04-28 22:57:34

Assignee: sage-combinat

CC:  sage-combinat




---

Comment by nthiery created at 2010-05-21 15:11:20

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-05-21 15:11:20

Changing keywords from "" to "root systems, affine weyl groups, translations".


---

Comment by nthiery created at 2010-06-02 11:02:33

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by aschilling created at 2010-06-02 21:21:40

I carefully checked the results of translation_factor, adding extra tests to compare with Kashiwara's private notes. Nicolas and I discussed at length the correct factors for type BC (see the corresponding doc in the code).

All tests passed on massena and all tests in combinat/root_systems passed on my machine.

Positive review.


---

Comment by aschilling created at 2010-06-02 21:21:40

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 22:27:23

Resolution: fixed
