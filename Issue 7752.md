# Issue 7752: RAM is not free after deleting a worksheet

Issue created by migration from https://trac.sagemath.org/ticket/7752

Original creator: pang

Original creation time: 2009-12-23 14:16:30

Assignee: was

CC:  was acleone mpatel

Total RAM use does not decrease after deleting a worksheet. In the Trash section, it appears as (running).

I suggest the page is stopped, then deleted, as usually someone deleting a worksheet does not plan on working on it further.

When I have to correct a lot of worksheets from the students, I upload one, correct it, save it, and delete it, but RAM eventually gets collapsed.


---

Attachment

Quits a worksheet only if the only user viewing the worksheet is the person trashing it.


---

Comment by timdumol created at 2010-01-19 10:43:00

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-19 10:43:00

This should do the trick. It only quits a worksheet if the only user viewing it is the person trashing it, as it may otherwise ruin other people's sessions.


---

Comment by acleone created at 2010-01-19 12:53:17

LGTM.


---

Comment by acleone created at 2010-01-19 12:53:17

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 01:01:58

Resolution: fixed
