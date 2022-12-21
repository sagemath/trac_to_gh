# Issue 8713: Prepare the ground for moving Parent._an_element_ to Sets().ParentMethods

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-04-18 21:23:04

Assignee: nthiery

CC:  sage-combinat

Keywords: an_element

As stated in the documentation of Parent._an_element_, this method
need not be blazingly fast since an_element is cached anyway. Also,
having it implemented in Parent, rather than in the categories makes
it impossible for categories to override this default implementation
with something more meaningful. Therefore it would be best moved to
the ParentMethods of Sets().

This first patch is a step in that direction. It just makes
_an_element_ a def method rather than a cpdef method. This little
change by itself causes the recompilation of a big part of Sage, which
makes it completely impractical to work on a patch containing it (or
in a patch queue containing it). So it would be nice to have this
patch merged in Sage 4.4, so that we can start working comfortably on
the moving of _an_element_ once it has been merged in.


---

Attachment


---

Comment by nthiery created at 2010-04-18 21:46:21

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-04-18 21:46:21

Changing type from defect to enhancement.


---

Comment by hivert created at 2010-04-19 21:05:22

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-04-19 21:05:22

According to Robert Bradshaw:
> Don't have time to review it, but sounds reasonable to me.

Moreover patch look good and all tests are ok !


---

Comment by jhpalmieri created at 2010-04-23 17:08:32

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:08:32

Merged into 4.4.alpha2.
