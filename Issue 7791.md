# Issue 7791: upgrade numpy to 1.4

Issue created by migration from https://trac.sagemath.org/ticket/7791

Original creator: jason

Original creation time: 2009-12-29 19:19:41

Assignee: tbd

CC:  jkantor mpatel

Numpy 1.4 has been released.  As a matter of procedure, we probably ought to upgrade our numpy spkg.


---

Comment by mhansen created at 2009-12-30 07:25:54

Plus, we get npycore which should help with Cygwin / FreeBSD / other systems without C99 stuff.


---

Comment by dagss created at 2010-02-14 09:06:28

NumPy 1.4. is retracted and unsupported; likely better wait until 2.0 is released in some weeks.

(However, strictly speaking, the only problem with NumPy 1.4 was that of binary compatability with older versions; something Sage doesn't care about.)


---

Comment by kcrisman created at 2010-09-21 18:15:20

This should be closed as a duplicate of #9808.


---

Comment by mpatel created at 2010-09-21 20:23:58

Resolution: duplicate
