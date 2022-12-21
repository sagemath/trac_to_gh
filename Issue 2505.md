# Issue 2505: [with patch, needs review] Sage has no Wronskian function

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-03-13 07:58:20

Assignee: mabshoff

Keywords: wronskian, calculus

The Wronskian is a basic tool in differential equations. It's used to see if a set of functions is linearly independent. The attached patch adds such a function to calculus.py.




---

Comment by ddrake created at 2008-03-13 08:06:50

Changing assignee from mabshoff to was.


---

Comment by ddrake created at 2008-03-13 08:06:50

Changing component from Cygwin to calculus.


---

Attachment


---

Comment by ddrake created at 2008-03-13 09:26:46

New version of patch; puts the function into a new calculus/functions.py file, as suggested by gfurnish on IRC. Patch is against 2.10.3.


---

Comment by mhansen created at 2008-03-15 21:28:12

Applies to 2.10.4.alpha0 and works for me.


---

Comment by mabshoff created at 2008-03-16 00:04:03

Merged in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-16 00:04:03

Resolution: fixed
