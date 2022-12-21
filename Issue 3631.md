# Issue 3631: pbuild broken by binary *.pyc files in extcode

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-07-10 08:57:57

Assignee: gfurnish

The pbuild install in 3.0.4 was broken by (among other things) *.pyc files left in data/extcode/sagebuild.  All pyc files here should automatically get nuked when the spkg is created. 


---

Comment by gfurnish created at 2008-07-14 10:49:03

Changing assignee from gfurnish to mabshoff.


---

Comment by jdemeyer created at 2012-03-12 21:30:02

This is no longer relevant in sage-5.0, since any file which doesn't belong in the repository will be detected by `hg status`.


---

Comment by jdemeyer created at 2012-03-12 21:30:02

Resolution: invalid
