# Issue 2585: [with-patch] padic bugfix - check=False in constructor

Issue created by migration from https://trac.sagemath.org/ticket/2585

Original creator: roed

Original creation time: 2008-03-18 12:06:34

Assignee: roed

Fixes bug in Qp, Zp, etc that causes segmentation faults in the constructor.


---

Attachment


---

Comment by mhansen created at 2008-03-19 01:16:44

I fixed a small bug in the patch (changed p in Zq integer check to q).  Apply 2585.patch.  Otherwise, it looks good to me.


---

Comment by mabshoff created at 2008-03-19 01:23:13

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 01:23:13

Merged in Sage 2.11.alpha0
