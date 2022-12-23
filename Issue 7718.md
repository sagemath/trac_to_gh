# Issue 7718: Segfault in coercion code

Issue created by migration from https://trac.sagemath.org/ticket/7718

Original creator: roed

Original creation time: 2009-12-17 07:27:13

Assignee: robertwb

Keywords: coercion, segfault

A segfault is caused by failure to check whether elements are None.


---

Attachment


---

Comment by roed created at 2009-12-17 07:36:20

Changing status from new to needs_review.


---

Comment by robertwb created at 2009-12-17 10:14:47

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-12-17 10:14:47

Nice catch.


---

Comment by mhansen created at 2009-12-19 20:07:07

Resolution: fixed
