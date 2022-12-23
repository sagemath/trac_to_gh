# Issue 3413: [with patch; needs review] sage-3.0.3.alpha2 -- endianess issue with time_series doctest

Issue created by migration from https://trac.sagemath.org/ticket/3413

Original creator: was

Original creation time: 2008-06-13 14:21:32

Assignee: was

Two of the doctests for time_series.pyx have endianess issues on osxppc.  I fixed them.


---

Attachment

We need a review for this patch.

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-15 20:33:30

William is going to add one more tiny (literally 5 character) patch, and this will be ready to go.


---

Comment by was created at 2008-06-15 22:38:28

adds ",2"; and works.


---

Attachment

Looks good. It's ready to go.


---

Comment by mabshoff created at 2008-06-16 04:56:15

Resolution: fixed


---

Comment by mabshoff created at 2008-06-16 04:56:15

Merged in Sage 3.0.3.rc0
