# Issue 4447: graph attributes (_boundary, _pos, etc.) are not updated properly

Issue created by migration from https://trac.sagemath.org/ticket/4447

Original creator: jason

Original creation time: 2008-11-05 19:09:05

Assignee: rlm

The attached patch fixes a number of small issues with updating graph attributes.


---

Attachment

all tests in graphs/*.py and graphs/*.pyx pass.


---

Comment by rlm created at 2008-11-13 16:01:48

This is good code. I don't have time to run tests, but as long as they pass this should definitely be merged.


---

Comment by mabshoff created at 2008-11-13 18:42:46

Resolution: fixed


---

Comment by mabshoff created at 2008-11-13 18:42:46

Merged in Sage 3.2.rc1 - doctests do pass.

Cheers,

Michael
