# Issue 8343: email address marked as confirmed even after changing it

Issue created by migration from https://trac.sagemath.org/ticket/8343

Original creator: ddrake

Original creation time: 2010-02-24 03:38:29

Assignee: was

CC:  jason chapoton

While working on #7630, I discovered that even if a user has confirmed an email address, if the user changes it on the Account Settings page, the new address is marked as "confirmed" even though no re-confirmation email is sent out.

I don't know if we want to re-send confirmation emails every time a user changes their email address, but at least we should mark the address as unconfirmed.


---

Comment by kcrisman created at 2014-12-10 21:42:45

https://github.com/sagemath/sagenb/issues/302


---

Comment by kcrisman created at 2014-12-10 21:42:45

Changing priority from major to minor.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-08 18:00:19

Resolution: invalid
