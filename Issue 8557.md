# Issue 8557: is_singular method for projective plane curves

Issue created by migration from https://trac.sagemath.org/ticket/8557

Original creator: cturner

Original creation time: 2010-03-18 15:09:13

Assignee: AlexGhitza

CC:  cremona

It would be useful to have a way of checking whether a projective curve has any singular points. 
A patch to do this is on its way.


---

Comment by cturner created at 2010-03-20 10:17:26

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2010-04-03 06:01:18

Looks good.

We should (more generally) wrap Singular's slocus function which computes the singular locus of an ideal in a multivariate polynomial ring, but that should be a new ticket.


---

Comment by AlexGhitza created at 2010-04-03 06:01:18

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-17 04:11:28

This doesn't apply cleanly; it apparently conflicts with a patch merged into Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0, and we'll try hard to get this into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-17 04:11:28

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-18 05:30:35

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-04-18 05:30:35

Never mind, I've taken care of it.


---

Comment by jhpalmieri created at 2010-04-18 05:30:41

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by jhpalmieri created at 2010-04-19 05:19:29

Merged "trac_8557_rebased.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:19:29

Resolution: fixed
