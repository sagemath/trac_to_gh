# Issue 3665: add initial species code

Issue created by migration from https://trac.sagemath.org/ticket/3665

Original creator: mhansen

Original creation time: 2008-07-16 00:44:45

Assignee: mhansen

CC:  sage-combinat




---

Attachment


---

Comment by rlm created at 2008-10-07 23:52:12

The patch here depends on #4139.


---

Comment by rlm created at 2008-10-07 23:54:41

Applies, builds, passes `sage -t -long sage/combinat`, and coverage is perfect, except for:

series.py: 96% (55 of 57)

I say it's good to merge, if we can test those last two functions.


---

Comment by mabshoff created at 2008-10-08 08:43:55

Resolution: fixed


---

Comment by mabshoff created at 2008-10-08 08:43:55

Merged in Sage 3.1.3.alpha3


---

Attachment
