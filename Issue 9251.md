# Issue 9251: Lazy attribute does not properly handles the doc of Cython methods

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-06-16 23:29:05

Assignee: jason

CC:  nthiery

Keywords: Lazy Attributes

A request `Parent.element_class?` gives the doc of the class `lazy_attribute` instead of the doc of the function itself.


---

Comment by hivert created at 2010-06-16 23:39:45

Changing status from new to needs_review.


---

Attachment


---

Attachment


---

Comment by hivert created at 2010-06-16 23:42:56

Changing assignee from jason to hivert.


---

Comment by robertwb created at 2010-06-22 20:52:52

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 07:54:16

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 07:54:16

Merged attachment:trac_9251-lazy_attribute_cython-fh.2.patch in 4.5.2.alpha1.
