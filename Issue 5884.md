# Issue 5884: OpenSuse 11/x86-64: doctest failure in groups/perm_gps/permgroup.py

Issue created by migration from https://trac.sagemath.org/ticket/5884

Original creator: mabshoff

Original creation time: 2009-04-24 00:43:57

Assignee: mabshoff

CC:  wdj

This might be a side effect of me screwing up at #5697:

```
sage -t -long "devel/sage/sage/groups/perm_gps/permgroup.py"
********************************************************************
File "/space/wstein/farm/sage-3.4.1/devel/sage/sage/groups/perm_gps/permgroup.py", line 914:
   sage: G.random_element()
Expected:
   (1,2)(4,5)
Got:
   (2,3)(4,5)
********************************************************************
```



---

Comment by mabshoff created at 2009-05-15 14:32:09

Hmm, this seems to be gone, so "invalid" until we find a reproducible test case.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 14:32:09

Resolution: invalid


---

Comment by ddrake created at 2009-10-14 03:04:58

This has cropped up again in 4.1.2.rc2 -- see #7206.
