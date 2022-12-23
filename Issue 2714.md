# Issue 2714: [with patch, needs review] many interfaces have gp-specific code

Issue created by migration from https://trac.sagemath.org/ticket/2714

Original creator: cwitty

Original creation time: 2008-03-29 02:20:37

Assignee: was

It looks like template.py was created based on gp.py, but kept some vestiges of code that was only useful for gp.  Then, in an excellent display of cargo-cult programming, this useless code was copied to many other interfaces.

The attached patch cleans up this useless code.



---

Attachment


---

Comment by AlexGhitza created at 2008-03-29 13:25:25

Looks good.


---

Comment by mabshoff created at 2008-03-29 14:24:16

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 14:24:16

Merged in Sage 2.11.rc0
