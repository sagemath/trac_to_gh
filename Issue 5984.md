# Issue 5984: cmp related doctest failure in sage/modular/arithgroup/arithgroup_perm.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-05-05 04:33:53

Assignee: mabshoff


```
sage -t -long devel/sage/sage/modular/arithgroup/arithgroup_perm.py
**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage-main/sage/modular/arithgroup/arithgroup_perm.py", line 204:
    sage: cmp(G, Gamma0(8))
Expected:
    1
Got:
    -1
**********************************************************************
```



---

Comment by mabshoff created at 2009-05-05 04:34:19

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-05 04:34:19

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-05-05 05:38:51

Resolution: fixed


---

Comment by mabshoff created at 2009-05-05 05:38:51

Merged in Sage 3.4.2.

Cheers,

Michael
