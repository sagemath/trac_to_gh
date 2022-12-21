# Issue 5481: devel/doc/output/* should be filtered from the list of files to doctest

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-03-11 06:31:10

Assignee: mabshoff

CC:  mhansen

There can be many rst files under devel/doc/output - those should be filtered from the list of files to doctest since they are duplicate doctests from the main Sage library in many cases.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-06-09 22:11:13

Has this been fixed?  The file sage-maketest looks good to me already.


---

Comment by was created at 2009-06-15 23:24:05

Changing priority from blocker to critical.


---

Comment by jhpalmieri created at 2009-06-16 03:12:22

Maybe sage-ptest needs changing.  I'm still trying to figure out what the issue is here.


---

Attachment

Here's a patch.  (The first change -- deleting all.py and __init__.py -- comes from #6108.)


---

Comment by mhansen created at 2009-06-20 01:29:00

Looks good to me.


---

Comment by mhansen created at 2009-06-20 01:29:00

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 01:29:00

Changing assignee from mabshoff to mhansen.


---

Comment by boothby created at 2009-06-26 17:43:01

Resolution: fixed
