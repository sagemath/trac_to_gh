# Issue 3998: [with patch, needs review] doctest the sage0 interface

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-29 21:59:57

Assignee: was




---

Attachment


---

Comment by mabshoff created at 2008-08-29 23:00:35

Resolution: duplicate


---

Comment by mabshoff created at 2008-08-29 23:00:35

This looked very familiar and in fact the patch is already in 3.1.2.alpha2:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run -R < trac_3998.patch\?format\=raw 
patching file sage/interfaces/sage0.py
```

So, this is a dupe of #3983.

Cheers,

Michael
