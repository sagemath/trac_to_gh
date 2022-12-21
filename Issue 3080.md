# Issue 3080: testdoc.py hangs

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-05-02 13:26:09

Assignee: yi


```
sage -t devel/sage/sage/dsage/tests/testdoc.py
```

never finishes for me (even after 1hr +).  I have to Ctrl-C my doctests to get them to finish.  


---

Comment by gfurnish created at 2008-05-02 13:31:25

This is using 3.0.1.alpha1.  It happens about 75% of the time with both parallel and non-parallel testers using gcc-4.2.3 on gentoo.  The cpu utilization is near zero while this is happening.


---

Comment by mabshoff created at 2008-05-03 17:06:16

#3097 is the real issue here. Sorry I forgot to update this ticket, but I am closing this as a dupe.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 17:06:16

Resolution: duplicate
