# Issue 6188: [with patch, needs review] Add more files in sage/rings/number_field to reference manual

Issue created by migration from https://trac.sagemath.org/ticket/6188

Original creator: davidloeffler

Original creation time: 2009-06-02 17:22:41

Assignee: was

Keywords: documentation

This patch adds the files {{{
order.py}}}, `number_field_element_quadratic.pyx`, `number_field_rel.py`, `number_field_ideal_rel.py`, and `unit_group.py` to the reference manual, and makes the necessary ReST formatting fixes to get them to build correctly.


---

Comment by davidloeffler created at 2009-06-02 17:24:23

patch against 4.0.1.alpha0


---

Comment by davidloeffler created at 2009-06-02 17:25:51

Changing status from new to assigned.


---

Attachment


---

Comment by davidloeffler created at 2009-06-02 17:25:51

Changing assignee from was to davidloeffler.


---

Comment by cremona created at 2009-06-03 21:29:12

I am half way through reviewing this and should be able to finish tomorrow.


---

Attachment

Apply after previous


---

Comment by cremona created at 2009-06-04 21:46:01

I reviewed David's patch by rebuilding the reference manual and looking through the relavant sections.  I found quite a few more things needing tidying up (several in functions I wrote, so my fault), hence the second patch nearly half as large as the first.

I'm happy to OK David's contribution, but someone else (David?) should run mine.  It's all docstring changes, but I did check that all tests in sage/rings/number_field still pass.


---

Comment by davidloeffler created at 2009-06-05 08:28:52

Looks fine to me.


---

Comment by ncalexan created at 2009-06-13 19:47:35

Resolution: fixed
