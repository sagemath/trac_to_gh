# Issue 8493: Complex conjugation in Galois groups

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-03-10 21:20:09

Assignee: davidloeffler

CC:  cremona

Keywords: Galois groups

The attached patch contains some simple code which will return the element of the Galois group of a number field corresponding to complex conjugation (at a specified complex place, or the "default" complex embedding where that exists).

The code also uses embeddings into QQbar, so I've moved QQbar over to the new coercion model (a simple case of renaming the ``__call__`` method to ``_element_constructor_``).


---

Attachment


---

Comment by davidloeffler created at 2010-03-10 23:29:47

Changing status from new to needs_review.


---

Comment by cremona created at 2010-03-13 14:38:53

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-03-13 14:38:53

Looks good, applies fine to 4.3.4.alpha1, and all tests pass.


---

Comment by jhpalmieri created at 2010-04-17 04:11:57

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-17 04:11:57

This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0 -- I don't think this will be too hard -- and we'll try hard to get this into 4.4.alpha1.


---

Attachment

now rebased against 4.4.alpha0


---

Comment by davidloeffler created at 2010-04-17 09:55:40

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-04-17 10:19:07

The new patch is actually functionally identical to the old one -- it's only one of the "context" marker lines that has changed, due to another patch changing import statements in `galois_group.py` -- so I'm taking the liberty of setting it straight back to "positive_review".

David


---

Comment by davidloeffler created at 2010-04-17 10:19:07

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-17 11:33:10

I am happy with this (as original reviewer).  I looked at the new patch, but have not tested it as I am still building 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-17 18:41:17

Replying to [comment:5 davidloeffler]:
> I'm taking the liberty of setting it straight back to "positive_review".

I think that's fine.  It applies cleanly to 4.4.alpha0; I'm checking doctests and will report if there are any problems.  Otherwise, it will get merged into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:13:40

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-19 05:13:40

Merged "trac_8493-complex_conjugation.2.patch" into 4.4.alpha1
