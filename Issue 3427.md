# Issue 3427: [with patch; needs review] remove ntl library from sage_object build dependency in setup.py

Issue created by migration from https://trac.sagemath.org/ticket/3427

Original creator: was

Original creation time: 2008-06-14 22:15:34

Assignee: mabshoff

I can think of no good reason that the ntl library is linked into sage_object.pyx!  It absolutely shouldn't be needed.   Not having it there is needed for making sagelite. 


---

Attachment

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-15 19:15:54

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 19:15:54

Resolution: fixed
