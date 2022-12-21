# Issue 2331: Polynomial_singular_repr is pretty messed up

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-27 11:04:18

Assignee: malb

** the superclass injection trick is a bad design decision
 * derivatives don't need to be handled by Singular
 * the `have_ring` option should go, because we don't need this dirty speed improvement anymore (we have libSingular)


---

Comment by malb created at 2008-09-20 15:56:04

Changing status from new to assigned.


---

Comment by malb created at 2009-01-22 20:13:08

This is an enhancement.


---

Comment by malb created at 2009-01-22 20:13:08

Changing type from defect to enhancement.


---

Comment by klee created at 2022-06-05 05:46:25

Changing status from new to needs_review.


---

Comment by klee created at 2022-06-05 05:46:25

Item (3) is handled in #33949. The objectives of the other items are not clear and perhaps not valid after 14 years.


---

Comment by vdelecroix created at 2022-06-16 20:11:11

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-08-02 06:31:03

Resolution: invalid
