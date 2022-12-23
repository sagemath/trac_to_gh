# Issue 2825: notebook -- document js.py some more

Issue created by migration from https://trac.sagemath.org/ticket/2825

Original creator: was

Original creation time: 2008-04-06 07:53:14

Assignee: boothby




---

Comment by was created at 2008-04-06 08:11:15

NOTE: In this patch, I fixed a weird design choice.  Namely, in the list of completion dialog, pressing the up arrow at the very top killed the whole dialog instead of wrapping around.  This is weird because the list wraps around in all other directions except up.  Also, esc gets one out of the dialog, so up arrow isn't needed to do this.  I suspect it was just tricky to implement this as wrap around, so Tom didn't.  But now in this patch it is "fixed".


---

Attachment


---

Comment by mabshoff created at 2008-04-06 14:42:12

Patch looks good to me. One minor spelling issue:

```
 Discard the curretn worksheet and quit the currently
```

I am fixing that in the patch I am applying.

Cheers,

Michaeel


---

Comment by mabshoff created at 2008-04-06 14:43:40

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 14:43:40

Resolution: fixed
