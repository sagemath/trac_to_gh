# Issue 1843: [with patch; needs review] cputime for gp interface

Issue created by migration from https://trac.sagemath.org/ticket/1843

Original creator: was

Original creation time: 2008-01-19 01:14:11

Assignee: was

CC:  malb




---

Attachment


---

Comment by malb created at 2008-01-20 14:27:57

The actual code looks good, but note that 
 * no doctests were added
 * this patch will conflict with #1714 (but that is my fault because I didn't appropriately describe the attached patch in the ticket description)


---

Comment by was created at 2008-01-21 05:50:51

this adds doctests  (apply both patches)


---

Attachment

They both apply and work for me.


---

Comment by mabshoff created at 2008-01-21 05:57:44

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 05:57:44

Merged in Sage 2.10.1.alpha1
