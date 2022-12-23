# Issue 3472: Running sage from a non-existent directory pretends to work

Issue created by migration from https://trac.sagemath.org/ticket/3472

Original creator: craigcitro

Original creation time: 2008-06-19 21:13:49

Assignee: craigcitro

Running sage from a directory that doesn't exist thinks it's working, but really just fails. I'm attaching a new `$SAGE_ROOT/sage` replacement that checks this on startup.


---

Attachment


---

Comment by mabshoff created at 2008-06-27 00:14:12

Positive review to the changes made by Craig. As it turned out `sage -upgrade` does not fix (this is now #3517)

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-27 00:14:23

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-27 00:14:23

Resolution: fixed
