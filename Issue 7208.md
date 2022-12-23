# Issue 7208: Refactorisation of families

Issue created by migration from https://trac.sagemath.org/ticket/7208

Original creator: nthiery

Original creation time: 2009-10-14 12:44:35

Assignee: nthiery

CC:  sage-combinat

Keywords: Family, enumerated set

Log of the attached patch:

- Families are parents, in the (Finite/Infinite)EnumeratedSets category
- New class EnumeratedFamily; Family accept any (Finite)EnumeratedSet as input
- Improves the output of lazy families, and update accordingly the
  doctests in CombinatorialFreeModule, ...
- Clean trailing whitespaces
- Use TestSuite


---

Comment by nthiery created at 2009-10-14 12:46:15

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-10-14 12:46:24

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2009-10-16 14:38:38

We should use the occasion to fix this bug:

	sage: f = Family(["c", "a", "b"], lambda x: x+x)
	sage: list(f)
	['aa', 'cc', 'bb']


---

Comment by nthiery created at 2009-10-16 14:38:38

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2009-10-16 14:53:48

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-10-16 14:53:48

The updated patch is supposed to fix it. Florent: please review!


---

Attachment


---

Comment by nthiery created at 2009-10-16 15:01:21

Fixed missing doctests


---

Comment by hivert created at 2009-10-16 15:03:40

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-10-16 15:03:40

Things are *now* ok :-) Positive review.

Florent


---

Comment by mhansen created at 2009-11-19 16:57:44

Resolution: fixed
