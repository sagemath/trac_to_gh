# Issue 2084: default 20/40 in padics factory hard coded everywhere

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-02-07 10:40:41

Assignee: was

CC:  roed

This should probably be factored out. 


---

Comment by robertwb created at 2008-02-07 10:41:58

Changing component from algebraic geometry to number theory.


---

Comment by mhansen created at 2009-06-04 21:19:47

In sage/rings/padics/factory.py, there is a twenty= and forty= at the top of the file.

It looks like we can close this ticket.  Robert, David, thoughts?


---

Comment by davidloeffler created at 2009-06-07 13:14:11

Changing assignee from was to roed.


---

Comment by davidloeffler created at 2009-06-07 13:14:11

Changing component from number theory to padics.


---

Attachment


---

Comment by mhansen created at 2010-01-17 07:43:17

I've changed the names.


---

Comment by mhansen created at 2010-01-17 07:43:17

Changing status from new to needs_review.


---

Comment by roed created at 2010-01-19 20:27:51

Changing priority from major to minor.


---

Comment by roed created at 2010-01-19 20:27:51

Looks good.  All doctests in sage.rings.padics pass, as I would expect from the fact that this patch shouldn't change any functionality.


---

Comment by roed created at 2010-01-19 20:27:51

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-24 12:45:26

Resolution: fixed
