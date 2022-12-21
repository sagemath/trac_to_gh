# Issue 1695: on osx 10.4 missing libintl.3.dylib in 2.9.2 dmg

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2008-01-05 23:21:03

Assignee: boothby

The sage-2.9.2 in the osx 10.4 dmg failed to work because of missing libintl.
This failure occurred when starting the notebook.
Putting  http://sagemath.org/SAGEbin/apple_osx/intel/10.4-extra_files/libintl.3.dylib
in local/lib fixed it





---

Comment by boothby created at 2008-03-16 19:07:31

Changing component from notebook to distribution.


---

Comment by boothby created at 2008-03-16 19:07:31

Changing assignee from boothby to mabshoff.


---

Comment by was created at 2008-03-16 20:33:51

Closed because I don't build sage on the machine that led to this problem anymore.  In fact that machine physically no longer exists.


---

Comment by was created at 2008-03-16 20:33:51

Resolution: invalid
