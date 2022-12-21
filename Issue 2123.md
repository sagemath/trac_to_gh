# Issue 2123: bug in modular symbols setting sign on subspace

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-09 03:59:11

Assignee: craigcitro

This is wrong:


```
sage: A = ModularSymbols(1,80,0,base_ring=GF(37))

sage: A.plus_submodule().cuspidal_submodule().sign()
 0

```


I'll fix it at some point soon.


---

Comment by craigcitro created at 2008-02-12 07:26:28

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-02-12 07:26:28

... and it's fixed.


---

Attachment


---

Comment by was created at 2008-02-12 07:29:09

looks good!


---

Comment by mabshoff created at 2008-02-13 07:59:27

Resolution: fixed


---

Comment by mabshoff created at 2008-02-13 07:59:27

Merged in Sage 2.10.2.alpha0
