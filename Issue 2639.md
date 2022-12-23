# Issue 2639: ZZ(QQbar(0)) fails

Issue created by migration from https://trac.sagemath.org/ticket/2639

Original creator: cwitty

Original creation time: 2008-03-21 22:04:39

Assignee: cwitty

Values in QQbar cannot be coerced to integers, as reported here: http://groups.google.com/group/sage-devel/browse_thread/thread/8cf79f359cceef3d/e931afceebf3fe35#


---

Attachment


---

Comment by mabshoff created at 2008-03-22 09:09:07

Patch looks good to me and fixes the issue. It also adds a nice number of doctests. Positive review.


---

Comment by mabshoff created at 2008-03-22 09:11:29

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-22 09:11:29

Resolution: fixed
