# Issue 8028: Improvements to element_wrapper

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-01-21 17:08:34

Assignee: sage-combinat

Keywords: ElementWrapper, partial order

Improvements to element_wrapper:

 - Don't define __cmp__ by default to not force a total order on subclasses
 - Define __lt__ to have elements incomparable by default
 - Provide alternative implementations as _cmp_by_value, _lt_by_value
 - Update accordingly:
   - FiniteSemigroups().example
 - Misc polishing (copyright header, whitespace, ...)

This will be used by upcoming patches for crystals, ...


---

Attachment


---

Comment by nthiery created at 2010-01-21 17:14:57

Changing status from new to needs_review.


---

Comment by hivert created at 2010-01-23 11:16:07

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-01-23 11:16:07

Everything ok !


---

Comment by mvngu created at 2010-01-23 14:00:52

Resolution: fixed
