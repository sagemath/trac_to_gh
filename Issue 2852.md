# Issue 2852: ctrl-enter broken in firefox/linux

Issue created by migration from https://trac.sagemath.org/ticket/2852

Original creator: boothby

Original creation time: 2008-04-08 05:35:26

Assignee: boothby




---

Attachment

The attached should be approached with distrust.  It makes a very low-level change to how key events are handled.  Test all keycodes in all browsers before and after applying this patch.


---

Comment by was created at 2008-04-08 13:27:32

It looks good to me.  I'm going to test the heck out of the notebook before 3.0 is released anyways, so I say we apply this. 

NOTE: I updated a comment that should be updated because of this patch, but that will go in a subsequent "fix of a few small bugs" notebook patch I'll post shortly.


---

Comment by mabshoff created at 2008-04-08 15:33:45

Resolution: fixed


---

Comment by mabshoff created at 2008-04-08 15:33:45

Merged in Sage 3.0.alpha3
