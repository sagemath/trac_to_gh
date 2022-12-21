# Issue 2878: notebook -- cython .c and .html links should open in new links (use target="_new"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-11 16:01:48

Assignee: boothby

Do this, because otherwise user (1) clicks html or c link, then (2) sees the html or c, then (3) presses browser back button, then (4) PANICS! since all their work is gone (actually they can get it back by pressing refresh).  This is VERY confusing, and I've had users ask about it multiple times recently. 

Alternatively, is there a way so that when a user navigates to a worksheet page via the back button, the page is automatically refreshed.


---

Attachment


---

Comment by boothby created at 2008-04-12 06:53:41

"Alternatively, is there a way so that when a user navigates to a worksheet page via the back button, the page is automatically refreshed?"

This is a hard problem.  Let's think about making a new ticket out of that issue (because the problem is ultimately larger than these links), and take this patch for now.


---

Comment by mabshoff created at 2008-04-12 10:49:19

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 10:49:19

Resolution: fixed
