# Issue 1856: 3d graphics -- bug in setting options via the show command

Issue created by migration from https://trac.sagemath.org/ticket/1856

Original creator: was

Original creation time: 2008-01-19 23:45:50

Assignee: was

Try this:

```
sage: sphere((0,0,0), figsize=2).show(viewer='tachyon', figsize=10)
```

A tiny picture of a sphere appears.  It should be that the second figsize overwrites the first.


---

Comment by was created at 2008-01-19 23:45:55

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2008-01-20 00:08:41

This fixes the problem mentioned above in a simple clean way, adds the ability to globally override the defaults, and adds an unrelated doctest.


---

Attachment


---

Comment by mhansen created at 2008-01-21 03:56:03

The patch I posted applies (after #1854) and passes tests.


---

Comment by mabshoff created at 2008-01-21 04:19:50

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 04:19:50

Merged trac-1856.patch in Sage 2.10.1.alpha. mhansen's patch gave rejects.
