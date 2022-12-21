# Issue 3774: __radd__ doesn't work when left hand side is an Element

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-08-05 08:24:46

Assignee: robertwb

CC:  alexghitza


```
On Aug 1, 2008, at 7:05 AM, Nils Skoruppa wrote:


It seems that,  for non elements,  __radd__ is set disfunctional
by the coercion model. On the other hand, it might be desirable
to have this enabled for people writing their own classes but having
reasons to avoid (parts of)  the coercion system (like me :-)


```



---

Attachment


---

Comment by robertwb created at 2008-08-11 16:33:01

Might depend on #3738.


---

Comment by mhansen created at 2008-08-25 00:02:30

This could use a doctest.  robertwb, do you want to write one, if not, I can probably do it a bit later.


---

Comment by robertwb created at 2008-08-25 16:58:41

Please go ahead and write one, though implementing `__radd__` should not be encouraged.


---

Attachment


---

Comment by mhansen created at 2008-09-24 02:11:26

Okay, the new patch should apply.  Positive review.


---

Comment by mabshoff created at 2008-09-24 04:23:27

Merged trac_3774.patch in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-24 04:23:27

Resolution: fixed
