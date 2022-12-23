# Issue 3114: blacklist  gcc version 4.0.0 on OSX

Issue created by migration from https://trac.sagemath.org/ticket/3114

Original creator: mabshoff

Original creation time: 2008-05-06 22:06:10

Assignee: mabshoff

Any gcc 4.0.0 provided by Apple is buggier than a Florida swamp. Refuse to build Sage with it at start up!

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:19:02

Changing priority from blocker to major.


---

Comment by wjp created at 2010-01-17 06:32:54

`prereq` currently checks for gcc >= 4.0.1, so this has already been taken care of.


---

Comment by wjp created at 2010-01-17 06:32:54

Resolution: fixed
