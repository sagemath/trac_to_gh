# Issue 3044: phcpack improvements: path tracking

Issue created by migration from https://trac.sagemath.org/ticket/3044

Original creator: mhampton

Original creation time: 2008-04-27 14:10:00

Assignee: jkantor

I (Marshall Hampton) and Alex Jokela have added a number of improvements to the phcpack interface, including solution classification, path-tracking, and some utility functions.  This also includes much better doctesting.


---

Comment by mhampton created at 2008-04-27 14:10:56

Changing keywords from "" to "phcpack, interfaces, optional packages".


---

Attachment


---

Comment by mhampton created at 2008-05-05 16:03:05

Changing assignee from jkantor to somebody.


---

Comment by craigcitro created at 2008-06-15 21:57:37

Changing keywords from "phcpack, interfaces, optional packages" to "phcpack, interfaces, optional packages, editor_cwitty".


---

Attachment


---

Comment by cwitty created at 2008-06-18 02:04:11

Looks good!  Doctests pass with phc installed; the plot looks pretty; and after applying my phcpack-optional.patch, doctests pass without phc installed.


---

Comment by mabshoff created at 2008-06-23 11:28:43

Merged both patches in Sage 3.0.4.alpha0


---

Comment by mabshoff created at 2008-06-23 11:28:43

Resolution: fixed
