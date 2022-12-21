# Issue 7198: Free Algebra Iteration, needs review

Issue created by migration from Trac.

Original creator: PolyBoRi

Original creation time: 2009-10-13 10:20:32

Assignee: tbd

CC:  burcin saliola malb

Keywords: free algebra

Iteration over free algebra elements and monoid elements


---

Attachment


---

Attachment

new version free_algebra.2.patch
redesigns the iterator based on Burcins review.


---

Comment by PolyBoRi created at 2009-10-16 14:01:17

Changing status from new to needs_review.


---

Attachment


---

Comment by burcin created at 2009-10-16 20:42:11

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2009-10-16 20:42:11

Changing type from defect to enhancement.


---

Comment by burcin created at 2009-10-16 20:42:11

I uploaded a new patch with minor formatting changes, attachment:trac_7198-free_algebra_iterator.patch.

Mike, please apply only attachment:trac_7198-free_algebra_iterator.patch.


---

Comment by mhansen created at 2009-10-19 05:52:17

Resolution: fixed


---

Comment by mhansen created at 2009-10-19 13:00:38

I backed this out of sage-4.2.alpha1.

This caused problems since there were other free monoid elements that expected to have an __iter__ which returned something different than what was chosen for this patch.  For example, things in the StringMonoid and free monoid elements in sage/crypto.


---

Comment by mhansen created at 2009-10-19 13:00:38

Changing status from closed to needs_work.


---

Comment by burcin created at 2009-12-29 21:35:43

fix doctests, add `__iterator__` method to StringMonoidElement


---

Comment by burcin created at 2009-12-29 21:44:43

Changing status from needs_work to needs_review.


---

Attachment

I added a new patch which restores the expected iterator interface of `StringMonoidElement`s.

Martin, can you review my changes?

Both
 * attachment:trac_7198-free_algebra_iterator.patch and
 * attachment:trac_7198-string_monoid_element_iterator.patch
should be applied.


---

Comment by mhansen created at 2010-01-19 01:40:10

Changing status from needs_review to positive_review.
