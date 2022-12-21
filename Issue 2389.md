# Issue 2389: linbox charpoly crashes on OS X 10.5-intel

Issue created by migration from Trac.

Original creator: cpernet

Original creation time: 2008-03-04 22:07:30

Assignee: cpernet

The proposed linbox-1.1.5rc1.p0 crashes on OS X 10.5-intel for charpoly computations. The bug shows up at initialization of static variables, and may be related to the specific OS X gcc compiler behaviour.

http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html, may help. 

Same issue as #2388, but need a clean fix.


---

Comment by cpernet created at 2008-03-04 22:10:04

Changing component from Cygwin to packages.


---

Comment by mabshoff created at 2008-03-15 05:45:48

This ticket has been superseded by #2525 and ought to be closed once that ticket has been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 05:45:48

Changing assignee from cpernet to mabshoff.


---

Comment by mabshoff created at 2008-03-15 05:45:48

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-05 18:47:39

Resolution: fixed
