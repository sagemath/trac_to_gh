# Issue 2823: notebook -- safari 3.1 introspection completely broken

Issue created by migration from https://trac.sagemath.org/ticket/2823

Original creator: was

Original creation time: 2008-04-06 06:32:26

Assignee: mabshoff

Introspection (via tab completion), and most other keyboard stuff,
etc., is broken in safari 3.1 because they changed their even handling system.


---

Comment by was created at 2008-04-06 06:32:34

Changing component from Cygwin to notebook.


---

Comment by was created at 2008-04-06 06:32:34

Changing assignee from mabshoff to boothby.


---

Comment by was created at 2008-04-06 07:50:38

This depends on #2818


---

Attachment

Everything seems to work for me, except I can't hit return when doing tab completion to select an item.


---

Comment by robertwb created at 2008-04-06 08:06:15

tab-then-enter is a separate issue--it's never worked and there is another ticket for it. Other than that it's working great.


---

Comment by mabshoff created at 2008-04-06 14:15:06

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 14:15:06

Merged in Sage 3.0.alpha2
