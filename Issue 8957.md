# Issue 8957: Word problem broken for matrix groups

Issue created by migration from https://trac.sagemath.org/ticket/8957

Original creator: davidloeffler

Original creation time: 2010-05-12 18:17:43

Assignee: joyner

The method "word_problem" in the matrix groups class is broken in two separate ways. Firstly, it's supposed to allow you to specify a custom set of generators but it silently ignores them and uses the default ones. Secondly, it returns a Factorization object which assumes (!) that the group is commutative, and hence the results are complete junk for nonabelian groups.

I have a rough patch for this but it needs some polishing (mainly adding tests and docstrings).


---

Comment by davidloeffler created at 2010-05-15 18:52:29

patch against 4.4.1


---

Comment by davidloeffler created at 2010-05-15 18:54:27

Changing status from new to needs_review.


---

Attachment


---

Comment by wdj created at 2010-05-16 01:38:29

The code seems reasonable, the docstring looks good, applies to 4.4.2.a0 okay and passes sage -testall
(except for unrelated failures).


---

Comment by wdj created at 2010-05-16 01:38:29

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 20:11:53

Resolution: fixed
