# Issue 3609: Update eclib to eclib-20080310.p5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3609

Original creator: mabshoff

Original creation time: 2008-07-08 11:56:38

Assignee: cremona

A slightly updated spkg is at

http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20080310.p5.spkg

According to John:

```
There's a new version with that file deleted (and the mercurial logs
up to date) in the same place as before, called eclib-20080310.p5.spkg

John
```


John is talking about src/procs/ressol.c which is copyrighted by "Copyright (c) 1994, 1995 by the LiDIA Group". LiDIA is now GPL, but since the file is no longer used it was completely deleted.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-09 16:29:39

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-31 01:50:06

Spkg looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 01:51:49

Merged in Sage 3.1.alpha0


---

Comment by mabshoff created at 2008-07-31 01:51:49

Resolution: fixed
