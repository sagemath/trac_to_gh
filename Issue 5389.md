# Issue 5389: Creating a  updated workspace with -tp is racy

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-26 23:33:09

Assignee: mabshoff

See a comment on #5366. When one does doctest Sage with -tp and GAP has been updated, but Sage not started the creation of the workspace is racy since many processes will try to update it at the same time.

Starting up Sage once at the start of -tp via "sage -c" ought to fix the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-26 23:33:22

Changing status from new to assigned.


---

Comment by wjp created at 2011-01-11 01:11:23

I believe that since `sage-starts` is now executed at the beginning of parallel testing, this has already been fixed.


---

Comment by jdemeyer created at 2011-01-11 06:14:46

Replying to [comment:2 wjp]:
> I believe that since `sage-starts` is now executed at the beginning of parallel testing, this has already been fixed.

I agree.


---

Comment by jdemeyer created at 2011-01-11 06:14:46

Resolution: worksforme
