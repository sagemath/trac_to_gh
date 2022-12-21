# Issue 4094: evaluate all causes massive browser hang

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-09-09 20:52:27

Assignee: tbd

#4078 was done wrong.  Any reference to eval_bool should be removed.  Non-async calls _must never be used_.


---

Comment by boothby created at 2008-09-09 20:53:00

Changing assignee from tbd to boothby.


---

Comment by boothby created at 2008-09-09 20:53:00

Changing component from algebra to notebook.


---

Comment by boothby created at 2008-09-09 21:09:58

Changing priority from major to blocker.


---

Attachment


---

Comment by boothby created at 2008-09-09 23:02:16

The attached does *NOT* depend on #4078.  In fact, it conflicts hugely.  If it is possible to reverse #4078, please do so.  Otherwise, I'll resolve the conflict tonight.


---

Attachment


---

Comment by mhansen created at 2008-09-10 00:25:44

This is a better fix.  Apply only trac_4094.patch which should apply fine against the current tree.


---

Comment by mabshoff created at 2008-09-10 01:11:01

Resolution: fixed


---

Comment by mabshoff created at 2008-09-10 01:11:01

Merged in Sage 3.1.2.rc2
