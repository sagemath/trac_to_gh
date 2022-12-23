# Issue 4528: [with patch, needs review] Implement Krull dimension for orders in number fields

Issue created by migration from https://trac.sagemath.org/ticket/4528

Original creator: cremona

Original creation time: 2008-11-15 16:56:35

Assignee: was

Keywords: number fields, orders

This is a triviality, but I noticed it while doing something else. All order in number fields have Krull dimension 1, but this was not implemented -- not even for the maximal order.  Now it is.

Patch based on 3.2.rc1, touches rings/ring.pyx and rings/number_field/order.py



---

Attachment


---

Comment by craigcitro created at 2008-11-21 10:19:58

This looks good.

As a really trivial issue, someone should add a `.` at the end of line 754 of `ring.pyx`. It didn't seem worth another patch.


---

Comment by mabshoff created at 2008-11-21 11:26:11

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 11:26:11

Merged in Sage 3.2.1.alpha0
