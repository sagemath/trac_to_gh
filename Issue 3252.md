# Issue 3252: add kbase functionality to libsingular

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-05-18 03:35:33

Assignee: was

implemented a cython wrapper for singular's kbase command. This is significantly faster than doing singular.kbase() because it doesn't have the pexpect overhead. 


---

Attachment


---

Comment by malb created at 2008-05-18 14:35:40

The patch looks good, applies cleanly and does as advertised. However, two new functions are introduced without doctests. Though they are only wrappers every new function must have a doctest these days.


---

Attachment

add doctests as requested by reviewer


---

Comment by yi created at 2008-05-18 15:13:13

Attached a patch which doctests the 2 functions mentioned. Apply after the first patch.


---

Comment by malb created at 2008-05-18 15:29:17

Great! and even greater: We know have a new libSingular developer :-)


---

Comment by mabshoff created at 2008-05-18 16:18:01

Resolution: fixed


---

Comment by mabshoff created at 2008-05-18 16:18:01

Merged both patches in Sage 3.0.2.alpha1
