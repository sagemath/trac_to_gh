# Issue 5351: Sage 3.3 broke the update of  easy-install.pth

Issue created by migration from https://trac.sagemath.org/ticket/5351

Original creator: mabshoff

Original creation time: 2009-02-23 19:06:18

Assignee: mabshoff

When unpacking a Sage 3.3 binary the update of easy-install.pth is broken:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at
most a few minutes)...
Do not interrupt this.
Warning: something went wrong updating the easy-install.pth file.
```



---

Comment by mabshoff created at 2009-03-01 05:52:33

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-03-02 05:05:12

Looks good to me.


---

Comment by mabshoff created at 2009-03-02 05:24:29

Resolution: fixed


---

Comment by mabshoff created at 2009-03-02 05:24:29

Merged in Sage 3.4.rc0.

Cheers,

Michael
