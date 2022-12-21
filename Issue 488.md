# Issue 488: python on itanium -- fix readline

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-24 07:46:07

Assignee: was

Python2.5.1 is broken on itanium.  The fix in SAGE is also broken in sage-2.8.2.  Fix this for sage-2.8.3. 
 
 1. look at old hack from sage-1.5.*
 2. get rid of #else and #ifdef stuff from around line 33
 3. keep the casting stuff around line 670??



---

Comment by mabshoff created at 2007-08-24 13:17:03

Changing component from algebraic geometry to packages.


---

Comment by was created at 2007-08-29 03:49:20

Resolution: fixed


---

Comment by was created at 2007-08-29 03:49:20

fixed in python-2.5.1.p6
