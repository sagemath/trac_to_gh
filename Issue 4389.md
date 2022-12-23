# Issue 4389: [with patch, needs review] Sage 3.1.4: optional doctest failure in sage/groups/perm_gps/permgroup.py

Issue created by migration from https://trac.sagemath.org/ticket/4389

Original creator: mabshoff

Original creation time: 2008-10-30 05:35:08

Assignee: mabshoff


```
sage -t -long -optional devel/sage/sage/groups/perm_gps/permgroup.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/permgroup.py", line 179:
    sage: H.gens()                            # requires optional database_gap
Expected:
    ((1,2,3,4), (1,3))
Got:
    [(1,2,3,4), (1,3)]
**********************************************************************
```

The above is caused by changing the printing of permutations that went into Sage a while ago. The fix is obvious.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-10-30 05:47:50

+1


---

Comment by ddrake created at 2008-10-30 05:50:34

+1 here too


---

Comment by mabshoff created at 2008-10-30 05:50:56

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-30 05:50:56

Resolution: fixed
