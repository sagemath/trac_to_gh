# Issue 2856: [with patch, needs review] PyLint unused variable cleanup for sage.rings.polynomial 2

Issue created by migration from https://trac.sagemath.org/ticket/2856

Original creator: malb

Original creation time: 2008-04-08 14:54:02

Assignee: cwitty

Keywords: pylint

the usual stuff:
 * delete unused variables
 * remove unused imports

PS: After this patch, I'll get down to fixing real bugs again rather than introducing some via unforeseen sideeffects of these clean-ups :-)


---

Attachment


---

Comment by mabshoff created at 2008-04-08 15:41:48

Patch applies cleanly and doctests fine. All changes are sane. +1 for PyLint. Positive review. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 15:44:08

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 15:44:46

Merged in Sage 3.0.alpha3 and close the ticket ;)


---

Comment by mabshoff created at 2008-04-08 15:44:46

Resolution: fixed
