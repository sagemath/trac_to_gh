# Issue 5222: wrap FLINTs pseudo-division algorithm for univariate polynoials over ZZ

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-09 19:05:18

Assignee: somebody

Flint has a super-fast pseudo-division algorithm over ZZ, but Sage doesn't yet wrap it.  The point of this ticket is to wrap it.  


---

Attachment


---

Comment by burcin created at 2009-02-09 20:29:13

Patch looks good, tests pass.


---

Comment by mabshoff created at 2009-02-10 07:17:31

Resolution: fixed


---

Comment by mabshoff created at 2009-02-10 07:17:31

Merged in Sage 3.3.rc0.

Cheers,

Michael
