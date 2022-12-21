# Issue 4279: Sage 3.1.3.rc0: numerical noise in rings/real_lazy.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-14 09:42:43

Assignee: mabshoff


```
sage -t  devel/sage/sage/rings/real_lazy.pyx 
********************************************************************** 
File "/Users/mh/Desktop/sage-3.1.3.rc0/tmp/real_lazy.py", line 549: 
    sage: complex(CLF(-1)^(1/4)) 
Expected: 
    (0.70710678118654757+0.70710678118654746j) 
Got: 
    (0.70710678118654746+0.70710678118654757j) 
*********************************************************************
```



---

Comment by mabshoff created at 2008-10-14 09:42:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-14 11:18:55

On a G5 with 10.4 I am seeing the following issue:

```
sage -t -long devel/sage/sage/rings/real_lazy.pyx           
**********************************************************************
File "/Users/mabshoff/sage-3.1.3.rc0/tmp/real_lazy.py", line 549:
    sage: complex(CLF(-1)^(1/4))
Expected:
    (0.70710678118654757+0.70710678118654746j)
Got:
    (0.70710678118654746+0.70710678118654757j)
**********************************************************************
```



---

Attachment


---

Comment by mhansen created at 2008-10-14 11:58:15

Looks good to me.


---

Comment by mabshoff created at 2008-10-14 12:25:43

Merged in 3.1.3.final


---

Comment by mabshoff created at 2008-10-14 12:25:43

Resolution: fixed
