# Issue 5272: [with patch, needs review] extend sage_input to work with RIF, CIF, AA, and QQbar

Issue created by migration from https://trac.sagemath.org/ticket/5272

Original creator: cwitty

Original creation time: 2009-02-14 15:20:25

Assignee: cwitty

The attached patch adds support for intervals and for algebraic numbers to the sage_input system.  I'm going to mark it as Milestone 3.3, but I'm feeling no urgency about it... I'm happy to rebase against 3.4.whatever if it doesn't make it into 3.3.


---

Attachment


---

Comment by mhampton created at 2009-02-14 17:37:06

This appears to work as intended, and passes doctests for me.

In examining the coverage of these files, the additions are well documented and tested, but the remaining coverage of some of them are quite low.  I will file some tickets about that once I check that they don't already exist.

I am giving this a positive review but it wouldn't hurt if someone who uses this code looked at it - I have not used sage_input before.  I don't think that's a reason not to put it in a release candidate though.


---

Comment by mabshoff created at 2009-02-15 07:56:24

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 07:56:24

Resolution: fixed
