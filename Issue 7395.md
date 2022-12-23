# Issue 7395: The enumerated set of non negative integers !

Issue created by migration from https://trac.sagemath.org/ticket/7395

Original creator: hivert

Original creation time: 2009-11-05 15:28:35

Assignee: hivert

CC:  sage-combinat

Keywords: Non negative integers

The following patch implement the set of non-negative integers in the category `EnumeratedSets()`. This is needed when making the unions of a family of enumerated sets such has `Permutations()` being defined as the union of `Permutations(n)` for all `n`. 

Depends on the category framework #5891.

Florent 


---

Comment by hivert created at 2009-11-05 15:34:27

Changing status from new to needs_review.


---

Attachment


---

Attachment

The updated patch fixes 3 typos which have been cross-reviewed by Florent


---

Comment by nthiery created at 2009-11-05 16:17:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-19 16:58:17

Resolution: fixed
