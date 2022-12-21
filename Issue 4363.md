# Issue 4363: Do not automatically evaluate interact cells in notebook

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-10-24 15:15:48

Assignee: boothby

Current behavior is that `@`interact cells automatically evaluate upon opening a worksheet.  This can cause problems if (for instance) the cell depends on other cells which are not automatically evaluated, and also can take a long time if there are lots of them.  

Since other cells do not auto-evaluate, and since this functionality still is easily available by putting #auto in the cell, this ticket calls for the current behavior to be changed.



---

Comment by jason created at 2008-10-24 21:30:25

I second that this should be changed.


---

Comment by mhansen created at 2008-11-13 23:25:25

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-13 23:25:25

I've also added this as a test case to the notebook test suite.


---

Comment by mhansen created at 2008-11-13 23:25:25

Changing assignee from boothby to mhansen.


---

Comment by was created at 2008-11-14 00:13:01

I think to solve this trac ticket, it is necessary that:

 1. Output of interact cells should be completely empty when a worksheet is open.

 2. `@`interact needs to work with #auto (or %auto?) because I have a project with a student that involves making a bunch of interacts that are all %hideall'd, so one sees *only* the controls.


---

Comment by was created at 2008-11-14 00:13:54

Just to emphasize, the patch above mysteriously doesn't work with #auto...


---

Attachment


---

Comment by mhansen created at 2009-01-19 04:19:24

I've posted a patch which does not enqueue interact cells at startup and deletes their output so that users don't think that they're running.

I've also made a ticket to fix the auto-evaluation at http://trac.sagemath.org/sage_trac/ticket/5020 .  I think this is a separate issue, and I'm looking into it.


---

Comment by mhampton created at 2009-01-19 05:01:06

This seems to solve the problem, and the auto-launch problem of #4947.  My setup seems to have some issues with #auto cells, so I can't test the compatibility of this patch with that, but that is addressed in other ways by #5020.


---

Comment by mhampton created at 2009-01-19 05:01:06

Changing priority from minor to major.


---

Comment by mabshoff created at 2009-01-19 06:10:52

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 06:10:52

Merged in Sage 3.3.alpha0
