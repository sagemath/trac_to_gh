# Issue 4598: add sage/libs/gmp/__init__.py to MANIFEST.in

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-23 21:20:17

Assignee: mabshoff

This causes build failures of the Sage library in Sage 3.2.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 21:20:24

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-25 11:11:55

Without the patch:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha0$ hg status
! sage/libs/gmp/__init__.py
```

With the patch applied:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha00$ hg stat
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha00$ 
```



---

Attachment


---

Comment by certik created at 2008-11-25 13:44:09

Looks good to me. Thanks!


---

Comment by mabshoff created at 2008-11-25 13:46:13

Merged in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-25 13:46:13

Resolution: fixed
