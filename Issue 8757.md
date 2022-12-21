# Issue 8757: Use SQLAlchemy for storage in SageNB

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-04-24 22:42:58

Assignee: jason, was

Using a database engine will be much faster, hopefully lessening the speed issues we have.


---

Comment by timdumol created at 2010-04-24 22:44:17

Preliminary work. Schema in sagenb.notebook.models.models.


---

Attachment


---

Comment by kcrisman created at 2015-01-06 14:32:14

See also #15593.


---

Comment by kcrisman created at 2015-01-06 14:41:12

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2015-01-06 14:41:12

This is a noble goal, but currently very unlikely.


---

Comment by kcrisman created at 2015-01-06 14:56:57

See also #4268.


---

Comment by kcrisman created at 2015-01-06 14:59:46

In fact, this is (essentially) #3456 which I closed before.


---

Comment by kcrisman created at 2015-01-06 14:59:46

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-01-06 14:59:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-13 01:22:41

Resolution: fixed
