# Issue 5432: sage-combinat fixes: sage calls and qselect

Issue created by migration from https://trac.sagemath.org/ticket/5432

Original creator: nthiery

Original creation time: 2009-03-03 23:28:24

Assignee: nthiery

CC:  sage-combinat

Bug fixes:
 - Honor the SAGE_ROOT env variable to call sage
 - Removed config file handling which is now useless
 - Fixed missing default value for guards in qselect_backward_compatibility_patches



---

Attachment


---

Comment by mabshoff created at 2009-03-04 19:32:51

Mike,

can you review this?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-04 22:36:12

Well, no point of shipping 3.4 with a broken combinat script, so make this a blocker :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-04 22:36:12

Changing priority from major to blocker.


---

Comment by hivert created at 2009-03-04 23:15:37

Patch applies smootly and is working for me ! I'm giving it a +1.


---

Comment by mabshoff created at 2009-03-04 23:54:55

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-04 23:54:55

Resolution: fixed
