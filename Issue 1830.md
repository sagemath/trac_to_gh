# Issue 1830: sage-current-location.txt not unpdated on "make install"

Issue created by migration from Trac.

Original creator: pgrinber

Original creation time: 2008-01-18 13:42:02

Assignee: cwitty

when running "DESTDIR=/usr/lib make install", the file /usr/lib/sage/local/lib/sage-current-location.txt should be updated with the correct new path of $DESTDIR/sage



---

Comment by was created at 2008-01-18 16:39:15

I disagree.  /usr/lib/sage/local/lib/sage-current-location.txt should *only* be updated if Sage is actually run in the new location.   And if "make install" hasn't run the Sage in the new location, then you better not update that file (or Sage will be installed in a totally broken state).  

Maybe what I'm saying is that "make install" should run the Sage in the install location once in order to update sage-current-location.txt.


---

Comment by mabshoff created at 2008-09-15 04:49:47

This seems closely related to #3122. The fix that William suggests should be implemented since otherwise people will complain about this issue again in the future.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 10:20:40

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-12-01 08:31:38

Resolution: fixed


---

Comment by mabshoff created at 2008-12-01 08:31:38

This is fixed via #3122.

Cheers,

Michael
