# Issue 3563: sage/misc/cython.py: make "def atlas()" deal with the Accelerate Framework on OSX

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-06 12:04:15

Assignee: mabshoff

The review of #3530 exposed a bug hidden in sage/misc/cython.py: "def atlas()" would not return anything useful on OSX since we need to link against the Accelerate Framework.


---

Comment by mabshoff created at 2008-09-14 11:13:24

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-14 11:13:24

This issue actually breaks Cython on OSX 10.4 since the linker fails after it complains about a missing ATLAS.

Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2008-09-15 12:20:32

Looks good to me, and

```
[05:11am] mabshoff: ok, fixed the tests, passes on OSX and not-OSX: #3563
```



---

Comment by mabshoff created at 2008-09-15 12:22:50

Resolution: fixed


---

Comment by mabshoff created at 2008-09-15 12:22:50

Merged in Sage 3.1.2.rc4
