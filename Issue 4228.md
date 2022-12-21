# Issue 4228: eclib-20080310.p6.spkg is broken with 'export MAKE="make -j4"'

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-01 08:54:28

Assignee: mabshoff

Just as the title says. spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-12 23:59:57

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-12 23:59:57

The spkg fixes that issue by disabling parallel make for know. In case gmake is used it passes it to the main makefile, so the OpenBSD build still works. The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/rc0/eclib-20080310.p7.spkg

Cheers,

Michael


---

Comment by mhansen created at 2008-10-13 00:14:58

Looks good to me and builds on my box.


---

Comment by mabshoff created at 2008-10-13 00:25:21

Resolution: fixed


---

Comment by mabshoff created at 2008-10-13 00:25:21

Merged in Sage 3.1.3.rc0
