# Issue 472: Drop dependencies on flex and bison

Issue created by migration from Trac.

Original creator: jmbr

Original creation time: 2007-08-20 23:13:13

Assignee: jmbr

To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.



---

Comment by jmbr created at 2007-08-23 00:04:55

Replying to [ticket:472 jmbr]:
> To build Singular we need flex and bison but we could make sure those programs are not needed by using some spkg-install trickery.

Make will invoke flex and bison if the *.[ly] files are newer than the C++ files they generate.  Thus, we have to make sure the C++ files are fresher.


---

Comment by jmbr created at 2007-08-23 00:04:55

Resolution: worksforme


---

Comment by was created at 2007-08-29 03:43:24

This is not closed, since there isn't a singular spkg yet that implements it.


---

Comment by was created at 2007-08-29 03:43:24

Resolution changed from worksforme to 


---

Comment by was created at 2007-08-29 03:43:24

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-08-29 21:08:25

If malb's new singular.spkg goes in this is resolved.

Cheers,

Michael


---

Comment by was created at 2007-08-29 21:13:57

Resolution: fixed
