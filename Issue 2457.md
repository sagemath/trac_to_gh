# Issue 2457: ideal.py doctest failure

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-03-10 14:07:03

Assignee: gfurnish


```
File "ideal.py", line 384:
    sage: I.is_prime()
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError
Got:
    True
```




---

Attachment


---

Comment by gfurnish created at 2008-03-10 14:09:16

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-10 14:09:16

This doctest did not work because 7 is in a PID and thus has an is_prime function.


---

Comment by mabshoff created at 2008-03-10 14:54:32

Patch looks good to me and fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-10 14:55:31

Resolution: fixed


---

Comment by mabshoff created at 2008-03-10 14:55:31

Merged in Sage 2.10.3.rc4
