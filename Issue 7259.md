# Issue 7259: Revert Sets().category() from Sets() to Objects()

Issue created by migration from https://trac.sagemath.org/ticket/7259

Original creator: nthiery

Original creation time: 2009-10-21 08:36:14

Assignee: nthiery

CC:  sage-combinat

Keywords: categories, sets

In Sage 4.1, the category of a category was changed from Objects() to
Sets(). I.e. we used to have:

	sage: Groups().category()
	Category of objects

And now we have:

	sage: Groups().category()
	Category of sets

The former sounds more natural to me, in particular because the
objects of Sets() are exactly the parents.


---

Comment by nthiery created at 2009-10-21 08:41:43

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2009-10-21 13:20:40

For the record, all tests pass with this applied.


---

Comment by mhansen created at 2009-10-23 09:11:19

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-23 09:11:19

I think this can go in now and then we'll switch it over to the "Category of Categories" when appropriate.


---

Comment by mhansen created at 2009-10-23 09:11:54

Resolution: fixed
