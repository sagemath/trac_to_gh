# Issue 3823: Interact - get rid of default height

Issue created by migration from https://trac.sagemath.org/ticket/3823

Original creator: itolkov

Original creation time: 2008-08-12 20:38:42

Assignee: itolkov

Interactions have a minimum height of 400px, which consumes space when only part of it is used.


---

Attachment

I changed the default height to 20px, since it's probably good to have one.


---

Comment by mabshoff created at 2008-08-13 06:46:16

Changing component from notebook to interact.


---

Comment by jason created at 2008-08-27 14:05:58

Looks good to me.  Positive review.


---

Comment by mabshoff created at 2008-08-27 21:39:47

This does not apply cleanly any more, but should be trivial to rebase:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/devel/sage$ patch -p1 < trac_3823_sage.patch 
patching file sage/server/notebook/interact.py
Hunk #1 FAILED at 1397.
1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej
```


Igor: In the future please name the patches you post trac_XXXX_description.patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-29 00:58:22

Resolution: fixed


---

Attachment

Merged trac_3823_sage.patch in Sage 3.1.2.alpha2
