# Issue 5473: create extra pickle jar for old format pickles (followup of #4640)

Issue created by migration from https://trac.sagemath.org/ticket/5473

Original creator: mabshoff

Original creation time: 2009-03-10 20:39:38

Assignee: cwitty

CC:  mkoeppe

When we currently update the pickle jar we do not keep pickles for older versions around. Due to this we could break unconverted pickles without knowing it. 

In that context it might also be nice to check that format conversion works.

Cheers,

Michael


---

Comment by chapoton created at 2021-10-20 08:22:49

Changing status from new to needs_review.


---

Comment by chapoton created at 2021-10-20 08:22:49

outdated, can we close ?


---

Comment by mkoeppe created at 2021-10-20 16:00:23

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2021-10-20 17:49:28

Resolution: invalid
