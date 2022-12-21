# Issue 3369: bool(x<0) should raise an error rather than return False

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-06-05 00:08:53

Assignee: gfurnish

CC:  cwitty jason

See, e.g. discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/bcdc671d2791056e/e086a9d59ff4b9ba


---

Comment by gfurnish created at 2008-06-05 00:11:46

This is absolutely not a bug and will break all kinds of things horribley, kill performance, require lots of try statements around trivial code, etc.  Recommend closing as "not a bug."


---

Comment by gfurnish created at 2008-06-05 00:12:37

This was also discussed on IRC with wstein (IIRC) some time ago I believe and the concensus was that raising errors was bad.


---

Comment by robertwb created at 2008-06-05 00:20:31

Hmmm... so concensus on IRC != concensus on sage-devel. Can you give an example of something that would be really bad?


---

Comment by cwitty created at 2008-06-05 00:23:17

When I said "nobody ever opened a trac ticket", I was wrong; see #2781 (which has a prototype patch to implement this).


---

Comment by robertwb created at 2008-06-05 00:34:47

Ah, OK. Then I guess we should close this.


---

Comment by mabshoff created at 2008-06-09 06:16:26

Closed as invalid upon request by Robert.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-09 06:16:26

Resolution: invalid
