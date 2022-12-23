# Issue 2540: dsage doctest fails in 2.10.4.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/2540

Original creator: yi

Original creation time: 2008-03-16 02:17:22

Assignee: yi

People have been reporting dsage doctest failures which have been caused because the necessary "long time" flags were not set. 
Attached is a patch which fixes this. 


---

Attachment

dsage doctest fix


---

Comment by mabshoff created at 2008-03-16 02:30:36

Patch looks good to me an fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 02:31:49

Merged in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-16 02:31:49

Resolution: fixed
