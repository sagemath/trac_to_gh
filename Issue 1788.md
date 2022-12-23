# Issue 1788: cython annotation in notebook

Issue created by migration from https://trac.sagemath.org/ticket/1788

Original creator: robertwb

Original creation time: 2008-01-15 22:33:28

Assignee: boothby

Cython now has the ability to display, in an html format, the c code corresponding to each line of the cython file. This is useful for getting clean, fast cython code. 


---

Attachment


---

Comment by robertwb created at 2008-01-15 22:34:35

This patch creates an .html file which is linked below next to the .c file.


---

Comment by mhansen created at 2008-01-16 05:18:11

Applies and works correctly for me.


---

Comment by mabshoff created at 2008-01-16 05:18:37

Merged in Sage 2.10.alpha4


---

Comment by mabshoff created at 2008-01-16 05:18:37

Resolution: fixed
