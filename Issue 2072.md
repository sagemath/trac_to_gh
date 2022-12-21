# Issue 2072: Remove _neg_c_impl and _invert_c_impl from some classes.

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-02-06 07:20:25

Assignee: somebody

Unary arithmetic operations don't benefit from the coercion model, `__neg__` and `__invert__` should be used instead. 


---

Comment by mmezzarobba created at 2015-04-13 15:35:53

New commits:


---

Comment by mmezzarobba created at 2015-04-13 15:35:53

Changing priority from major to minor.


---

Comment by mmezzarobba created at 2015-04-13 15:35:53

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-04-21 12:14:24

Use `~foo` instead of `foo.__invert__()`.


---

Comment by jdemeyer created at 2015-04-21 12:14:24

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-04-22 12:03:35

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2015-04-22 12:13:42

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2015-04-22 13:03:26

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-23 03:21:52

Resolution: fixed
