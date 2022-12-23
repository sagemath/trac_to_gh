# Issue 2939: piecewise.py improvements (docstring and laplace fixes)

Issue created by migration from https://trac.sagemath.org/ticket/2939

Original creator: wdj

Original creation time: 2008-04-16 02:24:18

Assignee: was

Jim Morrow reported by private email some nonsense in the docstrings of several piecewise.py functions. These are now fixed. Also, I added 2 lines to the laplace function which allows it to compute with functions which are defined over an infinite interval. These 2 lines were the only code changes in this patch, the rest of the changes are docstring fixes and additions.


---

Attachment


---

Comment by AlexGhitza created at 2008-04-24 03:34:24

Looks good.


---

Comment by mabshoff created at 2008-04-24 03:42:16

Merged in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-24 03:42:16

Resolution: fixed
