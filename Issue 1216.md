# Issue 1216: cremona.homspace extension fails to compile on osx 10.4

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 15:37:07

Assignee: mabshoff

I have got a simple patch that fixes the issue. It will be added to this ticket shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 15:37:13

Changing status from new to assigned.


---

Attachment

The patch as is causes some problem on Linux, but I think it should work everywhere by linking pari instead if pari-gmp.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 23:24:58

Resolution: fixed


---

Comment by mabshoff created at 2007-11-20 23:24:58

Merged in 2.8.13.rc1.
