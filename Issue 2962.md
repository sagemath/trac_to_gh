# Issue 2962: modify .name() method for ExpectElements to allow renaming

Issue created by migration from https://trac.sagemath.org/ticket/2962

Original creator: mhansen

Original creation time: 2008-04-20 01:34:20

Assignee: was




---

Attachment


---

Comment by mhansen created at 2008-04-20 01:36:00

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-04-20 01:36:00

Changing status from new to assigned.


---

Comment by broune created at 2008-05-12 11:23:23

Is there a reason that get-name and clone-and-change-name should be combined into the same method? I would prefer a clone method or some such with an optional name parameter, unless this is a Python idiom that I'm just unaware of.


---

Comment by mabshoff created at 2008-06-23 06:19:27

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 06:19:27

Merged in Sage 3.0.4.alpha0
