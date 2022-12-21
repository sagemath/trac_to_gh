# Issue 4585: "sage -upgrade" shall call the "sage-starts" script

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2008-11-22 22:46:31

Assignee: mabshoff

On a system where "root" upgrades incrementally a system-wide Sage installation, and only "normal" users ever run Sage, there might be trouble.

More precisely, the rights to create the "sage-flags.txt" file --- or also the "sage-location.txt" file --- might not be owned by the normal user.

Even if this would be only a corner case, the obvious fix (run "sage-starts" once during sage -upgrade") does not hurt anybody, hence this ticket. 


---

Comment by GeorgSWeber created at 2008-11-22 22:50:49

Changing assignee from mabshoff to GeorgSWeber.


---

Comment by GeorgSWeber created at 2008-11-23 08:04:58

Hmmm,

it's better to call the "sage-location" script directly, because starting Sage as "root" will create certain files/directories (.sage/...) in root's home directory, which is avoidable.


---

Comment by jdemeyer created at 2013-05-19 13:19:04

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:19:04

`sage-location` is run when doing `sage --upgrade`.


---

Comment by jdemeyer created at 2013-05-19 13:19:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:23:55

Resolution: worksforme
