# Issue 139: automatic dependency checking for pyrex files

Issue created by migration from https://trac.sagemath.org/ticket/139

Original creator: was

Original creation time: 2006-10-20 01:08:54

Assignee: was

Add code to devel/sage/setup.py so that a Pyrex file is pyrexed if it
changes *or* if any pxd file that it cimports changes.


---

Comment by dmharvey created at 2006-10-20 01:20:30

It would also be good to check any .pxi files that are included. Maybe even any .h files that are referenced, because the C file compilation will depend on this too.


---

Comment by was created at 2006-10-21 01:26:06

I've made a change so when you do a "sage -upgrade" all .pyx files get rebuilt.  This is obviously slower, but will avoid a lot of stupid confusion for now.


---

Comment by was created at 2006-10-26 04:36:09

* Checking for dependencies on .h files doesn't work at all.

* Recursive dependencies don't work, i.e., if a depends on b and b on c, and
c changes, then a isn't rebuilt.


---

Comment by malb created at 2008-02-26 23:57:22

Is this still a valid ticket? We do check dependencies now, right?


---

Comment by was created at 2008-02-27 12:21:18

Resolution: fixed


---

Comment by was created at 2008-02-27 12:21:18

I implemented this and forgot to close the ticket.
