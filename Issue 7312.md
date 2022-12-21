# Issue 7312: Add a function .st (meaning "such that" )which is an alias to .add_constraint

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-26 13:35:41

Assignee: jkantor

Add a function .st (meaning "such that" )which is an alias to .add_constraint. This would shorten the code, as the add_constraint option is the most used, and copy the syntax used in Pymprog


---

Comment by mhansen created at 2009-10-26 17:18:42

I'm not convinced that this is a good idea.  I think that the benefit of shorter code is outweighed by making the code more cryptic.


---

Comment by ncohen created at 2009-10-26 18:44:48

What would you think of a .such_that method then ?


---

Comment by ncohen created at 2009-10-26 18:44:48

Changing status from new to needs_info.


---

Comment by mhansen created at 2009-11-02 04:55:45

I don't see how that that is much better than add_constraint.


---

Comment by ncohen created at 2009-11-02 06:52:33

True enough....

Then this ticket should be closed as "stupid idea" :-)

Nathann


---

Comment by robertwb created at 2010-01-14 05:54:56

No need to keep the ticket open then...


---

Comment by robertwb created at 2010-01-14 05:54:56

Resolution: wontfix
